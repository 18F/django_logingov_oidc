#!/usr/bin/env python
import os
import sys

import django
from django.conf import settings
from django.test.utils import get_runner


os.environ['DJANGO_SETTINGS_MODULE'] = 'djangooidc.tests.test_settings'
django.setup()

TestRunner = get_runner(settings)

test_runner = TestRunner(verbosity=1, interactive=True)
failures = test_runner.run_tests(['djangooidc', ])
sys.exit(failures)