import json

from django.views import View
from django.http import JsonResponse

from products.models import Drink



# wecode convention : "functionname+View"

# this class inheriting View class

class DrinksView(View):

    def post(self,request):
        pass

    # def get(self,request):
        
    #     drinks = Drink.objects.all()
    #     results = []

    #     for drink in drinks:
    #         results.append(
    #             {
    #                 "menu"    :product.category.menu.name,
    #                 "category":product.category.name,
    #                 "product" :product.name
    #             }
    #         )
    #     return JsonResponse({'results':results},status=200)

    
    
    
    




