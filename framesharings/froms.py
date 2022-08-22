from django import forms
from .models import Frame

class PostFrame(forms.ModelForm):
    class Meta:
        model = Frame
        fields = ["framephoto","frametitle","framekeyword","frameexample","framepublic","framememo"]

