from django.db import models
from django.contrib.auth.models import User


class UploadImage(models.Model):
    caption = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images')


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=200, null=True)
    slug = models.SlugField(null=True, unique=True)
    description = models.CharField(
        max_length=500, null=True, blank=True, verbose_name='Description')

    class Meta:
        verbose_name_plural = 'Category'

    def __str__(self):
        return str(self.name)


class Blog(models.Model):
    status = (
        ('active', 'active'),
        ('pending', 'pending')
    )

    title = models.CharField(max_length=200, null=True)
    slug = models.SlugField(max_length=200, unique=True)
    detail = models.TextField(max_length=2000, null=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    #catagories = models.ManyToManyField(Category)
    catagories = models.ForeignKey(
        Category, on_delete=models.DO_NOTHING, null=True)
    tags = models.ManyToManyField(Tag, blank=True)
    status = models.CharField(max_length=20, choices=status, default='pending')
    #show_hide = models.CharField(max_length=5,choices=visibility, default='show')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    featured = models.BooleanField(default=False)
    visit_count = models.IntegerField(default=0)
    visible = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Blog'

    def overview(self):
        short = self.detail[:30]
        return short

    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url

    def __str__(self):
        return f"{ self.title} | { self.author.username} | { self.catagories} | { self.status}"


class Comment(models.Model):
    post = models.ForeignKey(
        Blog, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100, null=True, blank=False)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.post.title} | {self.name } "


class Reply(models.Model):
    comment = models.ForeignKey(
        Comment, on_delete=models.CASCADE, related_name='reply')
    name = models.CharField(max_length=200, null=True, blank=False)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.comment} | { self.name } |{ self.created_at }"
