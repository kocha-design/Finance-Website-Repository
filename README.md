# Obrigado Finance - White-Label Corporate Website

![Django](https://img.shields.io/badge/Django-5.0-green)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-14-blue)
![Python](https://img.shields.io/badge/Python-3.13-yellow)
![License](https://img.shields.io/badge/License-Commercial-red)

A premium, fully dynamic, and responsive white-label website template designed for international finance and banking institutions. Built with **Django**, **PostgreSQL**, and **Vanilla HTML/CSS/JS**.

This project is designed so that **100% of the website content** (text, images, colors, services, team, etc.) is controlled via the Django Admin Dashboard. No coding is required to customize the site for a new client.

---

## 🌟 Key Features

### 1. 🎨 Full White-Label Branding (Admin Controlled)
- **Dynamic Colors:** Change Primary, Secondary, Accent, Dark, Text, and Background colors directly from the Admin using a visual **Color Picker**.
- **Dynamic Logo & Branding:** Upload a client logo, change the company name, and update footer text.
- **Dynamic Hero Slider:** Upload multiple high-resolution images with custom titles and subtitles for the homepage hero slider.
- **Dynamic WhatsApp Chat:** Set a WhatsApp number in the admin to activate a floating chat button on all pages.

### 2. 📄 Fully Dynamic Pages
- **Home Page:** Dynamic Hero Slider, Quick Stats, Auto-scrolling Partners Marquee, Features, Latest Insights, and Call-To-Action.
- **About Us:** Dynamic Mission/Vision, Core Values, Leadership Team (with photos), Statistics, and Client Testimonials.
- **Services:** Add unlimited services with custom emojis/icons and descriptions.
- **Gallery:** Upload images categorized by Events, Office, Team, or Awards with a hover overlay effect.
- **News & Alerts:** Post company announcements. Urgent alerts are highlighted with a red border and an "Important Alert" badge.
- **Insights (Blog):** Write articles with images, excerpts, and full content.
- **FAQ:** Add questions and answers, displayed in a smooth accordion layout.
- **Contact:** Dynamic address, email, phone, and a professional contact form.

### 3. 🚀 Technical Features
- **Database:** PostgreSQL (Production-ready) with environment variables (`.env`) for security.
- **Security:** `SECRET_KEY` and database credentials are hidden in `.env` (never pushed to GitHub).
- **Responsive Design:** Mobile-first CSS Grid and Flexbox layouts. Works perfectly on phones, tablets, and desktops.
- **Animations:** Smooth scroll-reveal animations, hover effects, and a floating "Scroll to Top" button.
- **Newsletter:** Footer subscription form that saves emails directly to the database.
- **Seed Data:** A custom management command (`seed_data`) to instantly populate the site with professional sample data (text, images, stats).

---

## 🛠️ Tech Stack

- **Backend:** Python 3, Django 5
- **Database:** PostgreSQL
- **Frontend:** HTML5, CSS3 (Custom Variables, Grid, Flexbox), Vanilla JavaScript
- **Icons & Fonts:** FontAwesome 6, Google Fonts (Manrope)
- **Environment Management:** `python-dotenv`

---

## ⚙️ Installation & Setup Guide

### Prerequisites
- Python 3.10+
- PostgreSQL installed and running
- Git

### 1. Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/obrigado-finance.git
cd obrigado-finance

2. Create a Virtual Environment
cmd

python -m venv venv
venv\Scripts\activate

3. Install Dependencies
cmd

pip install -r requirements.txt

4. Setup Environment Variables

Create a .env file in the root directory and add your credentials:
env

SECRET_KEY=your-super-secret-key-here
DEBUG=True
DB_NAME=finance_website_db
DB_USER=postgres
DB_PASSWORD=your-database-password
DB_HOST=localhost
DB_PORT=5432

5. Setup PostgreSQL Database

Open your PostgreSQL terminal (psql) and create the database:
sql

CREATE DATABASE obrigado_finance;

6. Run Migrations
cmd

python manage.py makemigrations
python manage.py migrate

7. Seed Sample Data (Optional but Recommended)

To instantly populate the website with professional sample data:
cmd

python manage.py seed_data

8. Create Superuser (Admin Account)
cmd

python manage.py createsuperuser

9. Run the Server
cmd

python manage.py runserver

    Public Website: http://127.0.0.1:8000/

    Admin Dashboard: http://127.0.0.1:8000/admin/

📁 Project Structure
text

obrigado_finance/
│
├── config/                 # Main Django project settings
├── core/                   # Main application (Models, Views, Admin)
│   ├── management/
│   │   └── commands/
│   │       └── seed_data.py # Custom command to seed sample data
│   ├── migrations/
│   ├── admin.py            # Admin dashboard configuration (Color pickers, etc.)
│   ├── models.py           # Database schema
│   ├── views.py            # Page logic
│   └── urls.py             # App routing
│
├── static/                 # Static files (CSS, JS, Admin custom JS)
│   ├── css/style.css       # Main stylesheet (Dynamic CSS variables)
│   ├── js/main.js          # Slider, FAQ, and Scroll animations
│   └── admin/js/           # Custom admin color picker script
│
├── templates/              # HTML Templates
│   ├── base.html           # Master layout (Header, Footer, Chat widget)
│   ├── home.html           # Homepage with slider
│   ├── about.html          # About Us page
│   ├── services.html       # Services page
│   ├── gallery.html        # Gallery page
│   ├── news.html           # News & Alerts page
│   ├── blog.html           # Insights list
│   ├── blog_detail.html    # Single article
│   ├── faq.html            # FAQ Accordion
│   └── contact.html        # Contact form
│
├── .env                    # Environment variables (Ignored by Git)
├── .env.example            # Example environment variables
├── .gitignore              # Git ignore file
├── manage.py               # Django management script
├── README.md               # This file
└── requirements.txt        # Python dependencies

🔒 Security Notes

    Never commit .env to GitHub. It contains your SECRET_KEY and database password.

    Before deploying to production (e.g., Heroku, DigitalOcean, AWS), set DEBUG=False in your .env file.

    Ensure you run python manage.py collectstatic before production deployment.

👨‍💻 Author & License

Developed as a premium white-label commercial template for finance companies.

Contact: For customizations, bug fixes, or new features, reach out to the developer.

(© 2026 Random Technology Solutions. All rights reserved.)