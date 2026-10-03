def goal_based_agent(temperature, goal=12, max_iters=10):

    iterations = 0

    while temperature != goal and iterations < max_iters:

        temperature -= 1
        iterations += 1

    if temperature == goal:
        return "Success"

    return "Failure"


print(goal_based_agent(20))