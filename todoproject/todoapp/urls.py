from django.urls import path
from . import views
urlpatterns = [

    path('',views.demo,name='demo'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('cvlistview/',views.listview.as_view(),name='cvlist'),
    path('cvdetailview/<int:pk>/',views.detailview.as_view(),name='cvdetail'),
    path('cvupdateview/<int:pk>/',views.updateview.as_view(),name='cvupdate'),
    path('cvdeleteview/<int:pk>/',views.deleteview.as_view(),name='cvdelete'),
]