from django.urls import path
from .views import SignUp

urlpatterns = [
    path("", SignUp.as_view(), name=('signUP')),
    # path('', include('core.urls'))

]