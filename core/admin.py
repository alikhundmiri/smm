from django.contrib import admin

from .models import interested, clientele, assignment

class InterestedAdmin(admin.ModelAdmin):
	list_display = ['email_address', 'interested_in',]
	list_filter = ['email_address', 'interested_in']
	search_fields = ['email_address', 'interested_in']
	list_editable = ['interested_in',]
	
	class Meta:
		model = interested

class ClienteleAdmin(admin.ModelAdmin):
	list_display = ['client', 'business_url','business_type']
	list_filter = ['client', 'business_url','business_type']
	search_fields = ['client', 'business_url','business_type']
	list_editable = ['business_url']
	
	class Meta:
		model = clientele

class AssignmentAdmin(admin.ModelAdmin):
	list_display = ['user', 'client', 'content_url', 'due_date', 'status']
	list_filter = ['user', 'client', 'content_url', 'due_date', 'status']
	search_fields = ['user', 'client', 'content_url', 'due_date', 'status']
	list_editable = ['status',]
	
	class Meta:
		model = assignment


admin.site.register(interested, InterestedAdmin)
admin.site.register(clientele, ClienteleAdmin)
admin.site.register(assignment, AssignmentAdmin)