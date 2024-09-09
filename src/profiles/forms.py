from django import forms

from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'name',
            'description',
            'featured',
            'email'
        ]
    
class RawProfileForm(forms.Form):
    name   = forms.CharField(label='',widget=forms.TextInput(attrs={"placeholder":"Your Name"}))
    description = forms.CharField(
                    required=False,
                    widget=forms.Textarea(
                        attrs={
                            "placeholder":"Description",
                            "class": "new-class-2",
                            "rows":3,
                            "cols":20
                        }
                    ))
    email = forms.EmailField()