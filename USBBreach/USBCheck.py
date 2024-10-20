# from infi.devicemanager import DeviceManager
# from twilio.rest import Client
# from tkinter import *
from tkinter import messagebox
import socket
import time

def send_whatsapp_message(message):
    account_sid = ''  # Twilio Account SID
    auth_token = ''    # Twilio Auth Token
    from_whatsapp_number = 'whatsapp:'  # Twilio WhatsApp-enabled number 
    to_whatsapp_number = 'whatsapp:'     # Replace with the recipient's WhatsApp number

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=message,
        from_=from_whatsapp_number,
        to=to_whatsapp_number
    )

    print(f"Message sent: {message.sid}")

hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)
dm = DeviceManager()
dm.root.rescan()
disks = dm.disk_drives
names = [disk.friendly_name for disk in disks]
#allowed_devices = names
max_lenght = len(names) #number of drives in disks
print(max_lenght)

x = 1
while x != 100:
    time.sleep(5)
    dm.root.rescan()
    disks = dm.disk_drives
    names = [disk.friendly_name for disk in disks]
    lenght_check = len(names)
    if lenght_check > max_lenght:
        send_whatsapp_message(f"Drive added or USB detected on: {ip} Hostname: {hostname} Current Drives : {disks}")
        # print(f"Drive added or USB detected on: {ip} Hostname: {hostname} Current Drives : {disks}")
        time.sleep(10)

    if lenght_check < max_lenght:
        send_whatsapp_message(f"Drive removed or drive disconnected on: {ip} Hostname: {hostname} Current Drives : {disks}")
        #print(f"Drive removed or drive disconnected on: {ip} Hostname: {hostname} Current Drives : {disks}")
        time.sleep(10)