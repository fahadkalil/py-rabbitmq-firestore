# consumer.py

import pika, os
from dotenv import load_dotenv

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Arquivo de credenciais do Firebase
cred = credentials.Certificate('firerabbit-e3631-firebase-adminsdk-fbsvc-73105c6167.json')
firebase_admin.initialize_app(cred)

db = firestore.client()
print("Client Firestore inicializado")

load_dotenv()

# URL de conexão com o RabbitMQ definida no arquivo .env
url = os.environ.get('CLOUDAMQP_URL', 'amqp://guest:guest@localhost:5672/')
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
channel = connection.channel() # start a channel

# Cria ou faz uso da fila: 'hello'
channel.queue_declare(queue='hello', durable=True)

def callback(ch, method, properties, body):
    msg_received = body.decode()
    print(" [x] Mensagem recebida de RabbitMQ: " + str(msg_received))
    print(" Encaminhando para o Firestore")
  
    data = {        
        'timestamp': firestore.SERVER_TIMESTAMP,
        'msg': msg_received
    }

    update_time, doc_ref = db.collection('notifications').add(data)

    print(f"Documento inserido com o ID: {doc_ref.id} às {update_time}")

channel.basic_consume('hello',
                      callback,
                      auto_ack=True)

print(' [*] Aguardando mensagem de RabbitMQ. Para sair pressione CTRL+C:')
channel.start_consuming()
connection.close()