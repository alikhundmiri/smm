from django.shortcuts import render
from django.http import (
	Http404, HttpResponse, HttpResponsePermanentRedirect, HttpResponseRedirect,
)
from django.urls import reverse

from . models import interested, clientele, assignment
from .forms import InterestedForm

# LANDING PAGE
def index(request):
	context = {
		'show_last_div' : False,
	}

	return render(request, 'landing.html', context)

# HOMEPAGE FOR PAYING CUSTOMER.
def welcome(request, user_id=None):

	client_assignment = assignment.objects.filter(client=user_id)
	
	if client_assignment.count() == 0:
		client_assignment = None
	context = {
		'client_assignment' : client_assignment,
		'show_last_div' : False,
	}

	return render(request, 'core/welcome.html', context)

# PAGE TO SETUP ACCOUNT. REDIRECT AFTER FIRST REGISTER.
def setup(request, user_id=None):
	context = {

	}
	return render(request, 'core/setup.html', context)

# PAGE TO CREATE A NEW ASSIGNMENT
def new_assignment(request, user_id=None):
	context = {

	}
	return render(request, 'core/new_assignment.html', context)