import pytest
from src import strings as st

@pytest.mark.JAN_RELEASE
def test_to_upper():
    assert st.to_upper("welcome") == "WELCOME"

def test_to_lower():
    assert st.to_lower("WELCOME") == "welcome"
    assert st.to_lower("wel___COME") == "wel___come"

@pytest.mark.JAN_RELEASE
def test_capetalize():
    assert st.capetalize("hello my team") == "Hello my team"

def test_ends_with():
    assert st.ends_with("hello my team","team") == True
    assert st.ends_with("hello my team","tears") == False
    

