class IsNotAlphaError(Exception):
    """Custom exception for input that is not an alphabet."""
    pass

def get_int(request):
    while True:
        try:
            return int(input(request))
        
        except KeyboardInterrupt:
            print("\nProgram ended by user.")
            exit()

        except:
            print("Input is not an int")


def get_int_within_range(request, y, z):
    while True:
        x = get_int(request)
        if x < y or x > z:
            print("Number is not within range")
        else:
            return x


def get_string(request):
    while True:
        try:
            return input(request)
        except:
            print("Input is not an int")


def get_alpha(request):
    while True:
            try:
                letter = input(request).lower()

                if len(letter) != 1:
                    raise ValueError("Length of input can't be greater than 1")
                
                if letter not in "abcdefghijklmnopqrstuvwxyz":
                    raise IsNotAlphaError("Input must be an alphabet")
                
                return letter
        
            except KeyboardInterrupt:
                print("\nProgram ended by user.")
                exit()
