Eventverse - Event and Festival Announcement System
Author: Rajkumar Kirar
Registration No.: 26BCE11128
Course: Python Essential
Academic Year: 2026-27
About the Project
Eventverse is a menu-driven Python application that announces upcoming events and festival celebrations. It keeps all important details in one place: event name and category, date and timing, venue, organizer name and contact, and participant details.
Features
Add new events and festivals
View all upcoming events (sorted by date)
Search events by name, city, venue, category or date
Register participants for an event
View the participant list of an event
Update event details (name, date, time, venue, organizer contact)
Cancel / delete an event
Data is saved permanently in a events.json file
Requirements
Python 3.10 or above
No external libraries needed (uses only json and datetime from the standard library)
How to Run
Download or copy main.py into a folder.
Open a terminal / command prompt in that folder.
Run:
python main.py
(On some systems use python3 main.py.)
Menu Options
Option
Action
1
Add new event
2
View all upcoming events
3
Search events
4
Register participant
5
View participants of an event
6
Update event
7
Cancel / delete event
8
Exit
Data Stored for Each Event
Field
Description
event_id
Unique ID given automatically
title
Name of the event / festival
category
Festival, Cultural, Sports, Technical, etc.
description
Short description
date
Event date (YYYY-MM-DD)
time
Start and end timing
venue, city
Where the event is held
organizer_name, organizer_contact
Organizer details
participants
List of registered participants (name, contact)
Sample Output
[101] Diwali Night  (Festival)
  Description : Cultural evening
  Date        : 2026-11-08
  Time        : 6 PM - 10 PM
  Venue       : Community Hall, Bhopal
  Organizer   : Anita Sharma
  Contact     : 98000001
  Participants: 1
Project Files
Eventverse/
|-- main.py        # Main program
|-- events.json    # Created automatically when the first event is added
|-- README.md      # Project documentation
Future Improvements
GUI (Tkinter) or web version (Flask / Django)
Database support (SQLite / MySQL)
User login for organizers and participants
Email / SMS reminders
Conclusion
Eventverse shows how core Python concepts such as functions, lists, dictionaries, loops, conditions and file handling can be used to build a practical event announcement system.
