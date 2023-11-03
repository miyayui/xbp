import requests

def get_temperature(city_name, api_key):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric"  # 摂氏温度で取得
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()
        temperature = data["main"]["temp"]
        return temperature
    except Exception as e:
        print("エラー:", e)
        return None

def main():
    city_name = input("地名の名前をローマ字表記で記入")  # 取得したい都市の名前を指定
    api_key = "31271437f69c8c0f1e30401c2f81d303"  # あなたのOpenWeatherMap APIキーを入力

    temperature = get_temperature(city_name, api_key)

    if temperature is not None:
        print(f"{city_name}の現在の気温は {temperature}℃ です。")
        
        feeling=input("この気温についてどのように感じますか？（暑い/寒い/ちょうどいい）")

        if feeling=="暑い" and temperature>30:
            print("ノースリーブ")
        elif feeling=="寒い" and temperature>30:
            print("七分丈のシャツ/ノースリーブ+薄手のシャツ") 
        elif feeling=="寒い" and 25<temperature<31:
            print("長袖または七分丈のシャツ/半袖+薄手のシャツ")
        elif feeling=="暑い" and 25<temperature<31:
            print("ノースリーブ")
        elif feeling=="寒い" and 20<temperature<26:
            print("カーディガン/長袖+薄手のジャケット/スウェット")
        elif feeling=="暑い" and 20<temperature<26:
            print("半袖シャツ/七分丈のシャツ/ノースリーブ+薄手のシャツ")
        elif feeling=="寒い" and 15<temperature<21:
            print("セーター")
        elif feeling=="暑い" and 15<temperature<21:
            print("長袖または七分丈のシャツ/半袖+薄手のシャツ")
        elif feeling=="寒い" and 11<temperature<16:
            print("厚手のニット/トレンチコート")
        elif feeling=="暑い" and 11<temperature<16:
            print("カーディガン/長袖+薄手のジャケット/スウェット")
        elif feeling=="寒い" and 7<temperature<12:
            print("厚手のセーター/冬物のコート")
        elif feeling=="暑い" and 7<temperature<12:
            print("薄手のニット/トレンチコート/ダウンベスト")
        elif feeling=="寒い" and 6<temperature<8:
            print("厚手のセーター/冬物コート/ブーツやタイツ")
        elif feeling=="暑い" and 6<temperature<8:
            print("厚手のニット/トレンチコート")
        elif feeling=="寒い" and temperature<5:
            print("ダウンコート/ブーツ、マフラーや手袋/カイロ")
        elif feeling=="暑い" and temperature<5:
            print("厚手のセーター/冬物コート/ブーツやタイツ")
        else:
            print("今のままでok!")
    
    else:
        print("気温の取得に失敗しました。")


if __name__ == "__main__":
    main()
