from django.contrib.auth.models import User
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer, UserSerializer
from rest_framework import generics, permissions, renderers, viewsets
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .permissions import IsOwnerOrReadOnly

'''
*List all snippets, or create a new snippet.
class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # override a perform_create() method allow us to modify how the instance is saved
    # 可以被视作在调用本有的save方法后，又调用了perform_create()方法作补充
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


*Retrieve, update or delete a snippet instance.
class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, 
                          IsOwnerOrReadOnly]
    

*an endpoint for the highlighted snippets
class SnippetHighlight(generics.GenericAPIView):
    queryset = Snippet.objects.all()
    renderer_classes = [renderers.StaticHTMLRenderer]

    def get(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

使用了rest_framework中预先集成的形式，使用方便，但是局限性相对较大。
它的上一层是一个使用mixins的东西，有类似于ListModelMixin的集成。
再上一层就是使用各种函数做到目标效果，会有比较多的重复代码。
Response也是一个好用的特性！

Replace the -List, -Detail, -Highlight view classes with a sigle class
'''
class SnippetViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]
    
    '''
    Notice that we've also used the @action decorator to create a custom action, named highlight. 
    This decorator can be used to add any custom endpoints that don't fit into the standard create/update/delete style.
    Custom actions which use the @action decorator will respond to GET requests by default. 
    We can use the methods argument if we wanted an action that responded to POST requests.
    '''
    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


'''
refactor our UserList and UserDetail views into a single UserViewSet. 
We can remove the two views, and replace them with a single class.
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
'''
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


'''now create an entry point to API'''
@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'snippets': reverse('snippet-list', request=request, format=format)
    })
