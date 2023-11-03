from time import mktime

from contacts.models import Contact


def get_latest_hash(user=None):
    qs = Contact.objects.filter(owner=user)
    if qs.count() == 0:
        return None

    last_id = qs.order_by('-id').first().pk
    last_updated = qs.order_by('-last_updated').first().last_updated
    last_updated_timestamp = int(mktime(last_updated.timetuple()))

    return f'{last_id}_{last_updated_timestamp}'
