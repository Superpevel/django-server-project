from operator import rshift
from os import name
import re
from django.views.generic.list import ListView
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import authentication, permissions

from .models import GreatQ
from libs.raz_search import raz_search_method
import json
from libs.div_search import dv_search
from libs.fib_search import fib_search
from libs.kas_search import solve_algo_kas
from libs.sr_search import solve_algo_sr
class QuotesView(ListView):
    model = GreatQ
    template_name  = "quotes.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

def index(request):

    return render(request, "index.html")


class BackEnd(APIView):

    def post(self, request):

        return Response(f"hello {request.POST.get('name')}")   

class BackEndQuote(APIView):

    def post(self, request):
        quote = request.POST.get('name')
        saves = GreatQ(name='Георгий',quote=quote,year=2022)
        saves.save()
        return Response(f"hello")   

class BackendRazSearch(APIView):

    def post(self, request):
        try:
            print(request.POST)
            a = int(request.POST.get('a'))
            b = int(request.POST.get('b'))
            e = float(request.POST.get('e'))
        except Exception as e:
            print(e)
            return Response('Убидитесь что в правильности введенных чисел ')
        method = request.POST.get('method')
        print("WHY ALL IS ALL")
        if method == 'raz':
            result = raz_search_method(b,a,e)
            return Response({'x': result[0],'y': result[1], 'Iterations': result[2]})
        elif method == 'div':
            result = list(dv_search(a,b,e))
            return Response({'result': result[0],'Iterations': result[1]})
        elif method == 'fib':
            result = fib_search(a,b,e)
            print(f'{result} check this' )
            return Response({'result': result[0],'Iterations': result[2]})




def optimization_first(request):

    return render(request, "optimization_first.html")



class BackendSecond(APIView):

    def post(self, request):
        try:
            print(request.POST)
            a = int(request.POST.get('a'))
            b = int(request.POST.get('b'))
            e = float(request.POST.get('e'))
        except Exception as e:
            print(e)
            return Response('Убидитесь что в правильности введенных чисел ')
        method = request.POST.get('method')
        print("WHY ALL IS SECOND")
        if method == 'dv':
            result = list(solve_algo_sr(a,b,e))
            return Response(result)
        elif method == 'kas':
            print('here')
            result = list(solve_algo_kas(b,a,e))
            return Response(result)
        return Response('No method checked')




def optimization_second(request):

    return render(request, "optimization_second.html")