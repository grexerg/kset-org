from django.conf.urls import url, patterns, include
from django.contrib import admin

from feed import RssProgramFeed, AtomProgramFeed
from filebrowser.sites import site

admin.autodiscover()

urlpatterns = patterns('',

    # feeds
    (r'^feeds/rss/$', RssProgramFeed()),
    (r'^feeds/atom/$', AtomProgramFeed()),

    # news - homepage
    url(r'^$', 'news.views.active', name='root'),
    url(r'^arhiva/vijesti/', 'news.views.archive', name='news-archive'),
    url(r'^vijest/(?P<slug>[-a-zA-Z0-9]+)/$', 'news.views.by_slug', name='news-slug'),

    # events
    url(r'^arhiva/dogadaji/(?P<year>\d{4})/', 'events.views.archive', name='events-archive-year'),
    url(r'^arhiva/dogadaji/', 'events.views.archive', name='events-archive'),
    url(r'^dogadaj/(?P<slug>[-a-zA-Z0-9]+)/$', 'events.views.by_slug', name='event-slug'),
    url(r'^kalendar/$', 'events.views.calendar', name="calendar"),
    url(r'^dogadaji/(?P<date>[-0-9]+)/$', 'events.views.by_date', name='events-date'),


    # newsletter
    url(r'^newsletter/$', 'events.views.newsletter', name='newsletter'),
    url(r'^subscribe/$', 'newsletter.views.subscribe', name='subscribe'),

    # search
    url(r'^trazi/$', 'search.views.search', name='search'),

    url(r'^klub/sekcije/(?P<slug>[-a-zA-Z0-9]+)/$', 'subpages.views.by_slug', name='subpage-slug'),
    url(r'^klub/alumni/$', 'subpages.views.by_slug', {'slug': 'alumni'}, name='alumni'),
    url(r'^klub/$', 'subpages.views.by_slug', name='club'),


    url(r'^multimedia/$', 'subpages.views.multimedia', name='multimedia'),

    url(r'^gallery/$', 'gallery.views.show_gallery'),
    url(r'^gallery/(?P<category>live)/$', 'gallery.views.list_albums'),
    url(r'^gallery/(?P<category>foto)/$', 'gallery.views.list_albums'),
    url(r'^gallery/live/(?P<album_slug>[-_a-zA-Z0-9]+)/$', 'gallery.views.view_album'),
    url(r'^gallery/foto/(?P<album_slug>[-_a-zA-Z0-9]+)/$', 'gallery.views.view_album'),
    url(r'^gallery/(?P<category>live)/albumi/(?P<year>\d{4})/$', 'gallery.views.list_albums'),
    url(r'^gallery/(?P<category>foto)/albumi/(?P<year>\d{4})/$', 'gallery.views.list_albums'),
    url(r'^gallery/live/[-_a-zA-Z0-9]+/(?P<image_slug>[-_a-zA-Z0-9]+)/$', 'gallery.views.view_image'),
    url(r'^gallery/foto/[-_a-zA-Z0-9]+/(?P<image_slug>[-_a-zA-Z0-9]+)/$', 'gallery.views.view_image'),


    url(r'^dezurstva/$', 'savjet.views.list_attendance', name='dezurstva'),

    # ispis crvenih za pozivnice
    url(r'^crveni/$', 'members.views.red', name='crveni'),
    url(r'^crveni-lista/$', 'members.views.red_list', name='crveni-lista'),

    url(r'^clanovi/$', 'members.views.main', name='members'),
    url(r'^clanovi/login/$', 'members.views.login', name='members-login'),
    url(r'^clanovi/logout/$', 'members.views.logout', name='members-logout'),
    url(r'^clanovi/svi/$', 'members.views.listAll', name='members-list-all'),
    url(r'^clanovi/clan/([0-9]+)/$', 'members.views.member', name='members-show-member'),
    url(r'^clanovi/uredi/$', 'members.views.edit', name='members-edit'),


)

## Admin and similar
urlpatterns += patterns('',

    (r'^tinymce/', include('tinymce.urls')),

    url(r'^admin/filebrowser/', include(site.urls)),
    (r'^grappelli/', include('grappelli.urls')),
    (r'^admin/', include(admin.site.urls)),
)
