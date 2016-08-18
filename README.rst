 
=====
Multiimap
=====

Multiimap is a simple Django app to manage login via imap server.


Quick start
-----------

1. Add "multiimap" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'django-multiimap',
    ]


2. In project settings, add multiimap backend to the backend tuple:
    AUTHENTICATION_BACKENDS = (
    'django_multiimap.backend.Backend',
    'django.contrib.auth.backends.ModelBackend',
)

3. In project settings, add an 'IMAP_SERVER' dictionary like this:
IMAP_SERVER = {
    'domain': {'host': 'domain_address', 'group_name': 'the_group_name'},
    'domain1': {'host': 'domain1_address', 'group_name': 'the_group_name1'}
}

This module will create a group with a name like 'multiimap_group_%s' % domain where domain is the @domain.com in user email.
