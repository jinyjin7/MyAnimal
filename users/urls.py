from django.urls import path
from users import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('signup/', views.SignupView.as_view(),
         name='sign_up_view'),  # /users/signup/
    path('login/', views.CustomTokenObtainPairView.as_view(),
         name='login_view'),  # /users/login/
    path("refresh/", TokenRefreshView.as_view(),
         name="token_refresh"),  # /users/refresh/
    path('profile/<int:user_id>/', views.ProfileView.as_view(),
         name="profile_view"),  # /users/profile/<int:user_id>/
    path('follow/<int:user_id>/', views.FollowView.as_view(),
         name='follow_view'),  # /users/follow/<int:user_id>/

    path('password_reset/', auth_views.PasswordResetView.as_view(),
         name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(),
         name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),
]
