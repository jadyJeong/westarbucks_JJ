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


class ProductView(View):

    # Create
    def post(self, request):

        data     = json.loads(request.body)
        menu     = Menu.objects.create(name=data['menu'])
        # send create query to DB
        category = Category.objects.create(

                name=data['category'],
                menu=menu

        )

        product  = Drink.objects.create(

                name=data['product']['name'],
                category=category

        )

        return JsonResponse({'MESSAGE':'SUCCESS'}, status=201)


    # Read
    def get(self,request):
        
        products = Drink.objects.all()

        result  = []
        for product in products:
            dict = (
                {
                    'menu'    : product.category.menu.name,
                    'category': product.category.name,
                    'drink'   : product.category
                }
            ) 
            result.append(dict)

        return JsonResponse({'results':result},status=200)

    
    
    
    
class CategoryView(View):


