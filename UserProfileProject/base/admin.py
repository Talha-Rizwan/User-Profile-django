"""Register models here to see them on admin panel."""
from django.contrib import admin

from .models import User

admin.site.register(User)
