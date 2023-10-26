import random

# ゲームで使用する単語リスト
words = ["python", "programming", "code", "computer", "keyboard", "practice", "challenge"]

def main():
    print("Welcome to the Typing Game!")
    input("Press Enter to start...")

    while True:
        score = 0
        incorrect = False

        while True:
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
        print(f"Gane Over! Your score:{score}")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break

    

if __name__ == "__main__":
    main()


