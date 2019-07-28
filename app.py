from flask import Flask
import os
import socket
import torch

app = Flask(__name__)

@app.route("/")

def hello():
    try:
        x = torch.rand(5, 3)
    except RedisError:
        x = "<i>cannot connect to pytorch</i>"

    html =  "<h3>Hello {name}!</h3>" \
            "<b>Hostname:</b> {hostname}<br/>" \
            "<b>PyTorch Test:</b> {x}"

    return html.format(name=os.getenv("NAME", "PyTorchTest"), hostname=socket.gethostname(), x=x)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
