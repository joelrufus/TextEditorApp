

---

# TextEditorApp

A feature-rich, command-line-based text editor that allows users to perform **Create, Read, Update, Delete (CRUD)** operations on text files. This application is built with a **C++ backend** for efficient file handling and a **Python Tkinter-based UI** for an interactive user interface. The repository contains both the source code and precompiled executables for easy use.

## Features

- **Create**: Create new text files with user-provided content.
- **Read**: View the content of existing text files.
- **Update**: Append new content to an existing file.
- **Delete**: Remove a text file from the system.
- **Search**: Search for specific words in a file.
- **File Statistics**: View word count, line count, and character count for a file.

## Technologies Used

- **C++**: Backend operations for file management and text processing.
- **Python (Tkinter)**: Graphical User Interface (GUI) for a user-friendly experience.
- **Subprocess Module**: Used to integrate Python with the C++ backend.

## Project Structure

```
TextEditorApp/
│
├── dist/               # Folder containing executables
│   ├── text_editor.exe     # C++ executable for file operations
│   └── text_editor_ui.exe  # Python executable for the user interface
│
├── src/                # Source code folder
│   ├── text_editor.cpp     # C++ source code for backend file handling
│   └── text_editor_ui.py   # Python source code for the Tkinter UI
│
├── README.md           # Project documentation
├── .gitignore          # Files/folders to ignore in the repository
└── LICENSE             # License file (optional)
```

## How to Use

### 1. Using the Executables:
- Download the `dist/` folder and run `text_editor_ui.exe` to open the text editor UI.
- The UI provides buttons for the following operations:
  - **Create File**: Create new text files by entering a file name and content.
  - **Read File**: Display the content of an existing file.
  - **Update File**: Append additional content to an existing file.
  - **Delete File**: Permanently delete a file.
  - **Search Word**: Search for a specific word in a file.
  - **Show File Statistics**: Display word count, line count, and character count.

### 2. Running the Source Code:

#### Running the Python UI:
To run the Python Tkinter UI from the source code:
```bash
python src/text_editor_ui.py
```

#### Compiling the C++ Code:
To recompile the C++ backend (`text_editor.cpp`):
```bash
g++ src/text_editor.cpp -o dist/text_editor
```

## Requirements

- **Python 3.x** (for running the Python source code)
- **g++ compiler** (for compiling the C++ source code)
- **Tkinter** (for Python UI, installed by default with Python)

## Installation (For Developers)

To clone and run the project locally:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/TextEditorApp.git
   cd TextEditorApp
   ```

2. Install the required dependencies (if running from source):
   ```bash
   pip install tk
   ```

3. Run the Python UI:
   ```bash
   python src/text_editor_ui.py
   ```

4. Compile the C++ code if modified:
   ```bash
   g++ src/text_editor.cpp -o dist/text_editor
   ```

## License

This project is licensed under the [MIT License](LICENSE). You are free to use, modify, and distribute this software under the terms of the license.

---

Feel free to modify this README as necessary to match your exact project setup or add additional sections (such as screenshots or known issues). This provides clear documentation for users and developers alike.

