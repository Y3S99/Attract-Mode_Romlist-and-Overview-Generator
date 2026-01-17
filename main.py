import customtkinter as ctk
from tkinter import filedialog
from romlist import genrate_rom
from overview import genrate_overview

def open_file(var):
    file_path = filedialog.askopenfilename(
        title="Select a file",
        filetypes=[("XML files", "*.xml"), ("All files", "*.*")]
    )
    if file_path:
        log("XML File Path:"+file_path)
        var.set(file_path)

def pick_folder(var):
    folder = filedialog.askdirectory(title="Select Folder")
    if folder:
        log("Output Folder Path:"+folder)
        var.set(folder)


def genrom():
    emu=emu_var.get().strip()
    file=path_var.get().strip()
    out=out_path_var.get().strip()
    if not out:
        log("Output Folder Not Selected")
        return
    genrate_rom(file,emu,out,log)

def genov():
    file=tab2_path_var.get().strip()
    out=tab2_out_path_var.get().strip()
    if not out:
        log("Output Folder Not Selected")
        return
    genrate_overview(file,out,log)

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("550x420")

tabview = ctk.CTkTabview(app)
tabview.pack(fill="both", expand=True, padx=10, pady=10)

tab1 = tabview.add("Gamelist.xml to romlist")
tab2 = tabview.add("Gamelist.xml to Overview")

# ---------- TAB 1 LAYOUT ----------

ctk.CTkLabel(
    tab1,
    text="ES gamelist.xml to romlist.txt",
    font=("", 20)
).grid(row=0, column=0, columnspan=3, sticky="w", padx=(10,0), pady=(20, 15))

ctk.CTkLabel(tab1, text="Input Xml file:").grid(
    row=1, column=0, sticky="w", padx=10, pady=5
)
path_var = ctk.StringVar(value="Select a file...")
input_entry=ctk.CTkEntry(tab1,width=300,textvariable=path_var).grid(
    row=1, column=1, sticky="w", padx=5, pady=5
)

open_btn=ctk.CTkButton(tab1,width=50,text="Open",command=lambda: open_file(path_var)).grid(
    row=1, column=2, sticky="w", padx=5, pady=5
)

ctk.CTkLabel(tab1, text="Emulator Name:").grid(
    row=2, column=0, sticky="w", padx=10, pady=10
)

emu_var = ctk.StringVar(value="")
emulatorname_entry=ctk.CTkEntry(tab1,width=300,textvariable=emu_var).grid(
    row=2, column=1, sticky="w", padx=5, pady=5
)

ctk.CTkLabel(tab1, text="Output Location:").grid(
    row=3, column=0, sticky="w", padx=10, pady=5
)
out_path_var = ctk.StringVar(value="")
output_entry=ctk.CTkEntry(tab1,width=300,textvariable=out_path_var).grid(
    row=3, column=1, sticky="w", padx=5, pady=5
)

out_btn=ctk.CTkButton(tab1,width=50,text="Browse",command=lambda: pick_folder(out_path_var)).grid(
    row=3, column=2, sticky="w", padx=5, pady=5
)

genraterom_btn=ctk.CTkButton(tab1,width=100,text="Generate Romlist",command=genrom).grid(
    row=4, column=0, sticky="w", padx=5, pady=(10,0)
)

# ---------- TAB 2 LAYOUT ----------
ctk.CTkLabel(
    tab2,
    text="ES gamelist.xml to overview",
    font=("", 20)
).grid(row=0, column=0, sticky="w", padx=10, pady=20 ,columnspan=3)

ctk.CTkLabel(tab2, text="Input Xml file:").grid(
    row=1, column=0, sticky="w", padx=10, pady=5
)
tab2_path_var = ctk.StringVar(value="Select a file...")
tab2_input_entry=ctk.CTkEntry(tab2,width=300,textvariable=tab2_path_var).grid(
    row=1, column=1, sticky="w", padx=5, pady=5
)

tab2_open_btn=ctk.CTkButton(tab2,width=50,text="Open",command=lambda: open_file(tab2_path_var)).grid(
    row=1, column=2, sticky="w", padx=5, pady=5
)


ctk.CTkLabel(tab2, text="Output Location:").grid(
    row=2, column=0, sticky="w", padx=10, pady=5
)
tab2_out_path_var = ctk.StringVar(value="")
output_entry=ctk.CTkEntry(tab2,width=300,textvariable=tab2_out_path_var).grid(
    row=2, column=1, sticky="w", padx=5, pady=5
)

tab2_out_btn=ctk.CTkButton(tab2,width=50,text="Browse",command=lambda: pick_folder(tab2_out_path_var)).grid(
    row=2, column=2, sticky="w", padx=5, pady=5
)

genrateov_btn=ctk.CTkButton(tab2,width=50,text="Genrate Overview",command=genov).grid(
    row=3, column=0, sticky="w", padx=5, pady=(10,0)
)


log_frame = ctk.CTkFrame(app)
log_frame.pack(fill="both", expand=True, padx=10, pady=10)

log_box = ctk.CTkTextbox(log_frame, height=150)
log_box.pack(fill="both", expand=True)


def log(msg):
    log_box.configure(state="normal")
    log_box.insert("end", msg + "\n")
    log_box.see("end")
    log_box.configure(state="disabled")
log("------------------------------")
log("Application started")
log("Ready...")

app.mainloop()