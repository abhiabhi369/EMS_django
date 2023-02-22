from django.shortcuts import render
from django.contrib.auth import authenticate
from django.db.models import Count
from django.db import models
from django.db.models.expressions import Case, When


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from Ems_app.models import (Users, Country, State, District, Constituency, Token, Voters, Todo,
                            WardIssues, ImportanatPeople, FavourTo, SubCaste, Caste)
from Ems_app.forms import UsersForm, VotersForm
from Ems_app.serializers import (CountrySerailizer, StateSerializer,WardIssuesSerializer,
                                 DistrictSerializer,ConstiSerializer, VoterSerializer)
from Ems_app.Tauthentication import TAuthentication

import string,random

class Home(APIView):
    def get(self,request):
        # users = Users.objects.all()
        # print('users',users)
        user = Users(email='abhilashgangula3702gmail.com',first='gangula',last='abhilash',
                     phone='9849314733')
        user.set_password('98493@Abhi')
        user.save()
        print('user',user)
        return Response({'message':'Hello....'})
    def post(self,request):
        print('request',request.data)
        user = authenticate(email=request.data['email'],password=request.data['password'])
        print('user',user)
        if user is not None:
            return Response({'message':'Hello....'})
        else:
            return Response({'message':'failed...'})

class Signup(APIView):

    permission_classes = [AllowAny]

    def get(self,request):
        form = UsersForm()
        # dic = {}
        # all_count = Country.objects.all()
        # all_states = State.objects.all()
        # all_dist = District.objects.all()
        # all_const = Constituency.objects.all()
        # coun_ser = CountrySerailizer(all_count,many=True)
        # state_ser = StateSerializer(all_states,many=True)
        # dist_ser = DistrictSerializer(all_dist,many=True)
        # const_ser = ConstiSerializer(all_const,many=True)
        # dic['Countries'] = coun_ser.data
        # dic['States'] = state_ser.data
        # dic['Districts'] = dist_ser.data
        # dic['Constituency'] = const_ser.data
        # print('dic',dic)
        # return Response({'data':dic})
        return render(request,'Signup.html',context={'form':form})
    def post(self,request):
        print('request.data',request.data)
        email = request.data['email']
        if email not in list(Users.objects.all().values_list('email',flat=True)):
            password = request.data['password']
            first = request.data['first']
            last = request.data['last']
            phone = request.data['phone']
            country = Country.objects.get(country_id=int(request.data['country']))
            state = State.objects.get(state_id=int(request.data['state']))
            district = District.objects.get(district_id=int(request.data['district']))
            constituency = Constituency.objects.get(const_id=int(request.data['constituency']))
            # print(email,password,first,last,phone,country,state,district,constituency)
            user = Users(email=email,first=first,last=last,phone=phone,country=country,
                         state=state,district=district,constituency=constituency)
            user.set_password(password)
            user.save()
        else:
            return Response({'data': 'Email already exist, please use other email'})
        print('user',user.first+' '+user.last)
        return Response({'data':{'message':'Account Created...','user':user.first+' '+user.last}})

class Login(APIView):

    permission_classes = [AllowAny]

    def token(self):
        letters = string.ascii_letters + string.digits
        return ''.join(random.sample(letters, 30))
    def post(self,request):
        print(request.data)
        user = authenticate(email=request.data['email'],password=request.data['password'])
        print('user',user)
        if user is None:
            return Response({'data':{'message':'User not found..please provide valid credentials...'}})
        else:
            token = self.token()
            if_token = Token.objects.filter(user=user)
            print('if_token',if_token)
            if if_token:
                print('there is a token')
                if_token.delete()
            else:
                print('there is no token')
            tk = Token(token=token,user=user)
            tk.save()
            print('user.constituency',user.constituency.const_id)
            user_const = user.constituency.const_id
            const_voters = Voters.objects.filter(constituency = user_const).count()
            male_voters = Voters.objects.filter(gender=1,constituency = user_const).count()
            female_voters = Voters.objects.filter(gender=2,constituency = user_const).count()
            print('const_voters',const_voters)
            print('male_voters',male_voters)
            print('female_voters',female_voters)
            res = Response({'data':{'message':'Loggedin...','user':user.first+' '+user.last,'Total_voters':const_voters,
                                    'Male_voters':male_voters,'Female_voters':female_voters}})
            res.set_cookie('token_value',token,max_age=None,httponly=True)
            print('request.user',request.user1)
            return res


class VillageIssues(APIView):
    permission_classes = [TAuthentication]

    def get(self,request):
        print('in get')
        issues = WardIssues.objects.all()
        serializer = WardIssuesSerializer(issues,many=True)
        print(serializer.data)
        return Response({'data':serializer.data})

    def post(self,request):
        print('request.data',request.data)
        print(type(request.user1))
        issue = WardIssues(id=request.data['id'],issue=request.data['issue'],created_by=request.user1,is_approved=0,status=0)
        issue.save()
        return Response({'message':'Hello...'})


class VotersCreate(APIView):
    permission_classes = [AllowAny]
    def get(self,request):
        form = VotersForm()
        return render(request,'Voters_create.html',context={'form':form})

    def post(self,request):
        print(request.data)
        serializer = VoterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
        else:
            print(serializer.errors)
            return Response({'message':serializer.errors})
        return Response({'message':'hello....'})

class FavourToView(APIView):
    permission_classes = [TAuthentication]
    def get(self,request):
        dic = {}
        favours_list = FavourTo.objects.annotate(num_votes=models.Count('voters')).filter(state=request.user1.state.state_id)
        print('aaaaaaaaaaa',favours_list)
        for i in favours_list:
            dic[i.favour_to_name]=i.num_votes
            # dic['Count'] = i.num_votes
        return Response({'data':dic})

class CasteFilter(APIView):
    permission_classes = [TAuthentication]
    def get(self,request):
        # all_caste = SubCaste.objects.annotate(num_caste=Count('voters')).filter
        # print('all_caste',all_caste)
        # for i in all_caste:
        #     print(i.sub_caste_name)
        #     print(i.num_caste)
        #     lis.append(i.num_caste)
        all_caste = SubCaste.objects.annotate(num_caste=Count(Case(When(voters__constituency=2,then=1)))).all()
        print('all_caste',all_caste)
        for i in all_caste:
            print(i.num_caste,i.sub_caste_name)
        return Response({'message':'hello...'})


class Check(APIView):
    permission_classes = [AllowAny]
    def get(self,request):
        print("request.data",request.data)
        # print('request.user1',request.user1)
        # print(Voters.objects.all().values('constituency'))
        print('Hello...')
        return Response({'message':'hello...'})


'''
{
"email":"abhilashgangula37@gmail.com",
"password":"98493@Abhi"
}
'''
