import streamlit as st

def app():
    st.title("📧 Email Spam Detector")

    st.markdown(
        """
        <style>
        .main {
            background-color: #f5f5f5;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
        }
        .header {
            font-size: 24px;
            font-weight: bold;
            color: #4a4a4a;
        }
        .subheader {
            font-size: 20px;
            color: #4a4a4a;
        }
        .content {
            font-size: 16px;
            color: #4a4a4a;
            line-height: 1.6;
        }
        .icon {
            font-size: 24px;
            color: #4a4a4a;
            vertical-align: middle;
        }
        .email-icon {
            font-size: 50px;
            color: #1f77b4;
            vertical-align: middle;
        }
        </style>
        """, unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="main">
            <p class="header">Overview</p>
            <p class="content">
                The <span class="email-icon">📧</span> <strong>Email Spam Detector</strong> is a machine learning-based application designed to help users determine whether a given email is spam or not. By analyzing the content of the email, the system can classify it as either 'Spam' or 'Not Spam' with a certain level of probability.
            </p>
            <p class="header">Purpose</p>
            <p class="content">
                Spam emails are not only annoying but can also pose significant risks including phishing, scams, and the spread of malware. This tool aims to provide a simple yet effective way to identify and filter out such unwanted emails, enhancing email security and user productivity.
            </p>
            <p class="header">Technology Stack</p>
            <p class="content">
                The Email Spam Detector is built using the following technologies:
            </p>
            <ul class="content">
                <li><span class="icon">🌐</span> <strong>Streamlit</strong>: For creating the interactive web interface.</li>
                <li><span class="icon">🔍</span> <strong>Scikit-learn</strong>: For building and training the machine learning model.</li>
                <li><span class="icon">💾</span> <strong>Joblib</strong>: For model serialization and deserialization.</li>
                <li><span class="icon">📊</span> <strong>Pandas</strong>: For data manipulation and preprocessing.</li>
                <li><span class="icon">📈</span> <strong>Matplotlib & WordCloud</strong>: For data visualization.</li>
            </ul>
            <p class="header">How It Works</p>
            <p class="content">
                The application works as follows:
            </p>
            <ol class="content">
                <li><strong>Input Text</strong>: Users can enter the text of an email into the provided text area on the homepage.</li>
                <li><strong>Text Vectorization</strong>: The entered text is transformed into numerical features using TF-IDF (Term Frequency-Inverse Document Frequency) vectorization.</li>
                <li><strong>Prediction</strong>: A pre-trained Support Vector Machine (SVM) model processes the vectorized text to predict whether the email is spam or not.</li>
                <li><strong>Probability Display</strong>: The probabilities of the email being 'Spam' or 'Not Spam' are displayed to the user, along with a visualization.</li>
            </ol>
            <p class="header">Usage</p>
            <ul class="content">
                <li><strong>HomePage</strong>: Enter the email text and classify it to see if it's spam.</li>
                <li><strong>DataInsight</strong>: View detailed insights and visualizations based on the email content.</li>
                <li><strong>Bulk Email Classifier</strong>: Upload a CSV file containing multiple emails for bulk classification.</li>
            </ul>
            <p class="header">Team</p>
            <p class="content">
                This project was developed by a team of dedicated data scientists and software engineers committed to enhancing email security through innovative machine learning solutions.
            </p>
            <p class="header">Contact</p>
            <p class="content">
                If you have any questions or feedback, please reach out to us at <a href="mailto:support@spamdetector.com">support@spamdetector.com</a>.
            </p>
            <p class="content">
                Thank you for using the Email Spam Detector!
            </p>
        </div>
        """, unsafe_allow_html=True
    )

if __name__ == "__main__":
    app()
