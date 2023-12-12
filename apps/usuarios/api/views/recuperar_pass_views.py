from rest_framework.response import Response
from rest_framework import status, viewsets
from django.core.mail import send_mail, BadHeaderError
from apps.usuarios.api.serializers.recuperar_pass_serializer import RecuperarPassSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from apps.usuarios.models import Usuario

class RecuperarPassViewSet(viewsets.ViewSet):
    serializer_class = RecuperarPassSerializer

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']

            try:
                user = Usuario.objects.get(email=email)
            except Usuario.DoesNotExist:
                return Response({'message': 'El correo electrónico proporcionado no está registrado.'},
                                status=status.HTTP_400_BAD_REQUEST)

            refresh = RefreshToken.for_user(user)
            refresh['blacklist_after_use'] = True  # Invalidar token después del primer uso
            token = str(refresh.access_token)

            reset_link = f'http://127.0.0.1:8000/usuarios/recuperar_pass/?token={token}'

            message = f"""  
            Esta dirección de correo electrónico está en el archivo para recuperar su cuenta de Shoes Company. Si inició este proceso de recuperación de cuenta, diríjase al link que aparece a continuación para recuperar su cuenta HP.

            {reset_link}

            Si no inició este proceso de recuperación de cuenta y tiene una cuenta Shoes Company registrada con esta dirección de correo electrónico, alguien podría estar tratando de acceder a su cuenta. No envíe de ninguna forma este link a ninguna otra persona.
            """

            try:
                send_mail(
                    'Recuperación de Contraseña',
                    message,
                    'shoes.company246@gmail.com',  # Reemplaza con tu dirección de correo
                    [email],
                    fail_silently=False,
                )
            except BadHeaderError:
                return Response({'message': 'Encabezado inválido. Inténtelo de nuevo.'}, status=status.HTTP_400_BAD_REQUEST)
            except Exception as e:
                return Response({'message': f'Error al enviar el correo electrónico: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            return Response({'message': 'Correo electrónico de recuperación de contraseña enviado.'}, status=status.HTTP_200_OK)

        return Response({'message': '', 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
