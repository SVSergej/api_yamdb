from django.utils import timezone
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def year_validator(value):
    if value > timezone.now().year:
        raise ValidationError(
            _('%(value)s is not a correcrt year!'),
            params={'value': value}, )
