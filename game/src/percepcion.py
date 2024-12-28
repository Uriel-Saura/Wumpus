def hay_brisa(self, posicion):
    x, y = posicion
    adyacentes = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
    for ax, ay in adyacentes:
        if self.es_posicion_valida((ax, ay)) and (ax, ay) in self.main_window.pits:
            print(f"Brisa detectada cerca de pozo en ({ax},{ay})")
            return True
    return False

def hay_hedor(self, posicion):
    x, y = posicion
    adyacentes = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
    for ax, ay in adyacentes:
        if self.es_posicion_valida((ax, ay)) and (ax, ay) in self.main_window.wumpus:
            print(f"Hedor detectado cerca de Wumpus en ({ax},{ay})")
            return True
    return False