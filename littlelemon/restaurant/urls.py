from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
#     . . . ,
    path('', views.index, name='index'),
    path('menu/', views.MenuItemsView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
<<<<<<< HEAD
    path('message/', views.msg),
    path('api-token-auth/', obtain_auth_token),
=======
>>>>>>> 9d926dc5d0c254ce520f18ca7ebd4c90f1e7c0b8
]
