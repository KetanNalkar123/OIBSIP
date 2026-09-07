"""
Advanced BMI Calculator
OASIS INFOBYTE - Python Programming Internship
Task 2: Advanced BMI Calculator
"""

import tkinter as tk
from tkinter import ttk, messagebox

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

from bmi_calculator import calculate_bmi, get_category_color
import database


class BMICalculatorApp:
    """
    Main application class for the Advanced BMI Calculator.
    """

    def __init__(self, root):
        self.root = root

        self.root.title("Advanced BMI Calculator")
        self.root.geometry("1050x700")
        self.root.minsize(900, 600)

        self.root.configure(bg="#F4F6F7")

        self.setup_style()

        self.create_variables()

        try:
            database.initialize_database()
        except RuntimeError as error:
            messagebox.showerror(
                "Database Error",
                str(error)
            )

        self.create_header()
        self.create_notebook()
        self.create_calculator_tab()
        self.create_history_tab()
        self.create_footer()

        self.refresh_history()
        self.refresh_users()

    # ---------------------------------------------------------
    # STYLE
    # ---------------------------------------------------------

    def setup_style(self):
        """
        Configure ttk styles.
        """

        style = ttk.Style()

        try:
            style.theme_use("clam")
        except tk.TclError:
            pass

        style.configure(
            "TButton",
            font=("Segoe UI", 10, "bold"),
            padding=(12, 8)
        )

        style.configure(
            "TLabel",
            font=("Segoe UI", 10)
        )

        style.configure(
            "Title.TLabel",
            font=("Segoe UI", 24, "bold")
        )

        style.configure(
            "Subtitle.TLabel",
            font=("Segoe UI", 10)
        )

        style.configure(
            "TNotebook.Tab",
            font=("Segoe UI", 10, "bold"),
            padding=(20, 10)
        )

        style.configure(
            "Treeview",
            font=("Segoe UI", 10),
            rowheight=30
        )

        style.configure(
            "Treeview.Heading",
            font=("Segoe UI", 10, "bold")
        )

    # ---------------------------------------------------------
    # VARIABLES
    # ---------------------------------------------------------

    def create_variables(self):
        """
        Create Tkinter variables.
        """

        self.name_var = tk.StringVar()
        self.weight_var = tk.StringVar()
        self.height_var = tk.StringVar()

        self.result_bmi_var = tk.StringVar(
            value="--"
        )

        self.result_category_var = tk.StringVar(
            value="Enter your details and calculate BMI"
        )

        self.history_user_var = tk.StringVar(
            value="All Users"
        )

        self.status_var = tk.StringVar(
            value="Ready"
        )

    # ---------------------------------------------------------
    # HEADER
    # ---------------------------------------------------------

    def create_header(self):
        """
        Create application header.
        """

        header = tk.Frame(
            self.root,
            bg="#2C3E50",
            height=90
        )

        header.pack(
            fill="x"
        )

        header.pack_propagate(False)

        title = tk.Label(
            header,
            text="Advanced BMI Calculator",
            bg="#2C3E50",
            fg="white",
            font=("Segoe UI", 24, "bold")
        )

        title.pack(
            pady=(15, 0)
        )

        subtitle = tk.Label(
            header,
            text="Track BMI, maintain history and visualize your progress",
            bg="#2C3E50",
            fg="#D5DBDB",
            font=("Segoe UI", 10)
        )

        subtitle.pack()

    # ---------------------------------------------------------
    # NOTEBOOK
    # ---------------------------------------------------------

    def create_notebook(self):
        """
        Create notebook tabs.
        """

        self.notebook = ttk.Notebook(
            self.root
        )

        self.notebook.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=15
        )

        self.calculator_tab = ttk.Frame(
            self.notebook
        )

        self.history_tab = ttk.Frame(
            self.notebook
        )

        self.notebook.add(
            self.calculator_tab,
            text="  BMI Calculator  "
        )

        self.notebook.add(
            self.history_tab,
            text="  History & Trends  "
        )

    # ---------------------------------------------------------
    # CALCULATOR TAB
    # ---------------------------------------------------------

    def create_calculator_tab(self):
        """
        Create BMI calculator interface.
        """

        main_frame = tk.Frame(
            self.calculator_tab,
            bg="#F4F6F7"
        )

        main_frame.pack(
            fill="both",
            expand=True
        )

        left_frame = tk.Frame(
            main_frame,
            bg="white",
            bd=1,
            relief="solid"
        )

        left_frame.pack(
            side="left",
            fill="both",
            expand=True,
            padx=(10, 5),
            pady=10
        )

        right_frame = tk.Frame(
            main_frame,
            bg="white",
            bd=1,
            relief="solid"
        )

        right_frame.pack(
            side="right",
            fill="both",
            expand=True,
            padx=(5, 10),
            pady=10
        )

        # ---------------- INPUT SECTION ----------------

        input_title = tk.Label(
            left_frame,
            text="Enter Your Details",
            bg="white",
            fg="#2C3E50",
            font=("Segoe UI", 18, "bold")
        )

        input_title.pack(
            pady=(30, 25)
        )

        # Name

        name_label = tk.Label(
            left_frame,
            text="User Name",
            bg="white",
            fg="#34495E",
            font=("Segoe UI", 11, "bold")
        )

        name_label.pack(
            anchor="w",
            padx=45
        )

        self.name_entry = ttk.Entry(
            left_frame,
            textvariable=self.name_var,
            font=("Segoe UI", 11)
        )

        self.name_entry.pack(
            fill="x",
            padx=45,
            pady=(5, 20)
        )

        # Weight

        weight_label = tk.Label(
            left_frame,
            text="Weight (kg)",
            bg="white",
            fg="#34495E",
            font=("Segoe UI", 11, "bold")
        )

        weight_label.pack(
            anchor="w",
            padx=45
        )

        self.weight_entry = ttk.Entry(
            left_frame,
            textvariable=self.weight_var,
            font=("Segoe UI", 11)
        )

        self.weight_entry.pack(
            fill="x",
            padx=45,
            pady=(5, 20)
        )

        # Height

        height_label = tk.Label(
            left_frame,
            text="Height (cm)",
            bg="white",
            fg="#34495E",
            font=("Segoe UI", 11, "bold")
        )

        height_label.pack(
            anchor="w",
            padx=45
        )

        self.height_entry = ttk.Entry(
            left_frame,
            textvariable=self.height_var,
            font=("Segoe UI", 11)
        )

        self.height_entry.pack(
            fill="x",
            padx=45,
            pady=(5, 25)
        )

        # Buttons

        button_frame = tk.Frame(
            left_frame,
            bg="white"
        )

        button_frame.pack(
            pady=10
        )

        calculate_button = tk.Button(
            button_frame,
            text="Calculate BMI",
            command=self.calculate_and_save,
            bg="#27AE60",
            fg="white",
            activebackground="#229954",
            activeforeground="white",
            font=("Segoe UI", 11, "bold"),
            padx=18,
            pady=10,
            relief="flat",
            cursor="hand2"
        )

        calculate_button.pack(
            side="left",
            padx=5
        )

        clear_button = tk.Button(
            button_frame,
            text="Clear",
            command=self.clear_fields,
            bg="#7F8C8D",
            fg="white",
            activebackground="#707B7C",
            activeforeground="white",
            font=("Segoe UI", 11, "bold"),
            padx=25,
            pady=10,
            relief="flat",
            cursor="hand2"
        )

        clear_button.pack(
            side="left",
            padx=5
        )

        # Information

        info = tk.Label(
            left_frame,
            text=(
                "BMI = Weight (kg) / Height² (m)\n\n"
                "This calculator is for educational purposes only\n"
                "and should not replace professional medical advice."
            ),
            bg="white",
            fg="#7F8C8D",
            font=("Segoe UI", 9),
            justify="center"
        )

        info.pack(
            pady=(30, 10)
        )

        # ---------------- RESULT SECTION ----------------

        result_title = tk.Label(
            right_frame,
            text="BMI Result",
            bg="white",
            fg="#2C3E50",
            font=("Segoe UI", 18, "bold")
        )

        result_title.pack(
            pady=(30, 20)
        )

        self.result_card = tk.Frame(
            right_frame,
            bg="#ECF0F1",
            width=300,
            height=210
        )

        self.result_card.pack(
            padx=30,
            pady=10
        )

        self.result_card.pack_propagate(False)

        bmi_heading = tk.Label(
            self.result_card,
            text="Your BMI",
            bg="#ECF0F1",
            fg="#34495E",
            font=("Segoe UI", 12, "bold")
        )

        bmi_heading.pack(
            pady=(25, 5)
        )

        self.bmi_result_label = tk.Label(
            self.result_card,
            textvariable=self.result_bmi_var,
            bg="#ECF0F1",
            fg="#2C3E50",
            font=("Segoe UI", 40, "bold")
        )

        self.bmi_result_label.pack()

        self.category_label = tk.Label(
            self.result_card,
            textvariable=self.result_category_var,
            bg="#ECF0F1",
            fg="#34495E",
            font=("Segoe UI", 12, "bold"),
            wraplength=300
        )

        self.category_label.pack(
            pady=5
        )

        # BMI ranges

        range_title = tk.Label(
            right_frame,
            text="BMI Categories",
            bg="white",
            fg="#2C3E50",
            font=("Segoe UI", 13, "bold")
        )

        range_title.pack(
            pady=(20, 10)
        )

        ranges = [
            ("Underweight", "Below 18.5", "#3498DB"),
            ("Normal", "18.5 - 24.9", "#27AE60"),
            ("Overweight", "25.0 - 29.9", "#F39C12"),
            ("Obese", "30.0 and above", "#E74C3C")
        ]

        for category, value, color in ranges:

            row = tk.Frame(
                right_frame,
                bg="white"
            )

            row.pack(
                fill="x",
                padx=70,
                pady=3
            )

            color_box = tk.Label(
                row,
                bg=color,
                width=2
            )

            color_box.pack(
                side="left",
                padx=(0, 8)
            )

            label = tk.Label(
                row,
                text=f"{category}: {value}",
                bg="white",
                fg="#34495E",
                font=("Segoe UI", 9)
            )

            label.pack(
                side="left"
            )

    # ---------------------------------------------------------
    # CALCULATE BMI
    # ---------------------------------------------------------

    def calculate_and_save(self):
        """
        Validate inputs, calculate BMI and save record.
        """

        name = self.name_var.get().strip()
        weight_text = self.weight_var.get().strip()
        height_text = self.height_var.get().strip()

        if not name:
            messagebox.showwarning(
                "Input Required",
                "Please enter the user name."
            )
            self.name_entry.focus()
            return

        if not weight_text:
            messagebox.showwarning(
                "Input Required",
                "Please enter your weight."
            )
            self.weight_entry.focus()
            return

        if not height_text:
            messagebox.showwarning(
                "Input Required",
                "Please enter your height."
            )
            self.height_entry.focus()
            return

        try:
            weight = float(weight_text)
            height = float(height_text)

        except ValueError:
            messagebox.showerror(
                "Invalid Input",
                "Weight and height must be numeric values."
            )
            return

        if weight <= 0:
            messagebox.showerror(
                "Invalid Weight",
                "Weight must be greater than 0."
            )
            return

        if height <= 0:
            messagebox.showerror(
                "Invalid Height",
                "Height must be greater than 0."
            )
            return

        if weight > 500:
            messagebox.showerror(
                "Invalid Weight",
                "Please enter a realistic weight below 500 kg."
            )
            return

        if height > 300:
            messagebox.showerror(
                "Invalid Height",
                "Please enter a realistic height below 300 cm."
            )
            return

        try:
            bmi, category = calculate_bmi(
                weight,
                height
            )

            database.add_record(
                name,
                weight,
                height,
                bmi,
                category
            )

        except (ValueError, RuntimeError) as error:
            messagebox.showerror(
                "Error",
                str(error)
            )
            return

        self.result_bmi_var.set(
            f"{bmi:.2f}"
        )

        self.result_category_var.set(
            category
        )

        category_color = get_category_color(
            category
        )

        self.result_card.configure(
            bg=category_color
        )

        self.bmi_result_label.configure(
            bg=category_color,
            fg="white"
        )

        self.category_label.configure(
            bg=category_color,
            fg="white"
        )

        self.status_var.set(
            f"BMI calculated successfully for {name}."
        )

        self.refresh_history()
        self.refresh_users()

        messagebox.showinfo(
            "BMI Calculated",
            f"{name}'s BMI is {bmi:.2f} ({category}).\n\n"
            "The result has been saved to history."
        )

    # ---------------------------------------------------------
    # CLEAR FIELDS
    # ---------------------------------------------------------

    def clear_fields(self):
        """
        Clear calculator fields and reset result.
        """

        self.name_var.set("")
        self.weight_var.set("")
        self.height_var.set("")

        self.result_bmi_var.set("--")

        self.result_category_var.set(
            "Enter your details and calculate BMI"
        )

        self.result_card.configure(
            bg="#ECF0F1"
        )

        self.bmi_result_label.configure(
            bg="#ECF0F1",
            fg="#2C3E50"
        )

        self.category_label.configure(
            bg="#ECF0F1",
            fg="#34495E"
        )

        self.status_var.set(
            "Fields cleared."
        )

        self.name_entry.focus()

    # ---------------------------------------------------------
    # HISTORY TAB
    # ---------------------------------------------------------

    def create_history_tab(self):
        """
        Create history and trend interface.
        """

        container = tk.Frame(
            self.history_tab,
            bg="#F4F6F7"
        )

        container.pack(
            fill="both",
            expand=True
        )

        top_frame = tk.Frame(
            container,
            bg="white",
            bd=1,
            relief="solid"
        )

        top_frame.pack(
            fill="x",
            padx=10,
            pady=(10, 5)
        )

        title = tk.Label(
            top_frame,
            text="BMI History",
            bg="white",
            fg="#2C3E50",
            font=("Segoe UI", 18, "bold")
        )

        title.pack(
            side="left",
            padx=20,
            pady=15
        )

        user_label = tk.Label(
            top_frame,
            text="Filter User:",
            bg="white",
            fg="#34495E",
            font=("Segoe UI", 10, "bold")
        )

        user_label.pack(
            side="left",
            padx=(20, 5)
        )

        self.user_combo = ttk.Combobox(
            top_frame,
            textvariable=self.history_user_var,
            state="readonly",
            width=20
        )

        self.user_combo.pack(
            side="left",
            padx=5
        )

        self.user_combo.bind(
            "<<ComboboxSelected>>",
            lambda event: self.refresh_history()
        )

        refresh_button = ttk.Button(
            top_frame,
            text="Refresh",
            command=self.refresh_history
        )

        refresh_button.pack(
            side="left",
            padx=5
        )

        graph_button = ttk.Button(
            top_frame,
            text="Show BMI Trend",
            command=self.show_trend
        )

        graph_button.pack(
            side="left",
            padx=5
        )

        delete_button = ttk.Button(
            top_frame,
            text="Delete Selected",
            command=self.delete_selected
        )

        delete_button.pack(
            side="left",
            padx=5
        )

        # ---------------- TABLE ----------------

        table_frame = tk.Frame(
            container,
            bg="white",
            bd=1,
            relief="solid"
        )

        table_frame.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=5
        )

        columns = (
            "id",
            "name",
            "weight",
            "height",
            "bmi",
            "category",
            "date"
        )

        self.history_tree = ttk.Treeview(
            table_frame,
            columns=columns,
            show="headings",
            selectmode="extended"
        )

        headings = {
            "id": "ID",
            "name": "User",
            "weight": "Weight (kg)",
            "height": "Height (cm)",
            "bmi": "BMI",
            "category": "Category",
            "date": "Date & Time"
        }

        widths = {
            "id": 50,
            "name": 140,
            "weight": 100,
            "height": 100,
            "bmi": 80,
            "category": 120,
            "date": 170
        }

        for column in columns:

            self.history_tree.heading(
                column,
                text=headings[column]
            )

            self.history_tree.column(
                column,
                width=widths[column],
                anchor="center"
            )

        scrollbar_y = ttk.Scrollbar(
            table_frame,
            orient="vertical",
            command=self.history_tree.yview
        )

        scrollbar_x = ttk.Scrollbar(
            table_frame,
            orient="horizontal",
            command=self.history_tree.xview
        )

        self.history_tree.configure(
            yscrollcommand=scrollbar_y.set,
            xscrollcommand=scrollbar_x.set
        )

        self.history_tree.pack(
            side="left",
            fill="both",
            expand=True
        )

        scrollbar_y.pack(
            side="right",
            fill="y"
        )

        scrollbar_x.pack(
            side="bottom",
            fill="x"
        )

        # ---------------- BOTTOM INFO ----------------

        bottom_frame = tk.Frame(
            container,
            bg="#F4F6F7"
        )

        bottom_frame.pack(
            fill="x",
            padx=10,
            pady=(5, 10)
        )

        info = tk.Label(
            bottom_frame,
            text=(
                "Select a user to view their records and BMI trend. "
                "All calculations are stored locally using SQLite."
            ),
            bg="#F4F6F7",
            fg="#7F8C8D",
            font=("Segoe UI", 9)
        )

        info.pack(
            side="left"
        )

    # ---------------------------------------------------------
    # REFRESH USERS
    # ---------------------------------------------------------

    def refresh_users(self):
        """
        Refresh user names in the filter combobox.
        """

        try:
            users = database.get_user_names()

            values = ["All Users"] + users

            self.user_combo["values"] = values

            if self.history_user_var.get() not in values:
                self.history_user_var.set("All Users")

        except RuntimeError as error:
            self.status_var.set(
                f"Database error: {error}"
            )

    # ---------------------------------------------------------
    # REFRESH HISTORY
    # ---------------------------------------------------------

    def refresh_history(self):
        """
        Refresh the history table.
        """

        if not hasattr(self, "history_tree"):
            return

        for item in self.history_tree.get_children():
            self.history_tree.delete(item)

        selected_user = self.history_user_var.get()

        if selected_user == "All Users":
            selected_user = None

        try:
            records = database.get_records(
                selected_user
            )

            for record in records:

                record_id = record[0]
                name = record[1]
                weight = record[2]
                height = record[3]
                bmi = record[4]
                category = record[5]
                recorded_at = record[6]

                self.history_tree.insert(
                    "",
                    "end",
                    values=(
                        record_id,
                        name,
                        f"{weight:.2f}",
                        f"{height:.2f}",
                        f"{bmi:.2f}",
                        category,
                        recorded_at
                    )
                )

        except RuntimeError as error:

            self.status_var.set(
                f"Database error: {error}"
            )

    # ---------------------------------------------------------
    # DELETE RECORD
    # ---------------------------------------------------------

    def delete_selected(self):
        """
        Delete selected history records.
        """

        selected_items = self.history_tree.selection()

        if not selected_items:
            messagebox.showwarning(
                "No Selection",
                "Please select at least one record to delete."
            )
            return

        confirm = messagebox.askyesno(
            "Confirm Delete",
            "Are you sure you want to delete the selected record(s)?"
        )

        if not confirm:
            return

        try:

            for item in selected_items:

                values = self.history_tree.item(
                    item,
                    "values"
                )

                record_id = values[0]

                database.delete_record(
                    int(record_id)
                )

            self.refresh_history()
            self.refresh_users()

            self.status_var.set(
                "Selected record(s) deleted successfully."
            )

        except (RuntimeError, ValueError) as error:

            messagebox.showerror(
                "Delete Error",
                str(error)
            )

    # ---------------------------------------------------------
    # BMI TREND
    # ---------------------------------------------------------

    def show_trend(self):
        """
        Display BMI trend chart for the selected user.
        """

        selected_user = self.history_user_var.get()

        if selected_user == "All Users":
            messagebox.showwarning(
                "Select User",
                "Please select a specific user to view the BMI trend."
            )
            return

        try:
            records = database.get_records(
                selected_user
            )

        except RuntimeError as error:

            messagebox.showerror(
                "Database Error",
                str(error)
            )
            return

        if not records:
            messagebox.showinfo(
                "No Data",
                "There are no BMI records for this user."
            )
            return

        # Records are newest first, so reverse them
        records = list(reversed(records))

        dates = [
            record[6]
            for record in records
        ]

        bmi_values = [
            record[4]
            for record in records
        ]

        graph_window = tk.Toplevel(
            self.root
        )

        graph_window.title(
            f"BMI Trend - {selected_user}"
        )

        graph_window.geometry(
            "850x600"
        )

        graph_window.configure(
            bg="white"
        )

        title = tk.Label(
            graph_window,
            text=f"BMI Trend for {selected_user}",
            bg="white",
            fg="#2C3E50",
            font=("Segoe UI", 18, "bold")
        )

        title.pack(
            pady=15
        )

        figure = Figure(
            figsize=(8, 5),
            dpi=100
        )

        axis = figure.add_subplot(111)

        axis.plot(
            dates,
            bmi_values,
            marker="o",
            linewidth=2,
            label="BMI"
        )

        axis.axhline(
            y=18.5,
            linestyle="--",
            linewidth=1,
            label="Underweight Limit"
        )

        axis.axhline(
            y=25,
            linestyle="--",
            linewidth=1,
            label="Normal Limit"
        )

        axis.axhline(
            y=30,
            linestyle="--",
            linewidth=1,
            label="Obese Limit"
        )

        axis.set_title(
            "BMI Progress Over Time"
        )

        axis.set_xlabel(
            "Date & Time"
        )

        axis.set_ylabel(
            "BMI"
        )

        axis.grid(
            True,
            alpha=0.3
        )

        axis.legend()

        figure.autofmt_xdate()

        figure.tight_layout()

        canvas = FigureCanvasTkAgg(
            figure,
            master=graph_window
        )

        canvas.draw()

        canvas.get_tk_widget().pack(
            fill="both",
            expand=True,
            padx=20,
            pady=(0, 20)
        )

    # ---------------------------------------------------------
    # FOOTER
    # ---------------------------------------------------------

    def create_footer(self):
        """
        Create application footer.
        """

        footer = tk.Frame(
            self.root,
            bg="#2C3E50",
            height=35
        )

        footer.pack(
            fill="x"
        )

        footer.pack_propagate(False)

        status_label = tk.Label(
            footer,
            textvariable=self.status_var,
            bg="#2C3E50",
            fg="white",
            font=("Segoe UI", 9)
        )

        status_label.pack(
            side="left",
            padx=15
        )

        copyright_label = tk.Label(
            footer,
            text="OASIS INFOBYTE | Python Programming Internship | Task 2",
            bg="#2C3E50",
            fg="#D5DBDB",
            font=("Segoe UI", 9)
        )

        copyright_label.pack(
            side="right",
            padx=15
        )


# -------------------------------------------------------------
# APPLICATION START
# -------------------------------------------------------------

if __name__ == "__main__":

    root = tk.Tk()

    app = BMICalculatorApp(
        root
    )

    root.mainloop()