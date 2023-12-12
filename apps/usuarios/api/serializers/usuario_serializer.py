from rest_framework import serializers
from apps.usuarios.models import Usuario
from apps.usuarios.models import Roles
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('username', 'email', 'name', 'last_name')

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'username': instance.username,
            'password': instance.password,
            'email': instance.email,
            'rol': instance.roles_id.nombre_rol if instance.roles_id is not None else '',
            'nombre_usuario': instance.name,
            'apellido_usuario':instance.last_name,
            'direccion_usuario': instance.direccion,
            'telefono_usuario':instance.telefono,
            'tipo_documento': instance.tipo_documento,
            'documento_identidad': instance.documento,
        }

class UsuarioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Usuario
        exclude = (
            'state', 'is_staff', 'is_active', 'is_superuser', 'roles_id', 'created_at', 'modified_at', 'deleted_at',
            'groups', 'last_login', 'user_permissions')

    def create(self, validated_data):
        # Obtener el rol 'cliente'
        cliente_role = Roles.objects.get(nombre_rol='cliente')

        # Crear el usuario con el rol cliente asignado
        usuario = Usuario.objects.create(**validated_data, roles_id=cliente_role)

        # Establecer la contraseña del usuario si se proporcionó
        password = validated_data.get('password')
        if password:
            usuario.set_password(password)
            usuario.save()

        return usuario

    def update(self, instance, validated_data):
        # Verificar si el usuario tiene el rol 'local'
        tiene_rol_local = instance.roles_id.nombre_rol == 'local' if instance.roles_id else False

        if not tiene_rol_local:
            # Obtener el rol 'cliente'
            cliente_role = Roles.objects.get(nombre_rol='cliente')

            # Si no tiene un rol o tiene un rol diferente de 'local', se asigna el rol cliente
            validated_data['roles_id'] = cliente_role

        # Actualizar el usuario
        update_usuario = super().update(instance, validated_data)

        # Actualizar la contraseña si se proporciona
        if 'password' in validated_data:
            update_usuario.set_password(validated_data['password'])
            update_usuario.save()

        return update_usuario
    def to_representation(self, instance):
        return {
            'id': instance.id,
            'username': instance.username,
            'password': instance.password,
            'email': instance.email,
            'rol': instance.roles_id.nombre_rol if instance.roles_id is not None else '',
            'nombre_usuario': instance.name,
            'apellido_usuario':instance.last_name,
            'direccion_usuario': instance.direccion,
            'telefono_usuario':instance.telefono,
            'tipo_documento': instance.tipo_documento,
            'documento_identidad': instance.documento,
        }

class PasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=128, min_length=6, write_only=True)
    password2 = serializers.CharField(max_length=128, min_length=6, write_only=True)

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError(
                {'password':'Debe ingresar ambas contraseñas iguales'}
            )
        return data


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    pass

class CustomSerializerLogout(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('')

