from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, CommentForm
from .models import Post, Comment
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy, reverse



# Let handle user registration
def home(request):
    posts = Post.objects.all().order_by('-published_date')
    return render(request, "blog/home.html", {'posts':posts})

# Let accept registration data from user
def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = CustomUserCreationForm()
        return render(request, "blog/register.html", {"form": form})

# Here let login the user
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        # Here we check the user login details if its correct to what used when register.
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)

            # And if the detail is correct, Login the user
            if user is not None:
                login(request, user)
                return redirect("profile")
    else:
        form = AuthenticationForm()

        return render(request, "blog/login.html", {"form":form})

# Let logout the user.
def logout_view(request):
    logout(request)
    return redirect("login")

# To allow only authenticated user to view the profile.
@login_required
def profile(request):
    return render(request, "blog/profile.html")

# This allow everyone to view the post
class PostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"
    context_object_name = "posts"
    ordering = ["-published_date"]

class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"

# Let allow authenticated users to be able to create post.
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ["title", "content"]
    template_name = "blog/post_form.html"
    success_url = reverse_lazy('post-list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
# Let handle update of the post for only authenticated users.
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ["title", "content"]
    template_name = "blog/post_form.html"
    success_url = reverse_lazy('posts')

    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user
    
# Let handle delete of the post for only authenticated users.
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = "blog/post_delete.html"
    success_url = reverse_lazy("posts")

    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user



# Now, let allow authenticated user only to comment on a post
class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = "blog/comment_form.html"

    def form_valid(self, form):
        post = get_object_or_404(Post, pk=self.kwargs["post_id"])
        form.instance.post = post
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse("post-detail", kwargs={"pk": self.kwargs["post_id"]})
    

class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    form_class = CommentForm

    def test_func(self):
        comment = self.get_object()
        return comment.author == self.request.user

    def get_success_url(self):
    
        return reverse("post-detail", kwargs={"pk": self.object.post.pk})

class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    comment = Comment

    def test_func(self):
        comment = self.get_object()
        return comment.author == self.request.user
    
    def get_success_url(self):
        return reverse("post-detail", kwargs={"pk": self.object.post.id})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form =  CommentForm
    return render(request, 'post_detail.html', {'post': post, 'form': form})