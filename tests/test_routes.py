import pytest
from app import create_app, db
from app.models import User

@pytest.fixture
def client():
    """Create a test client for the app."""
    app = create_app('testing')
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Create the database tables
        yield client
        with app.app_context():
            db.drop_all()  # Drop the database tables after tests

@pytest.fixture
def add_user(client):
    """Create a test user."""
    user = User(username='testuser', password_hash='hashedpassword')  # Use a hash function in production
    db.session.add(user)
    db.session.commit()
    return user

def test_home_page(client):
    """Test the home page route."""
    response = client.get('/')
    assert response.status_code == 200
    assert b'Welcome to BDT&VR RFID Solution' in response.data

def test_about_page(client):
    """Test the about page route."""
    response = client.get('/about')
    assert response.status_code == 200
    assert b'About' in response.data

def test_contact_page(client):
    """Test the contact page route."""
    response = client.get('/contact')
    assert response.status_code == 200
    assert b'Contact' in response.data

def test_dashboard_page(client, add_user):
    """Test the dashboard page route."""
    response = client.get('/dashboard')
    assert response.status_code == 200
    assert b'Dashboard' in response.data

def test_invalid_route(client):
    """Test an invalid route."""
    response = client.get('/invalid')
    assert response.status_code == 404
    assert b'Not found' in response.data

def test_login_page(client):
    """Test the login page route (assuming you have a login route)."""
    response = client.get('/login')
    assert response.status_code == 200
    assert b'Login' in response.data

def test_register_page(client):
    """Test the registration page route (assuming you have a registration route)."""
    response = client.get('/register')
    assert response.status_code == 200
    assert b'Register' in response.data

def test_login_functionality(client, add_user):
    """Test the login functionality."""
    response = client.post('/login', data={'username': 'testuser', 'password': 'wrongpassword'})
    assert response.status_code == 200
    assert b'Invalid credentials' in response.data

    response = client.post('/login', data={'username': 'testuser', 'password': 'hashedpassword'})
    assert response.status_code == 302  # Redirect after successful login
    assert response.location == 'http://localhost/dashboard'  # Adjust based on your redirect

def test_logout_functionality(client, add_user):
    """Test the logout functionality."""
    client.post('/login', data={'username': 'testuser', 'password': 'hashedpassword'})
    response = client.get('/logout')
    assert response.status_code == 302  # Redirect after logout
    assert response.location == 'http://localhost/'  # Adjust based on your redirect
