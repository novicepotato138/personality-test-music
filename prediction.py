import streamlit as st
import pandas as pd
import pickle


def predict(params):
    X1 = generate_X1(params)
    X2 = generate_X2(params)
    models = pickle.load(open('pickle_model.pkl','rb'))

    st.dataframe(data=X2)
    
    st.markdown("""<hr style="height:4px;border:none;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)
    st.title('Prediction Results:')
    pred = []

    for i in range(len(models)):
        prediction = models[i].predict(X2)
        # st.write(label[i], prediction[0])
        pred.append(prediction[0])
    

    return pred


def generate_X1(params):
    location, gender, isMusician, age, \
    qc2, qc3, qc4, qc5, qc6, qc7, qc8, \
    qc9, qc10, qc11, qc12, qc13, qc14, \
    qc15, qc16, qc17, qc18, qc19, qc20,\
    qc21, qc22, qc23 = params

    mellow = (qc6 + qc13 + qc11)/3
    unpretentious = (qc16 + qc5 + qc20)/3
    sophisticated = (qc3 + qc12 + qc2 + qc7 + qc4 + qc9 + qc15)/7
    intense = (qc21 + qc17 + qc10)/3
    contemporary = (qc18 + qc22 + qc8 + qc19)/4
    # genres = [mellow, unpretentious, sophisticated, intense, contemporary]

    mellow = round(mellow, 4)
    unpretentious = round(unpretentious, 4)
    sophisticated = round(sophisticated, 4)
    intense = round(intense, 4)
    contemporary = round(contemporary, 4)

    # forming DataFrame for prediction
    txtFile = open(r'X1.csv', 'w')
    txtFile.write("bluegrass,blues,classical,country,dance,folk,funk,gospel,heavymetal,world,jazz,newage,oldies,opera,pop,punk,rap,reggae,religious,rock,rnb,soundtracks,Mellow,Unpretentious,Sophisticated,Intense,Contemporary,location,gender,isMusician,age\n")
    arrangement = ','.join([qc2,qc3,qc4,qc5,qc6,qc7,qc8,qc9,qc10,qc11,qc12,qc13,qc14,qc15,qc16,qc17,qc18,qc19,qc20,qc21,qc22,qc23,mellow,unpretentious,sophisticated,intense,contemporary])
    txtFile.write(arrangement)
    txtFile.close()

    # perform prediction
    df = pd.read_csv("X1.csv")
    return pd.get_dummies(df)
    

def generate_X2(params):
    return pd.DataFrame()

