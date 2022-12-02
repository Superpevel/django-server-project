from operator import rshift
from os import name
import re
from django.views.generic.list import ListView
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import authentication, permissions
from django.core.paginator import Paginator
from .models import GreatQ, FinOtchet, FinOtchetStats, FinOtchetRows
from libs.raz_search import raz_search_method
import json
from libs.div_search import dv_search
from libs.fib_search import fib_search
from libs.kas_search import solve_algo_kas
from libs.sr_search import solve_algo_sr
import openpyxl
from django.shortcuts import redirect


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

def fin_otchet(request):
    logistics_list = []
    sells_list = []
    stats = {}
    if request.method == 'POST':
        excel_file = request.FILES["excel_file"]
        wb = openpyxl.load_workbook(excel_file)
    
        worksheet = wb["Sheet1"]
        print(worksheet)
        excel_data = list()
        # iterating over the rows and
        # getting value from each cell in row
        for row in worksheet.iter_rows(min_row=2):
            row_data = list()
            # article = row[3].value
            row_data = {
                'article': row[3].value,
                'type': row[10].value,
                'date': row[11].value,
                'wb_price': row[15].value,
                'selling_price': row[19].value,
                'kvv': row[21].value,
                'reward': row[29].value,
                'logistics_amount': row[32].value,
            }
            if row_data['type'] == 'Логистика':
                logistics_list.append(row_data)
            elif row_data['type'] == 'Продажа':
                sells_list.append(row_data)
        
        for sell in sells_list:
            if not stats.get(sell['article']):
                stats[sell['article']] = {'sells': [sell] , 'avarage_price': sell['reward'], 'logistics_avarage': 0, 'amount': 1, 'logistics_amount': 0}
            else:
                stats[sell['article']]['sells'].append(sell)
                stats[sell['article']]['avarage_price'] = (stats[sell['article']]['avarage_price'] + sell['reward']) // 2
                stats[sell['article']]['amount'] =  stats[sell['article']]['amount'] + 1
        for log in logistics_list:
            if not stats.get(log['article']):
                stats[log['article']] = {'sells': [] , 'avarage_price': 0, 'logistics_avarage': log['logistics_amount'], 'logistics_amount': log['logistics_amount'],'amount': 0}
            else:
                stats[log['article']]['logistics_avarage'] = (stats[log['article']]['logistics_avarage'] + log['logistics_amount']) // 2 if stats[log['article']]['logistics_avarage'] else log['logistics_amount']
                stats[log['article']]['logistics_amount'] = stats[log['article']]['logistics_amount'] + log['logistics_amount']
        otchet = FinOtchet.objects.create()
        for k,v in stats.items():
            stat = FinOtchetStats.objects.create(article=k, avarage_price=v['avarage_price'], logistics_avarage=v['logistics_avarage'], finotchet=otchet, logistics_return_amount=0, logistics_amount=v['logistics_amount'], buyout_amount=v['amount'])
            for sell in v['sells']:
                FinOtchetRows.objects.create(article=sell['article'],type=sell['type'], date=sell['date'], wb_price=sell['wb_price'], selling_price=sell['selling_price'], kvv=sell['kvv'], reward=sell['reward'], logistics_amount=sell['logistics_amount'], stat=stat)
        return redirect(f'fin_otchet/{otchet.id}')
        # for sell in sells_list:
        #     if not stats.get(sell['article']):
        #         stats[sell['article']] = {}
        # print(sells_list)
        # print('-----------------------')
        # print(logistics_list)

    return render(request, "fin_otchet.html", {'sells': sells_list, 'logistics': logistics_list, 'stats': stats})

def optimization_first(request):
    return render(request, "optimization_first.html")


def fin_detail(request, id):
    otchet_stats = FinOtchetStats.objects.filter(finotchet=id)
    
    return render(request, "fin_otchet_1.html", {'id': id, 'stats': otchet_stats})

def fin_details(request, otchet_id, id):
    otchet_stats = FinOtchetRows.objects.filter(stat=id)
    return render(request, "fin_details.html", {'rows': otchet_stats})


class FinOtchetRowsListView(ListView):
    template_name = 'fin_details.html'
    model = FinOtchetRows
    paginate_by = 100  # if pagination is desired

    def get_queryset(self):
        print(self.request.GET)
        id = self.kwargs['id']
        queryset = FinOtchetRows.objects.filter(stat=id)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['now'] = timezone.now()
        return context

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