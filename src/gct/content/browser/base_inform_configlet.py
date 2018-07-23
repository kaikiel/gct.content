# -*- coding: utf-8 -*-
from gct.content import _
from plone.app.registry.browser.controlpanel import RegistryEditForm
from plone.app.registry.browser.controlpanel import ControlPanelFormWrapper
from zope import schema
from zope.interface import Invalid
from zope.interface import invariant
from plone.z3cform import layout
from z3c.form import form
from plone.directives import form as Form
import re


class IInform(Form.Schema):

    email = schema.Text(
        title=_(u'Your Email'),
        description=_(u'Display on Footer and Contact us page'),
        required=True,
    )
    cellphone = schema.Text(
        title=_(u'Your Cellphone'),
        description=_(u'Display on Footer and Contact us page'),
        required=True,
    )
    address = schema.Text(
        title=_(u'Your Address'),
        description=_(u'Display on Footer and Contact us page'),
        required=True
    )
    fax = schema.Text(
        title=_(u'Your Fax'),
        description=_(u'Display on Footer and Contact us page'),
        required=True
    )
    test = schema.TextLine(
        title=_(u'Subscribe Emails'),
        description=_(u'Used to receiving Email from Contact us page'),
        required=True
    )

    @invariant
    def email_invariant(data):
        com_email = data.email
        sub_email = data.test
        if com_email:
            for email in com_email.split('\r\n'):
                if not re.match(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$", email):
                    raise Invalid(_(u'Your Email is not valid!'))
        if sub_email and not re.match(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$", sub_email):
            raise Invalid(_(u'Subscribe Email is not valid!'))

class BasicInformControlPanelForm(RegistryEditForm):
    form.extends(RegistryEditForm)
    schema = IInform

CustomControlPanelView = layout.wrap_form(BasicInformControlPanelForm, ControlPanelFormWrapper)
CustomControlPanelView.label = _(u"Basic Inform")
