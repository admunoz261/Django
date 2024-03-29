from django.http import HttpResponse
from datetime import datetime
import json 

def hello_word(request):
    
    return HttpResponse('Hello, World! Current server time is {now}'.format(
        now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    ))

def sort_integers(request):
    numbers = [int(i) for i in request.GET['numbers'].split(',')]
    sorted_ints = sorted(numbers)
    data = {
        'status': 'ok',
        'numbers': sorted_ints,
        'message': 'Integer sorted successfully'
    }
    return HttpResponse(json.dumps(data, indent=4), content_type='application/json')
    
def say_hi(request,name,age):
    if age < 12:
        message = "I`m sorry {}, you are not allowed here".format(name)
    else:
        message = 'Hello!, {}! Welcome to platzigram'.format(name)
    return HttpResponse(message)