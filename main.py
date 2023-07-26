import streamlit as st
import pandas as pd
import lightgbm as lgb
import pickle

header = st.container()


with header:
    st.title('Crop Recommendation App')
    st.text('This app was created to work as a gardening assistant.')
    st.text('With the crop recommendation system, all the guess work is taken out of gardening.')
    st.text('Simply enter readings from your own garden into the User Input Sidebar')
    st.text('and we will suggest the crop best suited to these conditions')


st.sidebar.header('User Input Sidebar')


def user_input_features():
    Nitrogen = st.sidebar.number_input('Input your Nitrogen reading here (0-150)', value=0, min_value=0, max_value=150, step=1, format='%d')
    Phosphorus = st.sidebar.number_input('Input your Phosphorus reading here (0-150)', value=0, min_value=0, max_value=150, step=1, format='%d')
    Potassium = st.sidebar.number_input('Input your Potassium reading here (0-210)', value=0, min_value=0, max_value=210, step=1, format='%d')
    Temperature = st.sidebar.number_input('Input your Temperature reading here (0-50)', value=0.0, min_value=0.0, max_value=50.0, step=0.1, format="%.1f")
    Humidity = st.sidebar.number_input('Input your Humidity reading here (0-100)', value=0, min_value=0, max_value=100, step=1, format='%d')
    PH = st.sidebar.number_input('Input your PH reading here (0-14)', value=0.0, min_value=0.0, max_value=14.0, step=0.1, format="%.1f")
    Rainfall = st.sidebar.number_input('Input your Rainfall reading here (0-400)', value=0, min_value=0, max_value=400, step=1, format='%d')

    data = {'Nitrogen': Nitrogen,
            'Phosphorus': Phosphorus,
            'Potassium': Potassium,
            'Temperature': Temperature,
            'Humidity': Humidity,
            'PH': PH,
            'Rainfall': Rainfall
            }
    features = pd.DataFrame(data, index=[0])
    return features
input_df = user_input_features()
st.write(input_df)


load_clf = pickle.load(open('/Users/alistair/Desktop/STREAM/lgb_model.pkl', 'rb'))
prediction = load_clf.predict(input_df)

st.subheader('Prediction')
st.write(prediction)

