=====
Multiimap
=====

Multiimap is a simple Django app to manage login via imap server.


Quick start
-----------

1. Add "multiimap" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'django_multiimap',
    ]


2. In project settings, add multiimap backend to the backend tuple::

    AUTHENTICATION_BACKENDS = (
        'django_multiimap.backend.Backend',
        'django.contrib.auth.backends.ModelBackend',
    )

3. In project settings, add an 'MULTIIMAP_SERVERS' dictionary like this::

    MULTIIMAP_SERVERS = {
        'domain': {'host': 'domain_address', 'group_name': 'the_group_name', 'superusers': ['address@email.com']},
        'domain1': {'host': 'domain1_address', 'group_name': 'the_group_name1', 'superusers': []}
    }

This module will create a group with a name like 'multiimap_group_%s' % domain where domain is the @domain.com in user email.
Users mail addresses in superuser list will be set as django superuser.
