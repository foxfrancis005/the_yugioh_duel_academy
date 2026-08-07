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

### Restricciones de invocación

Las **restricciones de invocación** representan propiedades estructurales de un monstruo que definen **cómo puede ingresar al Campo**.

A diferencia de las primitivas `(v)` y de los efectos continuos `(c)`, **no representan un efecto**, no poseen jerarquía de ejecución y **no forman parte de una cadena**. Su única función es definir los métodos de invocación permitidos o prohibidos para la carta.

Su notación general es:

- **(s)**: Restricción de invocación (*Summon Restriction*).

#### Modos de invocación

La primera línea declara los métodos de invocación permitidos o restringidos.

Ejemplos:

```text
-(s): [Normal]
```

La carta SOLO puede ser Invocada de Modo Normal.

```text
-(s): [Special]
```

La carta SOLO puede ser Invocada de Modo Especial.

#### Procedimiento de invocación

Después del modo de invocación pueden declararse los requisitos propios de dicho procedimiento utilizando la misma sintaxis empleada por las primitivas.

- **(Tipo de Invocación: costo)**: Acción que debe realizarse para efectuar ese tipo de invocación.
- **[Tipo de Invocación: condición]**: Condición que debe cumplirse para efectuar ese tipo de invocación.

Ejemplo:

```text
-(s): [Special]
    -(Special Summon: Baraja de tu GY al Deck
      3 monstruos, 3 Magias y 3 Trampas)
```

Ejemplo con condición:

```text
-(s): [Special]
    -[Special Summon: Debes controlar exactamente 1 monstruo]
```

Ejemplo con costo y condición:

```text
-(s): [Special]
    -(Special Summon: Destierra 2 monstruos de tu GY)
    -[Special Summon: Debes controlar una carta de Campo]
```

#### Notas

- Una restricción de invocación **no es un efecto**.
- No posee jerarquía `(v)`.
- No genera una cadena.
- No puede expresarse mediante primitivas, ya que describe una propiedad inherente de la carta y no una ejecución.

### Lista de resumen
##### - Restricciones de invocación
- **(s)**: [Tipo de invocación permitida], [...],...
  - (tipo de invocación: costo)
  - [tipo de invocación: condición]
##### - Primitivas continuas:
- **(cf)**: Efecto continuo sobre una carta en el juego. Este especifica que el efecto solo influye a la **carta fuente**
- **(cp)**: Efecto continuo sobre ciertas cartas en el juego. Este especifica que el efecto influye a las **cartas del propietario, excepto a la carta fuente**
- **(co)**: Efecto continuo sobre ciertas cartas en el juego. Este especifica que el efecto influye a solo a las **cartas del oponente**.
- **(cfp)**: Efecto continuo sobre ciertas cartas en el juego. Este especifica que el efecto influye a las **cartas del propietario, incluyendo la carta fuente**
- **(cfo)**: Efecto continuo sobre ciertas cartas en el juego. Este especifica que el efecto influye a **las cartas del oponente y la carta fuente**. Muy poco común en el juego
- **(cfpo)**: Efecto continuo sobre ciertas cartas en el juego. Este especifica que el efecto influye en **cartas del oponente y del propietario**.

**_Nota_**: La sintaxis no define la procedencia (deck, mano, zona de monstruos, cementerio, etc.). Esta debe definirse en la descripción de la misma primitiva

##### - Jerarquías de ejecución:
- **(v1) Counter**: Máxima jerarquía de ejecución conocida. Permite responder a efectos de jerarquía inferior, incluidos los efectos Quick. Ejemplo principal: Counter Traps.
- **(v2a) Quick effect manual**: Permite incorporar un efecto como respuesta durante una ventana válida de interacción. El jugador puede decidir su ejecución
- **(v2b) Quick effect auto**: Permite incorporar un efecto como respuesta durante una ventana válida de interacción. Su ejecución es obligatoria
- **(v3) Conditional auto**: Cuando sucede el evento correspondiente, el efecto debe incorporarse a la siguiente cadena válida. El jugador no decide si activarlo
- **(v4) Conditional manual**: Cuando sucede el evento correspondiente, el efecto puede incorporarse a la siguiente cadena válida. El jugador puede decidir activarlo
- **(v5) Manual**: El efecto no espera un evento disparador. El jugador lo activa voluntariamente durante una ventana legal
##### - Sintaxis de requerimientos:
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

