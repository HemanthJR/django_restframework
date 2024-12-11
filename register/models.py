from django.contrib.auth.models import AbstractUser 
from django.db import models
from django.conf import settings

class CustomUser(AbstractUser): 
    STUDENT = 'student' 
    TUTOR = 'tutor' 
    ADMIN = 'admin' 
    ROLE_CHOICES = [ 
        (STUDENT, 'Student'), 
        (TUTOR, 'Tutor'), 
        (ADMIN, 'Admin'), 
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default=STUDENT)
    email = models.EmailField(unique=True)
    dob = models.DateField(null=True, blank=True) 
    mobile = models.CharField(max_length=15, null=True, blank=True) 

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def save(self, *args, **kwargs): 
        if self.is_superuser: 
            self.role = self.ADMIN 
            super().save(*args, **kwargs)

    def __str__(self): 
        return self.email

class StudentDetails(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # fullname = models.CharField(max_length=100, null=False)
    # email = models.EmailField(unique=True, null=False)
    # mobile = models.CharField(max_length=15, null=False, blank=True)
    age = models.IntegerField(null=True)
    city = models.CharField(max_length=225, null=False)
    occupation = models.CharField(max_length=50, choices=[
        ('student','student'),
        ('working_professional', 'working professional'),
        ('freelancer', 'freelancer'),
        ('others','others' )
    ])
    institute_name = models.CharField(max_length=255, null=True, blank=True)
    interest = models.CharField(max_length=255, null=True, blank=True)
    worked_in_ai_ml = models.BooleanField()
    ai_experience_details = models.TextField(null=True, blank=True)
    excited_to_learn = models.JSONField(default=list)
    session_timing = models.CharField(max_length=50, choices=[ 
        ('morning', 'Morning (9:00 AM - 12:30 PM)'), 
        ('afternoon', 'Afternoon (1:30 PM - 5:30 PM)'), 
        ('full_day', 'Full Day (9:00 AM - 5:30 PM)'), ], null=True, blank=True)
    payment_proof = models.CharField(max_length=5000, null=False)
    agreement = models.BooleanField()

    def __str__(self):
        return self.user.email
    