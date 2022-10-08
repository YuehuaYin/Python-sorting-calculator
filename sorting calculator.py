#Yuehua Yin 2022
#This is a sorting caluclator I am making in python using tkinter. This is my first proper project using tkinter aside from following tutorials online and short tests.
#The user can enter a list of numbers and click a button to select how the numbers should be sorted. Each step of the sorting is displayed along with number total steps.
#CURRENT SORTING ALGORITHMS AVAILABLE: bubble sort, insertion sort, merge sort, merge sort with inerstion sort (uses insertion sort to sort arrays <= 5)

from tkinter import *
from tkinter import scrolledtext
from types import NoneType

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
enter = Entry(left_frame, width = 70, font = ("Arial", 15))
enter.grid(row = 1)

#set up scrolltext widget
scrolltxt = scrolledtext.ScrolledText(left_frame, width=75, height=20, font = ("Times New Roman", 15))
scrolltxt.grid(row = 2)
scrolltxt.configure(state='disabled')

#set up step count label
s = 0
steps_label = Label(left_frame, text = "Step count for sort goes here!", font = ("Arial", 15))
steps_label.grid(row = 3)

#merge sort recursion function
def merge_sort(a):

    #variables
    global s

    if len(a) > 1:
        #split array into halved arrays until array has length one
        mid = len(a)//2
        left = a[:mid]
        right = a[mid:]
        scrolltxt.insert("insert", "\n\nSplit " + str(a) + " into " + str(left) + " and " + str(right))
        s = s + 1
        #recursive call
        merge_sort(left)
        merge_sort(right)
        #merge arrays back into sorted array
        merge(left, right, a)

#merge function
def merge(x, y, a):

    #variables
    global s

    #merge
    i = 0
    j = 0
    k = 0
    scrolltxt.insert("insert", "\n\nMerge " + str(x) + " and " + str(y) + ": ")
    while i < len(x) and j < len(y):
        scrolltxt.insert("insert", "\nCompare " + str(x[i]) + " and " + str(y[j]))
        s = s + 1
        if x[i] < y[j]:
            temp = a[:]
            a[k] = x[i]
            scrolltxt.insert("insert", "\nAdd " + str(x[i]) + " to " + str(temp) + ": " + str(a))
            s = s + 1
            i = i + 1
        else:
            temp = a[:]
            a[k] = y[j]
            scrolltxt.insert("insert", "\nAdd " + str(y[j]) + " to " + str(temp) + ": " + str(a))
            s = s + 1
            j = j + 1
        k = k + 1

    while i < len(x):
        temp = a[:]
        a[k] = x[i]
        scrolltxt.insert("insert", "\nAdd " + str(x[i]) + " to " + str(temp) + ": " + str(a))
        s = s + 1
        i = i + 1
        k = k + 1
    
    while j < len(y):
        temp = a[:]
        a[k] = y[j]
        scrolltxt.insert("insert", "\nAdd " + str(y[j]) + " to " + str(temp) + ": " + str(a))
        s = s + 1
        j = j + 1
        k = k + 1


#insertion sort function
def insertion_sort(a):

    #variables
    global s
    n = len(a)

    for i in range (1, n):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            scrolltxt.insert("insert", "\nCompare " + str(key) + " to " + str(a[j]))
            s = s + 1
            a[j + 1] = a[j]
            j = j - 1
        scrolltxt.insert("insert", "\nCompare " + str(key) + " to " + str(a[j]))
        s = s + 1
        a[j + 1] = key
        scrolltxt.insert("insert", "\nInsert " + str(a[j+1]) + " after " + str(a[j]) + ": " + str(a) + "\n")
        s = s + 1
    
    return a

#merge sort with insertion sort function
def merge_insertion_sort(a):

    #variables
    global s

    #split array into arrays of length 5 (short=good for insertion sort)
    if len(a) > 5:
        #split array into halved arrays
        mid = len(a)//2
        left = a[:mid]
        right = a[mid:]
        scrolltxt.insert("insert", "\n\nSplit " + str(a) + " into " + str(left) + " and " + str(right))
        s = s + 1
        merge_insertion_sort(left)
        merge_insertion_sort(right)
        
        #sorts short arrays using insertion sort
        if len(left) <= 5:
            left = insertion_sort(left)

        if len(right) <= 5:
            right = insertion_sort(right)
        
        #merges sorted arrays
        merge(left, right, a)