## Definiciones de términos:
- #### **Ventana válida de activación**: Es un estado del juego que permite activar uno o mas efectos de cierta jerarquía. 
  ##### Características:
  - Es el estado justo cuando las condiciones de un efecto en particular se cumplen
  - Puede aparecer en un estado reglamentario del juego
  - Puede aparecer entre cada efecto eslabon (chain link) del chain stack de una cadena. Al ser así, este efecto se agrega inmediatamente al siguiente eslabón
  - Puede aparecer en la resolución del chain stack. Al ser así, se espera a que termine la resolución de esa cadene, y el efecto se ejecuta fuera de este. Si llegan a haber efectos simultaneos alternos (con misma jerarquía), estos efectos se acomodan en una nueva cadena
- #### **Ciclo de vida de un efecto**: Es la serie de fases que contiene un efecto, desde su existencia inactiva en el juego, hasta su finalización. 
  ##### Fases:
  - **Latente**: El efecto está preparado, en espera de una ventana válida para su ejecución
  - **Habilitado**: El efecto obtuvo la ventana válida de activación, y puede activarse en automático, o el jugador puede decidir activarlo
  - **Declarado**: El efecto es declarado verbalmente, e inmediatamente se verifica el costo de acivación.
    - ##### Protocolo de activación:
      - *Verificación del costo de activación*: Si se cumple, se puede pasar a la siguiente fase. Si no, el efecto queda cancelado y vuelve a la fase Latente.
  - **En espera**: El efecto entra en espera sin ejecutar el potencial de acción hasta que la cadena comience a ejecutar su fase de resolución (Esto en caso de que dicho efecto ya esté incorporado en el chain stack de una cadena)
  - **Resolución**: Se comienzan a ejecutar las acciones del efecto, en caso de que la activación no se haya anulado (porque el estado del juego ya no permite su resolución), cancelado (en caso de que el costo de activación no se cumpla) o negado.
  - **Finalizado**: El efecto se disuelve
- #### Estructura de una cadena:
  - 0. **Inexistente**
  - 1. **Evento generador**: El efecto detonante.
  - 2. **Apertura**:
    *Nota*: Si el efecto de apertura se activa, y no existen efectos alternos que se activen en simultaneo con este efecto de apertura, la cadena se cierra y comienza a resolver este único efecto. De lo contrario, el evento generador se convierte en el primer eslabón de la cadena
    - **/CL1/**: Efecto detonante
      - [condición]: El estado del juego que permite activarlo
      - **(costo)**: Acciones que se deben cumplir para la incorporación del efecto en un eslabon de la cadena. Como es el efecto detonante, se asume que este costo ya fue cumplido
      - **-Ventana válida para el siguiente eslabón-**: Aquí, si una condición de algun efecto extra se cumple, se puede incorporar despues de este eslabón
    - **/CL2/**: Segundo eslabón
    ...(misma estructura)... 
  - 3. **Cierre**: Cuando en la última vetana válida ya no existan efectos compatibles, o los jugadores ya no pueden responder con algo mas
  - 4. **Resolución** (A la inversa):
    - **/CLn/**: Comienzan a ejecutarse las acciones potenciales del último efecto de la cadena, considerando las reglas definidas en la fase de resolución del ciclo de vida del efecto
    - **-Ventana válida para algún efecto-**: Si existe, este efecto generará otra cadena nueva, cuyo efecto será el efecto detonante.
    - **/CLn-1/**: ......(misma estructura)...
    - ...
    - **/CL1/**: ...(misma estructura)...


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
