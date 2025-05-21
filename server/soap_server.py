from spyne import Application, rpc, ServiceBase, Unicode
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from wsgiref.simple_server import make_server

import pika

class ColorService(ServiceBase):
    @rpc(Unicode, _returns=Unicode)
    def process_color(ctx, color):
        # forward to rabbitmq exchange
        channel.basic_publish(exchange='colorExchange', routing_key=color, body=color)
        print(f"Received: {color}")
        return f"Server received: {color}"

application = Application(
    [ColorService],
    tns='spyne.examples.string',
    in_protocol=Soap11(validator='lxml'),
    out_protocol=Soap11()
)

if __name__ == '__main__':
    print("SOAP server listening on http://localhost:8000")

    """
    connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
    channel = connection.channel()

    channel.exchange_declare(exchange='colorExchange', exchange_type='direct', durable=True)
    """
    wsgi_app = WsgiApplication(application)
    server = make_server('0.0.0.0', 8000, wsgi_app)
    server.serve_forever()