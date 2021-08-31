from django.db.models import fields
from contacts.models import Contact
from rest_framework import serializers


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = [
            'country_code',
            'id',
            'first_name',
            'last_name',
            'phone_number',
            'contact_picture',
            'is_favorite'
            ]
