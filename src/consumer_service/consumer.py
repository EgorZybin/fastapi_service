import pika
from selenium import webdriver
from fastapi_service.config import RABBITMQ_HOST, QUEUE_NAME, SELENIUM_HUB_URL


def consume():
    def callback(ch, method, properties, body):
        url = body.decode()
        print(f"Processing URL: {url}")

        # Настройка драйвера для подключения к Selenium Grid
        options = webdriver.ChromeOptions()
        driver = webdriver.Remote(command_executor=SELENIUM_HUB_URL, options=options)

        try:
            driver.get(url)
            print(driver.page_source)
        except Exception as e:
            print(f"Error: {e}")
        finally:
            driver.quit()

        ch.basic_ack(delivery_tag=method.delivery_tag)

    # Подключение к RabbitMQ
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=RABBITMQ_HOST))
    channel = connection.channel()
    channel.queue_declare(queue=QUEUE_NAME)
    channel.basic_consume(queue=QUEUE_NAME, on_message_callback=callback)

    print("Waiting for messages. To exit press CTRL+C")
    channel.start_consuming()


if __name__ == "__main__":
    consume()
