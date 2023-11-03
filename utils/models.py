import datetime
import warnings

from django.conf import settings
from django.core import exceptions
from django.db.models import DateField
from django import forms
from django.utils import timezone
from django.utils.dateparse import (
    parse_date,
    parse_datetime,
)
from django.utils.translation import gettext_lazy as _


class DateTimeField(DateField):
    empty_strings_allowed = False
    default_error_messages = {
        "invalid": _(
            "“%(value)s” value has an invalid format. It must be in "
            "YYYY-MM-DD HH:MM[:ss[.uuuuuu]][TZ] format."
        ),
        "invalid_date": _(
            "“%(value)s” value has the correct format "
            "(YYYY-MM-DD) but it is an invalid date."
        ),
        "invalid_datetime": _(
            "“%(value)s” value has the correct format "
            "(YYYY-MM-DD HH:MM[:ss[.uuuuuu]][TZ]) "
            "but it is an invalid date/time."
        ),
    }
    description = _("Date (with time)")

    # __init__ is inherited from DateField

    def _check_fix_default_value(self):
        """
        Warn that using an actual date or datetime value is probably wrong;
        it's only evaluated on server startup.
        """
        if not self.has_default():
            return []

        value = self.default
        if isinstance(value, (datetime.datetime, datetime.date)):
            return self._check_if_value_fixed(value)
        # No explicit date / datetime value -- no checks necessary.
        return []

    def get_internal_type(self):
        return "DateTimeField"

    def to_python(self, value):
        if value is None:
            return value
        if isinstance(value, datetime.datetime):
            return value
        if isinstance(value, datetime.date):
            value = datetime.datetime(value.year, value.month, value.day)
            if settings.USE_TZ:
                # For backwards compatibility, interpret naive datetimes in
                # local time. This won't work during DST change, but we can't
                # do much about it, so we let the exceptions percolate up the
                # call stack.
                warnings.warn(
                    "DateTimeField %s.%s received a naive datetime "
                    "(%s) while time zone support is active."
                    % (self.model.__name__, self.name, value),
                    RuntimeWarning,
                    )
                default_timezone = timezone.get_default_timezone()
                value = timezone.make_aware(value, default_timezone)
            return value

        try:
            parsed = parse_datetime(value)
            if parsed is not None:
                return parsed
        except ValueError:
            raise exceptions.ValidationError(
                self.error_messages["invalid_datetime"],
                code="invalid_datetime",
                params={"value": value},
            )

        try:
            parsed = parse_date(value)
            if parsed is not None:
                return datetime.datetime(parsed.year, parsed.month, parsed.day)
        except ValueError:
            raise exceptions.ValidationError(
                self.error_messages["invalid_date"],
                code="invalid_date",
                params={"value": value},
            )

        raise exceptions.ValidationError(
            self.error_messages["invalid"],
            code="invalid",
            params={"value": value},
        )

    def pre_save(self, model_instance, add):
        if self.auto_now or (self.auto_now_add and add):
            value = timezone.now()
            setattr(model_instance, self.attname, value)
            return value
        else:
            return super().pre_save(model_instance, add)

    # contribute_to_class is inherited from DateField, it registers
    # get_next_by_FOO and get_prev_by_FOO

    def get_prep_value(self, value):
        value = super().get_prep_value(value)
        value = self.to_python(value)
        if value is not None and settings.USE_TZ and timezone.is_naive(value):
            # For backwards compatibility, interpret naive datetimes in local
            # time. This won't work during DST change, but we can't do much
            # about it, so we let the exceptions percolate up the call stack.
            try:
                name = "%s.%s" % (self.model.__name__, self.name)
            except AttributeError:
                name = "(unbound)"
            warnings.warn(
                "DateTimeField %s received a naive datetime (%s)"
                " while time zone support is active." % (name, value),
                RuntimeWarning,
                )
            default_timezone = timezone.get_default_timezone()
            value = timezone.make_aware(value, default_timezone)
        return value

    def from_db_value(self, value, expression, connection):
        if value is None:
            return value

        if value.microsecond >= 500_000:
            value += datetime.timedelta(seconds=1)
        value = value.replace(microsecond=0)

        return value.astimezone()

    def get_db_prep_value(self, value, connection, prepared=False):
        # Casts datetimes into the format expected by the backend
        if not prepared:
            value = self.get_prep_value(value)
        return connection.ops.adapt_datetimefield_value(value)

    def value_to_string(self, obj):
        val = self.value_from_object(obj)
        return "" if val is None else val.isoformat()

    def formfield(self, **kwargs):
        return super().formfield(
            **{
                "form_class": forms.DateTimeField,
                **kwargs,
            }
        )
