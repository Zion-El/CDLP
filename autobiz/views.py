
# from django.shortcuts import render
# from django.contrib.messages.views import SuccessMessageMixin
# from django.contrib.sites.shortcuts import get_current_site
# from django.core.mail import EmailMessage
# from .models import CustomUser
# from django.views import generic
# from django.forms.utils import ErrorList
# from django import forms
# from django.shortcuts import get_object_or_404, redirect, render
# from django.template.loader import get_template
# from django.urls import reverse_lazy
# from django.contrib.auth.forms import UserChangeForm, UserCreationForm

# # Create your views here.

# # HANDLING SIGNUP
# class SignUp(SuccessMessageMixin, generic.CreateView):
#     form_class = CustomUserCreationForm
#     success_url = reverse_lazy("login")
#     template_name = "signup.html"
#     # success_messages = 'Please confirm your email address to complete the registration,activation link has been sent to your email, also check your email spam folder'
#     success_messages = "You have successfully Registered, Kindly login to continue"


#     def abc(self):
#         ref = ""
#         if "referal" in self.request.session:
#             ref = self.request.session["referal"]

#         return ref

#     def get_context_data(self, **kwargs):
#         context = super(SignUp, self).get_context_data(**kwargs)
#         context["referal_user"] = self.abc()

#         return context

#     def form_valid(self, form):
#         object = form.save(commit=False)
#         username = object.username
#         email = object.email
#         # object.email_verify = False
#         # object.is_active = False
#         user = object

#         # to check if the username is available or used
#         if CustomUser.objects.filter(username__iexact=object.username).exists():
#             form._errors[forms.forms.NON_FIELD_ERRORS] = ErrorList(
#                 ["This username has been taken"]
#             )
#             return self.form_invalid(form)

#         # to check if email is available or used
#         elif CustomUser.objects.filter(email__iexact=object.email).exists():
#             form._errors[forms.forms.NON_FIELD_ERRORS] = ErrorList(
#                 ["This email has been taken"]
#             )
#             return self.form_invalid(form)
#         elif CustomUser.objects.filter(Phone__iexact=object.Phone).exists():
#             form._errors[forms.forms.NON_FIELD_ERRORS] = ErrorList(
#                 ["This Phone has been taken"]
#             )
#             return self.form_invalid(form)

#         elif not object.email.endswith(("@gmail.com", "@yahoo.com")):
#             form._errors[forms.forms.NON_FIELD_ERRORS] = ErrorList(
#                 ["We accept only valid gmail or yahoo mail account"]
#             )
#             return self.form_invalid(form)

#         elif object.referer_username:
#             if CustomUser.objects.filter(
#                 username__iexact=object.referer_username
#             ).exists():
#                 referal_user = CustomUser.objects.get(
#                     username__iexact=object.referer_username
#                 )

#             else:
#                 object.referer_username = None

#         form.save()

#         # try:
#         #     current_site = get_current_site(self.request)
#         #     mail_subject = "Activate your legitdata account."
#         #     message = {
#         #         "user": user,
#         #         "domain": current_site.domain,
#         #         "uid": urlsafe_base64_encode(force_bytes(user.pk)),
#         #         "token": account_activation_token.make_token(user),
#         #     }
#         #     message = get_template("acc_active_email.html").render(message)
#         #     to_email = email
#         #     email = EmailMessage(mail_subject, message, to=[to_email])
#         #     email.content_subtype = "html"
#         #     email.send()

#         # except:
#         #     pass
#         # try:
#         #     Referal_list.objects.create(user=referal_user, username=username)
#         # except:
#         #     pass
#         # try:
#         #     # messages.success( self.request, 'Please confirm your email address to complete the registration,activation link has been sent to your email,, also check your email spam folder')

#         #     sendmail(
#         #         "Welcome to legitdata.com.ng",
#         #         "Welcome to alegitdata.com.ngWe offer instant recharge of Airtime, Databundle, CableTV (DStv, GOtv & Startimes), Electricity Bill Payment and Airtime to Cash.",
#         #         email,
#         #         username,
#         #     )

#         # except:
#         #     pass
#         # try:

#         #     def create_id():
#         #         random.randint(1, 10)
#         #         num_2 = random.randint(1, 10)
#         #         num_3 = random.randint(1, 10)
#         #         return str(num_2) + str(num_3) + str(uuid.uuid4())[:4]

#         #     body = {
#         #         "accountReference": create_id(),
#         #         "accountName": username,
#         #         "currencyCode": "NGN",
#         #         "contractCode": f"{get_config().monnify_contract_code}",
#         #         "customerEmail": email,
#         #         "incomeSplitConfig": [],
#         #         "restrictPaymentSource": False,
#         #         "allowedPaymentSources": {},
#         #     }

#         #     if not email:
#         #         data = json.dumps(body)
#         #         ad = requests.post(
#         #             "https://api.monnify.com/api/v1/auth/login",
#         #             auth=HTTPBasicAuth(
#         #                 f"{get_config().monnify_API_KEY}",
#         #                 f"{get_config().monnify_SECRET_KEY}",
#         #             ),
#         #         )
#         #         mydata = json.loads(ad.text)

#         #         headers = {
#         #             "Content-Type": "application/json",
#         #             "Authorization": "Bearer {}".format(
#         #                 mydata["responseBody"]["accessToken"]
#         #             ),
#         #         }
#         #         ab = requests.post(
#         #             "https://api.monnify.com/api/v1/bank-transfer/reserved-accounts",
#         #             headers=headers,
#         #             data=data,
#         #         )

#         #         mydata = json.loads(ab.text)

#         #         user = CustomUser.objects.get(email__iexact=email)

#         #         user.reservedaccountNumber = mydata["responseBody"]["accountNumber"]
#         #         user.reservedbankName = mydata["responseBody"]["bankName"]
#         #         user.reservedaccountReference = mydata["responseBody"][
#         #             "accountReference"
#         #         ]
#         #         user.save()

#         #     else:
#         #         pass

#         # except:
#         #     pass
#         return super(SignUp, self).form_valid(form)