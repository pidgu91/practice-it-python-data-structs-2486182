from collections import deque


def main():
    numbers = deque(maxlen=5)
    numbers.append("STA001")
    ordered_foods = ['DES003', 'STA002', 'ENT004', 'ENT001']
    numbers.extend(ordered_foods)
    numbers.append('STA003')
    print(numbers)
    return

if __name__ == "__main__":
    main()