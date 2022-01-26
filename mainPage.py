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
import sendEmail, prediction

# Header
st.set_page_config(page_title='MusicMind', page_icon='brainstorm.png', layout="centered", initial_sidebar_state="expanded")

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

st.image('logo-hybrid.png', width=200)
st.title("Predict Your Personality Through Your Music Preference")
st.write("Created by : Woon Jia Xin")
st.write("Supervised by : Dr. Siti Soraya binti Abdul Rahman")

st.sidebar.header('Part A: Demographic Background')

location = st.sidebar.selectbox('Where are you from?', ('Choose an option','Malaysia', 'Asia (Other than Malaysia)', 'Australia', 'Europe', 'North America', 'South America'), key="get_loc")
gender = st.sidebar.selectbox('Which gender do you identify most with?', ('Choose an option', 'Male', 'Female', 'Rather not to say'))
isMusician = st.sidebar.selectbox('Are you a musician?', ('Choose an option', 'Yes','No'))
age = st.sidebar.selectbox('What is your age?', ('Choose an option', 'Under 18 years old','18-24 years old', '25-34 years old', '35-44 years old', '45-54 years old', 'Above 55 years old'))

st.sidebar.header('Part B: Music Preference')
st.sidebar.write('Please indicate your basic preference for each of the following genres using the scale provided. Example video of each genre is given as a guide if you are not familiar with the genre.')
# image
img = Image.open('frame3.png')
st.sidebar.image(img)

# st.sidebar.video('https://www.youtube.com/watch?v=4ah-2pGcOWY')
# qc1 = st.sidebar.radio('1. How much do you like the the genre, Alternative or the music in Video 1.',('1', '2', '3', '4', '5', '6', '7'))
# st.sidebar.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

st.sidebar.video('https://www.youtube.com/watch?v=LnI3b9aHV9Q')
qc2 = st.sidebar.radio('1. Bluegrass',('1', '2', '3', '4', '5', '6', '7'))
st.sidebar.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

st.sidebar.video('https://www.youtube.com/watch?v=OIW4ARVbhrw')
qc3 = st.sidebar.radio('2. Blues',('1', '2', '3', '4', '5', '6', '7'))
st.sidebar.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

st.sidebar.video('https://www.youtube.com/watch?v=qr0f6t2UbOo')
qc4 = st.sidebar.radio('3. Classical',('1', '2', '3', '4', '5', '6', '7'))
st.sidebar.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

st.sidebar.video('https://www.youtube.com/watch?v=jh169rVMveA')
qc5 = st.sidebar.radio('4. Country',('1', '2', '3', '4', '5', '6', '7'))
st.sidebar.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

st.sidebar.video('https://www.youtube.com/watch?v=gCYcHz2k5x0')
qc6 = st.sidebar.radio('5. Dance/Electronica',('1', '2', '3', '4', '5', '6', '7'))
st.sidebar.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

st.sidebar.video('https://www.youtube.com/watch?v=kMLm6ti4e10')
qc7 = st.sidebar.radio('6. Folk',('1', '2', '3', '4', '5', '6', '7'))
st.sidebar.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

st.sidebar.video('https://www.youtube.com/watch?v=6sIjSNTS7Fs')
qc8 = st.sidebar.radio('7. Funk',('1', '2', '3', '4', '5', '6', '7'))
st.sidebar.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

st.sidebar.video('https://www.youtube.com/watch?v=yJpbb8ZKgwA')
qc9 = st.sidebar.radio('8. Gospel',('1', '2', '3', '4', '5', '6', '7'))
st.sidebar.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

st.sidebar.video('https://www.youtube.com/watch?v=h2LG7JXK5mQ')
qc10 = st.sidebar.radio('9. Heavy Metal',('1', '2', '3', '4', '5', '6', '7'))
st.sidebar.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

st.sidebar.video('https://www.youtube.com/watch?v=JBxreBgrJSA')
qc11 = st.sidebar.radio('10. World',('1', '2', '3', '4', '5', '6', '7'))
st.sidebar.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

st.sidebar.video('https://www.youtube.com/watch?v=iA8lgca-3RM')
qc12 = st.sidebar.radio('11. Jazz',('1', '2', '3', '4', '5', '6', '7'))
st.sidebar.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

st.sidebar.video('https://www.youtube.com/watch?v=Jl8iYAo90pE')
qc13 = st.sidebar.radio('12. New Age',('1', '2', '3', '4', '5', '6', '7'))
st.sidebar.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

st.sidebar.video('https://www.youtube.com/watch?v=5GWDgirgsq4')
qc14 = st.sidebar.radio('13. Oldies',('1', '2', '3', '4', '5', '6', '7'))
st.sidebar.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

