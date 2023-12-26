# # from django.db import models
# # from django.contrib.auth.models import AbstractUser

# # class CustomUser(AbstractUser):
# #     # Add any additional fields you need

# #     # Add related_name to avoid clashes with auth.User model
# #     groups = models.ManyToManyField(
# #         'auth.Group',
# #         related_name='customuser_set',
# #         related_query_name='user',
# #         blank=True,
# #         help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
# #     )
# #     user_permissions = models.ManyToManyField(
# #         'auth.Permission',
# #         related_name='customuser_set',
# #         related_query_name='user',
# #         blank=True,
# #         help_text='Specific permissions for this user.',
# #     )
# from django.db import models

# class  CustomUser(models.Model):
#     username = models.CharField(max_length=255)
#     password = models.CharField(max_length=255)
from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # Add any additional fields you need

    # Add related_name to avoid clashes with auth.User model
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',
        related_query_name='user',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',
        related_query_name='user',
        blank=True,
        help_text='Specific permissions for this user.',
    )