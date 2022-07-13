from django.urls import path

from . import views

app_name= 'draft'

urlpatterns = [
    path('leak-draft-create/<int:category_id>/<int:subcategory_id>/', views.DraftLeakCreate.as_view(), name='leak-draft-create'),
    path('leak-draft-edit/<int:pk>/', views.DraftLeakUpdate.as_view(), name='leak-draft-edit'),
    path('leak-draft-list/', views.DraftLeakList.as_view(), name='leak-draft-list'),
    path('leak-draft-detail/<int:pk>/', views.DraftLeakDetail.as_view(), name='leak-draft-detail'),
    path('leak-draft-delete/<int:pk>/', views.DraftLeakDelete.as_view(), name='leak-draft-delete'),


    path('convert-draft-to-leak/<int:draft_id>/', views.ConvertDraftToLeak.as_view(), name='convert-draft-to-leak'),

]