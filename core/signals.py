import random
import uuid
from hashlib import sha256

from django.contrib.auth.signals import user_logged_in
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

from .models import Member


@receiver(post_save, sender=Member)
def generate_api_key_and_referral_code(sender, instance, created, **kwargs):
    if created:
        # Generate a unique API key
        api_key = uuid.uuid4().hex
        # Hash the API key
        hashed_api_key = sha256(api_key.encode()).hexdigest()
        # Generate a referral code
        referral_code = generate_referral_code()
        # Create an APIModel instance for the new user
        # APIModel.objects.create(user=instance, api_key=hashed_api_key, referral_code=referral_code)
        instance.api_key = hashed_api_key
        instance.save()

def generate_referral_code():
    # Generate a random 6-character alphanumeric referral code
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    referral_code = ''.join(random.choice(chars) for _ in range(6))
    return referral_code


@receiver(user_logged_in)
def update_user_log_in(sender, user, **kwargs):
    """
    Custom signal receiver to update the last_login date for
    the user logging in.
    """
    user.lastvisitdate = timezone.now()
    user.noofvisits += 1
    user.save() 
    print("i got here")
    