st.sidebar.video('https://www.youtube.com/watch?v=yiTFXTNzOI0')
qc15 = st.sidebar.radio('14. Opera',('1', '2', '3', '4', '5', '6', '7'))
st.sidebar.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

st.sidebar.video('https://www.youtube.com/watch?v=vS0YXAfUo4k')
qc16 = st.sidebar.radio('15. Pop',('1', '2', '3', '4', '5', '6', '7'))
st.sidebar.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

st.sidebar.video('https://www.youtube.com/watch?v=g7KrBgnjaLY')
qc17 = st.sidebar.radio('16. Punk',('1', '2', '3', '4', '5', '6', '7'))
st.sidebar.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

st.sidebar.video('https://www.youtube.com/watch?v=FvRI37xLBjU')
qc18 = st.sidebar.radio('17. Rap/Hip Hop',('1', '2', '3', '4', '5', '6', '7'))
st.sidebar.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

st.sidebar.video('https://www.youtube.com/watch?v=HNBCVM4KbUM')
qc19 = st.sidebar.radio('18. Reggae',('1', '2', '3', '4', '5', '6', '7'))
st.sidebar.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

st.sidebar.video('https://www.youtube.com/watch?v=COQ6cni_TG8')
qc20 = st.sidebar.radio('19. Religious',('1', '2', '3', '4', '5', '6', '7'))
st.sidebar.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

st.sidebar.video('https://www.youtube.com/watch?v=7nqcL0mjMjw')
qc21 = st.sidebar.radio('20. Rock',('1', '2', '3', '4', '5', '6', '7'))
st.sidebar.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

st.sidebar.video('https://www.youtube.com/watch?v=MssKkD3Ykg8')
qc22 = st.sidebar.radio('21. Soul/R&B',('1', '2', '3', '4', '5', '6', '7'))
st.sidebar.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

st.sidebar.video('https://www.youtube.com/watch?v=c56t7upa8Bk&list=OLAK5uy_kzIUyhcmhq2z13VRW6uIvdTxgHM0r2vCQ')
qc23 = st.sidebar.radio('22. Soundtracks/Theme Song',('1', '2', '3', '4', '5', '6', '7'))
st.sidebar.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

# st.sidebar.video('https://www.youtube.com/watch?v=YxmsRbInkF4&list=OLAK5uy_lEmoWg3fL6OaCarWMvQ55LjfAiJmKFixY')
# qc24 = st.sidebar.radio('23. How much do you like the the genre, Lo-Fi or the music in Video 24.',('1', '2', '3', '4', '5', '6', '7'))
# st.sidebar.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

input = (
    location, gender, isMusician, age, \
    qc2, qc3, qc4, qc5, qc6, qc7, qc8, \
    qc9, qc10, qc11, qc12, qc13, qc14, \
    qc15, qc16, qc17, qc18, qc19, qc20,\
    qc21, qc22, qc23
    )
submitBtn = st.sidebar.button('Predict my personality')

if submitBtn:
    if location=='Choose an option' or gender=='Choose an option' or isMusician=='Choose an option' or age=='Choose an option':
        st.sidebar.warning('Please fill up incomplete answers before proceed.')
    else:
        pred = prediction.predict(input)
        sendEmail.sendEmail(time_msg, input_id, attachmentmsg)

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

        label = ['Openness to Experience (O)', 'Conscientiousness (C)', 'Extroversion (E)', 'Agreableness (A)', 'Neuroticism (N)']
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

        st.write("We sincerely thank you for using MusicMind. Please complete user acceptance test (UAT) over the link below. Your feedback is highly appreciated.")
        st.markdown(
            """
            <a href='https://forms.gle/1YCWwkGhqCERC3jSA'><button>Answer UAT Here</button></a>
            """,
        unsafe_allow_html=True,
        )
        # st.write("[Link to the form](https://forms.gle/1YCWwkGhqCERC3jSA)")
        st.write("Please include the test ID below when you are filling the acceptance test form.")
        st.code(input_id)


        st.write('Description of each trait:')
        st.markdown("• **Extroversion (E)** is the personality trait of seeking fulfillment from sources outside the self or in community. High scorers tend to be very social while low scorers prefer to work on their projects alone.")
        st.markdown("• **Agreeableness (A)** reflects much individuals adjust their behavior to suit others. High scorers are typically polite and like people. Low scorers tend to 'tell it like it is'.")
        st.markdown("• **Conscientiousness (C)** is the personality trait of being honest and hardworking. High scorers tend to follow rules and prefer clean homes. Low scorers may be messy and cheat others.")
        st.markdown("• **Neuroticism (N)** is the personality trait of being emotional.")
        st.markdown("• **Openness to Experience (O)** is the personality trait of seeking new experience and intellectual pursuits. High scores may day dream a lot. Low scorers may be very down to earth.")
        st.header(" ")

        