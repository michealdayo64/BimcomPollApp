from django.db import models

# Create your models here.


class State(models.Model):
    state_name = models.CharField(max_length=50, default="", null=True, blank=True) 

class Lga(models.Model):
    lga_id = models.IntegerField(null=True, blank=True)
    lga_name = models.CharField(max_length = 50, blank=True, null=True)
    state_id = models.IntegerField(null=True, blank=True)
    lga_description = models.TextField(null=True, blank=True)
    entered_by_user = models.CharField(max_length = 50, blank=True, null=True)
    date_entered = models.DateTimeField(null=True, blank=True)
    user_ip_address = models.CharField(max_length = 100, null=True, blank=True)


class Ward(models.Model):
    ward_id = models.IntegerField(null=True, blank=True)
    ward_name = models.CharField(max_length = 50, blank=True, null=True)
    lga_id = models.IntegerField(null=True, blank=True)
    ward_description = models.TextField(null=True, blank=True)
    entered_by_user = models.CharField(max_length = 50, blank=True, null=True)
    date_entered = models.DateTimeField(null=True, blank=True)
    user_ip_address = models.CharField(max_length = 100, null=True, blank=True)


class PollingUnit(models.Model):
    polling_unit_id = models.IntegerField(null=True, blank=True)
    ward_id = models.IntegerField(null=True, blank=True)
    lga_id = models.IntegerField(null=True, blank=True)
    uniquewardid = models.IntegerField(null=True, blank=True)
    polling_unit_number = models.CharField(max_length = 100, null=True, blank=True)
    polling_unit_name = models.CharField(max_length = 100, null=True, blank=True)
    polling_unit_description = models.TextField(null=True, blank=True)
    lat = models.CharField(max_length = 100, null=True, blank=True)
    longi = models.CharField(max_length = 100, null=True, blank=True)
    entered_by_user = models.CharField(max_length = 50, blank=True, null=True)
    date_entered = models.DateTimeField(null=True, blank=True)
    user_ip_address = models.CharField(max_length = 100, null=True, blank=True)

    def __str__(self):
        return self.polling_unit_name


class Party(models.Model):
    partyid = models.CharField(max_length = 100, null=True, blank=True)
    partyname = models.CharField(max_length = 100, null=True, blank=True)


class AnnouncedPuResults(models.Model):
    polling_unit_uniqueid = models.CharField(max_length = 100, null=True, blank=True)
    party_abbreviation = models.CharField(max_length = 100, null=True, blank=True)
    party_score = models.IntegerField(null=True, blank=True)
    entered_by_user = models.CharField(max_length = 50, blank=True, null=True)
    date_entered = models.DateTimeField(null=True, blank=True)
    user_ip_address = models.CharField(max_length = 100, null=True, blank=True)


class AnnouncedLgaResults(models.Model):
    lga_name = models.CharField(max_length = 100, null=True, blank=True)
    party_abbreviation = models.CharField(max_length = 100, null=True, blank=True)
    party_score = models.IntegerField(null=True, blank=True)
    entered_by_user = models.CharField(max_length = 50, blank=True, null=True)
    date_entered = models.DateTimeField(null=True, blank=True)
    user_ip_address = models.CharField(max_length = 100, null=True, blank=True)