#Yuehua Yin 2022
#This is a sorting caluclator I am making in python using tkinter. This is my first proper project using tkinter aside from following tutorials online and short tests.
#The user can enter a list of numbers and click a button to select how the numbers should be sorted. Each step of the sorting is displayed along with number total steps.
#CURRENT SORTING ALGORITHMS AVAILABLE: bubble sort, insertion sort, merge sort, merge sort with inerstion sort, quick sort, quick sort with insertion sort

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

options_frame = LabelFrame(root)
options_frame.grid(column = 1, row = 1)

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

#checkbox
check = IntVar()
checkbox = Checkbutton(button_frame, text="Print array with every step", font = ("Arial", 16), variable=check)
checkbox.grid(row = 8, padx = 15, pady = 5)

#set up step count label
s = 0
steps_label = Label(left_frame, text = "Step count for sort goes here!", font = ("Arial", 15))
steps_label.grid(row = 3)

#merge sort recursion function
def merge_sort(a):

    #variables
    global s
    global check

    if len(a) > 1:
        #split array into halved arrays until array has length one
        mid = len(a)//2
        left = a[:mid]
        right = a[mid:]
        if check.get() == 0:
            scrolltxt.insert("insert", "\n\nSplit " + str(a))
        elif check.get() == 1:
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
    global check

    #merge
    i = 0
    j = 0
    k = 0
    scrolltxt.insert("insert", "\n\nMerge " + str(x) + " and " + str(y) + ": ")

    #compare first unsorted element of each array with each other
    while i < len(x) and j < len(y):
        scrolltxt.insert("insert", "\nCompare " + str(x[i]) + " and " + str(y[j]))
        s = s + 1
        #choose smallest and put in sorted array first
        if x[i] < y[j]:
            if check.get() == 0:
                scrolltxt.insert("insert", "\nAdd " + str(x[i]))
                a[k] = x[i]
            elif check.get() == 1:
                scrolltxt.insert("insert", "\nAdd " + str(x[i]) + " to " + str(a) + ": ")
                a[k] = x[i]
                scrolltxt.insert("insert", "\n" + str(a))
            s = s + 1
            i = i + 1
        else:
            if check.get() == 0:
                scrolltxt.insert("insert", "\nAdd " + str(y[j]))
                a[k] = y[j]
            elif check.get() == 1:
                scrolltxt.insert("insert", "\nAdd " + str(y[j]) + " to " + str(a) + ": ")
                a[k] = y[j]
                scrolltxt.insert("insert", "\n" + str(a))
            s = s + 1
            j = j + 1
        k = k + 1

    #if at the end of one array, can put numbers in other array in sorted array without worrying about comparing
    while i < len(x):
        if check.get() == 0:
            scrolltxt.insert("insert", "\nAdd " + str(x[i]))
            a[k] = x[i]
        elif check.get() == 1:
            scrolltxt.insert("insert", "\nAdd " + str(x[i]) + " to " + str(a) + ": ")
            a[k] = x[i]
            scrolltxt.insert("insert", "\n" + str(a))
        s = s + 1
        i = i + 1
        k = k + 1
    
    while j < len(y):
        if check.get() == 0:
            scrolltxt.insert("insert", "\nAdd " + str(y[j]))
            a[k] = y[j]
        elif check.get() == 1:
            scrolltxt.insert("insert", "\nAdd " + str(y[j]) + " to " + str(a) + ": ")
            a[k] = y[j]
            scrolltxt.insert("insert", "\n" + str(a))
        s = s + 1
        j = j + 1
        k = k + 1

#insertion sort function
def insertion_sort(a):

    #variables
    global s
    global check
    n = len(a)

    #iterate through all numbers
    for i in range (1, n):
        key = a[i]
        j = i - 1
        #conpare with each number before it
        while j >= 0 and a[j] > key:
            scrolltxt.insert("insert", "\nCompare " + str(key) + " to " + str(a[j]))
            s = s + 1
            a[j + 1] = a[j]
            j = j - 1
        #insert in correct place
        scrolltxt.insert("insert", "\nCompare " + str(key) + " to " + str(a[j]))
        s = s + 1
        a[j + 1] = key
        if check.get() == 0:
            scrolltxt.insert("insert", "\nInsert " + str(a[j+1]) + " after " + str(a[j]) + "\n")
        elif check.get() == 1:
            scrolltxt.insert("insert", "\nInsert " + str(a[j+1]) + " after " + str(a[j]) + ": " + str(a) + "\n")
        s = s + 1
    
    return a

#merge sort with insertion sort function
def merge_insertion_sort(a):

    #variables
    global s
    global check

    #split array into arrays of length 10 (short=good for insertion sort)
    if len(a) > 10:
        #split array into halved arrays
        mid = len(a)//2
        left = a[:mid]
        right = a[mid:]
        if check.get() == 0:
            scrolltxt.insert("insert", "\n\nSplit " + str(a))
        elif check.get() == 1:
            scrolltxt.insert("insert", "\n\nSplit " + str(a) + " into " + str(left) + " and " + str(right))
        s = s + 1

        #recursive function call
        merge_insertion_sort(left)
        merge_insertion_sort(right)
        
        #sorts short arrays using insertion sort
        if len(left) <= 10:
            left = insertion_sort(left)

        if len(right) <= 10:
            right = insertion_sort(right)
        
        #merges sorted arrays
        merge(left, right, a)
    
    else:
        insertion_sort(a)

