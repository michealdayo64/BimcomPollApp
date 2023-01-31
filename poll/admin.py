from django.contrib import admin
from .models import State, Lga, Ward, PollingUnit, Party, AnnouncedPuResults, AnnouncedLgaResults
# Register your models here.

admin.site.register([State, Lga, Ward, PollingUnit, Party, AnnouncedPuResults, AnnouncedLgaResults])
