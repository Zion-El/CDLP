from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.core.validators import MinValueValidator
from django.db import models, transaction


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


class CustomUserManager(UserManager):
    def get_by_natural_key(self, username):
        case_insensitive_username_field = "{}__iexact".format(self.model.USERNAME_FIELD)
        return self.get(**{case_insensitive_username_field: username})

# Create your models here.
class Members(AbstractUser):
    objects = CustomUserManager()
    UserId = models.CharField(max_length=10, null=True)
    UserCode = models.CharField(max_length=200, null=True)
    r_id = models.CharField(max_length=200, null=True)
    email = models.EmailField()
    FirstName = models.CharField(max_length=200, null=True)
    LastName = models.CharField(max_length=200, null=True)
    Address = models.CharField(max_length=500, null=True)
    BankName = models.CharField(max_length=100, choices=Bank, blank=True)
    AccountNumber = models.CharField(max_length=40, blank=True)
    Phone = models.CharField(max_length=30, blank=True)
    AccountName = models.CharField(max_length=200, blank=True)
    Account_Balance = models.FloatField(default=0.00, null=True, validators=[MinValueValidator(0.0)],)
    Password = models.CharField(null=True, blank=True, max_length=10)
    Salt = models.CharField(max_length=200, null=True)
    Secret_Question_1 = models.CharField(max_length=200, null=True)
    Secret_Question_2 = models.CharField(max_length=200, null=True)
    Secret_Answer_1 = models.CharField(max_length=200, null=True)
    Secret_Answer_2 = models.CharField(max_length=200, null=True)
    ref_id = models.CharField(max_length=50, blank=True, null=True)
    Confirm = models.CharField(max_length=100, null=True,)
    Email_confirmed = models.CharField(max_length=100, null=True,)
    Phone_Confirmed = models.CharField(max_length=100, null=True,)
    Api_key = models.CharField(max_length=100, null=True,)
    api_active = models.CharField(max_length=100, null=True,)
    alert_date = models.DateTimeField()
    when_joined = models.DateTimeField()
    when_edited = models.DateTimeField()
    toured = models.CharField(max_length=100, null=True,) 
    access_status = models.CharField(max_length=100, null=True,)
    pg_access = models.CharField(max_length=100, null=True,)
    pg_limit = models.CharField(max_length=100, null=True,)
    manager_role = models.CharField(max_length=100, null=True,)
    firebase_unique_id = models.CharField(max_length=100, null=True,)
    block_funds = models.CharField(max_length=100, null=True,)
    name_verification_info = models.CharField(max_length=100, null=True,)
    api_ip_access_list = models.CharField(max_length=100, null=True,)
    no_of_visits = models.CharField(max_length=100, null=True,)
    last_visit_date = models.CharField(max_length=100, null=True,)
    pw_change = models.CharField(max_length=100, null=True,)
    RegIp = models.TextField(max_length=100, null=True,)
    FindUs = models.CharField(max_length=100, null=True,)
    first_payment = models.BooleanField(default=False)
    Referer_Bonus = models.FloatField(default=0.00, null=True, validators=[MinValueValidator(0.0)],)
    user_type = models.CharField(max_length=30, choices=user_type, default="Smart Earner", null=True)
    dedicatedaccountNumber = models.CharField(max_length=100, blank=True, null=True)
    reservedbankName = models.CharField(max_length=100, blank=True, null=True)
    reservedaccountReference = models.CharField(max_length=100, blank=True, null=True)
    Bonus = models.FloatField(default=0.00, null=True, validators=[MinValueValidator(0.0)],)
    DOB = models.DateField(null=True, blank=True,)
    Sex = models.CharField(max_length=6, null=True,)
    State = models.CharField(max_length=100, null=True,)
    City = models.CharField(max_length=200, null=True)
    Country = models.CharField(max_length=200, null=True)
    Local_gov_of_origin = models.CharField(max_length=100, null=True,)
    BVN = models.CharField(max_length=50, null=True,)
    passport_photogragh = models.ImageField(upload_to="passport_images", null=True, help_text="Maximum of 50kb in size")
    accounts = models.TextField(blank=True, null=True)
    

    def __str__(self):
        return self.username

    # def f_account(self):
    #     try:
    #         return json.loads(self.accounts)
    #     except:
    #         return {"accounts": []}

    # def passport(self):
    #     if self.passport_photogragh:
    #         return "https://www.legitdata.com.ngmedia/%s" % (self.passport_photogragh)
    #     else:
    #         return "https://png.pngtree.com/png-vector/20190704/ourmid/pngtree-businessman-user-avatar-free-vector-png-image_1538405.jpg"



    # def image_tag(self):
    #     from django.utils.html import mark_safe

    #     return mark_safe(
    #         '<img src="https://www.legitdata.com.ngmedia/%s" width="150" height="150" />'
    #         % (self.passport_photogragh)
    #     )

    # image_tag.short_description = "Image"

    # def walletb(self):
    #     return str(round(self.Account_Balance))

    # def bonusb(self):
    #     return str(round(self.Referer_Bonus))

    # def ref_deposit(self, amount):
    #     self.Referer_Bonus += amount
    #     self.Referer_Bonus = round(self.Referer_Bonus, 2)
    #     self.save()

    # def ref_withdraw(self, amount):
    #     if self.self.Referer_Bonus > amount or amount < 0:
    #         return False
    #     self.Referer_Bonus -= amount
    #     self.Referer_Bonus = round(self.Referer_Bonus, 2)
    #     self.save()

    # @classmethod
    # def withdraw(cls, id, amount):
    #     with transaction.atomic():
    #         account = cls.objects.select_for_update().get(id=id)
    #         # print(account)
    #         balance_before = account.Account_Balance
    #         if account.Account_Balance < amount or amount < 0:
    #             return False
    #         account.Account_Balance -= amount
    #         account.save()

    #     try:
    #         Transactions.objects.create(
    #             user=CustomUser.objects.get(id=id),
    #             transaction_type="DEBIT",
    #             balance_before=balance_before,
    #             balance_after=balance_before - amount,
    #             amount=amount,
    #         )

    #     except:
    #         pass

    # @classmethod
    # def deposit(cls, id, amount, transfer=False, medium="NONE"):
    #     with transaction.atomic():
    #         account = cls.objects.select_for_update().get(id=id)
    #         # if transfer == False:
    #         #     if account.referer_username:
    #         #         if CustomUser.objects.filter(username__iexact=account.referer_username).exists():
    #         #             if account.first_payment == False:
    #         #                 referer = CustomUser.objects.get(
    #         #                     username__iexact=account.referer_username)
    #         #                 if amount >= 5000:
    #         #                     referer.ref_deposit(100)
    #         #                     account.first_payment = True
    #         #                 else:
    #         #                     referer.ref_deposit((0.05*amount))
    #         #                     account.first_payment = True

    #         balance_before = account.Account_Balance
    #         if medium != "NONE":
    #             if ChargeUser.objects.filter(username=account.username).exists():
    #                 pending_charge = ChargeUser.objects.filter(
    #                     username=account.username
    #                 ).last()
    #                 if pending_charge.pending_amount > 0:
    #                     if amount > pending_charge.pending_amount:
    #                         amt = amount - pending_charge.pending_amount
    #                         balance_before = account.Account_Balance
    #                         pending_charge.balance_before = balance_before
    #                         account.Account_Balance += amt
    #                         account.save()

    #                         try:
    #                             WalletSummary.objects.create(
    #                                 user=account,
    #                                 product=f"N{pending_charge.pending_amount} pending wallet charge paid",
    #                                 amount=amount,
    #                                 previous_balance=balance_before,
    #                                 after_balance=balance_before + amount,
    #                             )
    #                         except:
    #                             pass
    #                         pending_charge.comment = f"N{pending_charge.pending_amount} pending wallet charge paid"
    #                         pending_charge.balance_after = amt
    #                         pending_charge.pending_amount = 0
    #                         pending_charge.save()

    #                     else:
    #                         balance_before = account.Account_Balance
    #                         pending_charge.balance_before = balance_before
    #                         amt = pending_charge.pending_amount - amount
    #                         pending_charge.comment = f"N{amount} paid from  pending wallet charge, pending amount remain {amount} "
    #                         pending_charge.pending_amount = amt
    #                         pending_charge.balance_after = 0
    #                         pending_charge.save()

    #                 else:
    #                     account.Account_Balance += amount
    #                     account.save()
    #             else:
    #                 account.Account_Balance += amount
    #                 account.save()

    #         try:
    #             Transactions.objects.create(
    #                 user=CustomUser.objects.get(id=id),
    #                 transaction_type="CREDIT",
    #                 balance_before=balance_before,
    #                 balance_after=balance_before + amount,
    #                 amount=amount,
    #             )

    #         except:
    #             pass

    #         try:
    #             WalletFunding.objects.create(
    #                 user=CustomUser.objects.get(id=id),
    #                 medium=medium,
    #                 previous_balance=balance_before,
    #                 after_balance=balance_before + amount,
    #                 amount=amount,
    #             )

    #         except:
    #             pass

    #     return account

    # def ref_withdraw(self, amount):
    #     if self.Referer_Bonus > 0.0:
    #         self.Referer_Bonus -= amount
    #         self.Referer_Bonus = round(self.Referer_Bonus, 2)
    #         self.save()

    class Meta:
        verbose_name_plural = "USERS MANAGEMENT"
