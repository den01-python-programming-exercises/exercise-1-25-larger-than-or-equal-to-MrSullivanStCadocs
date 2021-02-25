def main():
    #write your code below this line
    first_number = int(input("Give the first number:"))
    second_number = int(input("Give the second number:"))

    if(first_number>second_number):
      print("The greater number is " + str(first_number))
    elif(first_number<second_number):
      print("The greater number is " + str(second_number))
    elif(first_number==second_number):
      print("The numbers are equal!")

if __name__ == '__main__':
    main()
