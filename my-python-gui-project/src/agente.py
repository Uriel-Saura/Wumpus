from tkinter import messagebox


class Agente:
    def __init__(self, main_window):
        self.main_window = main_window
        self.conocimiento = {}
        self.posicion_actual = (0, 0)
        self.oro_recogido = False
        self.movimientos = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Derecha, Abajo, Izquierda, Arriba
        self.visitados = set()
        self.por_visitar = [(0, 0)]
        self.peligros = set()

    def resolver_juego(self):
        while not self.main_window.game_over and not self.oro_recogido:
            if not self.por_visitar:
                break
            self.mover_agente()

    def mover_agente(self):
        if self.por_visitar:
            siguiente_posicion = self.por_visitar.pop(0)
            self.mover_a_posicion(siguiente_posicion)

    def mover_a_posicion(self, posicion):
        if self.es_posicion_valida(posicion):
            self.posicion_actual = posicion
            self.main_window.move_image(posicion[0], posicion[1])
            self.actualizar_conocimiento()
            self.explorar_alrededor()

    def es_posicion_valida(self, posicion):
        x, y = posicion
        return 0 <= x < self.main_window.rows and 0 <= y < self.main_window.columns and posicion not in self.visitados and posicion not in self.peligros

    def actualizar_conocimiento(self):
        x, y = self.posicion_actual
        self.visitados.add((x, y))
        if (x, y) in self.main_window.pits:
            self.main_window.game_over = True
            messagebox.showinfo("Fin del juego", "¡Has caído en un pozo! Fin del juego.")
        elif (x, y) in self.main_window.wumpus:
            self.main_window.game_over = True
            messagebox.showinfo("Fin del juego", "¡Has sido devorado por el Wumpus! Fin del juego.")
        elif (x, y) in self.main_window.gold:
            self.recoger_oro()

    def explorar_alrededor(self):
        x, y = self.posicion_actual
        for dx, dy in self.movimientos:
            nueva_posicion = (x + dx, y + dy)
            if self.es_posicion_valida(nueva_posicion):
                if self.detectar_peligro(nueva_posicion):
                    self.peligros.add(nueva_posicion)
                else:
                    self.por_visitar.append(nueva_posicion)

    def detectar_peligro(self, posicion):
        x, y = posicion
        adyacentes = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
        for ax, ay in adyacentes:
            if (ax, ay) in self.main_window.pits or (ax, ay) in self.main_window.wumpus:
                return True
        return False

    def recoger_oro(self):
        if self.posicion_actual in self.main_window.gold:
            self.main_window.gold.remove(self.posicion_actual)
            self.main_window.cells[self.posicion_actual].config(bg="gray")
            self.oro_recogido = True
            messagebox.showinfo("Oro recogido", "¡Has recogido el oro!")
            if not self.main_window.gold:
                messagebox.showinfo("Victoria", "¡Has recolectado todos los oros! ¡Has ganado el juego!")
                self.main_window.game_over = True