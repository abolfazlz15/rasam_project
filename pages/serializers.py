from rest_framework import serializers

from pages.models import ContactUs
from utils.date_conversion.utils import jajali_converter


class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        exclude = ('created_at', 'is_check')