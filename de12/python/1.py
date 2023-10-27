import random
import time
# ゲームで使用する単語リスト
words = ["python", "programming", "code", "computer", "keyboard", "practice", "challenge"]

def main():
    print("Welcome to the Typing Game!")
    input("Press Enter to start...")
    
    
    while True:
        score = 0
        game_duration=60

        start_time=time.time()
        end_time=start_time+game_duration

        incorrect = False

        while time.time()<end_time:
            target_word = random.choice(words)
            print(f"Type this word: {target_word}")

            user_input = input()
            if user_input == target_word:
                    score += 1
                    print("Correct!")
            else:
                    print("Incorrect!")
                    incorrect = True
                    break  # 間違えた場合、内部の無限ループを終了

        if incorrect:
            print(f"Game Over! Your score:{score}")
            play_again = input("Do you want to play again? (yes/no): ").lower()
            if play_again != "yes":
                break
        else:
             break
        
    print(f"Time Over! Your score:{score}")

if __name__ == "__main__":
    main()