import matplotlib.pyplot as plt

# Dữ liệu
cities = [
    'Los Angeles', 'San Diego', 'California City', 'San Jose',
    'San Francisco', 'Fresno', 'Sacramento',
    'Long Beach', 'Oakland', 'Bakersfield'
]

areas = [1302, 964, 527, 469, 600, 298, 259, 133, 202, 388]

# Sắp xếp giảm dần
combined = list(zip(cities, areas))
combined.sort(key=lambda x: x[1], reverse=True)

cities, areas = zip(*combined)

# Vẽ biểu đồ
plt.barh(cities, areas)
plt.gca().invert_yaxis()

plt.title('Top 10 thành phố lớn nhất California (km²)')
plt.xlabel('Diện tích (km²)')
plt.ylabel('Thành phố')

plt.show()