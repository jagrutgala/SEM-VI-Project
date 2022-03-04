# Characteristics of a Question
# string, type, difficulty, ans, fake_options?
# Characteristics of a Question Generator
# format string, *numbergenerator_objs, difficulty
# format string, number_of_numbers_needed, types_of_numbers_needed, position_of_numbers_needed

def gcd(n,d):
    if (d == 0):
        return n
    return gcd(d, n%d)

def gcdArray(num_list:list):
    num_list.sort()
    hcf = num_list.pop()
    while len(num_list):
        print(hcf, num_list[0])
        hcf = gcd(hcf, num_list[0])
        num_list.pop(0)
    return hcf

def lcm(n1, n2, gcd):
    return (n1 * n2) / gcd

def lcmArray(num_list):
    ...

def main():
    num_list:list[int] = list(map(int, input("Enter <space> separated list of numbers> \n").split()))
    result = lcmArray(num_list)
    print(f"result {result}")

if __name__ == "__main__":
    main()