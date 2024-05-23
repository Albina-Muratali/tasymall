from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from core import views
from core.customer import views as customer_views
from core.courier import views as courier_views, apis as courier_apis

from django.conf import settings
from django.conf.urls.static import static

# Customer URL patterns
customer_urlpatterns = [
    path('', customer_views.home, name="home"),
    path('profile/', customer_views.profile_page, name="profile"),
    path('payment_method/', customer_views.payment_method_page, name="payment_method"),
    path('create_job/', customer_views.create_job_page, name="create_job"),
    path('jobs/current/', customer_views.current_jobs_page, name="current_jobs"),
    path('jobs/archived/', customer_views.archived_jobs_page, name="archived_jobs"),
    path('jobs/<job_id>/', customer_views.job_page, name="job"),
]

# Courier URL patterns
courier_urlpatterns = [
    path('', courier_views.home, name="home"),
    path('jobs/available/', courier_views.available_jobs_page, name="available_jobs"),
    path('jobs/available/<id>/', courier_views.available_job_page, name="available_job"),
    path('api/jobs/available/', courier_apis.available_jobs_api, name="available_jobs_api"),
]

# Main URL patterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('sign-in/', auth_views.LoginView.as_view(template_name="sign_in.html"), name='sign_in'),
    path('sign-out/', auth_views.LogoutView.as_view(next_page="sign-up.html"), name='sign_out'),
    path('sign-up/', views.sign_up, name='sign_up'),
    path('customer/', include((customer_urlpatterns, 'customer'))),
    path('courier/', include((courier_urlpatterns, 'courier'))),
]

# Static files (images, CSS, JavaScript, etc.)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)