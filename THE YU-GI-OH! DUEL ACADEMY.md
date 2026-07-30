# THE YU-GI-OH! DUEL ACADEMY
## Glosario:
### Primitivas continuas
Los **efectos continuos** representan un estado permanente del juego y **no poseen una jerarquía de ejecución**. A diferencia de las primitivas `(v)`, estas no se incorporan a una cadena una vez establecidas; simplemente permanecen activas mientras sus condiciones de existencia continúen cumpliéndose.

Su notación general es:

  - **(c...)**: Primitiva continua.

El sufijo de la notación define el **alcance nominal** de la primitiva.

#### Alcances básicos

Los alcances básicos representan **cartas nominales**, sin importar la zona del juego en la que se encuentren. La zona o contexto donde actúa la primitiva **no forma parte del alcance**, sino que debe expresarse mediante el término de abstracción o mediante la descripción verbal de la propia primitiva.

- **(cf)**: La primitiva afecta únicamente a la **carta fuente**.
- **(cp)**: La primitiva afecta únicamente a **cartas propias**, excluyendo la carta fuente.
- **(co)**: La primitiva afecta únicamente a **cartas del oponente**.

#### Alcances compuestos

Los alcances pueden combinarse simplemente concatenando los identificadores básicos.

- **(cfp)**: Carta fuente + cartas propias.
- **(cfo)**: Carta fuente + cartas del oponente.
- **(cpo)**: Cartas propias + cartas del oponente, excluyendo la carta fuente.
- **(cfpo)**: Carta fuente + cartas propias + cartas del oponente.

No existen notaciones especiales para estas combinaciones; únicamente se concatenan los alcances correspondientes.

#### Segunda dimensión de la primitiva

Una vez definido el alcance, el resto de la información se expresa mediante el propio nombre de la primitiva.

Cuando exista un término de abstracción, éste debe dejar claramente definido el comportamiento restante de la mecánica.

#### Lista de resumen
- **(cf)**: Efecto continuo sobre una carta en el juego. Este especifica que el efecto solo influye a la **carta fuente**
- **(cp)**: Efecto continuo sobre ciertas cartas en el juego. Este especifica que el efecto influye a las **cartas del propietario, excepto a la carta fuente**
- **(co)**: Efecto continuo sobre ciertas cartas en el juego. Este especifica que el efecto influye a solo a las **cartas del oponente**.
- **(cfp)**: Efecto continuo sobre ciertas cartas en el juego. Este especifica que el efecto influye a las **cartas del propietario, incluyendo la carta fuente**
- **(cfo)**: Efecto continuo sobre ciertas cartas en el juego. Este especifica que el efecto influye a **las cartas del oponente y la carta fuente**. Muy poco común en el juego
- **(cfpo)**: Efecto continuo sobre ciertas cartas en el juego. Este especifica que el efecto influye en **cartas del oponente y del propietario**.

**_Nota_**: La sintaxis no define la procedencia (deck, mano, zona de monstruos, cementerio, etc.). Esta debe definirse en la descripción de la misma primitiva

### Jerarquías de ejecución:
- **(v1) Counter**: Máxima jerarquía de ejecución conocida. Permite responder a efectos de jerarquía inferior, incluidos los efectos Quick. Ejemplo principal: Counter Traps.
- **(v2a) Quick effect manual**: Permite incorporar un efecto como respuesta durante una ventana válida de interacción. El jugador puede decidir su ejecución
- **(v2b) Quick effect auto**: Permite incorporar un efecto como respuesta durante una ventana válida de interacción. Su ejecución es obligatoria
- **(v3) Conditional auto**: Cuando sucede el evento correspondiente, el efecto debe incorporarse a la siguiente cadena válida. El jugador no decide si activarlo
- **(v4) Conditional manual**: Cuando sucede el evento correspondiente, el efecto puede incorporarse a la siguiente cadena válida. El jugador puede decidir activarlo
- **(v5) Manual**: El efecto no espera un evento disparador. El jugador lo activa voluntariamente durante una ventana legal
### Sintaxis de requerimientos:
- **(acción de costo)**: accion nominal que se debe hacer ANTES de ejecutar el efecto. Esto es a fondo perdido 
- **[condicion a cumplir]**: accion pasada o presente que se debe cumplir para permitir la ejecucion del efecto
- **{obligación despues del cumplimiento del efecto}**: accion que debe realizarse DESPUES de la resolucion satisfactoria del efecto
- **~tiempo de vida~**: Tiempo en el que un efecto de modificación de carta o comportamiento se aplica. Este se expresa en el texto de la carta o se asume sobre la mecánica 
- **•frecuencia de activación•**: Intervalo explicito de cuantas veces se puede aplicar el efecto. Este se expresa en el texto de la carta 
- **«restricción alterna»**: modificacion alternativa posterior del comportamiento del juego actual

