from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _

from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):

    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given email and password.
        """
        if not email:
            raise ValueError(_("The Email must be set"))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("email address"), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    SELECCION_GENERO = (
            ('Hombre', 'Hombre'),
            ('Mujer', 'Mujer'),
            ('Otro', 'Otro'),
            )
    genero = models.CharField(
        max_length=9,
        choices=SELECCION_GENERO,
        default='HOMBRE',
        null=True, blank=True)
    profile_picture = models.CharField(max_length=350, null=True, blank=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

# class CustomUserManager(BaseUserManager):
#     """
#     Custom user model manager where email is the unique identifiers
#     for authentication instead of usernames.
#     """
#     def create_user(self, email, password, **extra_fields):
#         """
#         Create and save a user with the given email and password.
#         """
#         if not email:
#             raise ValueError(_("The Email must be set"))
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save()
#         return user
#    
#     def create_superuser(self, email, password, **extra_fields):
#         """
#         Create and save a SuperUser with the given email and password.
#         """
#         extra_fields.setdefault("is_staff", True)
#         extra_fields.setdefault("is_superuser", True)
#         extra_fields.setdefault("is_active", True)
#    
#         if extra_fields.get("is_staff") is not True:
#             raise ValueError(_("Superuser must have is_staff=True."))
#         if extra_fields.get("is_superuser") is not True:
#             raise ValueError(_("Superuser must have is_superuser=True."))
#         return self.create_user(email, password, **extra_fields)
#
#

# class CustomUser(AbstractBaseUser, PermissionsMixin):
#     email = models.EmailField(_("correo electronico"), unique=True)
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     edad = models.IntegerField(null=True, blank=True)
#     is_staff = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=True)
#     date_joined = models.DateTimeField(default=timezone.now)
#     SELECCION_GENERO = (
#             ('Hombre', 'Hombre'),
#             ('Mujer', 'Mujer'),
#             ('Otro', 'Otro'),
#             )
#     genero = models.CharField(
#         max_length=9,
#         choices=SELECCION_GENERO,
#         default='HOMBRE',
#         null=True, blank=True)
#     profile_picture = models.CharField(max_length=350, null=True, blank=True)
#     USERNAME_FIELD = "email"
#     REQUIRED_FIELDS = []
#     def __str__(self):
#         return self.email
#








# Create your models here.
#class Usuario(models.Model):
#    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#    edad = models.IntegerField(null=True, blank=True)
#    SELECCION_GENERO = (
#            ('Hombre', 'Hombre'),
#            ('Mujer', 'Mujer'),
#            ('Otro', 'Otro'),
#            )
#    genero = models.CharField(
#        max_length=9,
#        choices=SELECCION_GENERO,
#        default='HOMBRE',
#        null=True, blank=True)
#   # profile_picture = models.CharField(max_length=350, null=True, blank=True)
#   # mis_actividades = models.ManyToManyField(Actividades)
#    def __str__(self):
#        return self.user.first_name + " " +  self.user.last_name
#
#class Friends(models.Model):
#    users = models.ManyToManyField(Usuario)
#    current_user=models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='owner')
#
#    @classmethod
#    def make_friend(cls, current_user, new_friend):
#        friend, created = cls.objects.get_or_create(
#            current_user = current_user
#        )
#        friend.users.add(new_friend)
#
#    @classmethod
#    def remove_friend(cls, current_user, new_friend):
#        friend, created = cls.objects.get_or_create(
#            current_user = current_user
#        )
#        friend.users.remove(new_friend)
#
#    def __str__(self):
#        return str(self.current_user)
#
#@login_required
#def add_or_remove_friends(request, username, verb):
#    n_f = get_object_or_404(User, username=username)
#    owner = request.user.userprofile
#    new_friend = UserProfile.objects.get(user=n_f)
#
#    if verb == "add":
#        new_friend.followers.add(owner)
#        Friend.make_friend(owner, new_friend)
#    else:
#        new_friend.followers.remove(owner)
#        Friend.remove_friend(owner, new_friend)
#
#    return redirect(new_friend.get_absolute_url())
