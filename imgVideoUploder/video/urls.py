from django.urls import path,include
from video import views
urlpatterns = [
    # path('',views.index, name='index' ),
    path('',views.home, name='home' ),
    path('delete/<int:id>',views.delete,name='delete')
]