from rest_framework.authentication import get_authorization_header
from apps.usuarios.authentication import ExpiracionTokenAuthentication
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
class Authenticacion(object):

    def get_user(self, request):
        token = get_authorization_header(request).split()
        if token:
            try:
                token = token[1].decode()
            except:
                return None
            token_expire = ExpiracionTokenAuthentication()
            user, token, message = token_expire.authenticate_credentials(token)
            if user != None and token != None:
                return user
            return message
        return None
    def dispatch(self, request, *args, **kwargs):
        user = self.get_user(request)
        #found token in request
        if user  is not None:
            if type(user) == str:
                response = Response({'error':user})
                response.accepted_renderer = JSONRenderer()
                response.accepted_media_type = 'application/json'
                response.renderer_context = {}
                return response
            return super().dispatch(request, *args, **kwargs)
        response = Response({'error':'No se han enviado las credenciales'})
        response.accepted_renderer = JSONRenderer()
        response.accepted_media_type = 'application/json'
        response.renderer_context = {}
        return response