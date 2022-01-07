from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from libs.get_films import get_film
from core.models import Film
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import json
import time
from .serializers.films import FilmSerializer
import logging

options = Options()
options.headless = True

logger = logging.getLogger(__name__)

class Index(APIView):

    authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser]

    def get(self, request):
        get_film()

        return Response({2:'1'})

class ViewToken(APIView):

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        print(request.user)
        return Response({2:'1'})


class GetFilm(APIView):

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        request_list = json.loads(request.body)
        if request_list.get('name'):
            films = Film.objects.filter(name__icontains=request_list.get('name'))

        serializer = FilmSerializer(films, many=True)
        return Response(serializer.data)   

class GetFilmUrl(APIView):

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        logger.info("lol!!")
        request_list = json.loads(request.body)

        id = int(request_list.get('id'))

        film = Film.objects.get(id=id)
        driver = webdriver.Firefox(options=options)

        try:
            print(film.link)
            driver.get(film.link)
            time.sleep(2)

            driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
            element2 = driver.find_element(By.XPATH, """/html/body/div/pjsdiv/pjsdiv[1]/video""")

        
            print(element2.get_attribute('src'))

            itog = str(element2.get_attribute('src'))

            a1 = itog.split('/240.mp4') 
            a2 = str(a1[0]) + "/720.mp4"

        except Exception as e:
            logger.info(e)
            print('Error')

        driver.quit()
        return Response({'url': a2})


