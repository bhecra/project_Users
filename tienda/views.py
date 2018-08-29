"""Platzigram views"""

from django.http import HttpResponse, JsonResponse
#Utilities
from datetime import datetime
import json



def hello_world_view(request):

    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse('Hi, Current server time is {now}'.format(now = str(now)))

def sort_view(request):
    
    numbers = request.GET["number"].split(',')
    #import pdb; pdb.set_trace()
    c = [ int(number) for number in numbers ]
    sorted_data = sorted(c)
    data = {
        'status' : 'Ok',
        'numbers' : sorted_data,
        'message' : 'Integers sorted successfully.',
    }
    return HttpResponse(
        json.dumps(data, indent=4), 
        content_type='application/json')
    
def say_hi_view(request, name, age):

    if age < 12:
        message = 'sorry {}, you not allowed here'.format(name)
    else:
        message = "Hello {}, welcome".format(name)
    return HttpResponse(message)