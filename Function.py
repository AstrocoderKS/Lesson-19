def process_square_range(start, end):
    # Initialize lists to store filtered square values
    even_squares = []
    odd_squares = []
    
    # Loop through the range of numbers (inclusive of the end value)
    for num in range(start, end + 1):
        square = num ** 2
        
        # Filter based on whether the square value is even or odd
        if square % 2 == 0:
            even_squares.append(square)
        else:
            odd_squares.append(square)
            
    # Print the filtered results
    print(f"Even square values: {even_squares}")
    print(f"Odd square values: {odd_squares}")