from django.db import models
from django.core.urlresolvers import reverse
from time import time

def get_upload_file(instance,filename):
    return "uploaded_files/%s_%s" % (str(time()).replace('.','_'),filename)


class Category(models.Model):
    name = models.CharField(max_length=200,db_index=True)
    slug = models.SlugField(max_length=200,db_index=True,unique=True)
    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_absolute_url(self):
        return reverse('eshop:product_list_by_category',args=[self.slug])

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products')
    name = models.CharField(max_length=200, db_index=True)
    location = models.TextField(blank=True)
    basin = models.TextField(blank=True)
    deposition = models.TextField(blank=True)
    summary=models.TextField(blank=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d',blank=True)
    image1 = models.ImageField(upload_to='products/%Y/%m/%d',blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    thumbnail=models.FileField(upload_to=get_upload_file,blank=False)



    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('eshop:product_detail',args=[self.id, self.slug])

class Comment(models.Model):
        product = models.ForeignKey(Product, related_name='comments')
        name = models.CharField(max_length=80)
        email = models.EmailField()
        body = models.TextField()
        created = models.DateTimeField(auto_now_add=True)
        updated = models.DateTimeField(auto_now=True)
        active = models.BooleanField(default=True)



        class Meta:
            ordering = ('created',)
            index_together = (('id',),)



        def __str__(self):
            return 'Comment by {} on {}'.format(self.name, self.product)
