import os
import pickle

def input_scores():
    scores = []
    index = 1
    while True:
        score = int(input(f"# {index}? "))
        if score < 0:
            break
        scores.append(score)
        index += 1
    return scores

def get_average(scores):
    if not scores:
        return 0
    return sum(scores) / len(scores)

def show_scores(scores):
    print("개인점수:", end=" ")
    for score in scores:
        print(score, end=" ")
    print()

def save_scores(scores, filename):
    with open(filename, 'wb') as file:
        pickle.dump(scores, file)

def load_scores(filename):
    if os.path.exists(filename):
        with open(filename, 'rb') as file:
            return pickle.load(file)
    return None

# 주 프로그램부
if __name__ == "__main__":
    filename = 'score.bin'
    scores = load_scores(filename)
    
    if scores is not None:
        print("[점수 출력]")
        show_scores(scores)
        average = get_average(scores)
        print(f"평균: {average:.1f}")
    else:
        print("[점수 입력]")
        scores = input_scores()
        average = get_average(scores)
        print("[점수 출력]")
        show_scores(scores)
        print(f"평균: {average:.1f}")
        save_scores(scores, filename)
