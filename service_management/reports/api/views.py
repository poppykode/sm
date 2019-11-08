from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK,
    HTTP_204_NO_CONTENT,
    HTTP_201_CREATED,
    HTTP_405_METHOD_NOT_ALLOWED
)
from rest_framework.response import Response

from .serializers import EnquirySerializer,SalesFunnelSerialize
from enquiries.models import Enquiry
from projects.models import ProjectInstallationAssessement

@csrf_exempt
@api_view(['GET',])
def sales_funel(request):
    if request.method== 'GET':
        qs = Enquiry.objects.all()
        labels = ['New', 'Open', 'Won','Lost','Assements']
        new = qs.filter(status='new')
        open = qs.filter(status='open')
        won = qs.filter(status='won')
        lost = qs.filter(status='lost')
        assement = qs.filter(status='assement')
        new_ = new.count()
        open_ = open.count()
        won_ = won.count()
        lost_ =lost.count()
        qs_ = qs.count()
        assement_ = assement.count()
        data = [new_,open_,won_,lost_,assement_]
        sf = {
            'labels':labels,
            'data':data   
        }
        return Response(sf)
        message={'error':'method not allowed.'}
    return Response(message,status= HTTP_405_METHOD_NOT_ALLOWED)
    
@csrf_exempt
@api_view(['GET',])
def project_overview(request):
    if request.method== 'GET':
        qs = ProjectInstallationAssessement.objects.all()
        assements = qs.filter(type='assement').count()
        projects = qs.filter(type='project').count()
        installations = qs.filter(type='installation').count()
        labels = ['Assements', 'Projects', 'Installations']
        data = [assements,projects,installations]
        sf = {
            'labels':labels,
            'data':data   
        }
        return Response(sf)
        message={'error':'method not allowed.'}
    return Response(message,status= HTTP_405_METHOD_NOT_ALLOWED)




