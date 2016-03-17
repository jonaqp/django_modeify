from django.conf.urls import url, include

from  .views import TaskList

urlpatterns = [
    url(r'^tasks/$', TaskList.as_view(), name='task_list'),

]
