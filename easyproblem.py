if __name__ == "__main__":
    a_string = int(input("Enter a string: "))
    last_char = last_char_of_string(a_string)
    if last_char:
      
      print("The last character of the string is:",last_char)
    else:
      print("The string is empty.")
