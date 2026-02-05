# Chemical Equipment Data Visualizer

This project is a full-stack system developed to upload, analyze, visualize, and report industrial equipment datasets.  
It supports **Web visualization (React + Chart.js)** and **Desktop visualization (PyQt + Matplotlib)** connected to a **Django backend**.

---

## Features
- CSV Upload API using Django  
- Data Summary API (count, averages, equipment distribution)  
- React Web Dashboard with Chart.js visualizations  
- Desktop Visualization Tool using PyQt and Matplotlib  
- Upload History Management (stores last 5 uploaded datasets)  
- PDF Report Generation  
- Basic Authentication for login  
- Sample dataset support for testing  

---

## Tech Stack

**Backend**
- Django
- Pandas
- SQLite

**Frontend**
- React.js
- Chart.js
- Axios

**Desktop Application**
- Python
- PyQt5
- Matplotlib

---

## How to Run

### Backend
```bash
cd backend
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
