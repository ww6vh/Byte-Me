from django import forms


class SignUpForm(forms.Form):
    username = forms.CharField(label='Username', max_length=50)
    email = forms.CharField(label='Email', max_length=50)
    password = forms.CharField(label='Password', max_length=50)
    confirm_password = forms.CharField(label='Confirm Password', max_length=50)


class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=50)
    password = forms.CharField(label='Password', max_length=50)


class CreateListingForm(forms.Form):
    make = forms.CharField(label="Make", max_length=100)
    model = forms.CharField(label="Model", max_length=100)
    condition = forms.CharField(label="Condition", max_length=10)
    description = forms.CharField(label='Description', max_length=500)