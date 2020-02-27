from django.shortcuts import render

# Create your views here.
def home(request):
    if request.POST.get("find value"):
        num = request.POST['x']
        num2 = request.POST['y']
        operate = request.POST.getlist("operate_list")
        result_list = {}
        for operate in operate:

            if operate == "+":
                result = int(num) + int(num2)
                result_list[operate]=result
            elif operate == "-":
                result = int(num) - int(num2)
                result_list[operate]=result
            elif operate == "*":
                result = int(num) * int(num2)
                result_list[operate]=result
            elif operate == "/":
                result = int(num) / int(num2)
                result_list[operate]=result
        return render(request, "calculator/home.html", {"result": result, "operate": operate, "x": num, "y": num2,"result_list":result_list})

    return render(request,"calculator/home.html")