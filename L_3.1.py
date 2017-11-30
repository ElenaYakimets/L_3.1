# тест был пройден 06.11.2017

mass = [1, 2, 3, 4, 5, 12, 18, 30, 24]
result = [x**3 for x in mass if x % 3 == 0 and x % 4 == 0]
print(result)