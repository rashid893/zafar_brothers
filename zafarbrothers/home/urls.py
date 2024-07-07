""
from django.contrib import admin
from django.urls import path,include
from home import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("",views.home,name="home"),
    path("module1/",views.module1,name="module1"),
    path("module2/",views.module2,name="module2"),
    path("module3/",views.module3,name="module3"),
    path("module4/",views.module4,name="module4"),
    path("query_module4/",views.query_module4,name="query_module4"),
    path("entry_module4/",views.entry_module4,name="entry_module4"),
    path("module6_stockout/",views.module6_stockout,name="module6_stockout"),
   # path("product_average/",views.product_average,name="product_average"),
    

    path("views_data_module1/",views.views_data_module1,name="views_data_module1"),
    path("views_data_module2/",views.views_data_module2,name="views_data_module2"),
    path("views_data_module3/",views.views_data_module3,name="views_data_module3"),
    path("views_data_module4/",views.views_data_module4,name="views_data_module4"),
    path("views_data_module6/",views.views_data_module6,name="views_data_module6"),


  #  path("module1products/",views.moduel1products,name="module1products"),



]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

