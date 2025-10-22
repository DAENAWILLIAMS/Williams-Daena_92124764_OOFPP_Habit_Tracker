from datetime import datetime

class Habit:
    """
    Represents a habit that the user wants to track.
    Attributes:
        name (str): Name of the habit.
        periodicity (str): Frequency of the habit ('daily' or 'weekly').
        creation_date (datetime): Date and time the habit was created.
        completions (list): List of datetime objects when the habit was completed.
    """
    def __init__(self, name, periodicity):
        self.name = name
        self.periodicity = periodicity
        self.creation_date = datetime.now()
        self.completions = []

    def mark_complete(self):
        """Marks the habit as completed by appending the current date and time."""
        self.completions.append(datetime.now())

    def get_streak(self):
        """
        Calculates the current streak of habit completions based on the periodicity.

        The streak is calculated by checking consecutive completions in chronological order
        and counting how many consecutive periods (days/weeks) have completions.
        
        Returns:
            int: The number of consecutive periods where the habit was completed.
        """
        if not self.completions:
            return 0
        
        # Convert to dates (without time) and remove duplicates
        completion_dates = sorted(set([c.date() for c in self.completions]))
        
        if not completion_dates:
            return 0
            
        streak = 1
        current_streak = 1
        
        for i in range(1, len(completion_dates)):
            prev_date = completion_dates[i-1]
            curr_date = completion_dates[i]
            delta = curr_date - prev_date
            
            if self.periodicity.lower() == 'daily':
                # For daily habits: consecutive days should have exactly 1 day difference
                if delta.days == 1:
                    current_streak += 1
                elif delta.days > 1:
                    # Streak broken - reset counter but continue checking for longer streaks
                    current_streak = 1
            elif self.periodicity.lower() == 'weekly':
                # For weekly habits: check if dates are in consecutive weeks
                # Using isocalendar to handle week boundaries properly
                prev_week = prev_date.isocalendar()[1]  # week number
                curr_week = curr_date.isocalendar()[1]
                prev_year = prev_date.isocalendar()[0]
                curr_year = curr_date.isocalendar()[0]
                
                # Handle year boundaries
                if curr_year == prev_year and curr_week - prev_week == 1:
                    current_streak += 1
                elif curr_year - prev_year == 1 and curr_week == 1 and prev_week == 52:
                    current_streak += 1
                else:
                    # Streak broken
                    current_streak = 1
            
            # Update the longest streak found
            if current_streak > streak:
                streak = current_streak
        
        return streak