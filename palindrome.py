def is_palindrome( list ):
    if ( len(list) < 1 ):
         return True
    elif ( list[0] == list[ len(list)-1]):
        return is_palindrome(  list[1: (len(list)-1)])
    else:
         return False



def is_palindrome2(s):
    if len(s) < 1:
        return True
    else:
        if s[0] == s[-1]:
            return is_palindrome(s[1:-1])
        else:
            return False

list = [ 'a', 'b', 'c','b','a' ];
         

test = is_palindrome( "a")

if (  test == True  ):
    print("Yes" )
if ( test == False ):
    print("no")
    