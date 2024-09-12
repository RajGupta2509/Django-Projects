from django.shortcuts import render
from .models import Tweet
from .forms import TweetForm, UserRegistrationForm
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

# Create your views here.

def index(request):
    return render(request, 'tweetIndex.html')


# to show all the tweets on a web page
def displayTweet(request):
    tweets = Tweet.objects.all().order_by("-created_at")
    # Tweet.objects.all().order_by('-created_at')
    return render(request, 'allTweets.html', {'tweets':tweets})


@login_required
# Create a New Tweet
def createTweet(request):
    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES)
        if form.is_valid():
            tweet =form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('displayTweet')
    else:
        form = TweetForm()
    return render(request, 'tweetForm.html', {'form':form})


@login_required
# Edit an Existing Tweet
def editTweet(request, tweetId):
    tweet=get_object_or_404(Tweet, pk=tweetId, user=request.user)
    if request.method=='POST':
        form = TweetForm(request.POST, request.FILES, instance=tweet)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('displayTweet')      
    else:
        form = TweetForm(instance=tweet)
    return render(request, 'tweetForm.html', {'form':form})

@login_required
# deleting an existing Tweet
def deleteTweet(request,tweetId):
    tweet=get_object_or_404(Tweet, pk=tweetId, user=request.user)
    if request.method=='POST':
        tweet.delete()
        return redirect('displayTweet')      
    else:
        form = TweetForm(instance=tweet)
    return render(request, 'tweetDelete.html', {'tweet':tweet})


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request,user)
            return redirect('displayTweet')
    else:
        form=UserRegistrationForm()
        
    return render(request, 'registration/register.html', {'form':form})