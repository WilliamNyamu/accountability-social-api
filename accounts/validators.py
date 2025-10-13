# validators.py
import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_phone_number(value):
    # Regular expression for a basic phone number format
    # This example allows numbers with or without a country code and spaces/dashes
    if not re.match(r'^\+?1?\d{9,15}$', value):
        raise ValidationError(
            _('%(value)s is not a valid phone number.'),
            params={'value': value},
        )
    