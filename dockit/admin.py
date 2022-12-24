from django.contrib import admin
from .models import User, IP, Host, Image, Container
# Register your models here.
admin.site.register(User)
admin.site.register(IP)
admin.site.register(Host)
admin.site.register(Image)
admin.site.register(Container)