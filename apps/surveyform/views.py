from django.shortcuts import render, redirect

def index(request):
	return render(request, "surveyform/index.html")

def submit(request):
	request.session['name'] = request.POST['name']
	request.session['dojo_location']= request.POST['dojo_location']
	request.session['favlanguage']= request.POST['favlanguage']
	request.session['comment']= request.POST['comment']
	return redirect('/result')

def result(request):
	return render(request, "surveyform/result.html")