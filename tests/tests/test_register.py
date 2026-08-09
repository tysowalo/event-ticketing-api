def test_event_id_exists():

    event = {
        "eventId": "EVT001",
        "name": "Test User",
        "email": "test@example.com",
        "phone": "0240000000"
    }

    assert event["eventId"] == "EVT001"