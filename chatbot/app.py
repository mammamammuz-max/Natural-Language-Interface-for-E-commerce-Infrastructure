from flask import Flask, request, jsonify
from flask_cors import CORS
from brain import agent_executor

app = Flask(__name__)
CORS(app)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_input = data.get("message")
    try:
        response = agent_executor.invoke({"input": user_input})
        return jsonify({"reply": response["output"]})
    except Exception as e:
        return jsonify({"reply": f"Thinking Error: {str(e)}"})

if __name__ == '__main__':
    print("--- Server Starting on http://127.0.0.1:5000 ---")
    app.run(port=5000, debug=True)