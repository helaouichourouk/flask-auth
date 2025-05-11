# Flask OAuth Authentication with GitHub

This is a simple Flask application that demonstrates how to implement OAuth authentication with GitHub using the `requests_oauthlib` library. The application allows users to log in with their GitHub account and view their GitHub username on a dashboard page.

## Features

- **Login via GitHub**: The app allows users to authenticate using their GitHub credentials.
- **Dashboard**: After authentication, users are redirected to a dashboard displaying their GitHub username.
- **Logout**: Users can log out and clear their session.

## Requirements

- Python 3.6+
- Flask
- requests_oauthlib
- python-dotenv

## Setup Instructions

### 1. Clone the repository

Clone this repository to your local machine:

```bash
git clone https://github.com/helaouichourouk/flask-auth.git
cd flask-auth
```

### 2. Create a virtual environment

Create a virtual environment to manage the project's dependencies:

```bash
python3 -m venv venv
```

Activate the virtual environment:

On macOS/Linux:

```bash
source venv/bin/activate
```

On Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

### 4. Set up environment variables

Create a `.env` file in the root directory of the project and add the following environment variables:

```bash
GITHUB_CLIENT_ID=your_github_client_id
GITHUB_CLIENT_SECRET=your_github_client_secret
SECRET_KEY=your_secret_key
```

- `GITHUB_CLIENT_ID` and `GITHUB_CLIENT_SECRET`: Obtain these by registering your application in your [GitHub developer settings](https://github.com/settings/developers).
- `SECRET_KEY`: A secret key used for securely signing Flask session cookies. You can generate one using Python:

```python
import os
print(os.urandom(24))
```

### 5. Run the application

Start the Flask development server:

```bash
flask run
```

By default, the app will run on `http://127.0.0.1:5000`.

### 6. Access the application

Navigate to `http://127.0.0.1:5000` in your browser.

- Click the "Login with GitHub" button to authenticate.
- After logging in, you will be redirected to the dashboard, where your GitHub username will be displayed.
- You can log out by clicking the "Logout" button.

## File Structure

```bash
flask-auth/
├── app.py               # Main Flask application
├── .env                 # Environment variables (GITHUB_CLIENT_ID, GITHUB_CLIENT_SECRET, SECRET_KEY)
├── requirements.txt     # Project dependencies
├── templates/
│   ├── home.html        # Home page template
│   └── dashboard.html   # Dashboard page template
├── venv/                # Virtual environment
└── README.md            # This file
```

## Dependencies

- **Flask**: A lightweight WSGI web application framework.
- **requests_oauthlib**: A library to handle OAuth authentication flows.
- **python-dotenv**: A library to load environment variables from a `.env` file.

Install all dependencies from the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

## Troubleshooting

### 1. MismatchingStateError

If you encounter the `MismatchingStateError` (CSRF warning), make sure that the state parameter in the URL and the session match. Here are a few steps to resolve it:

- Check that the Flask session is properly configured with a `SECRET_KEY`.
- Ensure the callback URL in your GitHub OAuth app matches the one used in your app.

### 2. Invalid or expired token

If you get an invalid or expired token error, try clearing your cookies or logging out of the app manually and then logging back in.

## License

This project is licensed under the MIT License.
