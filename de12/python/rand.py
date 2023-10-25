import random

# ゲームで使用する単語リスト
words = ["python", "programming", "code", "computer", "keyboard", "practice", "challenge"]

score=0
while True:
        target_word = random.choice(words)
        print(f"次の文字を打て！: {target_word}")
        
        user_input = input()
        if user_input == target_word:
            print("○")
            score+=1
        else:
            print("×")
            score=-1

