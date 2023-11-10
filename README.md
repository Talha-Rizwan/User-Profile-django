# Django Custom User Management Project

This Django project provides a custom user management system with extended user profile fields, email-based authentication, and various user actions such as signup, login, profile editing, password change, and account deactivation.

## Installation

1. Clone the repository:

   ```bash
   git clone <repository-url>
   ```

2. Create a virtual environment:

   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

4. Install project dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Apply migrations:

   ```bash
   python manage.py migrate
   ```

6. Create a superuser (admin) account:

   ```bash
   python manage.py createsuperuser
   ```

7. Run the development server:

   ```bash
   python manage.py runserver
   ```

8. Access the application in your browser at `http://127.0.0.1:8000/`.

## User Actions

### Homepage

- Click on "Login" to access the login page.
- Click on "Signup" to access the signup page.

### Signup Page

- Enter email, password, and confirm password.
- After signup, the user's status is set to "Unverified."

### Login Page

- Enter email and password to log in.

### Greetings Page

- After successful login/signup, the user is redirected to a greetings page.
- Options available:
  - Logout: Logs the user out.
  - Edit Profile: Allows the user to edit their profile details.

### Edit Profile Page

- User can edit phone number, address, gender, and password.
- Status and email cannot be edited from the profile.
- Separate form for changing the password.
- "Deactivate Account" button to deactivate the user's account.

## Pylint

Before submitting the project, run pylint on the entire project:

```bash
pylint .
```

## Additional Notes

- The admin can update the user's status to "Active."
- A deactivated user cannot log in.

Feel free to explore the functionalities of the custom user management system. If you encounter any issues or have suggestions, please let us know by opening an issue in the repository.
