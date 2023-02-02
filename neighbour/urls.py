from django.urls import URLPattern, path, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
# from django.urls import reverse_lazy

neighbour='mainapp'
urlpatterns=[
  path('home/', views.index , name="index"),
  re_path(r'^register-neighbourhood/', views.upload_neighbourhood, name="upload"),
  re_path(r'^register-business/', views.add_business, name="add-business"),
  path('', views.profile, name="profile"),
  re_path(r'^search/', views.search_results, name='search_results'),
  re_path(r'^post/', views.post , name="post"),
  re_path('accounts/login/', auth_views.LoginView.as_view(template_name='django_registration/login.html'), name='login'),
  path('accounts/login/', views.redirect_view,name = 'redirect'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)