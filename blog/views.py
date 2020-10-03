from blog.models import Post, Comment
from django.utils import timezone
from django.urls import reverse_lazy
from blog.forms import PostForm, CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import (TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView)


# Create your views here.
class AboutView(TemplateView):
	template_name = 'about.html'

class PostListView(ListView):
	model = Post

	def get_queryset(self):
		return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

class PostDetailView(DetailView):
	model = Post

# LoginRequiredMixin is an advanced built in class that restricts the user to perform any action 
# without Login
class CreatePostView(CreateView, LoginRequiredMixin):
	# below all fields are all predefined and should be used as they are named according to Django Documentation
	login_url = '/login/'
	redirect_field_name = 'blog/details.html'
	form_class = PostForm
	model = Post

class UpdatePostView(UpdateView, LoginRequiredMixin):
	login_url = '/login/'
	redirect_field_name = 'blog/details.html'
	form_class = PostForm
	model = Post

class DeletePostView(DeleteView, LoginRequiredMixin):
	model = Post

	# Now we use the reverse_lazy method here to redirect to another page only after successful deletion.
	# The reverse_lazy method will wait for the deletion process to end and then go to the success url specified below.
	success_url = reverse_lazy('home')


class DraftPostView(LoginRequiredMixin, ListView):
	login_url = '/login/'
	redirect_field_name = 'blog/post_list.html'
	model = Post

	def get_queryset(self):
		return Post.objects.filter(published_date__isnull=True).order_by('created_date')


@login_required
def publish_post(req, pk):
	#post = Post.objects.filter(published_date__isnull=True)
	post_tobe_published = post.objects.get(pk = pk)
	post_tobe_published.publish()
	return redirect('post_detail', pk = pk)


# Restricts any unauthenticated user to add comment to a post
@login_required
def add_comment(req, pk):
	# Get the post with primary key = pks
	post = get_object_or_404(Post, pk = pk)

	#########################################################################################
	# TODO: handle if the post is null(got 404 for the post with primary key as pk from DB)##
	#########################################################################################

	if req.method == 'POST':
		# Get the form filled data in a new CommentForm instance
		# if the data is valid, save it to comment as well as the post model
		form = CommentForm(req.POST)
		if form.is_valid():
			comment = form.save(commit = False)
			comment.post = post
			comment.save()
			return redirect('post_detail', pk = pk)

	else:
		form = CommentForm()

	return render(req, 'blog/comment_form.html', {'form':form})


@login_required
def comment_approval(req, pk):
	post = get_object_or_404(Comment, pk = pk)
	Comment.approve_comment()

	# Once the comment is approved, go to the post detail page
	return redirect('post_detail', pk = comment.post.pk)

@login_required
def delete_comment(req, pk):
	comment = get_object_or_404(Comment, pk = pk)
	post_pk = comment.post.pk
	comment.delete()
	return redirect('post_detail', pk = post_pk)

































