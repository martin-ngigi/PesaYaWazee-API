from django.shortcuts import render
import json
from datetime import date
from rest_framework.response import Response
from django.http import HttpResponse
import http.client


# import package
import africastalking
from django.views.decorators.csrf import csrf_exempt 

'''
eg: POST ->
{
    "phonenumber": "+254725482843"
}
'''

# Create your views here.
@csrf_exempt
def sms(request):
    if request.method =='POST':
        username = "wazee"    # use 'sandbox' for development in the test environment
        api_key = "a1db729e7d8ecfe06471bdae0f8b112814091b0ab6cfc37a1ab23b35cacc48db"      # use your sandbox app API key for development in the test environment
        africastalking.initialize(username, api_key)


        # Initialize a service e.g. SMS
        sms = africastalking.SMS

        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        content = body['phonenumber']
        # Use the service synchronously
        # response = sms.send("Hello Message!", [content])
        # print(response)

        # Or use it asynchronously
        def on_finish(error, response):
            if error is not None:
                raise error
            print(response)
        today = date.today()
        sms.send(f"Confrimed that you have received pension beneficiary of amount: 5,000 on {today}", [content], callback=on_finish)    


@csrf_exempt
def sendmoney(request):
    if request.method =='POST':
        conn = http.client.HTTPSConnection("api.connect.stanbicbank.co.ke")


        payload = '''{
        "originatorAccount": {
            "identification": {
            "mobileNumber": "254759459364"
            }
        },
        "requestedExecutionDate": "2022-12-01",
        "dbsReferenceId": "21899424091970",
        "txnNarrative": "TRANSACTION NARRATIVE",
        "callBackUrl": "http://client_domain.com/omnichannel/esbCallback",
        "transferTransactionInformation": {
            "instructedAmount": {
            "amount": "10.00",
            "currencyCode": "KES"
            },
            "mobileMoneyMno": {
            "name": "MPESA"
            },
            "counterparty": {
            "name": "J. Sparrow",
            "mobileNumber": "254797292290",
            "postalAddress": {
                "addressLine1": "Some street",
                "addressLine2": "99",
                "postCode": "1100 ZZ",
                "town": "Amsterdam",
                "country": "NL"
            }
            },
            "remittanceInformation": {
            "type": "UNSTRUCTURED",
            "content": "SALARY"
            },
            "endToEndIdentification": "5e1a3da132cc"
        }
        }'''

        headers = {
            'Authorization': "Bearer AAIgZTBhMzg0NzlhOTM1NTY2NWRhZjk1NzU5Mjg1YTE1MWXiodvgMlKX8Dis_RzqRqjJEDHm0Wq6LBWBjYspzE-b1dPmu1YXgHUKH0VmkvNv6YqcFp-PqcMSwiZJrZyJjVhIyrOc6TqnJ70QfJKhEb0L-HWcD7-ChDEMH6kd0YJU4IU",
            'content-type': "application/json",
            'accept': "application/json"
            }

        conn.request("POST", "/api/sandbox/mobile-payments/", payload, headers)

        res = conn.getresponse()
        data = res.read()

        print(data.decode("utf-8"))
        m_pay = json.loads(data)
        pay = json.dumps(m_pay,indent=4,sort_keys=True)
        # print(type(pay))
        print(pay)
        return HttpResponse(pay)