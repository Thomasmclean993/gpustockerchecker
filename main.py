import logging
import requests
import smtplib
from os.path import dirname, abspath
from email.message import EmailMessage

response = requests.get('https://api.nvidia.partners/edge/product/search?page=1&limit=9&locale=en-us&category=GPU&gpu=RTX%203080&manufacturer=NVIDIA&manufacturer_filter=NVIDIA~1,ASUS~1,EVGA~3,GIGABYTE~2,MSI~1,PNY~0,ZOTAC~0')

products = response.json()['searchedProducts']['productDetails']
email = f''
# what important? ANS= product title and prd status

for product in products:
    for retailers in product['retailers']:
        print(retailers)
        if retailers['stock']>=0:
            email +=f"{retailers['productTitle']} is available at {retailers['retailerName']}"
print(email)
# client = smtplib.SMTP('localhost')
# server = smtplib.SMTP('gpustocker2021@gmail.com')
#
# msg = MIMEMultipart()
# msg['From'] = 'gpustocker2021@gmail.com'
# msg['To'] = 'gpustocker2021@gmail.com'
# msg['Subject'] = "Gpu Alert"
# Message = "There are GPUs available!!!"
#
# password = "BennyButcher2020"
# server.login(msg['From'], password, true)
#
# print("Message is sent from" + msg['From'] + " to " + msg['To'])



