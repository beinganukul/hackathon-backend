from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
        path('v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
        path('v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
        path('v1/books', views.getBooks),
        path('v1/users', views.getUser),
        path('v1/user/<str:pk>', views.getProfile),
        path('v1/account/register', views.RegistrationView.as_view()), 
        path('v1/account/logout', views.userlogout),
        #path('v1/account/change-password', views.ChangePasswordView.as_view()),
        ]
