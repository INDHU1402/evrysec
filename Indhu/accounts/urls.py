from django.urls import path
from . import views


urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('report/', views.report, name='report'),
    path('page/',views.page,name="page"),
]
