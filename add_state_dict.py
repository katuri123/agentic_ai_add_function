def goal_based_agent(temperature, goal=12, max_iters=10):

    state = {
        "done": False,
        "steps": 0
    }

    while temperature != goal and state["steps"] < max_iters:

        temperature -= 1
        state["steps"] += 1

    if temperature == goal:
        state["done"] = True
        return "Success", state

    return "Failure", state


result, state = goal_based_agent(20)

print("Result:", result)
print("State:", state)