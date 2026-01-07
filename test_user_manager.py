import pytest
from unittest.mock import patch
from user_manager import UserManager

# 1. PATCH THE CLASS WHERE IT IS USED
@patch('user_manager.PostgresDriver')
def test_get_users_flow(mock_driver_class):
    
    # 2. SETUP THE INSTANCE (The Chain)
    # The class (mock_driver_class) returns an instance when called ()
    mock_db_instance = mock_driver_class.return_value
    
    # 3. CONFIGURE THE BEHAVIOR
    # We want execute_query to return specific fake data
    mock_db_instance.execute_query.return_value = ["Alice", "Bob"]
    
    # --- ACT ---
    
    # 4. INITIALIZE MANAGER
    # Crucial: This triggers __init__, which calls PostgresDriver() and .connect()
    # Since we patched it, it uses our mock_db_instance.
    manager = UserManager("postgres://fake-url")
    
    # 5. CALL THE METHOD
    users = manager.get_all_users()
    
    # --- ASSERT ---
    
    # Check 1: Did we get the data from the mock?
    assert users == ["Alice", "Bob"]
    
    # Check 2: Did __init__ actually call connect?
    mock_db_instance.connect.assert_called_once()
    
    # Check 3: Did we run the correct SQL?
    mock_db_instance.execute_query.assert_called_once_with("SELECT * FROM users")