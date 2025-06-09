from django.urls import path
from .views import  announcements_list , announcement_detail



app_name = "guidance"
urlpatterns = [
    path('news/',announcements_list , name="total_news"  ) ,  
    path('news/<int:pk>/', announcement_detail, name='detail_news'),
]
