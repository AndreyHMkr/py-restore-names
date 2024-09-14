import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize("input_data, expected_data", [
    (
        [
            {
                "first_name": None,
                "last_name": "Holy",
                "full_name": "Jack Holy"
            },
            {
                "last_name": "Adams",
                "full_name": "Mike Adams"
            }
        ],
        [
            {
                "first_name": "Jack",
                "last_name": "Holy",
                "full_name": "Jack Holy"
            },
            {
                "first_name": "Mike",
                "last_name": "Adams",
                "full_name": "Mike Adams"
            }
        ]
    ),
    (
        [
            {
                "first_name": "John",
                "last_name": "Doe",
                "full_name": "John Doe"
            }
        ],
        [
            {
                "first_name": "John",
                "last_name": "Doe",
                "full_name": "John Doe"
            }
        ]
    ),
    (
        [
            {
                "last_name": "Smith",
                "full_name": "Anna Smith"
            }
        ],
        [
            {
                "first_name": "Anna",
                "last_name": "Smith",
                "full_name": "Anna Smith"
            }
        ]
    ),
    (
        [
            {
                "first_name": None,
                "last_name": "Doe",
                "full_name": "John William Doe"
            }
        ],
        [
            {
                "first_name": "John",
                "last_name": "Doe",
                "full_name": "John William Doe"
            }
        ]
    )
])
def test_restore_names(
        input_data: set,
        expected_data: set
) -> None:
    restore_names(input_data)
    assert input_data == expected_data
