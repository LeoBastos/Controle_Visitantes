from django import db
from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser,PermissionsMixin


class UsuarioManager(BaseUserManager):
    def create_user(self, email, password=None):
        usuario = self.model(
            email = self.normalize_email(email)
        )
        usuario.is_active = True
        usuario.is_staff = False
        usuario.is_superuser = False

        if password:
            usuario.set_password(password)

        usuario.save()

        return usuario

    def create_superuser(self, email, password):
        usuario = self.create_user(
            email = self.normalize_email(email),
            password = password,
        )

        usuario.is_active = True
        usuario.is_staff = True
        usuario.is_superuser = True

        usuario.set_password(password)

        usuario.save()

        return usuario
    


class Usuario(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=100,unique=True,verbose_name='E-mail do Usuário')
    is_active = models.BooleanField(default=True ,verbose_name='Usuário esta Ativo')
    is_staff = models.BooleanField(default=False ,verbose_name='Usuário e da equipe de Desenvolvimento')
    is_superuser = models.BooleanField(default=False ,verbose_name='Usuário e um SuperUsuario')

    USERNAME_FIELD = 'email'
    
    objects = UsuarioManager()

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
        db_table = 'usuario'

    def __str__(self):
        return self.email

