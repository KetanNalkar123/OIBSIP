"""
SQLite Database Management
OASIS INFOBYTE - Python Programming Internship
Task 2: Advanced BMI Calculator
"""

import os
import sqlite3
from datetime import datetime


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
DB_PATH = os.path.join(DATA_DIR, "bmi_history.db")


def get_connection():
    """Create and return a connection to the SQLite database."""
    os.makedirs(DATA_DIR, exist_ok=True)
    return sqlite3.connect(DB_PATH)


def initialize_database():
    """Create the BMI records table if it does not exist."""

    try:
        with get_connection() as connection:
            connection.execute(
                """
                CREATE TABLE IF NOT EXISTS bmi_records (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_name TEXT NOT NULL,
                    weight REAL NOT NULL,
                    height REAL NOT NULL,
                    bmi REAL NOT NULL,
                    category TEXT NOT NULL,
                    recorded_at TEXT NOT NULL
                )
                """
            )

            connection.commit()

    except sqlite3.Error as error:
        raise RuntimeError(
            f"Unable to initialize database: {error}"
        )


def add_record(user_name, weight, height, bmi, category):
    """Save a BMI calculation record."""

    try:
        recorded_at = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )

        with get_connection() as connection:
            connection.execute(
                """
                INSERT INTO bmi_records
                (user_name, weight, height, bmi, category, recorded_at)
                VALUES (?, ?, ?, ?, ?, ?)
                """,
                (
                    user_name,
                    weight,
                    height,
                    bmi,
                    category,
                    recorded_at
                )
            )

            connection.commit()

    except sqlite3.Error as error:
        raise RuntimeError(
            f"Unable to save BMI record: {error}"
        )


def get_records(user_name=None):
    """Return BMI records."""

    try:
        with get_connection() as connection:

            if user_name:
                cursor = connection.execute(
                    """
                    SELECT id, user_name, weight, height,
                           bmi, category, recorded_at
                    FROM bmi_records
                    WHERE user_name = ?
                    ORDER BY id DESC
                    """,
                    (user_name,)
                )
            else:
                cursor = connection.execute(
                    """
                    SELECT id, user_name, weight, height,
                           bmi, category, recorded_at
                    FROM bmi_records
                    ORDER BY id DESC
                    """
                )

            return cursor.fetchall()

    except sqlite3.Error as error:
        raise RuntimeError(
            f"Unable to retrieve BMI records: {error}"
        )


def get_user_names():
    """Return all unique user names."""

    try:
        with get_connection() as connection:
            cursor = connection.execute(
                """
                SELECT DISTINCT user_name
                FROM bmi_records
                ORDER BY user_name
                """
            )

            return [row[0] for row in cursor.fetchall()]

    except sqlite3.Error as error:
        raise RuntimeError(
            f"Unable to retrieve users: {error}"
        )


def delete_record(record_id):
    """Delete a BMI record by ID."""

    try:
        with get_connection() as connection:
            connection.execute(
                """
                DELETE FROM bmi_records
                WHERE id = ?
                """,
                (record_id,)
            )

            connection.commit()

    except sqlite3.Error as error:
        raise RuntimeError(
            f"Unable to delete BMI record: {error}"
        )


def clear_all_records():
    """Delete all BMI records."""

    try:
        with get_connection() as connection:
            connection.execute(
                "DELETE FROM bmi_records"
            )

            connection.commit()

    except sqlite3.Error as error:
        raise RuntimeError(
            f"Unable to clear BMI records: {error}"
        )