# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class CasteDetails(models.Model):
    caste_id = models.AutoField(db_column='Caste_Id', primary_key=True)  # Field name made lowercase.
    caste_name = models.CharField(db_column='Caste_Name', max_length=20)  # Field name made lowercase.
    created_id = models.CharField(db_column='Created_Id', max_length=50)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_Date')  # Field name made lowercase.
    updated_id = models.CharField(db_column='Updated_Id', max_length=50)  # Field name made lowercase.
    updated_date = models.DateTimeField(db_column='Updated_Date')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Caste_Details'


class ConstituencyDetails(models.Model):
    constituency_id = models.IntegerField(db_column='Constituency_Id', primary_key=True)  # Field name made lowercase.
    constituency_name = models.CharField(db_column='Constituency_Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    constituency_type = models.CharField(db_column='Constituency_Type', max_length=20, blank=True, null=True)  # Field name made lowercase.
    dist = models.ForeignKey('DistrictDetails', models.DO_NOTHING, db_column='Dist_Id', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_Date')  # Field name made lowercase.
    updated_id = models.CharField(db_column='Updated_Id', max_length=50)  # Field name made lowercase.
    updated_date = models.DateTimeField(db_column='Updated_Date')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Constituency_Details'


class CountryDetails(models.Model):
    country_id = models.AutoField(db_column='Country_Id', primary_key=True)  # Field name made lowercase.
    country_code = models.CharField(db_column='Country_Code', max_length=5, blank=True, null=True)  # Field name made lowercase.
    country_name = models.CharField(db_column='Country_Name', max_length=50)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_Date')  # Field name made lowercase.
    updated_id = models.CharField(db_column='Updated_Id', max_length=50)  # Field name made lowercase.
    updated_date = models.DateTimeField(db_column='Updated_Date')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Country_Details'


class DistrictDetails(models.Model):
    dist_id = models.AutoField(db_column='Dist_ID', primary_key=True)  # Field name made lowercase.
    dist_name = models.CharField(db_column='Dist_Name', max_length=50)  # Field name made lowercase.
    state = models.ForeignKey('StateDetails', models.DO_NOTHING, db_column='State_Id', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_Date')  # Field name made lowercase.
    updated_id = models.CharField(db_column='Updated_Id', max_length=50)  # Field name made lowercase.
    updated_date = models.DateTimeField(db_column='Updated_Date')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'District_Details'


class GenderDetails(models.Model):
    gender_id = models.AutoField(db_column='Gender_Id', primary_key=True)  # Field name made lowercase.
    gender_name = models.CharField(db_column='Gender_Name', max_length=6, blank=True, null=True)  # Field name made lowercase.
    created_id = models.CharField(db_column='Created_Id', max_length=50)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_Date')  # Field name made lowercase.
    updated_id = models.CharField(db_column='Updated_Id', max_length=50)  # Field name made lowercase.
    updated_date = models.DateTimeField(db_column='Updated_Date')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Gender_Details'


class StateDetails(models.Model):
    state_id = models.AutoField(db_column='State_Id', primary_key=True)  # Field name made lowercase.
    state_code = models.CharField(db_column='State_Code', max_length=3, blank=True, null=True)  # Field name made lowercase.
    state_name = models.CharField(db_column='State_Name', max_length=50)  # Field name made lowercase.
    country = models.ForeignKey(CountryDetails, models.DO_NOTHING, db_column='Country_Id', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_Date')  # Field name made lowercase.
    updated_id = models.CharField(db_column='Updated_Id', max_length=50)  # Field name made lowercase.
    updated_date = models.DateTimeField(db_column='Updated_Date')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'State_Details'


class SubCasteDetails(models.Model):
    sub_caste_id = models.AutoField(db_column='Sub_Caste_Id', primary_key=True)  # Field name made lowercase.
    sub_caste_name = models.CharField(db_column='Sub_Caste_Name', max_length=20, blank=True, null=True)  # Field name made lowercase.
    caste = models.ForeignKey(CasteDetails, models.DO_NOTHING, db_column='Caste_Id', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_Date')  # Field name made lowercase.
    updated_id = models.CharField(db_column='Updated_Id', max_length=50)  # Field name made lowercase.
    updated_date = models.DateTimeField(db_column='Updated_Date')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Sub_Caste_Details'


class UserDetails(models.Model):
    email_id = models.CharField(db_column='Email_id', primary_key=True, max_length=100)  # Field name made lowercase.
    first_name = models.CharField(db_column='First_Name', max_length=32, blank=True, null=True)  # Field name made lowercase.
    last_name = models.CharField(db_column='Last_Name', max_length=32, blank=True, null=True)  # Field name made lowercase.
    user_pwd = models.CharField(db_column='User_Pwd', max_length=32, blank=True, null=True)  # Field name made lowercase.
    phone_no = models.IntegerField(db_column='Phone_No', blank=True, null=True)  # Field name made lowercase.
    country_id = models.CharField(db_column='Country_id', max_length=10, blank=True, null=True)  # Field name made lowercase.
    state_id = models.CharField(db_column='State_id', max_length=50, blank=True, null=True)  # Field name made lowercase.
    district_id = models.CharField(db_column='District_id', max_length=50, blank=True, null=True)  # Field name made lowercase.
    constituency_id = models.CharField(db_column='Constituency_id', max_length=50, blank=True, null=True)  # Field name made lowercase.
    user_role = models.CharField(db_column='User_Role', max_length=50, blank=True, null=True)  # Field name made lowercase.
    created_id = models.CharField(db_column='Created_Id', max_length=50)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_Date')  # Field name made lowercase.
    updated_id = models.CharField(db_column='Updated_Id', max_length=50)  # Field name made lowercase.
    updated_date = models.DateTimeField(db_column='Updated_Date')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'User_Details'
