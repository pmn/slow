from flask import Flask, request
import random
import time


app = Flask(__name__)

@app.route('/')
def home():
    try:
        delay = int(request.args.get('delay', 3))
    except:
        delay = 3
    time.sleep(delay)
    return "Your random number is {}".format(random.randint(0, 1000)) 