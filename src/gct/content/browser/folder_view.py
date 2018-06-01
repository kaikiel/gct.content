# -*- coding: utf-8 -*-
from Acquisition import aq_base
from Acquisition import aq_inner
from Products.CMFPlone.interfaces import ISiteSchema
from plone.app.contenttypes import _
from plone.app.contenttypes.interfaces import IFolder
from plone.app.contenttypes.interfaces import IImage
from plone.event.interfaces import IEvent
from plone.memoize.view import memoize
from plone.registry.interfaces import IRegistry
from Products.CMFPlone.PloneBatch import Batch
from Products.CMFPlone.utils import safe_callable
from Products.Five import BrowserView
from zope.component import getMultiAdapter
from zope.component import getUtility
from zope.contentprovider.interfaces import IContentProvider

import random


HAS_SECURITY_SETTINGS = True
try:
    from Products.CMFPlone.interfaces import ISecuritySchema
except ImportError:
    HAS_SECURITY_SETTINGS = False


class FolderView(BrowserView):

    text_class = None
    _plone_view = None
    _portal_state = None
    _pas_member = None

    def pdb(self):
        import pdb;pdb.set_trace()

    @property
    def plone_view(self):
        if not self._plone_view:
            self._plone_view = getMultiAdapter(
                (self.context, self.request),
                name=u'plone'
            )
        return self._plone_view

    @property
    def portal_state(self):
        if not self._portal_state:
            self._portal_state = getMultiAdapter(
                (self.context, self.request),
                name=u'plone_portal_state'
            )
        return self._portal_state

    @property
    def pas_member(self):
        if not self._pas_member:
            self._pas_member = getMultiAdapter(
                (self.context, self.request),
                name=u'pas_member'
            )
        return self._pas_member

    @property
    def b_size(self):
        b_size = getattr(self.request, 'b_size', None)\
            or getattr(self.request, 'limit_display', None) or 12
        return int(b_size)

    @property
    def b_start(self):
        b_start = getattr(self.request, 'b_start', None) or 0
        return int(b_start)

    def results(self, **kwargs):
        """Return a content listing based result set with contents of the
        folder.

        :param **kwargs: Any keyword argument, which can be used for catalog
                         queries.
        :type  **kwargs: keyword argument

        :returns: plone.app.contentlisting based result set.
        :rtype: ``plone.app.contentlisting.interfaces.IContentListing`` based
                sequence.
        """
        # Extra filter
        kwargs.update(self.request.get('contentFilter', {}))
        if 'object_provides' not in kwargs:  # object_provides is more specific
            kwargs.setdefault('portal_type', self.friendly_types)
        kwargs.setdefault('batch', True)
        kwargs.setdefault('b_size', self.b_size)
        kwargs.setdefault('b_start', self.b_start)

        listing = aq_inner(self.context).restrictedTraverse(
            '@@folderListing', None)
        if listing is None:
            return []
        results = listing(**kwargs)
        return results

    def batch(self):
        batch = Batch(
            self.results(),
            size=self.b_size,
            start=self.b_start,
            orphan=1
        )
        return batch

    @property
    def friendly_types(self):
        return self.portal_state.friendly_types()

    @property
    def use_view_action(self):
        registry = getUtility(IRegistry)
        return registry.get('plone.types_use_view_action_in_listings', [])

    @property
    def no_items_message(self):
        return _(
            'description_no_items_in_folder',
            default=u'There are currently no items in this folder.'
        )

