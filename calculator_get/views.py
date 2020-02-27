from django.shortcuts import render

# Create your views here.
from calculator_get.models import Calculate_get


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
    history_list = Calculate_get.objects.all()
    string_list = []
    for history in history_list:
        string_list.append(str(history.num1) + history.operate + str(history.num2) + " " +"is"+" "+":"+str(history.result))
    if request.POST.get("find value"):
        num = request.POST['x']
        num2 = request.POST['y']
        operates = request.POST.getlist("operate_list")
        if num == '' or num2 == '' or operates == []:
            return render(request,"get_templates/home.html",{"result_list":"plz enter your input"})
        else :
            result_list = {}
            for operate in operates:
                object = Calculate_get.objects.create()
                result = calculating(num,num2,operate)
                result_list[operate]=result
                object.caculate(num, num2, operate, result)

        return render(request, "get_templates/home.html", {"operate": operate,'op':operates, "x": num, "y": num2,"result_list":result_list,"history":string_list})
    if request.POST.get('clear_history'):
        for history in history_list:
            history.delete()
        return render(request,"get_templates/home.html",{"history":Calculate_get.objects.all()})
    return render(request,"get_templates/home.html",{"history":string_list})


