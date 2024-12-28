# Mundo de Wumpus - Agente Inteligente

Un agente inteligente que explora el Mundo de Wumpus usando lógica proposicional.

## Sobre el Juego

- El agente debe encontrar el oro evitando pozos y al Wumpus
- Usa sensores para detectar brisas (cerca de pozos) y hedores (cerca del Wumpus)
- Aplica lógica proposicional para tomar decisiones seguras
- Se mueve usando la tecla 'w' para avanzar

## Componentes

- `agente.py`: Lógica del agente inteligente
- `logica.py`: Funciones de lógica proposicional
- `percepcion.py`: Detección de brisas y hedores
- `peligro.py`: Evaluación de casillas peligrosas
- `movimiento.py`: Control de movimiento
- `main.py`: Interfaz gráfica y motor del juego

## Ejecución

```bash
python src/main.py