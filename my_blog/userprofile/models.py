from django.db import models
from django.contrib.auth.models import User

# import django built in signal
from django.db.models.signals import post_save
# import signal receiver's decorator
from django.dispatch import receiver

