import tkinter as tk

root = tk.Tk()
root.config(bg="blue")
root.bind_all("<Button-1>", lambda event: event.widget.focus_set())

frame = tk.Frame(root, bg="red")
frame.pack(fill="both", expand=True, padx=40, pady=40)

entry = tk.Entry(frame)
entry.pack(fill="both", expand=True, padx=40, pady=40)

root.mainloop()