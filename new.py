from tkinter import *
import requests
from bs4 import BeautifulSoup

root = Tk()
root.geometry("900x300")
root.configure(bg="light blue")
root.title("Live Cricket Score")


def show_score():
    url = "https://www.cricbuzz.com/"

    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")

    div = soup.findAll("ul",class_="videos-carousal-wrapper")[0].get_text()
    final_text = div.strip().split("  ")[0]
    var.set(final_text)


Label(root, text="Cricket Score", font=("Arial", 28, "bold"), bg="lightblue", fg="red").pack(pady=10)
Button(root, text="Check Score", command=show_score).pack(pady=10)

status = StringVar()
Label(root, textvariable=status, bg="white", fg="black").pack(side = BOTTOM, fill="both")
status.set("Status: Running")


var = StringVar()
score_board = Label(root, textvariable=var, font=("Comic sans ms", 15), bg="lightblue")
score_board.pack()


root.mainloop()
