from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from rest_framework import generics


from .models import Companies
from .serializers import CompaniesSerializer

class ModelList(generics.ListAPIView):
    queryset = Companies.objects.all()
    serializer_class = CompaniesSerializer
def model_list(request):
    data = Companies.objects.all()
    return render(request, 'list.html', {'data': data})