import asyncio
import smtplib
import os
import pandas as pd
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

async def send_email_async(sender_email, password, smtp_server, port, email_data):
    server = smtplib.SMTP(smtp_server, port)
    server.starttls()
    server.login(sender_email, password)
    
    for data in email_data:
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = data['email']
        msg['Subject'] = data['subject']
        msg.attach(MIMEText(data['body'], 'html'))
        
        with open(data['attachment'], 'rb') as attachment:
            part = MIMEApplication(attachment.read(), Name=os.path.basename(data['attachment']))
        part['Content-Disposition'] = f'attachment; filename="{os.path.basename(data["attachment"])}"'
        msg.attach(part)
        
        server.sendmail(sender_email, data['email'], msg.as_string())
        print(f"Email sent to {data['name']}")
    
    server.quit()

async def main():
    contacts = pd.read_csv('Book1.csv') #file name

    smtp_server = 'smtp.gmail.com'
    port = 587  
    sender_email = 'shreyaashree.17@gmail.com' #change email
    password = 'evfg rwzq ikus xkyj' #password

    pdf_directory = r'C:\Users\shrey\Dropbox\PC\Desktop\Proposal' #Proposal folderfile

    email_data = []
    for index, contact in contacts.iterrows():
        email_data.append({
            'name': contact['Name'],
            'email': contact['Email'],
            'subject': f'Collaborating with {contact["Company"]} for Antaragni \'24',
            'body': f"""<html> ... </html>""", # Your HTML body here
            'attachment': os.path.join(pdf_directory, f"{contact['Company']}.pdf")
        })

    await send_email_async(sender_email, password, smtp_server, port, email_data)

if __name__ == "__main__":
    asyncio.run(main())
