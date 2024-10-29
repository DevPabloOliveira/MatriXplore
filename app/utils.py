import csv
import numpy as np
from io import StringIO

def process_matrices(data_list):
    matrices = {}
    relations = {}
    sets = {}  
    current_matrix = None
    current_matrix_data = []

    for data in data_list:
        csvfile = StringIO(data)
        reader = csv.reader(csvfile)

        for row in reader:
            if not row or row[0].startswith("#"):
                continue

            # Detecta o início de uma matriz
            if row[0] == "Matriz":
                if current_matrix and current_matrix_data:
                    matrices[current_matrix] = np.array(current_matrix_data, dtype=int)
                    current_matrix_data = []
                current_matrix = row[1]

            # Detecta dados da matriz
            elif current_matrix and row[0].isdigit():
                current_matrix_data.append(list(map(int, row)))

            # Detecta conjuntos
            elif row[0] == "Conjunto":
                sets[row[1]] = row[2:]

            # Detecta relações
            elif row[0] == "Relação":
                relations[row[1]] = [tuple(pair.strip("()").split(", ")) for pair in row[2:]]

        # Adiciona a última matriz processada
        if current_matrix and current_matrix_data:
            matrices[current_matrix] = np.array(current_matrix_data, dtype=int)

    results = {"matrices": {}, "relations": relations, "sets": sets}  # Inclui conjuntos no resultado

    # Processa cada matriz e suas propriedades
    for matrix_name, matrix_data in matrices.items():
        original_properties = {
            "Functional": is_functional(matrix_data),
            "Injective": is_injective(matrix_data),
            "Total": is_total(matrix_data),
            "Surjective": is_surjective(matrix_data),
            "Monomorphism": is_monomorphism(matrix_data),
            "Epimorphism": is_epimorphism(matrix_data),
            "Isomorphism": is_isomorphism(matrix_data)
        }
        results["matrices"][matrix_name] = {
            "original": matrix_data.tolist(),
            "original_properties": original_properties
        }

    # Calcula a matriz resultante e sua transposta se houver ao menos duas matrizes compatíveis
    matrix_names = list(matrices.keys())
    if len(matrix_names) >= 2:
        matrix_a, matrix_b = matrices[matrix_names[0]], matrices[matrix_names[1]]
        if matrix_a.shape[1] == matrix_b.shape[0]:
            combined_matrix = np.dot(matrix_a, matrix_b)
            combined_transpose = combined_matrix.T

            combined_properties = {
                "Functional": is_functional(combined_matrix),
                "Injective": is_injective(combined_matrix),
                "Total": is_total(combined_matrix),
                "Surjective": is_surjective(combined_matrix),
                "Monomorphism": is_monomorphism(combined_matrix),
                "Epimorphism": is_epimorphism(combined_matrix),
                "Isomorphism": is_isomorphism(combined_matrix)
            }

            transpose_properties = {
                "Functional": is_functional(combined_transpose),
                "Injective": is_injective(combined_transpose),
                "Total": is_total(combined_transpose),
                "Surjective": is_surjective(combined_transpose),
                "Monomorphism": is_monomorphism(combined_transpose),
                "Epimorphism": is_epimorphism(combined_transpose),
                "Isomorphism": is_isomorphism(combined_transpose)
            }

            results["combined_matrix"] = combined_matrix.tolist()
            results["combined_properties"] = combined_properties
            results["combined_transpose"] = combined_transpose.tolist()
            results["transpose_properties"] = transpose_properties
        else:
            results["combined_matrix_error"] = "As matrizes selecionadas não possuem dimensões compatíveis para multiplicação."

    return results


# Funções de verificação de propriedades
def is_functional(matrix):
    return "Sim" if np.all(np.sum(matrix, axis=0) <= 1) else "Não"

def is_injective(matrix):
    return "Sim" if np.all(np.sum(matrix, axis=1) <= 1) else "Não"

def is_total(matrix):
    return "Sim" if np.all(np.sum(matrix, axis=0) >= 1) else "Não"

def is_surjective(matrix):
    return "Sim" if np.all(np.sum(matrix, axis=1) >= 1) else "Não"

def is_monomorphism(matrix):
    return "Sim" if is_injective(matrix) == "Sim" else "Não"

def is_epimorphism(matrix):
    return "Sim" if is_surjective(matrix) == "Sim" else "Não"

def is_isomorphism(matrix):
    return "Sim" if is_injective(matrix) == "Sim" and is_surjective(matrix) == "Sim" else "Não"
