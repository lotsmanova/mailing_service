from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from users.tokens import account_activation_token

def register_send_mail(new_user, current_site):
    mail_subject = 'Активация аккаунта'
    message = render_to_string('users/activation_email.html', {
        'user': new_user,
        'domain': current_site.domain,
        'uid': urlsafe_base64_encode(force_bytes(new_user.pk)),
        'token': account_activation_token.make_token(new_user),
    })

    send_mail(mail_subject, message, settings.EMAIL_HOST_USER, [new_user.email])
