import matrix

def main():
    print("Starting: ")
    validate(['aaab','aaaa','jdda','ppod'],"a")
    validate(['aaab','aaaa','jdda','pppp'],"x")
    validate(['aaab','aaaa','jdda','pppp'],"p")

def validate(array = [], char = ''):
    mtx = matrix.Matrix(array)
    if mtx .hasSequenceOf(char):
        print("     Has sequence")
    else:
        print("     Has NOT sequence")


main()
