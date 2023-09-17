from django.db import models
from utils.date_conversion.utils import jajali_converter

from django.utils.translation import gettext as _


class ContactUs(models.Model):
    title = models.CharField(max_length=155, verbose_name=_('موضوع'))
    email = models.EmailField(max_length=255, verbose_name=_('ایمیل'))
    text = models.TextField(verbose_name=_('متن'))
    is_check = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('تاریخ ایجاد'))

    def __str__(self):
        return f'{self.email} - {self.title}'
    
    def get_jalali_date(self):
        return jajali_converter(self.created_at)
    get_jalali_date.short_description = 'تاریخ عضویت'