# board
# 모든사람들이 조회할 수 있는 게시판

from django.urls import path
from . import views
app_name = "board"
urlpatterns = [
    path('',views.index, name = 'index'),
    path('new/',views.new, name = 'new'),
    path('create/',views.create, name = 'create'),
    path('detail/<str:no>',views.detail, name='detail'),
    path('delete/<str:no>',views.delete, name='delete'),
    path('update/<str:no>',views.update, name='update'),
    path('updated',views.updated, name='updated'),
    path('newComment/<str:no>',views.newComment, name = 'newComment'),
    path('deleteComment/<str:no>',views.deleteComment, name = 'deleteComment'),
    path('updateComment/<str:no>',views.updateComment, name = 'updateComment'),
    path('<int:article_pk>/like',views.like,name='like'),
]
