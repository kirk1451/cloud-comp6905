#!/usr/bin/env python2
#eange this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
from azure.servicebus import ServiceBusService, Message, Queue
import threading


def sender():
        bus_service = ServiceBusService(
        service_namespace='comp6905',
        shared_access_key_name='RootManageSharedAccessKey',
        shared_access_key_value='rK2FMzVKvCjpad7xVSj1AB3hDimhxZq3WtEE4y28yaM=')
        x = 0
        while(True):
                msg1 = bus_service.receive_queue_message('numbers', peek_lock=False)
#    print (msg1.body.decode("utf-8"))
                msg2 = msg1.body.decode("utf-8")
                msg3 = str(int(msg2) + 501)

                msg4 = Message(msg3.encode('utf-8'))
                bus_service.send_queue_message('numbers', msg4)
                premessage = '{"TransactionID":"'+ msg2+'","UserId":"A1","SellerID":"S1","Product Name":"Financial Trap","Sale Price":"1000000","Transaction Date":"2016-11-01T13:19:42.963Z"}'
 #   print(premessage)
                preMbytes = premessage.encode('utf-8')
                msg = Message(preMbytes )
                x = x+1
                #print(x)
                bus_service.send_queue_message('queue1', msg)

threads =[]
for i in range(10):
        t = threading.Thread(target=sender)
        threads.append(t)
        t.start()
