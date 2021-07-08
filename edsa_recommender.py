"""

    Streamlit webserver-based Recommender Engine.

    Author: Explore Data Science Academy.

    Note:
    ---------------------------------------------------------------------
    Please follow the instructions provided within the README.md file
    located within the root of this repository for guidance on how to use
    this script correctly.

    NB: !! Do not remove/modify the code delimited by dashes !!

    This application is intended to be partly marked in an automated manner.
    Altering delimited code may result in a mark of 0.
    ---------------------------------------------------------------------

    Description: This file is used to launch a minimal streamlit web
	application. You are expected to extend certain aspects of this script
    and its dependencies as part of your predict project.

	For further help with the Streamlit framework, see:

	https://docs.streamlit.io/en/latest/

"""
# Streamlit dependencies
import streamlit as st

# Data handling dependencies
import pandas as pd
import numpy as np

# Custom Libraries
from utils.data_loader import load_movie_titles
from recommenders.collaborative_based import collab_model
from recommenders.content_based import content_model

# Data Loading
title_list = load_movie_titles('resources/data/movies.csv')

# App declaration
def main():

    # DO NOT REMOVE the 'Recommender System' option below, however,
    # you are welcome to add more options to enrich your app.
    page_options = ["Recommender System","Solution Overview", "Company Information, Background & Team"]

    # -------------------------------------------------------------------
    # ----------- !! THIS CODE MUST NOT BE ALTERED !! -------------------
    # -------------------------------------------------------------------
    page_selection = st.sidebar.selectbox("Choose Option", page_options)
    if page_selection == "Recommender System":
        # Header contents
        st.write('# Movie Recommender Engine')
        st.write('### EXPLORE Data Science Academy Unsupervised Predict')
        st.image('resources/imgs/Image_header.png',use_column_width=True)
        # Recommender System algorithm selection
        sys = st.radio("Select an algorithm",
                       ('Content Based Filtering',
                        'Collaborative Based Filtering'))

        # User-based preferences
        st.write('### Enter Your Three Favorite Movies')
        movie_1 = st.selectbox('Fisrt Option',title_list[14930:15200])
        movie_2 = st.selectbox('Second Option',title_list[25055:25255])
        movie_3 = st.selectbox('Third Option',title_list[21100:21200])
        fav_movies = [movie_1,movie_2,movie_3]

        # Perform top-10 movie recommendation generation
        if sys == 'Content Based Filtering':
            if st.button("Recommend"):
                try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = content_model(movie_list=fav_movies,
                                                            top_n=10)
                    st.title("We think you'll like:")
                    for i,j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                except:
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")


        if sys == 'Collaborative Based Filtering':
            if st.button("Recommend"):
                try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = collab_model(movie_list=fav_movies,
                                                           top_n=10)
                    st.title("We think you'll like:")
                    for i,j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                except:
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")


    # -------------------------------------------------------------------

    # ------------- SAFE FOR ALTERING/EXTENSION -------------------
    if page_selection == "Solution Overview":
        st.title("Solution Overview")
        st.write("Describe your winning approach on this page")

###########################################################################################
################################ EDA ######################################################
###########################################################################################
	# Building out the "Company Information, Background & Team" page
    if page_selection == "Company Information, Background & Team":
                st.info("Meet the amazing team members that contributed to this project.")
                # st.markdown("<h1 style='text-align: center;'>Contributors</h1>", unsafe_allow_html=True)
                # st.markdown("\n\n")

                ### IN ALPHABETICAL ORDER ###
                # Bulelani
                st.markdown("<h3 style='text-align: center;'>Bulelani Nkosi</h3>", unsafe_allow_html=True)
                st.markdown("<p style='text-align: center;'>Streamlit App Coordinator | Data Analyst</p>", unsafe_allow_html=True)
                st.image('resources/imgs/Bulelani.jpg', width=120)
                st.markdown("<a href='https://www.linkedin.com/in/bulelanin' target='_blank'>LinkedIn</a>", unsafe_allow_html=True)
                st.markdown("<a href='https://github.com/BNkosi' target='_blank'>GitHub</a>", unsafe_allow_html=True)

                # Lizette
                st.markdown("<h3 style='text-align: center;'>Lizette Loubser</h3>", unsafe_allow_html=True)
                st.markdown("<p style='text-align: center;'>Notebook Coordinator | ML Engineer</p>", unsafe_allow_html=True)
                st.image('resources/imgs/Lizette.jpg', width=120)
                st.markdown("<a href='http://www.linkedin.com/in/lizette-loubser' target='_blank'>LinkedIn</a>", unsafe_allow_html=True)
                st.markdown("<a href='https://github.com/Lizette95' target='_blank'>GitHub</a>", unsafe_allow_html=True)

                # Neli
                st.markdown("<h3 style='text-align: center;'>Nelisiwe Mabanga</h3>", unsafe_allow_html=True)
                st.markdown("<p style='text-align: center;'>Data Journalist | Analyst</p>", unsafe_allow_html=True)
                st.image('resources/imgs/nelly.jpeg', width=120)
                st.markdown("<a href='https://www.linkedin.com/in/nelisiwe-mabanga-8bb409106/' target='_blank'>LinkedIn</a>", unsafe_allow_html=True)
                st.markdown("<a href='https://github.com/Phiwe-Mabanga' target='_blank'>GitHub</a>", unsafe_allow_html=True)

                # Nolu
                st.markdown("<h3 style='text-align: center;'>Noluthando Khumalo</h3>", unsafe_allow_html=True)
                st.markdown("<p style='text-align: center;'>Streamlit App Designer</p>", unsafe_allow_html=True)
                st.image('resources/imgs/Thando.jpg', width=120)
                st.markdown("<a href='https://www.linkedin.com/in/noluthando-khumalo-3870ab191/' target='_blank'>LinkedIn</a>", unsafe_allow_html=True)
                st.markdown("<a href='https://github.com/ThandoKhumalo' target='_blank'>GitHub</a>", unsafe_allow_html=True)

                # Nompilo
                st.markdown("<h3 style='text-align: center;'>Nompilo Nhlabathi</h3>", unsafe_allow_html=True)
                st.markdown("<p style='text-align: center;'>Streamlit App Designer</p>", unsafe_allow_html=True)
                st.image('resources/imgs/Nompilo.png', width=120)
                st.markdown("<a href='http://www.linkedin.com/in/nompilo-nhlabathi-2701791b2' target='_blank'>LinkedIn</a>", unsafe_allow_html=True)
                st.markdown("<a href='https://github.com/mapilos' target='_blank'>GitHub</a>", unsafe_allow_html=True)

                # Sizwe
                st.markdown("<h3 style='text-align: center;'>Sizwe Bhembe</h3>", unsafe_allow_html=True)
                st.markdown("<p style='text-align: center;'>Notebook Assistant</p>", unsafe_allow_html=True)
                st.image('resources/imgs/Sizwe.jpg', width=120)
                st.markdown("<a href='https://www.linkedin.com/in/sizwe-bhembe-372880101' target='_blank'>LinkedIn</a>", unsafe_allow_html=True)
                st.markdown("<a href='https://github.com/sjbhembe' target='_blank'>GitHub</a>", unsafe_allow_html=True)

#

if __name__ == '__main__':
    main()
    
