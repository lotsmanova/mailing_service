from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse_lazy
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from django.views.generic import CreateView, TemplateView

from users.forms import UserRegisterForm
from users.models import User
from users.services import register_send_mail
from users.tokens import account_activation_token

class LoginView(BaseLoginView):
    """Контроллер входа в аккаунт"""

    template_name = 'users/login.html'


class LogoutView(BaseLogoutView):
    """Контроллер выхода из аккаунта"""

    pass


class RegisterView(CreateView):
    """Контроллер регистрации пользователя"""

    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        new_user = form.save(commit=False)
        new_user.is_active = False
        new_user.save()

        current_site = get_current_site(self.request)

        register_send_mail(new_user, current_site)

        return super().form_valid(form)


class UserActivateView(TemplateView):
    """Контроллер верификации аккаунта"""

    template_name = 'users/activate.html'

    def get(self, request, uidb64, token, *args, **kwargs):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user is not None and account_activation_token.check_token(user, token):
            user.is_active = True
            user.save()
            return self.render_to_response({'activated': True})

        return self.render_to_response({'activated': False})

