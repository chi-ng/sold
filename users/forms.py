from django import forms
from django.contrib.auth.forms import UserCreationForm


from django.utils.translation import ugettext, ugettext_lazy as _

from bootstrap_datepicker_plus import DatePickerInput

import logging
logger = logging.getLogger('django')

#models
from django.contrib.auth.models import User

from .models import Profile
from welcome.models import Bid


class CustomUserCreationForm(UserCreationForm):
    error_messages = {
        'password_mismatch': _("The two password fields didn't match."),
    }
    password1 = forms.CharField(label=_("Password"),
        widget=forms.PasswordInput)
    password2 = forms.CharField(label=_("Password confirmation"),
        widget=forms.PasswordInput,
        help_text=_("Enter the same password as above, for verification."))
    class Meta:
        model = User
        fields = ("username", "email",)
    def clean_username(self):
        username = self.cleaned_data.get("username")
        logger.info(username)
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("This username has been registered!")
        return username
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email has been registered!")
        return email
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2
    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields=['username', 'email']
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields=['date_of_birth', 'image']
        widgets = {
            'date_of_birth': DatePickerInput(),
        }
class BidCreationForm(forms.ModelForm):
    def __init__(self, *args, pk=None, **kwargs):
        super(forms.Form, self).__init__(*args, **kwargs)
        if productor_pk is not None:
            self.fields['productos'].queryset = Item.objects.filter(
                id=pk
            )
    def clean_price(self,form):
        price = self.cleaned_data.get("price")
        item
        if image:
            if image._size > settings.MAX_IMAGE_SIZE:
                raise ValidationError("Image file too large ( > 20mb )")
        else:
            raise ValidationError("Couldn't read uploaded image")

    class Meta:
        model = Bid
        fields=['price']
