import smtplib
import time
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class EmailReminder:
    def __init__(self):
        self.reminders = []

    def display_menu(self):
        print("\nAutomated Email Reminder")
        print("1. Add a new reminder")
        print("2. View all reminders")
        print("3. Send scheduled reminders")
        print("4. Exit")

    def add_reminder(self):
        email = input("Enter the recipient's email: ")
        subject = input("Enter the subject of the reminder: ")
        message = input("Enter the reminder message: ")
        date_str = input("Enter date and time for reminder (YYYY-MM-DD HH:MM): ")

        try:
            reminder_time = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
            self.reminders.append({
                "email": email,
                "subject": subject,
                "message": message,
                "time": reminder_time
            })
            print("Reminder added successfully!")
        except ValueError:
            print("Invalid date/time format. Please try again.")

    def view_reminders(self):
        if self.reminders:
            print("\nScheduled Reminders:")
            for idx, reminder in enumerate(self.reminders):
                print(f"{idx + 1}. To: {reminder['email']} | Subject: {reminder['subject']} | Time: {reminder['time']}")
        else:
            print("\nNo reminders scheduled.")

    def send_email(self, email, subject, message):
        sender_email = "your_email@gmail.com"
        sender_password = "your_password"
        
        try:
            msg = MIMEMultipart()
            msg['From'] = sender_email
            msg['To'] = email
            msg['Subject'] = subject
            msg.attach(MIMEText(message, 'plain'))

            with smtplib.SMTP('smtp.gmail.com', 587) as server:
                server.starttls()
                server.login(sender_email, sender_password)
                server.sendmail(sender_email, email, msg.as_string())
                print(f"Email sent to {email} with subject '{subject}'")
        except Exception as e:
            print(f"Failed to send email. Error: {e}")

    def check_and_send_reminders(self):
        print("Checking for reminders to send...")
        current_time = datetime.now()
        for reminder in self.reminders[:]:
            if current_time >= reminder['time']:
                self.send_email(reminder['email'], reminder['subject'], reminder['message'])
                self.reminders.remove(reminder)

    def start(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")

            if choice == '1':
                self.add_reminder()
            elif choice == '2':
                self.view_reminders()
            elif choice == '3':
                self.check_and_send_reminders()
            elif choice == '4':
                print("Exiting Automated Email Reminder. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    reminder_app = EmailReminder()
    reminder_app.start()
