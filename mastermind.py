# mastermind.py
import collections

def calculate_score(answer: str, guess: str) -> tuple[int, int]:
    correct_color_and_position = 0
    color_count_answer = collections.defaultdict(int)
    color_count_guess = collections.defaultdict(int)
    for x, y in zip(answer, guess):
        if x == y:
            correct_color_and_position += 1
        else:
            color_count_answer[x] += 1
            color_count_guess[y] += 1
    correct_color_wrong_position = 0
    for x, appearances in color_count_answer.items():
        if x in color_count_guess:
            correct_color_wrong_position += min(appearances, color_count_guess[x])
    return (correct_color_and_position, correct_color_wrong_position)

def test_calculate_score() -> bool:
    codes = ['1111', '1112', '1122', '1133', '1233', '3344', '4567']
    for x in codes:
        for y in codes:
            print(f'{x} {y} {calculate_score(x, y)}')

def generate_string(idx: int, length: int=4, charset: tuple[str]=('1', '2', '3', '4', '5', '6')) -> str:
    numchars = len(charset)
    result = []
    for i in range(length):
        idx, remainder = divmod(idx, numchars)
        result.append(charset[remainder])
    return "".join(reversed(result))





if __name__ == "__main__":
    # test_calculate_score()
    for i in range(1296):
        print(f'{i} {generate_string(i)}')