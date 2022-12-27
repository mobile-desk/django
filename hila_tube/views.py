from django.shortcuts import render, redirect, get_object_or_404
from email import message
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from mysite import settings
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Video, Category, Profile, Contact, Comment
from .forms import VideoForm, EditProfileForm, EditPasswordForm, ProfileForm, ContactForm, CommentForm
from django.urls import reverse_lazy, reverse

from django.views import View
from django.http import HttpResponseRedirect

from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


#def hometube(request):
#    data = Video.objects.all()
#    context = {
#        'data': data
#    }
#    return render(request, 'tube_home.html', context)


#view logged in user profile

#class ViewUser(ListView):
#    model = Video
#    template_name = 'tube/profile.html'
#    context_object_name = 'videos'
#
#    def get_context_data(self, **kwargs):
#        context = super().get_context_data(**kwargs)
#        context['user'] = self.request.user
#        return context
#
#    def get_queryset(self):
#        return Video.objects.filter(author=self.request.user)


#view logged in user profile

def view_user_posts(request):
    user = request.user
    videos = Video.objects.all()
    profiles = Profile.objects.all()
    context = {
        'videos': videos,
        'profiles': profiles,
    }
    return render(request, 'tube/profile.html', context)





def LikeView(request, pk):
    video = get_object_or_404(Video, id=request.POST.get('video_id'))
    
    #check if current user has liked post
    liked = False
    if video.likes.filter(id=request.user.id).exists():
        video.likes.remove(request.user)
        liked = False
    else:
        video.likes.add(request.user)
        liked = True

    return HttpResponseRedirect(reverse('viewtube', args=[str(pk)]))






