import uuid


def test_register_user(get_client):
    unique_email = f"{uuid.uuid4()}@example.com"

    response = get_client.post(
        "/auth/register",
        json={
            "name": "Test User",
            "email": unique_email,
            "password": "password123"
        }
    )

    assert response.status_code == 201

    data = response.json()

    assert data["name"] == "Test User"
    assert data["email"] == unique_email
    assert data["role"] == "CUSTOMER"


def test_login_success(get_client):
    email = f"{uuid.uuid4()}@example.com"

    register_response = get_client.post(
        "/auth/register",
        json={
            "name": "Login User",
            "email": email,
            "password": "password123"
        }
    )

    assert register_response.status_code == 201

    response = get_client.post(
        "/auth/login",
        data={
            "username": email,
            "password": "password123"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert "access_token" in data
    assert data["token_type"] == "bearer"


def test_login_invalid_credentials(get_client):
    email = f"{uuid.uuid4()}@example.com"

    register_response = get_client.post(
        "/auth/register",
        json={
            "name": "Wrong Password User",
            "email": email,
            "password": "password123"
        }
    )

    assert register_response.status_code == 201

    response = get_client.post(
        "/auth/login",
        data={
            "username": email,
            "password": "wrongpassword"
        }
    )

    assert response.status_code == 401
    assert response.json()["detail"] == "Invalid credentials"