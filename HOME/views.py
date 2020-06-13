from django.http import HttpResponse, HttpResponseRedirect,JsonResponse
from django.shortcuts import render
from django.views import View
from django.urls import reverse
from django.utils import timezone;

from django.shortcuts import render
from .models import User,Score

def Index(request): 			## function for index page
	user = get_user(request);

	if user == False:		## IF NO USER LOGED IN
		context = {
		'user':user
		}
		return render(request,'HOME/index.html',context)

	else:					## IF A USER LOGED IN
		context = {
		'user':user
		}
		return render(request,'HOME/index.html',context)


def Register(request):				## function to register a new user in database
	if request.method == "POST":
		u = User();
		u.user_name = request.POST['user_name'];
		u.user_mail = request.POST['user_mail'];
		u.user_pass = request.POST['user_pass'];
		if is_mail_exist(u.user_mail):
			return HttpResponseRedirect(reverse('home'))
		else:
			u.save();
			return LogIn(request);
	else:
		return HttpResponseRedirect(reverse('home'));

def LogIn(request):					## function to login a user and allocating a session
	mail = request.POST['user_mail'];
	password = request.POST['user_pass']
	if is_mail_exist(mail):
		user = User.objects.get(user_mail = mail);
		if(password == user.user_pass):
			LogOut(request);
			request.session['session_id'] = user.id
			return HttpResponseRedirect(reverse('home'))
	return HttpResponse('Wrong password or mail :/');

def LogOut(request):				## function to logout a user and flush session
    try:
        request.session.flush();
    except KeyError:
        return HttpResponse('Error Occur While Logging You Out, Please Try Again')
    return HttpResponseRedirect(reverse('home'))

def SaveScore(request):				## function to save scores of the user
	user = get_user(request)

	if user and request.is_ajax():

		sc = Score();
		sc.time = request.POST['time'];
		sc.score = request.POST['score'];
		sc.user = user; 
		sc.date = timezone.now();
		sc.save()
		if( int(user.user_best_score) < int(sc.score) ):#Is the Score is Best?(True)
			user.user_best_score = sc.score;
			user.user_best_time = sc.time;
			user.save();
	return JsonResponse('Success');

def UpdatePhoto(request):
	user = get_user(request);
	if user and request.method == 'POST' and request.is_ajax():
		photo = request.FILES['img']
		user.user_img = photo;
		user.save()
		return JsonResponse({'success':'Image is Successfully save.'});

def Rank(request):
	user = get_user(request)
	rank = User.objects.order_by('user_best_score')
	rank = rank.reverse();
	context = {'rank':rank, 'user':user};
	return render(request,'HOME/rank.html',context);

def Progress(request):
	user = get_user(request);
	if user:
		scores = Score.objects.filter(user=user).order_by('-date');
		try:
			scores = scores[0:10]
		except:
			pass;
		s = [i.score for i in scores]
		s.reverse();
		context = {'scores':s,'user':user};
		return render(request,'HOME/progress.html',context);
	return HttpResponseRedirect(reverse('home'))


################################################## Extra Function  ###################################################

def is_mail_exist(mail):			## A function which check that a mail is already saved in the database or not
	mail_list = User.objects.values('user_mail')
	for item in mail_list:
		if item['user_mail'] == mail:
			return True;
	return False;

def get_user(request):				## A function which get user_id from the session key (if not present it return false)
	if 'session_id' in request.session:
		return User.objects.get(id = request.session['session_id']);
	return False;