from flask import Flask, render_template, request, jsonify
import openai
import os
import PyPDF2

app = Flask(__name__)

# ನಿಮ್ಮ OpenAI API key ಇಲ್ಲಿ ಹಾಕಿ
openai.api_key = "YOUR_API_KEY"

# Home page
@app.route("/")
def home():
    return render_template("index.html")

# Chatbot route
@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_input}]
    )

    reply = response['choices'][0]['message']['content']
    return jsonify({"reply": reply})

# Resume Upload & Analysis
@app.route("/upload", methods=["POST"])
def upload_file():
    file = request.files["file"]

    if file.filename.endswith(".pdf"):
        pdf_reader = PyPDF2.PdfReader(file)
        text = ""

        for page in pdf_reader.pages:
            text += page.extract_text()

        # AI analysis
        prompt = f"Analyze this resume and give improvement suggestions:\n{text}"

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )

        result = response['choices'][0]['message']['content']
        return jsonify({"analysis": result})

    return jsonify({"analysis": "Upload PDF only"})
    

if __name__ == "__main__":
    app.run(debug=True)