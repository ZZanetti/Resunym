import sys

if __name__ == "__main__":
    print("hello world", sys.argv[0])
    if len(sys.argv) > 1:
        print("you supplied additional arguments")
        one = sys.argv[1]
        print(f"the first argument is {str(one)}.")

def sanitycheck(a, b):
    return a + b

def polishWord(target, key):
    return key
