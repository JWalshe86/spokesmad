from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    short_description = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    activity = models.CharField(max_length=255)
    image = models.ImageField(upload_to='post_images/')
    images = models.ManyToManyField('Image', blank=True, related_name='posts')

    def __str__(self):
        return self.title

class Image(models.Model):
    post = models.ForeignKey(Post, related_name='images_set', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post_images/')
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.description

