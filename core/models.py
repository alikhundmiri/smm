from django.conf import settings
from django.db import models
from django.utils import timezone
from datetime import timedelta
def return_date_time():
		now = timezone.now()
		return now + timedelta(days=3)

# Create your models here.
class interested(models.Model):
	TYPE_LIST = (
		('Blogger', 'blogger'),
		('Youtuber', 'youtuber'),
		('Local Business', 'local_business'),
		('Other', 'other'),
		)
	
	email_address 			=			models.EmailField(max_length=254, blank=False, null=False)

	interested_in			=			models.CharField(max_length=20, choices=TYPE_LIST, default=TYPE_LIST[0][0])

	timestamp				=			models.DateTimeField(auto_now=False, auto_now_add=True)
	updated					=			models.DateTimeField(auto_now=True, auto_now_add=False)

	def __str__(self):
		return(self.email_address)

	class Meta:
		ordering	 		=			["-timestamp", "-updated"]
		verbose_name 		= 			"Interested Person"
		verbose_name_plural = 			"Interested People"

class clientele(models.Model):
	CLIENT_LIST = (
		('Blog', 'blog'),
		('Youtube', 'youtube'),
		('Local Business', 'local_business'),
		('Other', 'other'),
		)

	client					=			models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
	business_url			=			models.URLField()
	business_type			=			models.CharField(max_length=20, choices=CLIENT_LIST, default=CLIENT_LIST[0][0])
	timestamp				=			models.DateTimeField(auto_now=False, auto_now_add=True)
	updated					=			models.DateTimeField(auto_now=True, auto_now_add=False)

	def __str__(self):
		return(self.business_type + " by " + str(self.client))

	class Meta:
		ordering	 		=			["-timestamp", "-updated"]
		verbose_name 		= 			"Client"
		verbose_name_plural = 			"clientele"

class assignment(models.Model):
	ASSIGNMENT_STATUS = (
		('InReview', 'inreview'),
		('Error', 'error'),
		('Working', 'working'),
		('Completed', 'completed'),
		('Rejected', 'rejected'),
		)

	# Add a new field for user. replace it with client.
	# and for client, connect with with clientele

	user					=			models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
	client 					=			models.ForeignKey('clientele', related_name='assignments', on_delete=models.CASCADE, default=1)

	content_url				=			models.URLField()
	due_date				=			models.DateTimeField(default=return_date_time)
	status					=			models.CharField(max_length=20, choices=ASSIGNMENT_STATUS, default=ASSIGNMENT_STATUS[0][0])

	timestamp				=			models.DateTimeField(auto_now=False, auto_now_add=True)
	updated					=			models.DateTimeField(auto_now=True, auto_now_add=False)

	def __str__(self):
		return( str(self.user) +" "+ str(self.client) +" "+ self.status)


	class Meta:
		ordering	 		=			["-timestamp", "-updated"]
		verbose_name 		= 			"Assignment"
		verbose_name_plural = 			"Assignments"






