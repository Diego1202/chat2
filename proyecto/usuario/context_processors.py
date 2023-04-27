# en un archivo llamado `context_processors.py`

from usuario.models import Profile

def all_profiles(request):
    if request.user.is_authenticated:
        profile = Profile.objects.exclude(user=request.user)
    else:
        profile = Profile.objects.all()
    return  {'all_profiles': profile}
