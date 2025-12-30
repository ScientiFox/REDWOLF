# Define the target number
target = 11385

# Initialize n as an integer greater than the cube root of the target number
n = int(target ** (1/3)) + 1

# Loop until we find a cube that is greater than the target number
while True:
    # Calculate the cube of n
    cube = n * n * n
    
    # If the cube is greater than the target number, return it
    if cube > target:
        print(cube)
        break
    
    # Increment n to try the next number
    n += 1
    
