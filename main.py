import openai
from flask import Flask, request, render_template

app = Flask(__name__)
openai.api_key = "sk-"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=userText,
        temperature=0.8,
        max_tokens=1024,
        n=1,
        stop=None,
    )
    answer = response["choices"][0]["text"]
    return answer

if __name__ == "__main__":
    app.run()

