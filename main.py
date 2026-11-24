import os

os.makedirs("/output", exist_ok=True)
review = "1/5 stars: Opens 47 browser tabs at 2 AM, asks me to fix a syntax error he caused, and then blames my latency when his Wi-Fi drops."

with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(review)
