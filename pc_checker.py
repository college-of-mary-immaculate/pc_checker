from tkinter import filedialog, scrolledtext, messagebox, simpledialog
import tkinter as tk

class WidgetGenerator:
    @staticmethod
    def create_label(master, text=None, bg=None, width=None, height=None, fg=None, font=None, grid=None, pack=None, place=None):
        label = tk.Label(master, text=text, bg=bg, fg=fg, width=width, height=height, font=font)
        WidgetGenerator.set_geometry_manager(label, pack=pack, grid=grid, place=place)
        return label

    @staticmethod
    def create_button(master, text=None, font=None, width=None, bg=None, fg=None, command=None, grid=None, pack=None, place=None, state=None, image=None):
        button = tk.Button(master, text=text, font=font, width=width, bg=bg, fg=fg, state=state, command=command, image=image, compound=tk.LEFT)
        WidgetGenerator.set_geometry_manager(button, pack=pack, grid=grid, place=place)
        return button

    @staticmethod
    def create_entry(master, font=None, show=None, state=None, width=None, grid=None, pack=None, place=None):
        entry = tk.Entry(master, font=font, state=state, show=show, width=width)
        WidgetGenerator.set_geometry_manager(entry, pack=pack, grid=grid, place=place)
        return entry

    @staticmethod
    def create_listbox(master, width=None, height=None, font=None, grid=None, pack=None, place=None):
        listbox = tk.Listbox(master, width=width, height=height, font=font)
        WidgetGenerator.set_geometry_manager(listbox, pack=pack, grid=grid, place=place)
        return listbox

    @staticmethod
    def create_frame(master, width=None, height=None, bg=None, bd=None, relief=None, grid=None, pack=None, place=None):
        frame = tk.Frame(master, width=width, height=height, bg=bg, bd=bd, relief=relief)
        WidgetGenerator.set_geometry_manager(frame, pack=pack, grid=grid, place=place)
        return frame

    @staticmethod
    def set_geometry_manager(widget, pack=None, grid=None, place=None):
        if pack:
            widget.pack(**pack)
        elif grid:
            widget.grid(**grid)
        elif place:
            widget.place(**place)
        else:
            widget.pack()

class DifferenceCheckerApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.header_frame = None
        self.main_frame = None
        self.result_window = None

        self.__configure_window()
        self.show_menu()
        self.show_homepage()

    def show_homepage(self):
        if self.main_frame:
            self.main_frame.destroy()
        self.show_header()

        self.main_frame = WidgetGenerator.create_frame(self, width=800, height=600, pack={'fill': 'both', 'expand': True}, bg="#f2f2f2", bd=5, relief=tk.SUNKEN)
        self.main_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.text1_frame = WidgetGenerator.create_frame(self.main_frame, grid={'row': 0, 'column': 0, 'padx': 20, 'pady': 10}, bg="#f2f2f2")
        self.label1 = WidgetGenerator.create_label(self.text1_frame, text="Text 1:", grid={'row': 0, 'column': 0, 'ipadx': 20}, fg="#333333", bg="#f2f2f2", font=('Helvetica', 14, 'bold'))
        self.browse_text1 = WidgetGenerator.create_button(self.text1_frame, bg="#333333", fg="white", text="Browse...", command=self.browse_file1, grid={'row': 0, 'column': 1, 'padx': 10})
        self.text1 = scrolledtext.ScrolledText(self.text1_frame, wrap=tk.WORD, width=50, height=10, bg="#ffffff", fg="#333333", insertbackground="#333333", font=('Helvetica', 12))
        self.text1.grid(row=1, column=0, columnspan=2, pady=10)

        self.text2_frame = WidgetGenerator.create_frame(self.main_frame, grid={'row': 0, 'column': 1, 'padx': 20, 'pady': 10}, bg="#f2f2f2")
        self.label2 = WidgetGenerator.create_label(self.text2_frame, text="Text 2:", grid={'row': 0, 'column': 0, 'ipadx': 20}, fg="#333333", bg="#f2f2f2", font=('Helvetica', 14, 'bold'))
        self.browse_text2 = WidgetGenerator.create_button(self.text2_frame, bg="#333333", fg="white", text="Browse...", command=self.browse_file2, grid={'row': 0, 'column': 1, 'padx': 10})
        self.text2 = scrolledtext.ScrolledText(self.text2_frame, wrap=tk.WORD, width=50, height=10, bg="#ffffff", fg="#333333", insertbackground="#333333", font=('Helvetica', 12))
        self.text2.grid(row=1, column=0, columnspan=2, pady=10)

        self.compare_button = WidgetGenerator.create_button(self.main_frame, width=20, bg="#333333", fg="white", font=('Helvetica', 14, 'bold'), text="Compare", command=self.show_result, grid={'row': 1, 'column': 0, 'columnspan': 2, 'pady': 20})

    def show_result(self):
        if self.result_window:
            self.result_window.destroy()

        self.result_window = tk.Toplevel(self, background="#f2f2f2")
        self.result = WidgetGenerator.create_frame(self.result_window, width=800, height=600, pack={'fill': 'both', 'expand': True}, bg="#f2f2f2", bd=5, relief=tk.SUNKEN)
        #self.result.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.result_frame1 = WidgetGenerator.create_frame(self.result, grid={'row': 0, 'column': 0, 'padx': 20, 'pady': 10}, bg="#f2f2f2")
        WidgetGenerator.create_button(self.result, bg="#333333", fg="white", text="Merge Change >", command=lambda:[self.merge_change('left')], place={'x': 280, 'y': 5})
        self.result_text1 = scrolledtext.ScrolledText(self.result_frame1, wrap=tk.WORD, width=50, height=10, state=tk.DISABLED, bg="#ffffff", fg="#333333", insertbackground="#333333", font=('Helvetica', 12))
        self.result_text1.grid(row=1, column=1)

        self.result_frame2 = WidgetGenerator.create_frame(self.result, grid={'row': 0, 'column': 1, 'padx': 20, 'pady': 10}, bg="#f2f2f2")
        WidgetGenerator.create_button(self.result, bg="#333333", fg="white", text="< Merge Change", command=lambda:[self.merge_change('right')], place={'x': 780, 'y': 5})
        self.result_text2 = scrolledtext.ScrolledText(self.result_frame2, wrap=tk.WORD, width=50, height=10, state=tk.DISABLED, bg="#ffffff", fg="#333333", insertbackground="#333333", font=('Helvetica', 12))
        self.result_text2.grid(row=1, column=1)

        self.compare_texts()
    
    def merge_change(self, text):
        if text == 'left':
            self.text2.delete('1.0', tk.END)
            self.text2.insert('1.0', self.text1.get('1.0', tk.END))

            self.compare_texts()
        
        if text == 'right':
            self.text1.delete('1.0', tk.END)
            self.text1.insert('1.0', self.text2.get('1.0', tk.END))

            self.compare_texts()

    def browse_file1(self):
        file_path = filedialog.askopenfilename()
        content = self.reader1(file_path)
        if content is not None:
            self.text1.delete('1.0', tk.END)
            self.text1.insert('1.0', content)

    def browse_file2(self):
        file_path = filedialog.askopenfilename()
        content = self.reader2(file_path)
        if content is not None:
            self.text2.delete('1.0', tk.END)
            self.text2.insert('1.0', content)

    def reader1(self, file_path):
        try:
            with open(file_path, 'r') as file:
                content = file.read()
            return content
        except FileNotFoundError:
            res = messagebox.askretrycancel('', "File not Found!")
            if res:
                self.browse_file1()
            return None
        
    def reader2(self, file_path):
        try:
            with open(file_path, 'r') as file:
                content = file.read()
            return content
        except FileNotFoundError:
            res = messagebox.askretrycancel('', "File not Found!")
            if res:
                self.browse_file2()
            return None

    def levenshtein_distance(self, s1, s2):
        if len(s1) < len(s2):
            return self.levenshtein_distance(s2, s1)
        if len(s2) == 0:
            return len(s1)
        previous_row = range(len(s2) + 1)
        for i, c1 in enumerate(s1):
            current_row = [i + 1]
            for j, c2 in enumerate(s2):
                insertions = previous_row[j + 1] + 1
                deletions = current_row[j] + 1
                substitutions = previous_row[j] + (c1 != c2)
                current_row.append(min(insertions, deletions, substitutions))
            previous_row = current_row
        return previous_row[-1]

    def compare_texts(self):
        text1 = self.text1.get("1.0", tk.END).strip()
        text2 = self.text2.get("1.0", tk.END).strip()
        if text1 and text2:
            length = max(len(text1), len(text2))
            distance = self.levenshtein_distance(text1, text2)
            sim_distance = f"{(1 - (distance / length)) * 100:.2f}"
            self.highlight_differences(text1, text2, sim_distance)
        
        else:
            self.result_window.destroy()
            if not text1 and not text2:
                messagebox.askokcancel('', 'Enter text in both fields')
            elif not text1:
                messagebox.askokcancel('', 'Enter text in field 1')
            elif not text2:
                messagebox.askokcancel('', 'Enter text in field 2')
            
    def highlight_differences(self, text1, text2, distance):
        self.result_text1.config(state=tk.NORMAL)
        self.result_text1.delete("1.0", tk.END)
        self.result_text2.config(state=tk.NORMAL)
        self.result_text2.delete("1.0", tk.END)
        self.result_text1.insert(tk.END, f"SIMILARITY: {distance}%\n\n", 'distance')
        self.result_text2.insert(tk.END, f"SIMILARITY: {distance}%\n\n", 'distance')
        i = j = 0
        while i < len(text1) and j < len(text2):
            if text1[i] == ' ' or text1[i] != text2[j] or text2[j] == ' ':
                self.result_text1.insert(tk.END, text1[i], 'text1')
                self.result_text2.insert(tk.END, text2[i], 'text2')
            else:
                self.result_text1.insert(tk.END, text1[i], 'match')
                self.result_text2.insert(tk.END, text2[i], 'match')
            i += 1
            j += 1
        while i < len(text1):
            self.result_text1.insert(tk.END, text1[i], 'text1')
            i += 1
        while j < len(text2):
            self.result_text2.insert(tk.END, text2[j], 'text2')
            j += 1
        self.result_text1.tag_config('text1', background='#ffcbbd')
        self.result_text1.tag_config('match', background='#ff9d97')
        self.result_text1.tag_config('distance', font=('Helvetica', 12, 'bold',))
        self.result_text1.tag_config('distance', background= "#f2f2f2")
        self.result_text1.config(state=tk.DISABLED)
        self.result_text2.tag_config('text2', background='#ddf7ee')
        self.result_text2.tag_config('match', background='#80e0bd')
        self.result_text2.tag_config('distance', font=('Helvetica', 12, 'bold',))
        self.result_text2.tag_config('distance', background= "#f2f2f2")
        self.result_text2.config(state=tk.DISABLED)

    def show_header(self):
        if self.header_frame:
            self.header_frame.destroy()
        self.header_frame = WidgetGenerator.create_frame(self, pack={'fill': 'x'}, bg="#333333")
        self.icon = WidgetGenerator.create_label(self.header_frame, bg="#333333", text="PC", font=("Helvetica", 36, "bold"), pack={'side': 'left', 'padx': 20}, fg="#f2f2f2")
        self.header = WidgetGenerator.create_label(self.header_frame, bg="#333333", text="CHECKER", font=("Helvetica", 24, "bold"), pack={'side': 'left', 'padx': 10}, fg="#f2f2f2")

    def about_info(self):
        about_message = "Difference Checker\nVersion 1.0\n\nDevelopers: \nEsmabe, Wilson\nBedaña, Christian Joy\n\nContact us: \nwilsonesmabe2003@gmail.com\nchirtianbedana@gmail.com"
        messagebox.showinfo("About", about_message)

    def show_instruction(self):
        instruction_text = """
        Difference Checker Instructions\n\nWelcome to the Difference Checker app. This advanced tool empowers you to compare two text files with precision and efficiency.\n\nHow to Use:\n1. Navigate to the 'Text 1' section and select your first text file by clicking the 'Browse...' button.\n2. Proceed to the 'Text 2' section and select the second text file in a similar manner.\n3. Once both files are selected, unleash the power of our cutting-edge algorithm by clicking the 'Compare' button.\n4. Behold the magic as the app unveils the differences between the texts, presented with unmatched clarity.\n5. Explore further by utilizing the 'Merge Change' buttons in the result window to integrate modifications seamlessly.\n\nThe different outcomes of the plagiarism detection results, each with its corresponding background color:\n\n1. Upon completion of the plagiarism analysis, if no instances of plagiarism are detected, the result will be displayed as "No plagiarism" \nwith a 0% similarity score. Indicating a pristine and original document devoid of any plagiarized content.\n2. In cases where the similarity score falls within the range of 1% to 25%, the result will be labeled as "Low" similarity. \nSignifying a minimal level of similarity between the submitted content and existing sources, suggesting a low risk of plagiarism.\n3. For similarity scores ranging from 26% to 50%, the result will be categorized as "Mid" similarity. This indicates a moderate level \nof resemblance between the submitted text and other sources. Serving as a cautionary indication of the need for further review and potential citation adjustments.\n4. If the similarity score falls within the range of 51% to 75%, the result will be designated as "Moderate" similarity. This suggests a substantial \ndegree of overlap between the submitted content and existing sources. Highlighting the need for thorough revision and citation to ensure academic integrity.\n5. In instances where the similarity score exceeds 75% and reaches up to 100%, the result will be marked as "Severe" similarity, indicating a significant portion \nof the submitted text matches existing sources. Serving as a warning sign of potential plagiarism and urging immediate attention to rectify and properly attribute sources to maintain academic honesty.\n\nAdditional Information:\n- For a seamless user experience, ensure both files contain text data only.\n- The app's intuitive interface ensures ease of use, empowering users of all skill levels.\n- Experience the future of text comparison with our state-of-the-art Difference Checker.\n\nFor any inquiries or feedback, please contact the developer at Help > About.\n\nThank you for joining us on this journey into the future with Difference Checker!
        """
        simpledialog.askstring('INSTRUCTION', prompt=instruction_text)

    def show_menu(self):
        self.menu_bar = tk.Menu(self)
        file_menu = tk.Menu(self.menu_bar, tearoff=0, bg="#1c1c1c", fg="#ffffff", font=('Segoe UI', 12))
        file_menu.add_command(label="Exit", command=self.destroy)
        help_menu = tk.Menu(self.menu_bar, tearoff=0, bg="#1c1c1c", fg="#ffffff", font=('Segoe UI', 12))
        help_menu.add_command(label="About", command=self.about_info)
        overview_menu = tk.Menu(self.menu_bar, tearoff=0, bg="#1c1c1c", fg="#ffffff", font=('Segoe UI', 12))
        overview_menu.add_command(label="Instruction", command=self.show_instruction)
        self.menu_bar.add_cascade(label="Change", menu=file_menu)
        self.menu_bar.add_cascade(label="Help", menu=help_menu)
        self.menu_bar.add_cascade(label="Overview", menu=overview_menu)
        self.config(menu=self.menu_bar)

    def __configure_window(self):
        self.title("CHECKER")
        self.geometry("1155x600")
        self.config(bg="#f2f2f2")

if __name__ == "__main__":
    app = DifferenceCheckerApp()
    app.mainloop()