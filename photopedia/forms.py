from django import forms
from .models import *


class ForgetPasswordForm(forms.Form):
    email = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "type": "email",
                "class": "form-control",
                "placeholder": "Email",
                "required": "",
            }
        )
    )


class LoginForm(forms.Form):
    email = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "type": "email",
                "class": "form-control",
                "placeholder": "Email",
                "required": "",
            }
        )
    )
    password = forms.CharField(
        max_length=100,
        widget=forms.PasswordInput(
            attrs={
                "type": "password",
                "class": "form-control",
                "placeholder": "password",
                "required": "",
            }
        )
    )


class SignUpForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = (
            'first_name',
            'last_name',
            'email',
            'password',
            'password_confirm',
            'department',
            'user_type',
        )

    first_name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={
                "placeholder": "First Name",
                "class": "form-control",
            }
        )
    )
    last_name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Last Name",
                "class": "form-control",
            }
        )
    )
    email = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "type": "email",
                "class": "form-control",
                "placeholder": "Email",
                "required": "",
            }
        )
    )
    password = forms.CharField(
        max_length=100,
        widget=forms.PasswordInput(
            attrs={
                "type": "password",
                "class": "form-control",
                "placeholder": "password",
                "required": "",
            }
        )
    )
    password_confirm = forms.CharField(
        max_length=100,
        widget=forms.PasswordInput(
            attrs={
                "type": "password",
                "class": "form-control",
                "placeholder": "Confirm Password",
                "required": "",
            }
        )
    )
    department = forms.CharField(
        widget=forms.Select(
            choices=DeptChoice,
            attrs={
                "class": "form-control",
                "required": "",
            })
    )
    user_type = forms.CharField(
        widget=forms.Select(
            choices=userType,
            attrs={
                "class": "form-control",
                "required": "",
            })
    )


class ProfileFrom(forms.ModelForm):

    class Meta:
        model = Account
        fields = (
            'first_name',
            'last_name',
            'department',
            'year',
            'semester',
            'enrollment',
            'profile_pic',
        )

    first_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "placeholder": "First Name",
                "class": "form-control",
            }
        )
    )
    last_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "placeholder": "First Name",
                "class": "form-control",
            }
        )
    )
    department = forms.CharField(
        widget=forms.Select(
            choices=DeptChoice,
            attrs={
                "class": "form-control",
                "required": "",
            })
    )
    year = forms.CharField(
        required=False,
        widget=forms.Select(
            choices=YearChoice,
            attrs={
                "class": "form-control",
                "required": "",
            })
    )
    semester = forms.CharField(
        required=False,
        widget=forms.Select(
            choices=SemChoice,
            attrs={
                "class": "form-control",
                "required": "",
            })
    )
    enrollment = forms.CharField(
        required=False,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
            }
        )
    )
    profile_pic = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'id': "customFile",
                "class": "custom-file-input",
            }
        )
    )


class PinForm(forms.ModelForm):
    class Meta:
        model = Pin
        fields = (
            'title',
            'image',
            'details',
            'category',
            'tag',
        )

    title = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Add Your title",
                "class": "form-control",
            }
        )
    )
    image = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'id': "customFile",
                "class": "custom-file-input",
            }
        )
    )
    details = forms.CharField(
        max_length=1000,
        widget=forms.Textarea(
            attrs={
                "rows": "3",
                "placeholder": "Write about your pin",
                "class": "form-control",
            }
        )
    )
    category = forms.CharField(
        widget=forms.Select(
            choices=pin_category,
            attrs={
                "class": "form-control",
                "required": "",
            })
    )
    tag = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Add tag's",
                "class": "form-control",
            }
        )
    )
