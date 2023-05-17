# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from core.models import Member


class AirtimeToCash(models.Model):
    user = models.ForeignKey('Member', models.DO_NOTHING)
    network = models.CharField(max_length=11, blank=True, null=True)
    transfer_number = models.IntegerField(blank=True, null=True)
    airtime_amount = models.CharField(max_length=255, blank=True, null=True)
    payment_method = models.CharField(max_length=12, blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    bank_name = models.CharField(max_length=255, blank=True, null=True)
    account_number = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'airtime_to_cash'


class Api(models.Model):
    api_id = models.AutoField(primary_key=True)
    api_vendor_id = models.IntegerField()
    api_name = models.CharField(unique=True, max_length=255)
    api_system_code = models.CharField(unique=True, max_length=255)
    api_username = models.CharField(max_length=255)
    api_userid = models.CharField(max_length=255)
    api_password = models.CharField(max_length=500)
    api_key = models.CharField(max_length=500)
    api_date = models.DateTimeField()
    api_demo_public_key = models.CharField(max_length=2500, blank=True, null=True)
    api_demo_private_key = models.CharField(max_length=2500, blank=True, null=True)
    api_live_public_key = models.CharField(max_length=2500, blank=True, null=True)
    api_live_private_key = models.CharField(max_length=2500, blank=True, null=True)
    api_server_url = models.CharField(max_length=255, blank=True, null=True)
    api_route = models.IntegerField(blank=True, null=True)
    api_spctype = models.CharField(max_length=4, blank=True, null=True)
    main_port = models.IntegerField(blank=True, null=True)
    backup_port = models.IntegerField(blank=True, null=True)
    phone_number = models.IntegerField(blank=True, null=True)
    sim_id = models.IntegerField(blank=True, null=True)
    device_token = models.CharField(max_length=255, blank=True, null=True)
    firebase_token = models.CharField(max_length=255, blank=True, null=True)
    sim_pin = models.CharField(max_length=3)
    other_codes = models.CharField(max_length=255, blank=True, null=True)
    mode = models.IntegerField(blank=True, null=True)
    percent_charge = models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    charge_above_2500 = models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    charge_above_10000 = models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)

    class Meta:
        db_table = 'api'


class Autorenew(models.Model):
    autorenew_id = models.AutoField(primary_key=True)
    autorenew_service_id = models.IntegerField(blank=True, null=True)
    autorenew_service_name = models.CharField(max_length=255, blank=True, null=True)
    autorenew_service_amount = models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    autorenew_client_id = models.IntegerField(blank=True, null=True)
    autorenew_reseller_id = models.IntegerField(blank=True, null=True)
    autorenew_account = models.CharField(max_length=255, blank=True, null=True)
    autorenew_count_target = models.IntegerField(blank=True, null=True)
    autorenew_count = models.IntegerField(blank=True, null=True)
    autorenew_start_date = models.DateTimeField()
    autorenew_next_date = models.DateTimeField(blank=True, null=True)
    autorenew_end_date = models.DateTimeField(blank=True, null=True)
    autorenew_status = models.CharField(max_length=12, blank=True, null=True)
    autorenew_frequency = models.CharField(max_length=20, blank=True, null=True)
    autorenew_order_completed = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'autorenew'


class BillDeliveryLog(models.Model):
    bill_delivery_log_id = models.AutoField(primary_key=True)
    dsr_message_id_record = models.CharField(max_length=255)
    dsr_gateway_response = models.CharField(max_length=5000)
    dsr_date_created = models.DateTimeField()

    class Meta:
        db_table = 'bill_delivery_log'


class Bonus(models.Model):
    bonus_id = models.AutoField(primary_key=True)
    userid = models.OneToOneField('Member', models.DO_NOTHING, db_column='userid')
    r_id = models.IntegerField()
    amount = models.DecimalField(max_digits=11, decimal_places=2)
    date = models.DateTimeField()

    class Meta:
        db_table = 'bonus'


class BonusTransactions(models.Model):
    bt_id = models.AutoField(primary_key=True)
    bonus_id = models.IntegerField()
    userid = models.ForeignKey('Member', models.DO_NOTHING, db_column='userid')
    r_id = models.IntegerField()
    beneficiary = models.CharField(max_length=255)
    amount = models.CharField(max_length=50)
    after_balance = models.DecimalField(max_digits=11, decimal_places=2)
    date = models.DateTimeField()
    remarks = models.CharField(max_length=255)
    tran_type = models.CharField(max_length=14)
    status = models.CharField(max_length=11)
    process = models.CharField(max_length=20)
    txgateway = models.CharField(db_column='txGateway', max_length=100)  # Field name made lowercase.
    txgatewayresponse = models.CharField(db_column='txGatewayResponse', max_length=5000)  # Field name made lowercase.
    recharge_trans_id = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'bonus_transactions'


