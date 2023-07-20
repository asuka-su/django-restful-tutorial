from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

"""
'''
If we're going to have a hyperlinked API, we need to make sure we name our URL patterns. Let's take a look at which URL patterns we need to name.

The root of our API refers to 'user-list' and 'snippet-list'.
Our snippet serializer includes a field that refers to 'snippet-highlight'.
Our user serializer includes a field that refers to 'snippet-detail'.
Our snippet and user serializers include 'url' fields that by default will refer to '{model_name}-detail', which in this case will be 'snippet-detail' and 'user-detail'.
'''

urlpatterns = [
    path('', views.api_root), 
    path('snippets/', views.SnippetList.as_view(), name='snippet-list'), 
    path('snippets/<int:pk>/', views.SnippetDetail.as_view(), name='snippet-detail'), 
    path('users/', views.UserList.as_view(), name='user-list'), 
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'), 
    path('snippets/<int:pk>/hightlight/', views.SnippetHighlight.as_view(), name='snippet-highlight')
]

urlpatters = format_suffix_patterns(urlpatterns)
"""

"""
snippet_list = SnippetViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
snippet_detail = SnippetViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
snippet_highlight = SnippetViewSet.as_view({
    'get': 'highlight'
}, renderer_classes=[renderers.StaticHTMLRenderer])
user_list = UserViewSet.as_view({
    'get': 'list'
})
user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})
'''Notice how we're creating multiple views from each ViewSet class, by binding the http methods to the required action for each view.'''

urlpatterns = format_suffix_patterns([
    path('', api_root),
    path('snippets/', snippet_list, name='snippet-list'),
    path('snippets/<int:pk>/', snippet_detail, name='snippet-detail'),
    path('snippets/<int:pk>/highlight/', snippet_highlight, name='snippet-highlight'),
    path('users/', user_list, name='user-list'),
    path('users/<int:pk>/', user_detail, name='user-detail')
])
"""

"""
Because we're using ViewSet classes rather than View classes, 
we actually don't need to design the URL conf ourselves. 
The conventions for wiring up resources into views and urls can be handled automatically, 
using a Router class. 
"""
# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet,basename="snippet")
router.register(r'users', views.UserViewSet,basename="user")

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]