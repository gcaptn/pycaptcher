import tkinter as tk
import tkinter.filedialog


class UI:
    def __init__(self):
        root = tk.Tk()
        root.title("pycaptcher")
        root.attributes("-topmost", True)
        root.geometry("600x360")
        root.wm_attributes("-transparentcolor", root["bg"]) # Transparent background

        topbar = tk.Frame(bg="#373e4d", pady=2, padx=2)

        # Wrap in a frame, so we can size it with pixels
        # Capture button
        b_capture_frame = tk.Frame(master = topbar, height=25, width=25)
        b_capture_frame.pack_propagate(0)
        b_capture = tk.Button(master = b_capture_frame, bg="#50596e", activebackground="#455066",
                              borderwidth=0, text="📷", fg="white", font=("bold", 18))
        b_capture.pack(fill="both", expand=1)
        b_capture_frame.pack(side = tk.RIGHT)

        # Record button
        b_record_frame = tk.Frame(master=topbar, height=25, width=25)
        b_record_frame.pack_propagate(0)
        b_record = tk.Button(master=b_record_frame, bg="#50596e", activebackground="#455066",
                             borderwidth=0, text="⦿", fg="white", font=("bold", 16))
        b_record.pack(fill="both", expand=1)
        b_record_frame.pack(side=tk.RIGHT)

        # File save location entry
        e_filesave_frame = tk.Frame(master=topbar, height=25, width=200)
        e_filesave_frame.pack_propagate(0)
        e_filesave = tk.Entry(master=e_filesave_frame, bg="#50596e", font=("Arial", 10),
                              fg="white", borderwidth=0)
        e_filesave.insert(0, "C:/Users/Administrator/Desktop/pycaptcher")
        e_filesave.pack(fill="both", expand=1)
        e_filesave_frame.pack(side=tk.RIGHT, padx=2)

        # File save dialog button
        b_filesave_frame = tk.Frame(master = topbar, height=25, width=25)
        b_filesave_frame.pack_propagate(0)
        b_filesave = tk.Button(master = b_filesave_frame, bg="#50596e", activebackground="#455066",
                              borderwidth=0, text="🖿", fg="white", font=("bold", 18))
        b_filesave.pack(fill="both", expand=1)
        b_filesave_frame.pack(side = tk.RIGHT)

        # Status text 
        status_var = tk.StringVar()
        status_text_frame = tk.Frame(master=topbar, height=25, width=168,  bg="#373e4d")
        status_text = tk.Label(master=status_text_frame, height=1, font=("Arial", 10),
                               textvariable=status_var, bg="#373e4d", fg="white", justify="left")
        status_var.set("pycaptcher")
        status_text.pack()
        status_text_frame.pack(side=tk.LEFT)

        topbar.pack(fill="x")

        # Border frame to indicate the ends of the border
        border_frame = tk.Frame(master=root, highlightthickness=1, highlightbackground="#373e4d")
        border_frame.pack(fill="both", expand=1)

        self.root = root
        self.b_capture = b_capture
        self.b_record = b_record
        self.b_filesave = b_filesave
        self.e_filesave = e_filesave
        self.status_var = status_var

    def run(self):
        # Bind
        def prompt_file_dialog():
            result = tk.filedialog.askdirectory()
            if len(result.strip()) == 0:
                return
            self.set_filesave(result)
        
        self.b_filesave.configure(command=prompt_file_dialog)
        
        # Main loop
        self.root.mainloop()
    
    def set_lock(self, enabled = True):
        self.root.resizable(width=enabled, height=enabled)
    
    def set_filesave(self, value):
        self.e_filesave.delete(0, "end")
        self.e_filesave.insert(0, value)

    def get_filesave(self):
        return self.e_filesave.get()

    def set_statustext(self, value):
        self.status_var.set(value)

    def set_capture_callback(self, callback):
        self.b_capture.configure(command = callback)

    def set_record_callback(self, callback):
        self.b_record.configure(command = callback)

    def get_bounding_rect(self):
        x, y, width, height = self.root.winfo_rootx(), self.root.winfo_rooty(), self.root.winfo_width(), self.root.winfo_height()
        return x+1, y+30, width-2, height-31 # Crop


if __name__ == "__main__":
    interface = UI()
    interface.run()