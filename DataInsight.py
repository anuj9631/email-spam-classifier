import matplotlib.pyplot as plt
import matplotlib.patches as patches
from wordcloud import WordCloud
import streamlit as st
import joblib

def app(input_text):

    if 'input_text' in st.session_state:
        input_text = st.session_state['input_text']
        model = joblib.load('model.pkl')
        vectorizer = joblib.load('vectorizer.pkl')

        user_input_transformed = vectorizer.transform([input_text])

        # Predict using the model
        prediction = model.predict(user_input_transformed)
        prediction_prob = model.predict_proba(user_input_transformed)[0]

        fig, ax = plt.subplots()
        ax.bar(['Ham', 'Spam'], prediction_prob, color=['blue', 'red'])
        ax.set_ylim([0, 1])
        ax.set_ylabel('Probability')
        ax.set_title('Spam Detection Probability')
        st.pyplot(fig)



        wordcloud = WordCloud(width=200, height=100, background_color='white').generate(input_text)
        fig, ax = plt.subplots(figsize=(3, 2))
        ax.imshow(wordcloud)
        ax.axis('off')
        ax.set_title('Word Cloud')
        # Add border
        for spine in ax.spines.values():
            spine.set_edgecolor('black')
            spine.set_linewidth(2)
        rect = patches.Rectangle((0, 0), 200, 100, linewidth=2, edgecolor='black', facecolor='none')
        ax.add_patch(rect)

        st.pyplot(fig)
    else:
        st.markdown(
            """
            <style>
            .warning {
                background-color: #ffcccb;
                color: #ff0000;
                padding: 10px;
                border-radius: 5px;
                text-align: center;
                font-weight: bold;
            }
            </style>
            <div class="warning">
                ⚠️ No input text found. Please go to the homepage and enter some text.
            </div>
            """, unsafe_allow_html=True
        )

