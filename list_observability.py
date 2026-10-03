
def run_agent(temperature):
    logs = []

    logs.append("Agent started")
    logs.append(f"Observed temperature: {temperature}")

    if temperature > 100:
        action = "Cool"
    else:
        action = "Idle"

    logs.append(f"Decision made: {action}")
    logs.append(f"Action executed: {action}")
    logs.append("Agent completed")

    return logs


# Run the agent
execution_log = run_agent(120)

# Display full execution log
print("Full Execution Log:")
for step in execution_log:
    print(step)
