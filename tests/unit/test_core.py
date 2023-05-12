from YOUR_PACKAGE_NAME.core import get_message


def test_get_message():
  # Arrange
  expected_message = "hello"
  
  # Act
  message = get_message()
  
  # Assert
  assert expected_message == message
