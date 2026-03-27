from bs4 import BeautifulSoup
from imap_tools import AND, MailBox

import os
import time
from datetime import datetime
from dotenv import load_dotenv
import configparser
import re


root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class ConfigReader:
    
    config_file = os.path.join(root, "config.ini")
    confp = configparser.ConfigParser()
    confp.read(config_file)
    load_dotenv(os.path.join(root, ".env"))
    
    def get_browser(self):
        return self.confp.get("DEFAULT", "browser")

    def get_baseurl(self):
        time.sleep(1)
        return self.confp.get("DEFAULT", "base_url")
    
    def get_chromedriver_path(self):
        return self.confp.get("DEFAULT", "chromedriver_path")

  
    email: str = (os.getenv("email") or "").strip()
    password: str = (os.getenv("password") or "").strip()
    email_user: str = (os.getenv("email_user") or "").strip()
    email_pass: str = (os.getenv("email_pass") or "").strip()


    def get_email_otp(self):
        try:
            start_time = datetime.now()
            time.sleep(5)
            format_st_time = start_time.strftime("%Y-%m-%d %H:%M:%S")
            # print(f"start_time -- {format_st_time}")
            with MailBox("imap.gmail.com").login(self.email_user, self.email_pass, "INBOX")\
                as mailbox:
                for i in range(12):   # check for ~1 minute (12 × 5 sec)
                    mails = mailbox.fetch(AND( subject="Forgot Your Password")\
                        , reverse=True, limit=1)

                    for mail in mails:

                        mail_date = mail.date.astimezone()
                        # print(mail_date)
                        format_ml_date = mail_date.strftime("%Y-%m-%d %H:%M:%S")
                        # print(f"mail date {format_ml_date}")
                        # if mail_date > start_time:
                        # print('format', type(format_ml_date) ,type( format_st_time), format_ml_date , format_st_time)
                        if format_ml_date > format_st_time:
                            print('condition satisfied')
                            email_body = mail.html
                            soup = BeautifulSoup(email_body, "html.parser")
                            text = soup.get_text()
                            match = re.search(r'OTP:\s*(\d{4,6})', text)
                            if match:
                                mailbox.flag(mail.uid, '\\Seen', True)
                                return match.group(1)
                    print("OTP not received yet, retrying...")
                    time.sleep(5)
        except Exception as e:
            print(e)
            raise Exception("OTP not received within 1 minute")











    # def get_email_otp(self):
    #     with MailBox("imap.gmail.com").login(self.email_user, self.email_pass, "INBOX") as mailbox:
    #         for mail in mailbox.fetch(AND(subject="Forgot Your Password"),reverse=True, seen=False, limit=1):
    #             email_body = mail.html      
    #             soup = BeautifulSoup(email_body, "html.parser")
    #             text = soup.get_text()
    #             match = re.search(r'OTP:\s*(\d{4,6})', text)
    #             if match:
    #                 return match.group(1)
    #             else:
    #                 raise Exception("OTP not found")

confr = ConfigReader()


# otp=confr.get_email_otp()

# print(otp)
