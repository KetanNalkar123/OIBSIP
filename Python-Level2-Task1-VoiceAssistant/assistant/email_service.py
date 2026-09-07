"""
Email service using SMTP.
"""

import smtplib

from email.message import EmailMessage

from config.config import Config


class EmailService:
    """Send emails through an SMTP server."""

    def __init__(self):

        self.email_address = (
            Config.EMAIL_ADDRESS.strip()
        )

        self.email_password = (
            Config.EMAIL_PASSWORD.strip()
            .replace(" ", "")
        )

        self.smtp_server = (
            Config.EMAIL_SMTP_SERVER
        )

        self.smtp_port = (
            Config.EMAIL_SMTP_PORT
        )

    # ==================================================
    # Configuration Check
    # ==================================================

    def is_configured(self):

        return bool(
            self.email_address
            and self.email_password
            and self.smtp_server
            and self.smtp_port
        )

    # ==================================================
    # Send Email
    # ==================================================

    def send_email(
        self,
        recipient,
        subject,
        body
    ):

        if not self.is_configured():

            return (
                False,
                "The email service is not configured."
            )

        if not recipient:

            return (
                False,
                "The recipient email address is missing."
            )

        if not subject:

            return (
                False,
                "The email subject is missing."
            )

        if not body:

            return (
                False,
                "The email message is missing."
            )

        try:

            message = EmailMessage()

            message["From"] = (
                self.email_address
            )

            message["To"] = (
                recipient
            )

            message["Subject"] = (
                subject
            )

            message.set_content(
                body
            )

            with smtplib.SMTP(
                self.smtp_server,
                self.smtp_port,
                timeout=20
            ) as server:

                server.ehlo()

                server.starttls()

                server.ehlo()

                server.login(
                    self.email_address,
                    self.email_password
                )

                server.send_message(
                    message
                )

            return (
                True,
                "Email sent successfully."
            )

        except smtplib.SMTPAuthenticationError:

            return (
                False,
                "Email authentication failed. "
                "Please check your Gmail address "
                "and App Password."
            )

        except smtplib.SMTPException as error:

            print(
                f"SMTP error: {error}"
            )

            return (
                False,
                "The email could not be sent because "
                "of an SMTP error."
            )

        except OSError as error:

            print(
                f"Email connection error: {error}"
            )

            return (
                False,
                "I could not connect to the email server."
            )

        except Exception as error:

            print(
                f"Email error: {error}"
            )

            return (
                False,
                "An unexpected error occurred while "
                "sending the email."
            )