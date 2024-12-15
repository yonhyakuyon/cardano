import numpy as np


def create_grille(size, holes):
    """
    Создаёт решётку Кардано.

    :param size: Размер решётки (должен быть квадратом: 4x4, 6x6 и т.д.)
    :param holes: Список координат отверстий [(x1, y1), (x2, y2), ...]
    :return: Двумерный массив (решётка)
    """
    grille = np.zeros((size, size), dtype=int)
    for x, y in holes:
        grille[x, y] = 1
    return grille


def rotate_grille(grille):
    """Поворачивает решётку на 90 градусов по часовой стрелке."""
    return np.rot90(grille, k=-1)


def encrypt_cardano(message, grille):
    """
    Шифрует сообщение методом решётки Кардано.

    :param message: Сообщение для шифрования
    :param grille: Решётка Кардано
    :return: Зашифрованное сообщение
    """
    size = grille.shape[0]
    message = message.ljust(size * size, " ")  # Дополняем пробелами до нужной длины
    matrix = np.full((size, size), " ")  # Создаём пустую матрицу для шифрования
    msg_index = 0

    for step in range(4):  # 4 поворота
        print(f"Этап {step + 1} (перед заполнением):\n{grille}")
        for x in range(size):
            for y in range(size):
                if grille[x, y] == 1:
                    matrix[x, y] = message[msg_index]
                    msg_index += 1
        print(f"Матрица после заполнения этапа {step + 1}:\n{matrix}")
        grille = rotate_grille(grille)

    return "".join("".join(row) for row in matrix)


def decrypt_cardano(ciphertext, grille):
    """
    Расшифровывает сообщение методом решётки Кардано.

    :param ciphertext: Зашифрованное сообщение
    :param grille: Решётка Кардано
    :return: Расшифрованное сообщение
    """
    size = grille.shape[0]
    matrix = np.array(list(ciphertext)).reshape((size, size))
    message = []

    for step in range(4):  # 4 поворота
        print(f"Этап {step + 1} (перед чтением):\n{grille}")
        for x in range(size):
            for y in range(size):
                if grille[x, y] == 1:
                    message.append(matrix[x, y])
        print(f"Сообщение после этапа {step + 1}: {''.join(message)}")
        grille = rotate_grille(grille)

    return "".join(message).strip()


# Пример использования
size = 4
holes = [(0, 0), (0, 1), (1, 2), (2, 3)]  # Исправленные отверстия решётки
message = "сообщение"

# Создание решётки
grille = create_grille(size, holes)

# Шифрование
ciphertext = encrypt_cardano(message, grille)
print(f"Зашифрованное сообщение: {ciphertext}")

# Расшифровка
decrypted_message = decrypt_cardano(ciphertext, grille)
print(f"Расшифрованное сообщение: {decrypted_message}")
