from django.urls import path

from . import views



app_name = 'leak'

urlpatterns = [
    path('leak-detail/<int:pk>/', views.LeakDetail.as_view(), name='leak-detail'),
    path('', views.HomePage.as_view(), name='home'),
    path('category/<int:pk>/', views.CategoryLeakView.as_view(), name='category-leaks'),
    path('subcategory/<int:category_id>/<int:pk>/', views.SubcategoryLeakView.as_view(), name='subcategory-leaks'),
    path('category-create/', views.CategoryCreate.as_view(), name='category-create'),
    path('subcategory-create/<int:category_id>/', views.SubcategoryCreate.as_view(), name='subcategory-create'),

    path('leak-create/<int:category_id>/<int:subcategory_id>/', views.LeakCreate.as_view(), name='leak-create'),
]
