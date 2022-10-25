import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# loading the saved models

diabetes_model = pickle.load(
    open("C:/Users/punit/Desktop/Notes/NEW_PROJECTS/MULTIPLE_DISEASE_PREDICTION_SYSTEM/SAVED_MODELS/diabetes_model.sav",
         "rb"))

heart_disease_model = pickle.load(open(
    "C:/Users/punit/Desktop/Notes/NEW_PROJECTS/MULTIPLE_DISEASE_PREDICTION_SYSTEM/SAVED_MODELS/heart_disease_model.sav",
    "rb"))

parkinsons_model = pickle.load(open(
    "C:/Users/punit/Desktop/Notes/NEW_PROJECTS/MULTIPLE_DISEASE_PREDICTION_SYSTEM/SAVED_MODELS/Parkinsons_model.sav",
    "rb"))

# sidebar for navigation

with st.sidebar:
    selected = option_menu("Multiple Disease Prediction System Using ML",
                           ["Diabetes Predictor",
                            "Heart Disease Predictor",
                            "Parkinsons Predictor"],
                           icons=["activity", "heart", "person-fill"],
                           default_index=0)

# Diabetes Predictor Page
if (selected == "Diabetes Predictor"):
    # title
    st.title("Diabetes Prediction Using ML")

    # Getting input from user
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input("Number of Pregnancies")

    with col2:
        Glucose = st.text_input("Glucose Level")

    with col3:
        BloodPressure = st.text_input("Blood Pressure Value")

    with col1:
        SkinThickness = st.text_input("Skin Thickness Value")

    with col2:
        Insulin = st.text_input("Insulin Level")

    with col3:
        BMI = st.text_input("BMI Value")

    with col1:
        DiabetesPedigreeFunction = st.text_input("Diabetes Pedigree Function Value")

    with col2:
        Age = st.text_input("Age of The Person")

    # Prediction Code
    diab_diagnosis = ""

    # Button Creation for prediction

    if st.button("Diabetes Test Result"):
        diab_prediction = diabetes_model.predict(
            [[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])

        if (diab_prediction[0] == 1):
            diab_diagnosis = "The person is diabetic"
        else:
            diab_diagnosis = "The person is not diabetic"

    st.success(diab_diagnosis)

# Heart Disease Predictor Page
if (selected == "Heart Disease Predictor"):
    # title
    st.title("Heart Disease Prediction Using ML")

    # Getting input from user
    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input("Age")

    with col2:
        sex = st.text_input("Sex")

    with col3:
        cp = st.text_input("Chest Pain types")

    with col1:
        trestbps = st.text_input("Resting Blood Pressure")

    with col2:
        chol = st.text_input("Serum Cholestoral in mg/dl")

    with col3:
        fbs = st.text_input("Fasting Blood Sugar > 120 mg/dl")

    with col1:
        restecg = st.text_input("Resting Electrocardiographic results")

    with col2:
        thalach = st.text_input("Maximum Heart Rate Achieved")

    with col3:
        exang = st.text_input("exercise induced angina")

    with col1:
        oldpeak = st.text_input("ST depression induced by exercise relative to rest")

    with col2:
        slope = st.text_input("Slope of the peak exercise ST segment")

    with col3:
        ca = st.text_input("Major vessels colored by flourosopy")

    with col1:
        thal = st.text_input("thal: 0 = normal; 1 = fixed defect; 2 = reversable defect")

    # Prediction Code
    heart_dis_diagnosis = ""

    # Button Creation for prediction

    if st.button("Heart Disease Test Result"):
        heart_dis_prediction = heart_disease_model.predict(
            [[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])

        if (heart_dis_prediction[0] == 1):
            heart_dis_diagnosis = "The person has Heart Disease"
        else:
            heart_dis_diagnosis = "The person is not diabetic"

    st.success(heart_dis_diagnosis)

# Parkinsons Predictor Page
if (selected == "Parkinsons Predictor"):
    # title
    st.title("Parkinsons Prediction Using ML")

    # Getting input from user
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        Fo = st.text_input("MDVP:Fo(Hz)")

    with col2:
        Fhi = st.text_input("MDVP:Fhi(Hz)")

    with col3:
        Flo = st.text_input("MDVP:Flo(Hz)")

    with col4:
        Jitter_percent = st.text_input("MDVP:Jitter(%)")

    with col5:
        Jitter_Abs = st.text_input("MDVP:Jitter(Abs)")

    with col1:
        RAP = st.text_input("MDVP:RAP")

    with col2:
        PPQ = st.text_input("MDVP:PPQ")

    with col3:
        DDP = st.text_input("Jitter:DDP")

    with col4:
        Shimmer = st.text_input("MDVP:Shimmer")

    with col5:
        Shimmer_dB = st.text_input("MDVP:Shimmer(dB)")

    with col1:
        APQ3 = st.text_input("Shimmer:APQ3")

    with col2:
        APQ5 = st.text_input("Shimmer:APQ5")

    with col3:
        APQ = st.text_input("MDVP:APQ")

    with col4:
        DDA = st.text_input("Shimmer:DDA")

    with col5:
        NHR = st.text_input("NHR")

    with col1:
        HNR = st.text_input("HNR")

    with col2:
        RPDE = st.text_input("RPDE")

    with col3:
        DFA = st.text_input("DFA")

    with col4:
        spread1 = st.text_input("spread1")

    with col5:
        spread2 = st.text_input("spread2")

    with col1:
        D2 = st.text_input("D2")

    with col2:
        PPE = st.text_input("PPE")

    # Prediction Code
    parkinsons_diagnosis = ""

    # Button Creation for prediction

    if st.button("Parkinsons Test Result"):
        parkinsons_prediction = parkinsons_model.predict([[Fo, Fhi, Flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP,
                                                           Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE,
                                                           DFA, spread1, spread2, D2, PPE]])

        if (parkinsons_prediction[0] == 1):
            parkinsons_diagnosis = "The person has Parkinsons"
        else:
            parkinsons_diagnosis = "The person does not have Parkinsons"

    st.success(parkinsons_diagnosis)
