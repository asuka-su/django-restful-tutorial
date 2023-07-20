from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

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