#Yuehua Yin - September 2022
#This is a sorting caluclator I am making in python using tkinter. This is my first proper project using tkinter aside from following tutorials online and short tests.
#The user can enter a list of numbers and click a button to select how the numbers should be sorted. Each step of the sorting is displayed along with number total steps.
#CURRENT SORTING ALGORITHMS AVAILABLE: bubble sort

from tkinter import *

#set up window
root = Tk()

#label with instructions for entering numbers
enter_label = Label(root, text = "Enter numbers below seperated by a comma: ")
enter_label.grid(column = 0, row = 0)

#entry box for user to enter numbers
enter = Entry(root, width = 50)
enter.grid(column = 0, row = 1)

#row number to start displaying calculation labels
r = 2

#function for clearing labels
#clears all the labels in column 0 between row 2 and the last value for r
def clear_labels():
    for l in root.grid_slaves():
        if int(l.grid_info()["column"]) == 0:
            if int(l.grid_info()["row"]) >= 2:
                if int(l.grid_info()["row"]) <= r:
                    l.grid_forget()

#bubble sort function
def bubble_sort():

    #clear previous labels
    clear_labels()

    #get numbers from entry field
    input = enter.get().split(",")
    #CHANGE IT INTO INT OMG WHY DID I FORGET ABOUT THAT!!!!!!!!
    input = list(map(int,input))
    print(input)

    #variables
    global r
    r = 2
    n = len(input)
    swapped = True

    #iterate through list and swaps numbers if the current number is greater than the next number
    #once it gets to the end of list it starts again until no more swaps are made
    while swapped:
        swapped = False
        for i in range (0, n - 1):
            if input[i] > input[i + 1]:
                swapped = True
                input[i], input[i + 1] = input[i + 1], input[i]
                print(input)
                label = Label(root, text = "Swapped " + str(input[i + 1]) + " and " + str(input[i]) + ": " + str(input))
                label.grid(column = 0, row = r)
                r = r + 1

    #label showing how many steps it took to sort
    steps_label = Label(root, text = "Total steps: " + str(r - 2))
    steps_label.grid(column = 0, row = r)
        

#label for buttons
button_label = Label(root, text = "Click a button below to sort:")
button_label.grid(column = 1, row = 0)

#buttons
myButton = Button(root, text = "Bubble sort", command = bubble_sort)
myButton.grid(column = 1, row = 1)

root.mainloop()
