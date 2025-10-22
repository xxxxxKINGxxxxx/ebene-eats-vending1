from django.http import HttpResponse
from django.template import loader

def EbeneEats(request):
    template = loader.get_template('vending/firstproject.html')
    return HttpResponse(template.render({}, request))
