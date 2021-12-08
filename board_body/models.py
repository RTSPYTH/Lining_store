from django.db import models



class Post(models.Model):
    image = models.ImageField(upload_to='post_images')
    name = models.CharField(max_length=100)
    description = models.TextField()
    availability = models.CharField(max_length=100)
    price = models.IntegerField()
    categories = models.ManyToManyField('Categories', related_name='cate_post')
    created_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'


class Categories(models.Model):
    cate = models.CharField(max_length=100)
    parent = models.ForeignKey('Categories', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.cate}'


class Stock(models.Model):
    image = models.ImageField(upload_to='post_images')
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=100)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title}'







