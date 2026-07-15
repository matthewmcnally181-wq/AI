def execute(command, dry_run=False):
    action = command.get("action")
    params = command.get("parameters", {})

    if dry_run:
        return f"[DRY RUN] Would execute: {action} with {params}"

    if action == "organize_files":
        return organize_files(params["source"], params["destination"])

    elif action == "create_folder":
        return create_folder(params["destination"])

    elif action == "move_file":
        return move_file(params["source"], params["destination"])

    else:
        return "Unknown action"
