# -*- coding: utf-8 -*-
from gct.content import _
from zope import schema
from plone.dexterity.content import Container
from plone.supermodel import model
from zope.interface import implementer
from plone.app.textfield import RichText
from z3c.relationfield.schema import RelationChoice, RelationList
from plone.namedfile.field import NamedBlobImage, NamedBlobFile, NamedImage


class IProduct(model.Schema):
    title = schema.TextLine(
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

    body = RichText(
        title=_(u'Body'),
        required=False,
    )

    cover = NamedBlobImage(
        title=_(u"Cover Image"),
        required=False,
    )

    category = schema.TextLine(
	title=_(u'Category'),
	required=False,
    )

    subject = schema.TextLine(
	title=_(u'Subject'),
	required=False,
    )
