import streamlit as st

# Function to display the blockchain logs
def display_logs():
    # Open the blockchain log file and read its contents
    try:
        with open('blockchain_logs.txt', 'r') as f:
            logs = f.readlines()

        # Display logs in a Streamlit text area or as a simple table
        st.title("Blockchain Logs Viewer")
        st.write("### Recent Blockchain Logs")

        for log in logs:
            st.text(log)  # Display each log line in the app

    except FileNotFoundError:
        st.error("Blockchain logs file not found. Please ensure the blockchain is generating logs.")

# Call the function to display logs in the Streamlit app
display_logs()
