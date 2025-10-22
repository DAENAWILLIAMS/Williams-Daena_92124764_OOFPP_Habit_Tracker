from habit_tracker import HabitTracker
import analytics

print("\n----------------------------------------------------\n\nWelcome to your Habit Tracker!")

def main():
    """
    Entry point for the Habit Tracker Command Line Interface app.
    Provides an interactive menu for users to manage their habits.
    """
    tracker = HabitTracker()
    tracker.load_from_file()

    while True:
        print("\nPlease select an option below from the main menu:\n")
        print("1. Add Habit")
        print("2. Delete Habit")
        print("3. Complete Habit")
        print("4. List Habits")
        print("5. Analyze Habits")
        print("6. Exit")
        choice = input("\nSelect an option: ")

        # Main menu option handling
        # Each branch corresponds to a specific user action

        # Add Habit
        if choice == '1':
            name = input("\nEnter the name of your new habit: ").title()
            confirmation1 = input(f"\nIs this the habit that you want to create? ----- {name}\nEnter 'Y' for yes or 'N' for no: ")
            if confirmation1.lower() != "y":
                print("Your habit will not be added. Redirecting to the main menu.")
                continue

            periodicity = input("How often will you complete this habit?\nEnter 'daily' or 'weekly': ").title()
            if periodicity not in ('Daily', 'Weekly'):
                print("Invalid frequency entered. Redirecting to the main menu.")
                continue

            confirmation2 = input(f"\nYour new habit, {name}, should be done {periodicity}. Is this correct?\nEnter 'Y' for yes or 'N' for no: ")
            if confirmation2.lower() != "y":
                print("Your habit will not be added. Redirecting to the main menu.")
                continue

            tracker.add_habit(name, periodicity)
            print(f"Your new {periodicity} habit named '{name}' was added to your habit tracker.")
            tracker.save_to_file()

        # Delete Habit
        elif choice == '2':
            habits = tracker.list_habits()
            if not habits:
                print("You currently have no habits to delete.")
                continue

            print("\nHere is a list of your existing habits:")
            for habit in habits: 
                print(f"{habit.name.title()} ({habit.periodicity.title()})")

            name = input("\nEnter the habit you would like to delete: ").title()
            confirmation = input(f"\nAre you sure you want to delete the habit '{name}'?\nEnter 'Y' for yes or 'N' for no: ")
            if confirmation.lower() != "y":
                print("Your habit will not be deleted. Redirecting to the main menu.")
                continue

            if tracker.remove_habit(name):
                print(f"Habit '{name}' was successfully removed.")
                tracker.save_to_file()
            else:
                print(f"No habit named '{name}' was found.")

        # Complete Habit
        elif choice == '3':
            habits = tracker.list_habits()
            if not habits:
                print("You currently have no habits to complete.")
                continue

            print("\nHere is a list of your existing habits:")
            for habit in habits: 
                print(f"{habit.name.title()} ({habit.periodicity.title()})")

            name = input("Enter habit name to mark complete: ").title()

            habit_names = [habit.name for habit in habits]
            if name not in habit_names:
                print(f"No habit named '{name}' exists. Redirecting to the main menu.")
                continue
            
            confirmation = input(f"\nThe habit you want to complete is '{name}'.\nIs this correct? Enter 'Y' for yes or 'N' for no: ")
            if confirmation.lower() != "y":
                print("Your habit will not be marked as completed. Redirecting to the main menu.")
                continue

            tracker.complete_task(name.title())
            print(f"Your habit named '{name.title()}' was marked as completed.")
            tracker.save_to_file()

        # List Habits
        elif choice == '4':
            habits = tracker.list_habits()
            if not habits:
                #No habits created
                print("You currently have no habits.")
            else:
                print("\nYour current habits are:")
                #Habits sorted by periodicity then by name in alphabetical order
                for habit in sorted(habits, key=lambda h: (h.periodicity.title(), h.name.title())):
                    print(f"{habit.name.title()} ({habit.periodicity.title()})")

        # Analyze Habits
        elif choice == '5':
            print("\n=== Habit Analysis ===")

            all_habits = analytics.list_habits(tracker)
            if not all_habits:
                #No habits created
                print("No habits found to analyse.")
                continue
        
            print(f"\nAll Habits ({len(all_habits)} total):")
            #Streak for each habit outputed along with periodicity
            for habit in all_habits:
                streak = habit.get_streak()
                period_text = "day" if habit.periodicity.lower() == "daily" else "week"
                print(f"  - {habit.name} ({habit.periodicity}): {streak} {period_text} streak")
            
            daily_habits = analytics.habits_by_periodicity(tracker, 'daily')
            weekly_habits = analytics.habits_by_periodicity(tracker, 'weekly')
            
            #Habits listed by periodicity
            print(f"\nDaily Habits ({len(daily_habits)}): {daily_habits}")
            print(f"Weekly Habits ({len(weekly_habits)}): {weekly_habits}")
            
            #Habit with longest streak outtputed
            longest_streak = analytics.longest_streak(tracker)
            print(f"\nLongest Streak Overall: {longest_streak}")
            
            #Streak outputed for user inputted habit
            name = input("\nEnter habit name to check specific streak: ").title()
            streak = analytics.longest_streak_for(tracker, name)
            if streak > 0:
                print(f"Longest streak for '{name}': {streak}")
            else:
                print(f"No habit named '{name}' found.")

        # Exit
        elif choice == '6':
            tracker.save_to_file()
            print("\nYou have now exited your Habit Tracker. Thanks and goodbye!\n\n----------------------------------\n")
            break

        else:
            print("Invalid selection. You will be redirected to the main menu to choose a valid option.")

if __name__ == "__main__":
    main()
