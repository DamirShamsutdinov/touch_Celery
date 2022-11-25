from django.conf.urls import url

from users import views

# from users.views import ContactView

app_name = "users"

urlpatterns = [
    url(r'^create', views.create, name='create'),
    url(r'^home', views.home, name='home')
]
