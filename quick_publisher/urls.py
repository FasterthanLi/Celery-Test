from django.contrib import admin
from django.urls import path, include
from publish.views import ViewPost
from main.views import HomeView, VerifyView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name = 'home'), 
    path('<slug:slug>', ViewPost.as_view(), name='view_post'),
    path('verify/<uuid>',VerifyView.as_view(), name ='verify'),
]
