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

#### Procedimiento de invocación

Después del modo de invocación pueden declararse los requisitos propios de dicho procedimiento utilizando la misma sintaxis empleada por las primitivas.

- **(Tipo de Invocación: costo)**: Acción que debe realizarse para efectuar ese tipo de invocación.
- **[Tipo de Invocación: condición]**: Condición que debe cumplirse para efectuar ese tipo de invocación.

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
- **+Origen+**: ubicación que debe ocupar la carta fuente para que la primitiva tenga potencial de acción.
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

### Origen de las primitivas

El **origen** representa la ubicación que debe ocupar la **carta fuente** para que una primitiva tenga potencial de acción.

Su notación general es:

* **+Origen+**: Zona del juego desde la cual la primitiva posee potencial de acción.

#### Reglas de origen

* El origen es **obligatorio en toda primitiva**, incluso cuando la ubicación de la carta fuente resulte evidente por su tipo o comportamiento.
* Debe declararse inmediatamente después de la descripción nominal de la primitiva y antes de costos, condiciones, obligaciones, tiempos de vida, frecuencias de activación o restricciones alternas.
* El origen es una **propiedad estructural de la primitiva** y no una `[condición]`.
* El origen pertenece individualmente a cada primitiva y no a la carta completa. Una misma carta puede contener primitivas con diferentes orígenes.
* El origen describe exclusivamente la ubicación de la **carta fuente**. No representa la ubicación de cartas utilizadas como costo, objetivos, recursos, cartas afectadas ni destinos de una acción.
* La existencia de una carta fuente en el origen correspondiente determina que la primitiva posea potencial de acción. Sus demás requisitos determinan posteriormente si dicho potencial puede ser habilitado o ejecutado.

#### Orígenes generales

Las zonas externas al Campo se declaran directamente mediante su nombre correspondiente:

* **+Mano+**
* **+Deck+**
* **+GY+**
* **+Extra Deck+**
* **+Desterrado+**

Cuando una primitiva tiene como origen el Campo puede utilizarse:

* **+Campo+**

`+Campo+` representa por defecto la zona nominal del Campo correspondiente a la naturaleza de la carta fuente:

* Para una carta de Monstruo, `+Campo+` representa su ubicación nominal como monstruo.
* Para una carta de Magia o Trampa, `+Campo+` representa su ubicación nominal como Magia o Trampa.

Cuando la carta fuente deba encontrarse en una zona del Campo distinta de su ubicación nominal, el origen debe especificar explícitamente dicha zona.

Entre estas ubicaciones pueden declararse:

* **+Monster Zone+**
* **+Zona de Magias/Trampas+**
* **+Zona Péndulo+**
* **+Field Zone+**

La especificación explícita de una zona prevalece sobre cualquier ubicación que pudiera inferirse del tipo, naturaleza o comportamiento nominal de la carta fuente.

#### Propiedad del origen

Por defecto, todo origen se refiere a la zona correspondiente del **propietario de la carta fuente**, salvo que la propia mecánica establezca expresamente una relación diferente.

El origen no determina quién controla actualmente la carta, quién ejecuta una acción ni qué jugador resulta afectado por la primitiva. Su función se limita a establecer la ubicación requerida de la carta fuente.

### Términos formales de referencia

Las primitivas utilizan un conjunto de términos formales para establecer de manera inequívoca la relación entre la carta que contiene una primitiva, su propietario y el oponente.

Estos términos deben conservar su significado independientemente del jugador que lea, analice o ejecute la primitiva.

#### Carta fuente

**Carta fuente**: Carta que contiene la primitiva que se está analizando.

La carta fuente constituye el punto de referencia central para interpretar las relaciones de propiedad, oposición y ubicación expresadas dentro de la primitiva.

Cuando una expresión mencione explícitamente a la **carta fuente**, únicamente puede referirse a dicha carta y no al resto de cartas pertenecientes a su propietario.

#### Carta del propietario

**Carta del propietario**: Carta perteneciente al mismo jugador propietario de la carta fuente.

El término establece una relación de propiedad respecto de la carta fuente y no respecto del jugador que esté leyendo o analizando la primitiva.

Cuando el contexto no excluya explícitamente a la carta fuente, ésta puede formar parte del conjunto de cartas del propietario.

#### Tu carta

**Tu carta**: Sinónimo sintáctico de **carta del propietario**.

Los términos **tu**, **tus** y sus construcciones derivadas se interpretan siempre desde la perspectiva del propietario de la carta fuente.

Por lo tanto, el pronombre posesivo no cambia de significado dependiendo del lector, analista o jugador que consulte la primitiva.

