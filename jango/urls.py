"""
URL configuration for jango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('d',views.fun),
    # path('k',views.fun1),
    # path('t',views.fun2),
    # path('i',views.fun3),
    # path('z',views.pro),
    # path('b',views.fun4),
    # path('c',views.funct),
    # path('bookk',views.bk),
    # path('bk',views.display),
    # path('e',views.empp,name='x'),
    # path('ee',views.add),
    # path('pr',views.product,name='p'),
    # path('v',views.add_pr),
    # path('del/<int:id>',views.deletee,name='uid'),
    # path('upd/<int:id>',views.updatee,name='id'),
    # path('cus',views.view_cust,name='t'),
    # path('de/<int:id>',views.delt,name='id'),
    # path('adcus',views.adcus),
    # # path('up/<int:id>',views.updt,name='cid'),
    # path('vp',views.vpost,name='m'),
    # path('dp/<int:id>',views.dpost,name='pid'),
    # path('apk',views.apost),
    # # path('upk/<int:id>',views.upost,name='ubid'),
    
    
    # path('prk',views.vi_pro,name='f'),
    # path('xc',views.vi_add),

    
    # path('vbk',views.vi_bk,name='s'),
    # path('adk',views.adbk),
    # path('dd/<int:id>',views.dbk,name='bid'),
    # path('up/<int:id>',views.ubk,name='uid'),

    # path('vst',views.view_student,name='v_std'),
    # path('ast',views.add_student),
    # path('dlt/<int:id>',views.delt_student,name='sid'),
    # path('updt/<int:id>',views.update_stu,name='uid'),
    # path('dist/<int:id>',views.course_disp,name='cid'),

    path('c',views.view_organizer,name='z'),
    path('d/<int:id>',views.delt_organizer,name='oid'),
    path('a',views.add_organizer),
    path('u/<int:id>',views.update_organizer,name='oidd'),
    path('e',views.view_event,name='x'),
    path('f/<int:id>',views.delt_event,name='eid'),
    path('b',views.add_event),
    path('g/<int:id>',views.uptd_event,name='uid'),





]