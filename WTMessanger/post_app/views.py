from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import PostForm
from .models import Post, Image, Link, Tag
from django.http import HttpRequest
from user_app.models import Avatar
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.generic import ListView, FormView

class CreatePostView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post/create_post.html'
    success_url = reverse_lazy('core')  
    
    def get(self, request: HttpRequest): 
        profile = request.user.profile
        avatar = Avatar.objects.filter(profile = profile, active = True, shown = True).first()       
        
        all_posts = Post.objects.filter(author= request.user.profile).order_by('-id')

        if request.user.is_authenticated:
            # return JsonResponse({'profiles': list(all_posts.values())})
            return render(request, self.template_name, 
                context= {
                    'username': request.user.email,
                    'first_name': request.user.first_name,
                    'last_name': request.user.last_name,
                    'avatar': avatar,
                    'form': PostForm(),
                    'posts': all_posts
                })
        return render(request, self.template_name)
    
    def post(self, request: HttpRequest):
        form = PostForm(request.POST, request.FILES)
        
        if form.is_valid():
            post = form.save(commit = False)
            post.author = request.user.profile
            
            # CONTENT SPLIT
            content = form.cleaned_data.get('content')
            post.content = ' '.join(word for word in content.split() if not word.startswith('#'))
            post.save()
            
            for word in content.split():
                if word.startswith('#') and len(word) > 1: # startswith - якщо починається із '#' 
                    tag = Tag.objects.get_or_create(name= word[1:])[0] # зберігаємо тег без '#'
                    # word[1:] - зріз, беремо слово від 1 ел-ту і до кінця
                    # тег: #tag1 --> зберігаємо в бд: tag1 ((name= word[1:])[0])
                    # get_or_create() - повертає 2 об'єкти: сам тег і булеве значення, тому [0] - тег
                    post.tags.add(tag)
                    print(tag)
                
            # IMAGE SAVE
            # getlist - отримує всі файли з інпутв
            uploaded_files = request.FILES.getlist('images')
            post_images = []
            
            for file in uploaded_files:
                post_image = Image.objects.create(
                    filename = file.name, 
                    file = file
                )
                post_images.append(post_image)
                
            post.save()
            post.images.set(post_images)
            
            
            # LINKS SAVE
            links = request.POST.getlist('links')
            for link in links:
                if link.strip(): # strip - видаляє пробіли на початку/в кінці рядку
                    Link.objects.create(
                        post = post, 
                        url = link
                    )
            
            # TAGS SAVE
            # set - замінює усі зображення/теги/посилання для поста в полі manyToMany і зберігає в окремі моделі 
            tags = form.cleaned_data.get('tags')
            if tags:
                post.tags.set(tags)

            images = form.cleaned_data.get('images')
            if images:
                post.images.set(images)
                
            print('form is valid')
            all_posts = Post.objects.filter(author= request.user.profile).order_by('-id')
            avatar = Avatar.objects.filter(profile= request.user.profile, active=True, shown=True).first()

            # posts_tags = Tag.objects.all()
            # posts_links = Link.objects.all()
            # posts_images = Image.objects.all()
            # print(f'Tags: {posts_tags}\nLinks: {posts_links}\nImage: {posts_images}')

            # return render(request, self.template_name, 
            #     context = {
            #         'posts': all_posts,
            #         'form': PostForm(),
            #         'avatar': avatar,
            #         'username': request.user.email,
            #         'first_name': request.user.first_name,
            #         'last_name': request.user.last_name,
            #     }
            # )
            
            return redirect('core')

        all_posts = Post.objects.filter(author= request.user.profile).order_by('-id')
        avatar = Avatar.objects.filter(profile= request.user.profile, active=True, shown=True).first()

        print(form.errors)
        print('form is INvalid')
        
        return render(request, self.template_name, {
            'form': form,
            'posts': all_posts,
            'avatar': avatar,
            'username': request.user.email,
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
        })
        
        
    # def form_valid(self, form):
    #     form.instance.author = self.request.user.profile
    #     return super().form_valid(form)



#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['posts'] = Post.objects.all()
#         return context


