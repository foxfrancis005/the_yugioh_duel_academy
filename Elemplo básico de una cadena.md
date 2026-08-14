# Inicio de cadena
Dejemosle de llamar chain stack a todo. El chain stack es la lista de efectos que contiene la fase de Construcción, nada mas. Lo que llamamos "cadena" es todo el ciclo de vida con todas sus fases

Cartas:
  - A: (v5) - normal spell: Targetea un monstruo en el campo: Destruyelo. Después, añade 1 carta de tu GY a tu Mano
  - B: (v3) - monstruo: Cuando esta carta es destruida: Roba 1 carta
  - C: (v4) - monstruo: Cuando un un monstruo es destruido: Invoca especialmente esta carta
  - D: (v2a) - continuous trap card: Cuando un efecto de carta es activado; puedes descartar 1 carta: Niega la activación de ese efecto
  - E: (v2b) - field spell: Cuando una trampa o efecto de trampa es activado: ganas 500 LP
  - F: (v1) - counter trap card: Cuando un quick effect es activado; puedes activar esta carta: Niega la activación de ese quick effect

- ## Evento generador:
  - Activación de A(v5)
- ## Apertura:
  - /CL1/ -> A(v5): Targetea un monstruo en el campo: Destruyelo
    - (costo): Targetea carta: B(v3) Aprobado
    - -ventana válida para-:
      -D(v2a)
- ## Chain stack:
  - /CL2/ -> D(v2a): Cuando un efecto de carta es activado; puedes descartar 1 carta: Niega la activación de ese efecto. Objetivo: A(v5)
    - [condición]: Un efecto de carta es activado: A(v5): Cumple
    - (costo): Se descarta una carta alterna: Aprobado
    - -ventana válida para-:
      - E(v2b)
      - F(v1)
  - /CL3/ -> E(v2b): Cuando una trampa o efecto de trampa es activado: ganas 500 LP. Causa: Activación de D(v2a)
    - [condición]: Un efecto de trampa es activado: D(v2a): Cumple
    - -ventana válida para-:
      (vacío)
  - /CL4/ -> F(v1): Niega la activación de ese quick effect. Objetivo: D(v2a)
    - [condición]: Un quick effect es activado: D(v2a): Cumple
    - -ventana válida para-:
      (vacío)
- ## Cierre: Fin de la incorporación de efectos
- ## Resolución:
  - /CL4/ -> F(v1): Nego activación de D: Success
  - /CL3/ -> E(v2b): Se detectó la activación de D: se ganan los 500LP
  - /CL2/ -> D(v2a): Efecto negado por D: Failed
  - /CL1/ -> A(v5): Su negación por parte de D fue anulada. Destruye carta targeteada B(v3): Success
- ## Finalización

# Segunda cadena
- #### Evento generador:
  - Monstruo destruido por A(v5) al terminar la cadena anterior
- #### Apertura:
  - /CL1/ -> B(v3): Cuando esta carta es destruida: Roba 1 carta
    - [condición]: Este monstruo fue destruido: Cumple
    - -ventana válida para-:
      (vacío)
  - /CL2/ -> C(v4): Cuando un un monstruo es destruido: Invoca especialmente esta carta
    - [condición]: Monstruo A es destruido: Cumple
    - -ventana válida para-:
      (vacío)
- #### Chain stack:
  (vacío)
- #### Cierre: Fin de la incorporación de efectos
- #### Resolución:
  -/CL2/-> C(v4): Special summon de esta carta: Success
  -/CL1/-> B(v3): Roba una carta: Success
- #### Finalización

## Plantilla base

### - Evento generador
  - Acción inicial que abrió una ventana válida para la activación de un efecto
### - Apertura
  - /CL1/ -> Acción inicial
    - -ventana válida para la activación de algún otro efecto-
### - Chain stack
  - /CL2/ -> Efecto activado
    - (costo aplicado)
    - [condición cumplida para la activacion de este efecto]
    - -ventana válida-
  - /CLN/ ...
    - ...
    - -ventana válida-
  - ...
### - Fin de la incorporación de efectos
### - Resolución
  - /CL[N]/ -> Acciones de resolución del último efecto de la cadena: success/failed
    - -ventana válida para la activación de algún otro efecto (este se resolverá fuera de esta cadena, y este se puede ejecutar si la ejecución de la acción detonadora fue success)-
  - /CL[N-1]/ -> Acciones de resolución del efecto anterior: success/failed
    - -ventana válida-
  - ...
  - /CL1/ -> Acciones del primer evento generador: success/failed
    - -ventana válida-
### - Fin de la cadena
  - La cadena deja de existir
