"""
18. Desenvolva uma função que receba uma string como argumento e retorne 
essa string revertida.
"""
def inverter_string(string_: str) -> str:
    return string_[::-1]

string_ = "Penso, logo existo"
string_invertida = inverter_string(string_)
print(string_invertida)