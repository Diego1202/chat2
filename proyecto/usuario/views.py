from django.views.decorators.debug import sensitive_post_parameters
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .forms import UserCreationForm, LoginForm, ProfileForm, UpdatedForm, CustomPasswordChangeForm
from django.contrib.auth.views import LogoutView
from django.contrib import auth
from django.db.models import Q
from django.contrib.auth.models import User
from .models import Profile, Message
from django.contrib.auth.decorators import login_required
from django.dispatch import receiver
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.utils import timezone
from django.http import JsonResponse
from django.http import Http404

# Create your views here.
def home(request):
    return render(request, "usuario/home.html")

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'usuario/register.html', {'form': form})

def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = auth.authenticate(username = form.cleaned_data["username"], password =form.cleaned_data["password"])
            auth.login(request, user)
            profile = user.profile
            profile.is_online = True
            profile.save()
            return redirect("home")
    else:
        form = LoginForm()
    return render(request, 'usuario/login.html', {'form': form})

@login_required
def profile_update(request):
    profile = request.user.profile
    user = User.objects.get(id=request.user.id)
    profile_form = ProfileForm(request.POST or None, instance=profile)
    user_form = UpdatedForm(request.POST or None, instance=user)
    if profile_form.is_valid() and user_form.is_valid():
        profile_form.save()
        user_form.save()
        return redirect('home')
    return render(request, 'usuario/profile_update.html', {'profile_form': profile_form, 'user_form': user_form})

class logout(LogoutView):
    next_page='login'

@login_required
def chat(request):
    return render(request, 'usuario/chat.html')

@receiver(user_logged_in)
def got_online(sender, user, request, **kwargs):    
    user.profile.is_online = True
    user.profile.save()

@receiver(user_logged_out)
def got_offline(sender, user, request, **kwargs):   
    user.profile.is_online = False
    user.profile.last_logout = timezone.now()
    user.profile.save()

@login_required
@sensitive_post_parameters()
def message_view(request, username):
    sender_profile = request.user.profile
    receiver_profile = get_object_or_404(Profile, user__username=username)

    if request.user.id == receiver_profile.user.id:
        return redirect('chat')

    if request.method == 'POST':
        content = request.POST.get('content')
        message = Message.objects.create(sender=sender_profile, receiver=receiver_profile, content=content)

        return redirect('chat-user', username=username)

    # Retrieve messages for the current sender and receiver
    messages = Message.objects.filter(Q(sender=sender_profile, receiver=receiver_profile) | Q(sender=receiver_profile, receiver=sender_profile)).order_by('timestamp')

    # Mark messages as read
    unread_messages = messages.filter(receiver=request.user.profile, is_read=False)
    unread_messages.update(is_read=True, read_at=timezone.now())

    context = {
        'sender_profile': sender_profile,
        'receiver_profile': receiver_profile,
        'messages': messages,
    }

    return render(request, 'usuario/message_view.html', context)

@login_required
@sensitive_post_parameters()
def message_json(request, username):
    try:
        sender_profile = request.user.profile
        receiver_profile = get_object_or_404(Profile, user__username=username) #Profile.objects.get(user__username=username)

        # Retrieve messages for the current sender and receiver
        messages = Message.objects.filter(Q(sender=sender_profile, receiver=receiver_profile) | Q(sender=receiver_profile, receiver=sender_profile)).order_by('timestamp')

        # Mark messages as read
        unread_messages = messages.filter(receiver=request.user.profile, is_read=False)
        unread_messages.update(is_read=True, read_at=timezone.now())

        # Create a list with the messages data
        messages_list = []
        for message in messages:
            message_data = {
                'sender': message.sender.user.username,
                'receiver': message.receiver.user.username,
                'is_online': message.sender.is_online,
                'content': message.content,
                'timestamp': message.timestamp.strftime("%I:%M %p").lower(),
                'is_read': message.is_read,
                'read_at': message.read_at.strftime("%I:%M %p").lower() if message.read_at is not None else None,
            }
            messages_list.append(message_data)

        # Return the messages data in JSON format 
        return JsonResponse(messages_list, safe=False)
    except Profile.DoesNotExist:
        raise Http404("El perfil no existe")

from django.contrib.auth import update_session_auth_hash

@login_required
def change_password(request):
    if request.method == 'POST':
        form = CustomPasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            # Para mantener la sesión del usuario después de cambiar su contraseña
            auth.update_session_auth_hash(request, user)
            return redirect('home')
    else:
        form = CustomPasswordChangeForm(user=request.user)
        
    return render(request, 'usuario/cambio.html', {'form': form})

def error_404(request, exception):
    return render(request, '404.html', status=404)