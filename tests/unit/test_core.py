from PY_PACKAGE_NAME.core import get_message


def test_get_message() -> None:
    # Arrange
    expected_message = "hello"

    # Act
    message = get_message()

    # Assert
    assert expected_message == message
