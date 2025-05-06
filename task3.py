from flask import Flask, request, render_template_string
from transformers import pipeline

app = Flask(__name__)

# Load the Question Answering model
qa_model = pipeline("question-answering", model="deepset/roberta-base-squad2")

# HTML template with a form for input and a place to display the answer
html_template = """
<!DOCTYPE html>
<html>
<head>
    <title>Question Answering</title>
</head>
<body>
    <h1>Question Answering</h1>
    <form method="POST">
        <label for="context">Enter Context:</label><br>
        <textarea name="context" rows="5" cols="50" required></textarea><br>
        <label for="question">Enter Question:</label><br>
        <input type="text" name="question" required><br>
        <input type="submit" value="Get Answer">
    </form>
    {% if answer %}
        <h2>Answer:</h2>
        <p>{{ answer }}</p>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def answer_question():
    answer = None
    if request.method == "POST":
        context = request.form.get("context", "").strip()
        question = request.form.get("question", "").strip()
        if context and question:
            result = qa_model(question=question, context=context)
            answer = result['answer']
    return render_template_string(html_template, answer=answer)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
