# TODO: Implement the main program logic here

# Import your functions from src/introduction, src/findaverage, and src/comparetoavg
from src.introduction import introduction
from src.findaverage import findaverage
from src.comparetoavg import comparetoavg

# Call these functions accordingly in the main() function
def main():

    # call the introduction function
    introduction()  

    data_set_count = 0  # initiate counter for number of valid data sets processed
    
    # ask the user for three integers (until exit condition is met)
    # exit condition = (0 0 0)
    while True:
        print("\nEnter three integers (enter 0 0 0 to quit):")
        try:
            a = int(input("First integer: "))
            b = int(input("Second integer: "))
            c = int(input("Third integer: "))
        # error checking 
        except ValueError:
            print("Invalid input. Please only enter integers.")
            continue

        # check for termination condition
        if a == 0 and b == 0 and c == 0:
            break

        print(f"\nThe three original integers are: {a}, {b}, {c}")

        # calculate average
        avg = findaverage(a, b, c)
        print(f"The average is {avg:.3f}")

        # compare to average
        comparetoavg(a, b, c, avg)
        
        # count valid set
        data_set_count += 1 

    # end
    print(f"\nTotal number of data sets processed: {data_set_count}")
    if data_set_count < 10:
        # print statements to warn user about data integrity 
        print('\nWARNING: To effectivley test the program you should enter at least 10 data sets.')
        print('Have at least two sets where all three values are equal to the average.')
        print('At least three setswhere no value is equal to the average.')
        print('And at least five sets where one item is equal to the average.')
        
if __name__ == "__main__":
    main()
