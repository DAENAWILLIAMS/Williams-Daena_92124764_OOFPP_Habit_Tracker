import unittest
import os
import sys
from datetime import datetime, timedelta

# Add current directory to Python path to ensure imports work
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from habit import Habit
from habit_tracker import HabitTracker

class TestHabitTracker(unittest.TestCase):
    
    def setUp(self):
        """Set up a fresh tracker for each test"""
        self.tracker = HabitTracker()
    
    def test_add_habit(self):
        """Test adding a habit to the tracker"""
        print("Running test_add_habit...")
        self.tracker.add_habit("Exercise", "Daily")
        self.assertEqual(len(self.tracker.habits), 1)
        self.assertEqual(self.tracker.habits[0].name, "Exercise")
        self.assertEqual(self.tracker.habits[0].periodicity, "Daily")
        print("test_add_habit passed")

    def test_remove_habit(self):
        """Test removing a habit from the tracker"""
        print("Running test_remove_habit...")
        self.tracker.add_habit("Read", "Weekly")
        result = self.tracker.remove_habit("Read")
        self.assertTrue(result)
        self.assertEqual(len(self.tracker.habits), 0)
        print("test_remove_habit passed")

    def test_mark_complete(self):
        """Test marking a habit as completed"""
        print("Running test_mark_complete...")
        self.tracker.add_habit("Meditate", "Daily")
        self.tracker.complete_task("Meditate")
        self.assertEqual(len(self.tracker.habits[0].completions), 1)
        print("test_mark_complete passed")

    def test_daily_streak(self):
        """Test daily streak calculation"""
        print("Running test_daily_streak...")
        habit = Habit("Walk", "Daily")
        base_date = datetime(2025, 10, 10)
        habit.completions = [base_date, base_date + timedelta(days=1)]
        self.assertEqual(habit.get_streak(), 2)
        print("test_daily_streak passed")

    def test_weekly_streak(self):
        """Test weekly streak calculation"""
        print("Running test_weekly_streak...")
        habit = Habit("Meal Prep", "Weekly")
        base_date = datetime(2025, 10, 3)
        habit.completions = [base_date, base_date + timedelta(weeks=1)]
        self.assertEqual(habit.get_streak(), 2)
        print("test_weekly_streak passed")

if __name__ == '__main__':
    print("Starting unit tests...")
    unittest.main(verbosity=2)
    print("Tests completed!")