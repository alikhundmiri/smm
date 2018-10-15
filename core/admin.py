from django.contrib import admin

from .models import interested

class InterestedAdmin(admin.ModelAdmin):
	list_display = ['email_address', 'interested_in',]
	list_filter = ['email_address', 'interested_in']
	search_fields = ['email_address', 'interested_in']
	list_editable = ['interested_in',]
	
	class Meta:
		model = interested

admin.site.register(interested, InterestedAdmin)