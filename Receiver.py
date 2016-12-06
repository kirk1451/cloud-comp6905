from azure.servicebus import ServiceBusService, Message, Queue
from azure.storage.table import TableService, Entity
import threading
import json


def receiver():
        bus_service = ServiceBusService(
                service_namespace='comp6905',
                shared_access_key_name='RootManageSharedAccessKey',
                shared_access_key_value='rK2FMzVKvCjpad7xVSj1AB3hDimhxZq3WtEE4y28yaM=')
        table_service = TableService(account_name='comp6905kirk', account_key='H1YuP8hBxJ2PKw2hoW4Dr+DMAMvKZ/nGhstHw+87mE+OSBTb23cBxhkUvILgKOHWHA3hi3oaoohwVkp6lOXOlA==')
        while(True):
                msg = bus_service.receive_queue_message('queue1', peek_lock=False)
                msg1 = msg.body.decode("utf-8")
                print(msg1)
                parsed_json = json.loads(msg1)
    #print(parsed_json['UserId'
                task = {'PartitionKey': 'Zanko', 'RowKey': parsed_json['TransactionID'],  'UserId': parsed_json['UserId'], 'SellerId': parsed_json['SellerID'], 'ProductName': parsed_json['Product Name'], 'SalePrice': parsed_json['Sale Price'], 'TransactionDate': parsed_json['Transaction Date']}
                table_service.insert_entity('Requests', task)

threads=[]
for i in range (10):
        t =threading.Thread(target=receiver)
        threads.append(t)
        t.start()
