from django.contrib import admin
from .models import Person


class CertificateAdmin(admin.ModelAdmin):
    list_display = ['w_name']
    search_fields = ["w_name",]


admin.site.register(Person, admin_class=CertificateAdmin)


