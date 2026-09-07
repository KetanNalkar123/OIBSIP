"""
Advanced Random Password Generator
OASIS INFOBYTE - Python Programming Internship
Task 3: Advanced Random Password Generator
"""

import tkinter as tk
from tkinter import ttk, messagebox

import pyperclip

from password_generator import (
    generate_password,
    calculate_password_strength
)


class PasswordGeneratorApp:
    """
    Main GUI application for the Advanced Password Generator.
    """

    def __init__(self, root):
        self.root = root

        self.root.title(
            "Advanced Random Password Generator"
        )

        self.root.geometry(
            "950x720"
        )

        self.root.minsize(
            850,
            650
        )

        self.root.configure(
            bg="#F4F6F7"
        )

        # Last 5 generated passwords
        self.password_history = []

        self.setup_styles()
        self.create_variables()
        self.create_header()
        self.create_main_interface()
        self.create_footer()

    # =========================================================
    # STYLES
    # =========================================================

    def setup_styles(self):
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
            "TNotebook.Tab",
            font=("Segoe UI", 10, "bold"),
            padding=(20, 10)
        )

        style.configure(
            "TScale",
            background="#FFFFFF"
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

    # =========================================================
    # VARIABLES
    # =========================================================

    def create_variables(self):
        """
        Create Tkinter variables.
        """

        self.length_var = tk.IntVar(
            value=16
        )

        self.uppercase_var = tk.BooleanVar(
            value=True
        )

        self.lowercase_var = tk.BooleanVar(
            value=True
        )

        self.digits_var = tk.BooleanVar(
            value=True
        )

        self.special_var = tk.BooleanVar(
            value=True
        )

        self.ambiguous_var = tk.BooleanVar(
            value=False
        )

        self.password_var = tk.StringVar()

        self.strength_var = tk.StringVar(
            value="Strength: --"
        )

        self.strength_description_var = tk.StringVar(
            value="Generate a password to see its strength."
        )

        self.status_var = tk.StringVar(
            value="Ready"
        )

    # =========================================================
    # HEADER
    # =========================================================

    def create_header(self):
        """
        Create application header.
        """

        header = tk.Frame(
            self.root,
            bg="#2C3E50",
            height=95
        )

        header.pack(
            fill="x"
        )

        header.pack_propagate(
            False
        )

        title = tk.Label(
            header,
            text="Advanced Random Password Generator",
            bg="#2C3E50",
            fg="white",
            font=("Segoe UI", 23, "bold")
        )

        title.pack(
            pady=(16, 2)
        )

        subtitle = tk.Label(
            header,
            text=(
                "Generate secure passwords using Python's "
                "cryptographically secure secrets module"
            ),
            bg="#2C3E50",
            fg="#D5DBDB",
            font=("Segoe UI", 10)
        )

        subtitle.pack()

    # =========================================================
    # MAIN INTERFACE
    # =========================================================

    def create_main_interface(self):
        """
        Create the main notebook interface.
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

        self.generator_tab = tk.Frame(
            self.notebook,
            bg="#F4F6F7"
        )

        self.history_tab = tk.Frame(
            self.notebook,
            bg="#F4F6F7"
        )

        self.notebook.add(
            self.generator_tab,
            text="  Password Generator  "
        )

        self.notebook.add(
            self.history_tab,
            text="  Generation History  "
        )

        self.create_generator_tab()
        self.create_history_tab()

    # =========================================================
    # GENERATOR TAB
    # =========================================================

    def create_generator_tab(self):
        """
        Create password generator interface.
        """

        main_frame = tk.Frame(
            self.generator_tab,
            bg="#F4F6F7"
        )

        main_frame.pack(
            fill="both",
            expand=True
        )

        # -----------------------------------------------------
        # LEFT PANEL
        # -----------------------------------------------------

        settings_frame = tk.Frame(
            main_frame,
            bg="white",
            bd=1,
            relief="solid"
        )

        settings_frame.pack(
            side="left",
            fill="both",
            expand=True,
            padx=(10, 5),
            pady=10
        )

        settings_title = tk.Label(
            settings_frame,
            text="Password Settings",
            bg="white",
            fg="#2C3E50",
            font=("Segoe UI", 18, "bold")
        )

        settings_title.pack(
            pady=(25, 20)
        )

        # Length

        length_label = tk.Label(
            settings_frame,
            text="Password Length",
            bg="white",
            fg="#34495E",
            font=("Segoe UI", 11, "bold")
        )

        length_label.pack(
            anchor="w",
            padx=35
        )

        length_frame = tk.Frame(
            settings_frame,
            bg="white"
        )

        length_frame.pack(
            fill="x",
            padx=35,
            pady=(5, 20)
        )

        self.length_scale = ttk.Scale(
            length_frame,
            from_=4,
            to=64,
            orient="horizontal",
            command=self.update_length
        )

        self.length_scale.set(
            self.length_var.get()
        )

        self.length_scale.pack(
            side="left",
            fill="x",
            expand=True
        )

        self.length_display = tk.Label(
            length_frame,
            text="16",
            bg="#ECF0F1",
            fg="#2C3E50",
            font=("Segoe UI", 11, "bold"),
            width=5
        )

        self.length_display.pack(
            side="right",
            padx=(10, 0)
        )

        # Character types

        character_title = tk.Label(
            settings_frame,
            text="Character Types",
            bg="white",
            fg="#34495E",
            font=("Segoe UI", 11, "bold")
        )

        character_title.pack(
            anchor="w",
            padx=35,
            pady=(5, 10)
        )

        self.uppercase_check = ttk.Checkbutton(
            settings_frame,
            text="Uppercase Letters (A-Z)",
            variable=self.uppercase_var
        )

        self.uppercase_check.pack(
            anchor="w",
            padx=50,
            pady=4
        )

        self.lowercase_check = ttk.Checkbutton(
            settings_frame,
            text="Lowercase Letters (a-z)",
            variable=self.lowercase_var
        )

        self.lowercase_check.pack(
            anchor="w",
            padx=50,
            pady=4
        )

        self.digits_check = ttk.Checkbutton(
            settings_frame,
            text="Numbers (0-9)",
            variable=self.digits_var
        )

        self.digits_check.pack(
            anchor="w",
            padx=50,
            pady=4
        )

        self.special_check = ttk.Checkbutton(
            settings_frame,
            text="Special Characters (!@#$...)",
            variable=self.special_var
        )

        self.special_check.pack(
            anchor="w",
            padx=50,
            pady=4
        )

        # Ambiguous characters

        ambiguous_check = ttk.Checkbutton(
            settings_frame,
            text="Exclude ambiguous characters (I, l, 1, O, 0, o)",
            variable=self.ambiguous_var
        )

        ambiguous_check.pack(
            anchor="w",
            padx=50,
            pady=(15, 5)
        )

        # Generate button

        generate_button = tk.Button(
            settings_frame,
            text="Generate Secure Password",
            command=self.generate_password_action,
            bg="#27AE60",
            fg="white",
            activebackground="#229954",
            activeforeground="white",
            font=("Segoe UI", 11, "bold"),
            padx=20,
            pady=11,
            relief="flat",
            cursor="hand2"
        )

        generate_button.pack(
            pady=(25, 10)
        )

        # -----------------------------------------------------
        # RIGHT PANEL
        # -----------------------------------------------------

        result_frame = tk.Frame(
            main_frame,
            bg="white",
            bd=1,
            relief="solid"
        )

        result_frame.pack(
            side="right",
            fill="both",
            expand=True,
            padx=(5, 10),
            pady=10
        )

        result_title = tk.Label(
            result_frame,
            text="Generated Password",
            bg="white",
            fg="#2C3E50",
            font=("Segoe UI", 18, "bold")
        )

        result_title.pack(
            pady=(25, 20)
        )

        # Password display

        password_display_frame = tk.Frame(
            result_frame,
            bg="#ECF0F1",
            bd=1,
            relief="solid"
        )

        password_display_frame.pack(
            fill="x",
            padx=30,
            pady=10
        )

        self.password_entry = tk.Entry(
            password_display_frame,
            textvariable=self.password_var,
            font=("Consolas", 13, "bold"),
            bg="#ECF0F1",
            fg="#2C3E50",
            relief="flat",
            justify="center"
        )

        self.password_entry.pack(
            fill="x",
            padx=15,
            pady=18
        )

        # Copy button

        copy_button = tk.Button(
            result_frame,
            text="Copy Password",
            command=self.copy_password,
            bg="#3498DB",
            fg="white",
            activebackground="#2980B9",
            activeforeground="white",
            font=("Segoe UI", 10, "bold"),
            padx=25,
            pady=9,
            relief="flat",
            cursor="hand2"
        )

        copy_button.pack(
            pady=8
        )

        # Strength section

        strength_title = tk.Label(
            result_frame,
            text="Password Strength",
            bg="white",
            fg="#2C3E50",
            font=("Segoe UI", 13, "bold")
        )

        strength_title.pack(
            pady=(20, 8)
        )

        self.strength_label = tk.Label(
            result_frame,
            textvariable=self.strength_var,
            bg="white",
            fg="#7F8C8D",
            font=("Segoe UI", 16, "bold")
        )

        self.strength_label.pack()

        self.strength_description = tk.Label(
            result_frame,
            textvariable=self.strength_description_var,
            bg="white",
            fg="#7F8C8D",
            font=("Segoe UI", 9),
            wraplength=350,
            justify="center"
        )

        self.strength_description.pack(
            pady=(5, 15)
        )

        # Security information

        security_info = tk.Label(
            result_frame,
            text=(
                "Security:\n"
                "Passwords are generated using Python's\n"
                "cryptographically secure 'secrets' module.\n\n"
                "Generated passwords are kept only in memory\n"
                "during the current application session."
            ),
            bg="white",
            fg="#7F8C8D",
            font=("Segoe UI", 9),
            justify="center"
        )

        security_info.pack(
            pady=10
        )

    # =========================================================
    # LENGTH
    # =========================================================

    def update_length(self, value):
        """
        Update password length display.
        """

        length = int(float(value))

        self.length_var.set(
            length
        )

        self.length_display.configure(
            text=str(length)
        )

    # =========================================================
    # GENERATE PASSWORD
    # =========================================================

    def generate_password_action(self):
        """
        Generate a password based on selected options.
        """

        length = self.length_var.get()

        use_uppercase = self.uppercase_var.get()
        use_lowercase = self.lowercase_var.get()
        use_digits = self.digits_var.get()
        use_special = self.special_var.get()
        exclude_ambiguous = self.ambiguous_var.get()

        try:

            password = generate_password(
                length=length,
                use_uppercase=use_uppercase,
                use_lowercase=use_lowercase,
                use_digits=use_digits,
                use_special=use_special,
                exclude_ambiguous=exclude_ambiguous
            )

        except ValueError as error:

            messagebox.showwarning(
                "Invalid Settings",
                str(error)
            )

            return

        self.password_var.set(
            password
        )

        self.password_entry.selection_range(
            0,
            tk.END
        )

        self.update_strength(
            password
        )

        # Add password to session history
        self.password_history.insert(
            0,
            password
        )

        # Keep only last five
        self.password_history = (
            self.password_history[:5]
        )

        self.refresh_history()

        self.status_var.set(
            "Secure password generated successfully."
        )

    # =========================================================
    # STRENGTH
    # =========================================================

    def update_strength(self, password):
        """
        Update password strength display.
        """

        selected_count = sum(
            [
                self.uppercase_var.get(),
                self.lowercase_var.get(),
                self.digits_var.get(),
                self.special_var.get()
            ]
        )

        strength, score, description = (
            calculate_password_strength(
                password,
                selected_count
            )
        )

        self.strength_var.set(
            f"Strength: {strength}"
        )

        self.strength_description_var.set(
            description
        )

        if strength == "Weak":
            self.strength_label.configure(
                fg="#E74C3C"
            )

        elif strength == "Medium":
            self.strength_label.configure(
                fg="#F39C12"
            )

        elif strength == "Strong":
            self.strength_label.configure(
                fg="#27AE60"
            )

        else:
            self.strength_label.configure(
                fg="#7F8C8D"
            )

    # =========================================================
    # COPY
    # =========================================================

    def copy_password(self):
        """
        Copy generated password to clipboard.
        """

        password = self.password_var.get()

        if not password:
            messagebox.showwarning(
                "No Password",
                "Please generate a password first."
            )

            return

        try:

            pyperclip.copy(
                password
            )

            self.status_var.set(
                "Password copied to clipboard."
            )

            messagebox.showinfo(
                "Copied",
                "Password copied to clipboard successfully."
            )

        except Exception as error:

            messagebox.showerror(
                "Clipboard Error",
                f"Unable to copy password: {error}"
            )

    # =========================================================
    # HISTORY TAB
    # =========================================================

    def create_history_tab(self):
        """
        Create session history interface.
        """

        main_frame = tk.Frame(
            self.history_tab,
            bg="#F4F6F7"
        )

        main_frame.pack(
            fill="both",
            expand=True
        )

        top_frame = tk.Frame(
            main_frame,
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
            text="Last 5 Generated Passwords",
            bg="white",
            fg="#2C3E50",
            font=("Segoe UI", 18, "bold")
        )

        title.pack(
            side="left",
            padx=20,
            pady=15
        )

        clear_button = ttk.Button(
            top_frame,
            text="Clear History",
            command=self.clear_history
        )

        clear_button.pack(
            side="right",
            padx=20
        )

        # Table

        table_frame = tk.Frame(
            main_frame,
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
            "number",
            "password",
            "length",
            "strength"
        )

        self.history_tree = ttk.Treeview(
            table_frame,
            columns=columns,
            show="headings"
        )

        self.history_tree.heading(
            "number",
            text="#"
        )

        self.history_tree.heading(
            "password",
            text="Generated Password"
        )

        self.history_tree.heading(
            "length",
            text="Length"
        )

        self.history_tree.heading(
            "strength",
            text="Strength"
        )

        self.history_tree.column(
            "number",
            width=60,
            anchor="center"
        )

        self.history_tree.column(
            "password",
            width=500,
            anchor="center"
        )

        self.history_tree.column(
            "length",
            width=100,
            anchor="center"
        )

        self.history_tree.column(
            "strength",
            width=150,
            anchor="center"
        )

        scrollbar = ttk.Scrollbar(
            table_frame,
            orient="vertical",
            command=self.history_tree.yview
        )

        self.history_tree.configure(
            yscrollcommand=scrollbar.set
        )

        self.history_tree.pack(
            side="left",
            fill="both",
            expand=True
        )

        scrollbar.pack(
            side="right",
            fill="y"
        )

        # Information

        info = tk.Label(
            main_frame,
            text=(
                "Privacy: Password history exists only during "
                "the current application session and is never "
                "saved to a file or database."
            ),
            bg="#F4F6F7",
            fg="#7F8C8D",
            font=("Segoe UI", 9)
        )

        info.pack(
            pady=(5, 10)
        )

    # =========================================================
    # REFRESH HISTORY
    # =========================================================

    def refresh_history(self):
        """
        Refresh password history table.
        """

        if not hasattr(
            self,
            "history_tree"
        ):
            return

        for item in self.history_tree.get_children():
            self.history_tree.delete(
                item
            )

        for index, password in enumerate(
            self.password_history,
            start=1
        ):

            strength, _, _ = (
                calculate_password_strength(
                    password
                )
            )

            self.history_tree.insert(
                "",
                "end",
                values=(
                    index,
                    password,
                    len(password),
                    strength
                )
            )

    # =========================================================
    # CLEAR HISTORY
    # =========================================================

    def clear_history(self):
        """
        Clear password history from memory.
        """

        if not self.password_history:
            messagebox.showinfo(
                "History Empty",
                "There is no password history to clear."
            )

            return

        confirm = messagebox.askyesno(
            "Clear History",
            "Are you sure you want to clear the password history?"
        )

        if not confirm:
            return

        self.password_history.clear()

        self.refresh_history()

        self.status_var.set(
            "Password history cleared."
        )

    # =========================================================
    # FOOTER
    # =========================================================

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

        footer.pack_propagate(
            False
        )

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

        internship_label = tk.Label(
            footer,
            text=(
                "OASIS INFOBYTE | Python Programming "
                "Internship | Task 3"
            ),
            bg="#2C3E50",
            fg="#D5DBDB",
            font=("Segoe UI", 9)
        )

        internship_label.pack(
            side="right",
            padx=15
        )


# =============================================================
# APPLICATION START
# =============================================================

if __name__ == "__main__":

    root = tk.Tk()

    app = PasswordGeneratorApp(
        root
    )

    root.mainloop()