class Hometube(ListView):
    model = Video
    template_name = 'tube/tube_home.html'
    cats = Category.objects.all()
    ordering = ['-id']
    #ordering = ['-created_at']

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(Hometube, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context
    

class viewtube(DetailView):
    model = Video
    template_name = 'tube/tubevids.html'
    


    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(viewtube, self).get_context_data(*args, **kwargs)
        
        
        stuff = get_object_or_404(Video, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()

        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True

        context["cat_menu"] = cat_menu
        context["total_likes"] = total_likes
        context["liked"] = liked
        return context


#def hometube(request): 
#    return render(request, 'tube_home.html')

#class hometube(ListView):
#    model = Video
#    template_name = 'tube_home.html'


#class Add(CreateView):
#    model = Video
#    form_class = VideoForm
#    template_name = 'uploadvid.html'


class Add(LoginRequiredMixin, CreateView):
    model = Video
    form_class = VideoForm
    template_name = 'tube/uploadvid.html'


    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class AddCommentView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'tube/add_comment.html'
    #fields = '__all__'

    def form_valid(self, form):
        form.instance.commenter = self.request.user
        form.instance.videopost_id = self.kwargs['pk']
        return super().form_valid(form)






class Complaint(LoginRequiredMixin, CreateView):
    model = Contact
    form_class = ContactForm
    template_name = 'tube/complaint.html'


    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)



class CreateProfile(LoginRequiredMixin, CreateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'tube/uploadprof.html'


    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

def author_view(request, author_name):
    videos = Video.objects.filter(author__username=author_name)
    context = {
        'videos': videos,
        'author_name': author_name.upper()
    }
    return render(request, 'tube/user_posts.html', context)



class AddCategory(CreateView):
    model = Category
    #form_class = VideoForm
    template_name = 'tube/uploadcategory.html'
    fields = '__all__'


def CategoryListView(request):
    cat_menu_list = Category.objects.all()
    return render(request, 'tube/category_list.html', {'cat_menu_list': cat_menu_list})




def CategoryView(request, cats):
    category_video = Video.objects.filter(category=cats.replace('-', ' '))
    return render(request, 'tube/category.html', {'cats': cats.title().replace('-', ' '), 'category_video': category_video})


class Update(UpdateView):
    model = Video
    form_class = VideoForm
    template_name = 'tube/editvid.html'



#class UpdateProfile(UpdateView):
#    model = Profile
#    form_class = ProfileForm
#    template_name = 'tube/profile_settings.html'



def update_profile(request):
    if request.method == 'POST':
        # Handle form submission
        form = ProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        # Display the form for editing
        form = ProfileForm(instance=request.user.profile)
    return render(request, 'tube/profile_settings.html', {'form': form})



#def edit_user_profile(request):
#    if request.method == 'POST':
#        form = ProfileForm(request.POST, instance=request.user)
#        if form.is_valid():
#            form.save()
#            return redirect('profile')
#    else:
#        form = ProfileForm(instance=request.user)
#        context = {
#            'form': form
#        }
#    return render(request, 'tube/profile_settings.html', context)
    




#def edit_user_profile(request):
#    
#    if request.user.is_authenticated:
#        
#        from .models import Profile
#        user = request.user
#        profile = Profile.objects.get(user=user)
#        form = ProfileForm(initial={
#            'profile_pic': profile.profile_pic,
#            'birthday': profile.birthday,
#            'bio': profile.bio,
#            'link': profile.link,
#        })
#        context = {'form': form}
#        return render(request, 'tube/profile_settings.html', context)
#
#    else:
#        return redirect('home')
    
    
            


    
class Delete(DeleteView):
    model = Video 
    template_name = 'tube/deletevid.html'
    success_url = reverse_lazy('home')

#def view_user_videos(request, username, video_id):
#    user = User.objects.get(username=username)
#    video = Video.objects.get(id=video_id)
#    context = {
#        'user': user,
#        'video': video,
#    }
#    return render(request, 'user_posts.html', context)




def signup(request):
    
    
    if request.method == "POST":
        #username = request.POST.get('username')
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
    
        if User.objects.filter(username=username):
            messages.error(request, "Username already exists")
            return redirect('home')
        
        if User.objects.filter(email=email):
            messages.error(request, "Email already exists")
            return redirect('home')
        
        if len(username)>10:
            messages.error(request, "Username must be under 10 characters")
            return redirect('home')
         
        if password != password2:
            messages.error(request, "Passwords do not match!")  
            return redirect('home')
         
        if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric!")
            return redirect('home')      
    
        myuser = User.objects.create_user(username, email, password)
        myuser.first_name = fname
        myuser.last_name = lname
        
        
        myuser.save()    
        
        messages.success(request, "Your Account has been created successfully.")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            fname = user.first_name
            return redirect('create_profile')
            
        else:
            messages.error(request, "Login Error")
            return redirect('home')    

        #return redirect('create_profile')  
        
       
    
    return render(request, 'tube/signup.html')

def signin(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
    
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            fname = user.first_name
            return redirect('home')
            
        else:
            messages.error(request, "Login Error")
            return redirect('home')    
    
    return render(request, 'tube/signin.html')

def signout(request):
    logout(request)
    messages.success(request, "Successfully Logged Out ")
    return redirect('home')



def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = EditProfileForm(instance=request.user)
    context = {
        'form': form
    }
    return render(request, 'tube/privacy_settings.html', context)




def change_password(request):
    if request.method == 'POST':
        form = EditPasswordForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            return redirect('profile')
    else:
        form = EditPasswordForm(request.user)
    context = {
        'form': form
    }
    return render(request, 'tube/change_password.html', context)




#
#def edit_user(request):
#    if request.method == 'POST':
#        form = EditUserForm(request.POST)
#        if form.is_valid():
#            # Update the user's information
#            user = request.user
#            user.username = form.cleaned_data['username']
#            user.email = form.cleaned_data['email']
#            user.set_password(form.cleaned_data['password'])
#            user.save()
#            # Redirect the user back to the profile page
#            return redirect('home')
#    else:
#        form = EditUserForm(initial={'username': request.user.username, 'email': request.user.email})
#    return render(request, 'tube/privacy_settings.html', {'form': form})
#




