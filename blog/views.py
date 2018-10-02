from django.shortcuts import render, get_object_or_404
from .models import Post, Comment

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import EmailPostForm, CommentForm

from django.core.mail import send_mail



def post_list(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 2)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
    # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
    # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)
    return render(request, 'blog/post/list.html', {'page': page,'posts': posts})

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk = post_id)
    #Email

    comments = post.comments.filter(active = True)# related_name='comments'
    if request.method == 'POST':
        comment_form = CommentForm(data = request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit = False)
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentForm()
    return render(request, 'blog/post/detail.html', {'post': post, 'comments': comments, 'comment_form': comment_form})
        
        

    #Email
    return render(request, 'blog/post/detail.html', {'post': post})

def post_share(request, post_id):
    # Retrieve post by id
    post = get_object_or_404(Post, id = post_id)
    sent = False
    if request.method == 'POST':    # Form was submitted
        form = EmailPostForm(request.POST)
        if form.is_valid(): # Form fields passed validation(we validate the submitted data using the form's is_valid())
            cd = form.cleaned_data  # ... send email(If the form is valid, we retrieve the validated data accessing form.cleaned_data. This attribute is a dictionary of form fields and their values.)
            subject = '{} {}'.format(cd['name'], post.title)
            message = 'Read {} '.format(post.title)
            send_mail(subject, message, cd['email'], [cd['to']])
            sent = True
    else:
        form = EmailPostForm()  #if we get a GET request, an empty form has to be displayed
    return render(request, 'blog/post/share.html', {'post': post, 'form': form, 'sent': sent})

    #   you need to learn how to send e-mails with Django to put everything together.