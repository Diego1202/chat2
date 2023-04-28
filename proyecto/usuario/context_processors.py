from django.utils.translation import gettext as _
from django.http import JsonResponse
from usuario.models import Profile
from django.utils.timesince import timesince
from datetime import timedelta
from django.utils import timezone


def all_profiles(request):
    if request.user.is_authenticated:
        profile = Profile.objects.exclude(user=request.user)
    else:
        profile = Profile.objects.all()
    return  {'all_profiles': profile}

def profiles_with_messages(request):
    profiles = Profile.objects.all()
    profiles_data = []
    for profile in profiles:
        if profile.user.id != request.user.id:
            data = {
                'username': profile.user.username,
                'is_online': profile.is_online,
                'last_logout': tiempo_transcurrido(profile.last_logout),
                'has_unread_messages': profile.sender_messages.filter(is_read=False).exists(),
                'count': profile.sender_messages.filter(is_read=False).count(),
            }
            profiles_data.append(data)
    return JsonResponse({'profiles': profiles_data})

def tiempo_transcurrido(fecha):
    if fecha is None:
        return _("Activo nunca")

    ahora = timezone.now()
    diferencia = (ahora - fecha)
    if diferencia <= timedelta(minutes=1):
        return _("Activo hace unos segundos")
    elif diferencia <= timedelta(hours=1):
        minutos = round(diferencia.seconds / 60)
        if minutos == 1:
            return _("Activo hace un minuto")
        else:
            return _("Activo hace {} minutos").format(minutos)
    elif diferencia <= timedelta(days=1):
        horas = round(diferencia.seconds / 3600)
        if horas == 1:
            return _("Activo hace una hora")
        else:
            return _("Activo hace {} horas").format(horas)
    else:
        dias = diferencia.days
        if dias == 1:
            return _("Activo hace un día")
        else:
            return _("Activo hace {} días").format(dias)