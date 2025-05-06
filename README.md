# Flask-Question-Answering-App-
This is a simple Flask web application that provides question answering functionality using a pre-trained language model from Hugging Face. The app uses the deepset/roberta-base-squad2 model to generate answers based on a user-provided context and question.
Features

Web-based interface to input context and questions

Uses Hugging Face Transformers pipeline for question answering

Displays generated answer based on the context

Clean, embedded HTML template using Flask

Lightweight and easy to deploy locally

Technologies Used

Python 3

Flask

Transformers (Hugging Face)

HTML with Flask’s render_template_string

Project Structure

app.py or main.py (Flask application script)

How It Works

User inputs a text passage (context) and a question.

Upon form submission, the question and context are sent to the model.

The model processes the inputs and extracts the most probable answer.

The answer is displayed on the same page below the form.

How to Run

Make sure Python 3 is installed.

Install required packages:
pip install flask transformers

Save the script as app.py or main.py

Run the Flask server:
python app.py

Visit the application in your browser:
http://localhost:5000

Example Input
Context: "The Eiffel Tower is one of the most famous landmarks in Paris."
Question: "Where is the Eiffel Tower located?"
Answer: "Paris"

Future Enhancements

Add support for uploading documents as context

Enable response confidence display

Support multilingual question answering

Add user history or logging feature
