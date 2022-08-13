import streamlit as st
from streamlit_google_oauth import google_oauth2_required

@google_oauth2_required
def main():
    ALLOWED_ACCOUT_LIST = ['yoshiohagino0025@gmail.com','yoshio.hagino@jp.ricoh.com']

    user_id = st.session_state.user_id
    user_email = st.session_state.user_email 
    st.write(f"You're {user_id}, {user_email}")

    if user_email in  ALLOWED_ACCOUT_LIST:
        st.write(f"You're are allowed logged in this site")
    else:
        st.write(f"You can not loggin this site {user_id}, {user_email}")

main()