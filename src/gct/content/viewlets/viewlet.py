
# -*- coding: utf-8 -*-
from plone.app.layout.viewlets import common as base
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone import api
from zope.component import queryUtility
from plone.i18n.normalizer.interfaces import IIDNormalizer


class CoverBanner(base.ViewletBase):
    def update(self):
        portal = api.portal.get()
        bannerList = api.content.find(context=portal['banner'], portal_type='Image', sort_limit=6)
        self.bannerList = bannerList
