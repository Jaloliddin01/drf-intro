from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', 'POST'])
def hi(request: Request) -> Response:
    '''hi view'''
    pass


@api_view(['GET', 'POST'])
def addition(request: Request) -> Response:
    
    if request.method == "GET":
        query_params = request.query_params

        x = query_params.get('x', 0)
        y = query_params.get('y', 0)

        return Response({'result' : int(x)+int(y)}, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        query = request.data

        x = int(query.get('x', 0))
        y = int(query.get('y', 0))

        return Response({'result': x+y}, status=status.HTTP_200_OK)

    

@api_view(['GET'])
def subtraction(request: Request) -> Response:
    '''subtract two number'''
    pass
    

@api_view(['GET'])
def multiplication(request: Request) -> Response:
    '''multiply two number'''
    pass
    

@api_view(['GET'])
def division(request: Request) -> Response:
    '''divide two number'''
    pass