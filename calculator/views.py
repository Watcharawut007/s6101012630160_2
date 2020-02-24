from django.shortcuts import render

# Create your views here.
def home(request):
    if request.POST.get("find value"):
        num = request.POST['x']
        num2 = request.POST['y']
        operate = request.POST["operate_list"]
        if operate == "+":
            result = int(num) + int(num2)

            return render(request,"calculator/home.html",{"result":result,"operate":operate,"x":num,"y":num2})
        elif operate == "-":
            result = int(num) - int(num2)

            return render(request, "calculator/home.html", {"result": result, "operate": operate,"x":num,"y":num2})
        elif operate == "*":
            result = int(num) * int(num2)
            return render(request,"calculator/home.html",{"result":result,"operate":operate,"x":num,"y":num2})
        elif operate == "/":
            result = int(num) / int(num2)
            return render(request,"calculator/home.html",{"result":result,"operate":operate,"x":num,"y":num2})

    return render(request,"calculator/home.html")