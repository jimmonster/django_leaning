__author__ = 'jim'
__date__ = '9:19,2018/9/13'

import xadmin
from .models import UserAsk,CourseComments,UserFavorite,UserMessage,UserCourse


class UserAskAdmin(object):
    # 显示列表
    list_display=['name','mobile','course_name','add_time']
    # 搜索
    search_fields=['name','mobile','course_name']
    #筛选
    list_filter=['name','mobile','course_name','add_time']


class CourseCommentsAdmin(object):
    # 显示列表
    list_display=['user','course','comments','add_time']
    # 搜索
    search_fields=['user','course','comments']
    #筛选
    list_filter=['user','course','comments','add_time']


class UserFavoriteAdmin(object):
    # 显示列表
    list_display=['user','course','fav_id','fav_type','add_time']
    # 搜索
    search_fields=['user','course','fav_id','fav_type']
    #筛选
    list_filter=['user','course','fav_id','fav_type','add_time']


class UserMessageAdmin(object):
    # 显示列表
    list_display=['user','message','has_read','add_time']
    # 搜索
    search_fields=['user','message','has_read']
    #筛选
    list_filter=['user','message','has_read','add_time']


class UserCourseAdmin(object):
    # 显示列表
    list_display=['user','course','add_time']
    # 搜索
    search_fields=['user','course']
    #筛选
    list_filter=['user','course','add_time']




xadmin.site.register(UserAsk,UserAskAdmin)
xadmin.site.register(CourseComments,CourseCommentsAdmin)
xadmin.site.register(UserFavorite,UserFavoriteAdmin)
xadmin.site.register(UserMessage,UserMessageAdmin)
xadmin.site.register(UserCourse,UserCourseAdmin)