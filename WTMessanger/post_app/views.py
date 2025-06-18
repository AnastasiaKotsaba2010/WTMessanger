# from django.views.generic.edit import CreateView
# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.urls import reverse_lazy
# from .forms import PostForm
# from .models import Post
# from core_app.models import WtUser_Profile

# class CreatePostView(LoginRequiredMixin, CreateView):
#     model = Post
#     form_class = PostForm
#     template_name = 'post/create_post.html'
#     success_url = reverse_lazy('core')  

#     def form_valid(self, form):
#         # profile = WtUser_Profile.objects.get(user=self.request.user)
#         form.instance.author = profile
#         return super().form_valid(form)

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['posts'] = Post.objects.all()
#         return context