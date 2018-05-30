# -*- coding: utf-8 -*-
from gct.content import _
from zope import schema
from plone.dexterity.content import Container
from plone.supermodel import model
from zope.interface import implementer
from plone.namedfile.field import NamedBlobImage, NamedBlobFile, NamedImage


class IProductimg(model.Schema):
    image = NamedBlobImage(
        title=_(u"Image"),
        description=_(u"Add image in 'Product' content"),
    )
