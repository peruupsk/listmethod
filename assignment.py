cars=["bmw","mahindra","suzuki","rolls royce","bentnly","aston martin","tata","audi","mustang"]
#1.Append
cars.append("ferrari")#['bmw', 'mahindra', 'suzuki', 'rolls royce', 'bentnly', 'aston martin', 'tata', 'audi', 'mustang', 'ferrari']
print(cars)
#2.insert 
cars.insert(3,"porsche")#['bmw', 'mahindra', 'suzuki', 'porsche', 'rolls royce', 'bentnly', 'aston martin', 'tata', 'audi', 'mustang', 'ferrari']
print(cars)
#3.clear
print(cars.clear())
cars1=["bmw","mahindra","suzuki","rolls royce","bentnly","aston martin","tata","audi","mustang"]
#4.sort
sorted_cars=cars1.sort()
print(sorted_cars)
#5.remove
cars1.remove("audi")
print(cars1)
#6.index
ca=cars1.index("mustang")
print(ca)
#7.Extend
cars1.extend(["tesla","nissan"])
print(cars1)
#8.pop
print(cars1.pop())
#9.count
print(cars1.count("bmw"))
#10.append
cars1.append(["jaguar","fiat"])
print(cars1)
# 11.insert/multiple
cars1.insert(2,["volvo","honda"])
print(cars1)
#12.sort descending
cars1.sort(reverse=True)
print(cars1)
#13.check if empty 

