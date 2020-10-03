from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.

# Post class
class Post(models.Model):
	author = models.ForeignKey('auth.user', on_delete = models.CASCADE)
	title = models.CharField(max_length = 200)
	text = models.TextField()
	create_date = models.DateTimeField(default = timezone.now())
	published_date = models.DateTimeField(blank=True, null=True)


	### publish method to capture the timestamp of the publish time ###
	def publish(self):
		self.published_date = timezone.now()
		self.save()

	### this method will filter out all the approved comments for the post###
	def approve_comment(self):
		return self.comments.filter(approved_comment = True)

	# this is a built-in function that django searches for so that once a post
	# is created, django can redirect to that page(here - detail page for the 
	# newly created post)
	def get_absolute_url(self):
		return reverse('post_detail', kwargs={'pk':pk})

	### string representation of the class ###
	def __str__(self):
		return self.title


# comment class
class Comment(models.Model):
	post = models.ForeignKey('blog.Post', related_name = 'comment', on_delete = models.CASCADE)
	author = models.CharField(max_length=200)
	text = models.TextField()
	create_date = models.DateTimeField(default=timezone.now())
	approved_comment = models.BooleanField(default=False)

	def approve_comment(self):
		self.approved_comment = True
		self.save()

	# once a user comments on a post, the user will be redirected
	# to the post list page
	def get_absolute_url(self):
		return reverse('post_list')

	def __str__(self):
		return self.text
