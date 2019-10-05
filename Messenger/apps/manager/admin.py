from django.contrib import admin
#import all models
from .models import *

# Register your models here.
admin.site.register(category)
admin.site.register(author)
admin.site.register(post)
admin.site.register(web)
admin.site.register(social)
admin.site.register(contact)
admin.site.register(suscriber)

