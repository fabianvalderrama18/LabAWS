# hemoglobin_analysis.py
# Análisis de la hemoglobina humana beta

import json

# Ejercicio 4: Cargar la secuencia
try:
    with open("hemoglobin_clean.txt", "r") as f:
        sequence = f.read().strip()
    
    print("--- Información de la Proteína ---")
    print(f"Longitud: {len(sequence)} aminoácidos")

    # Ejercicio 5: Composición
    amino_acids_list = list(set(sequence))
    counts = {aa: sequence.count(aa) for aa in amino_acids_list}

    # Ejercicio 6 y 7: Peso Molecular
    def calculate_molecular_weight(seq):
        weights = {
            'A': 89.09, 'R': 174.20, 'N': 132.12, 'D': 133.10, 'C': 121.16,
            'E': 147.13, 'Q': 146.15, 'G': 75.07, 'H': 155.16, 'I': 131.18,
            'L': 131.18, 'K': 146.19, 'M': 149.21, 'F': 165.19, 'P': 115.13,
            'S': 105.09, 'T': 119.12, 'W': 204.23, 'Y': 181.19, 'V': 117.15
        }
        return sum(weights.get(aa, 0) for aa in seq)

    total_weight = calculate_molecular_weight(sequence)

    # Ejercicio 9: Porcentaje Hidrofóbico
    hydrophobic_aa = ['A', 'V', 'I', 'L', 'M', 'F', 'W', 'Y']
    hydro_count = sum(sequence.count(aa) for aa in hydrophobic_aa)
    hydro_percentage = (hydro_count / len(sequence)) * 100

    # Ejercicio 8: Guardar resultados en JSON
    results = {
        "protein_name": "hemoglobin subunit beta [Homo sapiens]",
        "length": len(sequence),
        "amino_acid_counts": counts,
        "molecular_weight": round(total_weight, 2),
        "hydrophobic_percentage": round(hydro_percentage, 2)
    }

    with open("hemoglobin_results.json", "w") as jf:
        json.dump(results, jf, indent=4)

    print("\nAnálisis completado con éxito. Revisa 'hemoglobin_results.json'.")

except FileNotFoundError:
    print("Error: No se encontró 'hemoglobin_clean.txt'.")