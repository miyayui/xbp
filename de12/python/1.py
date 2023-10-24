import random
import time

# ゲームで使用する単語リスト
words = ["python", "programming", "code", "computer", "keyboard", "practice", "challenge"]

def main():
    print("Welcome to the Typing Game!")
    input("Press Enter to start...")

    score = 0
    game_duration = 30  # ゲームの制限時間（秒）

    start_time = time.time()
    end_time = start_time + game_duration

    while time.time() < end_time:
        target_word = random.choice(words)
        print(f"Type this word: {target_word}")
        
        user_input = input()
        if user_input == target_word:
            score += 1
            print("Correct!")
        else:
            print("Incorrect!")

    print(f"Game Over! Your score: {score} in {game_duration} seconds.")

if __name__ == "__main":
    main()
