from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password

class UserManager(BaseUserManager):
    def create_user(self, username, password=None):
        if not username:
            raise ValueError('Nombre de Usuario Obligatorio!')
        user = self.model(username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user
    

class Usuario(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(primary_key=True, max_length = 20, unique=True)
    password = models.CharField('Password', max_length= 256)
    perfil = models.CharField('Perfil', max_length = 50)
    nombre = models.CharField('Nombre', max_length = 50)
    apellido = models.CharField('Apellido', max_length = 50)
    celular = models.CharField('Celular', max_length = 13)
    genero = models.CharField('Genero', max_length = 1)

    def save(self, **kwargs):
        some_salt = 'mMUj0DrIK6vgtdIYepkIxN'
        self.password = make_password(self.password, some_salt)
        super().save(**kwargs)
    objects = UserManager()
    USERNAME_FIELD = 'username' 
    