#### Propietario

**Propietario**: Jugador al que pertenece la carta fuente.

El propietario constituye el punto de referencia utilizado para interpretar expresiones relativas como **tu**, **tus**, **carta del propietario**, **tu Campo**, **tu Mano**, **tu Deck**, **tu GY** y demás relaciones equivalentes.

#### Oponente

**Oponente**: Jugador contrario al propietario de la carta fuente.

Toda expresión que haga referencia al **oponente**, **tu oponente**, **cartas del oponente**, **Campo del oponente** o cualquier construcción equivalente se interpreta desde la perspectiva del propietario de la carta fuente.

### Regla general de referencia

La **carta fuente** constituye el centro del sistema de referencia de una primitiva.

A partir de ella se determinan formalmente las siguientes relaciones:

* **Carta fuente**: la propia carta que contiene la primitiva.
* **Propietario**: jugador al que pertenece la carta fuente.
* **Tu / tus**: relación de pertenencia con el propietario de la carta fuente.
* **Carta del propietario**: carta perteneciente al propietario de la carta fuente.
* **Oponente**: jugador contrario al propietario de la carta fuente.
* **Carta del oponente**: carta perteneciente al jugador contrario al propietario de la carta fuente.

Estas relaciones permanecen constantes durante la interpretación de la primitiva y no dependen de la perspectiva del lector.

### Ciclo de vida de un efecto y Estructura de la Cadena

#### Ciclo de vida de un efecto
Todo efecto posee un ciclo de vida bien definido que describe los estados por los que transita desde que existe en una carta hasta que concluye completamente su ejecución:

1. **Latente**: El efecto existe como parte de la carta, pero todavía no puede incorporarse al juego. Permanece "cargado" esperando el estado del juego que permita su activación.
2. **Habilitado**: El efecto entra en una **ventana válida**. El estado actual permite su incorporación, pero aún no ha sido activado. Dependiendo de su jerarquía, puede requerir una decisión del jugador o incorporarse automáticamente.
3. **Activado / Declarado**: El efecto cambia oficialmente de estado. La activación ha sido declarada y se convierte en una ejecución pendiente. Aún no se ha resuelto ninguna acción.
4. **Incorporado al Chain Stack**: El efecto pasa a formar parte del Chain Stack. Permanece en espera mientras la cadena continúa construyéndose o hasta que llegue el momento de resolverla.
5. **Resolución**: El efecto comienza a ejecutarse. Se depuran secuencialmente todas las acciones que lo componen, verificando que sus condiciones de ejecución continúen siendo válidas.
6. **Finalizado**: La resolución ha concluido. El efecto abandona el Chain Stack y deja de existir como ejecución activa (aunque la carta pueda conservar el mismo efecto en estado latente para futuras oportunidades).

#### Estructura de la Cadena
La cadena (Chain) es la estructura integral que administra los efectos **durante su paso por el Chain Stack** (fases de Incorporación y Resolución), organizando el flujo de las interacciones. Consta de las siguientes fases fundamentales:

1. **Evento generador**: La acción del juego o activación previa que altera el estado actual del juego. Es el evento disparador que da origen a la necesidad de construir la cadena.
2. **Apertura**: El efecto inicial (o efectos simultáneos) que se activa en respuesta directa (o por voluntad libre) al evento generador. Forma el eslabón 1 de la cadena (Chain Link 1). Al abrirse, valida sus costos/condiciones y abre la primera ventana de interacción.
3. **Chain stack**: La fase de construcción de la cadena donde los jugadores incorporan secuencialmente efectos adicionales (Chain Link 2, 3, etc.) en respuesta a los eslabones anteriores. Cada eslabón evalúa sus condiciones y costos antes de adherirse, y abre su propia ventana de interacción válida para la jerarquía de los efectos que le sigan.
4. **Cierre**: Ocurre cuando la ventana de interacción queda vacía o los jugadores deciden no agregar más efectos al chain stack.
5. **Resolución**: Los efectos incorporados se ejecutan en orden inverso a su activación (LIFO: Last In, First Out). Cada eslabón resuelve y determina si su ejecución fue exitosa o si fue alterada/negada basándose en las resoluciones de eslabones previos.
6. **Finalización**: Concluye el ciclo de vida de la cadena. El nuevo estado del juego, tras todas las resoluciones, puede convertirse instantáneamente en el **Evento generador** de una nueva cadena.

#### Plantilla (Fórmula) de la Cadena

