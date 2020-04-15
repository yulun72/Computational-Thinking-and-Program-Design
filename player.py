# 輸入球員名字、身高、體重
## 文字字串

name = input("Enter a Name: ")
height = input("Enter a Height: ")
weight = input("Enter a Weight: ")

# 用輸入的資訊計算BMI ＝ 公斤 / 公尺平方
## 轉換資料類型
## 做計算

player_height = float(height)/100
player_weight = eval(weight)
player_BMI = player_weight/{(player_height)*(player_height)}


#列印結果

print('name, "的BMI為", player_BMI')
