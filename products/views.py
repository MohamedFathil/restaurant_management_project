from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.paginator import Paginator

from .models import MenuItem, MenuCategory
from .serializers import ItemSerializer, MenuCategorySerializer

'''
NOTE: Conside this as a reference and follow this same coding structure or format to work on you tasks
'''
class MenuCategoryView(APIView):
    def get(self, request):
        """Fetch all menu categories with error handling"""
        try:
            categories = MenuCategory.objects.all()
            serializer = MenuCategorySerializer(categories, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {'error':'Failed to retrieve categories', 'details':str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

class MenuItemsByCategoryView(APIView):
    def get(self, request):
        """Fetch menu items filtered by category"""
        category_name = request.query_params.get('category', None)

        if not category_name:
            return Response(
                {'error':'category query parameter is required'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            menu_items = MenuItem.objects.filter(
                category__name__iexact=category_name, available=True
            )
            if not menu_items.exists():
                return Response(
                    {'message':'No items found for this category'},
                    status=status.HTTP_404_NOT_FOUND
                )
            serializer = ItemSerializer(menu_items, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {'error':'Faliled to fetch items by category','details':str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

class ItemView(APIView):
    def get(self, request):
        items = MenuItem.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# API View for menu items
class MenuItemView(APIView):
    def get(self, request):
        """fetch all menu items with error handling"""
        try:
            menu_items = MenuItem.objects.all()
            serializer = ItemSerializer(menu_items, many=True )
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error":"Failed to retrive menu data", "details":str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

# template view for menu
def menu_page(request): 
    """Render menu page with item displayed in html."""
    menu_items = MenuItem.objects.all()
    query = request.GET.get('q','').strip()
    paginator = Paginator(menu_items, 8)
    if query:
        menu_items = menu_items.filter(name__icontains=query)
    
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    breadcrumb = [
        {'name':'Home','url':'/'},
        {'name':'Menu', 'url':'/menu/'}
    ]
    return render(request, 'menu.html', {'menu_items':menu_items,'breadcrumb':breadcrumb,'page_obj':page_obj,'query':query})
