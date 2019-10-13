from django.urls import path
from django.http import HttpResponse

SECRET_KEY = '**$o!d&7b!swmk(+p59!p(8b0^#ma8#x5zq&#g4az=&ie1_7bs'
DEBUG = True
ROOT_URLCONF = __name__


def home(request):
    return HttpResponse('Hello world!', content_type='text/plain')


urlpatterns = [path('', home)]
