from django.shortcuts import render
import random
import time
# Create your views here.


class ContextManager:
    def __enter__(self):
        print("enter section")
        return "__enter__()"

    def __exit__(self, exc_type, exc_val, ext_tb):
        print("exit setion")
        return "__exit__()"


def index(request):
    # import ipdb
    # ipdb.set_trace()
    return render(request, "base.html")




def num(number):
    for i in number:
        yield i*i


name = ['nitesh', 'kumar', 'singh', 'mohan', 'madad']
minaer = ['nitesh1', 'kumar1', 'singh1', 'mohan1', 'madad1']


def people_list(people_nom):
    result = []
    for i in range(people_nom):
        person = {"id": i, "name": random.choice(
            name), "miner": random.choice(minaer)}

        result.append(person)
    return result


def people_list_generator(people_nom):

    for i in range(people_nom):
        person = {"id": i, "name": random.choice(
            name), "miner": random.choice(minaer)}
        yield person


# def index(request):
#     peo = people_list_generator(100000)
#     # peo = people_list(100000)
#     print(peo)
#     # try:
#     #     Profile.objects.filter(user=request.user).first()
#     #     print("nitesh")
#     # except Exception as e:
#     #     print("kumar")
#     # finally:
#     #     print("singh")
#     # n = num([1, 2, 3, 4, 5])
#     # print(n)
#     # print(next(n))
#     # print(next(n))
#     # print(next(n))
#     # print(next(n))
#     # print(next(n))
#     return render(request, "base.html.j2")
