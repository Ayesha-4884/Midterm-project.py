class GoalSetter:
    def __init__(self):
        self.goals = {}

    def add_goal(self, goal_name, target_date):
        self.goals[goal_name] = {"target_date": target_date, "achieved": False}
        print(f"Goal added: {goal_name} by {target_date}")

    def view_goals(self):
        if not self.goals:
            print("No goals added.")
        else:
            for goal, details in self.goals.items():
                status = "Achieved" if details["achieved"] else "Not Achieved"
                print(f"Goal: {goal}, Target Date: {details['target_date']}, Status: {status}")

    def mark_achieved(self, goal_name):
        if goal_name in self.goals:
            self.goals[goal_name]["achieved"] = True
            print(f"Goal marked as achieved: {goal_name}")
        else:
            print("Goal not found.")

    def delete_goal(self, goal_name):
        if goal_name in self.goals:
            del self.goals[goal_name]
            print(f"Goal deleted: {goal_name}")
        else:
            print("Goal not found.")

def main():
    goal_setter = GoalSetter()

    while True:
        print("\nGoal Setter")
        print("1. Add Goal")
        print("2. View Goals")
        print("3. Mark Goal as Achieved")
        print("4. Delete Goal")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            goal_name = input("Enter goal name: ")
            target_date = input("Enter target date (YYYY-MM-DD): ")
            goal_setter.add_goal(goal_name, target_date)
        elif choice == "2":
            goal_setter.view_goals()
        elif choice == "3":
            goal_name = input("Enter goal name to mark as achieved: ")
            goal_setter.mark_achieved(goal_name)
        elif choice == "4":
            goal_name = input("Enter goal name to delete: ")
            goal_setter.delete_goal(goal_name)
        elif choice == "5":
            print("Exiting program.")
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
