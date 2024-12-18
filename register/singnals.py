from django.db.models.signals import post_save 
from django.dispatch import receiver 
from .models import *

@receiver(post_save, sender=CustomUser)
def create_or_update_student_profile(sender, instance, created, **kwargs):
    if created and instance.role == 'student':
        StudentDetails.objects.create(user=instance)
    elif instance.role == 'student': 
        instance.student_profile.save()