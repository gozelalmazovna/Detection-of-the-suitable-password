def password(string):
    """Detection of the suitable password

       Preconditions:
       string = str

       The string must contain:
       at least one upper-case letter
       at least one lower-case letter
       at least one digit
       and be of length at least eight

       Result:
       Boolean = True or False
    """
    val1 = False #Boolean values to keep tract of each case
    val2 = False
    val3 = False

    if len(string) < 8: #Check the length first
        return False
    else:
        for char in string: #Check each character
            if char.isalpha and char.isupper():
                val1 = True #Update valuea if condition is True
            if char.isalpha and char.islower():
                val2 = True #Update valuea if condition is True
            if char.isdigit():
                val3 = True #Update valuea if condition is True
        return (val1 and val2 and val3) #Final result

def test_password():
    """Test function to test the results
       If true no output should be produced
    """
    assert password("Love") == False
    assert password("Loveeeeee") == False
    assert password("Loveyou123") == True

test_password()#Calling test function
