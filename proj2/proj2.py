
from datetime import datetime
start_time = datetime.now()
import streamlit as st
import os
os.chdir(r'C:\Users\PRIYA RAJ\OneDrive\Documents\GitHub\2001EE46_2022\proj2')


def proj_octant_gui():
    st.set_page_config(page_title="CS384 Project 2",page_icon=":fire:",layout="wide")
    
    #--use local CSS
    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)
    
    local_css("style/style.css")
    #--Header section
    with st.container():
        st.title("Octant Analysis Website")
        st.header("Made by- Kanishk Giri and Priya Raj")
        st.subheader("2001EE24 and 2001EE46")
    
    #section for redirecting to function pages
    with st.container():
        st.write("---")
        #-----contact----- 

        contact_form='''<form action="https://formsubmit.co/kanishk.giri.08@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name "message" placeholder="Your message here" required></textarea> 
        <button type="submit">Send</button>
        </form>'''
                
        left_column, right_column=st.columns(2)
        with left_column:
            st.write("Send your feedback here")
            st.markdown(contact_form, unsafe_allow_html=True)
        with right_column:
            st.empty()
            
proj_octant_gui()

#This shall be the last lines of the code.
end_time = datetime.now()
print('Duration of Program Execution: {}'.format(end_time - start_time))