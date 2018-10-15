from django.shortcuts import render
from django.http import (
	Http404, HttpResponse, HttpResponsePermanentRedirect, HttpResponseRedirect,
)
from django.urls import reverse


# from .forms import InterestedForm

# LANDING PAGE
def index(request):
	context = {
		'show_last_div' : False,
	}

	return render(request, 'landing.html', context)

# HOMEPAGE FOR PAYING CUSTOMER.
def welcome(request):
	context = {
		'show_last_div' : False,
	}

	return render(request, 'core/welcome.html', context)

# PAGE TO SETUP ACCOUNT. REDIRECT AFTER FIRST REGISTER.
def setup(request):
	context = {

	}
	return render(request, 'core/setup.html', context)

# PAGE TO CREATE A NEW ASSIGNMENT
def new_assignment(request):
	context = {

	}
	return render(request, 'core/new_assignment.html', context)