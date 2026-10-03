
def execute_action(action):
    try:
        if action == "cool":
            return {"status": "success", "message": "Cooling started"}

        elif action == "idle":
            return {"status": "success", "message": "Agent is idle"}

        else:
            raise ValueError("Invalid action")

    except ValueError as e:
        return {"status": "error", "error": str(e)}


# Test the actions
actions = ["cool", "idle", "heat"]

for action in actions:
    result = execute_action(action)
    print(result)
