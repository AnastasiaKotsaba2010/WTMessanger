from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import PostForm
from .models import Post
from django.http import HttpRequest
from user_app.models import Avatar
from django.shortcuts import render

class CreatePostView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post/create_post.html'
    success_url = reverse_lazy('core')  
    
    def get(self, request: HttpRequest): 
        profile = request.user.profile
        avatar = Avatar.objects.filter(profile = profile, active = True, shown = True).first()       
        
        if request.user.is_authenticated:
            return render(
                request, 
                self.template_name, 
                context= {
                    'username': request.user.email,
                    'first_name': request.user.first_name,
                    'last_name': request.user.last_name,
                    'avatar': avatar,
                    'form': self.form_class
                })
        return render(request, self.template_name)

    def form_valid(self, form):
        form.instance.author = self.request.user.profile
        return super().form_valid(form)

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['posts'] = Post.objects.all()
#         return context