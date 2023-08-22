import sys
import time
import pygetwindow as gw
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel

class TimerApp(QMainWindow):
    """
    A PyQt5-based timer application that automatically starts and stops based on
    the specified target window's title.

    Attributes:
        timer_running (bool): Flag indicating whether the timer is currently running.
        start_time (float): Timestamp when the timer was started.
        target_window_title (str): Title of the target application window to track.
    """

    def __init__(self):
        super().__init__()

        self.init_ui()
        self.timer_running = False
        self.start_time = None
        self.target_window_title = "PyCharm"  # Adjust this to match the target application's window title

    def init_ui(self):
        """Initialize the user interface."""
        self.setGeometry(100, 100, 400, 250)  # Adjust width to accommodate the File Dialog button
        self.setWindowTitle("Application Timer")

        # Create and position UI elements
        self.timer_label = QLabel("00:00:00", self)
        self.timer_label.setGeometry(150, 50, 100, 30)

        self.start_button = QPushButton("Start", self)
        self.start_button.setGeometry(50, 150, 75, 30)
        self.start_button.clicked.connect(self.start_timer)

        self.stop_button = QPushButton("Stop", self)
        self.stop_button.setGeometry(175, 150, 75, 30)
        self.stop_button.clicked.connect(self.stop_timer)

        # Initialize the timer update loop
        QTimer.singleShot(1000, self.update_timer)

    def start_timer(self):
        """Start the timer."""
        try:
            if not self.timer_running:
                self.timer_running = True
                self.start_time = time.time()
        except Exception as e:
            print(f"An error occurred while starting the timer: {e}")

    def update_timer(self):
        """Update the timer display based on the active window state."""
        try:
            active_window = gw.getActiveWindow()
            if hasattr(self, 'target_window_title') and active_window and self.target_window_title in active_window.title:
                self.start_timer()
            else:
                self.stop_timer()

            if self.timer_running:
                elapsed_time = int(time.time() - self.start_time)
                formatted_time = time.strftime("%H:%M:%S", time.gmtime(elapsed_time))
                self.timer_label.setText(formatted_time)
                self.timer_label.repaint()

        except Exception as e:
            print(f"An error occurred while updating the timer: {e}")
        finally:
            QTimer.singleShot(1000, self.update_timer)

    def stop_timer(self):
        """Stop the timer and display the total time spent."""
        try:
            if self.timer_running:
                self.timer_running = False
                elapsed_time = int(time.time() - self.start_time)
                formatted_time = time.strftime("%H:%M:%S", time.gmtime(elapsed_time))
                self.timer_label.setText("00:00:00")
                self.timer_label.repaint()

                print(f"Time spent on application: {formatted_time}")  # Print here

        except Exception as e:
            print(f"An error occurred while stopping the timer: {e}")
        finally:
            self.start_time = None

if __name__ == '__main__':
    app = QApplication(sys.argv)
    timer_app = TimerApp()
    timer_app.show()
    sys.exit(app.exec_())
