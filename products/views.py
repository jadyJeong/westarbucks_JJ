import json

from products.models import Menu, Category, Drink
from django.views import View
from django.http import JsonResponse


from django.views import View
from django.http import JsonResponse

from products.models import *


# wecode convention : "functionname+View"

# this class inheriting View class

# - Category 생성 기능
# - Category 리스트 반환 기능
# - Product 생성 기능
# - Product 리스트 반환 기능

# Product 클래스가 가 여기서는 Drink 입니다.


# Product View CRUD methods.
class ProductView(View):

    # Create
    def post(self, request):

        data = json.loads(request.body)
        
        # send create query to DB
        drink = Drink.objects.create(

                category     = data['category'],
                korean_name  = data[''],
                english_name = data['english_name'],
                description  = data['description'],

        )

        return JsonResponse({'MESSAGE':'SUCCESS'}, status=201)


    # Read
    def get(self,request):
        
        products = Drink.objects.all()

    # serialize list to dict before returning as Jason
        results  = []
        for product in products:
            preprocess = (
                {
                'category'     : Drink.category,
                'korean_name'  : Drink.korean_name,
                'english_name' : Drink.english_name,
                'description'  : Drink.description
                }
            ) 
            results.append(preprocess)

        return JsonResponse({'results are ':results},status=200)
    

# Category View CRUD methods.
class CategoryView(View):

    # Create
    def post(self, request):

        data = json.loads(request.body)
        
        # send create query to DB
        category = Category.objects.create(
                name    = data['name'],
                menu    = data['menu']
        )

        return JsonResponse({'MESSAGE':'SUCCESS'}, status=201)


    # Read
    def get(self,request):
        
        categories = Category.objects.all()

    # serialize list to dict before returning as Jason
        results  = []
        for category in categories :
            preprocess = (
                {
                'name'    : Category.name,
                'menu'    : Category.menu
                }
            ) 
            results.append(preprocess)

        return JsonResponse({'results are ':results},status=200)
    
    
