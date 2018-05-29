# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from zope.publisher.interfaces.browser import IDefaultBrowserLayer
from plone.dexterity.content    import Container


class FolderishContent(Container):
    pass

class IGctContentLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""
