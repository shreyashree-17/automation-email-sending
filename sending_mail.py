import smtplib
import pandas as pd
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import asyncio

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
        
        server.sendmail(sender_email, data['email'], msg.as_string())
        print(f"Email sent to {data['name']}")
    
    server.quit()

async def main():
    contacts = pd.read_csv('Book1.csv') #file name

    smtp_server = 'smtp.gmail.com'
    port = 587  
    sender_email = 'shreyaashree.17@gmail.com' #change email
    password = 'evfg rwzq ikus xkyj' #password

    email_data = []
    for index, contact in contacts.iterrows():
        attachment_link = contact['AttachmentLink']
        
        if pd.isna(attachment_link) or attachment_link.strip() == "":
            print(f"Email not sent to {contact['Name']} - No attachment link")
            continue
        
        email_data.append({
            'name': contact['Name'],
            'email': contact['Email'],
            'subject': f'Collaborating with {contact["Company"]} for Antaragni \'24',
            'body': f"""<html>
                <head></head>
                <body>
                    <p style="font-family: Arial; font-size: 14px;">
                        Dear {contact['Name']},<br><br>
                        I hope this email finds you well.<br><br>
                        We wanted to approach your company, {contact['Company']} to collaborate with us for Antaragni ‘24, the annual cultural festival of IIT Kanpur, happening in October. Antaragni attracts participants from over 350+ colleges across India and has a footfall of 1.4+ lakhs. The four-day festival features competitions, professional shows, musical performances, DJ nights, fashion shows, and Indian folk dances, drawing significant media attention and a large audience.<br><br>
                        This collaboration could be a great opportunity for your company to connect with a vibrant and diverse audience and gain significant brand visibility. We have crafted various sponsorship packages and are open to customizing them to meet your marketing goals.<br><br>
                        As a sponsor of Antaragni 2024, {contact['Company']} stands to benefit from:<br><br>
                        - Prominent logo placement on event promotional materials, signage, and our official mobile app<br>
                        - Recognition in press releases and media coverage<br>
                        - Exclusive access to our diverse audience and networking events<br>
                        - Opportunity to distribute promotional materials or merchandise to event attendees<br><br>
                        Please refer to the attached sponsorship proposal for detailed information about the sponsorship.<br>
                        <a href="{attachment_link}">Sponsorship Proposal</a><br><br>
                        We would be delighted to discuss these sponsorship opportunities further and explore how our collaboration can be mutually beneficial. Please feel free to reach out to schedule a meeting or a phone call at your convenience.<br><br>
                        Thank you for your time and consideration.<br><br>
                        Warm Regards,<br><br>
                        Your Name<br>
                        Designation<br>
                    </p>
                </body>
                </html>"""
        })

    await send_email_async(sender_email, password, smtp_server, port, email_data)

if __name__ == "__main__":
    asyncio.run(main())
