#from django.shortcuts import render
from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.shortcuts import render
#from polls.models import Question
from donation_add.models import UserDetails, RequestTable, DonorsList, Donations
# from django.template import RequestContext, loader
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django import forms
from django.core import serializers
from django.db.models import Max
#from forms import UserRegForm, LoginForm


def get_user(request,user_id):
    try:
        user_detail = UserDetails.objects.filter(pk=user_id)
    except UserDetails.DoesNotExist:
       # raise Http404("User "+ user_id + " Doesnot Exist")
        return HttpResponse("User "+ user_id + " Doesnot Exist")
    return HttpResponse(serializers.serialize("json",user_detail))

def get_donor(request,user_id):
    try:
        donations = Donations.objects.filter(userid=user_id)
    except UserDetails.DoesNotExist:
        return HttpResponse("User "+ user_id + " Doesnot Exist")
    return HttpResponse(serializers.serialize("json",donations))

def get_donations(request,user_id):
    try:
        donations = Donations.objects.filter(userid=user_id).order_by('-donationDate')
        # donations = Donations.objects.a
    except Donations.DoesNotExist:
        return HttpResponse("User "+ user_id + " has not made any donations.")
    return HttpResponse(serializers.serialize("json",donations))

def get_requests(request,user_id):
    try:
        requests = RequestTable.objects.filter(userid=user_id).order_by('-requestDate')
        # donations = Donations.objects.a
    except Donations.DoesNotExist:
        return HttpResponse("User "+ user_id + " has not made any requests.")
    return HttpResponse(serializers.serialize("json", requests))

def get_request(request,request_id):
    try:
        request_details = RequestTable.objects.filter(id_requestid=request_id)
        # donations = Donations.objects.a
    except RequestTable.DoesNotExist:
        return HttpResponse("Request "+ request_id + " does not exist.")
    return HttpResponse(serializers.serialize("json", request_details))

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
#    output = ', '.join([p.question_text for p in latest_question_list])
#    return HttpResponse(output)
    template = loader.get_template('polls/index.html')
    context = RequestContext(request, {
        'latest_question_list': latest_question_list,
        'error': str(request.user),
    })
    return HttpResponse(template.render(context))
