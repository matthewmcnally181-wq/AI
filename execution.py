from actions import organize_files, create_folder, move_file

def execute(command):
    action = command.get("action")
    params = command.get("parameters", {})

    if action == "organize_files":
        return organize_files(params["source"], params["destination"])

    elif action == "create_folder":
        return create_folder(params["destination"])

    elif action == "move_file":
        return move_file(params["source"], params["destination"])

    else:
        return "Unknown action"