#bubble sort button function
def bubble_button():

    #delete and enable scrolltxt
    scrolltxt.configure(state='normal')
    scrolltxt.delete('1.0', END)
    
    #get numbers from entry field
    input = enter.get().split(",")
    #CHANGE IT INTO INT
    input = list(map(int,input))

    #variables
    global steps_label
    global s
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
                scrolltxt.insert("insert", "\nSwap " + str(input[i + 1]) + " and " + str(input[i]) + ": " + str(input) + "\n")
                s = s + 1

    #label showing how many steps it took to sort
    steps_label.grid_forget()
    steps_label = Label(left_frame, text = "Total steps (comparisons and swaps): " + str(s), font = ("Arial", 15))
    steps_label.grid(row = 3)

    #disable scrolltxt
    scrolltxt.configure(state='disabled')

#insertion sort button function
def insertion_button():

    #clear and enable scrolltxt
    scrolltxt.configure(state='normal')
    scrolltxt.delete('1.0', END)

    #get numbers from entry field
    input = enter.get().split(",")
    #CHANGE IT INTO INT
    input = list(map(int,input))

    #variables
    global steps_label
    global s
    s = 0

    #Insert numbers into sorted array one at a time by comparing each value to sorted array and inserting into correct position
    insertion_sort(input)

    #label showing how many steps it took to sort
    steps_label.grid_forget()
    steps_label = Label(left_frame, text = "Total steps (comparisons and insertions): " + str(s), font = ("Arial", 15))
    steps_label.grid(row = 3)

    #disable scrolltxt
    scrolltxt.configure(state='disabled')

#merge sort button function
def merge_button():

    #clear and enable scrolltxt
    scrolltxt.configure(state='normal')
    scrolltxt.delete('1.0', END)

    #get numbers from entry field
    input = enter.get().split(",")
    #CHANGE IT INTO INT
    input = list(map(int,input))

    #variables
    global steps_label
    global s
    s = 0

    #start recursion
    merge_sort(input)

    #label showing how many steps it took to sort
    steps_label.grid_forget()
    steps_label = Label(left_frame, text = "Total steps (splits, comparisons and adds): " + str(s), font = ("Arial", 15))
    steps_label.grid(row = 3)

    #disable scrolltxt
    scrolltxt.configure(state='disabled')

#mergesort with insertion button function
def merge_insertion_button():

    #clear and enable scrolltxt
    scrolltxt.configure(state='normal')
    scrolltxt.delete('1.0', END)

    #get numbers from entry field
    input = enter.get().split(",")
    #CHANGE IT INTO INT
    input = list(map(int,input))

    #variables
    global steps_label
    global s
    s = 0

    #lmao lets give it a shot
    merge_insertion_sort(input)

    #label showing how many steps it took to sort
    steps_label.grid_forget()
    steps_label = Label(left_frame, text = "Total steps (splits, comparisons and adds): " + str(s), font = ("Arial", 15))
    steps_label.grid(row = 3)



def quick_button():
    print("hi")

def quick_insertion_button():
    print("hi")

def radix_button():
    print("hi")

#label for buttons
button_label = Label(button_frame, text = "Select algorithm:", font = ("Impact", 20))
button_label.grid(row = 0)

#buttons
button = Button(button_frame, text = "Bubble sort", font = ("Arial", 16), command = bubble_button)
button.grid(row = 1, padx=25, pady=5)

button = Button(button_frame, text = "Insertion sort", font = ("Arial", 16), command = insertion_button)
button.grid(row = 2, padx= 25, pady=5)

button = Button(button_frame, text = "Merge sort", font = ("Arial", 16), command = merge_button)
button.grid(row = 3, padx= 25, pady=5)

button = Button(button_frame, text = "Merge sort with insertion sort", font = ("Arial", 16), command = merge_insertion_button)
button.grid(row = 4, padx= 25, pady=5)

button = Button(button_frame, text = "Quick sort", font = ("Arial", 16), command = quick_button)
button.grid(row = 5, padx= 25, pady=5)

button = Button(button_frame, text = "Quick sort with insertion sort", font = ("Arial", 16), command = quick_insertion_button)
button.grid(row = 6, padx= 25, pady=5)

button = Button(button_frame, text = "Radix sort", font = ("Arial", 16), command = radix_button)
button.grid(row = 7, padx= 25, pady=5)

#run program
root.mainloop()
