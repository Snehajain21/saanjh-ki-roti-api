def test_get_plans(get_client):
    response = get_client.get("/plans/")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_create_plan_without_auth(get_client):
    response = get_client.post(
        "/plans/",
        json={
            "name": "Monthly Premium",
            "price": 2800,
            "meal_type": "LUNCH",
            "diet_types": [
                "VEG",
                "NON_VEG"
            ],
            "billing_cycle": "MONTHLY"
        }
    )

    assert response.status_code == 401