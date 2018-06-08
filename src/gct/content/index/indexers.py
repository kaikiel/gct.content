#!/usr/bin/python
# -*- coding: utf-8 -*-

from plone.indexer.decorator import indexer
from gct.content.content.product import IProduct
from plone.app.contenttypes.interfaces import INewsItem

@indexer(IProduct)
def product_subject(obj):
    return obj.subject  

@indexer(IProduct)
def product_category(obj):
    return obj.category 

