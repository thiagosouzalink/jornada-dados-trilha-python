"""
04. Converter Celsius para Fahrenheit em uma Lista
"""
def converter_celsius_para_fahrenheit(lista_celsius: list[float]) -> list[float]:
    return [c * 1.8 + 32 for c in lista_celsius]

temperaturas_celsius = [29, 0, -10, 18.5, -5.6, 100, 180]
temperaturas_fahrenheit = converter_celsius_para_fahrenheit(temperaturas_celsius)
for c, f in zip(temperaturas_celsius, temperaturas_fahrenheit):
    print(f"{c}°C => {f:.2f}°F")
    
