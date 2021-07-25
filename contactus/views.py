from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_headers
from django.views.generic import TemplateView
from contactus.models import Contact
from django.core.mail import send_mail
from functools import lru_cache


@method_decorator(vary_on_headers('User-Agent', 'Cookie'), name='dispatch')
@method_decorator(cache_page(60 * .167, cache="default"), name='dispatch')
@method_decorator(lru_cache(maxsize=None), name='dispatch') 
class ContactUs(TemplateView):
    template_name = "contactus/contactus.html"


@vary_on_headers('User-Agent', 'Cookie')
@cache_page(60 * .167, cache="default")
def submit_query(request):
    contact = Contact()
    contact.name = request.POST.get('name')
    contact.email = request.POST.get('email')
    contact.subject = request.POST.get('subject')
    contact.query = request.POST.get('message')
    contact.resolved = False
    contact.save(using='contact')
    message = """ Dear """ + contact.name + """

        Thank you for letting us know about your issue and sorry for inconvenience. We will surely get back to you as soon as possible and also thank you for
        using our services.

        Sincerely,  
        Social Service Team
    """
    send_mail(contact.subject, message, 'dinesh.n@ahduni.edu.in', [contact.email])
    return redirect('/')
