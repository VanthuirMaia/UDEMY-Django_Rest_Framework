from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from ..models import Recipe
from ..serializers import RecipeSerializer


@api_view()
def recipe_api_list(request):
    recipes = Recipe.objects.get_published()[:10]
    serializer = RecipeSerializer(instance=recipes, many=True)
    return Response(serializer.data)

@api_view()
def recipe_api_detail(request, pk):
    recipes = Recipe.objects.get_published()[:10]
    serializer = RecipeSerializer(instance=recipes, many=True)
    return Response(serializer.data)