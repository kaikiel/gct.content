# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from gct.content.testing import GCT_CONTENT_INTEGRATION_TESTING  # noqa

import unittest


class TestSetup(unittest.TestCase):
    """Test that gct.content is properly installed."""

    layer = GCT_CONTENT_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if gct.content is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'gct.content'))

    def test_browserlayer(self):
        """Test that IGctContentLayer is registered."""
        from gct.content.interfaces import (
            IGctContentLayer)
        from plone.browserlayer import utils
        self.assertIn(
            IGctContentLayer,
            utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = GCT_CONTENT_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer.uninstallProducts(['gct.content'])
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if gct.content is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'gct.content'))

    def test_browserlayer_removed(self):
        """Test that IGctContentLayer is removed."""
        from gct.content.interfaces import \
            IGctContentLayer
        from plone.browserlayer import utils
        self.assertNotIn(
            IGctContentLayer,
            utils.registered_layers())
