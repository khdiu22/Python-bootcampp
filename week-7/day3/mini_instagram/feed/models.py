from django.core.validators import FileExtensionValidator
from django.db import models


def post_image_path(instance, filename):
    """Requirement 2: store all uploaded images under media/posts/."""
    return f'posts/{filename}'


class Post(models.Model):
    # Requirement 1: username, description, image, likes
    username = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    image = models.ImageField(
        upload_to=post_image_path,
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])],
    )
    likes = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.username}: {self.description[:30]}'
