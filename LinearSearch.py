def linearSearch(array, N):
    if not array:
        return "Empty Array."

    length = len(array)
    count = 0

    for i in range(length):
        if array[i] == N:
            count += 1

    return count


if __name__ == "__main__":
    array = list(map(int, input().split()))
    N = int(input())
    print(linearSearch(array, N))