# 🛡️ Insurance Management System – Django Web Application

A comprehensive web-based Insurance Management System built with Python and Django, inspired by the operational structure of the Ethiopian Insurance Corporation. It provides both administrative and customer-facing interfaces to streamline policy management, applications, and communication.

## 🚀 Features

### Admin Panel

- **Policy Management**: Create, update, and delete insurance policies and categories.

- **Customer Management**: View and manage customer profiles and submitted policy applications.

- **Application Workflow**: Approve or reject customer policy requests, with status tracking.

- **Communications**: Respond to customer inquiries via an integrated messaging interface.

### Customer Portal

- **User Registration & Authentication**: Secure sign‑up, login, and password recovery using Django’s built‑in system.

- **Browse Policies**: View all available insurance plans with details and pricing.

- **Policy Application**: Submit new insurance applications and monitor approval status in real time.

## 🛠️ Tech Stack

- **Backend**: [Django](https://www.djangoproject.com/) — High‑level Python web framework for rapid, clean development.
- **Database**: [SQLite](https://www.sqlite.org/) — Lightweight, file‑based SQL database engine.
- **Frontend**: HTML, CSS, [Bootstrap](https://getbootstrap.com/) responsive UI toolkit.
- **Authentication**: Django’s built‑in auth system (users, permissions, sessions).
- **Deployment**: Run locally with `python manage.py runserver` or deploy to any WSGI‑compatible host.

## 📦 Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/HiyawNT/Insurance-Management-System-Django.git
   cd Insurance-Management-System-Django
   ```
2. **Create & activate a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate      # macOS/Linux
   venv\Scripts\activate.bat     # Windows

   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt

   ```

4. **Apply migrations & create superuser**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   python manage.py createsuperuser
   ```

5. **Run the development server**

   ```bash
   python manage.py runserver
   ```

Open your browser to [http://localhost:8000](http://localhost:8000) to access the application.

## 📝 License

This project is licensed under the MIT License.

## 📬 Contact

For any inquiries or support, please contact [HiyawNT](https://github.com/HiyawNT) or via Email at [hiyaw.temitim@gmail.com](mailto:hiyaw.temitim@gmail.com).
