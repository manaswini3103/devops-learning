import json # read/write bookings to a JSON file
from datetime import datetime, timedelta # compare time values correctly (not as strings)
import os

# __file__ : Built-in Python variable, Contains path of current Python file
# os.path.abspath: Converts the file path into an absolute path and Removes any relative path confusion
# os.path.dirname: Extracts only directory and Removes filename (bookings.py), path is C:\GIT\devops-learning\Python
# os.path.join: Takes base directory and Appends "bookings.json" correctly for your OS
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_NAME = os.path.join(BASE_DIR, "bookings.json")
WORK_START = "09:00"
WORK_END = "18:00"

# ----------------- Utility Functions -----------------

# Opens bookings.json, Converts JSON → Python dictionary and Returns it
def load_data(): 
    with open(FILE_NAME, "r") as f:
        return json.load(f)

# Saves updated booking data back into JSON, indent=2 makes the file readable
def save_data(data):
    with open(FILE_NAME, "w") as f:
        json.dump(data, f, indent=2)

def to_time(t):
    return datetime.strptime(t, "%H:%M")

# calculates how many minutes are between given two time strings(start,end)
# to_time(end) - datetime object where python understands that it is time not text, the difference becomes timedelta object
# total.seconds() - the diff bet start and end converts to seconds, /60 converts seconds to minutes.
def minutes_between(start, end):
    return int((to_time(end) - to_time(start)).total_seconds() / 60)

# Automatically generates a unique ID for new record, by checking existing booking records
def generate_id(bookings):
    return max([b["id"] for b in bookings], default=0) + 1 # Finds the largest existing ID and adds 1

# ----------------- Option 1: List -----------------

def list_by_date(date):
    data = load_data() # data variable has all the bookings in form of dictionary
    #  if given date and date in bookings matches then that record/booking will be appened to meetings (list of dictionaries)
    meetings = [b for b in data["bookings"] if b["date"] == date]
    if not meetings:
        print("No meetings found.")
        return

    for m in meetings:
        print(f'ID:{m["id"]} | {m["title"]} | {m["start_time"]}-{m["end_time"]}')

# ----------------- Conflict & Slot Finder -----------------

def has_conflict(date, start, end, bookings):
    for b in bookings:
        if b["date"] == date:
            if not (end <= b["start_time"] or start >= b["end_time"]):
                return True
    return False

def find_available_slots(date, duration, bookings):
    slots = []
    day_bookings = sorted(
        [b for b in bookings if b["date"] == date], # Keeps only meetings for the selected date
        key=lambda x: x["start_time"] # Sorts meetings from earliest to latest using start time
    )

    current = WORK_START

    for b in day_bookings:
        if minutes_between(current, b["start_time"]) >= duration:
            slots.append(f"{current} - {b['start_time']}") # takes work starting time and first meeting start time from day_bookings in first iteration
            # then takes end time from first meeting and start time from second meeting and appends it to slot list
        current = b["end_time"]

    if minutes_between(current, WORK_END) >= duration:
        slots.append(f"{current} - {WORK_END}") # takes the end time of last meeting from day_bookings and work ending ending time and stores that string in slot list

    return slots

# ----------------- Option 2: Add -----------------

def add_booking():
    data = load_data() # all the bookings are stored in data
    bookings = data["bookings"] 

    title = input("Title: ")
    date = input("Date (YYYY-MM-DD): ")
    start = input("Start Time (HH:MM): ")
    end = input("End Time (HH:MM): ")

    if start < WORK_START or end > WORK_END:
        print("❌ Outside working hours (9AM - 6PM)")
        return

    duration = minutes_between(start, end)
    if duration < 15 or duration > 240:
        print("❌ Duration must be between 15 mins and 4 hours")
        return

    if has_conflict(date, start, end, bookings):
        print("❌ Time conflict detected.")
        slots = find_available_slots(date, duration, bookings)
        if slots:
            print("Available slots:")
            for s in slots:
                print(" ", s)
        else:
            print("No slots available.")
        return

    new_booking = {
        "id": generate_id(bookings),
        "title": title,
        "date": date,
        "start_time": start,
        "end_time": end
    }

    bookings.append(new_booking)
    save_data(data) # bookings and data both point to the same list in memory, once bookings get appended, the data will also be updated.
    print("✅ Booking added successfully.")

# ----------------- Option 3: Cancel -----------------

def cancel_booking():
    data = load_data()
    bookings = data["bookings"]

    for b in sorted(bookings, key=lambda x: (x["date"], x["start_time"])):
        print(f'{b["date"]} | ID:{b["id"]} | {b["title"]} | {b["start_time"]}-{b["end_time"]}')

    bid = int(input("Enter ID to cancel: "))
    # if current booking id doesn't match with given id, then add it to data["bookings"], if it matches don't add that to new booking_list
    # so data["bookings"] has the all the boookings ids except user givev booking id
    data["bookings"] = [b for b in bookings if b["id"] != bid] # this is called as List comprehension, it will implicitly adds that ids that are not matched with given id into data["bookings"]

    save_data(data) 
    print("✅ Booking cancelled.")

# ----------------- Option 4: Report -----------------
# takes all the bookings for the given date, tells how many meetings are there and duration of all those meetings
def report_by_date(date):
    data = load_data()
    meetings = [b for b in data["bookings"] if b["date"] == date]

    print(f"\nReport for {date}")
    print("-" * 30) # prints - for 30 times

    total_minutes = 0
    for m in meetings:
        duration = minutes_between(m["start_time"], m["end_time"])
        total_minutes += duration
        print(f'{m["title"]} | {m["start_time"]}-{m["end_time"]} ({duration} mins)')

    print(f"\nTotal meetings: {len(meetings)}")
    print(f"Total booked time: {total_minutes} mins")

# ----------------- Main Menu -----------------

def main():
    while True:
        print("\n1. List by date")
        print("2. Add booking")
        print("3. Cancel booking")
        print("4. Report by date")
        print("5. Exit")
        choice = input("Choose option: ")

        if choice == "1":
            list_by_date(input("Enter date (YYYY-MM-DD):"))
        elif choice == "2":
            add_booking()
        elif choice == "3":
            cancel_booking()
        elif choice == "4":
            report_by_date(input("Enter date (YYYY-MM-DD):"))
        elif choice == "5":
            break
        else:
            print("Invalid option")

if __name__ == "__main__":
    main()
