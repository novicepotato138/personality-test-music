import streamlit as st
import pandas as pd
import pickle


def predict(params):

    location, gender, isMusician, age, \
    qc2, qc3, qc4, qc5, qc6, qc7, qc8, \
    qc9, qc10, qc11, qc12, qc13, qc14, \
    qc15, qc16, qc17, qc18, qc19, qc20,\
    qc21, qc22, qc23 = params

    models = pickle.load(open('pickle_model.pkl','rb'))

    mellow = (int(qc6) + int(qc13) + int(qc11))/3
    unpretentious = (int(qc16) + int(qc5) + int(qc20))/3
    sophisticated = (int(qc3) + int(qc12) + int(qc2) + int(qc7) + int(qc4) + int(qc9) + int(qc15))/7
    intense = (int(qc21) + int(qc17) + int(qc10))/3
    contemporary = (int(qc18) + int(qc22) + int(qc8) + int(qc19))/4
    genres = [mellow, unpretentious, sophisticated, intense, contemporary]

    mellow = round(mellow, 4)
    unpretentious = round(unpretentious, 4)
    sophisticated = round(sophisticated, 4)
    intense = round(intense, 4)
    contemporary = round(contemporary, 4)

    # forming DataFrame for prediction
    txtFile = open(r'data.csv', 'w')
    txtFile.write("location,gender,isMusician,age,Mellow,Unpretentious,Sophisticated,Intense,Contemporary\n")
    txtFile.write(location + ',' + gender + ',' + isMusician + ',' + age + ',' + 
    str(mellow) + ',' + str(unpretentious) + ',' + str(sophisticated) + ',' + str(intense) + ',' + str(contemporary))
    txtFile.close()


    # perform prediction
    x_value = pd.read_csv("data.csv")
    st.dataframe(data=x_value)
    
    st.markdown("""<hr style="height:4px;border:none;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)
    st.title('Prediction Results:')
    pred = []

    for i in range(len(models)):
        prediction = models[i].predict(x_value)
        # st.write(label[i], prediction[0])
        pred.append(prediction[0])
    

    return pred