from django import forms

class HashForm(forms.Form):
    text = forms.CharField(label='Enter plane text.', widget=forms.Textarea)
    