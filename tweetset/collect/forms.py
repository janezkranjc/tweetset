from django import forms
from django.contrib.auth.models import User
from collect.models import Collection
from twython import Twython

class SignupForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput,required=True)
    repeat_password = forms.CharField(widget=forms.PasswordInput,required=True)
    i_agree = forms.BooleanField(required=True)

    def clean(self):
        cleaned_data = super(SignupForm, self).clean()
        password = cleaned_data.get("password")
        repeat_password = cleaned_data.get("repeat_password")
        email = cleaned_data.get("email")
        if password != repeat_password:
            msg = u"Passwords do not match."
            self._errors["repeat_password"] = self.error_class([msg])
            del cleaned_data["password"]
            del cleaned_data["repeat_password"]

        if User.objects.filter(email=email).count()>0:
            msg = u"This email is already used by another account."
            self._errors["email"] = self.error_class([msg])
            del cleaned_data["email"]
        return cleaned_data

class CollectionForm(forms.ModelForm):
    class Meta:
        model = Collection
        exclude = ['user','firehose']

    def clean(self):
        cleaned_data = super(CollectionForm, self).clean()
        consumer_key = cleaned_data.get("consumer_key",None)
        consumer_secret = cleaned_data.get("consumer_secret",None)
        access_token = cleaned_data.get("access_token",None)
        access_token_secret = cleaned_data.get("access_token_secret",None)
        try:
            twitter = Twython(consumer_key,consumer_secret,access_token,access_token_secret)
            twitter.verify_credentials()
        except:
            msg = u"Your Twitter credentials did not validate."
            self._errors["consumer_key"] = self.error_class([msg])
            self._errors["consumer_secret"] = self.error_class([msg])
            self._errors["access_token"] = self.error_class([msg])
            self._errors["access_token_secret"] = self.error_class([msg])
            del cleaned_data["consumer_key"]
            del cleaned_data["consumer_secret"]
            del cleaned_data["access_token"]
            del cleaned_data["access_token_secret"]
        return cleaned_data

