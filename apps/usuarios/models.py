from django.db import models
from django.contrib.auth.models import Group, Permission  # Agrega esta línea al inicio de tu archivo models.py
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from simple_history.models import HistoricalRecords
from apps.base.models import BaseModel


# Create your models here.

class UserManager(BaseUserManager):
    def _create_user(self, username, email, name, last_name, password, is_staff, is_superuser, **extra_fields):
        user = self.model(
            username=username,
            email=email,
            name=name,
            last_name=last_name,
            is_staff=is_staff,
            is_superuser=is_superuser,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, username, email, name, last_name, password=None, **extra_fields):
        return self._create_user(username, email, name, last_name, password, False, False, **extra_fields)

    def create_superuser(self, username, email, name, last_name, password=None, **extra_fields):
        return self._create_user(username, email, name, last_name, password, True, True, **extra_fields)

class Roles(BaseModel):
    id = models.AutoField(primary_key=True)
    nombre_rol = models.CharField('Nombre rol', max_length=30, blank=True, null=True)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    def __str__(self):
        return self.nombre_rol if self.nombre_rol else 'Sin nombre de rol'

class Usuario(AbstractBaseUser, PermissionsMixin, BaseModel):
    username = models.CharField(max_length=255, unique=True)
    name = models.CharField('Nombres', max_length=255, blank=True, null=True)
    last_name = models.CharField('Apellidos', max_length=255, blank=True, null=True)
    email = models.EmailField('Correo Electrónico', max_length=255, unique=True)
    direccion = models.CharField('Direccion usuario', max_length=50, blank=False, null=False, default='')
    telefono = models.CharField('Telefono usuario', max_length=10, blank=False, null=False, default='')
    tipo_documento = models.CharField('Tipo de documento', max_length=5, blank=False, null=False, default='')
    documento = models.PositiveSmallIntegerField(default=0)
    roles_id = models.ForeignKey(Roles, on_delete=models.CASCADE, verbose_name='Rol de usuario', null=True)
    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to.',
        related_name='usuarios_groups',  # Related name personalizado para groups
        related_query_name='user',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='usuarios_permissions',  # Related name personalizado para user_permissions
        related_query_name='user',
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    historical = HistoricalRecords()
    objects = UserManager()

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'name', 'last_name']

    def __str__(self):
        return f'{self.name} {self.last_name}'


class LocalUsuario(BaseModel):
    id = models.AutoField(primary_key=True)
    nombre_local = models.CharField('Nombre local', max_length=40, blank=False, null=False)
    direccion_local = models.CharField('Direccion local', max_length=50, blank=False, null=False)
    telefono_local = models.CharField('Telefono local', max_length=10, blank=False, null=False)
    nit_local = models.CharField('Nit local', max_length=9, blank=False, null=False)
    image = models.ImageField('Imagen de local', upload_to='locales/', max_length=255, null=True, blank=True)
    usuario_id = models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name='Usuario', null=True)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    def __str__(self):
        return self.nombre_local

    class Meta:
        verbose_name = 'Datos de local'
        verbose_name_plural = 'Datos de locales'



