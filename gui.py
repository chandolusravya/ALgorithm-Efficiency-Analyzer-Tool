from PyQt5.QtWidgets import QComboBox
from PyQt5.QtWidgets import QDialog, QVBoxLayout
from PyQt5.QtWidgets import QWidget, QTextEdit, QCheckBox, QPlainTextEdit, QPushButton
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from qt_material import apply_stylesheet, list_themes


class SortingApp(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        apply_stylesheet(self, theme='dark_pink.xml')

        # 1. Text box with padding
        self.text_box = QTextEdit(self)
        self.text_box.setMaximumHeight(100)

        self.text_box.setPlaceholderText(
            "Enter a list of numbers to sort, and analyze their efficiency. ( Comma Separated or Space Separated )")
        layout.addWidget(self.text_box)

        # 2. List of checkboxes with sorting algorithms
        self.checkboxes = {}
        from main import all_algorithms
        for algo in all_algorithms:
            checkbox = QCheckBox(algo["name"], self)
            self.checkboxes[algo["id"]] = checkbox
            layout.addWidget(checkbox)
        # Button that will run a function when clicked
        self.run_button = QPushButton("Run Selected Algorithms", self)
        layout.addWidget(self.run_button)

        self.analyze = QPushButton("All Algorithms Efficiency", self)
        layout.addWidget(self.analyze)

        self.show_stats = QPushButton("Show Stats", self)
        layout.addWidget(self.show_stats)

        self.random_button = QPushButton("Populate Random Numbers", self)
        layout.addWidget(self.random_button)

        # 3. White box for logs
        self.log_box = QPlainTextEdit(self)
        self.log_box.setReadOnly(True)
        layout.addWidget(self.log_box)

        # Add Theme Dropdown
        self.theme = QComboBox(self)
        self.theme.addItems(list_themes())
        self.theme.currentTextChanged.connect(lambda x: apply_stylesheet(self, theme=x))
        layout.addWidget(self.theme)

        self.setLayout(layout)
        self.setWindowTitle("Algorithms Efficiency Analyzer Tool")

        # Set the window size
        self.resize(600, 800)
        # self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)
        self.show()

    def update_text_box(self, text):
        self.text_box.setPlainText(text)

    def sample_function(self):
        selected_algorithms = self.get_selected_checkboxes()
        self.log_message(f"Selected algorithms: {', '.join(selected_algorithms)}")

    def log_message(self, message):
        """Function to display a message in the log box."""
        self.log_box.appendPlainText(message)

    # Utility functions

    def get_checkboxes(self):
        return self.checkboxes

    def update_checkboxes(self, selected_algorithms):
        for algo, checkbox in self.checkboxes.items():
            checkbox.setChecked(algo in selected_algorithms)

    def update_input_text(self, text):
        self.text_box.setPlainText(text)

    def debug(self, message):
        """Function to print a debug message to the terminal."""
        print(f"DEBUG: {message}")

    def get_input_text(self):
        return self.text_box.toPlainText()

    def on_run_button_clicked(self, callback):
        self.run_button.clicked.connect(callback)

    def on_analyze_button_clicked(self, callback):
        self.analyze.clicked.connect(callback)

    def on_random_button_clicked(self, callback):
        self.random_button.clicked.connect(callback)
    def on_show_stats_button_clicked(self, callback):
        self.show_stats.clicked.connect(callback)

    def show_plot_dialog_with_figure(self, fig):
        dialog = QDialog(self)
        dialog.setWindowTitle("Plot Dialog")

        layout = QVBoxLayout()

        # Embed the Matplotlib figure into the dialog
        canvas = FigureCanvas(fig)
        navBar = NavigationToolbar(canvas, dialog)

        layout.addWidget(navBar)
        layout.addWidget(canvas)

        dialog.setLayout(layout)
        dialog.exec_()
