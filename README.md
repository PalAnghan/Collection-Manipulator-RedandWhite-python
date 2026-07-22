<div align="center">

<img src="https://capsule-render.vercel.app/api?type=cylinder&color=0:8E2DE2,100:4A00E0&height=200&section=header&text=Collection%20Manipulator&fontSize=42&fontColor=ffffff&animation=twinkling&fontAlignY=40&desc=Student%20Data%20Organizer%20%7C%20Python%20Console%20App&descAlignY=65&descSize=18" />

<img src="https://readme-typing-svg.demolab.com/?font=JetBrains+Mono&weight=600&size=24&duration=2500&pause=800&color=8E2DE2&center=true&vCenter=true&width=650&lines=Lists+%C2%B7+Tuples+%C2%B7+Sets+%C2%B7+Dictionaries;Mutability+%26+Immutability+in+Action;Type+Casting+%2B+the+del+Keyword;A+Menu-Driven+Python+Project" alt="Typing SVG" />

<br>

![Python](https://img.shields.io/badge/Python-3.10+-8E2DE2?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Completed-4A00E0?style=for-the-badge)
![Type](https://img.shields.io/badge/Type-Console_App-black?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-2E2E2E?style=for-the-badge)

</div>

<img src="https://capsule-render.vercel.app/api?type=rect&color=0:8E2DE2,100:4A00E0&height=3&section=header" width="100%">

<br>

<div align="center">

### 📖 Table of Contents

<table>
<tr>
<td valign="top" width="33%">

**Overview**
- [About the Project](#-about-the-project)
- [Demo Video](#-demo-video)
- [Features](#-features)

</td>
<td valign="top" width="33%">

**Deep Dive**
- [Concepts Applied](#-concepts-applied-in-depth)
- [Program Flow](#️-program-flow)
- [Menu Walkthrough](#-menu-walkthrough)

</td>
<td valign="top" width="33%">

**Getting Started**
- [Sample Run](#-sample-run)
- [Tech Stack](#-tech-stack)
- [Installation](#-getting-started)

</td>
</tr>
<tr>
<td valign="top" width="33%">

**Reference**
- [Project Structure](#-project-structure)
- [Assumptions](#-assumptions)

</td>
<td valign="top" width="33%">

**What's Next**
- [Future Improvements](#-future-improvements)

</td>
<td valign="top" width="33%">

**Connect**
- [Author](#-author)

</td>
</tr>
</table>

</div>

<img src="https://capsule-render.vercel.app/api?type=rect&color=0:4A00E0,100:8E2DE2&height=3&section=header" width="100%">

<br>

## 🧩 About the Project

**Collection Manipulator** is a console-based Python application, built as an institute project, called the **Student Data Organizer**. It's designed around one core idea: give every one of Python's built-in collection types a real, practical job to do inside a single program.

Instead of treating `List`, `Tuple`, `Set`, and `Dictionary` as separate textbook topics, this project weaves them together — a student's editable details live in a dictionary, their permanent identity lives in a tuple, their subjects live in a set to avoid duplicates, and every student record lives inside a master list. The result is a small but complete data-management tool that mirrors how real applications structure information.

<br>

<div align="center">

## 🎬 Demo Video

<img src="https://img.shields.io/badge/Status-Coming_Soon-8E2DE2?style=for-the-badge&logo=youtube&logoColor=white">

*A walkthrough demo isn't recorded yet — this space is reserved for it.*

</div>

> 📌 **To add it later:** upload the video to GitHub (drag & drop into an Issue or the README editor to get a hosted link), then drop it in here as either:
> ```markdown
> https://github.com/user-attachments/assets/your-video-id
> ```
> or as a clickable thumbnail:
> ```markdown
> [![Watch the demo](thumbnail.png)](https://your-video-link)
> ```

<br>

<img src="https://capsule-render.vercel.app/api?type=rect&color=0:8E2DE2,100:4A00E0&height=2&section=header" width="100%">

<br>

## ✨ Features

| Feature | Description |
|---|---|
| 🧾 **Add Student** | Capture ID, name, age, grade, date of birth, and subjects in one flow |
| 📋 **Display All Students** | Neatly formatted, single-line-per-student output |
| ✏️ **Update Student Information** | Edit only the *mutable* fields — age, grade, subjects |
| ❌ **Delete Student** | Remove a record permanently using `del`, matched by ID |
| 📚 **Display Subjects Offered** | Aggregate every unique subject across all students |
| 🔁 **Persistent Menu Loop** | Runs continuously until the user chooses to exit |

<br>

<img src="https://capsule-render.vercel.app/api?type=rect&color=0:4A00E0,100:8E2DE2&height=2&section=header" width="100%">

<br>

## 🧠 Concepts Applied (In Depth)

<details>
<summary><b>📃 List — the master record book</b></summary>
<br>

Every student's dictionary is appended to a single list called `student`. This list is the backbone of the whole program — every menu option (display, update, delete) works by looping through it or indexing into it.

```python
student = []
student.append(student_data)
```
</details>

<details>
<summary><b>🔒 Tuple — the unchangeable identity</b></summary>
<br>

A student's **ID** and **date of birth** are combined into a tuple. Conceptually, these two values should never change once a student is registered — a tuple enforces that immutability at the language level.

```python
student_info = (stu_id, stu_b_date)
```
</details>

<details>
<summary><b>🎯 Set — subjects without duplicates</b></summary>
<br>

Subjects are entered as a comma-separated string and converted into a `set`, which automatically removes duplicate entries. This same technique is reused in **Display Subjects Offered**, where `.update()` merges every student's subjects into one de-duplicated collection.

```python
subject_set = set(stu_subjects.split(","))
display_subject.update(s["Subjects"])
```
</details>

<details>
<summary><b>🗂️ Dictionary — one record, many fields</b></summary>
<br>

Each student is represented as a dictionary with clear, labeled keys (`ID`, `Name`, `Age`, `Grade`, `DOB`, `Subjects`). This makes every field self-describing and easy to update by key rather than by position.

```python
student_data = {
    "ID": stu_id, "Name": stu_name, "Age": stu_age,
    "Grade": stu_grade, "DOB": stu_b_date, "Subjects": subject_set
}
```
</details>

<details>
<summary><b>🔁 Mutability vs Immutability</b></summary>
<br>

The dictionary's `Age`, `Grade`, and `Subjects` are freely reassigned during an update — demonstrating mutability. Meanwhile the tuple holding `ID` and `DOB` is never touched again after creation — demonstrating immutability, and reinforcing *why* a tuple was chosen for that data in the first place.
</details>

<details>
<summary><b>🔢 Type Casting</b></summary>
<br>

All numeric input from `input()` arrives as a string, so ID and age are explicitly cast with `int()` before being stored or compared.

```python
stu_id = int(input("student ID: "))
```
</details>

<details>
<summary><b>🗑️ The <code>del</code> Keyword</b></summary>
<br>

Deleting a student searches the list for a matching ID by index, then removes that exact entry from memory with `del student[i]` — rather than rebuilding the list or using a method like `.remove()`.
</details>

<br>

<img src="https://capsule-render.vercel.app/api?type=rect&color=0:8E2DE2,100:4A00E0&height=2&section=header" width="100%">

<br>

## 🗺️ Program Flow

```mermaid
flowchart TD
    A([Start Program]) --> B[Display Menu]
    B --> C{User Choice}
    C -->|1| D[Add Student]
    C -->|2| E[Display All Students]
    C -->|3| F[Update Student Info]
    C -->|4| G[Delete Student]
    C -->|5| H[Display Subjects Offered]
    C -->|6| I([Exit Program])
    D --> B
    E --> B
    F --> B
    G --> B
    H --> B
```

<br>

## 🧭 Menu Walkthrough

**1️⃣ Add Student** → prompts for ID, name, age, grade, DOB, and subjects → builds the tuple + set → stores everything in a dictionary → appends it to `student`.

**2️⃣ Display All Students** → loops through `student` and prints each record on a single formatted line; shows a friendly message if the list is empty.

**3️⃣ Update Student Information** → asks for an ID, locates the matching record, and lets the user overwrite age, grade, and subjects.

**4️⃣ Delete Student** → asks for an ID, finds its index in the list, and removes it with `del`.

**5️⃣ Display Subjects Offered** → builds a fresh `set`, merges every student's subjects into it, and prints the de-duplicated result.

**6️⃣ Exit** → breaks the loop and ends the program.

<br>

<img src="https://capsule-render.vercel.app/api?type=rect&color=0:4A00E0,100:8E2DE2&height=2&section=header" width="100%">

<br>

## 🖥️ Sample Run

```
Welcome to the Student Data Organizer!

Select Option:
1. Add Student
2. Display All Students
3. Update Student Information
4. Delete Student
5. Display Subjects Offered
6. Exit
Enter your choice: 1

Enter student details:
student ID: 101
Name: Alice
Age: 20
Grade: B+
Date of Birth (YYYY-MM-DD): 2002-05-14
Subjects (comma-separated): Math, Science, English

Student added successfully!

--- Display All Student ---
Student ID : 101 | Name: Alice | Age: 20 | Grade: B+ | DOB: 2002-05-14 | Subjects: {'Math', 'Science', 'English'}
```

<br>

<img src="https://capsule-render.vercel.app/api?type=rect&color=0:8E2DE2,100:4A00E0&height=2&section=header" width="100%">

<br>

## 🛠️ Tech Stack

![Python](https://img.shields.io/badge/-Python-8E2DE2?style=flat-square&logo=python&logoColor=white)
![CLI](https://img.shields.io/badge/-Command%20Line-4A00E0?style=flat-square&logo=windowsterminal&logoColor=white)
![Git](https://img.shields.io/badge/-Git-F05032?style=flat-square&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/-GitHub-181717?style=flat-square&logo=github&logoColor=white)

<br>

## 🚀 Getting Started

```bash
git clone https://github.com/<your-username>/collection-manipulator.git
cd collection-manipulator
python collection_manipulator.py
```

> Requires **Python 3.10+**, since the program uses the `match` statement for menu handling.

<br>

<img src="https://capsule-render.vercel.app/api?type=rect&color=0:4A00E0,100:8E2DE2&height=2&section=header" width="100%">

<br>

## 📂 Project Structure

```
collection-manipulator/
├── collection_manipulator.py
└── README.md
```

<br>

## 📝 Assumptions

- Student ID is assumed to be a unique integer entered manually by the user; no duplicate-check is enforced.
- Subjects are entered as a comma-separated string and converted into a `set` for automatic de-duplication.
- Input validation is kept minimal by design, so the project's focus stays on collection manipulation rather than defensive error handling.

<br>

## 🔮 Future Improvements

- Add duplicate-ID validation when adding a new student
- Persist data to a file or database instead of in-memory storage
- Add search/filter options (e.g., by grade or subject)
- Wrap numeric input parsing in try/except for graceful error handling
- Record and embed the demo video walkthrough

<br>

---

<div align="center">

## 👤 Author

**Pal Anghan**  
Final-year BCA Student · Aspiring MERN Stack Developer

[![LinkedIn](https://img.shields.io/badge/LinkedIn-pal--anghan-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/pal-anghan)
[![Email](https://img.shields.io/badge/Email-palanghan8%40gmail.com-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:palanghan8@gmail.com)

<img src="https://capsule-render.vercel.app/api?type=cylinder&color=0:4A00E0,100:8E2DE2&height=100&section=footer" />

**"Quality is our Motto." — Shaping skills for scaling higher...!!!**

</div>