```markdown
## Evento generador:
- (Acción del juego, resolución previa, o estado del tablero)

## Apertura:
- /CL1/: (v[x][n]) [Efecto o acción inicial]
  - [condición]: Condición para que se active este efecto (si aplica)
  - (costo): Acción nominal a fondo perdido (si aplica)
  - -ventana válida para-: [Lista de jerarquías o efectos disponibles en respuesta]

## Chain stack:
- /CL2/: (v[x][n]) [Efecto de respuesta al CL1]
  - [condición]: Condición para que se active este efecto (si aplica)
  - (costo): Acción nominal a fondo perdido (si aplica)
  - -ventana válida para-: [Lista de jerarquías o efectos disponibles en respuesta al CL2]
- /CL[N]/: ...
**_Nota_**: La sintaxis no define la procedencia (deck, mano, zona de monstruos, cementerio, etc.). Esta debe definirse en la descripción de la misma primitiva

##### - Jerarquías de ejecución:
- **(v1) Counter**: Máxima jerarquía de ejecución conocida. Permite responder a efectos de jerarquía inferior, incluidos los efectos Quick. Ejemplo principal: Counter Traps.
- **(v2a) Quick effect manual**: Permite incorporar un efecto como respuesta durante una ventana válida de interacción. El jugador puede decidir su ejecución
- **(v2b) Quick effect auto**: Permite incorporar un efecto como respuesta durante una ventana válida de interacción. Su ejecución es obligatoria
- **(v3) Conditional auto**: Cuando sucede el evento correspondiente, el efecto debe incorporarse a la siguiente cadena válida. El jugador no decide si activarlo
- **(v4) Conditional manual**: Cuando sucede el evento correspondiente, el efecto puede incorporarse a la siguiente cadena válida. El jugador puede decidir activarlo
- **(v5) Manual**: El efecto no espera un evento disparador. El jugador lo activa voluntariamente durante una ventana legal
##### - Sintaxis de requerimientos:
- **+Origen+**: ubicación que debe ocupar la carta fuente para que la primitiva tenga potencial de acción.
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

### Origen de las primitivas

El **origen** representa la ubicación que debe ocupar la **carta fuente** para que una primitiva tenga potencial de acción.

Su notación general es:

* **+Origen+**: Zona del juego desde la cual la primitiva posee potencial de acción.

#### Reglas de origen

* El origen es **obligatorio en toda primitiva**, incluso cuando la ubicación de la carta fuente resulte evidente por su tipo o comportamiento.
* Debe declararse inmediatamente después de la descripción nominal de la primitiva y antes de costos, condiciones, obligaciones, tiempos de vida, frecuencias de activación o restricciones alternas.
* El origen es una **propiedad estructural de la primitiva** y no una `[condición]`.
* El origen pertenece individualmente a cada primitiva y no a la carta completa. Una misma carta puede contener primitivas con diferentes orígenes.
* El origen describe exclusivamente la ubicación de la **carta fuente**. No representa la ubicación de cartas utilizadas como costo, objetivos, recursos, cartas afectadas ni destinos de una acción.
* La existencia de una carta fuente en el origen correspondiente determina que la primitiva posea potencial de acción. Sus demás requisitos determinan posteriormente si dicho potencial puede ser habilitado o ejecutado.

#### Orígenes generales

Las zonas externas al Campo se declaran directamente mediante su nombre correspondiente:

* **+Mano+**
* **+Deck+**
* **+GY+**
* **+Extra Deck+**
* **+Desterrado+**

Cuando una primitiva tiene como origen el Campo puede utilizarse:

* **+Campo+**

`+Campo+` representa por defecto la zona nominal del Campo correspondiente a la naturaleza de la carta fuente:

* Para una carta de Monstruo, `+Campo+` representa su ubicación nominal como monstruo.
* Para una carta de Magia o Trampa, `+Campo+` representa su ubicación nominal como Magia o Trampa.

Cuando la carta fuente deba encontrarse en una zona del Campo distinta de su ubicación nominal, el origen debe especificar explícitamente dicha zona.

Entre estas ubicaciones pueden declararse:

* **+Monster Zone+**
* **+Zona de Magias/Trampas+**
* **+Zona Péndulo+**
* **+Field Zone+**

La especificación explícita de una zona prevalece sobre cualquier ubicación que pudiera inferirse del tipo, naturaleza o comportamiento nominal de la carta fuente.

#### Propiedad del origen

Por defecto, todo origen se refiere a la zona correspondiente del **propietario de la carta fuente**, salvo que la propia mecánica establezca expresamente una relación diferente.

El origen no determina quién controla actualmente la carta, quién ejecuta una acción ni qué jugador resulta afectado por la primitiva. Su función se limita a establecer la ubicación requerida de la carta fuente.

### Términos formales de referencia

Las primitivas utilizan un conjunto de términos formales para establecer de manera inequívoca la relación entre la carta que contiene una primitiva, su propietario y el oponente.

Estos términos deben conservar su significado independientemente del jugador que lea, analice o ejecute la primitiva.

#### Carta fuente

**Carta fuente**: Carta que contiene la primitiva que se está analizando.

La carta fuente constituye el punto de referencia central para interpretar las relaciones de propiedad, oposición y ubicación expresadas dentro de la primitiva.

Cuando una expresión mencione explícitamente a la **carta fuente**, únicamente puede referirse a dicha carta y no al resto de cartas pertenecientes a su propietario.

#### Carta del propietario

**Carta del propietario**: Carta perteneciente al mismo jugador propietario de la carta fuente.

El término establece una relación de propiedad respecto de la carta fuente y no respecto del jugador que esté leyendo o analizando la primitiva.

Cuando el contexto no excluya explícitamente a la carta fuente, ésta puede formar parte del conjunto de cartas del propietario.

#### Tu carta

**Tu carta**: Sinónimo sintáctico de **carta del propietario**.

Los términos **tu**, **tus** y sus construcciones derivadas se interpretan siempre desde la perspectiva del propietario de la carta fuente.

Por lo tanto, el pronombre posesivo no cambia de significado dependiendo del lector, analista o jugador que consulte la primitiva.

#### Propietario

**Propietario**: Jugador al que pertenece la carta fuente.

El propietario constituye el punto de referencia utilizado para interpretar expresiones relativas como **tu**, **tus**, **carta del propietario**, **tu Campo**, **tu Mano**, **tu Deck**, **tu GY** y demás relaciones equivalentes.

#### Oponente

**Oponente**: Jugador contrario al propietario de la carta fuente.

Toda expresión que haga referencia al **oponente**, **tu oponente**, **cartas del oponente**, **Campo del oponente** o cualquier construcción equivalente se interpreta desde la perspectiva del propietario de la carta fuente.

### Regla general de referencia

La **carta fuente** constituye el centro del sistema de referencia de una primitiva.

A partir de ella se determinan formalmente las siguientes relaciones:

* **Carta fuente**: la propia carta que contiene la primitiva.
* **Propietario**: jugador al que pertenece la carta fuente.
* **Tu / tus**: relación de pertenencia con el propietario de la carta fuente.
* **Carta del propietario**: carta perteneciente al propietario de la carta fuente.
* **Oponente**: jugador contrario al propietario de la carta fuente.
* **Carta del oponente**: carta perteneciente al jugador contrario al propietario de la carta fuente.

Estas relaciones permanecen constantes durante la interpretación de la primitiva y no dependen de la perspectiva del lector.

### Ciclo de vida de un efecto y Estructura de la Cadena

#### Ciclo de vida de un efecto
Todo efecto posee un ciclo de vida bien definido que describe los estados por los que transita desde que existe en una carta hasta que concluye completamente su ejecución:

1. **Latente**: El efecto existe como parte de la carta, pero todavía no puede incorporarse al juego. Permanece "cargado" esperando el estado del juego que permita su activación.
2. **Habilitado**: El efecto entra en una **ventana válida**. El estado actual permite su incorporación, pero aún no ha sido activado. Dependiendo de su jerarquía, puede requerir una decisión del jugador o incorporarse automáticamente.
3. **Activado / Declarado**: El efecto cambia oficialmente de estado. La activación ha sido declarada y se convierte en una ejecución pendiente. Aún no se ha resuelto ninguna acción.
4. **Incorporado al Chain Stack**: El efecto pasa a formar parte del Chain Stack. Permanece en espera mientras la cadena continúa construyéndose o hasta que llegue el momento de resolverla.
5. **Resolución**: El efecto comienza a ejecutarse. Se depuran secuencialmente todas las acciones que lo componen, verificando que sus condiciones de ejecución continúen siendo válidas.
6. **Finalizado**: La resolución ha concluido. El efecto abandona el Chain Stack y deja de existir como ejecución activa (aunque la carta pueda conservar el mismo efecto en estado latente para futuras oportunidades).

#### Estructura de la Cadena
La cadena (Chain) es la estructura integral que administra los efectos **durante su paso por el Chain Stack** (fases de Incorporación y Resolución), organizando el flujo de las interacciones. Consta de las siguientes fases fundamentales:

1. **Evento generador**: La acción del juego o activación previa que altera el estado actual del juego. Es el evento disparador que da origen a la necesidad de construir la cadena.
2. **Apertura**: El efecto inicial (o efectos simultáneos) que se activa en respuesta directa (o por voluntad libre) al evento generador. Forma el eslabón 1 de la cadena (Chain Link 1). Al abrirse, valida sus costos/condiciones y abre la primera ventana de interacción.
3. **Chain stack**: La fase de construcción de la cadena donde los jugadores incorporan secuencialmente efectos adicionales (Chain Link 2, 3, etc.) en respuesta a los eslabones anteriores. Cada eslabón evalúa sus condiciones y costos antes de adherirse, y abre su propia ventana de interacción válida para la jerarquía de los efectos que le sigan.
4. **Cierre**: Ocurre cuando la ventana de interacción queda vacía o los jugadores deciden no agregar más efectos al chain stack.
5. **Resolución**: Los efectos incorporados se ejecutan en orden inverso a su activación (LIFO: Last In, First Out). Cada eslabón resuelve y determina si su ejecución fue exitosa o si fue alterada/negada basándose en las resoluciones de eslabones previos.
6. **Finalización**: Concluye el ciclo de vida de la cadena. El nuevo estado del juego, tras todas las resoluciones, puede convertirse instantáneamente en el **Evento generador** de una nueva cadena.

#### Plantilla (Fórmula) de la Cadena

```markdown
## Evento generador:
- (Acción del juego, resolución previa, o estado del tablero)

