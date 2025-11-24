

# 📘 Study Tracker — Python CLI Project

A simple and beginner-friendly **Python command-line Study & Habit Tracker** that helps users log study sessions, view summaries, and generate weekly reports.
Designed for learners building their first real Python portfolio project.

---

## 🚀 Features

### ✅ Core Functionality

* **Add Study Sessions**
  Log subject, duration, notes, and date.

* **Persistent Data Storage**
  All entries are saved in a JSON file (`logs.json`), so your progress is never lost.

* **Daily & Weekly Summary**
  Automatically calculates:

  * total study time
  * total sessions
  * most studied subject
  * longest session
  * average session duration

* **Weekly Report Generator**
  Creates a formatted `.txt` report under the `reports/` directory.

* **Clean, Menu-Based CLI**
  Beginner-friendly navigation.

---

## 🧱 Project Structure

```
study_tracker/
│
├── tracker.py               # Main application
│
├── data/
│   └── logs.json            # Stores all study entries
│
└── reports/
    └── (weekly reports saved here)
```

---

## 📂 Data Format (logs.json)

Each study entry is saved as a dictionary:

```json
{
  "subject": "Python",
  "duration": 45,
  "notes": "Practiced loops",
  "date": "2025-11-23"
}
```

The file contains a list of these entries.

---

## 🛠️ Technologies Used

* **Python 3.x**
* **JSON** for data storage
* **datetime** for date handling
* **File I/O** for report generation

---

## 🧠 Concepts Learned / Demonstrated

This project showcases:

* functional programming
* lists & dictionaries
* reading and writing JSON
* input validation
* loops & conditionals
* modular design
* CLI user experience
* simple data analysis
* file generation (reports)

Perfect for:

* **internship applications**
* **GitHub portfolios**
* **beginner Python practice**

---

## ▶️ How to Run the Project

1. **Clone this repository:**

```bash
git clone https://github.com/yourusername/study_tracker.git
```

2. **Navigate to the project folder:**

```bash
cd study_tracker
```

3. **Run the application:**

```bash
python tracker.py
```

---

## 📅 Roadmap (Future Upgrades)

* [ ] Export study data to CSV
* [ ] Add graphs (matplotlib)
* [ ] Habit streak tracker
* [ ] Desktop GUI version (Tkinter)
* [ ] Timer-based study sessions

---

## 🤝 Contribution

This project is open for improvement.
Feel free to fork and expand it!

---

## 📜 License

MIT License — free to use, modify, and distribute.



