import secrets

from redirector.redirector import create_redirection
from redirector.redirector import get_unique_token

def test_url_redirection():
    result = create_redirection({}, {})
    assert result["statusCode"] == 200

def test_generate_unique_key(mocker):
    mocker.patch.object(secrets, 'token_urlsafe')
    secrets.token_urlsafe.return_value = "XXXX"
    assert get_unique_token(10) == "XXXX"
    secrets.token_urlsafe.assert_called_once_with(10)