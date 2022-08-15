from django.shortcuts import render
from rest_framework import viewsets, filters
from .models import Company
from .serializers import CompanySerializer

class CompanyViewset(viewsets.ModelViewSet):
    queryset=Company.objects.all()
    serializer_class=CompanySerializer
    filter_backends=[filters.SearchFilter]
    search_fields=['id']


#for viewing the list of all employee visit-http://127.0.0.1:8000/api/company/
#there is search filter in the page to search by id
#for pages move to second page in the browsable api
#for running please install all requirements from requiremnts.txt
#for running you may also use container