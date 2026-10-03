def goal_based_agent(temperature, goal=12, max_iters=10):

    state = {
        "done": False,
        "steps": 0,
        "status": "running"
    }

    while temperature != goal and state["steps"] < max_iters:

        temperature -= 1
        state["steps"] += 1

    if temperature == goal:
        state["done"] = True
        state["status"] = "success"
    else:
        state["status"] = "failure"

    return state


result = goal_based_agent(20)

print(result)