## Apertura:
- /CL1/: (v[x][n]) [Efecto o acción inicial]
  - [condición]: Condición para que se active este efecto (si aplica)
  - (costo): Acción nominal a fondo perdido (si aplica)
  - -ventana válida para-: [Lista de jerarquías o efectos disponibles en respuesta]

## Chain stack:
- /CL2/: (v[x][n]) [Efecto de respuesta al CL1]
  - [condición]: Condición para que se active este efecto (si aplica)
  - (costo): Acción nominal a fondo perdido (si aplica)
  - -ventana válida para-: [Lista de jerarquías o efectos disponibles en respuesta al CL2]
- /CL[N]/: ...
- /CL3/: (v[x][n]) [Efecto de respuesta a cualquier eslabón previo o estado actual]
  - [condición]: Condición para que se active este efecto (si aplica)
  - (costo): Acción nominal a fondo perdido (si aplica)
  - -ventana válida para-: [Lista de jerarquías o efectos disponibles en respuesta a cualquier otro eslabón previo o estado actual]

## Cierre: 
- Fin de la incorporación de efectos

## Resolución:
- /CL[N]/: [Descripción de la resolución del efecto N (Success/Failed)]
- /CL2/: [Descripción de la resolución del efecto 2 (Success/Failed)]
- /CL1/: [Descripción de la resolución del efecto 1 (Success/Failed)]

