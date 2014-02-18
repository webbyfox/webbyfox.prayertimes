from webbyfox.prayertimes.interfaces import IExcludeFromNavigationForm
from zope.interface import implements

class ExcludeFromNavigationForm(object):
    implements(IExcludeFromNavigationForm)