__author__ = 'jim'
__date__ = '9:19,2018/9/13'

import xadmin
from .models import CityDict,CourseOrg,Teacher


class CityDictAdmin(object):
    # 显示列表
    list_display=['name','desc','add_time']
    # 搜索
    search_fields=['name','desc']
    #筛选
    list_filter=['name','desc','add_time']


class CourseOrgAdmin(object):
    # 显示列表
    list_display=['name','desc','click_nums','fav_nums','image','address','city','add_time']
    # 搜索
    search_fields=['name','desc','click_nums','fav_nums','image','address','city']
    #筛选
    list_filter=['name','desc','click_nums','fav_nums','image','address','city','add_time']

class TeacherAdmin(object):
    # 显示列表
    list_display=['org','name','work_years','work_company','worl_posithon','points','click_nums','fav_nums','add_time']
    # 搜索
    search_fields=['org','name','work_years','work_company','worl_posithon','points','click_nums','fav_nums']
    #筛选
    list_filter=['org','name','work_years','work_company','worl_posithon','points','click_nums','fav_nums','add_time']



xadmin.site.register(CityDict,CityDictAdmin)
xadmin.site.register(CourseOrg,CourseOrgAdmin)
xadmin.site.register(Teacher,TeacherAdmin)