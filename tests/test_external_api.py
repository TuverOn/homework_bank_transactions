import json
from unittest.mock import Mock, patch

from src.external_api import API_KEY, convert_to_rub


@patch("requests.get")
def test_convert_to_rub(mock_get):
    mock_response = Mock()
    mock_response.text = json.dumps({"result": 60})
    mock_get.return_value = mock_response
    assert convert_to_rub(20, "USD") == 60
    mock_get.assert_called_once_with(
        "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount=20",
        headers={"apikey": API_KEY},
    )
