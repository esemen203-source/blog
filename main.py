from flask import Flask
import random

app = Flask(__name__)

facts = [
    "Меня зовут Семён.",
    "Я играю в гта5.",
]

@app.route("/")
def hello_world():
    return random.choice(facts)


app.run(debug=True)
