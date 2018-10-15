from django import forms
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
)

User = get_user_model()

class UserLoginForm(forms.Form):
    username = forms.CharField(label='',widget = forms.TextInput(attrs={'placeholder': 'User Name', 'class':'form-control'}))
    password = forms.CharField(label='',widget = forms.PasswordInput(attrs={'placeholder': 'Password', 'class':'form-control'}))

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("This user does not exist.")
            if not user.check_password(password):
                raise forms.ValidationError("Incorrect Password.")
            if not user.is_active:
                raise forms.ValidationError("This user is no longer Active.")
        return super(UserLoginForm, self).clean(*args, **kwargs)


class UserRegisterForm(forms.ModelForm):
    username = forms.CharField(label='',widget = forms.TextInput(attrs={'placeholder': 'Create a new Unique Username.', 'class':'form-control'}))
    email = forms.EmailField(label='',widget = forms.TextInput(attrs={'placeholder': 'Your valid email address.', 'class':'form-control'}))
    password = forms.CharField(label='',widget=forms.PasswordInput(attrs={'placeholder': 'Enter the password you wish to set...', 'class':'form-control'}))

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password'
        ]