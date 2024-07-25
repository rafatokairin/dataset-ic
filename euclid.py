import numpy as np

def load_points(filename):
    points = []
    with open(filename, 'r') as file:
        for line in file:
            x, y = map(float, line.split())
            points.append((x, y))
    return points

def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def calculate_similarity(file1, file2, threshold=4.0):
    points_original = load_points(file1)
    points_interpolated = load_points(file2)
    
    point_sobreposto = 0
    distances_within_threshold = []
    used_points = [False] * len(points_interpolated)

    for point1 in points_original:
        menor_dist = float('inf')
        menor_dist_index = -1
        for i, point2 in enumerate(points_interpolated):
            if used_points[i]:
                continue
            aux_dist = euclidean_distance(point1, point2)
            if aux_dist < menor_dist:
                menor_dist = aux_dist
                menor_dist_index = i
        if menor_dist < threshold:
            point_sobreposto += 1
            distances_within_threshold.append(menor_dist)
            used_points[menor_dist_index] = True

    perc_original = point_sobreposto / len(points_original)
    perc_interpolado = point_sobreposto / len(points_interpolated)
    media_diferenca = np.mean(distances_within_threshold) if distances_within_threshold else 0

    return perc_original, perc_interpolado, media_diferenca

# Exemplo de uso
file1 = 'mmg4-f.txt'
file2 = 'spline3.txt'
perc_original, perc_interpolado, media_diferenca = calculate_similarity(file1, file2)

# Limitar a porcentagem a 100%
perc_original = min(perc_original, 1.0)
perc_interpolado = min(perc_interpolado, 1.0)

print(f"Porcentagem de sobreposição (original): {perc_original * 100:.2f}%")
print(f"Porcentagem de sobreposição (interpolado): {perc_interpolado * 100:.2f}%")
print(f"Média da diferença das distâncias: {media_diferenca:.2f}")
