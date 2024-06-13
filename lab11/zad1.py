
length = 5.0
width = 3.0
height = 2.5

door_height = 2.0
door_width = 0.9
window_height = 1.2
window_width = 1.5

wall1_area = 4 * (width * height)

ceiling_area = length * width

total_area_1 = wall1_area + ceiling_area

door_area = door_height * door_width
window_area = window_height * window_width

total_wd_area = door_area + window_area

total_area_2 = total_area_1 - total_wd_area

print(f"Całkowita powierzchnia ścian i sufitu bez uwzględnienia drzwi i okien: {total_area_1:.2f} m²")
print(f"Całkowita powierzchnia ścian i sufitu z uwzględnieniem drzwi i okien: {total_area_2:.2f} m²")
