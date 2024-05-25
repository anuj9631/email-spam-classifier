import streamlit as st
from streamlit_option_menu import option_menu
import Homepage, About, Bulk_Email_Classifier, DataInsight


st.set_page_config(
    page_title="Homepage",
)

class MultiApp:
    def __init__(self):
        self.app = []
    def add_app(self, title, function):
        self.apps.append({
            "title": title,
            "function": function
        })
    def run(input_text=Homepage):
        with st.sidebar:
            app = option_menu(
                menu_title='Main Menu ',
                options=['HomePage', 'Bulk_Email_Classifier', 'DataInsight', 'About'],
                icons=['house-fill'],
                menu_icon='chat-text-fill',
                default_index=0,
                styles={
                    "container": {"padding": "5!important", "background-color": 'black'},
                    "icon": {"color": "white", "font-size": "20px"},
                    "nav-link": {"color": "white", "font-size": "18px", "text-align": "left", "margin": "0px",
                                 "--hover-color": "blue"},
                    "nav-link-selected": {"background-color": "#02ab21"}, }

            )
        if app == "HomePage":
            Homepage.app()
        if app == "DataInsight":
            DataInsight.app(input_text)
        if app == "About":
            About.app()
        if app == "Bulk_Email_Classifier":
            Bulk_Email_Classifier.app()

    run()

