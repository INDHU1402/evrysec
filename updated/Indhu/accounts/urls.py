from django.urls import path
from . import views
from accounts.views import EmailAttachementView


urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('efire/', views.efire, name="efire"),
    #path('report/', views.report, name='report'),
    path('emailattachment/', views.EmailAttachementView.as_view(), name='emailattachment'),
    path('page/',views.page,name="page"),
    path('success1/',views.done1,name="success1"),
    path('success2/',views.done2,name="success2"),
    path('success3/',views.done3,name="success3"),
    path('success4/',views.done4,name="success4"),
    path('success5/',views.done5,name="success5"),
    path('success6/',views.done6,name="success6"),
    
    
]
