
def agent():
    logs = []

    for step in range(1, 3):
        print("Step:", step)

        if step == 1:
            action = "Observe"
        else:
            action = "Act"

        logs.append(action)
        print("Action:", action)

    return logs


result = agent()
print("Full Log:", result)
