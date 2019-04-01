import redis
import os
import logging
from flask import Flask
app = Flask(__name__)

def hello_message():
    """hello message from Redis"""
   
    try:
   
        redis_host = os.environ['REDIS_HOST']
        redis_port = int(os.environ['REDIS_PORT'])
        redis_password = os.environ['REDIS_ROOT_PASSWORD']

        r = redis.StrictRedis(host=redis_host, port=redis_port, 
                              password=redis_password, decode_responses=True)
   
        # Write message to Redis. Demo only
        r.set("msg:hello", "Hello, class CIS 4360! Welcome to Redis!")

        # Read message from Redis. Demo only
        msg = r.get("msg:hello")
        logging.info("message from redis: " + msg)
        return msg
   
    except Exception as e:
        logging.error(e)

@app.route('/')
def hello():
    hello = hello_message()
    return "<H3> %s </H3>" % hello

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')