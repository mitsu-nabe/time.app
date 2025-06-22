import time

# カウントダウンタイマーだ！！
count = 10

while True:
    print(count)
    count = count -1
    time.sleep(1)
    if count < 10: break

# カウントアップ_20でストップの巻
# while True:
    # print(count)
    # count = count +1
    # time.sleep(1)
    # if count > 20: break