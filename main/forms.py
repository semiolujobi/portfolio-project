from django import forms
from .models import ContactProfile


class ContactForm(forms.ModelForm):

	name = forms.CharField(max_length=100, required=True,
		widget=forms.TextInput(attrs={
			'placeholder': 'Your Name',
			'class': 'form-control'
			}))
	email = forms.EmailField(max_length=254, required=True, 
		widget=forms.TextInput(attrs={
			'placeholder': 'Your Email',
			'class': 'form-control'
			}))
	subject = forms.CharField(max_length=100, required=False,
		widget=forms.TextInput(attrs={
			'placeholder': 'Subject',
			'class': 'form-control'
			}))
	message = forms.CharField(max_length=1000, required=True, 
		widget=forms.Textarea(attrs={
			'placeholder': 'Message',
			'class': 'form-control',
			'rows': 6,
			}))


	class Meta:
		model = ContactProfile
		fields = ('name', 'email', 'subject', 'message',)