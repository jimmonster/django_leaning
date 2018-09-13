__author__ = 'jim'
__date__ = '9:19,2018/9/13'

import xadmin
from .models import Course,Lesson,Video,CourseResource


class CourseAdmin(object):
    # 显示列表
    list_display=['name','desc','detail','degree','lean_times','students','fav_num','image','click_num','add_time']
    # 搜索
    search_fields=['name','desc','detail','degree','lean_times','students','fav_num','image','click_num']
    #筛选
    list_filter=['name','desc','detail','degree','lean_times','students','fav_num','image','click_num','add_time']


class LessonAdmin(object):
    # 显示列表
    list_display=['course','name','add_time']
    # 搜索
    search_fields=['course','name']
    #筛选
    list_filter=['course','name','add_time']


class VideoAdmin(object):
    # 显示列表
    list_display=['lesson','name','add_time']
    # 搜索
    search_fields=['lesson','name']
    #筛选
    list_filter=['lesson','name','add_time']


class CourseResourceAdmin(object):
    # 显示列表
    list_display=['course','name','download','add_time']
    # 搜索
    search_fields=['course','name','download']
    #筛选
    list_filter=['course','name','download','add_time']







xadmin.site.register(Course,CourseAdmin)
xadmin.site.register(Lesson,LessonAdmin)
xadmin.site.register(Video,VideoAdmin)
xadmin.site.register(CourseResource,CourseResourceAdmin)
