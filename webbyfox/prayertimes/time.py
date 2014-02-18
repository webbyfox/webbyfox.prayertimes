from webbyfox.prayertimes import MessageFactory as _
from five import grok
from plone.app.textfield import RichText
from plone.supermodel import model
from zope import schema

# importing class to customising add view 
from plone.dexterity.browser.add import DefaultAddForm, DefaultAddView
from z3c.form import interfaces

# importing for fieldset
from plone.directives import form

#from zope import interface

# import for view class
from plone.dexterity.browser.add import DefaultAddForm, DefaultAddView

#from z3c.form.browser.textlines import TextLinesFieldWidget

#from interfaces import IExcludeFromNavigationForm

# import for edit form
from plone.directives import dexterity, form

from plone.namedfile.field import NamedBlobImage, NamedBlobFile

# widget for datetime
from collective.z3cform.datetimewidget.widget_datetime import Datetimewidget

class ITime(model.Schema):
    """
    Prayer time content types for Masjid. 
    """
    form.widget(title='Datetimewidget')
    title = schema.Date(
        title=_(u"Date which you would like to add prayer times"),
        required = False,
        )

    fajr_beings  = schema.Timedelta(
        title = _("Fajr begins time"),
        required=False,)
  
    fajr_jamaat = schema.Timedelta(
	   title = _("Fajr jamaat time"),
	   required=False,)
    
    dhor_begins = schema.Timedelta(
        title = _("Dhor begins"),
        required=False,)
    
    dhor_jamaat = schema.Timedelta(
        title = _("Dhor jamaat time"),
        required=False,)

    asar_begins = schema.Timedelta(
        title = _("Asar begins"),
        required=False,)

    asar_jamaat = schema.Timedelta(
        title = _("Asar jamaat time"),
        required=False,)
    
    magrib_begins = schema.Timedelta(
        title = _("Magrib begins"),
        required=False,)

    magrib_jamaat = schema.Timedelta(
        title = _("Magrib jamaat time"),
        required=False,) 
    
    esha_begin  = schema.Timedelta(
        title = _("Esha begins"),
        required=False,)

    esha_jamaat = schema.Timedelta(
        title = _("Esha jamaat time"),
        required=False,)
   


    upload_batch_file = NamedBlobFile(
		title = _(u"Upload Prayer times File"),
        description = _(u"for sample format, look into DOCS/prayertimessample/"),
        required = False,
		)

#@form.default_value(field = IExcludeFromNavigationForm['exclude_from_nav'])
#def excludeFromNavDefaultValue(data):
#    return True    
    
class View(grok.View):
    grok.context(ITime)
    grok.require('zope2.View')
    grok.name('view')


class AddForm(DefaultAddForm):
    
   # enable_form_tabbing = True
    
    def updateWidgets(self):
        super(AddForm, self).updateWidgets()
        

class AddView(DefaultAddView):
    form = AddForm

    
class EditForm(dexterity.EditForm):
    
    grok.context(ITime)
   # enable_form_tabbing = True

    def updateWidgets(self):
        dexterity.EditForm.updateWidgets(self)
        
