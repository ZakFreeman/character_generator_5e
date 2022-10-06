import tkinter as Tk
from tkinter import IntVar
from tkinter.ttk import Frame, Checkbutton
class TestGui(Frame):
  def __init__(self, parent):
      Frame.__init__(self, parent)

      self.var1 = IntVar()
      self.var1.set(0)
      button = Checkbutton(parent,
          text="Pick me, pick me!",
          variable=self.var1)
      button.grid()

root = Tk.Tk()
app = TestGui(root)
root.mainloop()