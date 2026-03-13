import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# loading the saved models
diabetes_model = pickle.load(open("diabetes_model.sav", "rb"))
heart_disease_model = pickle.load(open("heart_disease_model.sav", "rb"))
parkinsons_model = pickle.load(open("Parkinsons_model.sav", "rb"))

# sidebar for navigation
with st.sidebar:
    selected = option_menu(
        "Multiple Disease Prediction System Using ML",
        ["Diabetes Predictor", "Heart Disease Predictor", "Parkinsons Predictor"],
        icons=["activity", "heart", "person-fill"],
        default_index=0
    )

# Diabetes Predictor Page
if selected == "Diabetes Predictor":
    st.title("Diabetes Prediction Using ML")

    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.number_input("Number of Pregnancies", min_value=0, step=1)
    with col2:
        Glucose = st.number_input("Glucose Level", min_value=0.0, format="%.2f")
    with col3:
        BloodPressure = st.number_input("Blood Pressure Value", min_value=0.0, format="%.2f")

    with col1:
        SkinThickness = st.number_input("Skin Thickness Value", min_value=0.0, format="%.2f")
    with col2:
        Insulin = st.number_input("Insulin Level", min_value=0.0, format="%.2f")
    with col3:
        BMI = st.number_input("BMI Value", min_value=0.0, format="%.2f")

    with col1:
        DiabetesPedigreeFunction = st.number_input("Diabetes Pedigree Function Value", min_value=0.0, format="%.3f")
    with col2:
        Age = st.number_input("Age of The Person", min_value=0, step=1)

    diab_diagnosis = ""

    if st.button("Diabetes Test Result"):
        diab_prediction = diabetes_model.predict([[
            Pregnancies, Glucose, BloodPressure, SkinThickness,
            Insulin, BMI, DiabetesPedigreeFunction, Age
        ]])

        if diab_prediction[0] == 1:
            diab_diagnosis = "The person is diabetic"
        else:
            diab_diagnosis = "The person is not diabetic"

    st.success(diab_diagnosis)

# Heart Disease Predictor Page
if selected == "Heart Disease Predictor":
    st.title("Heart Disease Prediction Using ML")

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.number_input("Age", min_value=0, step=1)
    with col2:
        sex = st.number_input("Sex (0 = Female, 1 = Male)", min_value=0, max_value=1, step=1)
    with col3:
        cp = st.number_input("Chest Pain types", min_value=0, step=1)

    with col1:
        trestbps = st.number_input("Resting Blood Pressure", min_value=0.0, format="%.2f")
    with col2:
        chol = st.number_input("Serum Cholestoral in mg/dl", min_value=0.0, format="%.2f")
    with col3:
        fbs = st.number_input("Fasting Blood Sugar > 120 mg/dl (0/1)", min_value=0, max_value=1, step=1)

    with col1:
        restecg = st.number_input("Resting Electrocardiographic results", min_value=0, step=1)
    with col2:
        thalach = st.number_input("Maximum Heart Rate Achieved", min_value=0.0, format="%.2f")
    with col3:
        exang = st.number_input("Exercise induced angina (0/1)", min_value=0, max_value=1, step=1)

    with col1:
        oldpeak = st.number_input("ST depression induced by exercise relative to rest", format="%.2f")
    with col2:
        slope = st.number_input("Slope of the peak exercise ST segment", min_value=0, step=1)
    with col3:
        ca = st.number_input("Major vessels colored by flourosopy", min_value=0, step=1)

    with col1:
        thal = st.number_input("thal: 0 = normal; 1 = fixed defect; 2 = reversible defect", min_value=0, max_value=2, step=1)

    heart_dis_diagnosis = ""

    if st.button("Heart Disease Test Result"):
        heart_dis_prediction = heart_disease_model.predict([[
            age, sex, cp, trestbps, chol, fbs, restecg,
            thalach, exang, oldpeak, slope, ca, thal
        ]])

        if heart_dis_prediction[0] == 1:
            heart_dis_diagnosis = "The person has Heart Disease"
        else:
            heart_dis_diagnosis = "The person does not have Heart Disease"

    st.success(heart_dis_diagnosis)

# Parkinsons Predictor Page
if selected == "Parkinsons Predictor":
    st.title("Parkinsons Prediction Using ML")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        Fo = st.number_input("MDVP:Fo(Hz)", format="%.6f")
    with col2:
        Fhi = st.number_input("MDVP:Fhi(Hz)", format="%.6f")
    with col3:
        Flo = st.number_input("MDVP:Flo(Hz)", format="%.6f")
    with col4:
        Jitter_percent = st.number_input("MDVP:Jitter(%)", format="%.6f")
    with col5:
        Jitter_Abs = st.number_input("MDVP:Jitter(Abs)", format="%.6f")

    with col1:
        RAP = st.number_input("MDVP:RAP", format="%.6f")
    with col2:
        PPQ = st.number_input("MDVP:PPQ", format="%.6f")
    with col3:
        DDP = st.number_input("Jitter:DDP", format="%.6f")
    with col4:
        Shimmer = st.number_input("MDVP:Shimmer", format="%.6f")
    with col5:
        Shimmer_dB = st.number_input("MDVP:Shimmer(dB)", format="%.6f")

    with col1:
        APQ3 = st.number_input("Shimmer:APQ3", format="%.6f")
    with col2:
        APQ5 = st.number_input("Shimmer:APQ5", format="%.6f")
    with col3:
        APQ = st.number_input("MDVP:APQ", format="%.6f")
    with col4:
        DDA = st.number_input("Shimmer:DDA", format="%.6f")
    with col5:
        NHR = st.number_input("NHR", format="%.6f")

    with col1:
        HNR = st.number_input("HNR", format="%.6f")
    with col2:
        RPDE = st.number_input("RPDE", format="%.6f")
    with col3:
        DFA = st.number_input("DFA", format="%.6f")
    with col4:
        spread1 = st.number_input("spread1", format="%.6f")
    with col5:
        spread2 = st.number_input("spread2", format="%.6f")

    with col1:
        D2 = st.number_input("D2", format="%.6f")
    with col2:
        PPE = st.number_input("PPE", format="%.6f")

    parkinsons_diagnosis = ""

    if st.button("Parkinsons Test Result"):
        parkinsons_prediction = parkinsons_model.predict([[
            Fo, Fhi, Flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP,
            Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR,
            RPDE, DFA, spread1, spread2, D2, PPE
        ]])

        if parkinsons_prediction[0] == 1:
            parkinsons_diagnosis = "The person has Parkinsons"
        else:
            parkinsons_diagnosis = "The person does not have Parkinsons"

    st.success(parkinsons_diagnosis)
