
from django.core.files.storage import default_storage
from django.shortcuts import render

def upload_view(request):
    avatar_url = None

    if request.method == 'POST' and request.FILES.get('avatar'):
        avatar = request.FILES['avatar']
        path = default_storage.save('avatars/' + avatar.name, avatar)
        avatar_url = default_storage.url(path)

    return render(request, 'core/upload.html', {'avatar_url': avatar_url})

