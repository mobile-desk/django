from django import forms
from .models import Video, Category, Profile, Contact, Comment
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User

#from bootstrap_datepicker_plus import DatePickerInput
from bootstrap_datepicker_plus.widgets import DatePickerInput

#class ContactForm(forms.ModelForm):
#    class Meta:
#        model = Video
#
#        fields = '__all__'
#        exclude = ('author','comments', 'tags')


#choices = [('coding', 'coding'), ('sport', 'sport')]
choices = Category.objects.all().values_list('name','name')

choice_list = []

for item in choices:
    choice_list.append(item)

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video

        fields = '__all__'
        exclude = ('author', 'comments', 'tags', 'likes')


        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choice_list,attrs={'class': 'form-control form-select'}),
            'author': forms.Select(attrs={'class': 'form-control form-select'}),
            'thumbnail' : forms.FileInput(attrs={'class': 'form-control form-control-sm'}),
            'video_file' : forms.FileInput(attrs={'class': 'form-control form-control-sm'})
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment

        fields = '__all__'
        exclude = ('videopost', 'commenter', 'created_at', 'updated_at')


        widgets = {
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }







class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        
        fields = '__all__'
        exclude = ('user', 'created_at',)


        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'complaint': forms.Textarea(attrs={'class': 'form-control'}),
            'image' : forms.FileInput(attrs={'class': 'form-control form-control-sm'}),
            
        }




#class ProfileForm(forms.ModelForm):
#    class Meta:
#        model = Profile
#        fields = ['profile_pic', 'birthday', 'bio', 'link']
#
#
#    widgets = {
#        'profile_pic': forms.FileInput(attrs={'class': 'form-control form-control-sm'}),
#        'birthday': forms.DateField(attrs={'class': 'form-control form-control-sm'}),
#        'bio': forms.Textarea(attrs={'class': 'form-control'}),
#        'link': forms.TextInput(attrs={'class': 'form-control'}),
#    }


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_pic', 'birthday', 'bio', 'link']


    # Image field
    profile_pic = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={
            'class': 'form-control-file'
        })
    )

    # Date field
    birthday = forms.DateField(
        #widget = forms.DateField(widget=DatePickerInput())
        widget=DatePickerInput(attrs={
            'class': 'form-control',
            'placeholder': 'YYYY-MM-DD'
        })
    )

    # Text field
    bio = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control'
        })
    )

    # Charfield
    link = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control'
        })
    )




class EditProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


        widgets = {
            'username' : forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }


class EditPasswordForm(PasswordChangeForm):
    pass


#class EditUserForm(forms.Form):
#    username = forms.CharField(max_length=30)
#    email = forms.EmailField()
#    password = forms.CharField(max_length=30, widget=forms.PasswordInput)
#
#    widgets = {
#        'username': forms.TextInput(attrs={'class': 'form-control'}), 
#        'email': forms.TextInput(attrs={'class': 'form-control'}), 
#    }