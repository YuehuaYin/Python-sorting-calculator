#Yuehua Yin 2022
#This is a sorting caluclator I am making in python using tkinter. This is my first proper project using tkinter aside from following tutorials online and short tests.
#The user can enter a list of numbers and click a button to select how the numbers should be sorted. Each step of the sorting is displayed along with number total steps.
#CURRENT SORTING ALGORITHMS AVAILABLE: bubble sort, insertion sort

from tkinter import *
from tkinter import scrolledtext

#set up window
root = Tk()
root.title("Sorting calculator")

#frames for layout
left_frame = LabelFrame(root)
left_frame.grid(column = 0, row = 0)

button_frame = LabelFrame(root)
button_frame.grid(column = 1, row = 0)

#label with instructions for entering numbers
enter_label = Label(left_frame, text = "Enter numbers below seperated by a comma: ", font = ("Impact", 22))
enter_label.grid(row = 0)

#entry box for user to enter numbers
enter = Entry(left_frame, width = 50, font = ("Arial", 15))
enter.grid(row = 1)

#set up scrolltext widget
scrolltxt = scrolledtext.ScrolledText(left_frame, wrap=WORD, width=53, height=15, font = ("Times New Roman", 15))
scrolltxt.grid(row = 2)
scrolltxt.configure(state='disabled')

#set up step count label
steps_label = Label(left_frame, text = "Step count for sort goes here!", font = ("Arial", 15))
steps_label.grid(row = 3)

#bubble sort function
def bubble_sort():

    #delete and enable scrolltxt
    scrolltxt.configure(state='normal')
    scrolltxt.delete('1.0', END)
    
    #get numbers from entry field
    input = enter.get().split(",")
    #CHANGE IT INTO INT
    input = list(map(int,input))

    #variables
    global steps_label
    s = 0
    n = len(input)
    swapped = True

    #iterate through list and swaps numbers if the current number is greater than the next number
    #once it gets to the end of list it starts again until no more swaps are made
    while swapped:
        swapped = False
        for i in range (0, n - 1):
            scrolltxt.insert("insert", "Compare " + str(input[i]) + " and " + str(input[i + 1]) + "\n")
            s = s + 1
            if input[i] > input[i + 1]:
                swapped = True
                input[i], input[i + 1] = input[i + 1], input[i]
                #label to display step
                scrolltxt.insert("insert", "Swap " + str(input[i + 1]) + " and " + str(input[i]) + ": " + str(input) + "\n")
                s = s + 1

    #label showing how many steps it took to sort
    steps_label.grid_forget()
    steps_label = Label(left_frame, text = "Total steps (comparisons and swaps): " + str(s), font = ("Arial", 15))
    steps_label.grid(row = 3)

    #disable scrolltxt
    scrolltxt.configure(state='disabled')

#insertion sort function
def insertion_sort():

    #clear and enable scrolltxt
    scrolltxt.configure(state='normal')
    scrolltxt.delete('1.0', END)

    #get numbers from entry field
    input = enter.get().split(",")
    #CHANGE IT INTO INT
    input = list(map(int,input))

    #variables
    global steps_label
    s = 0
    n = len(input)

    #Insert numbers into sorted array one at a time by comparing each value to sorted array and inserting into correct position
    for i in range (1, n):
        key = input[i]
        j = i - 1
        while j >= 0 and input[j] > key:
            scrolltxt.insert("insert", "Compare " + str(key) + " and " + str(input[j]) + "\n")
            s = s + 1
            input[j + 1] = input[j]
            j = j - 1
        scrolltxt.insert("insert", "Compare " + str(key) + " to " + str(input[j]) + "\n")
        s = s + 1
        input[j + 1] = key
        scrolltxt.insert("insert", "Insert " + str(input[j+1]) + " after " + str(input[j]) + ": " + str(input) + "\n")
        s = s + 1

    #label showing how many steps it took to sort
    steps_label.grid_forget()
    steps_label = Label(left_frame, text = "Total steps (comparisons and insertions): " + str(s), font = ("Arial", 15))
    steps_label.grid(row = 3)

    #disable scrolltxt
    scrolltxt.configure(state='disabled')

#label for buttons
button_label = Label(button_frame, text = "Select algorithm:", font = ("Impact", 20))
button_label.grid(row = 0)

#buttons
button = Button(button_frame, text = "Bubble sort", font = ("Arial", 16), command = bubble_sort)
button.grid(row = 1, padx=25, pady=5)

button = Button(button_frame, text = "Insertion sort", font = ("Arial", 16), command = insertion_sort)
button.grid(row = 2, padx= 25, pady=5)

#run program
root.mainloop()