## Finalización
- Fin de la cadena actual
```

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
- Definición de presupuestos
- Gasto de aprendizaje vs gasto competitivo
- Presupuesto mensual asignado
- Planes de gasto
- Metas como duelista

### - Lore & Narrative
- Descubrimiento y conexión emocional con el juego
- Significado narrativo de los arquetipos
- Diferencia entre "cartas" y "personajes"

### - Mechanics
- Introducción a Mechanics
- Análisis de velocidades y nomenclatura
- Sintaxis de primitivas
- Desglose práctico de cartas en primitivas (Ej: Rikka)
- Jerarquías, costos y condiciones
- Dimensiones de procedencia y destino
- Regla de omisión nominal
- Diferenciación entre jerarquía de decisión y Spell Speed
- Ciclo de vida de un efecto (Latente a Finalizado)
- Administración de la cadena (Chain Stack)
- Etiqueta estructural de +Origen+
- Términos formales de referencia (Carta fuente, Propietario, Oponente)

### - Discovery
- El método Sandbox
- Extracción de primitivas
- Descomposición de decks insignia (Madolche)
- Exploración de decks desconocidos (The Weather Painter)

### - Pilotage
- Introducción al entorno competitivo
- Toma de decisiones
- Secuenciación correcta
- Aprovechamiento de recursos
- Ejecución de combos

### - Metagame and staples
- Evolución histórica del juego
- Análisis del Powercreep
- Herramientas de análisis

## Notas
- El archivo `Sistema de aprendizaje para Yu-Gi-Oh!.md` es el recurso didáctico del director, para administrar y guiar cualquier detalle que surja a lo largo del desarrollo docente de toda la academia. Aquí se plasman las decisiones a tomar durante el desarrollo del curso completo.
