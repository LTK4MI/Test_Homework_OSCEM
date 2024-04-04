def create_board():
    """Erzeugt ein leeres Schachbrett."""
    return [['-' for _ in range(8)] for _ in range(8)]

def is_valid_position(position):
    """Überprüft, ob eine Position auf dem Schachbrett gültig ist."""
    file, rank = position
    files = 'abcdefgh'
    ranks = '12345678'
    return file in files and rank in ranks

def print_board(board):
    """Gibt das Schachbrett auf der Konsole aus."""
    for row in board:
        print(' '.join(row))

def main():
    """Hauptfunktion"""
    board = create_board()
    print("Schachbrett:")
    print_board(board)

    # Beispiel für die Überprüfung einer Position
    position = input("Geben Sie eine Position (z.B. e4) ein, um ihre Gültigkeit zu überprüfen: ")
    if is_valid_position(position):
        print(f"{position} ist eine gültige Position auf dem Schachbrett.")
    else:
        print(f"{position} ist keine gültige Position auf dem Schachbrett.")

if __name__ == "__main__":
    main()

#Ich Kommentiere alles
