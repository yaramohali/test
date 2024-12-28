def calculate_circle_properties(radius):
    area = 3.14159 * radius ** 2
    
    circumference = 2 * 3.14159 * radius
    
    # Print the results
    print(f"Area of the circle: {area:.2f}")
    print(f"Circumference of the circle: {circumference:.2f}")

def main():
    radius = float(input("Enter the radius of the circle: "))
    
    calculate_circle_properties(radius)

if __name__ == "__main__":
    main()
