from django import forms
from .models import UserInfo

class UserInfoForm(forms.ModelForm):
    class Meta():
        model = UserInfo
        fields = ('name', 'email')
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.TextInput(attrs={'class':'form-control'})
        }