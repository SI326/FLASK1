from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def bot_reply(msg):
    msg = msg.lower()
    if "hello" in msg:
        return "Hi there! How can I help you?"
    elif "your name" or "name" in msg:
        return "I'm PyBot!"
    elif "bye" in msg:
        return "Goodbye!"
    elif "how are you" in msg:
        return "I'm fine, thank you!"
    elif "how are you doing" in msg:
        return "I'm fine, thank you!"
    elif "what is your name" in msg:
        return "I'm PyBot!"
    if "your name" in msg or "what is your name" in msg or "name" in msg:
        return "I'm PyBot, your virtual assistant!"
    elif "bye" in msg or "goodbye" in msg or "see you" in msg:
        return "Goodbye! Take care!"
    elif "how are you" in msg or "how are you doing" in msg:
        return "I'm doing great, thanks for asking!"
    elif "what's up" in msg or "how's it going" in msg:
        return "All systems running smoothly!"
    elif "hello" in msg or "hi" in msg or "hey" in msg:
        return "Hello there! How can I assist you today?"
    elif "what can you do" in msg or "help me" in msg or "features" in msg:
        return "I can answer your questions, give info, and help with tasks. Ask me anything!"
    elif "tell me a joke" in msg or "make me laugh" in msg:
        return "Why did the computer show up late to work? It had a hard drive!"
    elif "time" in msg or "current time" in msg:
        from datetime import datetime
        return f"The current time is {datetime.now().strftime('%I:%M %p')}."
    elif "date" in msg or "today's date" in msg:
        from datetime import datetime
        return f"Today's date is {datetime.now().strftime('%B %d, %Y')}."
    elif "thank you" in msg or "thanks" in msg:
        return "You're welcome!"
    elif "who made you" in msg or "who created you" in msg:
        return "I was created by developers using Python and a touch of AI magic!"
    elif "brith day" in msg or "brithday" in msg:
        return " now it self "
    elif msg != "":
        return "I'm not sure I understand. Can you say it differently?"
    elif msg == "":
        return "Please type something so I can respond."



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
