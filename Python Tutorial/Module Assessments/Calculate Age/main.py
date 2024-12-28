def main():
    flag = 1
    while flag == 1: 
        start_year = int(input("Please enter the year you've born in"))
        end_year = int(input("Please enter the current year"))
        age = end_year - start_year
        if age < 0: 
            print("Please enter a valid years")
        else:
            flag = 0    
    print(age)
    
if __name__ == "__main__":
    main()