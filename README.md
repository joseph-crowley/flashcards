# Flashcards

A modern, sleek, and responsive flashcards web application designed to help users study and memorize information quickly and efficiently. Built with Flask, this app reads JSON files containing question and answer pairs and displays them as interactive flashcards.

# Features

    Responsive design that looks great on desktop and mobile devices
    Customizable flashcard data via JSON files
    Smooth animations and transitions for an engaging user experience
    Easy question and answer toggling

# Getting Started
## Prerequisites

    Python 3.6 or higher
    Flask 1.0 or higher

## Installation

### Clone the repository:

```bash
git clone https://github.com/joseph-crowley/flashcards-app.git
cd flashcards-app
```

### (Optional) Create a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install Flask:

```bash
pip install Flask
```

# Run the app:

    python app.py

    Visit http://127.0.0.1:5000 in your web browser to start using the flashcards app.

# Customizing Flashcards

To customize the flashcards, create a JSON file with the following format:

```json
[
    { "QUESTION1": "ANSWER1" },
    { "QUESTION2": "ANSWER2" }
]
```

Save the JSON file in the same directory as the app.py file. To access the custom flashcards, visit the URL route http://127.0.0.1:5000/filename, where filename is the name of your JSON file without the .json extension.
# Built With

    Flask - The web framework used
    Bootstrap - Responsive styling and components
    Google Fonts - Typography
    Animate.css - Smooth animations


This project is licensed under the MIT License - see the LICENSE.md file for details.
