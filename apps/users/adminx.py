import xadmin
from .models import EmailVerifyRecord,Banner
from xadmin import views


class BaseSetting(object):
    # 是否支持主题
    enable_themes=True
    # 对应主题
    use_bootswatch=True


class GlobalSettings(object):
    site_title='后台管理系统'
    site_footer='create by jim monster'
    # 将列表变成可收缩类型
    menu_style='accordion'




class EmailVerifyRecordAdmin(object):
    # 显示列表
    list_display=['code','email','send_type','send_time']
    # 搜索
    search_fields=['code','email','send_type']
    #筛选
    list_filter=['code','email','send_type','send_time']

class BannerAdmin(object):
    # 显示列表
    list_display=['title','image','url','index','add_time']
    # 搜索
    search_fields=['title','image','url','index']
    #筛选
    list_filter=['title','image','url','index','add_time']




xadmin.site.register(EmailVerifyRecord,EmailVerifyRecordAdmin)
xadmin.site.register(Banner,BannerAdmin)
xadmin.site.register(views.BaseAdminView,BaseSetting)
xadmin.site.register(views.CommAdminView,GlobalSettings)
