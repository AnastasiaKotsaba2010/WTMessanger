from django.views.generic.edit import FormView
from django.views.generic import ListView
from django.contrib.auth import get_user_model
from .forms import MessageForm
from .models import ChatGroup, ChatMessage
from django.shortcuts import redirect, render
# from django.db.models import 
from django.views import View
from django.http import HttpRequest
from user_app.models import Profile


class ChatView(View):
    template_name = "messanger_app/chat.html"
    form_class = MessageForm

    def dispatch(self, request, *args, **kwargs):
        chat_group_id = self.kwargs['group_id']
        chat = ChatGroup.objects.get(pk=chat_group_id)

        user = request.user.profile
        if user in chat.members.all():
            current_group_messages = ChatMessage.objects.filter(chat_group=chat)
            for message in current_group_messages:
                message.views.add(user)
                message.save()
            return super().dispatch(request, *args, **kwargs)
        else:
            return redirect('groups')

    def get(self, request: HttpRequest, *args, **kwargs):
        if request.user.is_authenticated:
            profile = request.user.profile
            chat_group_id = kwargs["group_id"]
            chat_group = ChatGroup.objects.get(pk=chat_group_id)
            messages = ChatMessage.objects.filter(chat_group=chat_group)

            context = {
                'avatars': profile.avatar_set.filter(active=True, shown=True),
                'chat_group': chat_group,
                'messages': messages,
                'form_chat': MessageForm(),
                'list_chats': get_user_model().objects.exclude(pk=request.user.pk),
                'list_groups': ChatGroup.objects.filter(members=profile).exclude(is_personal_chat=True)
            }
            return render(request, self.template_name, context)
        else:
            return redirect('login')

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            form = MessageForm(request.POST, request.FILES)
            if form.is_valid():
                message = form.save(commit=False)
                message.author = request.user.profile
                message.chat_group = ChatGroup.objects.get(pk=kwargs['group_id'])
                message.save()
                return redirect(message.chat_group.get_absolute_url())
            else:
                return render(request, self.template_name, {
                    'form_chat': form,
                    'messages': ChatMessage.objects.filter(chat_group__pk=kwargs['group_id']),
                    'chat_group': ChatGroup.objects.get(pk=kwargs['group_id']),
                    'avatars': request.user.profile.avatar_set.filter(active=True, shown=True)
                })
        else:
            return redirect('login')
    
class ChatGroupListView(ListView):
    model = ChatGroup
    template_name = "messanger_app/chat.html"
    context_object_name = "list_groups"

class PersonalChatListView(ListView):
    template_name = "messanger_app/chat.html" 
    context_object_name = "list_chats"

    def get_queryset(self):
        queryset = get_user_model().objects.exclude(pk=self.request.user.pk)
        return queryset

def create_personal_chat(request, user_id):
    current_user = request.user.profile
    user_to_connect = Profile.objects.get(user__pk=user_id)
    group = ChatGroup.objects.filter(is_personal_chat=True).filter(members = current_user).filter(members = user_to_connect).first()
    if not group:
        group = ChatGroup.objects.create(
            name = f"Чат між {current_user} та {user_to_connect}",
            is_personal_chat = True,
            admin = current_user
        )
        group.members.add(current_user, user_to_connect)
        group.save()
    return redirect(group.get_absolute_url())