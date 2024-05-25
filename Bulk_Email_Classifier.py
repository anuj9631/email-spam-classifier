import streamlit as st
import joblib
import pandas as pd


def app():
    model = joblib.load('model.pkl')
    vectorizer = joblib.load('vectorizer.pkl')
    st.header("Bulk Email Classification")
    uploaded_file = st.file_uploader("Upload a CSV file with emails to classify", type="csv")

    if uploaded_file:
        data = pd.read_csv(uploaded_file,encoding="latin-1")

        if 'email' in data.columns:
            vectorizer1=vectorizer.transform(data['email'])
            predictions = model.predict(vectorizer1)
            data['spam'] = predictions
            st.write(data)
            st.download_button(label="Download predictions as CSV", data=data.to_csv(index=False), file_name='predictions.csv')
        else:
            st.error("The uploaded file does not have an 'email' column.")
app()
