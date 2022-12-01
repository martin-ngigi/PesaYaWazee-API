import http.client
import json
from django.shortcuts import render
from datetime import date
from rest_framework.response import Response


# import package
import africastalking
from django.views.decorators.csrf import csrf_exempt 


@csrf_exempt
def sendmoney(request):
    if request.method =='GET':
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
        return Response(data=pay)