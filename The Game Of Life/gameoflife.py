"""
The Game Of Life con la programmazione ad oggetti:
Il codice utilizza la programmazione ad oggetti (Object-Oriented Programming, OOP) in Python. In particolare, vengono utilizzati i seguenti concetti OOP:
- Incapsulamento: La classe GameOfLife incapsula lo stato del gioco, includendo la griglia, lo stato di esecuzione e le funzioni per gestire il gioco.
- Ereditarietà: Non viene utilizzato esplicitamente in questo codice, ma la classe GameOfLife potrebbe ereditare da una classe padre se necessario.
- Polimorfismo: Non viene utilizzato esplicitamente in questo codice, ma la funzione compute_next_state potrebbe essere overridata (ovvero essere riscritta da un metodo ereditato) in una sottoclasse per implementare regole del gioco diverse.

Scopo del gioco:
Il gioco consiste nel simulare la vita di una popolazione di cellule viventi in una griglia rettangolare. Le cellule viventi sono rappresentate da un
punto nella griglia, mentre le cellule morte sono rappresentate da uno spazio vuoto. Il gioco è basato sulle seguenti regole:

Regole del gioco:
Qualsiasi cellula viva con meno di due cellule vive adiacenti, muore, come per effetto d'isolamento;
Qualsiasi cellula viva con due o tre cellule vive adiacenti, sopravvive alla generazione successiva;
Qualsiasi cellula viva con più di tre cellule vive adiacenti, muore, come per effetto di sovrappopolazione;
Qualsiasi cellula morta con esattamente tre cellule vive adiacenti diventa una cellula viva, come per effetto di riproduzione.

Ora prova a avviare il programma e cliccare sulle cellule per creare una configurazione tutta tua, la vedrai evolversi premendo il pulsante "Start",
la potrai fermare con il pulsante "Stop", potrai fermare e resettare le cellule nella griglia con il pulsante "Reset" e
infine potrai vedere la tua popolazione di cellule evolversi step-by-step con il pulsante "Step".

Buon Divertimento!
"""

#Codice del gioco
import tkinter as tk

# Configurazione del gioco
GRID_SIZE = 30 # Dimensione della griglia del gioco
CELL_SIZE = 20  # Dimensione di ogni cellula della griglia
DELAY = 200  # Millisecondi tra gli aggiornamenti del gioco

class GameOfLife:
    def __init__(self, root):
        # Inizializza il gioco con una griglia vuota e un canvas per disegnare la griglia
        self.root = root
        self.grid = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
        self.canvas = tk.Canvas(root, width=GRID_SIZE * CELL_SIZE, height=GRID_SIZE * CELL_SIZE)
        self.canvas.pack()

        # Variabili per gestire lo stato del gioco
        self.running = False

        self.draw_grid()
        self.update_grid()

        # Crea i pulsanti per controllare il gioco
        self.start_button = tk.Button(root, text="Start", command=self.start_game)
        self.start_button.pack()

        self.stop_button = tk.Button(root, text="Stop", command=self.stop_game)
        self.stop_button.pack()

        self.reset_button = tk.Button(root, text="Reset", command=self.reset_game)
        self.reset_button.pack()

        self.step_button = tk.Button(root, text="Step", command=self.step_game)
        self.step_button.pack()

        # Associa il click sinistro del mouse alla funzione toggle_cell
        self.canvas.bind("<Button-1>", self.toggle_cell)

    def start_game(self):
        # Avvia il gioco
        self.running = True
        self.update_grid()

    def stop_game(self):
        # Ferma il gioco
        self.running = False

    def reset_game(self):
        # Resetta il gioco
        self.running = False
        self.grid = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
        self.draw_grid()

    def step_game(self):
        # Esegue un passo del gioco
        new_grid = [[self.compute_next_state(i, j) for j in range(GRID_SIZE)] for i in range(GRID_SIZE)]
        self.grid = new_grid
        self.draw_grid()

    def toggle_cell(self, event):
        # Alterna lo stato di una cellula quando viene cliccata
        x = event.x // CELL_SIZE
        y = event.y // CELL_SIZE
        self.grid[y][x] = 1 - self.grid[y][x]
        self.draw_grid()

    def draw_grid(self):
        # Disegna la griglia del gioco
        self.canvas.delete("all")
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                color = "black" if self.grid[i][j] == 1 else "white"
                self.canvas.create_rectangle(
                    j * CELL_SIZE, i * CELL_SIZE, 
                    (j + 1) * CELL_SIZE, (i + 1) * CELL_SIZE, 
                    fill=color, outline="gray"
                )

    def update_grid(self):
        # Aggiorna la griglia del gioco
        if self.running:
            new_grid = [[self.compute_next_state(i, j) for j in range(GRID_SIZE)] for i in range(GRID_SIZE)]
            self.grid = new_grid
            self.draw_grid()
            self.root.after(DELAY, self.update_grid)

    def compute_next_state(self, x, y):
        # Calcola lo stato successivo di una cellula
        # Calcola il numero di cellule vive adiacenti
        live_neighbors = 0
        for i in range(max(0, x - 1), min(x + 2, GRID_SIZE)):
            for j in range(max(0, y - 1), min(y + 2, GRID_SIZE)):
                if (i == x and j == y):
                    continue
                if self.grid[i][j] == 1:
                    live_neighbors += 1

        # Applica le regole del gioco
        if self.grid[x][y] == 1:
            if live_neighbors < 2 or live_neighbors > 3:
                return 0
            else:
                return 1
        else:
            if live_neighbors == 3:
                return 1
            else:
                return 0

if __name__ == "__main__":
    # Crea la finestra
    root = tk.Tk()
    gioco = GameOfLife(root)
    root.mainloop()