### Términos de abstracción:
| Término             | Mecánica cerrada                                                        |
| ------------------- | ----------------------------------------------------------------------- |
| Buscador            | Deck → Mano                                                             |
| Enterrador          | Deck → GY                                                               |
| Revividor           | GY → Campo (respetando condiciones de invocación)                       |
| Grave-Summoner      | GY → Campo (ignorando o sin requerir condiciones de invocación previas) |
| Extra-Summoner      | Extra Deck → Campo                                                      |
| Recuperador         | GY → Mano                                                               |
| Reciclador          | GY → Deck                                                               |
| Reciclador de Ban   | Desterrado → Deck                                                       |
| Desterrador         | Cualquier zona → Desterrado                                             |
| Rebotador           | Campo → Mano                                                            |
| Retornador          | Campo → Deck                                                            |
| Destructor          | Campo → GY mediante destrucción                                         |
| Tributador          | Tributa tus monstruos                                                   |
| Tributador ofensivo | Tributa monstruos del oponente                                          |
| Tributador global   | Tributa monstruos de ambos campos                                       |
| Protector           | Otorga protección a otra carta                                          |
| Inmunidad parcial   | No afectada por efectos (que no impliquen target)                       |
| Inmunidad de target | No puede ser seleccionada como objetivo                                 |
| Inmunidad total     | No afectada por efectos y no puede ser objetivo                         |
| Convertidor         | Modifica una propiedad del objeto de juego                              |
| Incrementador       | Incrementa una propiedad numérica del objeto de juego (Nivel, ATK, etc) |
| Reductor            | Disminuye una propiedad numérica del objeto de juego (Nivel, ATK, etc)  |

**_Nota_**: Cuando no se especifique la dimensión de procedencia, por defecto es el area del propietario (su mano, su deck, su lado del campo). Y cualquier contexto faltante se agrega en la descripción de la primitiva

## Materias

### - Rarities and economy
#### Definiendo presupuestos
- Dos colecciones diferentes
  - Gasto de aprendizaje: dinero invertido para comprender el juego, descubrir arquetipos y desarrollar habilidad.
  - Gasto competitivo: dinero invertido para transformar ese conocimiento en resultados dentro del ecosistema físico.
#### Perfil económico:
- Presupuesto mensual: ~$1500
- Carta virtual, carta real o ambas: Ambas
- **El presupuesto siempre se calcula en cartas físicas a lo largo de todo el curso**
##### Temas próximos:
- Costo sobre demanda
- Reprints
- Ventas y permutas 
### - Lore & Narrative
- Universos compartidos
- Cronología del lore
- Personajes
- Facciones
- Evolución narrativa
### - Pilotage
- Perfiles de jugador
- Sidecking
- Brick balance
### - Metagame and staples
- Staple actual
- Historico competitivo
- Tiers
### - Mechanics
#### Definición del lenguaje de análisis
- Corrección de definiciones
- Anatomía de una primitiva
- Comprensión estratégica
##### Temas próximos:
- Amplificación del arquetipo
- Como evaluar el staple en un arquetipo
- Desglose de primitivas
- Anatomía de combos
- Flushes
- Floodgates
### - Discovery
#### Arquetipos analizados:
- (pendiente)

## Notas
