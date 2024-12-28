from logica import evaluar_expresion, generar_tabla_verdad
from percepcion import hay_brisa, hay_hedor

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
        self.knowledge_base = {}  # Base de conocimiento proposicional
        self.esperando_tecla = False
        self.main_window.master.bind('<w>', self.continuar_movimiento)

    def resolver_juego(self):
        while not self.main_window.game_over and not self.oro_recogido:
            if not self.por_visitar:
                break
            self.mover_agente()

    def mover_agente(self):
        if self.por_visitar:
            siguiente_posicion = self.por_visitar.pop(0)
            self.mover_a_posicion(siguiente_posicion)

    def mover(self):
        if not self.main_window.game_over and self.por_visitar:
            siguiente_posicion = self.por_visitar.pop(0)
            self.mover_a_posicion(siguiente_posicion)
            return True
        return False

    def continuar_movimiento(self, event):
        """Continúa el movimiento cuando se presiona 'w'"""
        if self.esperando_tecla:
            self.esperando_tecla = False
            
    def mover_a_posicion(self, posicion):
        if self.es_posicion_valida(posicion):
            x, y = posicion
            self.posicion_actual = posicion
            self.visitados.add(posicion)
            # Actualizar posición visual
            self.main_window.move_image(x, y)
            
            # Esperar tecla w
            self.esperando_tecla = True
            while self.esperando_tecla:
                self.main_window.master.update()
            
            # Actualizar conocimiento
            self.actualizar_conocimiento()
            # Explorar alrededor
            self.explorar_alrededor()

    def es_posicion_valida(self, posicion):
        x, y = posicion
        return 0 <= x < self.main_window.rows and 0 <= y < self.main_window.columns and posicion not in self.visitados and posicion not in self.peligros

    def actualizar_conocimiento(self):
        x, y = self.posicion_actual
        self.visitados.add((x, y))
        if (x, y) in self.main_window.pits:
            self.main_window.game_over = True
            print("Fin del juego", "¡Has caído en un pozo! Fin del juego.")
        elif (x, y) in self.main_window.wumpus:
            self.main_window.game_over = True
            print("Fin del juego", "¡Has sido devorado por el Wumpus! Fin del juego.")
        elif (x, y) in self.main_window.gold:
            self.recoger_oro()

    def explorar_alrededor(self):
        x, y = self.posicion_actual
        for dx, dy in self.movimientos:
            nueva_posicion = (x + dx, y + dy)
            if self.es_posicion_valida(nueva_posicion) and nueva_posicion not in self.por_visitar:
                if not self.detectar_peligro(nueva_posicion):
                    self.por_visitar.append(nueva_posicion)
                else:
                    self.peligros.add(nueva_posicion)

    def detectar_peligro(self, posicion):
        x, y = posicion
        adyacentes = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
        
        # Variables para la tabla de verdad
        variables = []
        print(f"\nAnalizando posición ({x},{y})")
        
        # Verificar brisas y hedores en posición actual
        hay_brisa_actual = hay_brisa(self, posicion)
        hay_hedor_actual = hay_hedor(self, posicion)
        
        print(f"Posición anterior ({self.posicion_actual[0]},{self.posicion_actual[1]})")
        print(f"Brisa detectada: {hay_brisa_actual}")
        print(f"Hedor detectado: {hay_hedor_actual}")
        
        for ax, ay in adyacentes:
            if self.es_posicion_valida((ax, ay)):
                variables.append(f'P_{ax}_{ay}')
                variables.append(f'W_{ax}_{ay}')
                print(f"Verificando casilla ({ax},{ay})")
        
        tabla_verdad = generar_tabla_verdad(variables)
        
        # Construir expresiones lógicas
        expresion = ['OR']
        if hay_brisa_actual:
            for ax, ay in adyacentes:
                if self.es_posicion_valida((ax, ay)):
                    expresion.append(['AND', f'P_{ax}_{ay}'])
                    print(f"Posible pozo en ({ax},{ay})")
        
        if hay_hedor_actual:
            for ax, ay in adyacentes:
                if self.es_posicion_valida((ax, ay)):
                    expresion.append(['AND', f'W_{ax}_{ay}'])
                    print(f"Posible Wumpus en ({ax},{ay})")
        
        # Evaluar para cada combinación en la tabla de verdad
        for asignacion in tabla_verdad:
            if evaluar_expresion(expresion, asignacion):
                print(f"Peligro detectado en ({x},{y})")
                return True
        
        print(f"Casilla segura en ({x},{y})")
        return False

    def recoger_oro(self):
        if self.posicion_actual in self.main_window.gold:
            self.main_window.gold.remove(self.posicion_actual)
            self.main_window.cells[self.posicion_actual].config(bg="yellow")
            self.oro_recogido = True
            print("Oro recogido", "¡Has recogido el oro!")
            if not self.main_window.gold:
                print("Victoria", "¡Has recolectado todos los oros!")
                self.main_window.game_over = True
                self.main_window.mostrar_botones_final()  # Llamada al nuevo método