from django.shortcuts import render

# Create your views here.
from calculator.models import Calculate


def calculating(num, num2, operate):
    if operate == "+":
        resultvalue = int(num) + int(num2)
    elif operate == "-":
        resultvalue = int(num) - int(num2)
    elif operate == "*":
        resultvalue = int(num) * int(num2)
    elif operate == "/":
        resultvalue = int(num) / int(num2)
    return resultvalue
def home(request):
    history_list = Calculate.objects.all()
    string_list = []
    for history in history_list:
        string_list.append(str(history.num1) + history.operate + str(history.num2) + " " +"is"+" "+":"+str(history.result))
    if request.GET.get("find value"):
        num = request.GET['x']
        num2 = request.GET['y']
        operates = request.GET.getlist("operate_list")
        if num == '' or num2 == '' or operates == []:
            return render(request,"calculator/home.html",{"result_list":"plz enter your input"})
        else :
            result_list = {}
            for operate in operates:
                object = Calculate.objects.create()
                result = calculating(num,num2,operate)
                result_list[operate]=result
                object.calculate(num, num2, operate, result)

        return render(request, "calculator/home.html", {"operate": operate,'op':operates, "x": num, "y": num2,"result_list":result_list,"history":string_list})
    if request.GET.get('clear_history'):
        for history in history_list:
            history.delete()
        return render(request,"calculator/home.html",{"history":Calculate.objects.all()})
    return render(request,"calculator/home.html",{"history":string_list})


