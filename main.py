import logging
import smtplib
from os.path import dirname, abspath

path = dirname(abapath(_file_))
recipientsPath = f'{path}/recipients.json '
configPath = f'{path}/config.ini'
storesPath = f'{path}/stores.json'
productsPath = f'{path}/products.json'
client = smtplib.SMTP('localhost')

logging.basicConfig(filename='loggingPath,'
                             format='%(asctime)s - %(message)s',
                             level=loggin.Info)

server = smtplib.SMTP('gpustocker2021@gmail.com')

msg = MIMEMultipart()
msg['From'] = 'gpustocker2021@gmail.com'
msg['To'] = recipientsPath
msg['Subject'] = "Gpu Alert"
Message = "There are GPUs available!!!"

password = "BennyButcher2020"
server.login(msg['From'], msg['To'], msg.as.sting())

print("Message is sent from" + msg['From'] + " to " + msg['To'])



