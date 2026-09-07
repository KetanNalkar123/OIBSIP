"""
Secure Password Generator Logic
OASIS INFOBYTE - Python Programming Internship
Task 3: Advanced Random Password Generator
"""

import secrets
import string


# Character sets
LOWERCASE = string.ascii_lowercase
UPPERCASE = string.ascii_uppercase
DIGITS = string.digits
SPECIAL_CHARACTERS = string.punctuation

# Characters that can easily be confused
AMBIGUOUS_CHARACTERS = "Il1O0o"


def remove_ambiguous_characters(characters):
    """
    Remove visually ambiguous characters from a character set.
    """

    return "".join(
        character
        for character in characters
        if character not in AMBIGUOUS_CHARACTERS
    )


def generate_password(
    length,
    use_uppercase=True,
    use_lowercase=True,
    use_digits=True,
    use_special=True,
    exclude_ambiguous=False
):
    """
    Generate a cryptographically secure random password.

    The function guarantees at least one character from every
    selected character type.
    """

    if length < 4:
        raise ValueError(
            "Password length must be at least 4 characters."
        )

    selected_sets = []

    if use_uppercase:
        characters = UPPERCASE

        if exclude_ambiguous:
            characters = remove_ambiguous_characters(
                characters
            )

        selected_sets.append(characters)

    if use_lowercase:
        characters = LOWERCASE

        if exclude_ambiguous:
            characters = remove_ambiguous_characters(
                characters
            )

        selected_sets.append(characters)

    if use_digits:
        characters = DIGITS

        if exclude_ambiguous:
            characters = remove_ambiguous_characters(
                characters
            )

        selected_sets.append(characters)

    if use_special:
        characters = SPECIAL_CHARACTERS

        if exclude_ambiguous:
            characters = remove_ambiguous_characters(
                characters
            )

        selected_sets.append(characters)

    if not selected_sets:
        raise ValueError(
            "Please select at least one character type."
        )

    if length < len(selected_sets):
        raise ValueError(
            f"Password length must be at least "
            f"{len(selected_sets)} characters when "
            f"all selected character types are required."
        )

    # Combine all selected character sets
    all_characters = "".join(selected_sets)

    # Guarantee one character from each selected category
    password_characters = [
        secrets.choice(character_set)
        for character_set in selected_sets
    ]

    # Fill remaining positions securely
    remaining_length = length - len(password_characters)

    for _ in range(remaining_length):
        password_characters.append(
            secrets.choice(all_characters)
        )

    # Securely shuffle the generated password
    secrets.SystemRandom().shuffle(
        password_characters
    )

    return "".join(password_characters)


def calculate_password_strength(
    password,
    selected_types_count=0
):
    """
    Calculate password strength.

    Returns:
        tuple: (strength_name, score, description)
    """

    if not password:
        return (
            "No Password",
            0,
            "Generate a password to see its strength."
        )

    length = len(password)

    has_lowercase = any(
        character in LOWERCASE
        for character in password
    )

    has_uppercase = any(
        character in UPPERCASE
        for character in password
    )

    has_digit = any(
        character in DIGITS
        for character in password
    )

    has_special = any(
        character in SPECIAL_CHARACTERS
        for character in password
    )

    score = 0

    # Length score
    if length >= 8:
        score += 1

    if length >= 12:
        score += 1

    if length >= 16:
        score += 1

    # Character diversity score
    character_types = sum(
        [
            has_lowercase,
            has_uppercase,
            has_digit,
            has_special
        ]
    )

    if character_types >= 2:
        score += 1

    if character_types >= 3:
        score += 1

    if character_types == 4:
        score += 1

    # Strength classification
    if length < 8 or score <= 2:
        strength = "Weak"
        description = "Use a longer password with more character types."

    elif score <= 4:
        strength = "Medium"
        description = "Good password, but increasing length can improve it."

    else:
        strength = "Strong"
        description = "Strong password with good length and character diversity."

    return strength, score, description