# Personal Portfolio
https://jubby-portifolio.vercel.app/

A responsive personal portfolio website built with Flask to showcase my background, skills, projects, and interests in technology, business, and fintech.

The application also includes a contact system that stores visitor messages in PostgreSQL and sends transactional emails using Brevo.

## Features

- Responsive portfolio website
- Home, About, Projects, and Contact pages
- Custom 404 page
- Project showcase with technology badges and external links
- Contact form with server-side validation
- Contact messages stored in PostgreSQL
- Email notification sent to the portfolio owner
- Confirmation email sent to the visitor
- Visitor email used as the reply-to address
- Flash messages for form feedback
- Environment-based configuration
- Production deployment on Vercel

## Tech Stack

### Backend
- Python
- Flask
- Psycopg
- psycopg-pool
- python-dotenv

### Frontend
- HTML5
- CSS3
- JavaScript
- Bootstrap 5

### Database
- PostgreSQL
- Neon

### Email
- Brevo Transactional Email API
- Brevo Python SDK

### Deployment
- Vercel
- GitHub

## Contact System

The contact form allows visitors to submit their name, email address, and message.

When a form is submitted:

1. The submitted data is validated.
2. The message is stored in PostgreSQL.
3. A notification email is sent to the portfolio owner.
4. A confirmation email is sent to the visitor.
5. The visitor's email is used as the reply-to address.
6. A success or warning message is displayed on the website.

## Database

Contact messages are stored in PostgreSQL using the following table:

```sql
CREATE TABLE messages (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(255) NOT NULL,
    message TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## Project Structure

```text
homepage/
├── app.py
├── requirements.txt
├── .env
├── .gitignore
│
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── about.html
│   ├── projects.html
│   ├── contact.html
│   └── 404.html
│
└── public/
    ├── styles.css
    ├── script.js
    └── images/
        └── profile.JPG
```

## Environment Variables

Create a `.env` file in the project root:

```text
DATABASE_URL=your_neon_database_url
SECRET_KEY=your_flask_secret_key
BREVO_API_KEY=your_brevo_api_key
BREVO_SENDER_EMAIL=your_verified_brevo_email
NOTIFICATION_EMAIL=your_notification_email
```

Never commit the `.env` file or any API keys, database credentials, or secret keys to GitHub.

## Local Development

### Clone the repository

```bash
git clone https://github.com/jubbyshonhayi/homepage.git
cd homepage
```

### Create a virtual environment

```bash
python -m venv venv
```

### Activate the virtual environment on Windows

```powershell
venv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Configure environment variables

Create a `.env` file in the project root and add the required environment variables.

### Run the application

```bash
flask run
```

The application will be available at:

```text
http://127.0.0.1:5000
```

## Deployment

The application is deployed on Vercel and connected to the GitHub repository.

Production environment variables are configured in Vercel rather than stored in the repository.

Pushing changes to the `main` branch can trigger a new production deployment.

## Security

Sensitive credentials and environment-specific configuration are stored using environment variables.

The following should never be committed to the repository:

- `.env`
- API keys
- Database connection strings
- Secret keys

## Future Improvements

- Background email processing
- Additional portfolio analytics
- More detailed project case studies
- Additional interactive features

## License

This project is a personal portfolio website.