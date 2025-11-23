from django.shortcuts import render,redirect
def Home(request):
    return render(request,'App.html')
def Price(request):
    if request.method == "POST":
        area = request.POST.get("area")
        bedrooms = request.POST.get("bedrooms")
        bathrooms = request.POST.get("bathrooms")
        mainroad = request.POST.get("mainroad")
        guestroom = request.POST.get("guestroom")
        basement = request.POST.get("basement")
        airconditioning = request.POST.get("airconditioning")
        parking = request.POST.get("parking")
        prefarea = request.POST.get("prefarea")
        furnishingstatus = request.POST.get("furnishingstatus")

        print(area, bedrooms, bathrooms, mainroad, guestroom, prefarea,
              airconditioning, parking, furnishingstatus, basement)

        return render(request, 'Price.html', {
            "area": area,
            "bedrooms": bedrooms,
        })

    return render(request,'Price.html')
def Readme(request):
    return render(request,'Readme.html')