import streamlit as st
import pandas as pd
import pickle
import os

def predict(params):
    X1 = generate_X1(params)
    X2 = generate_X2(params)
    models = pickle.load(open('pickle_model.pkl','rb'))

    st.dataframe(data=X2.iloc[:, :5])
    st.markdown("""<hr style="height:4px;border:none;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)
    st.title('Prediction Results:')

    pred = []
    df_to_use = [X2, X1, X1, X1, X2]
    for i in range(len(models)):
        prediction = models[i].predict(df_to_use[i])
        # st.write(label[i], prediction[0])
        pred.append(prediction[0])

    return pred


def generate_X1(params):
    location, gender, isMusician, age, \
    qc2, qc3, qc4, qc5, qc6, qc7, qc8, \
    qc9, qc10, qc11, qc12, qc13, qc14, \
    qc15, qc16, qc17, qc18, qc19, qc20,\
    qc21, qc22, qc23 = params

    mellow = (int(qc6) + int(qc13) + int(qc11))/3
    unpretentious = (int(qc16) + int(qc5) + int(qc20))/3
    sophisticated = (int(qc3) + int(qc12) + int(qc2) + int(qc7) + int(qc4) + int(qc9) + int(qc15))/7
    intense = (int(qc21) + int(qc17) + int(qc10))/3
    contemporary = (int(qc18) + int(qc22) + int(qc8) + int(qc19))/4
    # genres = [mellow, unpretentious, sophisticated, intense, contemporary]

    mellow = round(mellow, 4)
    unpretentious = round(unpretentious, 4)
    sophisticated = round(sophisticated, 4)
    intense = round(intense, 4)
    contemporary = round(contemporary, 4)

    # forming DataFrame for prediction
    txtFile = open(r'X1.csv', 'w')

    txtFile.write("bluegrass,blues,classical,country,dance,folk,funk,gospel,heavymetal,world,jazz,newage,oldies,opera,pop,punk,rap,reggae,religious,rock,rnb,soundtracks,Mellow,Unpretentious,Sophisticated,Intense,Contemporary,location_asia,location_australia,location_europe,location_malaysia,location_north_america,location_south_america,gender_Female,gender_Male,gender_Prefer not to say,isMusician_No,isMusician_Yes,age_18 - 24,age_25 - 34,age_35 - 44,age_45 - 54,age_Above 55,age_Under 18\n")
    arrangement = ','.join([qc2,qc3,qc4,qc5,qc6,qc7,qc8,qc9,qc10,qc11,qc12,qc13,qc14,qc15,qc16,qc17,qc18,qc19,qc20,qc21,qc22,qc23,str(mellow),str(unpretentious),str(sophisticated),str(intense),str(contemporary),
    "1" if location == "Asia (Other than Malaysia)" else "0", "1" if location == "Australia" else "0", "1" if location == "Europe" else "0", "1" if location == "Malaysia" else "0", "1" if location == "North America" else "0", "1" if location == "South America" else "0",
    "1" if gender == "Female" else "0", "1" if gender == "Male" else "0", "1" if gender == "Prefer not to say" else "0",
    "1" if isMusician == "No" else "0", "1" if isMusician == "Yes" else "0",
    "1" if age == "18-24 years old" else "0", "1" if age == "25-34 years old" else "0", "1" if age == "35-44 years old" else "0", "1" if age == "45-54 years old" else "0", "1" if age == "Above 55 years old" else "0", "1" if age == "Under 18 years old" else "0"
    ])
    txtFile.write(arrangement)
    txtFile.close()

    # perform prediction
    df = pd.read_csv("X1.csv")

    # X1.csv will be remove at sendEmail.py after email is sent!

    return df
    

def generate_X2(params):
    location, gender, isMusician, age, \
    qc2, qc3, qc4, qc5, qc6, qc7, qc8, \
    qc9, qc10, qc11, qc12, qc13, qc14, \
    qc15, qc16, qc17, qc18, qc19, qc20,\
    qc21, qc22, qc23 = params

    mellow = (int(qc6) + int(qc13) + int(qc11))/3
    unpretentious = (int(qc16) + int(qc5) + int(qc20))/3
    sophisticated = (int(qc3) + int(qc12) + int(qc2) + int(qc7) + int(qc4) + int(qc9) + int(qc15))/7
    intense = (int(qc21) + int(qc17) + int(qc10))/3
    contemporary = (int(qc18) + int(qc22) + int(qc8) + int(qc19))/4
    # genres = [mellow, unpretentious, sophisticated, intense, contemporary]

    mellow = round(mellow, 4)
    unpretentious = round(unpretentious, 4)
    sophisticated = round(sophisticated, 4)
    intense = round(intense, 4)
    contemporary = round(contemporary, 4)

    # remove file
    if os.path.isfile("X2.csv"):
        os.remove("X2.csv")

    # forming DataFrame for prediction
    txtFile = open(r'X2.csv', 'w')

    txtFile.write("Mellow,Unpretentious,Sophisticated,Intense,Contemporary,location_asia,location_australia,location_europe,location_malaysia,location_north_america,location_south_america,gender_Female,gender_Male,gender_Prefer not to say,isMusician_No,isMusician_Yes,age_18 - 24,age_25 - 34,age_35 - 44,age_45 - 54,age_Above 55,age_Under 18\n")
    arrangement = ','.join([str(mellow),str(unpretentious),str(sophisticated),str(intense),str(contemporary),
    "1" if location == "Asia (Other than Malaysia)" else "0", "1" if location == "Australia" else "0", "1" if location == "Europe" else "0", "1" if location == "Malaysia" else "0", "1" if location == "North America" else "0", "1" if location == "South America" else "0",
    "1" if gender == "Female" else "0", "1" if gender == "Male" else "0", "1" if gender == "Prefer not to say" else "0",
    "1" if isMusician == "No" else "0", "1" if isMusician == "Yes" else "0",
    "1" if age == "18-24 years old" else "0", "1" if age == "25-34 years old" else "0", "1" if age == "35-44 years old" else "0", "1" if age == "45-54 years old" else "0", "1" if age == "Above 55 years old" else "0", "1" if age == "Under 18 years old" else "0"
    ])
    txtFile.write(arrangement)
    txtFile.close()

    # perform prediction
    df = pd.read_csv("X2.csv")

    # remove file after reading
    if os.path.isfile("X2.csv"):
        os.remove("X2.csv")

    return df
