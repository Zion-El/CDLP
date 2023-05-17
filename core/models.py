from django.contrib.auth.models import AbstractUser, AbstractBaseUser, PermissionsMixin, UserManager
from django.db import models
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

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
manager_role_choices = (
    ('yes', 'yes'), 
    ('no','no')
)
# Create your models here.


class CustomAbstractUser(AbstractBaseUser, PermissionsMixin):
    """
    An abstract base class implementing a fully featured User model with
    admin-compliant permissions.

    Username and password are required. Other fields are optional.
    """

    username_validator = UnicodeUsernameValidator()
    last_login = None

    username = models.CharField(
        _("username"),
        max_length=150,
        unique=True,
        help_text=_(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        validators=[username_validator],
        error_messages={
            "unique": _("A user with that username already exists."),
        },
    )
    firstname = models.CharField(_("first name"), max_length=150, blank=True)
    lastname = models.CharField(_("last name"), max_length=150, blank=True)
    email = models.EmailField(_("email address"), blank=True, unique=True)
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    whenjoined = models.DateTimeField(_("date joined"), default=timezone.now)

    objects = UserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")
        abstract = True

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self):
        """
        Return the firstname plus the lastname, with a space in between.
        """
        full_name = "%s %s" % (self.firstname, self.lastname)
        return full_name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.firstname



class Member(CustomAbstractUser):
    userid = models.BigAutoField(primary_key=True)
    user_code = models.CharField(unique=True, max_length=255, blank=True, null=True)
    salt = models.CharField(max_length=150, blank=True, null=True)
    sex = models.CharField(max_length=6, blank=True, null=True, choices=sex)
    phone = models.CharField(max_length=15, blank=True, null=True)
    street = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    user_type = models.IntegerField(default=0)
    r_id = models.IntegerField(default=0)
    secret_question1 = models.CharField(max_length=250, blank=True, null=True)
    secret_question2 = models.CharField(max_length=250, blank=True, null=True)
    secret_answer1 = models.CharField(max_length=100, blank=True, null=True)
    secret_answer2 = models.CharField(max_length=100, blank=True, null=True)
    email_confirm = models.BooleanField(default=False)
    phone_confirm = models.BooleanField(default=False)
    confirmed = models.BooleanField(default=False)
    aff_id = models.CharField(unique=True, max_length=32, blank=True, null=True)
    ref_id = models.CharField(max_length=32, blank=True, null=True)
    findus = models.CharField(max_length=32, blank=True, null=True)
    regip = models.CharField(db_column='regIP', max_length=15, blank=True, null=True)  # Field name made lowercase.
    api_key = models.CharField(unique=True, max_length=500, blank=True, null=True)
    api_active = models.BooleanField(default=True)
    api_ip_access_list = models.TextField(blank=True, null=True)
    noofvisits = models.IntegerField(default=0)
    pw_change = models.IntegerField(default=0)
    lastvisitdate = models.DateTimeField(_("last login"), blank=True, null=True)
    alert_date = models.DateTimeField(default=timezone.now)
    whenedited = models.DateTimeField(auto_now=True)
    toured = models.IntegerField(default=0)
    access_status = models.CharField(max_length=3, db_comment='This is the platform access status')
    pg_access = models.CharField(max_length=3, db_comment='This is the payment gateway access status')
    pg_limit = models.DecimalField(max_digits=11, decimal_places=2, default=0, db_comment='This is the payment gateway payment amount limit per user')
    manager_role = models.CharField(max_length=3, blank=True, null=True)
    bvn_no = models.CharField(max_length=15, blank=True, null=True, db_comment="Nigeria's bank verification number")
    firebase_unique_id = models.CharField(max_length=255, blank=True, null=True, db_comment='This is the individual app unique id use for push notifications')
    block_funds = models.DecimalField(max_digits=11, decimal_places=2, default=0)
    dedicated_account_number = models.CharField(unique=True, max_length=10, blank=True, null=True)
    name_verification_info = models.TextField(blank=True, null=True)
    bank_account_info = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'members'
    
    def __str__(self):
        return self.username
    
    




# class APIModel(models.Model):
#     api_key = models.CharField(max_length=50)
#     referral_code = models.CharField(max_length=6)
#     user = models.OneToOneField(Members, on_delete=models.CASCADE)
#     create_at = models.DateTimeField(auto_now_add=True)


#     def __str__(self):
#         return self.user.username