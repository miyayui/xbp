import random

# ゲームで使用する単語リスト
words = ["python", "programming", "code", "computer", "keyboard", "practice", "challenge"]

score=0
incorrect=False
while True:
        target_word = random.choice(words)
        print(f"次の文字を打て！: {target_word}")
        
        user_input = input()
        if user_input == target_word:
            print("○")
            score+=1
        else:
            print("×")
            incorrect=True
            break

        play_again=input("再挑戦しますか？（はい/いいえ）:").lower()
        if play_again !="はい":
             break
        
        print=(f"game over! あなたの正解数は{score}でした！")

