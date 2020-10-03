from django.conf.urls import url
from blog import views

urlpatterns = [
	url(r'^$', views.PostListView.as_view(), name = 'post_list'),
	url(r'^post/(?P<pk>\d+)/$', views.PostDetailView.as_view(), name = 'post_detail'),
	url(r'^about/$', views.AboutView.as_view(), name = 'about'),
	url(r'^post/new/', views.CreatePostView.as_view(), name = 'post_new'),
	url(r'^post/(?P<pk>\d+)/edit/$', views.UpdatePostView.as_view(), name = 'post_edit'),
	url(r'^post/(?P<pk>\d+)/delete/$', views.DeletePostView.as_view(), name = 'post_delete'),
	url(r'^drafts/$', views.DraftPostView.as_view(), name = 'post_draft_list'),
	url(r'^post/(?P<pk>\d+)/comment/$', views.add_comment, name = 'comment'),
	url(r'^comment/(?P<pk>\d+)/approve/$', views.comment_approval, name = 'approve_comment'),
	url(r'^comment/(?P<pk>\d+)/delete/$', views.delete_comment, name = 'delete_comment'),
	url(r'^post/(?P<pk>\d+)/publish', views.publish_post, name= 'publish_post')
]