from datetime import datetime, timedelta
import random

def suggest_slot(user_name):
    base_time = datetime.now().replace(hour=9, minute=0)  # Start from 9 AM
    available_slots = [base_time + timedelta(minutes=30 * i) for i in range(16)]
    return random.choice(available_slots).strftime("%Y-%m-%d %H:%M")
