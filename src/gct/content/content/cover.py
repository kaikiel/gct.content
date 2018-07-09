# -*- coding: utf-8 -*-
from gct.content import _
from plone.dexterity.content import Container
from plone.supermodel import model
from zope.interface import implementer
from zope import schema
from plone.app.textfield import RichText
from z3c.relationfield.schema import RelationChoice, RelationList
from plone.namedfile.field import NamedBlobImage, NamedBlobFile, NamedImage
from plone.app.vocabularies.catalog import CatalogSource


class ICover(model.Schema):
    title = schema.TextLine(
        title=_(u'Title'),
        required=True,
    )

    feature = RelationList(
        title=_(u"Featured Products"),
        default=[],
        value_type=RelationChoice(
            title=_(u"Related"),
            source=CatalogSource(portal_type='Product')
        ),
        required=True,
    )


@implementer(ICover)
class Cover(Container):
    """
    """

