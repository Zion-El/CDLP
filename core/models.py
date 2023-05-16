from django.db import models
from django.contrib.auth.models import AbstractUser



# from users.models import User


# USER BANKS
Bank = (
    ("Access Bank", "Access Bank"),
    ("Access(Diamond) Bank", "Access (Diamond) Bank"),
    ("ECO Bank", "ECO Bank"),
    ("First Bank of Nigeria", "First Bank of Nigeria"),
    ("FCMBank", "FCMBank"),
    ("FIdelity Bank", "FIdelity Bank"),
    ("GTBank", "GTBank"),
    ("Heritage Bank", "Heritage Bank"),
    ("Kuda Bank", "Kuda Bank"),
    ("Opay", "Opay"),
    ("Palmpay", "Palmpay"),
    ("Polarise Bank", "Polarise Bank"),
    ("Stanbic IBTC", "Stanbic IBTC"),
    ("Sterling Bank", "Sterling Bank"),
    ("UBA", "UBA"),
    ("Union Bank", "Union Bank"),
    ("Unity Bank", "Unity Bank"),
    ("Wema Bank", "Wema Bank"),
    ("Zenith Bank", "Zenith Bank"),
)

# USER TYPE
user_type = (
    ("Smart Earner", "Smart Earner"),
    ("Affilliate", "Affilliate"),
    ("TopUser", "TopUser"),
    ("API", "API"),
)

sex = (
    ('M', 'male'),
    ('F','female')
)
# Create your models here.
class Member(AbstractUser):
    UserCode = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=100, unique=True) 
    salt = models.CharField(max_length=200, null=True)
    sex = models.CharField(choices=sex,  max_length=6, null=True,)
    phone = models.CharField(max_length=30, blank=True)
    Street = models.CharField(max_length=100, null=True,)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=100, null=True,)
    country = models.CharField(max_length=200, null=True)
    DOB = models.DateField(null=True, blank=True,)
    user_type = models.CharField(max_length=30, choices=user_type, default="Smart Earner", null=True)
    r_id = models.CharField(max_length=200, null=True)
    Secret_Question_1 = models.CharField(max_length=200, null=True)
    Secret_Question_2 = models.CharField(max_length=200, null=True)
    Secret_Answer_1 = models.CharField(max_length=200, null=True)
    Secret_Answer_2 = models.CharField(max_length=200, null=True)
    Email_confirmed = models.CharField(max_length=100, null=True,)
    Phone_Confirmed = models.CharField(max_length=100, null=True,)
    Confirm = models.CharField(max_length=100, null=True,)
    aff_id = models.CharField(max_length=50, blank=True, null=True)
    ref_id = models.CharField(max_length=30, blank=True, null=True)
    FindUs = models.CharField(max_length=100, null=True,)
    RegIp = models.TextField(max_length=100, null=True,)
    Api_key = models.CharField(max_length=100, null=True,)
    api_active = models.CharField(max_length=100, null=True,)
    api_ip_access_list = models.CharField(max_length=50, blank=True, null=True)
    no_of_visits = models.CharField(max_length=100, null=True,)
    last_visit_date = models.CharField(max_length=100, null=True,)
    alert_date = models.DateTimeField(auto_now=True)
    when_joined = models.DateTimeField(auto_now_add=True)
    when_edited = models.DateTimeField(auto_now=True)
    toured = models.CharField(max_length=10, null=True,) 
    access_status = models.CharField(max_length=10, null=True,)
    pg_access = models.CharField(max_length=100, null=True,)
    pg_limit = models.CharField(max_length=100, null=True,)
    manager_role = models.CharField(max_length=100, null=True,)
    BVN = models.CharField(max_length=50, null=True,)
    firebase_unique_id = models.CharField(max_length=100, null=True,)
    block_funds = models.CharField(max_length=100, null=True,)
    dedicatedaccountNumber = models.CharField(max_length=100, blank=True, null=True)
    name_verification_info = models.CharField(max_length=100, null=True,)
    bank_account_info = models.CharField(max_length=200, blank=True)
    

    def __str__(self):
        return self.username


class APIModel(models.Model):
    api_key = models.CharField(max_length=50)
    referral_code = models.CharField(max_length=6)
    user = models.OneToOneField(Member, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.user.username