'''I count 35 heads and 94 legs among the chickens and rabbits on a farm. How many rabbits
 and how many chickens do I have?'''

# rabbits,y = 12
# chicken, x = 23


def find_values(a, b):
    x = 4*a //2 - b //2
    y = a - x
    return x, y 

def main():
    print(find_values(35, 94))

if __name__ == "__main__":
    main()

