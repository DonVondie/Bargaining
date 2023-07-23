# This is a sample Python script from PyCharm
# For my family, which is much bigger than I ever thought. And to new family I have yet to meet. 
# (But definitely a big thanks to the DGS for always finding the NBS. He is the best) 

def print_hi(name):
    x = len(name)
    y = ""
    for i in range(0,x,1):
        print(name[i])
        y += str((ord(name[i])-97)%26)
        print(y)

    print(name)  # Press Ctrl+F8 to toggle the breakpoint.
    print(y)

if __name__ == '__main__':
    print_hi("Caesar Cipher")
