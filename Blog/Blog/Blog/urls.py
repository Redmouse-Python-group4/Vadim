"""Blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from article.views import index, article, category, num_index, create_comments, logout, RegistrationForm, LoginForm
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^([0-9]+)/$', num_index, name="num_index"),
    url(r'^article/([0-9]+)/$', article, name='article'),
    url(r'^category/([0-9]+)/$', category, name='category'),
    url(r'^comments/([0-9]+)/$', create_comments, name="create_comments"),
    url(r'^admin/', admin.site.urls),
    url(r'^logout/$', logout, name='logout'),
    url(r'^reg/$', RegistrationForm.as_view(), name='reg'),
    url(r'^login/$', LoginForm.as_view(), name='login'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
