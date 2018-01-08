# Copyright (c) PagerDuty.
# See LICENSE for details.

import os
import unittest

from pypd import set_api_key_from_env_var

class SetAPIKeyTests(unittest.TestCase):
    def test_set_api_key_from_env_var(self):
        """pypd.set_api_key_from_env_var('test_env_var') == 'test_env_var_value' """

        os.environ['test_env_var'] = 'test_env_var_value'

        self.assertEqual(set_api_key_from_env_var('test_env_var'), 'test_env_var_value')

        del os.environ['test_env_var']

    def test_set_api_key_from_env_var_not_set(self):
        """pypd.set_api_key_from_env_var('test_env_var') == 'Not Set' """

        self.assertEqual(set_api_key_from_env_var('test_env_var'), 'Not Set')
