# -*- coding: utf-8 -*- 
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone import api


class DownloadFileView(BrowserView):
    template = ViewPageTemplateFile('templates/download_file_view.pt')
    def __call__(self):
        request = self.request
        portal = api.portal.get()
        fileBrains = api.content.find(context=portal['file_content'], portal_type='File')
        self.fileBrains = fileBrains
        return self.template()


class ProductView(BrowserView):
    template = ViewPageTemplateFile('templates/product_view.pt')
    def __call__(self):
        import pdb;pdb.set_trace()
        imgList = []
        if self.context.cover != None:
            imgList.append(self.context.cover)
#        if api.content.find:
            

        return self.template()
