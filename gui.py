import sys
from PySide6.QtCore import QObject, QProcess, Signal
from PySide6.QtWidgets import QApplication, QMainWindow

class ProcessManager(QObject):
    """Starts/stops sensors and apps. No UI code in here."""
    output = Signal(str, str)      # (name, text)
    state_changed = Signal(str, bool)
    # start(name, cmd), stop(name), stop_all() ...

class RosWorker(QObject):
    """rclpy node + executor in its own thread; emits signals only."""

class MainWindow(QMainWindow):
    """Widgets only. Talks to the backend via signals/slots."""

def main():
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()