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
            print("この服を着ましょう")

        elif feeling=="寒い" and 25<temperature<31:
            print("この服を着ましょう")

        elif feeling=="暑い" and 25<temperature>30:
            print("この服を着ましょう")

        elif feeling=="寒い" and 19<temperature<26:
            print("この服を着ましょう")

        elif feeling=="暑い" and 14<temperature<20:
            print("この服を着ましょう")

        elif feeling=="寒い" and 14<temperature<20:
            print("この服を着ましょう")
        
        else:
            print("この服を着ましょう")
    
    else:
        print("気温の取得に失敗しました。")


if __name__ == "__main__":
    main()
