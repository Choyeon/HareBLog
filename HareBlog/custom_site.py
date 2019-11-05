from django.contrib.admin import AdminSite


class CustomSite(AdminSite):
    site_header = "HareBlog"
    site_title = 'HareBlog后台管理'
    index_title = '首页'


custom_site = CustomSite(name='cus_admin')
