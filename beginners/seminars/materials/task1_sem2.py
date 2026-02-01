def input_data() -> tuple[int, int, list[int]]:
    array_len = int(input())
    search_number = int(input())

    array_elements = list(map(int, input().split()))

    return array_len, search_number, array_elements

def find_first_occurrence(array_len: int, search_number: int, array_elements: list[int]) -> int:
    answer = -1

    for i in range(array_len):
        if array_elements[i] == search_number:
            answer = i + 1
            break

    if answer == -1:
        raise IndexError("Number not found in the array.")

    return answer

def main():
    array_len, search_number, array_elements = input_data()

    try:
        answer = find_first_occurrence(array_len, search_number, array_elements)
        print(answer)
    except IndexError as error:
        print(error)

if __name__ == "__main__":
    main()
