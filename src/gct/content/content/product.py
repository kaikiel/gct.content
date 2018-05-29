# -*- coding: utf-8 -*-
from gct.content import _
from plone.dexterity.content import Container
from plone.supermodel import model
from zope.interface import implementer
from zope import schema
from plone.app.textfield import RichText
from plone.namedfile.field import NamedBlobImage, NamedBlobFile, NamedImage

class IProduct(model.Schema):
    name = schema.TextLine(
        title=_(u'Name'),
        required=True,
    )

    modelNo = schema.TextLine(
        title=_(u'Model No'),
        required=False,
    )

    beApplicable = schema.TextLine(
        title=_(u'Be Applicable'),
        required=False,
    )

    characteristic = schema.TextLine(
        title=_(u'Characteristic'),
        required=False,
    )

    description = RichText(
        title=_(u'Description'),
        required=False,
    )

    cover = NamedBlobImage(
        title=_(u"Cover Image"),
        required=False,
    )

