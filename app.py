from flask import Flask, render_template, request, jsonify
from ai_parser import parse_command
from executor import execute
from database import init_db, log_history, get_history
from scheduler import schedule_task, start_scheduler
from watcher import start_watcher

app = Flask(__name__)
init_db()
start_scheduler()

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

        log_history(user_input, result)

        return jsonify({
            "success": True,
            "parsed": command,
            "result": result
        })

    except Exception as e:
        return jsonify({"success": False, "error": str(e)})


@app.route("/history")
def history():
    return jsonify(get_history())


@app.route("/schedule", methods=["POST"])
def schedule():
    data = request.json
    command = data.get("command")
    seconds = int(data.get("seconds", 60))

    schedule_task(command, seconds)

    return jsonify({"success": True})


@app.route("/watch", methods=["POST"])
def watch():
    data = request.json
    path = data.get("path")
    command = data.get("command")

    start_watcher(path, command)

    return jsonify({"success": True})


if __name__ == "__main__":
    app.run(debug=True)