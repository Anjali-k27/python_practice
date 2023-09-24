# Write a function which will try to find out length of a string without using an inbuilt len function

def find_len(s):
    """This is a program which will help to find the length of string"""
    count = 0
    for i in s:
        if type(i) == str:
            count = count + 1
    return count

# Write a function which will be able to print an index of list element without using an index function

def find_index(l):
    """This is a program which will help to print index of list element"""
    for i in range(len(l)):
        print(f"Index of {l[i]} is {i}")

# Write a function which will be able to print an IP address of your system

import socket
def find_ip():
    """This is a program which will print IP address of your system"""
    ip = socket.gethostbyname(socket.gethostname())
    return ip

# Write a function which will shut down your system

import os
def sys_shut():
    """This function when executed, will shut down your system, Proceed with caution"""
    return os.system("shutdown /s /t 4")    # Initiate shutdown after 4 seconds

# /s - shutdown
# /r - restart
# /t 1 - timer

# Write a function which will take input as a list with any kind of numeric value and give output as multiplication

def mul_num(l):
    """This function will return product of all numeric elements of a list"""
    mul = 1
    for i in l:
        if type(i) == int or type(i) == float:
            mul = mul * i
    return mul

# Write a function which will be able to read all the mails

import imaplib, email                # Importing libraries

user = 'USER_EMAIL_ADDRESS'
password = 'USER_PASSWORD'
imap_url = 'imap.gmail.com'

def get_body(msg):                   # Function to get email content part i.e its body part
	if msg.is_multipart():
		return get_body(msg.get_payload(0))
	else:
		return msg.get_payload(None, True)

def search(key, value, con):          # Function to search for a key value pair
	result, data = con.search(None, key, '"{}"'.format(value))
	return data

def get_emails(result_bytes):          # Function to get the list of emails under this label
	msgs = []                          # all the email data are pushed inside an array
	for num in result_bytes[0].split():
		typ, data = con.fetch(num, '(RFC822)')
		msgs.append(data)

	return msgs

con = imaplib.IMAP4_SSL(imap_url)      # this is done to make SSL connection with GMAIL

con.login(user, password)              # logging the user in

con.select('Inbox')                    # calling function to check for email under this label

msgs = get_emails(search('FROM', 'MY_ANOTHER_GMAIL_ADDRESS', con))   # fetching emails from this user "a**6***@gmail.com"

# print(msgs)                           # Uncomment this to see what actually comes as data

# Finding the required content from our msgs
# User can make custom changes in this part to
# fetch the required content he / she needs

# printing them by the order they are displayed in your gmail
for msg in msgs[::-1]:
	for sent in msg:
		if type(sent) is tuple:

			content = str(sent[1], 'utf-8')           # encoding set as utf-8
			data = str(content)

			try:                                       # Handling errors related to unicodenecode
				indexstart = data.find("ltr")
				data2 = data[indexstart + 5: len(data)]
				indexend = data2.find("</div>")

				print(data2[0: indexend])               # printing the required content which we need to extract from our email i.e our body

			except UnicodeEncodeError as e:
				pass

# Write a function which will be able to send a mail to anyone

import smtplib, ssl
def send_mail():
    port = 465 # For SSL (No need to change)
    smtp_server = "smtp.gmail.com"
    sender_email = "xyz@gmail.com"      # Enter your mail address
    receiver_email = "abc@gmail.com"   # Enter receiver's mail
    password = 'fsdasfsdas'    #you will have to set app password on your google account, else you will not be able to successfully run this code
    message = """this is my message from python code"""

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

# Write a function which will be able to read a doc/word file from your system

import docx2txt
def read_doc():
    """This function will read word file from your system"""
    a = docx2txt.process('test.docx')
    return a