from django import forms
from blog.models import Post, Comment

#create forms classes

class PostForm(forms.ModelForm):

	#create the Meta class
	#This meta class helps us link the form to the model and also to css classes
	class Meta():
		# link this form to the Post model
		model = Post
		# select the fields to be edited
		fields = ('author', 'title', 'text')

		# To use CSS stylings, we define a widgets dictionary here 
		# which takes field name as the key and the type of field and the css classess 
		# to be used on that field
		widgets = {
			'title' : forms.TextInput(attrs = {'class': 'textinputclass'}),
			'text'  : forms.Textarea(attrs = {'class': 'editable medium-editor-textarea postcontent'})
		}


class CommentForm(forms.ModelForm):
	class Meta():
		model = Comment
		fields = ('author', 'text')

		widgets = {
			'author' : forms.TextInput(attrs = {'class': 'textinputclass'}),
			'text' : forms.Textarea(attrs = {'class': 'editable medium-editor-textarea'})
		}