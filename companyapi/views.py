from django.http import HttpResponse
from django.http import HttpResponse,JsonResponse

def  home_page(Request):
    friends=[
        "Ankit"
         'Ravi'
         'had'
    ]
    
    return JsonResponse(friends ,safe=False)