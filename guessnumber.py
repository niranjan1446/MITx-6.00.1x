start = 0
end = 100
mid = int((start+end)/2)
print ("Please think of a number between 0 and 100!")
def fun(mid,start,end):
    print("Is your secret number "+ str(mid)+"?")
    inp = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    if(inp == 'l'):
        start = mid
        mid = int((start+end)/2)
        fun(mid,start,end)
    elif(inp == 'h'):
        end = mid
        mid = int((start+end)/2)
        fun(mid,start,end)
    elif(inp == 'c'):
        print("Game Over. Your secret number was:", mid)
    else:
        print("Sorry, I did not understand your input.")
        fun(mid,start,end)
fun(mid,start,end)