#function for quick sort and quick sort with insertion sort
def quick_sort(a, b):

    #variables
    global s
    global check

    #check list length to decide what to do
    n = len(a)
    if b == False and n <= 1:
        return a
    #if using insertion sort and less than 10, use insertion sort
    elif b == True and n <= 10:
        return insertion_sort(a)
    else:
        scrolltxt.insert("insert", "\n\nSorting sub-list: " + str(a))
        pivot = a.pop()
        s = s + 1
    
    greater = []
    lesser = []

    scrolltxt.insert("insert", "\nPivot is " + str(pivot))

    for i in a:
        if i > pivot:
            greater.append(i)
            list = lesser + [pivot] + greater
            if check.get() == 0:
                scrolltxt.insert("insert", "\n" + str(i) + " is greater than pivot, add to right side")
            elif check.get() == 1:
                scrolltxt.insert("insert", "\n" + str(i) + " is greater than pivot, add to right side: " + str(list))
            s = s + 1

        else:
            lesser.append(i)
            list = lesser + [pivot] + greater
            if check.get() == 0:
                scrolltxt.insert("insert", "\n" + str(i) + " is less than pivot, add to left side")
            elif check.get() == 1:
                scrolltxt.insert("insert", "\n" + str(i) + " is less than pivot, add to left side: " + str(list))
            s = s + 1

    list = lesser + [pivot] + greater
    scrolltxt.insert("insert", "\n\nMerge to get partitioned sub-list: " + str(list))
    s = s + 1
    return quick_sort(lesser,b) + [pivot] + quick_sort(greater,b)


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
    global check
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
            #swap if current number smaller than next number
            if input[i] > input[i + 1]:
                swapped = True
                input[i], input[i + 1] = input[i + 1], input[i]
                #label to display step
                if check.get() == 0:
                    scrolltxt.insert("insert", "\nSwap " + str(input[i + 1]) + " and " + str(input[i]) + "\n")
                elif check.get() == 1:
                    scrolltxt.insert("insert", "\nSwap " + str(input[i + 1]) + " and " + str(input[i]) + ": " + str(input) + "\n")
                s = s + 1
    
    #print final sorted list
    scrolltxt.insert("insert", "\n\n\nSorted list: " + str(input))

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

    #print final sorted list
    scrolltxt.insert("insert", "\n\n\nSorted list: " + str(input))

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

    #print final sorted list
    scrolltxt.insert("insert", "\n\n\nSorted list: " + str(input))

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

    #print final sorted list
    scrolltxt.insert("insert", "\n\n\nSorted list: " + str(input))

    #label showing how many steps it took to sort
    steps_label.grid_forget()
    steps_label = Label(left_frame, text = "Total steps (splits, comparisons, insertions and adds): " + str(s), font = ("Arial", 15))
    steps_label.grid(row = 3)

    #disable scrolltxt
    scrolltxt.configure(state='disabled')

# button for quicksort
def quick_button():

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

    #call function
    input = quick_sort(input, False)

    #print final sorted list
    scrolltxt.insert("insert", "\n\n\nMerge sorted sub-lists to get sorted list: " + str(input))
    s = s + 1

    #label showing how many steps it took to sort
    steps_label.grid_forget()
    steps_label = Label(left_frame, text = "Total steps (getting pivot, partitioning): " + str(s), font = ("Arial", 15))
    steps_label.grid(row = 3)

    #disable scrolltxt
    scrolltxt.configure(state='disabled')

# button for quicksort
def quick_insertion_button():

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

    #call function
    input = quick_sort(input, True)

    #print final sorted list
    scrolltxt.insert("insert", "\n\n\nMerge sorted sub-lists to get sorted list: " + str(input))
    s = s + 1

    #label showing how many steps it took to sort
    steps_label.grid_forget()
    steps_label = Label(left_frame, text = "Total steps (getting pivot, partitioning, insertions): " + str(s), font = ("Arial", 15))
    steps_label.grid(row = 3)

    #disable scrolltxt
    scrolltxt.configure(state='disabled')

def radix_button():
    print("Not implemented yet, please check back later")

#label for buttons
button_label = Label(button_frame, text = "Select algorithm:", font = ("Impact", 24), pady=10)
button_label.grid(row = 0)

#buttons
button = Button(button_frame, text = "Bubble sort", font = ("Arial", 16), command = bubble_button)
button.grid(row = 1, padx=15, pady=10)

button = Button(button_frame, text = "Insertion sort", font = ("Arial", 16), command = insertion_button)
button.grid(row = 2, padx=15, pady=10)

button = Button(button_frame, text = "Merge sort", font = ("Arial", 16), command = merge_button)
button.grid(row = 3, padx=15, pady=10)

button = Button(button_frame, text = "Merge sort with insertion sort", font = ("Arial", 16), command = merge_insertion_button)
button.grid(row = 4, padx=15, pady=10)

button = Button(button_frame, text = "Quick sort", font = ("Arial", 16), command = quick_button)
button.grid(row = 5, padx=15, pady=10)

button = Button(button_frame, text = "Quick sort with insertion sort", font = ("Arial", 16), command = quick_insertion_button)
button.grid(row = 6, padx=15, pady=10)

button = Button(button_frame, text = "Radix sort", font = ("Arial", 16), command = radix_button)
button.grid(row = 7, padx=15, pady=10)

#run program
root.mainloop()
