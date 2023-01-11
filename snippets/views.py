from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework import mixins
from rest_framework import generics

"""
Using the mixin classes we've rewritten the views to use slightly less code than before, 
but we can go one step further. REST framework provides a set of already mixed-in generic 
views that we can use to trim down our views.py module even more.
"""

"""
List all code snippets, or create a new snippet.
"""
class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

"""
Retrieve, update or delete a code snippet.
"""
class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
