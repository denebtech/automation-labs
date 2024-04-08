from utils import response_message


class TestResponseMessage():
    def test_success_message(self):
        assert response_message([201]) == "Issues successfully created"
        assert response_message([201, 201, 201]) == "Issues successfully created"


    def test_error_message_single_code(self):
        assert response_message([400]) == "Issues created with errors"
        assert response_message([500]) == "Issues created with errors"


    def test_error_message_multi_codes(self):
        assert response_message([201, 400, 201]) == "Issues created with errors"
        assert response_message([201, 500, 201]) == "Issues created with errors"
        assert response_message([201, 201, 400]) == "Issues created with errors"
        assert response_message([201, 201, 500]) == "Issues created with errors"
