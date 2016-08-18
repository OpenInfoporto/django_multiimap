from imaplib import IMAP4
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.conf import settings


class Backend:

    def check_settings(self, domain):
        if not hasattr(settings, 'IMAP_SERVER'):
            raise AttributeError('Missing IMAP_SERVER configuration in settings')
        if not settings.IMAP_SERVER[domain]:
            raise AttributeError('Domain %s not found in settings' % domain)
        if not settings.IMAP_SERVER[domain]['host']:
            raise AttributeError('Host setting not found in settings for %s' % domain)

    def generate_group_name(self, domain):
        group_name = settings.IMAP_SERVER[domain].get('group_name', domain)
        return 'multiimap_group_%s' % group_name.replace(' ', '_').lower()

    def authenticate(self, username=None, password=None):

        try:
            domain = username.split('@')[1]
        except IndexError:
            return None

        self.check_settings(domain)

        try:
            address = settings.IMAP_SERVER[domain]['host']
            # Check if this user is valid on the mail server
            c = IMAP4(address)
            c.login(username, password)
            c.logout()
        except:
            return None

        user, created = get_user_model().objects.get_or_create(username=username)
        group, created = Group.objects.get_or_create(name=self.generate_group_name(domain))
        user.groups.add(group)

        return user

    # Required for your backend to work properly - unchanged in most scenarios
    def get_user(self, user_id):
        try:
            return get_user_model().objects.get(pk=user_id)
        except get_user_model().DoesNotExist:
            return None


