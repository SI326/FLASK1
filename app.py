from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def bot_reply(msg):
    msg = msg.lower()
    if "hello" in msg:
        return "Hi there! How can I help you?"
    elif "your name" in msg:
        return "I'm PyBot!"
    elif "bye" in msg:
        return "Goodbye!"
    else:
        return "Sorry, I didn't understand that."

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["GET"])
def get_response():
    user_msg = request.args.get("msg")
    reply = bot_reply(user_msg)
    return jsonify(reply)

if __name__ == "__main__":
    app.run(debug=True)
