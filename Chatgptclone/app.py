from flask import Flask, request, render_template
import openai

app = Flask(__name__)

openai.api_key = "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"

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")
@app.route("/upload", methods=["POST"])
def prompt():
        input_string = request.form["nm"]
        
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=input_string,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )
        
        generated_text = response.choices[0].text
        
        return render_template('index.html',out= generated_text)

if __name__ == "__main__":
    app.run(debug=True)
