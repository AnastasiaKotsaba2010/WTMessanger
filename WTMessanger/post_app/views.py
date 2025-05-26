from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import WTUserPostForm
from .models import  WTUser_Post
# Create your views here.


class CreatePostView(LoginRequiredMixin, CreateView):
    model = WTUser_Post
    form_class = WTUserPostForm
    template_name = 'post/create_post.html'
    success_url = reverse_lazy('core')  

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
