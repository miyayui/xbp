for i in range(3):
    print(i,"人目") #０からカウントが始まる   
#文字だからダブルクォテーションをいれた
    name=input("名前を入れてください")
#inputですきな数を入れられるようになる
    waist=float(input("腹囲を入れてください"))#floatは小数点の数を入れる
    age=int(input("年齢を入れてください"))#intは整数の数を入れる

    print(name, "さんは腹囲", waist, "cmで年齢は",age, "才ですね。")
#条件分岐
    if waist>=85 and age>=40:
        print(name,"さん、内臓脂肪蓄積注意です")
    else:
        print(name,"さん、腹囲は問題ありません")