import docx
from datetime import datetime
import sqlite3

def fill_invitation(template_path, output_path, invitee_data):
    try:
        doc = docx.Document(template_path)
        
        for paragraph in doc.paragraphs:
            for key, value in invitee_data.items():
                if key in paragraph.text:
                    for run in paragraph.runs:
                        run.text = run.text.replace(key, value)
        
        doc.save(output_path)
        print(f"Invitation saved as {output_path}")  # Use index 1 for first_name
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def retrieve_invitee_data_from_database():
    # Connect to your database
    conn = sqlite3.connect('invitee_database.db')
    cursor = conn.cursor()
    
    # Fetch invitee data from the database
    cursor.execute('SELECT * FROM invitees')
    invitee_data_list = cursor.fetchall()

    # Close the database connection
    conn.close()

    return invitee_data_list

if __name__ == "__main__":
    template_path = 'template.docx'

    invitee_data_list = retrieve_invitee_data_from_database()

    # print(invitee_data_list)
    def custom_date_format(date):
        day = date.day
        if 4 <= day <= 20 or 24 <= day <= 30:
            suffix = "th"
        else:
            suffix = ["st", "nd", "rd"][day % 10 - 1]

        formatted_date = date.strftime(f"%d{suffix} %b, %Y")
        return formatted_date

    # Get today's date
    today_date = datetime.now()

    # Format today's date
    formatted_date = custom_date_format(today_date)

    for invitee_data in invitee_data_list:
        # Create a unique output path for each invitation
        output_path = f"invitation_for_{invitee_data[2]}_{invitee_data[3]}.docx"  # Use first_name and last_name
        # Convert the tuple to a dictionary for easier key-value access
        invitee_dict = {
            '[Date]':formatted_date,
            '[Salutation]': invitee_data[1],
            '[Recipient Name]': invitee_data[2],
            '[Recipient Last Name]': invitee_data[3],
            '[Recipients Job Title]': invitee_data[4],
            '[Company Name]':'Bamba Co',
            '[Company Address]':'1 Bamba Dr',
            '[City, State, ZIP Code]':'NB, NJ, 12345',
            '[Event/Reason]':'Annual Christmas Party 2023',
            '[Event Date]':'25th December, 2023',
            '[Event Location]':'The Hyatt',
            '[Additional Information or Message]':'As we gather to celebrate the joyous holiday season, we have some exciting activities and surprises in store for you! Our Christmas party promises to be a memorable event filled with laughter, delicious food, and plenty of holiday cheer.\n\nDon\'t forget to wear your favorite festive attire, and we encourage you to bring your holiday spirit. Whether it\'s sharing your favorite holiday story, participating in our annual gift exchange, or simply enjoying the company of friends and colleagues, this event is all about spreading joy and building lasting memories.\n\nWe also have a special visit from Santa Claus scheduled for the little ones, so be sure to bring your children along for an unforgettable experience.\n\nPlease RSVP by [RSVP Deadline] so that we can make the necessary arrangements to ensure everyone has a fantastic time. If you have any special dietary requirements or preferences, please let us know in advance.\n\nWe look forward to celebrating the holiday season with you and your loved ones. See you at the Christmas party!',
            '[RSVP Deadline]':'1st December, 2023',
            '[Your Name]':'Anurag',
            '[Your Job Title]':'CEO',
            '[Your Company]':'Bamba Co',
            '[Your Contact Information]':'abamba@bamba.com'
        }
        fill_invitation(template_path, output_path, invitee_dict)
