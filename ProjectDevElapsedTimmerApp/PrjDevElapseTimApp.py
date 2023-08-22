import sys
import time
import psutil
import pygetwindow as gw
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QFileDialog, QLineEdit


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

        self.timer_label = QLabel("00:00:00", self)
        self.timer_label.setGeometry(150, 50, 100, 30)

        self.folder_path_label = QLabel("Project Folder Path:", self)
        self.folder_path_label.setGeometry(30, 100, 130, 20)

        self.folder_path_input = QLineEdit(self)
        self.folder_path_input.setGeometry(170, 100, 180, 20)

        self.browse_button = QPushButton("Browse", self)
        self.browse_button.setGeometry(360, 100, 70, 20)
        self.browse_button.clicked.connect(self.browse_folder)

        self.start_button = QPushButton("Start", self)
        self.start_button.setGeometry(50, 150, 75, 30)
        self.start_button.clicked.connect(self.start_timer)

        self.stop_button = QPushButton("Stop", self)
        self.stop_button.setGeometry(175, 150, 75, 30)
        self.stop_button.clicked.connect(self.stop_timer)

        self.update_timer()

    def browse_folder(self):
        """Open a folder dialog to select the project folder path."""
        folder_path = QFileDialog.getExistingDirectory(self, "Select Project Folder")
        if folder_path:
            self.folder_path_input.setText(folder_path)

    def start_timer(self):
        """Start the timer."""
        try:
            if not self.timer_running:
                self.timer_running = True
                self.start_time = time.time()
                self.target_window_title = self.folder_path_input.text()  # Set target window title based on folder path
        except Exception as e:
            print(f"An error occurred while starting the timer: {e}")

    def stop_timer(self):
        """Stop the timer and display the total time spent."""
        try:
            if self.timer_running:
                self.timer_running = False
                elapsed_time = int(time.time() - self.start_time)
                formatted_time = time.strftime("%H:%M:%S", time.gmtime(elapsed_time))
                print(f"Time spent on application: {formatted_time}")
                self.timer_label.setText("00:00:00")
                self.timer_label.repaint()
        except Exception as e:
            print(f"An error occurred while stopping the timer: {e}")
        finally:
            self.start_time = None

    # def update_timer(self):
    #     """Update the timer display and track the target window state."""
    #     try:
    #         active_window = gw.getActiveWindow()
    #         if active_window and self.target_window_title in active_window.title:
    #             self.start_timer()
    #         else:
    #             self.stop_timer()
    #
    #         if self.timer_running:
    #             elapsed_time = int(time.time() - self.start_time)
    #             formatted_time = time.strftime("%H:%M:%S", time.gmtime(elapsed_time))
    #             self.timer_label.setText(formatted_time)
    #             self.timer_label.repaint()
    #
    #     except Exception as e:
    #         print(f"An error occurred while updating the timer: {e}")
    #     finally:
    #         QTimer.singleShot(1000, self.update_timer)

    # ...

    def update_timer(self):
        """Update the timer display and track the target process state."""
        try:
            if self.target_window_title:
                project_folder = self.folder_path_input.text()
                target_process_name = "python"  # Change this to the process name of the application you want to track

                process_found = False
                for process in psutil.process_iter(attrs=['pid', 'name']):
                    try:
                        process_name = process.info['name']
                        if process_name == target_process_name:
                            cmdline = process.cmdline()
                            if len(cmdline) > 1 and project_folder in cmdline[1]:
                                process_found = True
                                break
                    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                        pass

                if process_found:
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

    # ...


if __name__ == '__main__':
    app = QApplication(sys.argv)
    timer_app = TimerApp()
    timer_app.show()
    sys.exit(app.exec_())