class ChangePasswordRequest(models.Model):
    cpr_id = models.AutoField(primary_key=True)
    userid = models.OneToOneField('Member', models.DO_NOTHING, db_column='userid')
    cprkey = models.CharField(db_column='cprKey', unique=True, max_length=128)  # Field name made lowercase.
    email = models.CharField(max_length=250)
    date_created = models.DateTimeField()

    class Meta:
        db_table = 'change_password_request'


class ClientLogo(models.Model):
    client_id = models.AutoField(primary_key=True)
    client_name = models.CharField(unique=True, max_length=50)
    client_logo = models.CharField(max_length=500)
    client_description = models.TextField()
    date_added = models.DateTimeField()

    class Meta:
        db_table = 'client_logo'


class ConfirmAltemail(models.Model):
    caemail_id = models.AutoField(db_column='cAEmail_id', primary_key=True)  # Field name made lowercase.
    userid = models.ForeignKey('Member', models.DO_NOTHING, db_column='userid')
    ckey = models.CharField(db_column='cKey', max_length=128)  # Field name made lowercase.
    email = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        db_table = 'confirm_altemail'


class ConfirmAltphone(models.Model):
    caphone_id = models.AutoField(db_column='cAPhone_id', primary_key=True)  # Field name made lowercase.
    userid = models.ForeignKey('Member', models.DO_NOTHING, db_column='userid')
    ckey = models.CharField(db_column='cKey', max_length=128)  # Field name made lowercase.
    phone = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        db_table = 'confirm_altphone'


class ConfirmEmail(models.Model):
    cemail_id = models.AutoField(db_column='cEmail_id', primary_key=True)  # Field name made lowercase.
    userid = models.OneToOneField('Member', models.DO_NOTHING, db_column='userid')
    ckey = models.CharField(db_column='cKey', unique=True, max_length=128)  # Field name made lowercase.
    email = models.CharField(max_length=250)

    class Meta:
        db_table = 'confirm_email'


class ConfirmPhone(models.Model):
    cphone_id = models.AutoField(db_column='cPhone_id', primary_key=True)  # Field name made lowercase.
    userid = models.ForeignKey('Member', models.DO_NOTHING, db_column='userid')
    ckey = models.CharField(db_column='cKey', unique=True, max_length=128)  # Field name made lowercase.
    phone = models.CharField(max_length=250)
    date_created = models.DateTimeField()

    class Meta:
        db_table = 'confirm_phone'


class DataVouchers(models.Model):
    vchid = models.AutoField(db_column='vchID', primary_key=True)  # Field name made lowercase.
    vchresellerid = models.IntegerField(db_column='vchResellerID')  # Field name made lowercase.
    vchclientid = models.IntegerField(db_column='vchClientID', blank=True, null=True)  # Field name made lowercase.
    vchcode = models.CharField(db_column='vchCode', max_length=50)  # Field name made lowercase.
    vchsoldstatus = models.CharField(db_column='vchSoldStatus', max_length=50)  # Field name made lowercase.
    vchusagestatus = models.CharField(db_column='vchUsageStatus', max_length=50)  # Field name made lowercase.
    vchunits = models.IntegerField(db_column='vchUnits')  # Field name made lowercase.
    vchdatecreated = models.DateTimeField(db_column='vchDateCreated')  # Field name made lowercase.
    vchdateused = models.DateTimeField(db_column='vchDateUsed', blank=True, null=True)  # Field name made lowercase.
    vchdatesold = models.DateTimeField(db_column='vchDateSold', blank=True, null=True)  # Field name made lowercase.
    vchtype = models.CharField(db_column='vchType', max_length=50)  # Field name made lowercase.
    data_response = models.TextField(blank=True, null=True)
    vchservicecode = models.CharField(db_column='vchServiceCode', max_length=50)  # Field name made lowercase.

    class Meta:
        db_table = 'data_vouchers'


class GoogleSentEmail(models.Model):
    subject = models.CharField(max_length=255)
    body = models.TextField()
    reciever = models.CharField(max_length=50)
    status = models.CharField(max_length=10)
    response_log = models.TextField()

    class Meta:
        db_table = 'google_sent_email'


