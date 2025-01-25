from django.urls import path
from.views import (
    login_view,
    logout_view,
    TestLogoutView,
    set_cookie_view,
    get_cookie_view,
    set_session_view,
    get_session_view,
)

app_name = 'test_auth'

urlpatterns = [
    # path('login/', login_view, name='login'),
    # path('login/', login_view.as_view(
    #     template_name='test_auth/login.html',
    #     redirect_authenticated_user=True,
    # )
    # , name='login'),
    path('cookie/get/', get_cookie_view, name='cookie_get'),
    path('cookie/set/', set_cookie_view, name='cookie_set'),

    path('session/get/', get_session_view, name='session_get'),
    path('session/set/', set_session_view, name='session_set'),
]