from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import MoringaMerch

class MerchSerializer(serializers.ModelSerializer):
  class Meta:
    model = MoringaMerch
    fields = ('id','name','description','price')