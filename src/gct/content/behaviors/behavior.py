# -*- coding: utf-8 -*-
from plone.autoform.interfaces import IFormFieldProvider
from plone.autoform import directives
from plone.supermodel import model
from zope import schema
from zope.interface import alsoProvides
from plone.app.z3cform.widget import AjaxSelectFieldWidget
from gct.content import _
from plone.autoform.interfaces import IFormFieldProvider
from z3c.form.interfaces import IAddForm
from z3c.form.interfaces import IEditForm
from zope.interface import provider


@provider(IFormFieldProvider)
class ICategory(model.Schema):

    # categorization fieldset
    model.fieldset(
        'categorization',
        label=_(u'label_schema_categorization', default=u'Categorization'),
        fields=['category', 'subject'],
    )

    category = schema.Tuple(
        title=_(u'label_category', default=u'Category'),
        description=_(
            u'help_tags',
            default=u'Tags are commonly used for ad-hoc organization of ' +
                    u'content.'
        ),
        value_type=schema.TextLine(),
        required=False,
        missing_value=(),
    )
    directives.widget(
        'category',
        AjaxSelectFieldWidget,
        vocabulary='plone.app.vocabularies.Keywords'
    )

    subject = schema.Tuple(
        title=_(u'label_subject', default=u'Subject'),
        description=_(
            u'help_tags',
            default=u'Tags are commonly used for ad-hoc organization of ' +
                    u'content.'
        ),
        value_type=schema.TextLine(),
        required=False,
        missing_value=(),
    )
    directives.widget(
        'subject',
        AjaxSelectFieldWidget,
        vocabulary='plone.app.vocabularies.Keywords'
    )


    directives.omitted('subject', 'category')
    directives.no_omit(IEditForm, 'subject', 'category')
    directives.no_omit(IAddForm, 'subject', 'category')
