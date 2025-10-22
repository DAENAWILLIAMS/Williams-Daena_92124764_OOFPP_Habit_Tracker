"""
Analytics module for habit tracking data analysis.

This module provides functions to analyze habit data including:
- Listing all habits
- Listing habits by periodicity  
- Calculating streak statistics
"""

def list_habits(tracker):
    """Returns all habit names with periodicity in the tracker."""
    return tracker.list_habits()

def habits_by_periodicity(tracker, periodicity):
    """Returns a list of habit names filtered by periodicity.
    
    Arguments:
        tracker (HabitTracker): The habit tracker instance
        periodicity (str): 'daily' or 'weekly' (case-insensitive)
    """
    return [h.name for h in tracker.habits if h.periodicity.lower() == periodicity.lower()]

def longest_streak(tracker):
    """Returns the longest streak across all habits."""
    return max((h.get_streak() for h in tracker.habits), default=0)

def longest_streak_for(tracker, name):
    """Returns the longest streak for a specific habit by name."""
    for habit in tracker.habits:
        if habit.name == name:
            return habit.get_streak()
    return 0
    