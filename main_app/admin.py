from django.contrib import admin
from .models import Dancer, Choreo, Team, Playlist

# Register your models here.
admin.site.register(Dancer)
admin.site.register(Choreo)
admin.site.register(Team)
admin.site.register(Playlist)