Overview

The 📧 Email Spam Detector is a machine learning-based application designed to help users determine whether a given email is spam or not. By analyzing the content of the email, the system can classify it as either 'Spam' or 'Not Spam' with a certain level of probability.
Livelink: https://email-spam-classifier-4l9x.onrender.com/
Purpose

Spam emails are not only annoying but can also pose significant risks including phishing, scams, and the spread of malware. This tool aims to provide a simple yet effective way to identify and filter out such unwanted emails, enhancing email security and user productivity.

Technology Stack

The Email Spam Detector is built using the following technologies:

🌐 Streamlit: For creating the interactive web interface.
🔍 Scikit-learn: For building and training the machine learning model.
💾 Joblib: For model serialization and deserialization.
📊 Pandas: For data manipulation and preprocessing.
📈 Matplotlib & WordCloud: For data visualization.
How It Works

The application works as follows:

Input Text: Users can enter the text of an email into the provided text area on the homepage.
Text Vectorization: The entered text is transformed into numerical features using TF-IDF (Term Frequency-Inverse Document Frequency) vectorization.
Prediction: A pre-trained Support Vector Machine (SVM) model processes the vectorized text to predict whether the email is spam or not.
Probability Display: The probabilities of the email being 'Spam' or 'Not Spam' are displayed to the user, along with a visualization.
Usage

HomePage: Enter the email text and classify it to see if it's spam.
DataInsight: View detailed insights and visualizations based on the email content.
Bulk Email Classifier: Upload a CSV file containing multiple emails for bulk classification.
![em-1](https://github.com/anuj963![em-3](https://github.com/anuj9631/email-spam-classifier/assets/124524155/3b427f9b-0b94-415d-b2ea-2ec44b3f0005)
1/email-spam-classifier/assets/124524155/28b184a7-62ca-4883-ac00-867b0ce3c52b)
![em-2](https://github.com/anuj9631/email-spam-classifier/assets/124524155/e93d7f7b-664c-4ec4-9716-f4f5f2f74a17)
