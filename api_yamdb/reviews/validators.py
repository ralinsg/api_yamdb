from django.core.exceptions import ValidationError
from django.utils import timezone


def validate_year(value):
    """Валидация поля year модели Title."""

    if value > timezone.now().year:
        raise ValidationError(
            (f'Год {value} больше текущего!'),
            params={'value': value},
        )
