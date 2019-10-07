from django.contrib import admin

from .models import CandidateRegistrationForm


class CandidateRegistrationAdmin(admin.ModelAdmin):
    fieldsets = [
        ("First name", {'fields':['first_name']}),
        ("Last name", {'fields':['last_name']}),
    ]
    list_display = ('first_name', 'last_name')
    list_filter = ['first_name', 'last_name']
    search_fields = ['first_name', 'last_name']

#Tell the admin that CandidateRegistrationForm objects have an admin interface
admin.Site.register(CandidateRegistrationForm, CandidateRegistrationAdmin)
