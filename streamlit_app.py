import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import numpy as np

st.title("🚀 My First Streamlit App")
st.write("DONE")

df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/refs/heads/master/penguins_cleaned.csv')


with st.expander('Penguin Data'):
    st.write("**RAW DATA**")
    df


    st.write("**X**: _features_")
    X_raw = df.drop('species', axis=1)
    X_raw

    st.write('**y**: _label_')
    y_raw = df.species
    y_raw


with st.expander('Data Visualization'):
    st.scatter_chart(data=df, x="bill_length_mm", y="body_mass_g", color="species")


# Input Features
with st.sidebar:
    st.header('Input Features')
    island = st.selectbox('Island', ('Biscoe', 'Dream', 'Torgersen'))
    bill_length_mm = st.slider('Bill length (mm)', 32.1, 59.6, 43.9)
    bill_depth_mm = st.slider('Bill depth (mm)', 13.1, 21.5, 17.2)
    flipper_length_mm = st.slider('Flipper length (mm)', 172.0, 231.0, 201.0)
    body_mass_g = st.slider('Body mass (g)', 2700.0, 6300.0, 4207.0)
    sex = st.selectbox('Sex', ('male', 'female'))

    # Create a DataFrame for the input features
    data = {'island': island,
            'bill_length_mm': bill_length_mm,
            'bill_depth_mm': bill_depth_mm,
            'flipper_length_mm': flipper_length_mm,
            'body_mass_g': body_mass_g,
            'sex': sex}
    
    input_df = pd.DataFrame(data, index=[0])
    input_penguins = pd.concat([input_df, X_raw], axis=0)


with st.expander('Input Features'):
    st.write('**Input Penguin**')
    input_df
    st.write('**Combined Penguins Data**')
    input_penguins


# Data Preparation
# Encode X
encode = ['island', 'sex']
df_penguins = pd.get_dummies(input_penguins, prefix=encode)

X = df_penguins[1:]
input_row = df_penguins[:1]

# Encode y
target_mapper = {
    'Adelie': 0,
    'Chinstrap': 1,
    'Gentoo': 2}
def target_encode(val):
    return target_mapper[val]

y = y_raw.apply(target_encode)

with st.expander('Data Preparation'):
    st.write('**Encoded X (input penguin)**')
    input_row
    st.write('**Encoding of y(species)**')
    st.write('''      Adelie:  0, Chinstrap:  1, Gentoo:  2''')
    st.write('**Encoded y**')
    y


# Model training and inference
# Traing the ML model
clf = RandomForestClassifier()
clf.fit(X, y)


# Apply model to make predictions
prediction = clf.predict(input_row)
prediction_proba = clf.predict_proba(input_row)

df_prediction_proba = pd.DataFrame(prediction_proba)
df_prediction_proba.columns = ['Adelie', 'Chinstrap', 'Gentoo']
df_prediction_proba.rename(columns={0: 'Adelie',
                                    1: 'Chinstrap',
                                    2: 'Gentoo'})

# Display predicted species
st.subheader('Predicted Species')
st.dataframe(df_prediction_proba,
             column_config={
                 'Adelie': st.column_config.ProgressColumn(
                     'Adelie',
                     format='%f',
                     width='medium',
                     min_value=0,
                     max_value=1
                 ),
                 'Chinstrap': st.column_config.ProgressColumn(
                     'Chinstap',
                     format='%f',
                     width='medium',
                     min_value=0,
                     max_value=1
                 ),
                 'Gentoo': st.column_config.ProgressColumn(
                     'Gentoo',
                     format='%f',
                     width='medium',
                     min_value=0,
                     max_value=1
                 ),
             }, hide_index=True)

df_prediction_proba

penguins_species = np.array(['Adelie', 'Chinstrap', 'Gentoo'])
st.success(str(penguins_species[prediction][0]))