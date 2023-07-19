from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework import generics

"""
List all snippets, or create a new snippet.
"""
class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


"""
Retrieve, update or delete a snippet instance.
"""
class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

'''
使用了rest_framework中预先集成的形式，使用方便，但是局限性相对较大。
它的上一层是一个使用mixins的东西，有类似于ListModelMixin的集成。
再上一层就是使用各种函数做到目标效果，会有比较多的重复代码。
Response也是一个好用的特性！
'''