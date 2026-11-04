class TicTacToe:
    """Ein Tic-Tac-Toe-Spiel für zwei Personen auf einem n × n grossen Feld."""

    def __init__(self, n=4):
        if not isinstance(n, int) or isinstance(n, bool) or n < 1:
            raise ValueError("n muss eine positive ganze Zahl sein.")
        self.n = n
        self.empty_token = "-"
        self.A_token = "X"
        self.B_token = "O"
        self.board = n * n * [self.empty_token]
        self.token_count = 0

    def print_board(self):
        print((2 * self.n + 1) * "#")
        for i in range(self.n):
            row = ""
            for j in range(self.n):
                row += "|" + self.board[i * self.n + j]
            print(row + "|")
        print((2 * self.n + 1) * "#")

    def check_win(self, token):
        winning_pattern = self.n * token

        # Zeilen prüfen.
        for i in range(self.n):
            row = ""
            for j in range(self.n):
                row += self.board[i * self.n + j]
            if row == winning_pattern:
                return True

        # Spalten prüfen.
        for j in range(self.n):
            column = ""
            for i in range(self.n):
                column += self.board[i * self.n + j]
            if column == winning_pattern:
                return True

        # Beide Diagonalen prüfen.
        diag = ""
        for i in range(self.n):
            diag += self.board[i * self.n + i]
        if diag == winning_pattern:
            return True
        diag = ""
        for i in range(self.n):
            diag += self.board[i * self.n + (self.n - 1) - i]
        if diag == winning_pattern:
            return True

        return False

    def play(self):
        # Jeder Aufruf startet eine neue Runde mit leerem Spielfeld.
        self.board = self.n * self.n * [self.empty_token]
        self.token_count = 0
        self.print_board()
        print("Die Felder sind zeilenweise von 1 bis", self.n * self.n, "nummeriert.")

        while self.token_count < self.n * self.n:
            if self.token_count % 2 == 0:
                player = "A"
                token = self.A_token
            else:
                player = "B"
                token = self.B_token

            try:
                move = int(input(player + " wo möchtest Du Dein Token setzen?\n")) - 1
            except ValueError:
                print("Bitte gib eine ganze Zahl ein.")
                continue

            if move < 0 or move >= self.n * self.n:
                print("Bitte wähle ein Feld von 1 bis", self.n * self.n)
                continue
            if self.board[move] != self.empty_token:
                print("Das Feld", move + 1, "ist bereits besetzt")
                continue

            self.board[move] = token
            self.token_count += 1
            self.print_board()
            if self.check_win(token):
                print(player, "hat gewonnen!")
                return

        print("Unentschieden!")


if __name__ == "__main__":
    spiel = TicTacToe(n=5)
    spiel.play()
