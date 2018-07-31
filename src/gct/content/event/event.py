from plone import api
from zope.globalrequest import getRequest
from gct.content.browser.views import UpdateConfiglet
from plone.app.textfield.value import RichTextValue

def move_to_top(item, event):
    request = getRequest()
    folder = item.getParentNode()
    folder.moveObjectsToTop(item.id)
    abs_url = folder.absolute_url()
    request.response.redirect('%s/folder_contents' %abs_url)

def add_configlet(item, event):
    try:
	request = getRequest()
	item.moveObjectsToTop(item.id)
        abs_url = api.portal.get().absolute_url()
        update_configlet = UpdateConfiglet()
        update_configlet()
    except Exception as e:
	print e

#to modify event,moveToTop will cause error
def modify_configlet(item, event):
    request = getRequest()
    abs_url = api.portal.get().absolute_url()
    update_configlet = UpdateConfiglet()
    update_configlet()

def toFolderContents(obj, event):
    """
    Return to Folder Contents
    """
    request = getRequest()
    try:
        folder = obj.getParentNode()
    except:
        return
    if folder == None:
        try:
            folder = api.portal.get()
        except:
            return
    elif getattr(obj, 'portal_type', None) == 'Plone Site':
        folder = obj

    if request:
        request.response.redirect('%s/folder_contents' % folder.absolute_url())

def back_to_folder_contents(event):
    request = getRequest()
    portal = api.portal.get()
    abs_url = portal.absolute_url()
    request.response.redirect('%s/folder_contents' %abs_url)

def replaceRichText(obj, attrStr):
    try:
        value = getattr(obj, attrStr, None).raw
        while 1:
            if '../resolveuid' in value:
                value = value.replace('../resolveuid', 'resolveuid')
            else:
                setattr(obj, attrStr, RichTextValue(value))
                break
    except:pass



def updateRichText(obj, event):
    replaceRichText(obj, 'body')
