from django.contrib import admin
from .models import Grade4blogpost
from .models import Grade3blogpost
from .models import Grade2blogpost

# add the models to the database
admin.site.register(Grade4blogpost)
admin.site.register(Grade3blogpost)
admin.site.register(Grade2blogpost)
