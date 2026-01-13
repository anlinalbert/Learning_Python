import streamlit as st
import requests
import pandas as pd

# The URL where your FastAPI is running
API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="Ticketing Tool", page_icon="🎫")
st.title("🎫 IT Ticketing Tool")

# --- SECTION 1: CREATE TICKET ---
st.header("Create a New Ticket")

with st.form("ticket_form"):
    # ADJUST THESE FIELDS to match your 'CreateTicket' model in models.py
    title = st.text_input("Ticket Title")
    description = st.text_area("Description")
    priority = st.selectbox("Priority", ["Low", "Medium", "High"])

    submitted = st.form_submit_button("Submit Ticket")

    if submitted:
        # Create the JSON payload
        ticket_data = {
            "title": title,
            "description": description,
            "priority": priority
        }

        try:
            # Send POST request to FastAPI
            response = requests.post(f"{API_URL}/create_ticket", json=ticket_data)

            if response.status_code == 200:
                st.success(f"Ticket created successfully! ID: {response.json().get('id')}")
            else:
                st.error(f"Error creating ticket: {response.text}")
        except requests.exceptions.ConnectionError:
            st.error("Could not connect to the API. Is FastAPI running?")

# --- SECTION 2: VIEW TICKETS ---
st.write("---")
st.header("Existing Tickets")

if st.button("Refresh Tickets"):
    try:
        # Send GET request to FastAPI
        response = requests.get(f"{API_URL}/tickets")

        if response.status_code == 200:
            tickets = response.json()
            if tickets:
                # Convert JSON to a Pandas DataFrame for a nice table
                df = pd.DataFrame(tickets)
                st.dataframe(df, use_container_width=True)
            else:
                st.info("No tickets found.")
        else:
            st.error("Failed to retrieve tickets.")

    except requests.exceptions.ConnectionError:
        st.error("Could not connect to the API. Is FastAPI running?")

# --- SECTION 2: VIEW TICKETS ---
st.write("---")
st.header("Existing Tickets")
if st.button("Clear DB"):
    try:
        response = requests.delete(f"{API_URL}/clear_db")

        if response.status_code == 200:
            tickets = response.json()
            if tickets:
                # Convert JSON to a Pandas DataFrame for a nice table
                df = pd.DataFrame(tickets)
                st.dataframe(df, use_container_width=True)
            else:
                st.info("DB cleared successfully.")
        else:
            st.error("Failed to clear DB.")

    except requests.exceptions.ConnectionError:
        st.error("Could not connect to the API. Is FastAPI running?")