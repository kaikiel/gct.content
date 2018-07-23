# -*- coding: utf-8 -*-
from gct.content import _
from zope import schema
from plone.dexterity.content import Container
from plone.supermodel import model
from zope.interface import implementer
from plone.supermodel.directives import fieldset
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

    description = schema.Text(
        title=_(u'Description'),
        required=False,
    )

    body = RichText(
        title=_(u'Product Description'),
        required=False,
    )

    cover = NamedBlobImage(
        title=_(u"Cover Image"),
        required=True,
    )

    category = schema.TextLine(
	title=_(u'Category'),
	required=True,
    )

    subject = schema.TextLine(
	title=_(u'Subject'),
	required=True,
    )

    fieldset(_('Slider'), fields=['img1', 'img2', 'img3', 'img4', 'img5'])
    img1 = NamedBlobImage(
        title=_(u"Slider Image1"),
        required=False,
    )

    img2 = NamedBlobImage(
        title=_(u"Slider Image2"),
        required=False,
    )

    img3 = NamedBlobImage(
        title=_(u"Slider Image3"),
        required=False,
    )

    img4 = NamedBlobImage(
        title=_(u"Slider Image4"),
        required=False,
    )

    img5 = NamedBlobImage(
        title=_(u"Slider Image5"),
        required=False,
    )

