# -*- coding: utf-8 -*-
from plone.dexterity.content import Container
from plone.supermodel import model
from zope.interface import implementer


class IProductimg(model.Schema):
    """ Marker interface for Productimg
    """


@implementer(IProductimg)
class Productimg(Container):
    """
    """
