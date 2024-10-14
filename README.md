# **Django Article Platform**
This Django web application allows users to register as either writers or clients. Writers can create and manage articles, while clients can read articles. The app integrates with PayPal for backend payments and includes email verification for user registration.

## Features
    User Registration: Allows users to sign up as either writers or clients.

    Email Verification: Verifies user emails upon registration.

    Article Creation and Management: Writers can create, edit, and delete articles.

    Article Viewing: Clients can view and read articles.

    PayPal Integration: Clients can make payments via PayPal for accessing premium content.

### Requirements
    Python 3.x

    Django 3.x

    django-allauth (for email verification)

    django-paypal (for PayPal integration)

### Installation 
    Create a virtual environment:
    python3 -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`

    Install the dependencies:
    pip install -r requirements.txt

    Set up the database:
    python manage.py migrate
    Create a superuser:
    python manage.py createsuperuser

    Run the development server:
    python manage.py runserver

## Configuration
### Email Verification:

    Update the EMAIL_BACKEND, EMAIL_HOST, EMAIL_PORT, EMAIL_USE_TLS, EMAIL_HOST_USER, and EMAIL_HOST_PASSWORD in the settings.py file.

### PayPal Integration:

    Update the PAYPAL_RECEIVER_EMAIL and PAYPAL_TEST settings in the settings.py file.

### Usage

    Register as a Writer or Client:

    Sign up on the registration page and verify your email.

    Create Articles (for Writers):

    Log in as a writer and create articles from the dashboard.

    Read Articles (for Clients):

    Log in as a client and browse articles. Make payments for premium content via PayPal.

### Contributing

    Fork the repository.

    Create a new branch: git checkout -b my-feature-branch.

    Make your changes and commit them: git commit -m 'Add my new feature'.

    Push to the branch: git push origin my-feature-branch.

    Submit a pull request.

License
This project is licensed under the MIT License. See the LICENSE file for more details.

Contact
For any questions or inquiries, please contact yourname@example.com.