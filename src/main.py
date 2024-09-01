import subprocess
import sys
import os
import venv


def install_package(package_name):
    """Installs a package using pip."""
    subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])


def is_package_installed(package_name):
    """Checks if a package is installed by trying to import it."""
    try:
        subprocess.check_call([sys.executable, "-c", f"import {package_name}"])
        return True
    except subprocess.CalledProcessError:
        return False


def create_and_activate_virtualenv(env_name="myenv"):
    """Creates a virtual environment if it doesn't exist and activates it."""
    if not os.path.exists(env_name):
        venv.create(env_name, with_pip=True)
        print(f"Virtual environment '{env_name}' created.")
    else:
        print(f"Virtual environment '{env_name}' already exists.")

    activate_script = os.path.join(env_name, "Scripts", "activate_this.py")
    if os.path.exists(activate_script):
        with open(activate_script) as script_file:
            exec(script_file.read(), {'__file__': activate_script})
        print(f"Activated virtual environment '{env_name}'.")
    else:
        print(f"Failed to activate virtual environment '{env_name}'.")


def main():
    env_name = "myenv"
    create_and_activate_virtualenv(env_name)

    required_packages = ["PyQt5", "PyQtWebEngine"]
    for package in required_packages:
        if not is_package_installed(package):
            print(f"{package} not found, installing...")
            install_package(package)
        else:
            print(f"{package} is already installed.")

    try:
        from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit
        from PyQt5.QtWebEngineWidgets import QWebEngineView
        from PyQt5.QtCore import QUrl, Qt
        from PyQt5.QtGui import QFont
    except ImportError as e:
        print(f"Failed to import necessary PyQt modules: {e}")
        sys.exit(1)

    class WebBrowser(QMainWindow):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

            self.setWindowTitle("Web Browser")
            self.setGeometry(200, 100, 1200, 800)

            self.browser = QWebEngineView()
            self.browser.setUrl(QUrl("http://www.google.com"))
            self.browser.setZoomFactor(1.25)

            self.url_bar = QLineEdit()
            self.url_bar.setMaximumHeight(35)
            self.url_bar.setFont(QFont("Arial", 12))
            self.url_bar.setStyleSheet("border-radius: 10px; padding: 5px;")
            self.url_bar.returnPressed.connect(self.navigate_to_url)

            self.go_btn = QPushButton("Go")
            self.go_btn.setMaximumHeight(35)
            self.go_btn.setFont(QFont("Arial", 12, QFont.Bold))
            self.go_btn.setStyleSheet("padding: 5px 10px; border-radius: 10px;")
            self.go_btn.clicked.connect(self.navigate_to_url)

            self.back_btn = QPushButton("<")
            self.back_btn.setMaximumHeight(35)
            self.back_btn.setFont(QFont("Arial", 12, QFont.Bold))
            self.back_btn.setStyleSheet("padding: 5px 10px; border-radius: 10px;")
            self.back_btn.clicked.connect(self.browser.back)

            self.forward_btn = QPushButton(">")
            self.forward_btn.setMaximumHeight(35)
            self.forward_btn.setFont(QFont("Arial", 12, QFont.Bold))
            self.forward_btn.setStyleSheet("padding: 5px 10px; border-radius: 10px;")
            self.forward_btn.clicked.connect(self.browser.forward)

            self.reload_btn = QPushButton("Reload")
            self.reload_btn.setMaximumHeight(35)
            self.reload_btn.setFont(QFont("Arial", 12, QFont.Bold))
            self.reload_btn.setStyleSheet("padding: 5px 10px; border-radius: 10px;")
            self.reload_btn.clicked.connect(self.browser.reload)

            self.zoom_in_btn = QPushButton("+")
            self.zoom_in_btn.setMaximumHeight(35)
            self.zoom_in_btn.setFont(QFont("Arial", 12, QFont.Bold))
            self.zoom_in_btn.setStyleSheet("padding: 5px 10px; border-radius: 10px;")
            self.zoom_in_btn.clicked.connect(self.zoom_in)

            self.zoom_out_btn = QPushButton("-")
            self.zoom_out_btn.setMaximumHeight(35)
            self.zoom_out_btn.setFont(QFont("Arial", 12, QFont.Bold))
            self.zoom_out_btn.setStyleSheet("padding: 5px 10px; border-radius: 10px;")
            self.zoom_out_btn.clicked.connect(self.zoom_out)

            self.layout = QVBoxLayout()
            self.horizontal_layout = QHBoxLayout()

            self.horizontal_layout.setSpacing(10)
            self.horizontal_layout.addWidget(self.url_bar)
            self.horizontal_layout.addWidget(self.go_btn)
            self.horizontal_layout.addWidget(self.back_btn)
            self.horizontal_layout.addWidget(self.forward_btn)
            self.horizontal_layout.addWidget(self.reload_btn)
            self.horizontal_layout.addWidget(self.zoom_in_btn)
            self.horizontal_layout.addWidget(self.zoom_out_btn)

            self.layout.addLayout(self.horizontal_layout)
            self.layout.addWidget(self.browser)

            container = QWidget()
            container.setLayout(self.layout)

            self.setCentralWidget(container)
            self.show()

        def navigate_to_url(self):
            url = self.url_bar.text()
            if not url.startswith("http"):
                url = "http://" + url
            self.browser.setUrl(QUrl(url))

        def zoom_in(self):
            current_zoom = self.browser.zoomFactor()
            self.browser.setZoomFactor(current_zoom + 0.1)

        def zoom_out(self):
            current_zoom = self.browser.zoomFactor()
            self.browser.setZoomFactor(current_zoom - 0.1)

        def keyPressEvent(self, event):
            if event.key() == Qt.Key_F11:
                self.toggle_fullscreen()

        def toggle_fullscreen(self):
            if self.isFullScreen():
                self.showNormal()
            else:
                self.showFullScreen()

    app = QApplication([])
    window = WebBrowser()
    app.exec_()


if __name__ == "__main__":
    main()





