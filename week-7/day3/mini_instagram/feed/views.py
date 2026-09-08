from django.contrib import messages
from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404, redirect, render

from .models import Post

# Requirement 3: accept only these extensions
ALLOWED_EXTENSIONS = ('jpg', 'jpeg', 'png')


def _has_allowed_extension(filename):
    return filename.lower().rsplit('.', 1)[-1] in ALLOWED_EXTENSIONS if '.' in filename else False


def feed(request):
    """
    Requirement 5/6: show all posts on one feed page, each with
    username, image, description, and likes.
    Requirement 4: handle uploads via multipart/form-data + request.FILES.
    """
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        description = request.POST.get('description', '').strip()
        image = request.FILES.get('image')  # requirement 4: request.FILES

        if not username:
            messages.error(request, 'Username is required.')
        elif not image:
            messages.error(request, 'Please choose an image to upload.')
        elif not _has_allowed_extension(image.name):
            # Requirement 3: reject anything that isn't jpg/jpeg/png
            messages.error(
                request,
                f'"{image.name}" was rejected. Only .jpg, .jpeg, and .png files are allowed.',
            )
        else:
            post = Post(username=username, description=description, image=image)
            try:
                post.full_clean()  # re-checks the model's FileExtensionValidator too
                post.save()
                messages.success(request, 'Post uploaded successfully!')
            except ValidationError as e:
                messages.error(request, ' '.join(sum(e.message_dict.values(), [])))

        return redirect('feed')

    posts = Post.objects.all()
    return render(request, 'feed/feed.html', {'posts': posts})


def like_post(request, post_id):
    """Requirement 7: Like button increases likes by 1."""
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        post.likes += 1
        post.save(update_fields=['likes'])
    return redirect('feed')
