import streamlit as st
import joblib



def app():
    def load_model_and_vectorizer():
        model = joblib.load("model.pkl")
        vectorizer = joblib.load("vectorizer.pkl")
        return model, vectorizer

    model, vectorizer = load_model_and_vectorizer()

    def classify_text(text):
        text_vectorized = vectorizer.transform([text])
        return model.predict(text_vectorized)[0]

    def classify_proba(text):
        text_vectorized = vectorizer.transform([text])
        return model.predict_proba(text_vectorized)[0]

    # Streamlit UI
    st.title("Email Spam Classifier")

    st.markdown(
        """
    This is a simple email spam classifier. Enter some text and click 'Classify' to see if it's classified as spam or not.
    """
    )

    # Input text area
    input_text = st.text_area("Enter email text here:", height=200)
    # Store the input text in the session state
    if input_text:
        st.session_state['input_text'] = input_text
    # Classify button
    if st.button("Classify"):
        if input_text:
            st.session_state['classified'] = True
            with st.spinner("Classifying..."):
                prediction = classify_text(input_text)
                proba = classify_proba(input_text)
            st.write("## Prediction:", "Spam" if prediction == 1 else "Not Spam")
            st.write("### Probability:")
            st.write(f"- Spam: {proba[1]:.2f}")
            st.write(f"- Not Spam: {proba[0]:.2f}")
        else:
            st.warning("Please enter some text.")

app()
