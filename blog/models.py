import os
import uuid

from accounts.models import User
from django.db import models
from django.utils.html import format_html
from django.utils.translation import gettext as _


def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = '%s.%s' % (uuid.uuid4(), ext)
    return os.path.join('article/post', filename)


class Tag(models.Model):
    title = models.CharField(max_length=255, verbose_name=_('عنوان'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('تاریخ ایجاد'))

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name=_('عنوان'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('تاریخ ایجاد'))

    def __str__(self):
        return self.title


class Article(models.Model):
    title = models.CharField(max_length=255, verbose_name=_('عنوان'))
    text = models.TextField(verbose_name=_('توضیحات'))
    image = models.ImageField(blank=True, null=True, upload_to=get_file_path, verbose_name=_('تصویر'))
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='article', verbose_name=_('نویسنده'))
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True, related_name='articles', verbose_name=_('دسته بندی'))
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, null=True, blank=True, related_name='articles', verbose_name=_('تگ'))
    status = models.BooleanField(default=False, verbose_name=_('وضعیت'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('تاریخ ایجاد'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('اخرین بروزرسانی'))



    def __str__(self):
        return f'{self.title} - {self.text[:20]}'

    def showImage(self):
        # show image in admin panel
        if self.image:
            return format_html(f'<img src="{self.image.url}" alt="" width="50px" height="50px">')
        else:
            return format_html('no image')
    showImage.short_description = 'image'
