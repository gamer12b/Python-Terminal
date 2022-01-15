import sys
import subprocess
import os
import random
import time
import socket
import platform
import js2py
import smtplib
import email.message
import imghdr
import wget


q = open("em.dat", "r")
qq = open("ps.dat","r")
em = q.read()
ps = qq.read()
q.close()
qq.close()
path = "C:/"
os.chdir(path)
hostn = socket.gethostname()
ip = socket.gethostbyname(hostn)
print("Terminal")
print("Type in help for a list of commands")
while True:
  code = input(">>> ")
  if code == "yes":
    ss = input("Enter a word/line: ")
    for i in range(99999999):
      try:
      print(ss)
      time.sleep(0.4)
      Exception 
  if code == "help":
    print("""
    <<<Commands>>>
    1. help | Lists all commands
    2. clear | Clears terminal
    3. ip | Prints desktop name and ip
    4. curdir | Prints current path
    5. chdir | Changes directory
    6. cat | Prints out file content in terminal
    7. del | Deletes a file or folder
    8. mk | Make a file or a folder
    9. run | Runs other code, only python, java, jar
    10. email | Sends email with text/image/file
    11. wget | Downloads custom or your own files
    """)
  if code == "clear":
    os.system('cls' if os.name == 'nt' else 'clear')
  if code == "restart":
   os.chdir("/home/runner/Terminal")
   print("Restarting..")
   os.execv(sys.executable, ["python"] + sys.argv)
  if code == "ip":
    print("Local ip: "+ip)
    print("Host name: "+hostn)
  if code == "curdir":
    print("Current dir: "+path)
  if code == "chdir":
    di = input("Enter new dir: ")
    os.chdir(di)
    path = ""+di
    print("New path: "+path)
  if code == "cat":
    di = input("Enter dir to file: ")
    r = open(di, "r")
    print("File content:")
    print(r.read())
    r.close()
  if code == "del":
    di = input("Enter file/folder dir: ")
    if os.path.isfile(di):
      os.remove(di)
    else:
      os.rmdir(di)
  if code == "mk":
    d = input("Enter folder/file: ")
    if d == "file":
      na = input("Enter name and extension of file to create: ")
      c = open(na, "a")
      c.close()
    else:
      na = input("Enter folder name to create: ")
      os.mkdir(na)
  if code == "run":
    tt = input("Input language: ")
    ee = input("File dir: ")
    if tt == "js":
      sc = open(ee,"r")
      s = sc.read()
      js2py.eval_js(s)
    if tt == "python":
      os.system("python "+ee)
    if tt == "jar":
      subprocess.call(['java', '-jar', f'{ee}'])
    if tt == "java":
      subprocess.call(['java', '-java', f'{ee}'])
  if code == "ls":
    print("Current directory")
    print(os.listdir(path))
  if code == "email":
    reciever = input("Enter who to send to: ")
    subject = input("Enter subject: ")
    text = input("Enter text to send: ")
    amount = input("Enter how many times to send: ")
    filess = input("Enter a file you wanna send: ")
    photo = input("Enter a photo you wanna send: ")
    emaile = em
    password = ps
    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
      smtp.ehlo()
      smtp.starttls()
      smtp.ehlo()
      a = 0
      for i in range(int(amount)):
       a += 1
       smtp.login(emaile, password)
       subject = str(subject)
       body = str(text)
       msg = email.message.EmailMessage()
       msg["Subject"] = subject
       msg["From"] = emaile
       msg["To"] = reciever
       bd = f"""
       {body}
       Sent from {hostn} / {ip}
       """
       bd_s = str(bd)
       msg.set_content(bd)
       if not photo == "":
         with open(photo, "rb") as f:
           photo_data = f.read()
           photo_type = imghdr.what(f.name)
           photo_name = f.name
           msg.add_attachment(photo_data, maintype="image", subtype=photo_type, filename=photo_name)
       if not filess == "":
         files = f"/home/runner/Terminal/{filess}"
         with open(files, "rb") as f:
            fi_da = f.read()
            fi_na = f.name
            msg.add_attachment(fi_da, maintype="application",subtype="octet-stream",filename=fi_na)
       smtp.send_message(msg)
       print("Successfully sent "+str(a)+ " times")