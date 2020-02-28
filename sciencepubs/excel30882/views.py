from django.shortcuts import render
from django.http import HttpResponse
from .models import Publication, PublicationCategory
from pandas import read_excel
import xlrd
import requests
# Create your views here.
def index(request):
    return render(request, "excel30882/index.html")

def importCategoryExcel(request):
  PublicationCategory.objects.all().delete()
  my_sheet='Kategorie'
  file_name= 'data.xlsx'
  workbook=xlrd.open_workbook(file_name)
  worksheet = workbook.sheet_by_name(my_sheet)
  total_cols=worksheet.ncols
  total_rows=worksheet.nrows
  table = list()
  record = list()
  for x in range(total_rows):
    for y in range(total_cols):
      record.append(worksheet.cell(x,y).value)
    table.append(record)
    record = []
    x += 1
  
  for x in table:
    #a=PublicationCategory()
    #a.PublicationCategoryName=x[0]
    #a.PublicationCategoryId=x[1]
    #a.save()
    api_url = "http://127.0.0.1:8000/api/sciencepublications/categories/"
    data = {'name': x[0],
            'catind': x[1]}
    requests.post(api_url, data=data)


  #return HttpResponse(f"Dodano kategorie")

def importPublicationsExcel(request):
  Publication.objects.all().delete()
  file_name= 'data.xlsx'
  workbook=xlrd.open_workbook(file_name)
  my_sheet='Czasopisma'
  worksheet = workbook.sheet_by_name(my_sheet)
  total_cols=worksheet.ncols
  total_rows=worksheet.nrows
  table = list()
  record = list()
  for x in range(total_rows):
    for y in range(total_cols):
      record.append(worksheet.cell(x,y).value)
    table.append(record)
    record = []
    x += 1

  kategorieId=[101,102,103,104,105,106,107,201,202,203,204,205,206,207,208,209,301,302,303,304,401,402,403,404,405,501,502,503,504,505,506,507,508,509,510,511,601,602,603,604,605,606,607,701]

  for x in table:
    #a=Publication()
    #a.publicationName=x[1]
    #a.publicationIssn=x[2]
    #a.publicationEissn=x[3]
    #a.publicationName2=x[4]
    #a.publicationIssn2=x[5]
    #a.publicationEissn2=x[6] 
    #a.PublicationPoints=x[7]
    #a.save()

    api_url = "http://127.0.0.1:8000/api/sciencepublications/publications/"
    data = {'name': x[1],
            'issn': x[2],
            'eissn': x[3],
            'name2': x[4],
            'issn2': x[5],
            'eissn2': x[6],
            'points': x[7]}
    requests.post(api_url, data=data)

    i=0
    while i<44:
      if x[8+i]=='x':
        kategoria=PublicationCategory.objects.get(PublicationCategoryId=kategorieId[i])
        a.PublicationCategories.add(kategoria)
      i += 1
    a.save()
  #return HttpResponse(f"dodano czasopisma z excela")

def importDataExcel(request):
    importCategoryExcel(request)
    importPublicationsExcel(request)
    return HttpResponse(f"Dodano kategorie i czasopisma")
