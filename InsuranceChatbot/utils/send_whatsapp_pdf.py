import requests

class whatsapp:
    @staticmethod
    def sendWhatsapp_pdf(phone_no):
        url = "http://api.gupshup.io/sm/api/v1/msg"

        payload = 'channel=whatsapp&source=917834811114&destination=' + phone_no + '&message={"type": "file","url": "https://www.buildquickbots.com/whatsapp/media/sample/pdf/sample01.pdf","filename": "Quotation Document"}}&src.name=KrRasaInsurance'
        print(payload)
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'apikey': 'dc4505cb443f459dc52f886f64db1e77'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))

    @staticmethod
    def sendWhatsapp_text(product_name, tariff, phone_no):
        print("inside whatsapp function" + phone_no)
        url = "http://api.gupshup.io/sm/api/v1/msg"

        message = "Your quotation: Product Name :" + product_name + "Premium : " + tariff + " Below PDF is included with your quotation for future use"
        #payload = 'channel=whatsapp&source=917834811114&destination=' + phone_no + '&message={"isHSM":"false","type": "text","text":' + message +' }}&src.name=KrRasaInsurance'
        payload = 'channel=whatsapp&source=917834811114&destination=' + phone_no + '&message= ' + message + '&src.name=KrRasaInsurance'

        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'apikey': 'dc4505cb443f459dc52f886f64db1e77'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))

    @staticmethod
    def sendWhatsapp_otp(phone_no, otp):
        print("inside whatsapp function" + phone_no)
        url = "http://api.gupshup.io/sm/api/v1/msg"

        message = "Your OTP for updating email address : " + otp
        # payload = 'channel=whatsapp&source=917834811114&destination=' + phone_no + '&message={"isHSM":"false","type": "text","text":' + message +' }}&src.name=KrRasaInsurance'
        payload = 'channel=whatsapp&source=917834811114&destination=' + phone_no + '&message= ' + message + '&src.name=KrRasaInsurance'

        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'apikey': 'dc4505cb443f459dc52f886f64db1e77'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))


# whatsapp.sendWhatsapp_pdf('919449599522')
# whatsapp.sendWhatsapp_text('918951603679')