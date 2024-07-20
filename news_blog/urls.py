from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from news import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/auth/', views.UserCreate.as_view(), name='user-create'),
    path('api/blogs/', views.BlogListCreate.as_view(), name='blog-list-create'),
    path('api/blogs/<int:pk>/like/', views.BlogLike.as_view(), name='blog-like'),
    path('api/blogs/', views.BlogList.as_view(), name='blog-list'),
]
