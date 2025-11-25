from django.shortcuts import render
import joblib

def Home(request):
    return render(request,'App.html')
def Price(request):
# Load model, scaler, encoders
    model = joblib.load("model.pkl")
    scaler = joblib.load("scaler.pkl")
    encoders = joblib.load("encoders.pkl")
    if request.method == "POST":
        print("POST DATA =", request.POST)
        # Numeric
        area = float(request.POST.get("area"))
        bedrooms = int(request.POST.get("bedrooms"))
        bathrooms = int(request.POST.get("bathrooms"))

        # Categorical (STRINGS)
        mainroad = request.POST.get("mainroad")
        guestroom = request.POST.get("guestroom")
        basement = request.POST.get("basement")
        airconditioning = request.POST.get("airconditioning")
        parking = request.POST.get("parking")
        prefarea = request.POST.get("prefarea")
        furnishingstatus = request.POST.get("furnishingstatus")

        # Apply encoders
        mainroad = encoders['mainroad'].transform([mainroad])[0]
        guestroom = encoders['guestroom'].transform([guestroom])[0]
        basement = encoders['basement'].transform([basement])[0]
        airconditioning = encoders['airconditioning'].transform([airconditioning])[0]
        parking = encoders['parking'].transform([parking])[0]
        prefarea = encoders['prefarea'].transform([prefarea])[0]
        furnishingstatus = encoders['furnishingstatus'].transform([furnishingstatus])[0]

        # Scale area
        area_scaled = scaler.transform([[area]])[0][0]

        # Input array
        input_data = np.array([
            area_scaled,
            bedrooms,
            bathrooms,
            mainroad,
            guestroom,
            basement,
            airconditioning,
            parking,
            prefarea,
            furnishingstatus
        ]).reshape(1, -1)

        predicted_price = model.predict(input_data)[0]

        return render(request, "Price.html", {
            "predicted_price": int(predicted_price),
        })

    return render(request, "Price.html")

def Readme(request):
    return render(request,'Readme.html')