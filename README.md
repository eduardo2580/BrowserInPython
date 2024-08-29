# MyWebBrowser

MyWebBrowser is a simple web browser built using Python's PyQt5 and PyQtWebEngine. It features essential web browsing functions, including navigation controls, zooming, and full-screen mode, with a modern UI design.

## Features

- **Basic Navigation**: Navigate to any URL, go back, forward, and reload pages.
- **Zoom Controls**: Zoom in and out on web pages.
- **Rounded UI Elements**: Modern buttons with rounded corners.
- **Full-Screen Mode**: Toggle full-screen mode using the `F11` key.

## Installation

### Prerequisites

- Python 3.x
- `pip` (Python package installer)

### Setup Instructions

1. **Clone the Repository**

   ```bash
   git clone https://github.com/eduardo2580/BrowserInPython.git
   cd BrowserInPython
   ```

2. **Run the Script**

   The script will automatically set up a virtual environment, install dependencies, and run the browser.

   ```bash
   python src/main.py
   ```

3. **Manual Virtual Environment Activation**

   If the virtual environment is not activated automatically, you can activate it manually:

   - **On Windows:**

     ```bash
     .\myenv\Scripts\activate
     ```

   - **On macOS/Linux:**

     ```bash
     source myenv/bin/activate
     ```

4. **Run the Browser**

   With the virtual environment activated, run the browser:

   ```bash
   python src/main.py
   ```

## How It Works

- **Virtual Environment Setup:** Checks for the existence of a virtual environment named `myenv`. If not present, it creates one and installs `PyQt5` and `PyQtWebEngine`.
  
- **Browser Interface:** Includes a URL bar, navigation buttons (Go, Back, Forward, Reload), and zoom controls. The main content area displays web pages using `QWebEngineView`.

- **Event Handling:** Handles user input through the URL bar and buttons. Supports full-screen toggling via the `F11` key.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your improvements.

## Acknowledgments

- Built using [PyQt5](https://www.riverbankcomputing.com/software/pyqt/intro) and [PyQtWebEngine](https://www.riverbankcomputing.com/software/pyqtwebengine/intro).
