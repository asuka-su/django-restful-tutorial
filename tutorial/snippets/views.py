from django.contrib.auth.models import User
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer, UserSerializer
from rest_framework import generics, permissions
from .permissions import IsOwnerOrReadOnly

"""
List all snippets, or create a new snippet.
"""
class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # override a perform_create() method allow us to modify how the instance is saved
    # 可以被视作在调用本有的save方法后，又调用了perform_create()方法作补充
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


"""
Retrieve, update or delete a snippet instance.
"""
class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, 
                          IsOwnerOrReadOnly]

'''
使用了rest_framework中预先集成的形式，使用方便，但是局限性相对较大。
它的上一层是一个使用mixins的东西，有类似于ListModelMixin的集成。
再上一层就是使用各种函数做到目标效果，会有比较多的重复代码。
Response也是一个好用的特性！
'''

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer