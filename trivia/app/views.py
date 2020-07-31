from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
class NameViewSet(viewsets.ViewSet):
    def list(self,request):
        namelist = Name.objects.all()
        page = request.GET.get('page')
        data=[]
        paginator = Paginator(namelist, 1)
        total_pages = paginator.num_pages
        try:
            namelist = paginator.page(page)
        except EmptyPage:
            namelist = paginator.page(1)
        except PageNotAnInteger:
            namelist = paginator.page(1)       
        for namelists in namelist:
            data.append({
                'your_Name':namelists.your_Name
            })
        return Response({'data list':data})
    def retrieve(self, request, pk=None):
        dataname=Name.objects.get(id=pk) 
        data=[{
            'your_Name':dataname.your_Name
        }]
        return Response({'user retrieve':data})
    def destroy(self, request, pk=None):
        nameset=Name.objects.filter(id=pk).delete()
        return Response({'Successfully data delete'})
    def update(self, request, pk=None):
        your_Name=request.data.get('your_Name')
        if not your_Name:
            return Response({'your_Name':'enter your your_Name'})       
        updatename=Name.objects.get(id=pk)
        updatename.your_Name=your_Name
        updatename.save()
        return Response({'data update':'data save'})      
    def create(self,request):
        usercreate = Name()
        usercreate.your_Name=request.data.get('your_Name')
        usercreate.save()
        return Response({'Create Data'})
class CricketerViewSet(viewsets.ViewSet):
    def list(self,request):
        cricketerlist = Cricketer.objects.all()
        page = request.GET.get('page')
        data=[]
        paginator = Paginator(cricketerlist, 1)
        total_pages = paginator.num_pages
        try:
            cricketerlist = paginator.page(page)
        except EmptyPage:
            cricketerlist = paginator.page(1)
        except PageNotAnInteger:
            cricketerlist = paginator.page(1)
        data=[]
        for cricketerlists in cricketerlist:
            data.append({
                'best_Cricketer':cricketerlists.best_Cricketer
            })
        return Response({'data list':data})
    def retrieve(self, request, pk=None):
        cricketeretrieve=Cricketer.objects.get(id=pk) 
        data=[{
            'best_Cricketer':cricketeretrieve.best_Cricketer
        }]
        return Response({'user retrieve':data})
    def destroy(self, request, pk=None):
        cricketerset=Cricketer.objects.filter(id=pk).delete()
        return Response({'Successfully data delete'})
    def update(self, request, pk=None):
        best_Cricketer=request.data.get('best_Cricketer')
        if not best_Cricketer:
            return Response({'best_Cricketer':'enter your best_Cricketer'})       
        cricketerupdate=Cricketer.objects.get(id=pk)
        cricketerupdate.best_Cricketer=best_Cricketer
        cricketerupdate.save()
        return Response({'data update':'data save'})      
    def create(self,request):
        cricketercreate = Cricketer()
        cricketercreate.best_Cricketer=request.data.get('best_Cricketer')
        cricketercreate.save()
        return Response({'Create Data'})
class FlagViewSet(viewsets.ViewSet):
    def list(self,request):
        flaglist = Flag.objects.all()
        page = request.GET.get('page')
        data=[]
        paginator = Paginator(flaglist, 1)
        total_pages = paginator.num_pages
        try:
            flaglist = paginator.page(page)
        except EmptyPage:
            flaglist = paginator.page(1)
        except PageNotAnInteger:
            flaglist = paginator.page(1)
        data=[]
        for flaglists in flaglist:
            data.append({
                'indian_National_Flag':flaglists.indian_National_Flag
            })
        return Response({'data list':data})
    def retrieve(self, request, pk=None):
        flagretrieve=Flag.objects.get(id=pk) 
        data=[{
            'indian_National_Flag':flagretrieve.indian_National_Flag
        }]
        return Response({'user retrieve':data})
    def destroy(self, request, pk=None):
        flagset=Flag.objects.filter(id=pk).delete()
        return Response({'Successfully data delete'})
    def update(self, request, pk=None):
        indian_National_Flag=request.data.get('indian_National_Flag')
        if not indian_National_Flag:
            return Response({'indian_National_Flag':'enter your indian_National_Flag'})       
        flagupdate=Flag.objects.get(id=pk)
        flagupdate.indian_National_Flag=indian_National_Flag
        flagupdate.save()
        return Response({'data update':'data save'})      
    def create(self,request):
        flagcreate = Flag()
        flagcreate.indian_National_Flag=request.data.get('indian_National_Flag')
        flagcreate.save()
        return Response({'Create Data'})
# class FlagViewSet(viewsets.ViewSet):
#     def list(self,request):
#         flaglist = Flag.objects.all()
#         data=[]
#         for flaglists in flaglist:
#             data.append({
#                 'indian_National_Flag':flaglists.indian_National_Flag
#             })
#         return Response({'data list':data})
class FinishViewSet(viewsets.ViewSet):
    def list(self,request):
        data=[]
        return Response({'data list':data})
    def retrieve(self, request, pk=None):
        finishretrieve=Finish.objects.get(id=pk) 
        data=[{
            'created_at':finishretrieve.created_at,
            'your_Name':finishretrieve.nameforo.your_Name,
            'best_Cricketer':finishretrieve.cricketerforo.best_Cricketer,
            'indian_National_Flag':finishretrieve.flagforo.indian_National_Flag
        }]
        return Response({'user retrieve':data})

class SummaryViewSet(viewsets.ViewSet):
    def list(self,request):
        summarylist = Summary.objects.all()
        page = request.GET.get('page')
        data=[]
        paginator = Paginator(summarylist, 1)
        total_pages = paginator.num_pages
        try:
            summarylist = paginator.page(page)
        except EmptyPage:
            summarylist = paginator.page(1)
        except PageNotAnInteger:
            summarylist = paginator.page(1)
        data=[]
        for summarylists in summarylist:
            data.append({
                'created_at':summarylists.finishfor.created_at,
                'your_Name':summarylists.namefor.your_Name,
                'best_Cricketer':summarylists.cricketerfor.best_Cricketer,
                'indian_National_Flag':summarylists.flagfor.indian_National_Flag,
            })
        return Response({'data list':data})
                                    