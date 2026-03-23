MAX_PREPARATION = 3
EXAM_REWARD = {
    0: 20,
    1: 50,
    2: 80,
    3: 100,
}


def clamp_preparation(level):
    return max(0, min(MAX_PREPARATION, level))


def transition(preparation_level, action):
    # Each action changes the student's preparation for the next day.
    if action == "Study":
        return clamp_preparation(preparation_level + 1), -3
    if action == "Review":
        return clamp_preparation(preparation_level), -1
    return clamp_preparation(preparation_level - 1), 2


def solve_study_mdp(days_left):
    actions = ["Study", "Review", "Rest"]
    values = {
        0: {
            preparation_level: EXAM_REWARD[preparation_level]
            for preparation_level in range(MAX_PREPARATION + 1)
        }
    }
    policy = {}

    for days in range(1, days_left + 1):
        values[days] = {}
        policy[days] = {}

        for preparation_level in range(MAX_PREPARATION + 1):
            best_action = None
            best_value = float("-inf")

            for action in actions:
                next_level, immediate_reward = transition(preparation_level, action)
                total_value = immediate_reward + values[days - 1][next_level]

                if total_value > best_value:
                    best_value = total_value
                    best_action = action

            values[days][preparation_level] = best_value
            policy[days][preparation_level] = best_action

    return values, policy


def get_int_input(prompt, minimum_value, maximum_value):
    while True:
        raw_value = input(prompt).strip()
        try:
            value = int(raw_value)
        except ValueError:
            print("Please enter a whole number.")
            continue

        if minimum_value <= value <= maximum_value:
            return value

        print(f"Please enter a number from {minimum_value} to {maximum_value}.")


def show_preparation_scale():
    print("Preparation level guide:")
    print("0 = Not prepared")
    print("1 = Slightly prepared")
    print("2 = Ready")
    print("3 = Very ready")


def main():
    print("Study Planner MDP Demo")
    days_left = get_int_input("Days before the exam (1 to 5): ", 1, 5)
    show_preparation_scale()
    preparation_level = get_int_input("Current preparation level (0 to 3): ", 0, 3)

    values, policy = solve_study_mdp(days_left)

    print("\nRecommended plan:")
    current_level = preparation_level
    for days in range(days_left, 0, -1):
        action = policy[days][current_level]
        next_level, _ = transition(current_level, action)
        print(
            f"With {days} day(s) left and preparation level {current_level}, "
            f"the best action is: {action}"
        )
        current_level = next_level

    print(f"\nExpected final score value: {values[days_left][preparation_level]}")


if __name__ == "__main__":
    main()
