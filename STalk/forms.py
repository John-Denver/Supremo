from django import forms
from . models import Deejay, User, Mc, Planner, Hype,  Events, Ethnic, Speakers


class DjForm(forms.ModelForm):

    class Meta:
        model = Deejay
        fields = '__all__'


class UserForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class McForm(forms.ModelForm):

    class Meta:
        model = Mc
        fields = '__all__'


class PlanForm(forms.ModelForm):

    class Meta:
        model = Planner
        fields = '__all__'


class HypeForm(forms.ModelForm):

    class Meta:
        model = Hype
        fields = '__all__'


class SpeakerForm(forms.ModelForm):

    class Meta:
        model = Speakers
        fields = '__all__'




