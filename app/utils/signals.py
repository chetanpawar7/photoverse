# myapp/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from app.models import PostMaster, ImageMaster

@receiver(post_save, sender=PostMaster)
def create_image_master(sender, instance, created, **kwargs):
    if created and instance.image_path:
        ImageMaster.objects.create(
            title=instance.title,
            image_path=instance.image_path
        )
