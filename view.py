import tkinter as tk
import ttkbootstrap as ttk
from sent import get_sentiment
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
class MainWindow(ttk.Window):
    def __init__(self):
        super(MainWindow, self).__init__(themename="lumen")

        self.current_sentence = ttk.StringVar(value="")
        self.entry = ttk.Entry(master=self, textvariable=self.current_sentence)
        ttk.Label(master=self, text="Sentiment analisys app", font=("Arial", 12, "bold")).place(x=400, y = 10, anchor="center")
        self.entry.place(x = 100, y = 50, height = 50, width=600)
        self.button = ttk.Button(master=self, command=self.print_sentiment, text="Get sentiment")
        self.button.place(x = 300, y = 200, height = 40, width = 200)
        self.show()
    def show(self) -> None:
        self.title("Sentiment analisys")
        self.resizable(width=False, height=False)
        self.geometry("800x800")
        self.attributes("-topmost", True)
        self.update()
        self.attributes("-topmost", False)
        self.place_window_center()
        self.mainloop()
        
    def print_sentiment(self):
        fig = Figure(figsize=(4,4))
        ax = fig.add_subplot(111)
        values = get_sentiment(self.current_sentence.get())
        labels=["positive", "negative", "neutral"]
        labels = [labels[i] for i in range(len(values)) if values[i] > 0]
        values = [value for value in values if value > 0]
        
        ax.pie(values, labels=labels, autopct='%1.1f%%')
        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas.get_tk_widget().place(x = 200, y = 300)
        canvas.draw()
if __name__ == "__main__":
    MainWindow()