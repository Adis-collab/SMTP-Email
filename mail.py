import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os

# Email details
sender_email = "adityaswami2114@gmail.com"
receiver_email = "adityaswami714@gmail.com"
password = "zpib hqkd xolk vqzw"
subject = "Subject of the Email"
body = "This is the body of the email."

# Create message object
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = subject

# Attach the body with the msg instance
msg.attach(MIMEText(body, 'plain'))

# File attachment path
filename = "1.jpg"
filepath = "/Users/adi/Desktop/1.jpg"

# Open the file to be sent
with open(filepath, "rb") as attachment:
    # Instance of MIMEBase and named as p
    part = MIMEBase('application', 'octet-stream')

    # To change the payload into encoded form
    part.set_payload(attachment.read())

# Encode into base64
encoders.encode_base64(part)

# Add header to the attachment
part.add_header('Content-Disposition', f"attachment; filename= {filename}")

# Attach the instance 'part' to the message
msg.attach(part)

# Create SMTP session for sending the mail
server = smtplib.SMTP('smtp.gmail.com', 587)  # Use SMTP with Gmail
server.starttls()  # Enable security
server.login(sender_email, password)  # Login with email and password
text = msg.as_string()  # Convert message to string format
server.sendmail(sender_email, receiver_email, text)  # Send the email
server.quit()

print("Email sent successfully!")



