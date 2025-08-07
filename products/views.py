from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Item
from .serializers import ItemSerializer

'''
NOTE: Conside this as a reference and follow this same coding structure or format to work on you tasks
'''

# Create your views here.
class ItemView(APIView):

    def get(self, request):
        items = Item.objects.all()
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
            menu_items = Item.objects.all()
            serializer = ItemSerializer(menu_items, many=True )
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error":"Failed to retrive menu data", "details":str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

# template view for menu
def menu_page(request):
    """Render menu page with item displayed in html."""
    menu_items = [
        {"name":"Pizza", "price":10},
        {"name":"Chappathi", "price":5},
        {"name":"Fried Rice", "price":25},
    ]
    return render(request, 'menu.html', {'menu_items':menu_items})
