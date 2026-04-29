# Josephus Problem Visualizer

An interactive Python GUI application that visualizes the classic Josephus Problem using Tkinter.

## Overview

The Josephus Problem is a famous theoretical problem where `n` people stand in a circle, and every `k`-th person is eliminated until only one survivor remains.

This project demonstrates the algorithm visually by placing soldiers around a circle and animating the elimination process step by step.

## Features

* Interactive GUI built with Tkinter
* Input fields for number of soldiers and step size
* Animated elimination process
* Survivor highlighted at the end
* Elimination order displayed in real time
* Input validation for invalid values
* Clean separation between algorithm logic and GUI

## Technologies Used

* Python
* Tkinter
* Math module

## Project Structure

```
josephus-visualizer/
├── main.py
├── josephus.py
├── gui.py
├── README.md
├── requirements.txt
└── .gitignore
```

## How to Run

Clone the repository:

```bash
git clone https://github.com/YOUR-USERNAME/josephus-visualizer.git
cd josephus-visualizer
```

Run the application:

```bash
python main.py
```

## Example

Input:

```
Number of soldiers: 7
Step size: 3
```

The program eliminates every third soldier until one survivor remains.

## What I Learned

Through this project, I practiced:

* Implementing the Josephus algorithm
* Working with lists and modular arithmetic
* Building a GUI with Tkinter
* Drawing and animating objects on a canvas
* Separating application logic from user interface code
* Handling invalid user input

## Future Improvements

* Add a speed control slider
* Add pause and resume buttons
* Export elimination order to a file
* Add unit tests for the algorithm
* Improve the visual design
* Add dark mode


