from django.shortcuts import render, get_object_or_404
from django.http import (
	Http404, HttpResponse, HttpResponsePermanentRedirect, HttpResponseRedirect,
)
from django.urls import reverse

from . models import interested, clientele, assignment
from .forms import InterestedForm, clienteleForm, assignmentForm

# LANDING PAGE
def index(request):
	context = {
		'show_last_div' : False,
	}

	return render(request, 'landing.html', context)

# HOMEPAGE FOR PAYING CUSTOMER.
def welcome(request):
	if request.user.is_authenticated:
		pass
	else:
		return HttpResponseRedirect(reverse('core:index'))
	# print(request.user.id)
	client_assignment = assignment.objects.filter(client_id=request.user.id)
	

	if client_assignment.count() == 0:
		client_assignment = None
	context = {
		'client_assignment' : client_assignment,
		'show_last_div' : False,
	}

	return render(request, 'core/welcome.html', context)

# PAGE TO SETUP ACCOUNT. REDIRECT AFTER FIRST REGISTER.
def setup(request, user_id=None):

	if request.method == 'POST':
		form = clienteleForm(request.POST or None)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.save()
			return HttpResponseRedirect(reverse('core:welcome'))
	else:
		form = clienteleForm()


	context = {
		'form' : form,
		"tab_text": "Confirm.",
	}
	return render(request, 'core/setup.html', context)

# PAGE TO CREATE A NEW ASSIGNMENT
def new_assignment(request, user_id=None):

	if request.method == 'POST':
		form = assignmentForm(request.POST or None)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.client_id = user_id
			instance.save()

			return HttpResponseRedirect(reverse('core:welcome'))
	else:
		form = assignmentForm()
	context = {
		'form' : form,
		"tab_text": "Confirm.",
	}
	return render(request, 'core/new_assignment.html', context)