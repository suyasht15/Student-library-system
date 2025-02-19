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
#### 🔑 Steps to Create `credentials.json` for Google Sheets API

To integrate your **Student Library Book Record System** with **Google Sheets**, you need to create a **service account** and download the `credentials.json` file. Follow the steps below:

#### **📌 Step 1: Create a Google Cloud Project**
1. Go to **[Google Cloud Console](https://console.cloud.google.com/)**.
2. Click **Select a Project** → **New Project**.
3. Enter a project name (e.g., `Library Management System`) and click **Create**.

#### **📌 Step 2: Enable Google Sheets API**
1. In the **Google Cloud Console**, search for **Google Sheets API**.
2. Click on **Enable**.

#### **📌 Step 3: Create a Service Account**
1. In the **Google Cloud Console**, go to **IAM & Admin** → **Service Accounts**.
2. Click **Create Service Account**.
3. Enter a **Service Account Name** (e.g., `library-records`).
4. Click **Create and Continue**.
5. Assign the role **Editor** or **Owner**.
6. Click **Done**.

#### **📌 Step 4: Generate Credentials JSON**
1. Open the newly created service account.
2. Go to the **Keys** tab → Click **Add Key** → **Create new key**.
3. Select **JSON** and click **Create**.
4. A file named **`credentials.json`** will be downloaded.

#### **📌 Step 5: Share Google Sheet Access with Service Account**
1. Open your **Google Sheet** where records will be stored.
2. Click **Share** and enter the service account email (found inside `credentials.json` under `client_email`).
3. Set permissions to **Editor**.

#### **📌 Step 6: Place `credentials.json` in Your Project**
1. Move the `credentials.json` file to your project directory.
2. Ensure your Python script correctly references this file.

---

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

## 📜 License
This project is licensed under the **MIT License**.

---

🚀 **Happy Coding!** 😊

