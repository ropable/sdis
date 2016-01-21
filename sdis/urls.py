from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView

from pythia.sites import site
from pythia.views import TermsAndConditions, spell_check

js_info_dict = {'packages': ('django.conf',), }

urlpatterns = patterns(
    '',
    url(r'^browserid/', include('django_browserid.urls')),
    url(r'^jsi18n$', 'django.views.i18n.javascript_catalog', js_info_dict),
    url(r'^browserid/', include('django_browserid.urls')),
    url(r'^spillchuck/$', spell_check),
    url(r'^terms-and-conditions/$',
        TermsAndConditions.as_view(), name='terms-and-conditions'),
    url(r'^terms-and-conditions-agreed/$',
        TemplateView.as_view(template_name="admin/terms-and-conditions-agreed.html"),
        name='terms-and-conditions-agreed'),
    url(r'^docs/dev/$',
        TemplateView.as_view(
            template_name="../../staticfiles/docs/dev/html/index.html"),
        name='dev-docs'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'', include(site.urls)),
)

#urlpatterns += patterns('django.contrib.staticfiles.views', url(r'^static/(?P<path>.*)$', 'serve'), )
urlpatterns += staticfiles_urlpatterns()
