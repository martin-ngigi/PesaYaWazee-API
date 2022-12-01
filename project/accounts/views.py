from django.shortcuts import render
import json
from datetime import date


# import package
import africastalking
from django.views.decorators.csrf import csrf_exempt 
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
