from django.http import HttpResponse,JsonResponse

def home_page(request):
    print("Home page requested")
    Words=[
        'hello',
        'world'
    ]
    return JsonResponse(Words,safe=False)