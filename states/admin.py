from django.contrib import admin

# Register your models here.
from .models import Side
admin.site.register(Side)

from .models import State
admin.site.register(State)

from .models import Comment
admin.site.register(Comment)