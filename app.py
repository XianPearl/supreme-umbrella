import requests
import streamlit as st
from streamlit_lottie import st_lottie


#https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title= 'My webpage', page_icon= ':beating_heart:', layout = 'wide')

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

#----USE LOCAL CSS----
def local_css(f_name):
    with open(f_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
        
local_css("style/style.css")

#-----LOAD ASSETS----
#Load animations using lotte files
lt_code = load_lottieurl('https://lottie.host/86f6308f-224c-4cb4-b2ea-8b3679809a82/00gcYZWVGr.json')
lottie_code = load_lottieurl('https://lottie.host/2c8b0e2f-17df-4610-8a65-06ffb4330d94/RSf8O0CR0D.json')
lot_code = load_lottieurl('https://lottie.host/154263de-eda0-4a5d-8f08-bfea88313d61/hQIX2HQIAZ.json')
l_code = load_lottieurl('https://lottie.host/95ab4ed0-85a0-45c1-9c9a-726d7546c464/z1HWyKD6yT.json')
#-----HEADER-----
st.header ('Hi, I an Ren :wave:')
st.title ('A student of STCET')
st.subheader ('I want to be a FULL STACK DEVELOPER')

#-----WHAT AM I DOING----
with st.container():
    st.write('---')
    left_col, right_col = st.columns((2.5,1.5))
    with left_col:
        st.write ('What am i doing?')
        st.write ('######')
        st.write (
        """
        To be a FULL STACK DEVELOPER, i need to fulfill the following demands:\n
        -Build a simple database to show we know how to develop front-end and back-end\n
        -Get the 'SET TO GO' or 'THUMBS UP' from sir, and then will only move to develop our real project\n
        -Write an abstract to explain the purpose of our product\n
        -Build a wireframe and a prototype\n
        -Once approved, we'll set to build our product\n
        -Once project gets completed, we'll become full-fledged FULL STACK DEVELOPERS\n
        """)
        st.write ("[Our website link >]()")
    with right_col:
        st_lottie(lt_code, height=500, key='coding')
        
        
#----PROJECTS----
with st.container():
    st.write('---')
    st.header('My Projects')
    st.write('##')
    img_col, txt_col = st.columns((1,2))
    with img_col:
        st_lottie(lottie_code, height=500, key='write')
    with txt_col:
        st.subheader("Scholars")
        st.write("Upload your research papers as well as read other's research works :student:")
        st.subheader ("[👉]()")
        
with st.container():
    img_col, txt_col = st.columns((1,2))
    with img_col:
        st_lottie(l_code, height=300, key='service')
    with txt_col:
        st.subheader("Pharmacy & Checkup")
        st.write("Our pharmacy servive as well as doctors are available for 24/7, you can reach us in any way possible :health_worker:")
        st.subheader ("[:telephone_receiver:]()")
        
#----CONTACT-----
with st.container():
    st.write('---')
    st.header('Contact Us !!!')
    st.write('##')
    #Documentation: https://formsubmit.co/  !!! CHANGE E-MAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/subho0634@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your Name" required>
        <input type="email" name="email" placeholder="Your E-mail Address" required>
        <input type="phone" name="phone" placeholder="Your Contact Number" optional>
        <textarea name="message" placeholder="Your Message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    
    txt_col, img_col = st.columns((2,1))
    with txt_col:
        st.markdown(contact_form, unsafe_allow_html=True)
    with img_col:
        st_lottie(lot_code, height=300, key='call')
        
