import streamlit as st
import webbrowser

# Default login credentials
default_username = "admin"
default_password = "password"

# Session state for login status
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

def login(username, password):
    """Checks if the login credentials are correct."""
    return username == default_username and password == default_password

def main():
    st.sidebar.title("Login Page")

    if not st.session_state.logged_in:
        st.sidebar.subheader("Please log in")

        username = st.sidebar.text_input("Username")
        password = st.sidebar.text_input("Password", type="password")

        if st.sidebar.button("Login"):
            if login(username, password):
                st.session_state.logged_in = True
                st.success("Login successful! Redirecting to Google...")
                webbrowser.open("https://www.google.com")
            else:
                st.sidebar.error("Invalid username or password")
    else:
        st.sidebar.success("You are logged in!")
        st.write("Welcome! Redirecting to Google...")
        webbrowser.open("https://www.google.com")

if __name__ == "__main__":
    main()
