from django.urls import path
from .views import RegisterView,LoginView,GenerateWebsiteView,WebsiteListView,WebsiteDetailView,preview_website

app_name = "website_builder"

urlpatterns = [path("register/",RegisterView.as_view(),name='register'),
               path("login/",LoginView.as_view(),name='login'),
               path('generate/', GenerateWebsiteView.as_view(), name='generate_website'),
               path('websites/', WebsiteListView.as_view(), name='website_list'),
               path('websitedetails/<int:pk>', WebsiteDetailView.as_view(), name='website_detail'),
               path('preview/<uuid:preview_id>/',preview_website,name = "preview_website")


]
