# Öklid  formülü => d = √(x₂-x₁)²+(y₂-y₁)²

distances = []
points = [(5,10), (10, 2), (1, 100), (24, 66)]

def euclideanDistance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2

    return ((x2-x1)**2 + (y2-y1)**2)**0.5


for i in range(len(points)):
    for j in range(i+1, len(points)):
            distance = euclideanDistance(points[i], points[j])
            distances.append(distance)

print(f"Tüm mesafeler: {distances}")

print(f"Minimum mesafe: {min(distances)}")