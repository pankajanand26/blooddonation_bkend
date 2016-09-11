from django.db import models

# Create your models here.
# class Donor(models.Model):
#      id_donor = models.IntegerField(default=0)
#      first_name = models.CharField(max_length=200)
#      last_name = models.CharField(max_length=200)
#      location = models.CharField(max_length=200)
#      city = models.CharField(max_length=200)
#      about_yourself = models.CharField(max_length=200)
#      gender = models.CharField(max_length=200)
#      available = models.CharField(max_length=200)
#      phone_number = models.IntegerField(default=0)
#      blood_group = models.CharField(max_length=200)
#      last_donated = models.DateTimeField('last donated')
#      trans_date = models.DateTimeField('transaction date')
#
# class Requester(models.Model):
#      id_requester = models.IntegerField(default=0)
#      first_name = models.CharField(max_length=200)
#      last_name = models.CharField(max_length=200)
#      location = models.CharField(max_length=200)
#      city = models.CharField(max_length=200)
#      phone_number = models.IntegerField(default=0)
#      blood_group = models.CharField(max_length=200)
#      units = models.IntegerField(default=0)
#      pub_date = models.DateTimeField('date published')
#      trans_date = models.DateTimeField('transaction date')

#class Donations(models.Model):
  #   id_donaton = models.IntegerField(default=0)
    # don_date = models.DateTimeField('donation date')
 #    donor = models.ForeignKey(Donor)
  #   requester = models.ForeignKey(Requester)
   #  trans_date = models.DateTimeField('transaction date')

class UserDetails(models.Model):
     id_userid = models.IntegerField(default=0)
     full_name = models.CharField(max_length=200)
     contact_number = models.IntegerField(default=0)
     entity = models.CharField(max_length=200)
     userType = models.CharField(max_length=200)
     blood_group = models.CharField(max_length=200)
     gender = models.CharField(max_length=200)
     user_available = models.CharField(max_length=200)
     blood_group = models.CharField(max_length=200)
     userPreference = models.CharField(max_length=200)
     trans_date = models.DateTimeField('transaction date')

class RequestTable(models.Model):
    id_requestid = models.IntegerField(default=0)
    userid = models.ForeignKey(UserDetails)
    requestFor = models.CharField(max_length=200)
    requestDate = models.DateTimeField('request date')
    requestContactName = models.CharField(max_length=200)
    requestContactNumber = models.IntegerField(default=0)
    requestNoOfUnits = models.IntegerField(default=0)
    requestLocation = models.CharField(max_length=200)
    requestGender = models.CharField(max_length=200)
    requestStatus = models.CharField(max_length=200)
    trans_date = models.DateTimeField('transaction date')

class Donations(models.Model):
     id_donationid = models.IntegerField(default=0)
     requestid = models.ForeignKey(RequestTable)
     donationLocation = models.CharField(max_length=200)
     donationDate = models.DateTimeField('donation date')
     requestLocation = models.CharField(max_length=200)
     requestGender = models.CharField(max_length=200)
     userid = models.ForeignKey(UserDetails)
     requstStatus = models.CharField(max_length=200)
     trans_date = models.DateTimeField('transaction date')

class DonorsList(models.Model):
     requestid = models.ForeignKey(RequestTable)
     userid = models.ForeignKey(UserDetails)


