import streamlit as st
from PIL import Image
import pandas as pd
import plotly.express as px
import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.application import MIMEApplication
from email import encoders
import pickle


st.set_page_config(layout="centered", initial_sidebar_state="expanded")

# set time as user come in
time = datetime.datetime.now()
time_msg = time.strftime("%c")
attachmentmsg = time.strftime('%x-%X')

input_id = 'id' + time.strftime("%d%m%y%H%M%S")

st.markdown(
    """
    <style>
    [data-testid="stSidebar"][aria-expanded="true"] > div:first-child {
        width: 500px;
    }
    [data-testid="stSidebar"][aria-expanded="false"] > div:first-child {
        width: 500px;
        margin-left: -500px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


st.title("Predict Your Personality Through Your Music Preference")
st.write("Created by : Woon Jia Xin")
st.write("Supervised by : Dr. Siti Soraya binti Abdul Rahman")
model = pickle.load(open('pickle_model.pkl','rb'))

st.sidebar.header('Part A: Demographic Background')


# location = st.sidebar.radio('Where are you from?', ('Malaysia', 'Other'))
# gender = st.sidebar.radio('Which gender do you identify most with?', ('Male', 'Female', 'Rather not to say'))
# isMusician = st.sidebar.radio('Are you a musician?', ('Yes','No'))
# age = st.sidebar.radio('What is your age?', ('Under 18 years old','18-24 years old', '25-34 years old', '35-44 years old', '45-54 years old', 'Above 55 years old'))
# duration = st.sidebar.radio('How long do you spend listening to music on a daily basis?', ('<1 hours', '1-3 hours', '>3 hours'))

location = st.sidebar.selectbox('Where are you from?', ('Choose an option','Malaysia', 'Other'))
gender = st.sidebar.selectbox('Which gender do you identify most with?', ('Choose an option', 'Male', 'Female', 'Rather not to say'))
isMusician = st.sidebar.selectbox('Are you a musician?', ('Choose an option', 'Yes','No'))
age = st.sidebar.selectbox('What is your age?', ('Choose an option', 'Under 18 years old','18-24 years old', '25-34 years old', '35-44 years old', '45-54 years old', 'Above 55 years old'))
duration = st.sidebar.selectbox('How long do you spend listening to music on a daily basis?', ('Choose an option', '<1 hours', '1-3 hours', '>3 hours'))

st.sidebar.header('Part B: Music Preference')
st.sidebar.write('Please indicate your basic preference for each of the following genres using the scale provided.')
# image
img = Image.open('frame3.png')
st.sidebar.image(img)

st.sidebar.video('https://www.youtube.com/watch?v=4ah-2pGcOWY')
qc1 = st.sidebar.radio('1. How much do you like the the genre, Alternative or the music in Video 1.',('1', '2', '3', '4', '5', '6', '7'))
st.sidebar.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

st.sidebar.video('https://www.youtube.com/watch?v=QXx4V7wXSRI')
qc2 = st.sidebar.radio('2. How much do you like the the genre, Bluegrass or the music in Video 2.',('1', '2', '3', '4', '5', '6', '7'))
st.sidebar.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

st.sidebar.video('https://www.youtube.com/watch?v=OIW4ARVbhrw')
qc3 = st.sidebar.radio('3. How much do you like the the genre, Blue or the music in Video 3.',('1', '2', '3', '4', '5', '6', '7'))
st.sidebar.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

st.sidebar.video('https://www.youtube.com/watch?v=dVkfEMKDEx4')
qc4 = st.sidebar.radio('4. How much do you like the the genre, Classical or the music in Video 4.',('1', '2', '3', '4', '5', '6', '7'))
st.sidebar.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

st.sidebar.video('https://www.youtube.com/watch?v=0oFi3bUI-UM')
qc5 = st.sidebar.radio('5. How much do you like the the genre, Country or the music in Video 5.',('1', '2', '3', '4', '5', '6', '7'))
st.sidebar.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

st.sidebar.video('https://www.youtube.com/watch?v=0faitZ956Ls')
qc6 = st.sidebar.radio('6. How much do you like the the genre, Dance/Electronica or the music in Video 6.',('1', '2', '3', '4', '5', '6', '7'))
st.sidebar.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

st.sidebar.video('https://www.youtube.com/watch?v=kMLm6ti4e10')
qc7 = st.sidebar.radio('7. How much do you like the the genre, Folk or the music in Video 7.',('1', '2', '3', '4', '5', '6', '7'))
st.sidebar.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)


st.sidebar.video('https://www.youtube.com/watch?v=6sIjSNTS7Fs')
qc8 = st.sidebar.radio('8. How much do you like the the genre, Funk or the music in Video 8.',('1', '2', '3', '4', '5', '6', '7'))
st.sidebar.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

st.sidebar.video('https://www.youtube.com/watch?v=nQWFzMvCfLE')
qc9 = st.sidebar.radio('9. How much do you like the the genre, Gospel or the music in Video 9.',('1', '2', '3', '4', '5', '6', '7'))
st.sidebar.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

st.sidebar.video('https://www.youtube.com/watch?v=h2LG7JXK5mQ')
qc10 = st.sidebar.radio('10. How much do you like the the genre, Heavy Metal or the music in Video 10.',('1', '2', '3', '4', '5', '6', '7'))
st.sidebar.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

st.sidebar.video('https://www.youtube.com/watch?v=JBxreBgrJSA')
qc11 = st.sidebar.radio('11. How much do you like the the genre, World or the music in Video 11.',('1', '2', '3', '4', '5', '6', '7'))
st.sidebar.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

st.sidebar.video('https://www.youtube.com/watch?v=iA8lgca-3RM')
qc12 = st.sidebar.radio('12. How much do you like the the genre, Jazz or the music in Video 12.',('1', '2', '3', '4', '5', '6', '7'))
st.sidebar.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

st.sidebar.video('https://www.youtube.com/watch?v=VSLsBi9xc1M')
qc13 = st.sidebar.radio('13. How much do you like the the genre, New Age or the music in Video 13.',('1', '2', '3', '4', '5', '6', '7'))
st.sidebar.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

st.sidebar.video('https://www.youtube.com/watch?v=5GWDgirgsq4')
qc14 = st.sidebar.radio('14. How much do you like the the genre, Oldies or the music in Video 14.',('1', '2', '3', '4', '5', '6', '7'))
st.sidebar.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

st.sidebar.video('https://www.youtube.com/watch?v=yiTFXTNzOI0')
qc15 = st.sidebar.radio('15. How much do you like the the genre, Opera or the music in Video 15.',('1', '2', '3', '4', '5', '6', '7'))
st.sidebar.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

st.sidebar.video('https://www.youtube.com/watch?v=vS0YXAfUo4k')
qc16 = st.sidebar.radio('16. How much do you like the the genre, Pop or the music in Video 16.',('1', '2', '3', '4', '5', '6', '7'))
st.sidebar.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

st.sidebar.video('https://www.youtube.com/watch?v=tZ4V3RrCev8')
qc17 = st.sidebar.radio('17. How much do you like the the genre, Punk or the music in Video 17.',('1', '2', '3', '4', '5', '6', '7'))
st.sidebar.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

st.sidebar.video('https://www.youtube.com/watch?v=FvRI37xLBjU')
qc18 = st.sidebar.radio('18. How much do you like the the genre, Rap/Hip Hop or the music in Video 18.',('1', '2', '3', '4', '5', '6', '7'))
st.sidebar.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

st.sidebar.video('https://www.youtube.com/watch?v=HNBCVM4KbUM')
qc19 = st.sidebar.radio('19. How much do you like the the genre, Reggae or the music in Video 19.',('1', '2', '3', '4', '5', '6', '7'))
st.sidebar.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

st.sidebar.video('https://www.youtube.com/watch?v=COQ6cni_TG8')
qc20 = st.sidebar.radio('20. How much do you like the the genre, Religious or the music in Video 20.',('1', '2', '3', '4', '5', '6', '7'))
st.sidebar.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

st.sidebar.video('https://www.youtube.com/watch?v=7nqcL0mjMjw')
qc21 = st.sidebar.radio('21. How much do you like the the genre, Rock or the music in Video 21.',('1', '2', '3', '4', '5', '6', '7'))
st.sidebar.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

st.sidebar.video('https://www.youtube.com/watch?v=MssKkD3Ykg8')
qc22 = st.sidebar.radio('22. How much do you like the the genre, Soul/R&B or the music in Video 22.',('1', '2', '3', '4', '5', '6', '7'))
st.sidebar.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

st.sidebar.video('https://www.youtube.com/watch?v=SJKEvEdPtqw')
qc23 = st.sidebar.radio('23. How much do you like the the genre, Soundtracks/Theme Song or the music in Video 23.',('1', '2', '3', '4', '5', '6', '7'))
st.sidebar.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

st.sidebar.video('https://www.youtube.com/watch?v=YxmsRbInkF4&list=OLAK5uy_lEmoWg3fL6OaCarWMvQ55LjfAiJmKFixY')
qc24 = st.sidebar.radio('24. How much do you like the the genre, Lo-Fi or the music in Video 24.',('1', '2', '3', '4', '5', '6', '7'))
st.sidebar.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)


submitBtn = st.sidebar.button('Predict my personality')

def predict():

    # calculation of big five genre
    mellow = (int(qc6) + int(qc13) + int(qc11) + int(qc24))/4
    unpretentious = (int(qc16) + int(qc5) + int(qc20))/3
    sophisticated = (int(qc3) + int(qc12) + int(qc2) + int(qc7) + int(qc4) + int(qc9) + int(qc15))/7
    intense = (int(qc21) + int(qc17) + int(qc1) + int(qc10))/4
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
    label = ['Openness to Experience (O)', 'Conscientiousness (C)', 'Extroversion (E)', 'Agreableness (A)', 'Neuroticism (N)']
    
    st.markdown("""<hr style="height:4px;border:none;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)
    st.title('Prediction Results:')
    pred = []

    for i in range(len(model)):
        prediction = model[i].predict(x_value)
        # st.write(label[i], prediction[0])
        pred.append(prediction[0])

    col1, col2, col3, col4, col5 = st.columns(5)
    col1.write('Openness to Experience')
    col2.write('Conscientiousness \n')
    col3.write('Extroversion \n')
    col4.write('Agreableness \n')
    col5.write('Neuroticism \n')
   
    col1, col2, col3, col4, col5 = st.columns(5)
    col1.header(round(pred[0], 4))
    col2.header(round(pred[1], 4))
    col3.header(round(pred[2], 4))
    col4.header(round(pred[3], 4))
    col5.header(round(pred[4], 4))
    st.header(" ")
    
    maxx = max(pred)
    idx = pred.index(maxx)
    st.write("Your most prominent(strongest) personality trait is: ")
    st.header(label[idx])

    # st.write(pred)
    df = pd.DataFrame(dict(
        r = pred,
        theta = ['Openness to Experience', 'Conscientiousness', 'Extroversion', 'Agreableness', 'Neuroticism']
        ))
    fig = px.line_polar(df, r='r', theta='theta', line_close=True)
    fig.update_traces(fill='toself')
    st.write(fig)


    st.write('Description of each trait:')
    st.markdown("• **Extroversion (E)** is the personality trait of seeking fulfillment from sources outside the self or in community. High scorers tend to be very social while low scorers prefer to work on their projects alone.")
    st.markdown("• **Agreeableness (A)** reflects much individuals adjust their behavior to suit others. High scorers are typically polite and like people. Low scorers tend to 'tell it like it is'.")
    st.markdown("• **Conscientiousness (C)** is the personality trait of being honest and hardworking. High scorers tend to follow rules and prefer clean homes. Low scorers may be messy and cheat others.")
    st.markdown("• **Neuroticism (N)** is the personality trait of being emotional.")
    st.markdown("• **Openness to Experience (O)** is the personality trait of seeking new experience and intellectual pursuits. High scores may day dream a lot. Low scorers may be very down to earth.")
    st.header(" ")

    st.write("Thank you for trying this predictor! Kindly fill in the feedback form over here. Your feedback is highly appreciated.")
    st.write("[Link to the form](https://forms.gle/xDK1VYjnt623NmVaA)")
    st.write("Please include the test ID below when you are feeling the feedback form")
    st.code(input_id)

def email():
    # x = datetime.datetime.now()
    # time_msg = x.strftime("%c")
    # attachmentmsg = time.strftime('%x-%X')

    mail_content = '''Attachment indicates new submission from the questionnaire site as following timing: ''' + time_msg

    #The mail addresses and password
    sender_address = 'bananaate12138@gmail.com'
    sender_pass = 'hmkskggnsyogrcxp'
    receiver_address = 'jessywoon@gmail.com'

    #Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = "[Questionnaire entry] " + time_msg

    #The subject line
    #The body and the attachments for the mail
    message.attach(MIMEText(mail_content, 'plain'))
    attach_file_name = 'data.csv'
    # filename = 'entry-%x-%X'

    # attach_file = open(attach_file_name, 'rb') 
    
    # # Open the file as binary mode

    # payload = MIMEBase('application', 'octate-stream')
    # payload.set_payload((attach_file).read())
    # attach_file.close()

    payload=MIMEApplication(open(attach_file_name,"rb").read())

    encoders.encode_base64(payload)

    #add payload header with filename
    # payload.add_header('Content-Decomposition', 'attachment', filename='attachment.csv')
    # message.attach(payload)

    # Add header to variable with attachment file
    payload.add_header('Content-Disposition', 'attachment', filename= 'entry-' + attachmentmsg + '.csv')
    # Then attach to message attachment file    
    message.attach(payload)
    

    #Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
    session.starttls() #enable security
    session.ehlo()
    session.login(sender_address, sender_pass) #login with mail_id and password
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()
    print('Mail Sent')


if submitBtn:
    if location=='Choose an option' or gender=='Choose an option' or isMusician=='Choose an option' or age=='Choose an option' or duration=='Choose an option':
        st.sidebar.warning('Please fill up incomplete answers before proceed.')
    else:
        predict()
        email()