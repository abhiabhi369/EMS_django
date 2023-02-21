# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,UserManager


class Caste(models.Model):
    caste_id = models.IntegerField(primary_key=True)
    caste_name = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.caste_name

    class Meta:
        managed = False
        db_table = 'caste'


class Constituency(models.Model):
    district = models.ForeignKey('District', models.DO_NOTHING, blank=True, null=True)
    const_id = models.IntegerField(primary_key=True)
    const_name = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.const_name

    class Meta:
        managed = False
        db_table = 'constituency'


class Country(models.Model):
    country_id = models.IntegerField(primary_key=True)
    county = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.county

    class Meta:
        managed = False
        db_table = 'country'


class District(models.Model):
    state = models.ForeignKey('State', models.DO_NOTHING, blank=True, null=True)
    district_id = models.IntegerField(primary_key=True)
    district_name = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.district_name

    class Meta:
        managed = False
        db_table = 'district'


class FavourTo(models.Model):
    favour_to_id = models.IntegerField(primary_key=True)
    favour_to_name = models.CharField(max_length=30, blank=True, null=True)
    state = models.ForeignKey('State', models.DO_NOTHING, db_column='state', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'favour_to'


class Gender(models.Model):
    gender_id = models.IntegerField(primary_key=True)
    gender_name = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return self.gender_name

    class Meta:
        managed = False
        db_table = 'gender'


class ImportanatPeople(models.Model):
    imp_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=32, blank=True, null=True)
    designation = models.CharField(max_length=32, blank=True, null=True)
    mobile_no = models.CharField(max_length=10, blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'importanat_people'

class State(models.Model):
    country = models.ForeignKey(Country, models.DO_NOTHING, blank=True, null=True)
    state_id = models.IntegerField(primary_key=True)
    state_name = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.state_name

    class Meta:
        managed = False
        db_table = 'state'


class SubCaste(models.Model):
    caste = models.ForeignKey(Caste, models.DO_NOTHING, blank=True, null=True)
    sub_caste_id = models.IntegerField(primary_key=True)
    sub_caste_name = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.sub_caste_name

    class Meta:
        managed = False
        db_table = 'sub_caste'


class Token(models.Model):
    token = models.CharField(primary_key=True, max_length=100)
    user = models.ForeignKey('Users', models.DO_NOTHING, db_column='user', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'token'


class Users(AbstractBaseUser):
    email = models.CharField(primary_key=True, max_length=100)
    password = models.CharField(max_length=100, blank=True, null=True)
    first = models.CharField(max_length=30, blank=True, null=True)
    last = models.CharField(max_length=30, blank=True, null=True)
    phone = models.CharField(max_length=10, blank=True, null=True)
    country = models.ForeignKey(Country, models.DO_NOTHING, db_column='country', blank=True, null=True)
    state = models.ForeignKey(State, models.DO_NOTHING, db_column='state', blank=True, null=True)
    district = models.ForeignKey(District, models.DO_NOTHING, db_column='district', blank=True, null=True)
    constituency = models.ForeignKey(Constituency, models.DO_NOTHING, db_column='constituency', blank=True, null=True)

    last_login = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()

    class Meta:
        managed = False
        db_table = 'users'

class Mandal(models.Model):
    dist = models.ForeignKey(District, models.DO_NOTHING, blank=True, null=True)
    mandal_id = models.IntegerField(primary_key=True)
    mandal_name = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mandal'

class Village(models.Model):
    mandal = models.ForeignKey(Mandal, models.DO_NOTHING, blank=True, null=True)
    village_id = models.IntegerField(primary_key=True)
    village_name = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'village'

class VoterType(models.Model):
    voter_type_id = models.IntegerField(primary_key=True)
    voter_type_name = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'voter_type'

class Voters(models.Model):
    voter_id = models.CharField(primary_key=True, max_length=32)
    title = models.CharField(max_length=32, blank=True, null=True)
    first_name = models.CharField(max_length=32, blank=True, null=True)
    middle_name = models.CharField(max_length=32, blank=True, null=True)
    last_name = models.CharField(max_length=32, blank=True, null=True)
    gender = models.ForeignKey(Gender, models.DO_NOTHING, db_column='gender', blank=True, null=True)
    mobile_no = models.CharField(max_length=10, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    father_name = models.CharField(max_length=50, blank=True, null=True)
    caste = models.ForeignKey(Caste, models.DO_NOTHING, db_column='caste', blank=True, null=True)
    sub_caste = models.ForeignKey(SubCaste, models.DO_NOTHING, db_column='sub_caste', blank=True, null=True)
    voter_type = models.ForeignKey(VoterType, models.DO_NOTHING, db_column='voter_type', blank=True, null=True)
    voter_favour_to = models.ForeignKey(FavourTo, models.DO_NOTHING, db_column='voter_favour_to', blank=True, null=True)
    constituency = models.ForeignKey(Constituency, models.DO_NOTHING, db_column='constituency', blank=True, null=True)

    def __str__(self):
        return self.first_name +' '+ self.last_name

    class Meta:
        managed = False
        db_table = 'voters'

class VoterAddress(models.Model):
    house_no_name = models.CharField(db_column='House_No_Name', max_length=20, blank=True, null=True)  # Field name made lowercase.
    street = models.CharField(db_column='Street', max_length=32, blank=True, null=True)  # Field name made lowercase.
    postalcode = models.IntegerField(db_column='PostalCode', blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(max_length=32, blank=True, null=True)
    constituency = models.ForeignKey(Constituency, models.DO_NOTHING, db_column='constituency', blank=True, null=True)
    state = models.ForeignKey(State, models.DO_NOTHING, db_column='state', blank=True, null=True)
    country = models.ForeignKey(Country, models.DO_NOTHING, db_column='country', blank=True, null=True)
    mandal = models.ForeignKey(Mandal, models.DO_NOTHING, db_column='mandal', blank=True, null=True)
    village = models.ForeignKey(Village, models.DO_NOTHING, db_column='village', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'voter_address'

class VoterWorkDetails(models.Model):
    company_name = models.CharField(max_length=32, blank=True, null=True)
    designation = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'voter_work_details'


class Todo(models.Model):
    id = models.IntegerField(primary_key=True)
    notes = models.CharField(max_length=150, blank=True, null=True)
    created_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='created_by', blank=True, null=True)

    def __str__(self):
        return self.notes

    class Meta:
        managed = False
        db_table = 'todo'

class WardIssues(models.Model):
    id = models.IntegerField(primary_key=True)
    issue = models.CharField(max_length=150, blank=True, null=True)
    created_by = models.ForeignKey(Users, models.DO_NOTHING, db_column='created_by', blank=True, null=True)
    is_approved = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.issue

    class Meta:
        managed = False
        db_table = 'ward_issues'
