import pytest


# 3 tests to test DB (Insertion, Update and Deletion)

@pytest.fixture(autouse=True,scope='module')
def before_each_test():
    print("\nOpen DB\n")

@pytest.fixture(autouse=True, scope='module')
def after_each_test():
    yield
    print("\nClose DB\n")

def test_insertion_operation():
    print("\nInserting...\n")
    print("Inserted Successfully\n")
    
def test_update_operation():
    print("\nUpdating...\n")
    print("Updated Successfully\n")


def test_deletion_operation():
    print("\nDeleting...\n")
    print("Deleted Successfully\n")
        
        