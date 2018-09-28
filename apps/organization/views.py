from django.shortcuts import render
from django.views.generic import View
# Create your views here.
from .models import CourseOrg,CityDict,Teacher

class OrgView(View):
    """
    课程机构列表功能
    """
    def get(self,request):
        # 课程机构
        all_orgs=CourseOrg.objects.all()
        # 城市
        all_citys=CityDict.objects.all()
        org_nums=all_orgs.count()


        return render(request,'org-list.html',{
            'all_orgs':all_orgs,
            'all_citys':all_citys,
            'org_nums':org_nums

        })


