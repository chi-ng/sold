from django.conf import settings
from django.conf.urls import include, url
#newer version of django url dispather
from django.urls import path
from django.contrib import admin

from django.http import HttpResponse


from django.conf.urls.static import static

#user
from django.contrib.auth import views as auth_views

#users app
from users import views as user_views





urlpatterns = [
    path(r'', include('welcome.urls', namespace='welcome')),
    path(r'user/', include('users.urls', namespace='users')),
    path(r'health/', lambda request: HttpResponse('okay')),
    path(r'admin/', admin.site.urls),
    path('signup/', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='welcome/index.html'), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name='welcome/logout.html'), name="logout"),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='welcome/password_change_done.html'),name='password_change_done'),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='welcome/password_change.html'), name='password_change'),
    path('password_reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='welcome/password_reset_done.html'),name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset_form/', auth_views.PasswordResetView.as_view(template_name='welcome/password_reset_form.html'), name='password_reset'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='welcome/password_reset_complete.html'),name='password_reset_complete'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
