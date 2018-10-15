from django.contrib.auth import (
	authenticate,
	get_user_model,
	login,
	logout
)
from django.shortcuts import render, redirect
from .forms import UserLoginForm, UserRegisterForm


def login_view(request):
	form = UserLoginForm(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data.get("username")
		password = form.cleaned_data.get("password")
		user = authenticate(username=username, password=password)
		login(request,user)
		# change redirect to profile page
		return redirect('core:welcome')
	context = {
		"name_nav" : 'Login',
		"nbar" : "Login",
		"form" : form,
	}
	return render(request, 'accounts/login.html', context)

def register_view(request):
	# if request.user.is_authenticated():
	# 	return redirect('core:welcome')
	# else:
	# 	pass
	form = UserRegisterForm(request.POST or None)
	if form.is_valid():
		user = form.save(commit=False)
		password = form.cleaned_data.get("password")
		user.set_password(password)
		user.save()
		new_user = authenticate(username=user.username, password=password)

		# loging in the newly registered user
		login(request, new_user)

		# change redirect to new user account form.
		return redirect("core:setup", user_id=user.id)

	context = {
		"name_nav" : 'Register',
		"nbar" : "Create Free Account",
		"form":form,
	}
	return render(request, 'accounts/login.html', context)


def logout_view(request):
	logout(request)
	return redirect('/')