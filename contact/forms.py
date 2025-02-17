from django import forms


class ContactForm(forms.Form):
    email = forms.EmailField(
        label='Your Email',
        widget=forms.EmailInput(attrs={'class': 'form-control'}))
    subject = forms.CharField(
        label='Subject',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    message = forms.CharField(
        label='Message',
        widget=forms.Textarea(attrs={'class': 'form-control'}))
