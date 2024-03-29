from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# from django.http import HttpResponse
from django.http import JsonResponse
# Create your views here.
@csrf_exempt 
def chat(request):
        if request.method == 'POST':
         message = request.POST.get('message')
         print(message)
         data = [
         {'message': 'Hello...This is a simple message. The model is in a development phase. Every Time it will generate the same response for your query. Please wait for the full development of this Chat-Bot.',
         'url': 'https://github.com/prabhjot-arora31/D_C/'}]
         return JsonResponse(data,safe=False)
        elif request.method == 'GET':
         return render(request,'home.html')
        else:
         print('Only POST method is allowed')
         return JsonResponse({'message':'error'})
def contact(request):
    return render(request,'contact.html')