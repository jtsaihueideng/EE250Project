def main():
    
    #taking input message
    message = input('What is your input!\n')
   
    # stripping the white spaces
    stripped_message = message.replace(" ", "").replace("\t", "").replace("\n", "")
    print(stripped_message)

if __name__ == "__main__":

    main()
