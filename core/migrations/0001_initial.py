# Generated by Django 4.2.1 on 2023-05-11 13:08

import core.models
import django.contrib.auth.validators
import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254)),
                ('FullName', models.CharField(max_length=200, null=True)),
                ('Address', models.CharField(max_length=500, null=True)),
                ('BankName', models.CharField(blank=True, choices=[('Access Bank', 'Access Bank'), ('Access(Diamond) Bank', 'Access (Diamond) Bank'), ('ECO Bank', 'ECO Bank'), ('First Bank of Nigeria', 'First Bank of Nigeria'), ('FCMBank', 'FCMBank'), ('FIdelity Bank', 'FIdelity Bank'), ('GTBank', 'GTBank'), ('Heritage Bank', 'Heritage Bank'), ('Kuda Bank', 'Kuda Bank'), ('Opay', 'Opay'), ('Palmpay', 'Palmpay'), ('Polarise Bank', 'Polarise Bank'), ('Stanbic IBTC', 'Stanbic IBTC'), ('Sterling Bank', 'Sterling Bank'), ('UBA', 'UBA'), ('Union Bank', 'Union Bank'), ('Unity Bank', 'Unity Bank'), ('Wema Bank', 'Wema Bank'), ('Zenith Bank', 'Zenith Bank')], max_length=100)),
                ('AccountNumber', models.CharField(blank=True, max_length=40)),
                ('Phone', models.CharField(blank=True, max_length=30)),
                ('AccountName', models.CharField(blank=True, max_length=200)),
                ('Account_Balance', models.FloatField(default=0.0, null=True, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('pin', models.CharField(blank=True, max_length=5, null=True)),
                ('referer_username', models.CharField(blank=True, max_length=50, null=True)),
                ('first_payment', models.BooleanField(default=False)),
                ('Referer_Bonus', models.FloatField(default=0.0, null=True, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('user_type', models.CharField(choices=[('Smart Earner', 'Smart Earner'), ('Affilliate', 'Affilliate'), ('TopUser', 'TopUser'), ('API', 'API')], default='Smart Earner', max_length=30, null=True)),
                ('reservedaccountNumber', models.CharField(blank=True, max_length=100, null=True)),
                ('reservedbankName', models.CharField(blank=True, max_length=100, null=True)),
                ('reservedaccountReference', models.CharField(blank=True, max_length=100, null=True)),
                ('Bonus', models.FloatField(default=0.0, null=True, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('verify', models.BooleanField(default=False)),
                ('email_verify', models.BooleanField(default=False)),
                ('DOB', models.DateField(blank=True, null=True)),
                ('Gender', models.CharField(max_length=6, null=True)),
                ('State_of_origin', models.CharField(max_length=100, null=True)),
                ('Local_gov_of_origin', models.CharField(max_length=100, null=True)),
                ('BVN', models.CharField(max_length=50, null=True)),
                ('passport_photogragh', models.ImageField(help_text='Maximum of 50kb in size', null=True, upload_to='passport_images')),
                ('accounts', models.TextField(blank=True, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name_plural': 'USERS MANAGEMENT',
            },
            managers=[
                ('objects', core.models.CustomUserManager()),
            ],
        ),
    ]
