import math

def display_trigonometric_values(angle_degrees):

    angle_radians = math.radians(angle_degrees)
    sin_value = math.sin(angle_radians)
    cos_value = math.cos(angle_radians)
    
    try:
        tan_value = math.tan(angle_radians)
    except Exception as e:
        tan_value = None

    try:
        if cos_value != 0:
            cot_value = 1 / tan_value
        else:
            cot_value = None
    except Exception as e:
        cot_value = None

    print(f"Kąt: {angle_degrees}°")
    print(f"sin({angle_degrees}°) = {sin_value:.4f}")
    print(f"cos({angle_degrees}°) = {cos_value:.4f}")
    
    if tan_value is not None and not math.isinf(tan_value):
        print(f"tan({angle_degrees}°) = {tan_value:.4f}")
    else:
        print(f"tan({angle_degrees}°) jest nieokreslony")
    
    if cot_value is not None and not math.isinf(cot_value):
        print(f"cot({angle_degrees}°) = {cot_value:.4f}")
    else:
        print(f"cot({angle_degrees}°) jest nieokreslony")
    
    

angles = [0, 70, 90, 35, 180, 240, 360]

for angle in angles:
    display_trigonometric_values(angle)
