from django.contrib import admin
# from django.conf.urls import url
# from django.template.response import TemplateResponse
# from asanpay.models import Security

# @admin.register(Security)
# class SecurityAdmin(admin.ModelAdmin):

#     def get_urls(self):

#         # get the default urls
#         urls = super(SecurityAdmin, self).get_urls()

#         # define security urls
#         security_urls = [
#             url(r'^configuration/$', self.admin_site.admin_view(self.security_configuration))
#         ]

#         return security_urls + urls

#     def security_configuration(self, request):
#         context = dict(
#             self.admin_site.each_context(request), # Include common variables for rendering the admin template.
#             something="test",
#         )
#         return TemplateResponse(request, "admin/configuration.html", context)