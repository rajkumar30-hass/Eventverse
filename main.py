"""
EVENTVERSE - Event and Festival Announcement System
Author : Rajkumar Kirar
Reg. No: 26BCE11128
Course : Python Essential (2026-27)
"""

import json
from datetime import datetime

FILE_NAME = "events.json"


# ---------- File handling ----------
def load_events():
    try:
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_events(events):
    with open(FILE_NAME, "w") as f:
        json.dump(events, f, indent=4)


# ---------- Helper functions ----------
def next_id(events):
    if not events:
        return 101
    return max(e["event_id"] for e in events) + 1


def get_valid_date(prompt):
    while True:
        value = input(prompt).strip()
        try:
            datetime.strptime(value, "%Y-%m-%d")
            return value
        except ValueError:
            print("Invalid date. Please use YYYY-MM-DD (e.g. 2026-11-08).")


def find_event(events, event_id):
    for e in events:
        if e["event_id"] == event_id:
            return e
    return None


def ask_event_id():
    try:
        return int(input("Enter event ID: "))
    except ValueError:
        print("Event ID must be a number.")
        return None


def show_event(e):
    print("-" * 55)
    print(f"[{e['event_id']}] {e['title']}  ({e['category']})")
    print(f"  Description : {e['description']}")
    print(f"  Date        : {e['date']}")
    print(f"  Time        : {e['time']}")
    print(f"  Venue       : {e['venue']}, {e['city']}")
    print(f"  Organizer   : {e['organizer_name']}")
    print(f"  Contact     : {e['organizer_contact']}")
    print(f"  Participants: {len(e['participants'])}")


# ---------- Main features ----------
def add_event(events):
    print("\n--- Add New Event ---")
    event = {
        "event_id": next_id(events),
        "title": input("Event/Festival name: ").strip(),
        "category": input("Category (Festival/Cultural/Sports/Technical): ").strip(),
        "description": input("Short description: ").strip(),
        "date": get_valid_date("Date (YYYY-MM-DD): "),
        "time": input("Timing (e.g. 06:00 PM - 10:00 PM): ").strip(),
        "venue": input("Venue: ").strip(),
        "city": input("City: ").strip(),
        "organizer_name": input("Organizer name: ").strip(),
        "organizer_contact": input("Organizer contact (phone/email): ").strip(),
        "participants": [],
    }
    events.append(event)
    save_events(events)
    print(f"Event added successfully! Event ID = {event['event_id']}")


def view_events(events):
    print("\n--- Upcoming Events ---")
    if not events:
        print("No events announced yet.")
        return
    for e in sorted(events, key=lambda x: x["date"]):
        show_event(e)
    print("-" * 55)


def search_events(events):
    print("\n--- Search Events ---")
    key = input("Enter keyword (name / city / venue / category / date): ").strip().lower()
    found = [
        e for e in events
        if key in e["title"].lower() or key in e["city"].lower()
        or key in e["venue"].lower() or key in e["category"].lower()
        or key in e["date"]
    ]
    if not found:
        print("No matching events found.")
        return
    print(f"{len(found)} event(s) found:")
    for e in found:
        show_event(e)


def register_participant(events):
    print("\n--- Register Participant ---")
    event_id = ask_event_id()
    if event_id is None:
        return
    e = find_event(events, event_id)
    if e is None:
        print("Event not found.")
        return
    name = input("Participant name: ").strip()
    contact = input("Participant contact: ").strip()
    e["participants"].append({"name": name, "contact": contact})
    save_events(events)
    print(f"{name} registered for '{e['title']}'.")


def view_participants(events):
    print("\n--- Participant List ---")
    event_id = ask_event_id()
    if event_id is None:
        return
    e = find_event(events, event_id)
    if e is None:
        print("Event not found.")
        return
    print(f"Event: {e['title']}  |  Total participants: {len(e['participants'])}")
    if not e["participants"]:
        print("No participants registered yet.")
        return
    for i, p in enumerate(e["participants"], start=1):
        print(f"  {i}. {p['name']} - {p['contact']}")


def update_event(events):
    print("\n--- Update Event ---")
    event_id = ask_event_id()
    if event_id is None:
        return
    e = find_event(events, event_id)
    if e is None:
        print("Event not found.")
        return
    print("Press Enter to keep the old value.")
    e["title"] = input(f"Name [{e['title']}]: ").strip() or e["title"]
    new_date = input(f"Date [{e['date']}] (YYYY-MM-DD): ").strip()
    if new_date:
        try:
            datetime.strptime(new_date, "%Y-%m-%d")
            e["date"] = new_date
        except ValueError:
            print("Invalid date, old date kept.")
    e["time"] = input(f"Time [{e['time']}]: ").strip() or e["time"]
    e["venue"] = input(f"Venue [{e['venue']}]: ").strip() or e["venue"]
    e["organizer_contact"] = (
        input(f"Organizer contact [{e['organizer_contact']}]: ").strip()
        or e["organizer_contact"]
    )
    save_events(events)
    print("Event updated successfully!")


def delete_event(events):
    print("\n--- Cancel / Delete Event ---")
    event_id = ask_event_id()
    if event_id is None:
        return
    e = find_event(events, event_id)
    if e is None:
        print("Event not found.")
        return
    confirm = input(f"Delete '{e['title']}'? (y/n): ").strip().lower()
    if confirm == "y":
        events.remove(e)
        save_events(events)
        print("Event deleted.")
    else:
        print("Cancelled.")


# ---------- Program start ----------
def main():
    events = load_events()
    while True:
        print("\n" + "=" * 40)
        print("        EVENTVERSE")
        print(" Event & Festival Announcement System")
        print("=" * 40)
        print("1. Add new event")
        print("2. View all upcoming events")
        print("3. Search events")
        print("4. Register participant")
        print("5. View participants of an event")
        print("6. Update event")
        print("7. Cancel / delete event")
        print("8. Exit")
        choice = input("Enter your choice (1-8): ").strip()

        if choice == "1":
            add_event(events)
        elif choice == "2":
            view_events(events)
        elif choice == "3":
            search_events(events)
        elif choice == "4":
            register_participant(events)
        elif choice == "5":
            view_participants(events)
        elif choice == "6":
            update_event(events)
        elif choice == "7":
            delete_event(events)
        elif choice == "8":
            print("Thank you for using Eventverse. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 8.")


if __name__ == "__main__":
    main()
