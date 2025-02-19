# 📚 Student Library Book Record System

This is a simple **Student Library Book Record System** built using **Streamlit** and **Google Sheets API**. It allows users to input and store book issuance records in a Google Spreadsheet.

## 🚀 Features
- 📄 **User-friendly Interface**: Built with Streamlit for easy interaction.
- 📑 **Google Sheets Integration**: Stores records directly in a Google Sheet.
- ✅ **Validation**: Ensures required fields are filled before submission.
- 📅 **Date Selection**: Users can pick issue and due dates from a calendar widget.

---

## 🛠️ Setup Instructions

### 1️⃣ Prerequisites
Ensure you have the following installed:
- Python 3.x
- Virtual environment (optional but recommended)
- Required Python packages (listed in `environment.yml`)

### 2️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/student-library-system.git
cd student-library-system
```

### 3️⃣ Install Dependencies
Using `pip`:
```bash
pip install -r requirements.txt
```
Using `conda` (from `environment.yml`):
```bash
conda env create -f environment.yml
conda activate library-system
```

### 4️⃣ Set Up Google Sheets API
1. Create a **Google Cloud Project** and enable the **Google Sheets API**.
2. Create a service account and download the `credentials.json` file.
3. Place the `credentials.json` file in the project directory.
4. Share your Google Sheet with the service account email.

### 5️⃣ Run the Application
```bash
streamlit run clg_lib_sys.py
```

---

## 📜 File Structure
```
📂 student-library-system
├── 📜 clg_lib_sys.py           # Main application script
├── 🔑 credentials.json         # Google API credentials (DO NOT SHARE)
├── 📄 environment.yml          # Conda environment dependencies
├── 📄 requirements.txt         # Python dependencies
└── 📝 README.md                # Project documentation
```

---

## 🎯 Usage
1. Open the Streamlit app.
2. Fill in student and book details.
3. Click **Submit Record** to store the entry in Google Sheets.
4. Records can be accessed directly from the linked Google Spreadsheet.

---

## 📌 To-Do & Future Enhancements
- [ ] **Add a Search Feature** to retrieve records.
- [ ] **Improve UI** with better styling.
- [ ] **Enable Book Return Management**.


---

🚀 **Happy Coding!** 😊

