from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Review, Publication
from .forms import ReviewForm
import datetime



def review_list(request):
    latest_review_list = Review.objects.order_by('-pub_date')[:9]
    context = {'latest_review_list':latest_review_list}
    return render(request, 'reviews/review_list.html', context)


def review_detail(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    return render(request, 'reviews/review_detail.html', {'review': review})


def pubs_list(request):
    pubs_list = Publication.objects.order_by('-publicationName')
    context = {'pubs_list':pubs_list}
    return render(request, 'reviews/pubs_list.html', context)


def pub_detail(request, pub_id):
    pub = get_object_or_404(Publication, pk=pub_id)
    return render(request, 'reviews/pub_detail.html', {'pub': pub})
	
def add_review(request, pub_id):
    pub = get_object_or_404(Publication, pk=pub_id)
    form = ReviewForm(request.POST)
    if form.is_valid():
        rating = form.cleaned_data['rating']
        comment = form.cleaned_data['comment']
        user_name = form.cleaned_data['user_name']
        review = Review()	
        review.pub = pub
        review.user_name = user_name
        review.rating = rating
        review.comment = comment
        review.pub_date = datetime.datetime.now()
        review.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('reviews:pub_detail', args=(pub.id,)))

    return render(request, 'reviews/pub_detail.html', {'pub': pub, 'form': form})


