from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializer import *


# create
@api_view(['POST'])
def create_todo(request):
    item = request.POST.get('item')
    Todo.objects.create(item=item)
    print(item)
    return Response('successfully submitted!')


# get tasks that are in progress(not fully done yet)
@api_view(['GET'])
def inprog(request):
    items = request.GET.get('status')
    item = Todo.objects.filter(status=1)
    ser = TodoSerializer(item, many=True)
    return Response(ser.data)


# get tasks that are finished
@api_view(['GET'])
def finished(request):
    items = request.GET.get('status')
    item = Todo.objects.filter(status=3)
    ser = TodoSerializer(item, many=True)
    return Response(ser.data)


# get deleted tasks
@api_view(['GET'])
def deleted(request):
    items = request.GET.get('status')
    item = Todo.objects.filter(status=2)
    ser = TodoSerializer(item, many=True)
    return Response(ser.data)


# edit a task
@api_view(['PUT'])
def update(request, pk):
    try:
        item = request.POST.get('item')
        status = request.POST.get('status')
        i = Todo.objects.get(id=pk)
        i.item = item
        i.status = status
        i.save()
        ser = TodoSerializer(i)
        return Response(ser.data)
    except Exception as err:
        return Response(f'{err}')

