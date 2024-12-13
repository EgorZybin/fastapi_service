import json
from models.schemas import RequestBody
import pika
from config import RABBITMQ_HOST, QUEUE_NAME
from fastapi import APIRouter

router = APIRouter()


@router.post("/browse")
async def browse(request: RequestBody):
    # Подключение к RabbitMQ
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=RABBITMQ_HOST))
    channel = connection.channel()

    # Обеспечиваем создание очереди, если она еще не существует
    channel.queue_declare(queue=QUEUE_NAME)

    # Отправка URL в очередь
    message = json.dumps({"url": request.url})
    channel.basic_publish(exchange='', routing_key=QUEUE_NAME, body=message)

    # Закрытие соединения
    connection.close()

    return {"message": "Request has been added to the queue"}


@router.get("/")
async def root():
    return {"message": "Hello World"}
