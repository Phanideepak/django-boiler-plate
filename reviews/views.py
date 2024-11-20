from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpResponse
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, CreateView
from .forms import ReviewForm
from .models import Review

# Create your views here.


'''
# ClassBasedView
class ReviewView(View):
    def get(self, request):
        form = ReviewForm()

        return render(request, 'reviews/review.html', {'form' : form})

    def post(self, request):
        if request.method == 'POST':
            # ModelForm
            form = ReviewForm(request.POST)

        if form.is_valid():
            # review = Review(user_name = form.cleaned_data['user_name'], 
            #                 review_text = form.cleaned_data['review_text'],
            #                 rating = form.cleaned_data['rating']
            #                 )
            form.save()
            return HttpResponseRedirect(reverse('thank_you'))
        
        return render(request, 'reviews/review.html', {'form' : form})
'''

# FormView
class ReviewView(FormView):
    form_class = ReviewForm
    template_name = 'reviews/review.html'
    success_url = '/thank-you'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
class ReviewView1(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'reviews/review.html'
    success_url = '/thank-you' 

#TemplateView
class ThankYouView(TemplateView):
    template_name = 'reviews/thank_you.html'

    # Overriding context data. 
    # Context data can be used in template
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'This Works!'
        return context

# TemplateView
'''
class ReviewListView(TemplateView):
    template_name = 'reviews/review_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        reviews = Review.objects.all()
        context['reviews'] = reviews
        return context
'''    

'''
# TemplateView
class SingleReviewView(TemplateView):
    template_name = 'reviews/single_review.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # id is path parameter
        review_id = kwargs['id']
        review = Review.objects.filter(id = review_id)
        context['review'] = review
        return context
'''
        
# DetailView
class SingleReviewView(DetailView):
    template_name = 'reviews/single_review.html'
    model = Review


# ListView
class ReviewListView(ListView):
    template_name = 'reviews/review_list.html'
    model = Review
    # List of Reviews will be stored in object_list (default)
    # object_list will be passed to template.
    
    # We can change object_list value to custom variable
    context_object_name = 'reviews'

    def get_queryset(self):
        base_query = super().get_queryset()
        data = base_query.filter(rating__gt = 0)
        return data





# Below methods are not linked to url routing.
def review(request):
    if request.method == 'POST':
        # ModelForm
        form = ReviewForm(request.POST)

        if form.is_valid():
            # review = Review(user_name = form.cleaned_data['user_name'], 
            #                 review_text = form.cleaned_data['review_text'],
            #                 rating = form.cleaned_data['rating']
            #                 )
            form.save()
            return HttpResponseRedirect(reverse('thank_you'))
    else:
        form = ReviewForm()

    return render(request, 'reviews/review.html', { 'form' : form})

def thank_you(request):
    return render(request, 'reviews/thank_you.html')