import os

from flask import Flask, render_template, jsonify, request
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)

channels_list = [{"name": "channel1",
                  "massages": [{"author": "ania",
                                "text": "hello",
                                "time": "21:00:00"}]}]


@app.route("/")
def index():
    return render_template("login.html")

@app.route("/channels")
def channels():
    return render_template("channels.html", channels=channels_list)

@app.route("/new_channel")
def new_channel():
    return render_template("new_channel.html", channels_list=channels_list, num=len(channels_list))

@socketio.on("channel_append")
def channel_append(data):
    name = data["name"]
    new_c = {"name": name, "massages": []}
    channels_list.append(new_c)
    emit("channels_new", channels_list, broadcast=True)

@app.route("/channel/<string:channel_name>")
def channel_review(channel_name):
    massages = ""
    for channel in channels_list:
        if (channel_name == channel["name"]):
            massages = channel["massages"]
    return render_template("channel.html", massages=massages, name=channel_name)

@socketio.on("add_massage")
def add_massage(data):
    text = data["text"]
    author = data["author"]
    time = data["time"]
    channel_name = data["channel"]
    new_m = {"author": author, "text": text, "time": time, "channel_name": channel_name}
    b = 0
    for channel in channels_list:
        if (channel_name == channel["name"]):
            if(len(channel["massages"]) > 99):
                for i in range(0, 99):
                    channel["massages"][i] = channel["massages"][i+1]
                del channel["massages"][99]
                b = 1
            channel["massages"].append(new_m)
    data = {"new_m": new_m, "b": b}
    emit("new_massage", data, broadcast=True)
