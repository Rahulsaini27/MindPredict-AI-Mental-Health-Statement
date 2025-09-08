
from django.contrib import admin
from django.urls import include
from django.urls import path
from .views import home, signup, user_login, predict, user_logout, prediction_history

urlpatterns = [
    path('', home, name='home'),
    path('signup/', signup, name='signup'),
    path('login/', user_login, name='login'),
    path('predict/', predict, name='predict_view'),
    path('predictionhistory/', prediction_history, name='prediction_history'),
    path('admin/', admin.site.urls),
     path('logout/', user_logout, name='logout'),
     
    
]
