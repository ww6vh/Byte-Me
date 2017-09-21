from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world!")

"""
def get_user(request):
	try:
        book_id=Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        raise Http404("Book does not exist")

    #book_id=get_object_or_404(Book, pk=pk)
    
    return render(
        request,
        'catalog/book_detail.html',
        context={'book':book_id,}
    )
"""

def get_user(pk, request): 
	return HttpResponse("Hello, world!")
	

