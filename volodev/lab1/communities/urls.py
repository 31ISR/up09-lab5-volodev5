from django.urls import path
from . import views 

app_name = 'communities'

urlpatterns = [
    path('', views.communities_list, name="list"),
    path('new-communitie/', views.communitie_new, name="new-communitie"),
    path('<slug:slug>', views.communitie_page, name="page"),

]
