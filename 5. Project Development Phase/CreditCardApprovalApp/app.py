from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

# Load trained model
model = joblib.load("credit_card_approval_model.pkl")

# ---------------- Encoding Dictionaries ---------------- #

gender_map = {"F": 0, "M": 1}

car_map = {"N": 0, "Y": 1}

realty_map = {"N": 0, "Y": 1}

income_type_map = {
    "Commercial associate": 0,
    "Pensioner": 1,
    "State servant": 2,
    "Student": 3,
    "Working": 4
}

education_map = {
    "Academic degree": 0,
    "Higher education": 1,
    "Incomplete higher": 2,
    "Lower secondary": 3,
    "Secondary / secondary special": 4
}

family_map = {
    "Civil marriage": 0,
    "Married": 1,
    "Separated": 2,
    "Single / not married": 3,
    "Widow": 4
}

housing_map = {
    "Co-op apartment": 0,
    "House / apartment": 1,
    "Municipal apartment": 2,
    "Office apartment": 3,
    "Rented apartment": 4,
    "With parents": 5
}

occupation_map = {
    "Accountants": 0,
    "Cleaning staff": 1,
    "Cooking staff": 2,
    "Core staff": 3,
    "Drivers": 4,
    "HR staff": 5,
    "High skill tech staff": 6,
    "IT staff": 7,
    "Laborers": 8,
    "Low-skill Laborers": 9,
    "Managers": 10,
    "Medicine staff": 11,
    "Private service staff": 12,
    "Realty agents": 13,
    "Sales staff": 14,
    "Secretaries": 15,
    "Security staff": 16,
    "Unknown": 17,
    "Waiters/barmen staff": 18
}

# ---------------- Home Page ---------------- #

@app.route("/")
def home():
    return render_template("home.html")


# ---------------- Prediction Form ---------------- #

@app.route("/predict")
def prediction_page():
    return render_template("index.html")


# ---------------- Prediction ---------------- #

@app.route("/predict", methods=["POST"])
def predict():

    new_data = pd.DataFrame({

        "CODE_GENDER":[gender_map[request.form["gender"]]],
        "FLAG_OWN_CAR":[car_map[request.form["car"]]],
        "FLAG_OWN_REALTY":[realty_map[request.form["realty"]]],
        "CNT_CHILDREN":[int(request.form["children"])],
        "AMT_INCOME_TOTAL":[float(request.form["income"])],
        "NAME_INCOME_TYPE":[income_type_map[request.form["income_type"]]],
        "NAME_EDUCATION_TYPE":[education_map[request.form["education"]]],
        "NAME_FAMILY_STATUS":[family_map[request.form["family"]]],
        "NAME_HOUSING_TYPE":[housing_map[request.form["housing"]]],
        "FLAG_MOBIL":[int(request.form["mobil"])],
        "FLAG_WORK_PHONE":[int(request.form["work_phone"])],
        "FLAG_PHONE":[int(request.form["phone"])],
        "FLAG_EMAIL":[int(request.form["email"])],
        "OCCUPATION_TYPE":[occupation_map[request.form["occupation"]]],
        "CNT_FAM_MEMBERS":[float(request.form["family_members"])],
        "AGE":[float(request.form["age"])],
        "YEARS_EMPLOYED":[float(request.form["employment"])]

    })

    prediction = model.predict(new_data)

    if prediction[0] == 0:
        result = "✅ Credit Card Approved"
    else:
        result = "❌ Credit Card Rejected"

    return render_template("result.html", prediction=result)


if __name__ == "__main__":
    app.run(debug=True)