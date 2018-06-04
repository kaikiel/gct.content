# -*- coding: utf-8 -*- 
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone import api
from email.mime.text import MIMEText


class DownloadFileView(BrowserView):
    template = ViewPageTemplateFile('templates/download_file_view.pt')
    def __call__(self):
        request = self.request
        portal = api.portal.get()
	fileList = []
        fileBrains = api.content.find(path='gct/file_container', portal_type='File')
	# sort_order not working
	for item in fileBrains:
	    fileList.append(item)
	fileList.reverse()
        self.fileList = fileList
        return self.template()


class ProductView(BrowserView):
    template = ViewPageTemplateFile('templates/product_view.pt')
    def __call__(self):
        imgList = []
        coverImg = self.context.cover
#        if coverImg != None:
#            imgList.append(self.context.absolute_url()+'/@@images/cover')
        productImgs = api.content.find(context=self.context, depth=1)
        for item in productImgs:
            imgList.append('{}/@@images/image/preview'.format(item.getObject().absolute_url()))
        self.imgList = imgList
        
        self.title = self.context.title
        self.modelNo = self.context.modelNo
        self.beApplicable = self.context.beApplicable
        self.characteristic = self.context.characteristic
        self.body = self.context.body.raw if self.context.body != None else None
        
        return self.template()


class CoverView(BrowserView):
    template = ViewPageTemplateFile('templates/cover_view.pt')
    def __call__(self):
        request = self.request
        portal = api.portal.get()

        featureList = self.context.feature
        self.featureList = featureList

	return self.template()


class FolderProductView(BrowserView):
    template = ViewPageTemplateFile('templates/folder_product_view.pt')
    def __call__(self):
	return self.template()


class FolderNewsView(BrowserView):
    template = ViewPageTemplateFile('templates/folder_news_view.pt')
    def __call__(self):
	return self.template()


class ContactUs(BrowserView):
    template = ViewPageTemplateFile('templates/contact_us.pt')
    def __call__(self):
        request = self.request
	name = request.get('name')
	email = request.get('email')
	message = request.get('message')
	if name and email and message:
	    body_str = """Name:{}<br/>Email:{}<br/>Message:{}""".format(name, email, message)
            mime_text = MIMEText(body_str, 'html', 'utf-8')
            api.portal.send_email(
                recipient="ah13441673@gmail.com",
                sender="henry@mingtak.com.tw",
                subject="意見提供",
                body=mime_text.as_string(),
            )
	api.portal.show_message(message='發送成功!'.decode('utf-8'), request=request)
        return self.template()


class NewsItemView(BrowserView):
    template = ViewPageTemplateFile('templates/news_item_view.pt')
    def __call__(self):
        request = self.request
        return self.template()
