from redirector.redirector import create_redirection

def test_url_redirection():
    result = create_redirection({}, {})
    assert result["statusCode"] == 200