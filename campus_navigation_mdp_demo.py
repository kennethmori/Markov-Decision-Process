DISCOUNT = 0.9
ITERATIONS = 25


# Each building lists the next buildings it can move to.
TRANSITIONS = {
    "USM Main Gate": {
        "Go to College of Education": "USM College of Education",
        "Go to Administration Building": "USM Administration Building",
    },
    "USM College of Education": {
        "Go to Main Gate": "USM Main Gate",
        "Go to College of Arts and Sciences": "USM College of Arts and Sciences",
        "Go to College of Engineering & Information Technology": "USM College of Engineering & Information Technology",
    },
    "USM Administration Building": {
        "Go to Main Gate": "USM Main Gate",
        "Go to Admission and Records Office": "USM Admission and Records Office",
        "Go to College of Arts and Sciences": "USM College of Arts and Sciences",
    },
    "USM College of Arts and Sciences": {
        "Go to College of Education": "USM College of Education",
        "Go to Administration Building": "USM Administration Building",
        "Go to College of Engineering & Information Technology": "USM College of Engineering & Information Technology",
    },
    "USM College of Engineering & Information Technology": {
        "Go to College of Education": "USM College of Education",
        "Go to College of Arts and Sciences": "USM College of Arts and Sciences",
        "Go to College of Agriculture": "USM College of Agriculture",
    },
    "USM College of Agriculture": {
        "Go to College of Engineering & Information Technology": "USM College of Engineering & Information Technology",
        "Go to Admission and Records Office": "USM Admission and Records Office",
    },
    "USM Admission and Records Office": {},
}


def build_rewards(goal_state):
    rewards = {}
    for state, actions in TRANSITIONS.items():
        rewards[state] = {}
        for action, next_state in actions.items():
            # Moving has a small penalty so the policy prefers shorter paths.
            rewards[state][action] = 20 if next_state == goal_state else -1
    return rewards


def value_iteration(goal_state):
    rewards = build_rewards(goal_state)
    values = {state: 0.0 for state in TRANSITIONS}
    policy = {}
    values[goal_state] = 20.0

    for _ in range(ITERATIONS):
        new_values = values.copy()
        for state, actions in TRANSITIONS.items():
            if state == goal_state or not actions:
                continue

            best_action = None
            best_value = float("-inf")

            for action, next_state in actions.items():
                action_value = rewards[state][action] + DISCOUNT * values[next_state]
                if action_value > best_value:
                    best_value = action_value
                    best_action = action

            new_values[state] = best_value
            policy[state] = best_action

        values = new_values

    return values, policy


def simulate_path(start_state, goal_state, policy):
    path = [start_state]
    current_state = start_state
    visited = {start_state}

    while current_state != goal_state:
        action = policy.get(current_state)
        if action is None:
            break

        next_state = TRANSITIONS[current_state][action]
        path.append(next_state)
        if next_state in visited:
            break
        visited.add(next_state)
        current_state = next_state

    return path


def choose_state(prompt):
    states = list(TRANSITIONS.keys())
    print(prompt)
    for index, state in enumerate(states, start=1):
        print(f"{index}. {state}")

    while True:
        raw_value = input("Enter number: ").strip()
        try:
            choice = int(raw_value)
        except ValueError:
            print("Please enter a whole number from the list.")
            continue

        if 1 <= choice <= len(states):
            return states[choice - 1]

        print("Please choose a valid number from the list.")


def main():
    print("Campus Navigation MDP Demo")
    start_state = choose_state("Choose the starting building:")
    goal_state = choose_state("Choose the destination building:")

    if start_state == goal_state:
        print("\nYou are already at the destination.")
        return

    _, policy = value_iteration(goal_state)
    path = simulate_path(start_state, goal_state, policy)

    print("\nBest path based on the MDP policy:")
    print(" -> ".join(path))

    if path[-1] == goal_state:
        print(f"Recommended next action: {policy[start_state]}")
    else:
        print("No complete path was found with the current setup.")


if __name__ == "__main__":
    main()
