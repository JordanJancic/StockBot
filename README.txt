***Nike StockBot Stock Alert Service***
ⒸCopyright 2021 Jordan Jancic

Download the ChomeDriver executable file from here:
https://chromedriver.chromium.org/

The below files must be in the same folder for this bot to work.
	-Nike_Stock_Bot.py
	-chromedriver.exe
	-data.csv

Ensure that all Python dependencies are installed.
	-Selenium
	-smtplib
	-numpy

1. Open the enclosed data.csv file.

	- Under sender_email (column A), enter your Gmail account email.

	- Under receiver_emails (column B), enter the email(s) you wish to be alerted. If you need multiple
	  emails, simply add additional ones in the rows below.

	- Under app_password, enter your unique GMail App Password. 
	  Follow to instructions here to get yours:
	  https://support.google.com/mail/answer/185833?hl=en-GB

	- Under url, enter the URL of the Nike product you wish to be alerted for.

	- Under xpath_disabled_button, enter the XPath of the disabled size button for the size you wish
	  to be alerted for. 
	  Go to the Nike product page and locate the disabled button for the size you would like to be alerted for.
	  
	  Right click > Inspect
		
	  Ensure that the element with the "disabled" attribute is selected, then Right-click > Copy > Copy XPath.

	- Save  data.csv. (ctrl-s)

	- Close data.csv. (alt-f4)

2. Run the Python file.

NOTE: If you ever need to force-quit the scipt from within command prompt window, hit ctrl-c repeatedly until it stops.
