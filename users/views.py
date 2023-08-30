from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LogoutView as BaseLogoutView

class LoginView(BaseLoginView):
    """Контроллер входа в аккаунт"""

    template_name = 'users/login.html'


class LogoutView(BaseLogoutView):
    """Контроллер выхода из аккаунта"""

    pass