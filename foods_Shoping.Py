Foods = []
Prices = []
total = 0


while True:
    food = input("Enter a fruit to buy:")
    if(food.lower() == "stop"):
        break

    try:
        Price = float(input("Enter The Food Price"))
        total += Price
    except:
        print("------Enter A valid Price--------")
        continue
    

    Foods.append(food)
    Prices.append(Price)

print("-------The Results------")

for item,pri in zip(Foods,Prices):
    print(f"The Price of {item} is {pri}")
 
print(f"The total Price is {total}")