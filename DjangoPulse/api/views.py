from django.shortcuts import render
from rest_framework.views import APIView
from pulse.models import puls
from rest_framework.response import Response
import random
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
class GetPulsInfo(APIView):
    def get(self, request):
        puls_id = request.GET.get('id')
        if puls.objects.filter(id=puls_id).exists():
            puls_get_obj = puls.objects.get(id = puls_id)
            return Response({
                'ok': True,
                'title': puls_get_obj.title,
                'description': puls_get_obj.description
            })
        else:
            return Response({
                'ok': False,
                'verbose': 'There is no such cordiac sensor'
            })

class GetMathsPuls(APIView):
    def get(self, request):
        equation = ''
        for i in range(random.randint(3, 5)):
            num = random.randint(0, 100)
            if random.randint(1, 2) == 1:
                symbol = '-'
            else:
                symbol = '+'
            equation += str(num) + symbol

        equation = equation[:len(equation) - 1]

        return Response({
            'ok': True,
            'equation': equation,
            'correct_answer': eval(equation)
        })
        return Response({
            'ok': False,
            'verbose': 'There is no such cordiac sensor'
        })

class SetPulsVote(APIView):
    def post(self, request):
        pollId = request.POST.get('pollId')
        answerId = request.POST.get('answerId')

        poll_obj = puls.objects.get(id=pollId)  

        if answerId == '0':
            poll_obj.firstVote += 1
        else:
            poll_obj.secondVote += 1



            
        poll_obj.save()

        return Response({'ok' : True})
        

class GetVotes(APIView):
    def get(self, request):
        pollId = request.GET.get('pollId')
        poll_obj = puls.objects.get(id=pollId)

        return Response({
            'ok': True,
            'firstChoice': poll_obj.fchoice.value,
            'secondChoice': poll_obj.schoice.value,
            'firstVoteCount': poll_obj.firstVote,
            'secondVoteCount': poll_obj.secondVote,
            'winVote': poll_obj.winVote
        })

        