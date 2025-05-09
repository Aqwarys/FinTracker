# 💰 FinTracker

**FinTracker** is a Django-based personal finance tracking application. It allows users to add, filter, and manage their financial transactions, as well as export them as a CSV file by specifying a date range.

---

## 🚀 Features

* Add income and expense transactions
* Categorize transactions
* Filter by operation type, category, and date
* Export transactions to CSV within a selected date range
* Responsive interface with integrated date pickers

---

## 🛠️ Tech Stack

* **Backend:** Django, Django REST Framework
* **Frontend:** Bootstrap, HTML, jQuery
* **Libraries:** Pandas (for export), Django Filter

---

## 📦 Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/fintracker.git
   cd fintracker
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Apply the migrations:

   ```bash
   python manage.py migrate
   ```

5. Start the development server:

   ```bash
   python manage.py runserver
   ```

6. Open your browser and go to:

   ```
   http://127.0.0.1:8000/
   ```

---

## 📁 Project Structure

```
fintracker/
├── tracker/             # Main Django app
│   ├── models.py        # Transaction model
│   ├── views.py         # Views for listing and exporting
│   ├── forms.py         # Forms for input and filtering
│   ├── urls.py          # App-specific routes
│   └── templates/
│       └── export_data/
│           └── export_data.html  # Export UI
├── static/              # CSS/JS files
├── manage.py
└── requirements.txt     # Project dependencies
```

---

## 📤 Exporting Data

To export transactions:

1. Go to the export section
2. Select a start and end date
3. Click **"Export"**
4. A CSV file will be automatically downloaded

---

## 🧪 Running Tests

*(Optional section – if you plan to add unit tests)*

```bash
python manage.py test
```

---


## 👤 Author

**Aqwarys**
GitHub: [Aqwarys](https://github.com/Aqwarys)

Contributions and feedback are always welcome!
