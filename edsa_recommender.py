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
# Logo imports
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import RendererAgg
from matplotlib.figure import Figure
_lock = RendererAgg.lock
import base64
from PIL import Image
# Custom Libraries
from utils.data_loader import load_movie_titles
from recommenders.collaborative_based import collab_model
from recommenders.content_based import content_model

# Data Loading
title_list = load_movie_titles('resources/data/movies.csv')

#
st.cache(suppress_st_warning=True,allow_output_mutation=True)
def subheading(title):
	html_temp = """<div style="background-color:{};padding:10px;margin-bottom:10px;"><h3 style="color:white;text-align:center;">"""+title+"""</h3></div>"""
	st.markdown(html_temp, unsafe_allow_html=True)


# App declaration
def main():

    # DO NOT REMOVE the 'Recommender System' option below, however,
    # you are welcome to add more options to enrich your app.

 ### Loading Company logo
    row1_space1, center_, row1_space2 = st.beta_columns((0.3, 1, 0.35, ))
    with center_,_lock :

        file_ = open('resources/imgs/logo1.gif', "rb")
        contents = file_.read()
        data_url = base64.b64encode(contents).decode("utf-8")
        file_.close()

        st.markdown(f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',unsafe_allow_html=True,)	

    
        page_options = ["Recommender System","Solution Overview", "Exploratory Data Analysis","Company Information", "Contact Us"]

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
    #Solution Overview Page
    if page_selection == "Solution Overview":
        overview_options = ["Select option"]
        st.title("Solution Overview")
        st.info('For the purpose of this project we have used two amazing techniques for building our movies  recommender App')
        
        col1, col2 = st.beta_columns(2)
        Rec_Pic =Image.open('resources/imgs/Reco.png') 
        col1.image(Rec_Pic,caption="", width=750)
        col1.write('')
        st.markdown(" __Content-based filtering__.")
        
        col3, col4,col5 = st.beta_columns(3)
        Cont =Image.open('resources/imgs/Content.png') 
        col4.image(Cont,caption="", width=200)
        
        body = 'Content-based filtering uses item features to recommend other items similar to what the user likes, based on their previous actions.'
        st.markdown(body, unsafe_allow_html=False)
        
        ##############################################################
        st.markdown("__Collaborative-based filtering__")
        
        col6, col7,col8 = st.beta_columns(3)
        Cont =Image.open('resources/imgs/Collaborative.png') 
        col7.image(Cont,caption="", width=290)
        body = 'Collaborative filtering uses similarities between users and items simultaneously to provide recommendations.'
        st.markdown(body, unsafe_allow_html=False)


        
        
        
        st.title("Play video for a brief walkthrough")
        video_file = open('resources/imgs/Pres1.webm', 'rb')
        video_bytes = video_file.read()
        st.video(video_bytes)


        
###########################################################################################
################################ Info Page ######################################################
###########################################################################################
	 	# Building out the "Company Information, Background & Team" page

    if page_selection == "Company Information":
        st.title("Company Information")
        st.info('Discover what pulled this project together and how we started')

        st.header('Our Mission')		
        st.write('To create ethical AI products and leverage the South African market for the 4th indusrtial revolution')

        st.header('Our Vision')
        st.write('A better and more intelligent South Africa, which is able to adapt to the fourth industrial revolution by using Data Science, for social good.')

        st.header('Our Amazing Team')
        st.write('A team 6 highly skilled and passionate individuals.')
        #First row of pictures

        col1, col2,col3 = st.beta_columns(3)
        Ric_Pic =Image.open('resources/imgs/resized3.jpeg') 
        col1.image(Ric_Pic,caption="Siyamukela Hadebe", width=150)
        col1.write('Data Steward')

        Cot_Pic =Image.open('resources/imgs/app_pic.jpg') 
        col2.image(Cot_Pic,caption="Courtney Murugan", width=150)
        col2.write('Project Manager')

        Cot_Pic =Image.open('resources/imgs/resized1.jpeg') 
        col3.image(Cot_Pic,caption="Nomvuselelo Simelane", width=150)
        col3.write('Software Engineer')

        #Second row of pictures
        col4, col5,col6 = st.beta_columns(3)
        vesh_Pic =Image.open('resources/imgs/resized2.jpeg') 
        col4.image(vesh_Pic,caption="Tebogo Sambo", width=150)
        col4.write('UX/UI Designer')

        Phiw_Pic =Image.open('resources/imgs/resized4.jpeg')
        col5.image(Phiw_Pic,caption="Kago Lentlopane", width=150)
        col5.write('Digital Marketer')

#Building out the Contact Page
    if page_selection == "Contact Us":
        st.title('Contact us') 
        body = ' '
        st.info('We would love to hear from you!')
        st.markdown(body, unsafe_allow_html=False)
        firstname = st.text_input("Enter your Name")
        lastname = st.text_input("Enter your last Name")
        contactdetails = st.text_input("Enter your Email address")
        message = st.text_area("Enter your Company information")

        if st.button("Submit"):
            result = ('Thanks for being awesome!')
            st.success(result)

    if page_selection == "Exploratory Data Analysis":
            #title_tag("Insights extracted from the data")
            visual_options = ["The top 10 actors", "Genres with the most number movies", "A count of films by directors"]
            visual_selection = st.selectbox("Select Option", visual_options)

            if visual_selection == "The top 10 actors":
                subheading('Top 15 movies by number of Ratings')
                st.image('resources/imgs/act001.JPG',use_column_width=True)
            elif visual_selection == "Genres with the most number movies":
                subheading('Genres with the most number movies')
                st.image('resources/imgs/genre01.JPG',use_column_width=True)
            elif visual_selection == "A count of films by directors":
                subheading('A count of films by directors')
                st.image('resources/imgs/directors001.JPG',use_column_width=True)

#
if __name__ == '__main__':
	main()
