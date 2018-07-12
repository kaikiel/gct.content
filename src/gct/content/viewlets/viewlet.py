# -*- coding: utf-8 -*-
from plone.app.layout.viewlets import common as base
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone import api
from zope.component import queryUtility
from plone.i18n.normalizer.interfaces import IIDNormalizer
from gct.content.browser.base_inform_configlet import IInform


class CoverBanner(base.ViewletBase):
    def update(self):
        portal = api.portal.get()
        #bannerList = api.content.find(path='gct/banner', portal_type='Image', sort_limit=6)
	bannerList = portal['banner'].getChildNodes()
        self.bannerList = bannerList


class NewsProduct(base.ViewletBase):
    def update(self):
        request = self.request
        portal = api.portal.get()
        productBrains = api.content.find(path='gct/products', portal_type='Product', sort_limit=4, sort_on='created', sort_order='descending')
        self.productBrains = productBrains

class NewsItemBanner(base.ViewletBase):
    def update(self):
        request = self.request
        portal = api.portal.get()
        newsItemBrains = portal['news_container'].getChildNodes() 
        self.newsItemBrains = newsItemBrains
