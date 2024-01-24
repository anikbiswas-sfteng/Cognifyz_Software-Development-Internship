def generate_pyramid(rows):
    for i in range(1, rows + 1):
        # Print spaces before the numbers
        for j in range(rows - i):
            print(" ", end="")
        
        # Print ascending numbers
        for k in range(1, i + 1):
            print(k, end="")
        
        # Print descending numbers
        for l in range(i - 1, 0, -1):
            print(l, end="")
        
        # Move to the next line after each row
        print()

if __name__ == "__main__":
    # Set the number of rows for the pyramid
    pyramid_rows = 10
    
    # Call the function to generate and print the pyramid pattern
    generate_pyramid(pyramid_rows)
#made by nikDev