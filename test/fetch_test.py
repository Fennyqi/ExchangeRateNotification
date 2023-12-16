# this tests the exchange rating fetching function...

from app.fetch import get_past_thirty_days_rates

def test_get_past_thirty_days_rates():
    data = get_past_thirty_days_rates()

    assert isinstance(data, list)
    assert len(data) == 30  # Assuming you expect exactly 30 days' worth of data
    assert isinstance(data[0], dict)

# this tests the email sending function...

from app.fetch import send_email

def test_send_email():
    assert send_email() == 202