import pytest
from app.restore_names import restore_names


def test_restore_name_which_is_not_filled_in():
    users = [
        {
            "last_name": "Adams",
            "full_name": "Mike Adams",
        }
    ]
    restore_names(users)
    assert users == [
        {
            "first_name": "Mike",
            "last_name": "Adams",
            "full_name": "Mike Adams",
        }
    ]


def test_restore_none_name():
    users = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]
    test_return = restore_names(users)
    assert test_return is None
    assert users == [
        {
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]


def test_dont_restore_different_name():
    users = [
        {
            "first_name": "Jim",
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]
    restore_names(users)
    assert users == [
        {
            "first_name": "Jim",
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]


def test_raises_error_when_no_names_in_dict():
    users = []
    restore_names(users)
    assert users == []


def test_restore_mixed_names():
    users = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
        {
            "last_name": "Adams",
            "full_name": "Mike Adams",
        },
        {
            "first_name": "Jim",
            "last_name": "Adams",
            "full_name": "Jack Holy",
        }
    ]
    restore_names(users)
    assert users == [
        {
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
        {
            "first_name": "Mike",
            "last_name": "Adams",
            "full_name": "Mike Adams",
        },
        {
            "first_name": "Jim",
            "last_name": "Adams",
            "full_name": "Jack Holy",
        }
    ]