class LienTransactions(models.Model):
    wt_id = models.AutoField(primary_key=True)
    wallet_id = models.IntegerField()
    userid = models.ForeignKey('Member', models.DO_NOTHING, db_column='userid')
    r_id = models.IntegerField()
    beneficiary = models.CharField(max_length=255)
    amount = models.CharField(max_length=50)
    after_balance = models.DecimalField(max_digits=11, decimal_places=2)
    date = models.DateTimeField()
    remarks = models.CharField(max_length=255)
    tran_type = models.CharField(max_length=14)
    status = models.CharField(max_length=11)
    process = models.CharField(max_length=20)
    txgateway = models.CharField(db_column='txGateway', max_length=100)  # Field name made lowercase.
    txgatewayresponse = models.TextField(db_column='txGatewayResponse')  # Field name made lowercase.

    class Meta:
        db_table = 'lien_transactions'


class LoginAttempts(models.Model):
    user = models.ForeignKey('Member', models.DO_NOTHING)
    time = models.CharField(max_length=30)

    class Meta:
        db_table = 'login_attempts'


class ManagerLog(models.Model):
    manager_id = models.IntegerField()
    action = models.CharField(max_length=255)
    request_data = models.CharField(max_length=255)
    user_details = models.CharField(max_length=255)

    class Meta:
        db_table = 'manager_log'




class Messages(models.Model):
    msgid = models.AutoField(primary_key=True)
    u = models.ForeignKey(Member, models.DO_NOTHING)
    r_id = models.IntegerField()
    senderid = models.CharField(max_length=20, db_collation='utf8_unicode_ci')
    recipients = models.TextField(db_collation='utf8_unicode_ci')
    message = models.TextField(db_collation='utf8_unicode_ci')
    schedule = models.DateTimeField(blank=True, null=True)
    delivered = models.DateTimeField()
    msgstatus = models.CharField(db_column='msgStatus', max_length=20, db_collation='utf8_unicode_ci')  # Field name made lowercase.
    dnd_status = models.CharField(max_length=1)
    dnd_resend_status = models.IntegerField()
    unitsused = models.DecimalField(db_column='unitsUsed', max_digits=10, decimal_places=2)  # Field name made lowercase.
    smscreated = models.DateTimeField(db_column='smsCreated')  # Field name made lowercase.
    channel = models.CharField(max_length=20, db_collation='utf8_unicode_ci')
    apidlvrid = models.CharField(db_column='apiDlvrID', max_length=255, db_collation='utf8_unicode_ci', blank=True, null=True)  # Field name made lowercase.
    dlvrid = models.CharField(db_column='dlvrID', max_length=255, db_collation='utf8_unicode_ci', blank=True, null=True)  # Field name made lowercase.
    apiresponse = models.TextField(db_column='apiResponse', db_collation='utf8_unicode_ci', blank=True, null=True)  # Field name made lowercase.
    dnd_resend_failed = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        db_table = 'messages'


class MessagesAchieve(models.Model):
    msgid = models.AutoField(primary_key=True)
    u_id = models.IntegerField()
    r_id = models.IntegerField()
    senderid = models.CharField(max_length=20, db_collation='utf8_unicode_ci')
    recipients = models.TextField(db_collation='utf8_unicode_ci')
    message = models.TextField(db_collation='utf8_unicode_ci')
    schedule = models.DateTimeField(blank=True, null=True)
    delivered = models.DateTimeField()
    msgstatus = models.CharField(db_column='msgStatus', max_length=20, db_collation='utf8_unicode_ci')  # Field name made lowercase.
    dnd_status = models.CharField(max_length=1)
    dnd_resend_status = models.IntegerField()
    unitsused = models.DecimalField(db_column='unitsUsed', max_digits=10, decimal_places=2)  # Field name made lowercase.
    smscreated = models.DateTimeField(db_column='smsCreated')  # Field name made lowercase.
    channel = models.CharField(max_length=20, db_collation='utf8_unicode_ci')
    apidlvrid = models.CharField(db_column='apiDlvrID', max_length=255, db_collation='utf8_unicode_ci', blank=True, null=True)  # Field name made lowercase.
    dlvrid = models.CharField(db_column='dlvrID', max_length=255, db_collation='utf8_unicode_ci', blank=True, null=True)  # Field name made lowercase.
    apiresponse = models.TextField(db_column='apiResponse', db_collation='utf8_unicode_ci', blank=True, null=True)  # Field name made lowercase.
    dnd_resend_failed = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        db_table = 'messages_achieve'


class MtnCgPins(models.Model):
    pin_id = models.AutoField(primary_key=True)
    pin_code = models.CharField(unique=True, max_length=10)
    pin_value = models.IntegerField()
    status = models.CharField(max_length=7)
    date_added = models.DateTimeField()
    date_used = models.DateTimeField()
    date_updated = models.DateTimeField()
    pin_user_id = models.IntegerField()
    pin_reseller_id = models.IntegerField()
    pin_purchase_user_id = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'mtn_cg_pins'


