from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Product, Comment
from .forms import CreateCommentForm


class ProductListView(ListView):
    queryset = Product.objects.filter(active=True)
    template_name = 'products/products.html'
    context_object_name = 'products'


class ProductDetailView(DetailView):
    queryset = Product.objects.prefetch_related('comments').all()
    template_name = 'products/product_detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CreateCommentForm()
        return context


class CommentCreateView(LoginRequiredMixin, CreateView):
    http_method_names = ['post']
    login_url = 'accounts:login'
    model = Comment
    form_class = CreateCommentForm

    def get_success_url(self):
        product_id = int(self.kwargs['product_id'])
        return reverse('products:product_detail', args=[product_id])

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        product_id = int(self.kwargs['product_id'])
        product = get_object_or_404(Product, id=product_id)
        obj.product = product
        return super().form_valid(form)


