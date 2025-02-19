import streamlit as st
import gspread
from google.oauth2.service_account import Credentials
import datetime

# --- Google Sheets Setup ---
# Path to your service account credentials JSON file
SERVICE_ACCOUNT_FILE = 'credentials.json'  # Ensure this file is in your project directory

# Define the required scopes for the Google Sheets API
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# Authenticate using the service account credentials
credentials = Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE,
    scopes=SCOPES
)

# Authorize and create a client to interact with the Google Sheet
gc = gspread.authorize(credentials)

# Use the Spreadsheet ID instead of the name
spreadsheet_id = '1CSeh0C2WGuFNtVwD-wyOgs0c_1H-272m48P-2YViLRI'  # Replace with your actual Spreadsheet ID

try:
    sheet = gc.open_by_key(spreadsheet_id).sheet1  # Open by spreadsheet ID
except Exception as e:
    st.error(f"Error accessing the spreadsheet: {e}")

# --- Streamlit UI ---
st.title("📚 Student Library Book Record")

st.markdown("Fill out the form below to add a new library record:")

# Create a form for user input
with st.form("record_form"):
    student_name = st.text_input("👤 Student Name")
    student_id = st.text_input("🎓 Student ID")
    contact_no= st.text_input("Contact No.")
    book_title = st.text_input("📖 Book Title")
    book_id = st.text_input("📚 Book ID")
    issue_date = st.date_input("📅 Issue Date", datetime.date.today())
    due_date = st.date_input("📅 Due Date", datetime.date.today())
    
    
    
    submit_button = st.form_submit_button("📌 Submit Record")

# --- Form Submission ---
if submit_button:
    # Validate required fields
    if not all([student_name, student_id, book_title, book_id]):
        st.error("⚠️ Please fill out all required fields.")
    else:
        try:
            # Prepare the row data (converting dates to strings)
            row = [
                student_name,
                student_id,
                contact_no,
                book_title,
                book_id,
                issue_date.strftime("%Y-%m-%d"),
                due_date.strftime("%Y-%m-%d")
            ]
            # Append the row to the Google Sheet
            sheet.append_row(row)
            st.success("✅ Record added successfully!")
        except Exception as e:
            st.error(f"❌ Error adding record: {e}")
