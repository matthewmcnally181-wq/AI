from flask import Flask, render_template, request, jsonify
from ai_parser import parse_command
from executor import execute

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/run", methods=["POST"])
def run_command():
    data = request.json
    user_input = data.get("command")

    try:
        command = parse_command(user_input)
        result = execute(command)

        return jsonify({
            "success": True,
            "parsed": command,
            "result": result
        })

    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        })


if __name__ == "__main__":
    app.run(debug=True)