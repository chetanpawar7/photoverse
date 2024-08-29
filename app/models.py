from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    profile_pic = models.CharField(blank=True, null=True)


class BaseModel(models.Model):
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class ImageMaster(BaseModel):
    title = models.CharField(max_length=255)
    image_path = models.CharField(max_length=1024)  # S3 URL

    class Meta:
        db_table = "image_master"


class PostMaster(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    image_path = models.CharField()  # S3 URL for the post image

    class Meta:
        db_table = "post_master"


class LikeMaster(BaseModel):
    post = models.ForeignKey(PostMaster, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')

    class Meta:
        db_table = "like_master"


class ShareMaster(BaseModel):
    post = models.ForeignKey(PostMaster, on_delete=models.CASCADE, related_name='shares')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='shares')

    class Meta:
        db_table = "share_master"


class CommentMaster(BaseModel):
    post = models.ForeignKey(PostMaster, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField()

    class Meta:
        db_table = "comment_master"


class Tag(BaseModel):
    name = models.CharField(max_length=50, unique=True)
    posts = models.ManyToManyField(PostMaster, related_name='tags')

    class Meta:
        db_table = "tag_master"
