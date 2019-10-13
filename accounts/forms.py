from django import forms
from django.contrib.auth import get_user_model


User = get_user_model()
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

    # def clean_username(self):
    #     username = self.cleaned_data.get('username')
    #     try:
    #         user = User.objects.get(username=username)
    #     except User.DoesNotExist:
    #         raise forms.ValidationError('Are you sure you registered? We cannot find this user name')
    #     return username
    def clean_password(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise forms.ValidationError('Are you sure you registered? We cannot find this user name')
        if not user.check_password(password):
            raise forms.ValidationError('Invalid Password')
        return password
        

class RegistrationForm(forms.ModelForm):
    email = forms.EmailField(label = 'Email')
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput())
    password2 = forms.CharField(label = 'Confirm Password', widget = forms.PasswordInput())
    class Meta:
        model = User
        fields = ['username','email']
    
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Passwords do not match')
        elif not password1 or not password2:
            raise forms.ValidationError('You need to fill password fields ')
        return password2
    def clean_email(self):
        email = self.cleaned_data.get('email')
        user_count = User.objects.filter(email=email).count()
        if user_count > 0:
            raise forms.ValidationError('This email has already been registered')
        return email
    def save(self, commit =True):
        user = super(RegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data.get('password2'))
        if commit:
            user.save()
        return user




