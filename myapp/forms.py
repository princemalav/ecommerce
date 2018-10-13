from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class ContactForm(forms.Form):
    # TODO: Define form fields here:
    fullname   =  forms.CharField(
    			widget=forms.TextInput(
    				attrs={"class":"form-control",
    						"placeholder":"Your full name"

    						}
    					)
    			)
 
    email      =  forms.EmailField(
    			widget=forms.EmailInput(
    				attrs={"class":"form-control",
    					   "placeholder":"Your Email"}
    				))
 
    content    =  forms.CharField(
    			widget=forms.Textarea(
    				attrs={"class":"form-control",
    						"placeholder":"Your content"

    				}
    			)
    		)
    #for validation of mail:- 
    def clean_email(self):
    	email = self.cleaned_data.get("email")
    	if not "gmail.com" in email:
    		raise forms.ValidationError("Please Enter Correct email")

    	return email
    	
class LoginForm(forms.Form):
    username = forms.CharField(
    	  		widget=forms.TextInput(
    	  			attrs={
    	  				"class":"form-control",
    	  				"placeholder":"Enter your username"}))
    password = forms.CharField(
    			widget=forms.PasswordInput(
    				attrs={
    					"class":"form-control",
    					"placeholder":"Enter password"}))


class RegisterForm(forms.Form):
	 username = forms.CharField(
    	  		widget=forms.TextInput(
    	  			attrs={
    	  				"class":"form-control",
    	  				"placeholder":"Enter your username"}))
	 
	 email   =  forms.EmailField(
	 			widget=forms.TextInput(
	 				attrs={
	 					"class":"form-control",
    	  				"placeholder":"Enter your email"
	 				 }))
	 password = forms.CharField(
    			widget=forms.PasswordInput(
    				attrs={
    					"class":"form-control",
    					"placeholder":"Enter password"}))
	 password2 = forms.CharField(
	 			label='Confirm Password',
    			widget=forms.PasswordInput(
    				attrs={
    					"class":"form-control",
    					"placeholder":"Enter password"}))
	 
	 def clean_username(self):
	 	username=self.cleaned_data.get('username')
	 	qs = User.objects.filter(username=username)
	 	if qs.exists():
	 		raise forms.ValidationError("Username is taken")
	 	return username

	 def clean_email(self):
	 	email=self.cleaned_data.get('email')
	 	qs = User.objects.filter(email=email)
	 	if qs.exists():
	 		raise forms.ValidationError("email is taken")
	 	return email	

	 def clean(self):
	 	data = self.cleaned_data
	 	password = self.cleaned_data.get('password')
	 	password2 = self.cleaned_data.get('password2')
	 	if password2 != password:
	 		raise forms.ValidationError("Password Is Not  Matching")

	 	return data