class Notifications(models.Model):
    notify_id = models.AutoField(primary_key=True)
    notify_title = models.CharField(max_length=255)
    notify_message = models.TextField()
    user_id = models.IntegerField()
    reseller_id = models.IntegerField()
    user_ids = models.JSONField()
    reseller_ids = models.JSONField()
    notify_type = models.CharField(max_length=13)
    nofity_date_start = models.DateTimeField()
    notify_date_end = models.DateTimeField()
    date_created = models.DateTimeField()
    date_updated = models.DateTimeField()

    class Meta:
        db_table = 'notifications'


class OnlineUsers(models.Model):
    online_user_id = models.AutoField(primary_key=True)
    session_id = models.CharField(max_length=150)
    user = models.ForeignKey(Member, models.DO_NOTHING)
    reseller_id = models.IntegerField()
    website = models.CharField(max_length=100)
    user_agent = models.CharField(max_length=5000)
    keep_alive = models.IntegerField()
    login_time = models.DateTimeField()
    login_expiry = models.DateTimeField()
    time_update = models.DateTimeField()

    class Meta:
        db_table = 'online_users'
        unique_together = (('session_id', 'user'),)


class OurDebtors(models.Model):
    creditid = models.AutoField(db_column='creditID', primary_key=True)  # Field name made lowercase.
    credit_user = models.ForeignKey(Member, models.DO_NOTHING)
    credit_reseller_id = models.IntegerField()
    credit_amount = models.DecimalField(max_digits=11, decimal_places=2)
    credit_sms_units = models.DecimalField(max_digits=11, decimal_places=0)
    credit_status = models.CharField(max_length=10)
    credit_date = models.DateTimeField()
    credit_paid = models.DateTimeField()

    class Meta:
        db_table = 'our_debtors'


class OurSettings(models.Model):
    s_no = models.AutoField(db_column='s/no', primary_key=True)  # Field renamed to remove unsuitable characters.
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    value = models.TextField()

    class Meta:
        db_table = 'our_settings'


