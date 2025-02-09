#this is Task 3.
""" Objective   : Print the multiplication table for a given number nnn.
 Input          : An integer nnn.
 Output         : Multiplication table from 111 to 101010.
 Hint           : Use a loop to iterate through values 1 to 10 and multiply by nnn."""
def tables_1_to_10():
    for i in range(1,11):
        for j in range(1,11):
            print (i,"X",j,"=",i*j)
        print("")
def main():
    tables_1_to_10()
if __name__ == "__main__":
    main()