import requests

apis = [
    ("JSONPlaceholder",  "https://jsonplaceholder.typicode.com/posts/1"),
    ("REST Countries",   "https://restcountries.com/v3.1/name/nepal"),
    ("Open-Meteo",       "https://api.open-meteo.com/v1/forecast?latitude=27.7&longitude=85.3&current_weather=true"),
    ("CoinGecko",        "https://api.coingecko.com/api/v3/ping"),
    ("Dog Facts",        "https://dogapi.dog/api/v2/facts"),
    ("Joke API",         "https://official-joke-api.appspot.com/random_joke"),
    ("Universities",     "http://universities.hipolabs.com/search?country=Nepal"),
    ("IP Info",          "https://ipapi.co/json/"),
    ("Numbers API",      "http://numbersapi.com/42/math"),
]

print("🔍 Testing APIs...\n")
for name, url in apis:
    try:
        r = requests.get(url, timeout=5)
        if r.status_code == 200:
            print(f"✅ {name} → Working!")
        else:
            print(f"⚠️  {name} → Status {r.status_code}")
    except requests.exceptions.Timeout:
        print(f"❌ {name} → Timeout!")
    except requests.exceptions.ConnectionError:
        print(f"❌ {name} → Connection Error!")