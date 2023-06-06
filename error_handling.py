while True:
    try:
        age=int(input('What is your age?'))
        10/age
    except ValueError:
        print("Please enter a number")
    except ZeroDivisionError:
        print("Please enter real age")
    else:
        print("Thank you!")
        break
    finally:
        print("Ok!!I am done")
    print("Can you hear me???")