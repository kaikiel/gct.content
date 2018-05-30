# -*- coding: utf-8 -*- 
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone import api


class DownloadFileView(BrowserView):
    template = ViewPageTemplateFile('templates/download_file_view.pt')
    def __call__(self):
        request = self.request
        portal = api.portal.get()
        fileBrains = api.content.find(context=portal['file_container'], portal_type='File')
        self.fileBrains = fileBrains
        return self.template()


class ProductView(BrowserView):
    template = ViewPageTemplateFile('templates/product_view.pt')
    def __call__(self):
        import pdb;pdb.set_trace()
        imgList = []
        coverImg = self.context.cover
#        if coverImg != None:
#            imgList.append(self.context.absolute_url()+'/@@images/cover')
        productImgs = api.content.find(context=self.context, depth=1)
        for item in productImgs:
            imgList.append(item.getObject().absolute_url())
        self.imgList = imgList
        
        self.title = self.context.title
        self.modelNo = self.context.modelNo
        self.beApplicable = self.context.beApplicable
        self.characteristic = self.context.characteristic
        self.body = self.context.body.raw
        
        return self.template()



class CoverView(BrowserView):
    template = ViewPageTemplateFile('templates/cover_view.pt')
    def __call__(self):
        request = self.request
        portal = api.portal.get()

        productBrains = api.content.find(context=portal['products'], portal_type='Product', sort_limit=4)
        self.productBrains = productBrains

        featureList = self.context.feature
        self.featureList = featureList

	return self.template()
