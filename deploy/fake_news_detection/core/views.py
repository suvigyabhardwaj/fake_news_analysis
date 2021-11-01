from django.shortcuts import redirect, render
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.model_selection import train_test_split
from fake_news_detection.settings import loaded_model,dataframe
from django.contrib import messages
from .forms import LoginForm
from django.contrib.auth import authenticate,login,logout
from .models import History
from .forms import SignUpForm

# Create your views here.

tfvect = TfidfVectorizer(stop_words='english', max_df=0.7)
loaded_model = loaded_model
dataframe = dataframe
x = dataframe['text']
y = dataframe['label']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

def fake_news_det(news):
    tfid_x_train = tfvect.fit_transform(x_train)
    tfid_x_test = tfvect.transform(x_test)
    input_data = [news]
    vectorized_input_data = tfvect.transform(input_data)
    prediction = loaded_model.predict(vectorized_input_data)
    return prediction

def home(request):
    return render(request,'core/home.html',{'home_active':'active','home_disabled':'disabled'})

def predict(request):
    if request.method == 'POST':
        news = request.POST['news']
        pred = fake_news_det(news)[0]
        if request.user.is_authenticated:
            History.objects.create(user=request.user,news=news,prediction=pred).save()
        return render(request,'core/result.html',{'prediction':pred,'news':news})
    else:
        return redirect('home')

def real(request):
    real_news=dataframe[dataframe['label']=='REAL']['title'][:10]
    return render(request,'core/real.html',{'real_active':'active','real_disabled':'disabled','real_news':real_news})

def fake(request):
    fake_news=dataframe[dataframe['label']=='FAKE']['title'][:10]
    return render(request,'core/fake.html',{'fake_active':'active','fake_disabled':'disabled','fake_news':fake_news})

def code(request):
    return render(request,'core/code.html')

def user_login(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            form=LoginForm(request=request,data=request.POST)
            if form.is_valid():
                uname=form.cleaned_data['username']
                upass=form.cleaned_data['password']
                user=authenticate(username=uname,password=upass)
                if user is not None:
                    login(request,user)
                messages.success(request,'Logged In Successfully !!')
                return redirect('home')
        else:
            form=LoginForm()
        context={
            'form':form,
            'login_active':'active',
            'login_disabled':'disabled'
            }
        return render(request,'core/login.html',context)
    else:
        return redirect('home')

def user_logout(request):
	logout(request)
	messages.success(request,'Logged Out Successfully !!')
	return redirect('home')

def user_signup(request):
    if request.method=='POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            messages.success(request,'Signup Successfully !!')
            user=form.save()
            login(request,user)
            return redirect('home')
    else:
        form=SignUpForm()
    return render(request,'core/signup.html',{'form':form})

def user_history(request):
    if request.user.is_authenticated:
        searhes=History.objects.filter(user=request.user)
        context={
            'searhes':searhes,
            'history_active':'active',
            'history_disabled':'disabled'
            }
        return render(request,'core/history.html',context)
    else:
        return redirect('home')