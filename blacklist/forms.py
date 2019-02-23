from django import forms

class UploadFileForm(forms.Form):
    blacklist = forms.FileField()