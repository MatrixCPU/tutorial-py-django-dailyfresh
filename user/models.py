from django.db import models
from django.utils import timezone
from .utils import generate_password_hash


class User(models.Model):
    username = models.CharField(max_length=20)
    password_hash = models.CharField(max_length=128)
    email = models.CharField(max_length=30)
    reg_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return "User: %s" % self.username

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute!')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return self.password_hash == generate_password_hash(password)


class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=6)
    phone = models.CharField(max_length=11)

    def __str__(self):
        return "%s, %s" % (self.user.username, self.phone)
