from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import ContactUs  # Import your ContactUs model
from .models import Question, Choice, Votes
# from django.utils import timezone

# Create your views here.
def home(request):
    # return HttpResponse("i m website")
    return render(request, 'index.html')

def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            print("succesfully logged in")
            return redirect('home')
    return render(request, 'loginPage.html')


def logout_view(request):
    logout(request)
    return redirect('home')

def signup(request):
    if request.method =='POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2') 
    
        if (password1 == password2) and (password1!= ''):
            user = User.objects.create_user(username, email,password1)
            user.save()
            return redirect('login')
    return render(request, 'signupPage.html')


def createPoll(request):
    if request.method == 'POST':
        question_text = request.POST.get('question_text')
        choice_text1 = request.POST.get('option1')
        choice_text2 = request.POST.get('option2')
        choice_text3 = request.POST.get('option3')
        choice_text4 = request.POST.get('option4')

        # Create Question object
        # question = Question.objects.create(question_text=question_text)
        question = Question()
        question.question_text= question_text
        question.choice_text1 = choice_text1
        question.choice_text2 = choice_text2
        question.choice_text3 = choice_text3
        question.choice_text4 = choice_text4
        question.save()


        # # Create Choice objects
        # choice1 = Choice.objects.create(question=question, choice_text=choice_text1)
        # choice2 = Choice.objects.create(question=question, choice_text=choice_text2)
        # choice3 = Choice.objects.create(question=question, choice_text=choice_text3)
        # choice4 = Choice.objects.create(question=question, choice_text=choice_text4)

        return redirect('polls')  # Redirect to a success page after creating the poll
    else:
        return render(request, 'createPollPage.html')
  

def contact(request):
    if request.method == 'POST':
        # Assuming you have a ContactUs model with fields name, email, and message
        name = request.POST.get('fullName')
        email = request.POST.get('email')
        message = request.POST.get('textContent')
        
        # Create a new instance of ContactUs model and save it
        contact = ContactUs(name=name, email=email, message=message)
        contact.save()
        
        # Redirect to a thank you page or any other page after successful form submission
        return HttpResponse('/thank-you/')
    else:
        # If it's a GET request, just render the empty form
        return render(request, 'contact.html')
    

def viewpoll(request):
    active_questions = Question.objects.filter(is_over=False)
    choices_lists = []
    for question in active_questions:
        choices = Choice.objects.filter(question=question)
        choices_lists.append({'question': question, 'choices': choices})
    return render(request, 'polls.html', {'choices_lists': choices_lists})


def send_vote(request, choiceoption):
    username = request.user.username
    if Votes.objects.filter(user = username).exists():
        return redirect('result.html')
    else:
        choice = Choice.objects.get(option = choiceoption)
        choice.votes +=1
        choice.save()

        # new_vote = Votes()
        # new_vote.user = username
        # new_vote.vote = True
        # new_vote.save()
        new_vote = Votes(user=request.user.username, vote=True)
        new_vote.save()
        return redirect('result.html')
    

def result(request):
    result = Choice.objects.filter(question__is_over=False)
    return render(request, 'results.html',{'results':result})