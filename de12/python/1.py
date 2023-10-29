import random
import time
# ゲームで使用する単語リスト
words = ["なまむぎなまごめなまたまご","あぶりかるび","てきしゅつしゅじゅつ","すもももももももものうち","ろうにゃくなんにょ","こまだいとまこまい","てきしゅつしゅじゅつ"]

def main():
    print("早口言葉タイピングゲーム!")
    print("制限時間は60秒！すべてひらがなで入力してね！")
    input("Enterでスタート！")
    
    
    while True:
        score = 0
        game_duration=60

        start_time=time.time()
        end_time=start_time+game_duration

        incorrect = False

        while time.time()<end_time:
            target_word = random.choice(words)
            print(f"次の言葉を打て！: {target_word}")

            user_input = input()
            if user_input == target_word:
                    score += 1
                    print("正解!")
            else:
                    print("不正解!")
                    incorrect = True
                    break  # 間違えた場合、内部の無限ループを終了

        if incorrect:
            print(f"Game Over!:{score}問正解！")
            play_again = input("もう一度挑戦しますか？（はい/いいえ）: ").lower()
            if play_again != "はい":
                break
        else:
             break
        
    print(f"終了！{score}問正解！")

if __name__ == "__main__":
    main()