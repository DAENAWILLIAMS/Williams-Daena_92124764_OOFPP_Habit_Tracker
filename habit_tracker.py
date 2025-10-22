import json
import os
from datetime import datetime
from habit import Habit

class HabitTracker:
    """
    Manages multiple habits. Allows adding, removing, completing, saving,
    and loading habits from a JSON file.

    Arguments:
        filename (str): Name of the file to save data to. Defaults to 'tracker_data.json'
    """
    def __init__(self):
        self.habits = []

    def add_habit(self, name, periodicity):
        """Adds a new habit to the tracker."""
        habit = Habit(name, periodicity)
        self.habits.append(habit)

    def remove_habit(self, name):
        """Removes a habit from the tracker by name.
        
        Arguments:
            name (str): Name of the habit to remove
            
        Returns:
            bool: True if habit was found and removed, False otherwise
        """
        for i, habit in enumerate(self.habits):
            if habit.name == name:
                del self.habits[i]
                return True  # Return success status
        return False  # Return failure status

    def complete_task(self, name):
        """Marks a habit as completed by name.
        
        Arguments:
            name (str): Name of the habit to mark complete
            
        Returns:
            bool: True if habit was found and marked complete, False otherwise
        """
        for habit in self.habits:
            if habit.name == name:
                habit.mark_complete()
                return True
        return False

    def list_habits(self):
        """Return a list of Habit objects."""
        return self.habits

    def save_to_file(self, filename='tracker_data.json'):
        """Saves the current list of habits to a JSON file in the same folder as the script."""
        # Gets the directory where the current script is located to ensure  the file is saved in the same folder regardless of working directory
        script_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_dir, filename)
        
        # Writes habit data to JSON format
        with open(file_path, 'w') as f:
            json.dump([
                {
                    'name': h.name,
                    'periodicity': h.periodicity,
                    'creation_date': h.creation_date.isoformat(),
                    'completions': [c.isoformat() for c in h.completions]
                } for h in self.habits
            ], f)
        
        print(f"Data saved to: {file_path}")  # Tells user where to find .json file

    def load_from_file(self, filename='tracker_data.json'):
        """Loads habits from a JSON file in the same folder as the script if it exists.

        Arguments:
        filename (str): Name of the file to load data from. Defaults to 'tracker_data.json'
        """
        try:
            # Get the directory where the current script is located
            script_dir = os.path.dirname(os.path.abspath(__file__))
            file_path = os.path.join(script_dir, filename)
            
            with open(file_path, 'r') as f:
                tracker_data = json.load(f)
                for item in tracker_data:
                    habit = Habit(item['name'], item['periodicity'])
                    habit.creation_date = datetime.fromisoformat(item['creation_date'])
                    habit.completions = [datetime.fromisoformat(c) for c in item['completions']]
                    self.habits.append(habit)
        except FileNotFoundError:
            pass  # File doesn't exist, in the case of new user or accidental .json file deletion