from django.views.generic.edit import FormView
from django.views.generic import ListView
from django.contrib.auth import get_user_model
from .forms import MessageForm
from .models import ChatGroup, ChatMessage
from django.shortcuts import redirect
from django.db.models import Q

class ChatView(FormView):
    template_name = "messanger_app/chat.html"
    form_class = MessageForm

    def dispatch(self, request, *args, **kwargs):
        chat_group_id = self.kwargs['group_id']
        chat = ChatGroup.objects.get(pk = chat_group_id)

        user = request.user
        if user in chat.users.all():
            current_group_messages = ChatMessage.objects.filter(chat_group = chat)
            for message in current_group_messages:
                message.views.add(user)
                message.save()

            return super().dispatch(request, *args, **kwargs)
        else:
            return redirect('groups')
       
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        chat_group_id = self.kwargs["group_id"]
        messages = ChatMessage.objects.filter(chat_group_id = chat_group_id)
        data["messages"] = messages
        data["chat_group"] = ChatGroup.objects.get(pk = chat_group_id)
        return data

    
class ChatGroupListView(ListView):
    model = ChatGroup
    template_name = "chat_app/groups.html"
    context_object_name = "list_groups"

class PersonalChatListView(ListView):
    template_name = "chat_app/personal_chats.html" 
    context_object_name = "list_chats"

    def get_queryset(self):
        queryset = get_user_model().objects.exclude(pk=self.request.user.pk)
        return queryset

def create_personal_chat(request, user_id):
    current_user = request.user
    user_to_connect = get_user_model().objects.get(pk=user_id)
    group = ChatGroup.objects.filter(is_personal_chat=True).filter(users = current_user).filter(users = user_to_connect).first()
    if not group:
        group = ChatGroup.objects.create(
            name = f"Чат між {current_user} та {user_to_connect}",
            is_personal_chat = True
        )
        group.users.add(current_user, user_to_connect)
        group.save()
    return redirect(group.get_absolute_url())