class OurVouchers(models.Model):
    vchid = models.AutoField(db_column='vchID', primary_key=True)  # Field name made lowercase.
    vchclientid = models.IntegerField(db_column='vchClientID', blank=True, null=True)  # Field name made lowercase.
    vchresellerid = models.IntegerField(db_column='vchResellerID')  # Field name made lowercase.
    website = models.CharField(max_length=50)
    vchcode = models.CharField(db_column='vchCode', max_length=50)  # Field name made lowercase.
    vchunits = models.IntegerField(db_column='vchUnits')  # Field name made lowercase.
    vchstatus = models.CharField(db_column='vchStatus', max_length=255)  # Field name made lowercase.
    vchdatecreated = models.DateTimeField(db_column='vchDateCreated')  # Field name made lowercase.
    vchdate = models.DateTimeField(db_column='vchDate')  # Field name made lowercase.
    vchtype = models.CharField(db_column='vchType', max_length=6, blank=True, null=True)  # Field name made lowercase.
    vchdateused = models.DateTimeField(db_column='vchDateUsed', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'our_vouchers'


class PaymentHookData(models.Model):
    pay_hook_id = models.AutoField(primary_key=True)
    pay_hook_user = models.ForeignKey(Member, models.DO_NOTHING)
    pay_hoot_reseller_id = models.IntegerField()
    pay_hook_ref = models.CharField(unique=True, max_length=255)
    pay_hook_amount = models.CharField(max_length=255)
    pay_hook_status = models.CharField(max_length=255)
    pay_hook_date = models.DateTimeField()
    pay_hook_response = models.TextField(blank=True, null=True)
    pay_hook_vendor = models.CharField(max_length=25)

    class Meta:
        db_table = 'payment_hook_data'


class PaymentNotify(models.Model):
    username = models.CharField(max_length=50)
    user_id = models.IntegerField()
    account_name = models.CharField(max_length=50)
    account_number = models.CharField(max_length=50)
    bank_name = models.CharField(max_length=50)
    amount_sent = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    date_created = models.DateTimeField()
    date_updated = models.DateTimeField()

    class Meta:
        db_table = 'payment_notify'


class PhoneNetworks(models.Model):
    pn_id = models.AutoField(primary_key=True)
    continient_id = models.IntegerField()
    country_id = models.IntegerField()
    network_name = models.CharField(max_length=100)
    mcc = models.CharField(max_length=5)
    mnc = models.CharField(max_length=5)
    nnc = models.CharField(max_length=10)
    network_price = models.DecimalField(max_digits=10, decimal_places=0)
    date_added = models.DateTimeField()

    class Meta:
        db_table = 'phone_networks'


class Plans(models.Model):
    service_id = models.AutoField(primary_key=True)
    plan_name = models.CharField(max_length=255)
    plan_details = models.CharField(max_length=255)
    plan_status = models.CharField(max_length=255)
    plan_access = models.CharField(max_length=255)
    plan_price = models.CharField(max_length=255)
    date_added = models.DateTimeField()
    date_updated = models.DateField()
    plan_expiry_date = models.DateField()
    plan_logo = models.CharField(max_length=255)
    plan_setting = models.TextField()
    plan_entry = models.CharField(max_length=255, db_collation='ascii_general_ci')
    plan_can_expiry = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        db_table = 'plans'


class RechargeLogicalPin(models.Model):
    logical_pin_id = models.AutoField(primary_key=True)
    logical_userid = models.ForeignKey(Member, models.DO_NOTHING, db_column='logical_userid')
    logical_reseller_id = models.IntegerField()
    network = models.CharField(max_length=10)
    amount = models.DecimalField(max_digits=11, decimal_places=0)
    pin = models.CharField(unique=True, max_length=25)
    pin_status = models.IntegerField()
    merchant_id = models.CharField(max_length=50)
    serial_number = models.CharField(max_length=50)
    transaction_id = models.CharField(max_length=50)
    pin_expiry = models.DateTimeField()
    date_added = models.DateTimeField()
    date_generated = models.DateTimeField()

    class Meta:
        db_table = 'recharge_logical_pin'


class Rechargecard(models.Model):
    rec_id = models.AutoField(primary_key=True)
    rec_client = models.ForeignKey(Member, models.DO_NOTHING)
    rec_reseller_id = models.IntegerField()
    account = models.CharField(max_length=50, blank=True, null=True)
    amount = models.DecimalField(max_digits=11, decimal_places=2)
    amount_charged = models.DecimalField(max_digits=11, decimal_places=2)
    after_balance = models.DecimalField(max_digits=11, decimal_places=2)
    billing_regime = models.CharField(max_length=10)
    bonus_earned = models.DecimalField(max_digits=11, decimal_places=2)
    service_id = models.IntegerField()
    service_name = models.CharField(max_length=50, blank=True, null=True)
    service_url = models.CharField(max_length=255, blank=True, null=True)
    source = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=50)
    pay_status = models.CharField(max_length=50)
    payment_gateway = models.CharField(max_length=255, blank=True, null=True)
    memo = models.CharField(max_length=200, blank=True, null=True)
    responsecode = models.CharField(db_column='responseCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    responsedescription = models.CharField(db_column='responseDescription', max_length=500, blank=True, null=True)  # Field name made lowercase.
    verify_response = models.CharField(max_length=15000, blank=True, null=True)
    providerresponse = models.CharField(db_column='ProviderResponse', max_length=20000, blank=True, null=True)  # Field name made lowercase.
    vendor_formatted_response = models.CharField(max_length=15000, blank=True, null=True)
    referrer = models.CharField(max_length=500, blank=True, null=True)
    date_added = models.DateTimeField()
    date_updated = models.DateTimeField()
    upload_id = models.IntegerField(blank=True, null=True)
    api_id = models.IntegerField(blank=True, null=True)
    vendor_id = models.IntegerField(blank=True, null=True)
    callback_url = models.CharField(max_length=255, blank=True, null=True)
    schedule = models.DateTimeField(blank=True, null=True)
    message = models.CharField(max_length=255, blank=True, null=True)
    bonus_given = models.CharField(max_length=1, blank=True, null=True)
    bonus_trans_id = models.IntegerField(blank=True, null=True)
    wallet_trans_id = models.IntegerField(blank=True, null=True)
    refund_trans_id = models.IntegerField(blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    company_name = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    logo = models.TextField(blank=True, null=True)
    data_card_pin = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        db_table = 'rechargecard'


class Referral(models.Model):
    reg_date = models.DateTimeField()
    referral_id = models.CharField(max_length=255)
    referred_by = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'referral'


class ReferralSettings(models.Model):
    referral_bonus = models.CharField(max_length=255, blank=True, null=True)
    reseller_id = models.IntegerField(unique=True)
    email_notification = models.CharField(max_length=50)
    p_number = models.CharField(max_length=255)
    mtn_percent = models.CharField(max_length=255)
    glo_percent = models.CharField(max_length=255)
    airtel_percent = models.CharField(max_length=255)
    etisalat_percent = models.CharField(max_length=255)
    mtn_number = models.CharField(max_length=255)
    glo_number = models.CharField(max_length=255)
    etisalat_number = models.CharField(max_length=255)
    airtel_number = models.CharField(max_length=255)
    ussd_channel_setting = models.CharField(max_length=50, blank=True, null=True)
    user_id = models.CharField(max_length=11, blank=True, null=True)

    class Meta:
        db_table = 'referral_settings'


class Resellers(models.Model):
    reseller_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Member, models.DO_NOTHING)
    website = models.CharField(unique=True, max_length=55)
    sub_website = models.CharField(unique=True, max_length=200)
    root_domain = models.CharField(max_length=100)
    registration_access = models.CharField(max_length=3)
    domain_folder = models.CharField(max_length=200)
    approvalmessage = models.CharField(db_column='approvalMessage', max_length=500)  # Field name made lowercase.
    newcreditmessage = models.CharField(db_column='newCreditMessage', max_length=500)  # Field name made lowercase.
    newordermessage = models.CharField(db_column='newOrderMessage', max_length=500)  # Field name made lowercase.
    notifyadmin = models.CharField(db_column='notifyAdmin', max_length=2)  # Field name made lowercase.
    neworderadminmessage = models.CharField(db_column='newOrderAdminMessage', max_length=500)  # Field name made lowercase.
    passwordchangemessage = models.CharField(db_column='passwordChangeMessage', max_length=2000)  # Field name made lowercase.
    creditremindermessage = models.CharField(db_column='creditReminderMessage', max_length=5000)  # Field name made lowercase.
    adminaddclient = models.CharField(db_column='adminAddClient', max_length=2000)  # Field name made lowercase.
    confirmation_msg = models.CharField(max_length=2000)
    confirmation_voice_message = models.CharField(max_length=200)
    admin_confirmed_msg = models.CharField(max_length=500)
    admin_credit_alert = models.CharField(max_length=500)
    debtor_paid_alert = models.CharField(max_length=500)
    inactive_member_alert = models.CharField(max_length=1000)
    inactive_member_alert_access = models.IntegerField()
    website_whatsapp_phone = models.CharField(max_length=14)
    reseller_phone = models.CharField(max_length=25)
    cost_structure = models.CharField(max_length=11)
    price_structure = models.CharField(max_length=500)
    voice_price_structure = models.CharField(max_length=1000)
    domain_based_routing = models.JSONField(blank=True, null=True)
    office_address = models.JSONField(blank=True, null=True)
    bank = models.CharField(max_length=500)
    recharge_bonus = models.IntegerField()
    page_list_lenght = models.CharField(max_length=5)
    page_range = models.CharField(max_length=10)
    google_email_add = models.CharField(max_length=30)
    google_email_pass = models.CharField(max_length=30)
    blocksender = models.TextField(db_column='blockSender')  # Field name made lowercase.
    smssender = models.CharField(db_column='smsSender', max_length=11)  # Field name made lowercase.
    emailsender = models.CharField(db_column='emailSender', max_length=150)  # Field name made lowercase.
    currency = models.CharField(max_length=3)
    country_code = models.CharField(max_length=5)
    date_created = models.DateTimeField()
    initial_free_credit = models.CharField(max_length=15)
    credit_limit = models.IntegerField()
    site_title = models.CharField(max_length=200)
    sms_site_setup_fee = models.CharField(max_length=15)
    sms_site_setup_sms_fee = models.CharField(max_length=15)
    facebook = models.CharField(max_length=150)
    twitter = models.CharField(max_length=150)
    gplus = models.CharField(max_length=150)
    enable_email_settings = models.IntegerField()
    email_sender_name = models.CharField(max_length=200)
    email_sender_email = models.CharField(max_length=200)
    smtp_host = models.CharField(max_length=150)
    smtp_port = models.CharField(max_length=3)
    smtp_username = models.CharField(max_length=150)
    smtp_password = models.CharField(max_length=128)
    checkencryption = models.IntegerField(db_column='checkEncryption')  # Field name made lowercase.
    template_folder = models.CharField(max_length=2)
    logo = models.CharField(max_length=50)
    login_background = models.CharField(max_length=50)
    register_background = models.CharField(max_length=50)
    frontend_theme = models.CharField(max_length=255)
    backend_theme = models.CharField(max_length=255)
    brand = models.CharField(max_length=255, blank=True, null=True)
    initial_free_wallet = models.IntegerField()
    modify_frontend_theme = models.IntegerField()
    website_email = models.CharField(max_length=255, blank=True, null=True)
    commissions = models.TextField(blank=True, null=True)
    commissions_new = models.TextField(blank=True, null=True)
    data_share = models.JSONField(blank=True, null=True)
    comm_regime = models.CharField(max_length=3, blank=True, null=True)
    chat_script = models.TextField()
    google_analytics = models.TextField()
    facebook_ad_code = models.TextField()
    other_javascript_based_code = models.TextField()
    main_services = models.TextField(blank=True, null=True)
    sub_services = models.TextField(blank=True, null=True)
    available_services = models.TextField(blank=True, null=True)
    documentation_url = models.CharField(max_length=500, blank=True, null=True)
    website_notification = models.TextField(blank=True, null=True)
    set_discounted_rate_default = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'resellers'


class SentClientsEmail(models.Model):
    email_id = models.AutoField(primary_key=True)
    email_uid = models.ForeignKey(Member, models.DO_NOTHING, db_column='email_uid')
    email_rid = models.IntegerField(blank=True, null=True)
    presave = models.TextField(blank=True, null=True)
    sender = models.CharField(max_length=250, blank=True, null=True)
    recipient = models.TextField(blank=True, null=True)
    cc = models.TextField(blank=True, null=True)
    bcc = models.TextField(blank=True, null=True)
    subject = models.CharField(max_length=500, blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    delivered = models.IntegerField(blank=True, null=True)
    failed = models.IntegerField(blank=True, null=True)
    pending = models.IntegerField(blank=True, null=True)
    schedule = models.DateTimeField(blank=True, null=True)
    date_added = models.DateTimeField(blank=True, null=True)
    date_updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'sent_clients_email'


class SentEmails(models.Model):
    se_id = models.AutoField(primary_key=True)
    website = models.CharField(max_length=100)
    sender = models.CharField(max_length=250)
    fromadd = models.CharField(db_column='fromAdd', max_length=250)  # Field name made lowercase.
    toadd = models.CharField(db_column='toAdd', max_length=250)  # Field name made lowercase.
    subject = models.CharField(max_length=250)
    file = models.CharField(max_length=100)
    details = models.CharField(max_length=500)
    replacement = models.CharField(max_length=500)
    status = models.IntegerField()
    date_sent = models.DateTimeField()

    class Meta:
        db_table = 'sent_emails'


class Testimonials(models.Model):
    testimonials_id = models.AutoField(primary_key=True)
    userid = models.ForeignKey(Member, models.DO_NOTHING, db_column='userid')
    resellerid = models.IntegerField()
    testimonials = models.TextField()
    active = models.IntegerField()
    date_added = models.DateTimeField()

    class Meta:
        db_table = 'testimonials'


class UploadTopup(models.Model):
    upload_id = models.AutoField(primary_key=True)
    upload_user = models.ForeignKey(Member, models.DO_NOTHING)
    upload_reseller_id = models.IntegerField()
    upload_name = models.CharField(max_length=255)
    upload_tmp = models.CharField(max_length=255)
    upload_type = models.CharField(max_length=255)
    upload_error = models.CharField(max_length=255)
    upload_size = models.FloatField()
    upload_content = models.TextField()
    upload_added = models.DateTimeField()
    upload_amount = models.CharField(max_length=255)
    upload_count = models.CharField(max_length=255)
    upload_status = models.CharField(max_length=255)

    class Meta:
        db_table = 'upload_topup'


class UserSettings(models.Model):
    settings_id = models.AutoField(primary_key=True)
    u = models.OneToOneField(Member, models.DO_NOTHING)
    r_id = models.IntegerField()
    notifyme = models.IntegerField(db_column='notifyMe')  # Field name made lowercase.
    sendreports = models.IntegerField(db_column='sendReports')  # Field name made lowercase.
    signature = models.CharField(max_length=160, blank=True, null=True)
    specialcost = models.CharField(db_column='specialCost', max_length=3, blank=True, null=True)  # Field name made lowercase.
    specialprice = models.TextField(db_column='specialPrice', blank=True, null=True)  # Field name made lowercase.
    voice_specialprice = models.CharField(db_column='voice_specialPrice', max_length=1000)  # Field name made lowercase.
    commissions = models.TextField(blank=True, null=True)
    commissions_new = models.TextField(blank=True, null=True)
    previous_plan_id = models.IntegerField(blank=True, null=True)
    data_share = models.JSONField(blank=True, null=True)
    country_code = models.CharField(max_length=5)
    deliveryurl = models.CharField(db_column='DeliveryURL', max_length=200, blank=True, null=True)  # Field name made lowercase.
    senddelivery = models.IntegerField(db_column='sendDelivery')  # Field name made lowercase.
    date_edited = models.DateTimeField()
    comm_regime = models.CharField(max_length=3)
    low_balance_trigger = models.DecimalField(max_digits=11, decimal_places=2)
    low_balance_sms_counter = models.IntegerField()

    class Meta:
        db_table = 'user_settings'


class UssdSessions(models.Model):
    session_id = models.CharField(max_length=50)
    service_code = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=30)
    voucher = models.CharField(max_length=30)
    dialing_response = models.TextField()

    class Meta:
        db_table = 'ussd_sessions'


class VendorSettings(models.Model):
    vendor_settings_id = models.AutoField(primary_key=True)  # The composite primary key (vendor_settings_id, vendor_id) found, that is not supported. The first column is selected.
    vendor_id = models.IntegerField()
    vendor_commission = models.TextField()
    updated = models.DateTimeField()

    class Meta:
        db_table = 'vendor_settings'
        unique_together = (('vendor_settings_id', 'vendor_id'), ('vendor_settings_id', 'vendor_id'),)


class Wallet(models.Model):
    wallet_id = models.AutoField(primary_key=True)
    userid = models.OneToOneField(Member, models.DO_NOTHING, db_column='userid')
    r_id = models.IntegerField()
    amount = models.DecimalField(max_digits=11, decimal_places=2)
    date = models.DateTimeField()

    class Meta:
        db_table = 'wallet'


class WalletTransactions(models.Model):
    wt_id = models.AutoField(primary_key=True)
    wallet_id = models.IntegerField()
    userid = models.ForeignKey(Member, models.DO_NOTHING, db_column='userid')
    r_id = models.IntegerField()
    beneficiary = models.CharField(max_length=255)
    amount = models.CharField(max_length=50)
    after_balance = models.DecimalField(max_digits=11, decimal_places=2)
    date = models.DateTimeField()
    remarks = models.CharField(max_length=255)
    tran_type = models.CharField(max_length=14)
    status = models.CharField(max_length=11)
    process = models.CharField(max_length=20)
    txgateway = models.CharField(db_column='txGateway', max_length=100)  # Field name made lowercase.
    txgatewayresponse = models.TextField(db_column='txGatewayResponse')  # Field name made lowercase.
    recharge_trans_id = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'wallet_transactions'


class WebpayTransactions(models.Model):
    transactionid = models.CharField(unique=True, max_length=10, blank=True, null=True)
    merchantid = models.CharField(max_length=12, blank=True, null=True)
    storeid = models.CharField(max_length=10, blank=True, null=True)
    website = models.CharField(max_length=100, blank=True, null=True)
    merchant_ref = models.CharField(max_length=100, blank=True, null=True)
    transaction_memo = models.CharField(max_length=500, blank=True, null=True)
    developer_code = models.CharField(max_length=100, blank=True, null=True)
    reoccurent = models.CharField(max_length=100, blank=True, null=True)
    interval_occurence = models.CharField(max_length=100, blank=True, null=True)
    item = models.CharField(max_length=100, blank=True, null=True)
    item_description = models.CharField(max_length=100, blank=True, null=True)
    item_price = models.CharField(max_length=100, blank=True, null=True)
    buyer_email = models.CharField(max_length=100, blank=True, null=True)
    currency_code = models.CharField(max_length=100, blank=True, null=True)
    transaction_date = models.DateTimeField(blank=True, null=True)
    transaction_status = models.CharField(max_length=100, blank=True, null=True)
    transaction_channel = models.CharField(max_length=100, blank=True, null=True)
    amount_paid_by_buyer = models.CharField(max_length=100, blank=True, null=True)
    gateway_charges = models.CharField(max_length=100, blank=True, null=True)
    amount_paid_to_mechant = models.CharField(max_length=100, blank=True, null=True)
    fund_maturity_date = models.DateField(blank=True, null=True)
    notify_url = models.CharField(max_length=100)
    success_url = models.CharField(max_length=100, blank=True, null=True)
    fail_url = models.CharField(max_length=100, blank=True, null=True)
    referrer = models.CharField(max_length=500, blank=True, null=True)
    gate_full_response = models.TextField()
    gateway_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'webpay_transactions'


class WebsiteAdverts(models.Model):
    advert_id = models.AutoField(primary_key=True)
    product_id = models.IntegerField()
    advert_title = models.CharField(max_length=50, blank=True, null=True)
    advert_content = models.TextField(blank=True, null=True)
    advert_impression_type = models.CharField(max_length=16)
    advert_impression_amount = models.CharField(max_length=50, blank=True, null=True)
    advert_status = models.CharField(max_length=1)
    advert_date = models.DateTimeField()

    class Meta:
        db_table = 'website_adverts'
