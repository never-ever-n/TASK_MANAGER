# TASK-MANAGER PROJECT
<br>
OVERVIEW:
<br>
<br>
Task Tracker - Tkinter & ttkbootstrap
<br>
A modern Task Tracker application built using Python, Tkinter, and ttkbootstrap for a sleek and stylish GUI. This app helps you manage tasks by allowing you to:
<br>
✅ Add tasks with a title, description, and priority.
<br>
✅ View all tasks in a structured table.
<br>
✅ Mark tasks as complete with a single click.
<br>
✅ Delete tasks when they're no longer needed.
<br>
<hr>
Features
<br>
Modern UI: Uses ttkbootstrap for a better-looking interface.
<br>
Task Prioritization: Assign priorities like Low, Medium, or High.
<br>
Task Persistence: Saves tasks in a tasks.json file, so they are not lost when the app is closed.
<br>
Interactive Table: Displays tasks in a structured Treeview table.
<br>
Responsive Buttons: Buttons with different styles for adding, marking complete, and deleting tasks.
<br>
<br>
<hr>
Installation & Setup
<br>
1. Install Python (if not installed)
<br>
Ensure you have Python installed (version 3.7+ recommended).
<br>
2. Install Dependencies
<br>
Run the following command to install the required package:
<br>
pip install ttkbootstrap
<br>
3. Run the Application
<br>
Download or clone the task_tracker.py file and run:
<br>
python task_tracker.py
<br>
<hr>
How to Use
<br>
Adding a Task
<br>
1. Enter a Task Title and Description.
<br>
2. Select a Priority (Low, Medium, or High).
<br>
3. Click the "Add Task" button.
<br>
<hr>
Marking a Task as Complete
<br>
1. Select a task from the list.
<br>
2. Click the "Mark Complete" button.
<br>
3. The task's status will change to ✔.
<br>
<hr>
Deleting a Task
<br>
1. Select a task from the list.
<br>
<br>
2. Click the "Delete Task" button to remove it permanently.
<br>
<hr>
Project Structure
<br>
task_tracker/
<br>
│── task_tracker.py   # Main application script
<br>
│── tasks.json        # Stores task data persistently
<br>
│── README.md         # Instructions to run the project
<br>
<hr>
Customization
<br>
Change the theme by modifying this line in task_tracker.py:
<br>
root = ttk.Window(themename="darkly")
<br>
Available themes: "darkly", "solar", "morph", "journal", etc.
<br>
Modify task priority options by editing:
<br>
priority_menu = ttk.Combobox(root, textvariable=priority_var, values=["Low", "Medium", "High"])
<br>
To reset all tasks, delete tasks.json and restart the app.
<br>
<hr>
License
<br>
This project is open-source. Feel free to modify and use it as needed!
<br>
🚀 Enjoy managing your tasks efficiently! 🚀
<br>
<hr>
CONTRIBUTION:
<br>
<br>
Phanindra O.V.A (Add task feature)
<br>
Yashwanth Kumar Monganti (Update task feature)
<br>
Akhil Bommu (Delete task feature)
<br>
SaiPardhiv Pamu (GUI feature)
<br>
Jyothi Sri Polavarapu (Save task feature and merge conflicts)
<br>
Praharsha Maroju (Mark as complete feature)
<br>
Sriram Kavadi (Load task feature and README file)



