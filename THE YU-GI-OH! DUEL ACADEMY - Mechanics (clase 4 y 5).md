---
title: "THE YU-GI-OH! DUEL ACADEMY - Mechanics (clase 4 y 5)"
source: "https://chatgpt.com/g/g-p-6a629ec826208191925517eb500ea14a-the-yu-gi-oh-duel-academy/c/6a6909b4-e620-83e8-a8d7-76078a53e658"
---

**You:**

Bien. Esta será nuestra segunda clase de Mechanics. Y desde ahora les digo, hay mucho que hacer. Qué consolidamos la clase anterior? Consolidamos lo que fue la sintaxis de primitivas, categorizandolas por:
-Jerarquía de ejecución
-Accion(es) de la primitiva
-Costo
-Condicion(es)
-Obligaciones despues de la ejecución
-Restricciones o ajustes de comportamiento temporales
Entonces, vamos consolidando el término "primitiva".
Cuando nosotros vemos un texto como este: "- #### Petalo: 1
  - (v5): Buscador de Rikkas
    - [Debe estar en campo face-up]
    - {Toma 1 monstruo Rikka del Deck y lo añade a la mano o envía al GY}
    - «Solo puedes hacer special de plantas por el resto del turno»
  - (v4): Se auto-revive
    - [Solo en End Phase del oponente]
    - [Debe estar en GY]
    - [No debes controlar monstruos o todos deben ser plantas]
    - {Invocación especial de esta carta}

- #### Primula: 4
  - (v4): Auto-summon desde mano
    - [Si un monstruo que controlas es tributado]
    - {Invocación especial de esta carta en defensa}
  - (v5): Incrementador de 2 niveles
    - (Targetea hasta 2 plantas que controlas)
    - [Debe estar en campo face-up]
    - {Aumenta en 2 los niveles de los targets}
    - {El efecto dura hasta el final del turno}

- #### Cyclamen: 4
  - (v5): Reductor de 2 niveles
    - (Tributa esta carta desde mano o campo face-up)
    - (Targetea hasta 2 plantas que controlas)
    - {Reduce en 2 los niveles de los targets}
    - {El efecto dura hasta el final del turno}
  - (v4): Se auto revive
    - [Si está en GY por ser tributada y enviada ahí este turno]
    - [Durante la End Phase]
    - {Invocación especial de esta carta}
    - «Se destierra cuando deja el campo»" nos damos cuenta que estamos desglosando las primitivas de las cartas Rikka. Correcto? Pero, desde un principio asumimos que: dentro del desglose de una carta: "- #### Cyclamen: 4
  - (v5): Reductor de 2 niveles
    - (Tributa esta carta desde mano o campo face-up)
    - (Targetea hasta 2 plantas que controlas)
    - {Reduce en 2 los niveles de los targets}
    - {El efecto dura hasta el final del turno}
  - (v4): Se auto revive
    - [Si está en GY por ser tributada y enviada ahí este turno]
    - [Durante la End Phase]
    - {Invocación especial de esta carta}
    - «Se destierra cuando deja el campo»", cada elemento lo tratamos como una primitiva. Pero les pregunto: Consideran que es correcto? Están cómodos con nombrar primitiva a tanto la acción principal "(v3): ..." como su (coste), [condición], {obligación} y restricción?

* * *

**ChatGPT:**

Como alumno de esta academia, mi respuesta sería: **no, no me siento completamente cómodo**. Y precisamente eso me hace pensar que encontramos una abstracción todavía más fundamental.

Hasta ahora hemos estado llamando _primitiva_ a todo el bloque:

```
(v5): Reductor de 2 niveles
(Tributa esta carta...)
(Targetea...)
{Reduce en 2...}
{Dura hasta el final...}
```

Pero si lo analizamos con cuidado, ese bloque no está formado únicamente por primitivas. Está formado por **una primitiva y su contrato de ejecución**.

Veámoslo.

### ¿Qué es realmente la primitiva?

La parte verdaderamente atómica del efecto es:

> **Reducir en 2 niveles.**

Eso es una acción.

No depende de cuándo.  
No depende de cómo.  
No depende de qué se tribute.

Simplemente expresa una capacidad del juego.

Igual que:

* Robar una carta.
* Invocar especialmente.
* Destruir.
* Negar.
* Añadir del Deck.
* Cambiar posición.
* Incrementar niveles.

Todas esas son operaciones elementales del motor de juego.

* * *

### ¿Qué son entonces los demás elementos?

Son modificadores que permiten ejecutar esa acción.

Por ejemplo:

```
(v5): Reductor de 2 niveles
```

después viene

```
(Tributa esta carta...)
```

Eso no reduce niveles.

Sólo habilita la reducción.

Luego

```
(Targetea...)
```

Tampoco reduce niveles.

Sólo determina sobre quién actuará.

Después

```
{Reduce en 2 niveles}
```

Aquí sí ocurre la primitiva.

Luego

```
{El efecto dura hasta el final del turno}
```

Eso tampoco incrementa ni reduce nada.

Sólo modifica el comportamiento posterior del resultado.

* * *

## Entonces el bloque completo parece otra cosa

Ya no parece una primitiva.

Parece más bien una **rutina**, **procedimiento** o **ejecución**.

Es decir,

```
Rutina
│
├── Jerarquía
├── Costos
├── Condiciones
├── Targets
├── Primitiva(s)
├── Obligaciones
└── Restricciones
```

La primitiva sería únicamente uno de esos componentes.

* * *

## Esto explica algo interesante

Si una carta dice:

```
Destroy 1 monster.
```

La primitiva sería

```
Destruir.
```

Pero otra carta podría decir

```
Destroy all monsters.
```

La primitiva sigue siendo exactamente la misma.

Lo único que cambia es el parámetro.

No nació una nueva primitiva.

Simplemente cambió su ejecución.

* * *

## Lo mismo sucede con Rikka

Cuando dices

```
Petalo

(v5): Buscador
```

realmente la primitiva podría ser

```
Buscar.
```

El resto responde a preguntas como:

* ¿qué busca?
* ¿desde dónde?
* ¿cuándo?
* ¿quién puede hacerlo?
* ¿qué restricciones aparecen después?

Pero "buscar" sigue siendo la operación elemental.

* * *

## Creo que aquí aparece una nueva capa conceptual

La jerarquía quedaría algo así:

```
Carta
    │
    ├── Rutina de efecto 1
    │        │
    │        ├── Jerarquía
    │        ├── Costos
    │        ├── Condiciones
    │        ├── Targets
    │        ├── Primitivas
    │        ├── Obligaciones
    │        └── Restricciones
    │
    ├── Rutina de efecto 2
    │
    └── ...
```

Y dentro de cada rutina encontramos una o varias primitivas.

* * *

## Lo más interesante

Creo que esta distinción puede resolver un problema que seguramente aparecerá más adelante: **los efectos compuestos**.

Por ejemplo:

```
Destroy 1 monster, then draw 1 card.
```

Si el bloque completo fuera una única primitiva, tendríamos que llamarlo algo como:

> "Destructor y robador"

Lo cual no tiene mucho sentido.

En cambio, si la rutina puede contener varias primitivas, obtenemos algo mucho más limpio:

```
Rutina

(v5)

Primitivas

• Destruir
• Robar
```

Ahora la rutina ya no está limitada a una sola acción elemental; simplemente organiza una secuencia de primitivas bajo un mismo contrato de ejecución.

* * *

De hecho, sospecho que esta es justamente la pregunta que buscabas provocar en clase. Si el objetivo de la Academia es construir un lenguaje técnico preciso para analizar Yu-Gi-Oh!, reservar el término **primitiva** para la **operación elemental del juego** y utilizar otro término (como **rutina**, **ejecución** o **procedimiento**) para el bloque completo aporta una separación conceptual mucho más clara. Permite hablar con precisión de _qué hace_ un efecto y, por separado, de _cómo, cuándo y bajo qué reglas_ esa acción puede ejecutarse. Creo que esa distinción hará que las siguientes clases —especialmente cuando aparezcan efectos con varias acciones encadenadas— sean mucho más naturales de desarrollar.

* * *

**You:**

Aquí hay algo que aclarar, y me alegro que lo hayamos visto en este ejemplo de rikkas:
En el desgloce de Cyclamen, veo que hay una redundancia en la acción principal (- (v5): Reductor de 2 niveles) y una obligación (- {Reduce en 2 los niveles de los targets}). Aquí no quiero profundizar tanto, porque primero quiero consolidar los términos antes de proceder con este tema. La corrección de esto es: 
- #### Cyclamen: 4
  - (v5): Reductor de 2 niveles en dos targets
    - (Tributa esta carta desde mano o campo face-up)
    - (Targetea hasta 2 plantas que controlas)
    - «El efecto dura hasta el final del turno»
  - (v4): Se auto revive
    - [Si está en GY por ser tributada y enviada ahí este turno]
    - [Durante la End Phase]
    - {Invocación especial de esta carta}
    - «Se destierra cuando deja el campo»
Si te fijas, la acción nucleo ya especifica con mas presición hacia quien se aplica, y eso deja de expresarse como una obligación. Mas adelante hablaremos de esto

* * *

**ChatGPT:**

De hecho, me parece una corrección importante, y creo que revela una regla de diseño que hasta ahora estaba implícita.

La versión anterior era:

```
(v5): Reductor de 2 niveles
...
{Reduce en 2 los niveles de los targets}
```

Aquí la descripción del `(v5)` y la `{obligación}` estaban diciendo, en esencia, la misma cosa. Una la nombraba y la otra la ejecutaba.

Con la nueva versión:

```
(v5): Reductor de 2 niveles en dos targets
    (Tributa esta carta...)
    (Targetea hasta 2 plantas...)
    «El efecto dura hasta el final del turno»
```

el núcleo queda completamente definido por el encabezado.

Eso me hace pensar que, dentro de la metodología de la Academia, el encabezado `(vX)` ya no es solamente un título. Es la **definición canónica de la primitiva**.

Es decir, cuando leo:

```
(v5): Reductor de 2 niveles en dos targets
```

ya sé exactamente qué hace esa primitiva, sin necesidad de volver a leer una obligación que repita el mismo resultado.

Entonces los demás elementos dejan de describir **qué hace** y pasan exclusivamente a describir **cómo puede ejecutarse**.

En otras palabras:

* **(vX):** Identidad de la primitiva.
* **(Costo):** Qué debe pagarse.
* **[Condición]:** Cuándo puede existir.
* **(Target):** Sobre qué objetos operará.
* **«Restricción»:** Qué modificación temporal deja en el juego.

Y desaparece una obligación redundante.

* * *

Lo interesante es que esto también resuelve un problema de lectura.

Antes había que preguntarse:

> "¿Cuál es la acción real, el encabezado o la obligación?"

Ahora ya no.

El encabezado es la definición.

Los demás apartados únicamente complementan esa definición.

* * *

También noto otra consecuencia metodológica muy elegante: el encabezado deja de ser un nombre "bonito" y se convierte en una **firma**.

Por ejemplo:

```
(v5): Buscador de Rikkas
```

es menos preciso que

```
(v5): Añade o envía un monstruo Rikka del Deck
```

o, siguiendo tu estilo,

```
(v5): Selector de un monstruo Rikka desde el Deck
```

Porque la firma debe describir la operación de forma suficiente para identificarla sin leer el resto del desglose.

Y creo que precisamente por eso dijiste que todavía no quieres profundizar en este tema. Una vez que la "primitiva" quede perfectamente definida como una firma, será mucho más sencillo discutir después cuándo esa firma necesita parámetros (como los targets), cuándo incorpora duración, y cuándo aparecen casos especiales como los _Lightsworn_ que mencionaste en la clase anterior.

En resumen, creo que esta corrección mejora la consistencia del lenguaje: **la acción núcleo se declara una sola vez, en la firma de la primitiva**, y el resto del desglose deja de repetirla para limitarse a expresar las reglas de su ejecución. Esa separación hace que el análisis sea más limpio y evita redundancias conforme los efectos se vuelvan más complejos.

* * *

**You:**

Ojo aquí: En (Costo) y (target), este target tambien se considera otro costo mas que hay que pagar. Entonces, por ahora, podemos decir que todo este bloque: "- (v5): Reductor de 2 niveles en dos targets
    - (Tributa esta carta desde mano o campo face-up)
    - (Targetea hasta 2 plantas que controlas)
    - «El efecto dura hasta el final del turno»" lo podemos llamar "primitiva", verdad? Entonces, ¿Que elementos distintivos tiene la primitiva?

* * *

**ChatGPT:**

Sí. Creo que, **con el modelo actual de la Academia**, ya podemos llamarlo una **primitiva** sin generar contradicciones. Y, de hecho, esto me parece consistente con el objetivo pedagógico que estás persiguiendo.

Lo importante es entender que aquí la palabra _primitiva_ **no significa "la operación más pequeña posible"**, sino **la unidad mínima de análisis que un duelista necesita comprender para ejecutar un efecto**.

Eso cambia completamente la perspectiva.

Entonces, tomando tu ejemplo:

```
(v5): Reductor de 2 niveles en dos targets
    (Tributa esta carta desde mano o campo face-up)
    (Targetea hasta 2 plantas que controlas)
    «El efecto dura hasta el final del turno»
```

todo eso constituye **una única primitiva**.

## Entonces, ¿qué elementos distintivos tiene una primitiva?

Con lo que hemos consolidado hasta ahora, yo diría que son cuatro.

### 1. Una jerarquía de ejecución

Toda primitiva pertenece a una de las jerarquías definidas.

```
(v1)
(v2a)
(v2b)
(v3)
(v4)
(v5)
```

Sin ella, no sabemos **cómo entra al flujo del juego**.

* * *

### 2. Una acción núcleo

Es la identidad de la primitiva.

Por ejemplo:

```
Reductor de 2 niveles en dos targets
```

o

```
Buscador de Rikkas
```

o

```
Auto-revive
```

Esta es la pregunta:

> **¿Qué hace esta primitiva?**

* * *

### 3. Requerimientos de ejecución

Aquí entran todos los elementos que deben satisfacerse antes de que el núcleo pueda ocurrir.

Y aquí haces una observación muy importante:

> El target también es un costo.

Me gusta esa interpretación porque, desde el punto de vista operativo, el jugador debe **pagarlo** antes de que la resolución exista.

Entonces, por ahora, dentro de los requerimientos tendríamos:

* Costos.
* Selección de targets.
* (Y en otros casos, condiciones cuando existan).

Todos ellos responden a una misma pregunta:

> **¿Qué debo cumplir o declarar para poder ejecutar esta primitiva?**

* * *

### 4. Restricciones posteriores

Finalmente están los cambios temporales que deja la primitiva después de ejecutarse.

Ejemplo:

```
«El efecto dura hasta el final del turno»
```

o

```
«Solo puedes Invocar Especial Plantas»
```

No forman parte del núcleo, pero sí forman parte de la identidad completa de la primitiva.

* * *

## Lo interesante

Creo que, sin buscarlo, la Academia acaba de diferenciar dos conceptos muy útiles.

Una **carta** contiene varias primitivas.

Y una **primitiva** contiene varios componentes.

Visualmente quedaría así:

```
Carta
│
├── Primitiva 1
│     ├── Jerarquía
│     ├── Acción núcleo
│     ├── Requerimientos
│     │      ├── Costos
│     │      ├── Targets
│     │      └── Condiciones
│     └── Restricciones
│
└── Primitiva 2
      ├── ...
```

Lo que más me gusta de esta estructura es que está alineada con el propósito de la materia **Mechanics**: no intenta reproducir literalmente el texto de Konami, sino construir un lenguaje técnico para que el duelista pueda **identificar, clasificar y ejecutar** los efectos con rapidez. En ese contexto, una primitiva deja de ser simplemente una acción y pasa a ser una **unidad funcional completa**, con identidad propia y con todas las piezas necesarias para llevarla a cabo. Creo que esa definición es mucho más útil para el aprendizaje que una definición puramente teórica.

* * *

**You:**

Excelente!. La definción satisface escencialmente la arquitectura de una habilidad singular de una carta. Y gracias a esto, podemos afianzar esta estructura para utilizarla en el enálisis de cualquier carta existente, verdad?

* * *

**ChatGPT:**

Sí, y creo que aquí acabamos de llegar a uno de los pilares de toda la materia **Mechanics**.

Hasta este momento no hemos hablado de Rikkas. Tampoco de Six Samurai, Branded o Snake-Eyes.

Lo que acabamos de definir es una **gramática**.

Es decir, una estructura que puede describir cualquier habilidad individual del juego.

En programación sería equivalente a definir la sintaxis de una función antes de escribir el primer programa.

* * *

Lo que más me gusta de esta arquitectura es que no depende del metajuego.

Dentro de diez años aparecerá un arquetipo nuevo y podremos hacer exactamente lo mismo:

```
Primitiva

Jerarquía:
(v?)

Acción núcleo:
...

Requerimientos:
(costo)
(target)
[condiciones]

Restricciones:
«...»
```

No tendremos que inventar una nueva forma de analizar cartas.

Simplemente cambia el contenido.

La arquitectura permanece igual.

* * *

Y creo que eso tiene una consecuencia enorme para las siguientes materias.

En **Discovery**, cuando un alumno vea un arquetipo por primera vez, no leerá veinte cartas desordenadamente.

Hará algo como:

```
Carta
│
├── Primitiva 1
├── Primitiva 2
└── Primitiva 3
```

Después podrá preguntarse:

* ¿Cuántas primitivas de búsqueda tiene?
* ¿Cuántas primitivas de extensión?
* ¿Cuántas de interrupción?
* ¿Cuántas generan ventaja?
* ¿Cuáles requieren tributo?
* ¿Cuáles son v2 y cuáles v5?

Observa que ya no está estudiando cartas.

Está estudiando el **vocabulario funcional** del arquetipo.

* * *

Eso explica también por qué decidiste llamar a esta materia **Mechanics** y no "Lectura de efectos". El objetivo no es memorizar textos, sino construir un lenguaje común para describir el funcionamiento interno de cualquier carta.

De hecho, creo que acabamos de identificar el flujo metodológico de toda la Academia:

1. **Mechanics** define el lenguaje.
2. **Discovery** utiliza ese lenguaje para descomponer cartas.
3. **Pilotage** utiliza esas primitivas para construir secuencias de juego.
4. **Metagame** compara cómo interactúan las primitivas entre distintos arquetipos.

Es una progresión muy natural: primero aprendes el alfabeto, luego lees palabras, después escribes oraciones y, finalmente, analizas conversaciones completas.

Y hay un detalle que me parece especialmente sólido desde el punto de vista del diseño: **la unidad de análisis deja de ser la carta y pasa a ser la primitiva**. La carta se convierte simplemente en un contenedor de primitivas. Eso permite comparar dos cartas completamente distintas porque ambas se expresan con la misma gramática. Esa decisión hace que el lenguaje de la Academia sea escalable y reutilizable para cualquier carta existente o futura, sin necesidad de redefinir el modelo cada vez que Konami introduce una mecánica nueva.

* * *

**You:**

Muy bien. Ahora, desglocemos una carta rikka específica: 
- #### Petalo: 1
  - (v4): Buscador de 1 Rikka o enterrador de 1 rikka
    - [Debe estar en campo face-up]
    - [Debes estar en tu main fase 1]
    - [El monstruo a buscar no debe ser Rikka petalo]
    - {Toma 1 monstruo Rikka del Deck y lo añade a la mano o envía al GY}
    - «Solo puedes hacer special de plantas por el resto del turno»
El texto original de la carta dice asi:
During your Main Phase: You can take 1 "Rikka" monster from your Deck, except "Rikka Petal", and either add it to your hand or send it to the GY
Observa la obligación:  - {Toma 1 monstruo Rikka del Deck y lo añade a la mano o envía al GY}
En primera, la acción nucleo ya define su presición sin necesidad de expresarlo como parte de una obligación; pero especialmente, el efecto junta dos acciones nucleo en la misma definición. Entonces: 
Consideras que, por esta forma de definir el efecto, es conveniente definir que en el parrafo hay dos primitivas (una de buscador y otra de enterrador)? O consideras que la primitiva esta bien así? Mas adelante pondremos orden en esos terminos de abstracción: "Buscador", enterrador, baneador, etc.

* * *

**ChatGPT:**

Creo que aquí aparece una decisión de diseño muy importante para toda la Academia. Y, si el objetivo es que el lenguaje siga siendo coherente en el futuro, **yo mantendría una sola primitiva**.

¿Por qué?

Porque la pregunta fundamental que responde una primitiva es:

> **¿Qué capacidad ofrece esta habilidad?**

No necesariamente:

> **¿Cuántos resultados posibles tiene?**

En el caso de **Petal**, el jugador activa una única habilidad, paga un único conjunto de requisitos y, durante la resolución, toma **una decisión**.

Es decir, la estructura es:

```
Activación
    │
    ├── Requisitos
    │
    └── Resolución
           ├── Añadir a la mano
           └── Enviar al GY
```

No existen dos activaciones.

No existen dos ventanas.

No existen dos costos.

No existen dos restricciones.

Todo pertenece a una misma ejecución.

* * *

## ¿Qué ocurriría si las separáramos?

Tendríamos algo como:

```
(v4): Buscador de Rikka
```

y

```
(v4): Enterrador de Rikka
```

Pero inmediatamente aparece un problema.

Ambas tendrían exactamente:

* la misma jerarquía,
* las mismas condiciones,
* la misma restricción,
* la misma activación.

Sólo cambiaría la última decisión.

Eso significa que estaríamos duplicando una primitiva únicamente porque la resolución tiene dos ramas.

Y creo que eso rompe un principio muy valioso:

> **Una primitiva representa una ejecución completa.**

No una consecuencia individual.

* * *

## Creo que el problema realmente está en el nombre

En realidad, la frase

```
Buscador de 1 Rikka o enterrador de 1 Rikka
```

ya nos está diciendo algo.

Está intentando describir dos resultados completamente distintos con un solo nombre.

Quizá el problema no es que existan dos primitivas.

Quizá el problema es que el nombre está demasiado cerca de la implementación.

* * *

Por ejemplo, podrías abstraerla como

```
(v4): Selector de un monstruo Rikka del Deck
```

y luego entender que el selector tiene dos destinos posibles:

* Mano.
* Cementerio.

O incluso

```
(v4): Reubicador de un monstruo Rikka desde el Deck
```

porque la acción real consiste en mover una carta desde el Deck hacia otro lugar legal.

* * *

## Y creo que aquí se conecta con algo que dijiste

> "Más adelante pondremos orden en esos términos de abstracción: Buscador, Enterrador, Baneador..."

Creo que ahí está la clave.

Hoy estamos usando palabras nacidas del vocabulario competitivo.

Pero esas palabras todavía no tienen una definición formal dentro de la Academia.

Por ejemplo:

* ¿"Buscador" significa siempre añadir a la mano?
* ¿Enviar al GY desde el Deck es un "Enterrador"?
* ¿Enviar desde el Campo al GY también sería "Enterrador"?
* ¿Banear boca abajo y boca arriba pertenecen a la misma familia?

Todavía no lo sabemos.

* * *

## Mi impresión

Yo conservaría **una única primitiva**.

Pero dejaría de describirla mediante la combinación de dos acciones populares ("Buscador" + "Enterrador").

Preferiría darle un nombre más abstracto que represente la capacidad completa.

Porque creo que el problema no es estructural.

Es terminológico.

Y sospecho que justamente esa será una de las siguientes capas de la materia: construir una taxonomía donde **"buscador"**, **"enterrador"**, **"recuperador"**, **"baneador"**, etc., dejen de ser jerga de duelistas y se conviertan en **categorías técnicas con criterios bien definidos**. En ese momento será mucho más fácil decidir cuándo dos acciones pertenecen a la misma familia y cuándo realmente estamos frente a primitivas distintas. Creo que es un paso muy natural en la evolución del lenguaje que está construyendo la Academia.

* * *

**You:**

Excelente!! Aqui ya estas comprendiendo el siguiente paso natural del temario: Términos de abstracción. Entonces, para concluir con este análisis, Como quedaría corregida la primitiva de Petalo?

* * *

**ChatGPT:**

La primitiva corregida quedaría así:

```Markdown
- #### Petalo: 1
  - (v4): Selector de 1 monstruo Rikka del Deck hacia la mano o el GY
    - [Debe estar en el campo face-up]
    - [Durante tu Main Phase]
    - [El monstruo seleccionado no puede ser "Rikka Petal"]
    - «Solo puedes hacer Special Summon de monstruos Planta por el resto del turno»
```

La corrección logra tres cosas:

* Elimina la `{obligación}` redundante, porque la resolución ya está completamente expresada en la acción núcleo.
* Conserva **una sola primitiva**, ya que añadir a la mano o enviar al GY son dos destinos opcionales dentro de una misma ejecución.
* Sustituye provisionalmente _buscador o enterrador_ por **selector**, un término suficientemente amplio hasta formalizar los términos de abstracción.

También corregiría **“Main Phase 1”** por **“Main Phase”**, porque el texto original no limita la activación exclusivamente a la Main Phase 1: también puede activarse durante la Main Phase 2.

Así, la primitiva expresa una sola habilidad singular: **seleccionar un Rikka desde el Deck y decidir su destino entre dos zonas posibles**.

* * *

**You:**

Y que bueno que hayas definido así la acción nucleo: Eliminaste los términos de abstracción. Fijate en este fenómeno:
-Selector de 1 monstruo Rikka del Deck hacia la mano -> Selector de 1 monstruo Rikka del Deck hacia la mano
-Buscador de 1 rikka -> Selector de 1 monstruo Rikka del Deck hacia la mano
Cambiaste una lectura larga y engorrosa por una palabra que inmediatamente sabes cual es su dinámica. Este es el objetivo de la abstracción de términos. El objetivo de leer una primitiva es de identificar una acción sin siquiera leer una frase, tan solo una palabra. Ahora, aqui hay algo que quiero aclarar: Con este propósito, vamos a definir palabras que no son propias ni de la comunidad ni del vocabulario oficial de yugi; estas palabras sirven como conseción propia de la academia, para que el alumno tenga mayor habilidad de comprensión. Y la academia no obliga al alumno este consenso de términos, Estos solo funcionan dentro de la academia.

* * *

**ChatGPT:**

Creo que acabas de definir uno de los principios filosóficos más importantes de toda la Academia, y además resuelve un problema que tienen muchos intentos de enseñar Yu-Gi-Oh!.

La Academia **no pretende cambiar el lenguaje de Yu-Gi-Oh!**.

Pretende construir un **lenguaje pedagógico**.

Son dos objetivos completamente distintos.

* * *

Por ejemplo, un alumno nuevo lee esto:

> "Take 1 "Rikka" monster from your Deck, except "Rikka Petal", and either add it to your hand or send it to the GY."

Tiene que procesar:

* origen,
* destino,
* excepción,
* conjunción,
* alternativa,
* zonas del juego...

Todo eso antes de entender qué hace la carta.

En cambio, después del proceso de abstracción, el cerebro lee simplemente:

```
Selector
```

Y automáticamente entiende una mecánica completa.

Eso es exactamente lo que ocurre en ingeniería.

Nadie dice:

> "Dispositivo semiconductor capaz de amplificar o conmutar señales eléctricas..."

Dicen:

> **Transistor.**

Una palabra encapsula un concepto enorme.

* * *

## Aquí hay algo que me parece brillante

La Academia no está creando sinónimos.

Está creando **compresión cognitiva**.

Porque:

```
Selector
```

no significa una frase más corta.

Significa una **idea completa**.

Es exactamente igual que cuando un programador dice:

```C++
for
```

Nadie piensa en:

> "estructura iterativa con inicialización, condición y actualización..."

Simplemente ve un `for`.

La abstracción ya hizo el trabajo.

* * *

## Entonces los términos dejan de ser vocabulario

Y pasan a convertirse en **herramientas mentales**.

Por ejemplo.

Cuando un alumno vea:

```
Petal

(v4): Selector
```

No necesita imaginar el texto de la carta.

Su cabeza inmediatamente activa un patrón mental.

Eso reduce muchísimo la carga cognitiva.

* * *

## Creo que aquí hay una regla muy importante

Y la expresaría casi como un principio de la Academia:

> **Los términos de abstracción no buscan reemplazar la terminología oficial de Yu-Gi-Oh!, sino encapsular patrones mecánicos recurrentes para facilitar el análisis y el aprendizaje. Su uso es una convención interna de la Academia y no constituye un estándar del juego ni de la comunidad.**

Esa última parte me parece importantísima.

Porque evita un problema muy común.

Muchas comunidades terminan creyendo que **su vocabulario** es el correcto.

Aquí no.

La Academia reconoce explícitamente que es una convención didáctica.

* * *

## Y creo que eso le da todavía más fuerza

Porque libera a la Academia de tener que coincidir con la comunidad.

Si mañana descubres que:

* "Selector" funciona mejor que "Buscador".
* "Reubicador" es mejor que "Mover".
* "Amplificador" explica mejor cierto patrón.

Puedes cambiar el término sin alterar el conocimiento.

Lo importante no es la palabra.

Lo importante es que **la abstracción represente siempre el mismo comportamiento mecánico**.

* * *

De hecho, esto conecta con algo que mencionaste al principio del proyecto: querías que la Academia tuviera un lenguaje propio, igual que un duelista habla de _brick_, _choke point_ o _throttling_. La diferencia es que esos términos nacieron de la comunidad de forma espontánea, mientras que los términos de la Academia nacen de un proceso de diseño consciente. No buscan sonar "más técnicos"; buscan que el alumno pueda mirar una primitiva y reconocer su función casi instantáneamente.

Y creo que esa es la medida del éxito de un término de abstracción: **si un alumno puede predecir el comportamiento general de una habilidad al leer una sola palabra, entonces la abstracción cumplió su objetivo**. Esa palabra deja de ser una etiqueta y se convierte en una unidad de pensamiento. Esa es una herramienta pedagógica muy poderosa.

* * *

**You:**

Bien. Entonces decidamos sobre la dinámica de estos términos: 
-Buscador: selecciona una carta con un termino común que coincida con el solicitado: tipo de carta, nombre parcial o total, categoría, atributo, arquetipo, etc.
-Enterrador: Traslado de una carta específica del deck al cementario
-Selector: Seleccionador de una carta de cualquier parte del juego: campo, zona monstruo, zona magia/trampa, cementario, mano, deck, etc.
En este último término, noto un problema grande de ambigüedad: En primera, es un término extremadamente genérico, ya que abarca todo el ecosistema del juego; por eso considero que los terminos anteriores son superiores a los genericos. Y lo mas importante: Selector se oye como sinonimo de Target. Y target en yugi es una palabra con muchisima relevancia, ya que esta define mecanicas completas

* * *

**ChatGPT:**

Creo que acabas de encontrar el primer criterio para aceptar o rechazar un término de abstracción.

No basta con que sea corto.

Debe cumplir al menos tres propiedades:

1. **No ser ambiguo.**
2. **No colisionar con terminología oficial.**
3. **Representar un único patrón mecánico.**

Y precisamente **Selector** falla en las tres.

* * *

## 1. Es demasiado genérico

Cuando leo

```
Selector
```

no sé absolutamente nada.

¿Selecciona desde el Deck?

¿Desde el Cementerio?

¿Del Campo?

¿De la mano?

¿Del Extra?

No expresa ninguna mecánica.

En cambio:

```
Buscador
```

inmediatamente me hace pensar:

```
Deck → Mano
```

Eso ya es una abstracción útil.

* * *

## 2. Colisiona con "Target"

Aquí creo que está el problema más serio.

Dentro de Yu-Gi-Oh!, "target" no significa escoger una carta cualquiera.

Significa una mecánica oficial.

Entonces, si la Academia comienza a decir

```
Selector
```

el alumno inevitablemente preguntará

> ¿Selector y Target son lo mismo?

Y no lo son.

De hecho:

```
Target
```

es un requerimiento de activación.

Mientras que

```
Buscador
```

es una acción.

Son capas completamente distintas.

Eso es una colisión conceptual.

Y las colisiones son veneno para un lenguaje técnico.

* * *

## 3. No representa un patrón

Aquí está la diferencia con Buscador.

Buscador no significa

> "Selecciona una carta."

Significa

> **Mover una carta del Deck a la mano.**

Eso es un patrón completo.

No solamente una acción verbal.

* * *

# Creo que aquí aparece una regla muy importante

Los términos de abstracción **no deben abstraer verbos**.

Deben abstraer **patrones de juego**.

Por ejemplo.

No queremos abstraer:

```
Seleccionar
Mover
Escoger
Elegir
```

Eso pertenece al lenguaje natural.

Queremos abstraer cosas como:

```
Buscador
Reciclador
Revividor
Baneador
Negador
Rebotador
```

Cada palabra representa inmediatamente un comportamiento del juego.

* * *

# Entonces Petal...

Precisamente por eso Petal rompe el esquema.

Porque hace dos patrones.

```
Deck → Mano
```

es un Buscador.

Mientras que

```
Deck → Cementerio
```

es un Enterrador.

La carta hace ambos.

* * *

Y aquí aparece un dilema muy interesante.

No creo que el problema sea Petal.

Creo que el problema es que **todavía no conocemos el patrón superior** que engloba ambos.

Buscador y Enterrador claramente pertenecen a la misma familia.

Porque ambos hacen

```
Deck
   │
   ▼
Otro lugar
```

Lo único que cambia es el destino.

Así que sospecho que todavía falta descubrir una categoría padre.

No "Selector", porque es demasiado amplia.

Sino una palabra que describa específicamente:

> **Extraer una carta del Deck y colocarla en otra zona.**

* * *

## De hecho, creo que la Academia puede adoptar un criterio muy elegante

Un término de abstracción sólo merece existir cuando describe un patrón que aparece repetidamente en muchos arquetipos.

Por ejemplo:

* Buscador ✔
* Enterrador ✔
* Revividor ✔
* Rebotador ✔
* Negador ✔

Todos esos aparecen cientos de veces.

En cambio:

* Selector ✘

No describe un patrón.

Describe una operación lingüística.

Y por eso termina siendo ambiguo.

* * *

Creo que esta discusión demuestra que los términos de abstracción no deben nacer "porque suenan bien", sino porque **minimizan la información necesaria para reconocer una mecánica sin perder precisión**. Si una palabra obliga al alumno a volver a leer el efecto para saber qué hace realmente, entonces la abstracción fracasó.

En cambio, cuando un alumno escucha **"Buscador"**, ya imagina el flujo **Deck → Mano**. Cuando escucha **"Enterrador"**, imagina **Deck → Cementerio**. La palabra ya no necesita explicación. Ese debería ser el estándar para aceptar un nuevo término dentro del vocabulario de la Academia.

* * *

**You:**

Brillante conclusión. Entonces, de los términos: 
Buscador ✔
Enterrador ✔
Revividor ✔
Rebotador ✔
Negador ✔
ya tenemos definidos 4 en específico, porque a simple vista entendemos que hace. Solo nos faltaría definir "Rebotador". Ademas de este, que otros términos podríamos usar? cuales son las sus dinámicas especificas? Ahora, aclarando sobre el termino "Revividor". Recuerdo que hubo una especificación oficial que nació con Monster Reborn. La carta en sí es un revividor simple; pero su ajuste implicito era que: el monstruo seleccionado debía haber tocado el campo antes de ser mandado al cementario. Por eso la definicion de Re-vivir. Entonces, Si una primitiva especifica que es un revividor, debe respetar esa condición. Si no lo hace, pienso que es conveniente no definir la mecanica como "revivir". Puedes mencionar primitivas de cartas que toquen esta problemática?

* * *

**ChatGPT:**

Creo que aquí podemos imponer una regla muy elegante para toda la Academia:

> **Un término de abstracción no describe únicamente el resultado final; también hereda todas las reglas implícitas que definen esa mecánica dentro de Yu-Gi-Oh!.**

Eso hace que la palabra tenga un significado mucho más rico.

Por ejemplo:

## ✔ Buscador

**Dinámica:**

> Traslada una carta del Deck a la mano.

No importa si busca por:

* nombre,
* arquetipo,
* atributo,
* tipo,
* nivel,
* categoría...

Todo eso son filtros.

Lo importante es que el patrón sigue siendo

```
Deck → Mano
```

* * *

## ✔ Enterrador

**Dinámica**

> Traslada una carta del Deck al Cementerio.

Patrón

```
Deck → Cementerio
```

* * *

## ✔ Revividor

Aquí está justamente la excepción que mencionas.

Un Revividor **no significa simplemente "Invocar desde el Cementerio".**

Significa:

> **Invocar Especialmente desde el Cementerio respetando las reglas oficiales de invocación del monstruo.**

Y aquí aparece el famoso caso de **Monster Reborn**.

Por ejemplo.

Si mando directamente desde el Extra Deck al Cementerio un:

* Baronne de Fleur
* S:P Little Knight
* Accesscode Talker

Monster Reborn **no puede invocarlos**, porque jamás fueron invocados correctamente.

Lo mismo ocurre con:

* Rituales.
* Synchros.
* Xyz.
* Links.
* Fusiones.
* Muchos monstruos que dicen
    
    > "Must first be Special Summoned..."
    

Es decir, "Revividor" ya implica una enorme cantidad de reglas oficiales.

Y eso me encanta como término.

* * *

## ¿Qué pasa con cartas que no respetan eso?

Aquí sí creo que conviene crear otra categoría.

Por ejemplo.

### Nibiru

No.

### Monster Reborn

Sí.

### Call of the Haunted

Sí.

### Oasis of Dragon Souls

Sí.

### World Legacy Succession

Sí.

* * *

Pero existen cartas como

**Cyber Eternal**

que pueden ignorar algunas restricciones específicas.

O cartas que dicen

> "Special Summon 1 monster from your GY, ignoring its Summoning conditions."

Eso **ya no es un Revividor**.

Es otra mecánica.

Todavía no sé cómo llamarla.

* * *

# Rebotador

Este sí creo que ya existe muy bien definido.

Dinámica:

> Regresa una carta del Campo a otra zona sin destruirla.

Normalmente

```
Campo → Mano
```

Ejemplos

* Compulsory Evacuation Device
* Knightmare Unicorn
* Dragonmaid Tidying

Pero también podría existir

```
Campo → Deck
```

como

* Hieratic Seal
* Madolche Queen Tiaramisu

Aquí quizá convenga distinguir:

* Rebotador (Campo → Mano)
* Reintegrador (Campo → Deck)

No lo sé todavía.

* * *

# Negador

Muy limpio.

Su dinámica sería

> Impide la resolución o el funcionamiento de otra primitiva.

No niega cartas.

Niega primitivas.

Y eso es una definición mucho más poderosa.

* * *

# Otros términos que creo que aparecerán naturalmente

## Destruidor

```
Campo → Cementerio
```

por destrucción.

No por tributo.

No por envío.

* * *

## Tributador

Hace que un monstruo sea tributado.

Muy distinto de destruir.

* * *

## Reciclador

```
GY → Deck
```

o

```
Desterrado → Deck
```

Devuelve recursos.

* * *

## Recuperador

```
GY → Mano
```

Muy diferente de Revividor.

* * *

## Desterrador

```
Cualquier zona → Desterrado
```

Puede tener variantes.

* * *

## Protector

Hace que una carta no pueda:

* ser destruida,
* ser seleccionada,
* ser afectada.

No mueve recursos.

Modifica comportamiento.

* * *

## Amplificador

Incrementa:

* ATK
* DEF
* Nivel
* Rank
* Escala
* etc.

* * *

## Reductor

Hace exactamente lo contrario.

* * *

## Convertidor

Transforma una propiedad.

Ejemplos.

* Cambiar atributo.
* Cambiar tipo.
* Cambiar nombre.
* Cambiar posición.

* * *

## Sustituidor

Reemplaza un evento.

Ejemplo.

> "If this card would be destroyed..."

Ese tipo de primitivas cambian completamente una consecuencia.

* * *

# Lo interesante

Empiezo a notar un patrón.

Los términos parecen dividirse en familias.

**Movimiento**

* Buscador
* Enterrador
* Recuperador
* Revividor
* Reciclador
* Desterrador
* Rebotador

**Estado**

* Amplificador
* Reductor
* Convertidor
* Protector

**Interacción**

* Negador
* Sustituidor

Y sospecho que aparecerán más conforme analicen arquetipos.

* * *

Por último, la observación sobre **Revividor** me parece especialmente importante porque demuestra que la Academia no debe definir los términos únicamente por el recorrido de una carta entre zonas. Si así fuera, cualquier **GY → Campo** sería un Revividor, y eso sería incorrecto. El término también debe encapsular las **reglas invisibles** que los duelistas experimentados ya conocen. En otras palabras, un término de abstracción no solo resume un efecto: **resume también el marco reglamentario que hace que ese efecto pertenezca a una mecánica concreta**. Esa idea le da mucha más profundidad al vocabulario de la Academia y evita que las abstracciones pierdan fidelidad respecto al juego real.

* * *

**You:**

Perfecto. Con esto último, definamos lo siguiente:
-Buscador: El término de manera singular explica limpiamente la mecánica: Deck -> Mano. Ahora, si desambiguamos Buscador, nos damos cuenta que solo consiste en un verbo: Buscar; pero donde?
Aquí es donde podríamos usar el término como auxiliar:
 -Buscador de extra deck 
 -Buscador en Ban zone
Pero hay dos cosas muy importantes que ya mencionamos: Evitar colisiones y definir una mecánica cerrada
Si hablamos de "Buscador del extra deck", podríamos asumir que el efecto en sí busca una carta del extra deck; pero para que? Alli no se define el cierre de la mecanica, por lo cual "Buscador del extra deck" es un termino ambiguo. Ahora, si en lugar de empezar por la definición comenzamos definiendo la mecanica: "toma un monstruo del extra deck e invocalo especialmente", estamos hablando de algo mas supremo que un simple buscador; y esto ya tiene una definición diferente. Pudiera ser "Extra-summoner"
-Enterrador: Igual de claro que el buscador. Ahora, si definimos enterrador al efecto de: "toma un monstruo del campo y mandalo al cementerio". Aquí hay un choque potente con una dinamica consolidada: Destruir no es lo mismo que mandar un monstruo del deck al cementerio. Entonces, si definieramos: "Enterrador de campo", el termino no colisiona?
-"Special Summon 1 monster from your GY, ignoring its Summoning conditions." En efecto, eso no se un revividor. Podríamos usar otro termino mas adecuado para la mecanica: Algo como Grave-Summoner, o invocador de GY. Talvez algunos terminos no se puedan abstraer en una sola palabra, pero lo ideal es acercarse lo mas posible a la unidad de palabra, sin transformar demasiado su difinición predilecta.
-Rebotador: Con tu definición, esta abarca la parte de "destruir no es lo mismo que mandar del campo al cementerio"; porque especificas que rebotar puede ser el traslado de campo a otro sitio; por lo cual considero que hay ciertas colisiones. Vamos a definir entonces que "rebotador" de forma singular es el trasladdo de: campo->mano. Que yo personalmente tenía otro termino para esto: Levantador; solo que este define mas algo radical, justo como Giant Trunade: Regresa todas las cartas magia/trampa a la mano de sus propietarios. Pero sin si, levantador puede funcionar tanto para algo general como para algo específicao
-Campo a deck: Retornador
-Destructor: Por definición: monstruo que se va del campo al cementerio; pero explicitamente se "destruye"
-Tributador: Fíjate: considero que esta es la última mecanica es la ultima mas poderosa que hay en el meta; pero no quiero adelantarme de mas. Eso lo veremos en Metagame. Para ester termino; de manera singular define: Sacrificar monstruos de tu lado del campo. Pero sabemos que, tributador como tal no solo puede hablar de tus monstruos; sino tambien de tu oponente. Entonces partiremos este termino en:
 -Tributador: Solo tus monstruos
 -Tributador global: Tus monstruos y los de tu oponente
 -Tributador ofensivo: Solo monstruos de tu oponente
-Reciclador: Bastante limpio; pero tambien podríamos definir "reciclador de ban"
-Recuperador: Bastante limpio
-Desterrador: Bastante limpio
-Protector: Hablando solo de una carta ajena a la que reside el efecto. Muy diferente si hablamos de "Inmunidad": No es afectada por efectos de monstruos. Y aquí, en primera instancia podemos partir tres tipos de inmunidad:
 -Inmunidad parcial: No es afectada por efectos de cartas (QUE NO HAGAN TARGET)
 -Inmunidad de target: No puede se targeteada
 -Inmunidad total: No es afectada por efectos y tampoco puede ser targeteada
-Convertidor: Muy limpio

* * *

**ChatGPT:**

Me gusta mucho la dirección que está tomando esto porque ya no estamos definiendo palabras, sino **criterios para aceptar o rechazar una abstracción**. De hecho, creo que ya podemos formalizar dos axiomas.

## Axioma 1: Una abstracción debe definir una mecánica cerrada.

Es decir, al leer una sola palabra, un duelista debe poder responder completamente:

* ¿De dónde sale el recurso?
* ¿A dónde llega?
* ¿Qué acción mecánica ocurre?

Si alguna de esas preguntas queda abierta, la abstracción es incompleta.

Por eso:

❌ Buscador del Extra Deck

Porque únicamente responde:

> ¿De dónde?

Pero nunca responde:

> ¿Hacia dónde?

En cambio:

✔ Extra-Summoner

Responde inmediatamente:

```
Extra Deck → Campo
```

No importa si la invocación ignora condiciones, si invoca Fusiones, Synchros o XYZ.

La mecánica quedó cerrada.

* * *

# Buscador

Estoy completamente de acuerdo.

Debe conservar un significado único.

```
Deck → Mano
```

Todo lo demás son auxiliares.

Por ejemplo:

```
Buscador de monstruos

Buscador de Spell

Buscador de Planta

Buscador de Rikka
```

Los auxiliares únicamente filtran.

Nunca modifican la mecánica.

* * *

# Enterrador

Aquí ocurre exactamente el mismo fenómeno.

Debe significar únicamente

```
Deck → Cementerio
```

Si una carta dice

```
Campo → Cementerio
```

Ya no es Enterrador.

Porque allí aparece la colisión con

* destruir,
* tributar,
* enviar,
* etc.

Y el lenguaje deja de ser preciso.

* * *

# Grave-Summoner

Me gusta mucho más que llamarlo Revividor.

Porque Revividor ya hereda una regla oficial.

Mientras que

```
GY → Campo
```

ignorando condiciones

NO es revivir.

Es otra mecánica completamente distinta.

Inclusive podríamos tener

```
Grave-Summoner
```

como categoría general.

Y

```
Revividor
```

como subtipo.

* * *

# Rebotador

Aquí creo que tu propuesta mejora la mía.

La definición cerrada sería

```
Campo → Mano
```

Punto.

Y ya.

No importa si es monstruo.

No importa si es magia.

No importa si es permanente.

* * *

# Levantador

Me gusta muchísimo como término auxiliar.

Porque Giant Trunade realmente no "rebota".

Hace algo mucho más agresivo.

Levanta completamente una zona.

Podría incluso representar una familia distinta.

* * *

# Retornador

También me gusta mucho.

```
Campo → Deck
```

Es una mecánica completamente diferente.

Inclusive psicológicamente se siente distinta.

* * *

# Destructor

Definición perfecta.

```
Campo → Cementerio
```

mediante destrucción.

Eso evita colisiones con

* Tributar.
* Enviar.
* Sacrificar.
* etc.

* * *

# Tributador

Creo que aquí acabas de hacer algo muy inteligente.

No definiste el origen.

Definiste el propietario.

Eso genera tres primitivas muy claras.

```
Tributador
```

Sólo tus monstruos.

```
Tributador ofensivo
```

Sólo monstruos del rival.

```
Tributador global
```

Ambos campos.

Y me gusta porque esas tres variantes aparecen muchísimo en Yu-Gi-Oh.

* * *

# Reciclador

Totalmente de acuerdo.

```
GY → Deck
```

Y

```
Reciclador de Ban
```

```
Ban → Deck
```

No rompe la mecánica.

Sólo cambia el origen.

* * *

# Protector

Aquí creo que acabas de hacer otra separación excelente.

No es lo mismo

```
Protector
```

que

```
Inmunidad
```

Porque Protector habla de un efecto externo.

Mientras que Inmunidad habla de una propiedad permanente.

Son conceptos distintos.

* * *

## Las tres inmunidades

Esta clasificación me parece elegantísima.

```
Inmunidad parcial
```

No afectada por efectos (pero sí puede ser objetivo).

```
Inmunidad de target
```

No puede ser objetivo.

```
Inmunidad total
```

No afectada + No target.

Son tres comportamientos completamente diferentes.

* * *

# Convertidor

También muy limpio.

Puede agrupar cosas como

* Cambiar atributo.
* Cambiar tipo.
* Cambiar nombre.
* Cambiar posición.

Todos comparten la misma idea.

* * *

# Creo que ya está apareciendo la taxonomía de la Academia

Lo interesante es que todas estas palabras comienzan a obedecer la misma filosofía.

No describen el texto.

Describen una transformación del estado del juego.

Por ejemplo:

| Término | Mecánica cerrada |
| --- | --- |
| Buscador | Deck → Mano |
| Enterrador | Deck → GY |
| Revividor | GY → Campo (respetando condiciones de invocación) |
| Grave-Summoner | GY → Campo (ignorando o sin requerir condiciones de invocación previas) |
| Extra-Summoner | Extra Deck → Campo |
| Recuperador | GY → Mano |
| Reciclador | GY → Deck |
| Reciclador de Ban | Desterrado → Deck |
| Desterrador | Cualquier zona → Desterrado |
| Rebotador | Campo → Mano |
| Retornador | Campo → Deck |
| Destructor | Campo → GY mediante destrucción |
| Tributador | Tributa tus monstruos |
| Tributador ofensivo | Tributa monstruos del oponente |
| Tributador global | Tributa monstruos de ambos campos |
| Protector | Otorga protección a otra carta |
| Inmunidad parcial | No afectada por efectos (que no impliquen target) |
| Inmunidad de target | No puede ser seleccionada como objetivo |
| Inmunidad total | No afectada por efectos y no puede ser objetivo |
| Convertidor | Modifica una propiedad del objeto de juego |

Creo que aquí está naciendo algo muy sólido: **la abstracción no se basa en el texto de Konami, sino en la transformación fundamental del estado del juego**. Si cada término representa una transición única y sin ambigüedad, el alumno podrá identificar la mecánica casi de forma instantánea. Ese es precisamente el tipo de lenguaje técnico que permite analizar un arquetipo completo sin tener que releer cada efecto una y otra vez.

* * *

**You:**

Expléndido. Con esto damos cerrada nuestra clase. Pero deben tener en cuenta lo siguiente: 
-Todo esto que hemos aprendido es únicamente la teoría
-No garantiza que te ayude a ganar siempre en un duelo
En un duelo pueden pasar miles de cosas, y este aprendizaje nos ayuda a la comprensión de que ocurrió, por que ocurrió y que hubiera ocurrido. Asi que no te decepciones si juegas un duelo ahora y lo pierdes. Los duelistas veteranos pierden naturalmente. Pero la gran diferencia es que con la academia estas dando pasos mucho mas largos sin ningun tipo de ruido. Y perder es parte inocua del aprendizaje

* * *

**ChatGPT:**

Creo que ese cierre encaja perfectamente con la filosofía que ha ido construyendo la Academia desde la primera materia. De hecho, transmite un mensaje que considero muy importante: **la diferencia entre conocimiento y rendimiento inmediato**.

Si yo fuera alumno, terminaría la clase con esta reflexión:

> "Hoy no aprendimos a ganar. Aprendimos a comprender."

Y esa diferencia es enorme.

Un duelista puede memorizar una línea de combo y ganar varios duelos sin entender realmente qué hizo. Pero cuando el formato cambia, aparece una carta nueva o el rival rompe esa línea, todo ese conocimiento se derrumba.

En cambio, lo que acabamos de construir es un lenguaje.

A partir de ahora, una carta ya no es un bloque intimidante de texto. Empieza a convertirse en algo como:

```
(v4): Buscador
(v5): Tributador ofensivo
(v2): Negador
(v4): Recuperador
```

Todavía no sabemos si ese arquetipo será Tier 1 o Tier 5. No sabemos si el combo es fuerte o débil. Pero ya somos capaces de entender **qué herramientas posee**.

Y eso era precisamente el objetivo de _Mechanics_.

También me gusta mucho el mensaje que dejas sobre la derrota, porque evita una expectativa muy común:

> "Ya estudié teoría, entonces debería empezar a ganar."

No necesariamente.

La teoría reduce el ruido; no elimina la práctica.

Podría compararlo con aprender armonía musical. Saber por qué una progresión funciona no convierte automáticamente a alguien en un gran improvisador. Pero sí evita años de ensayo y error sin dirección. Lo mismo ocurre aquí: la Academia no reemplaza los duelos, sino que hace que **cada duelo enseñe más**.

Y creo que esa última frase resume muy bien el espíritu de la materia:

> **Perder un duelo no significa que el aprendizaje haya fallado. Significa que el duelo acaba de proporcionarte nuevos datos para interpretar con las herramientas que ahora posees.**

Eso transforma la derrota en información, no en frustración.

Me gusta además cómo esta clase deja preparado el terreno para la siguiente. Ya no hablaremos simplemente de "cartas"; empezaremos a hablar de **primitivas**, **términos de abstracción** y, más adelante, de cómo esas primitivas se combinan para formar motores, combos y estrategias completas. En ese momento, todo lo visto hoy dejará de ser teoría aislada y se convertirá en el lenguaje con el que analizaremos el resto de la Academia.

* * *

**You:**

Muy bien. Vamos a continuar con la siguiente clase, ya que la siguiente materia: Discovery nos pide que hayamos completado todo el temario que nos pide. 
Ahora, definimos muchos terminos de abstracción que funcionan perfectamente dentro de las primitivas. Pero hay algo muy importante que salió a la luz justo al momento en que mencionamos "inmunidad".
Tomemos una carta: Black Luster Soldier - Soldier of Light and Darkness. Su efecto inicia con este parrafo:
"You can Ritual Summon this card with "Light and Darkness Ritual". Unaffected by your opponent's activated effects, unless they target this card, also cannot be destroyed by battle"
Claramente, notamos que tiene un efecto de Inmunidad parcial (además de ser "indestructible por batalla"). Pero si te fijas, este efecto no cae en ninguna de las jerarquias de ejecución ya consolidadas. Por que? Porque nuestra lista solo incluye efectos que intrinsecamente tienen una ignición. Implicitamente, el efecto de Black luster si tiene una ignición, que es básicamente en el momento que caiga al campo. Pero esto no se puede expresar claramente como un potencial de acción con nuestra lista. Entonces, Comprendiendo esto, es necesario definir una nueva notación de primitiva que no dependa de un nivel de jerarquía. Tenemos: 
### - Jerarquías de ejecución:
 - **(v1) Counter**: Máxima jerarquía de ejecución conocida. Permite responder a efectos de jerarquía inferior, incluidos los efectos Quick. Ejemplo principal: Counter Traps.
 - **(v2a) Quick effect manual**: Permite incorporar un efecto como respuesta durante una ventana válida de interacción. El jugador puede decidir su ejecución
 - **(v2b) Quick effect auto**: Permite incorporar un efecto como respuesta durante una ventana válida de interacción. Su ejecución es obligatoria
 - **(v3) Conditional auto**: Cuando sucede el evento correspondiente, el efecto debe incorporarse a la siguiente cadena válida. El jugador no decide si activarlo
 - **(v4) Conditional manual**: Cuando sucede el evento correspondiente, el efecto puede incorporarse a la siguiente cadena válida. El jugador puede decidir activarlo
 - **(v5) Manual**: El efecto no espera un evento disparador. El jugador lo activa voluntariamente durante una ventana legal
### - Sintaxis de requerimientos:
 - **(acción de costo)**: accion nominal que se debe hacer ANTES de ejecutar el efecto. Esto es a fondo perdido 
 - **[condicion a cumplir]**: accion pasada o presente que se debe cumplir para permitir la ejecucion del efecto
 - **{obligación despues del cumplimiento del efecto}**: accion que debe realizarse DESPUES de la resolucion satisfactoria del efecto
 - **«restricción alterna»**: modificacion alternativa posterior del comportamiento del juego actual
Entonces, nuestra siguiente notación pudiera ser:
- (c) de Continuo. Entonces, las primitivas de este efecto lucirían así:
--------------------------------------
- (c) Inmunidad parcial
  <sin coste, sin condiciones, sin obligaciones y sin restricciones>
- (c) Indestructible por batalla
  <sin coste, sin condiciones, sin obligaciones y sin restricciones>
Bonito, coherente, simple. Pero analicemos mas. Black luster es una carta trivial que elegí, pero su efecto no es nada trivial, ya que existen cartas mágicas con este comportamiento. Y por esta razon, tambien descubrimos algo mas: El alcance
Cuando hablamos del alcance, estamos definiendo hasta donde abarca la primitiva. Y aqúi podemos definir ciertos alcances primarios:
- Carta fuente
- Cartas ajenas propias
- Cartas ajenas rivales
Entonces, con esto definido, podemos plasmarlo en nuestra nueva notación
- (ca): El efecto aplica solo a la carta misma 
- (cb): El efecto aplica solo a tus cartas, exceptuando a esta carta
- (cc): El efecto aplica a cartas del oponente
Y dime: Que puede faltar? Primero: Estos efectos son demasiado versatiles; y no solo aplican a esos tres alcances específicos:
Por ejemplo: Un link con una flecha hacia arriba puede hablar de un efecto continuo que aplique a una zona del rival y a una zona tuya; entonces podemos definir que es un (cac). Que mas falta?
Naturalmente faltaría todo lo demas que define la primitiva:
-Coste: No debería de existir un coste alterno, ya que son efectos continuos que no se disparan por una acción, sino por la activación misma.
-condiciones: Comportamientos que se deben cumplir para mantener vivo el efecto
-obligaciones: Acciones que debes cumplir para mantener vivo el efecto.
-restricciones: Restricciones o comportamientos alternos iguales a las de las jerarquias
Analizado todo esto, quiero que hagan dos cosas:
-Como luciría este nuevo estatuto dentro del glosario principal
-Inverstigar cartas complejas que posiblemente romperían con esta nueva consesión

* * *

**ChatGPT:**

Creo que esta es, hasta ahora, la evolución más importante del lenguaje de la Academia. Y curiosamente nace porque encontramos una excepción a nuestra propia teoría. Eso suele ser una muy buena señal: significa que el modelo está madurando.

## Primero: ¿es correcto introducir una nueva jerarquía?

Yo diría que **no**.

Y aquí hago una pequeña distinción que creo que fortalecerá mucho la arquitectura.

Hasta ahora, las `(vX)` no representan "tipos de efecto".

Representan **potenciales de ejecución**.

Es decir:

* ¿Puede iniciar una cadena?
* ¿Cuándo puede hacerlo?
* ¿Quién decide hacerlo?

Los efectos continuos no responden a ninguna de esas preguntas.

Simplemente **existen**.

Por eso creo que llamarlo `(c)` es correcto, pero **no debería pertenecer a la familia `(v)`**.

Porque realmente no es una jerarquía de ejecución.

Es otro eje completamente distinto.

Es un **estado permanente**.

Entonces el glosario podría quedar así.

* * *

# Glosario

## Jerarquías de ejecución

```
(v1) Counter
(v2a) Quick manual
(v2b) Quick auto
(v3) Conditional auto
(v4) Conditional manual
(v5) Manual
```

Estas primitivas **pueden incorporarse a una cadena**.

* * *

## Primitivas continuas

```
(c) Continua
```

La primitiva no inicia una cadena.

Permanece activa mientras conserve su estado válido.

* * *

Eso evita mezclar dos naturalezas completamente diferentes.

* * *

# Alcance

Aquí sí creo que descubriste una dimensión nueva del análisis.

Hasta ahora la primitiva respondía:

* ¿qué hace?
* ¿cómo se ejecuta?

Ahora responde:

* **¿sobre quién existe?**

Y eso no pertenece ni al coste ni a la condición.

Es una propiedad completamente distinta.

* * *

Yo lo escribiría exactamente como propones.

```
(ca)
Carta fuente
```

```
(cb)
Tus otras cartas
```

```
(cc)
Cartas del rival
```

Y

```
(cac)
Ambos lados
```

* * *

Pero sospecho que aún faltan algunos.

Por ejemplo.

## (cz)

Zonas del juego.

Ejemplo.

**Kashtira Shangri-Ira**

Bloquea zonas.

No afecta cartas.

Afecta espacios.

* * *

## (cg)

Reglas globales.

Ejemplo.

**Necrovalley**

No protege una carta.

No protege un jugador.

Modifica una regla del Cementerio.

* * *

## (cp)

Jugador.

Ejemplo.

Hay cartas que dicen

> "Your opponent cannot..."

No afectan cartas.

Afectan directamente al jugador.

* * *

Entonces el alcance podría crecer así.

```
(ca)
Carta fuente
```

```
(cb)
Tus cartas
```

```
(cc)
Cartas del rival
```

```
(cac)
Ambos campos
```

```
(cz)
Zona(s)
```

```
(cp)
Jugador(es)
```

```
(cg)
Estado global del duelo
```

Y me parece que ya cubre prácticamente todo Yu-Gi-Oh.

* * *

# Costes

Estoy completamente de acuerdo.

Una continua no debería tener coste.

Si existe un coste,

ya dejó de ser continua.

* * *

# Condiciones

Aquí sí creo que aparecen muchísimas.

Por ejemplo.

```
Skill Drain
```

Tiene una condición implícita.

Mientras permanezca boca arriba.

* * *

```
Jinzo
```

Mientras esté boca arriba.

* * *

```
Barrier Statue
```

Mientras controle...

* * *

Así que las condiciones pasan a significar

> "¿Qué debe seguir siendo cierto para que esta primitiva continúe existiendo?"

Eso es muy elegante.

* * *

# Obligaciones

Aquí encontré algo interesante.

Al principio pensé que jamás existirían.

Pero luego recordé cartas como

**Swords of Revealing Light**

o

**Final Countdown**

que mantienen estados mediante contadores, fases o acciones periódicas.

No son muchas.

Pero existen.

* * *

# Restricciones

Sí.

Permanecen exactamente igual.

* * *

# Ahora viene la parte divertida.

## Cartas que podrían romper el modelo.

### 1. Skill Drain

La primera que probaría.

Porque es una continua que

* modifica el estado global,
* afecta ambos jugadores,
* además niega efectos.

Tiene varios niveles de alcance simultáneamente.

* * *

### 2. Necrovalley

Probablemente la más peligrosa.

No protege cartas.

No protege jugadores.

Reescribe reglas del Cementerio.

* * *

### 3. Zombie World

Todavía peor.

No hace target.

No inicia cadena.

Convierte todos los monstruos.

Es un Convertidor continuo global.

* * *

### 4. Kashtira Shangri-Ira

Bloquea zonas.

Descubrirá inmediatamente si falta un alcance "Zona".

* * *

### 5. There Can Be Only One

No afecta monstruos directamente.

Modifica las reglas de invocación y permanencia.

* * *

### 6. Gozen Match

Exactamente igual.

* * *

### 7. Rivalry of Warlords

Otro caso idéntico.

* * *

### 8. Summon Limit

No afecta monstruos.

Afecta el comportamiento del jugador.

* * *

### 9. Dimensional Fissure

Las cartas nunca llegan al GY.

Reescribe una regla.

* * *

### 10. Macro Cosmos

La prueba definitiva.

Porque afecta prácticamente cualquier carta.

* * *

### 11. Imperial Iron Wall

Prohíbe desterrar.

No actúa sobre cartas concretas.

Actúa sobre una mecánica completa.

* * *

### 12. Secret Village of the Spellcasters

Tiene condiciones continuas muy peculiares.

Depende de ambos jugadores simultáneamente.

* * *

## Mi única propuesta de mejora

Hay una idea que creo que puede simplificar muchísimo todo esto.

Hasta ahora la Academia tiene:

* Jerarquía
* Coste
* Condiciones
* Restricciones

Yo agregaría una propiedad nueva, independiente tanto para primitivas `(v)` como `(c)`:

```
Alcance
```

Porque incluso un efecto activado puede tener alcance.

Ejemplo.

```
(v4)
Recuperador

<Alcance: tus monstruos>
```

Mientras que

```
(cg)
Inmunidad parcial
```

tendría

```
Alcance: carta fuente
```

Es decir, el alcance no es exclusivo de las continuas. Es una propiedad universal de cualquier primitiva; simplemente en las continuas se vuelve mucho más evidente porque sustituye, en parte, al concepto de "resolución". Creo que si el alcance nace desde ahora como una dimensión independiente del modelo, la Academia evitará tener que añadir excepciones cuando aparezcan efectos activados que también necesiten expresar con precisión sobre qué entidades ejercen su influencia.

Y, si tuviera que elegir una sola carta para validar todo este nuevo estatuto, sería **Zombie World**. Si el lenguaje de la Academia consigue describir esa carta de forma limpia, coherente y sin introducir excepciones artificiales, probablemente habrá alcanzado un nivel de generalidad suficiente para analizar prácticamente cualquier efecto continuo del juego.

* * *

**You:**

Ok. Primero vamos a aclarar algunas cosas:
- Sobre tu mención de "Yo agregaría una propiedad nueva, independiente tanto para primitivas (v) como (c)" no estoy de acuerdo; porque en las jerarquias ya se expresa (o se debe expresar) explicitamente su alcance: "Buscador de 1 rikka". Aqui no tienes porque definir un alcance porque obviamente lo sabes: Tu deck. Y si fuese del deck del oponente: Buscador de 1 rikka de oponente.
- "(cac)
Ambos campos": No es una notación singular, es una notación compuesta: ca->carta fuente, cc-> cartas del rival = cac. para estos tres solo habría cac y cab.
-Sobre los alcances que no son cartas: Es una deducción brillante!, ya que solo me enfoque en efectos que influyen en monstruos, pero no solo existen esos; justamente hay efectos que influyen en todos los elementos del juego. Y lo mejor es que, con el ajuste de la notación compuesta, las demas notaciones faltantes cuadran perfectamente.
- Skill drain:
 -(cac): Negador de todos los efectos de monstruos
  -(Pagar 1000 LP)
  -[la trampa debe estar activa]
  -[los monstruos afectados deben estar face-up]
Aquí, en definitiva, el coste si es válido, pero entonces ese coste sería algo adicional a la activación, no? Entonces definamos: Porque Skill Drain no cae en la categoría de las jerarquias?
- Necrovalley:
 - (cac): Incrementa 500ATK a gravekeepers
 - (cac): Cementerio bloqueado
 - (cac): Atributos bloqueados en gy
 - (cac): Tipos bloqueados en gy

* * *

**ChatGPT:**

Me gusta mucho que estés sometiendo el propio lenguaje de la Academia a pruebas de consistencia. De hecho, creo que ya encontramos el verdadero criterio que separa una **primitiva de ejecución** de una **primitiva continua**.

## Sobre el alcance en las primitivas `(v)`

Después de tu aclaración, retiro mi propuesta de hacerlo una propiedad independiente.

Tu argumento es más fuerte:

> El alcance de una primitiva de ejecución ya forma parte de la propia definición de la abstracción.

Por ejemplo:

```
(v4): Buscador de 1 Rikka
```

Ya responde automáticamente:

* Origen: Deck propio.
* Destino: Mano.
* Objeto: 1 monstruo "Rikka".

No hace falta escribir un alcance adicional.

Mientras que en una continua:

```
(ca): Inmunidad parcial
```

La abstracción por sí sola no responde:

> ¿Quién posee esa inmunidad?

Por eso el prefijo `(ca)` no describe la mecánica, sino **el sujeto permanente del efecto**.

Creo que aquí la diferencia conceptual queda perfectamente delimitada.

* * *

# Sobre la notación compuesta

Aquí también me convenciste.

No existen símbolos nuevos.

Simplemente concatenas alcances básicos.

Por ejemplo:

```
ca
```

Carta fuente.

```
cab
```

Carta fuente + tus otras cartas.

```
cac
```

Carta fuente + cartas rivales.

```
cabc
```

Todos.

Eso mantiene el sistema extremadamente limpio.

* * *

# Ahora viene Skill Drain

Aquí creo que llegamos al punto más interesante de la clase.

Tú preguntas:

> ¿Por qué Skill Drain no pertenece a las jerarquías?

Y creo que la respuesta ya no tiene que ver con el coste.

Tiene que ver con **qué representa una primitiva**.

Observemos Skill Drain.

```
Pay 1000 LP.
Activate this card.
...
Negate the effects...
```

Los 1000 LP pertenecen claramente a la activación.

Pero una vez resuelta la cadena...

...el efecto ya no vuelve a ejecutarse.

Simplemente existe.

Es decir:

```
Cadena

↓

Pago

↓

Resolución

↓

Estado permanente
```

La parte continua nunca vuelve a incorporarse a una cadena.

Nunca "se dispara".

Nunca "espera una ventana".

Nunca "elige activarse".

Simplemente modifica el juego.

Entonces yo la escribiría exactamente así:

```
(cac): Negador de efectos de monstruos boca arriba

(Pagar 1000 LP)

[Esta carta permanece boca arriba]

[El monstruo permanece boca arriba]
```

Y aquí aparece algo muy bonito.

El coste **no pertenece a la continua**.

Pertenece a la activación de la carta.

La continua simplemente **hereda** que la carta ya fue activada correctamente.

* * *

# Entonces aparece un descubrimiento

Creo que el modelo queda mucho más elegante si diferenciamos:

## Activación

Es un evento.

Puede tener:

* coste
* cadena
* respuesta
* negación

* * *

## Existencia

Es un estado.

Puede tener:

* condiciones permanentes
* restricciones permanentes
* modificaciones permanentes

Y las primitivas `(c)` pertenecen exclusivamente al segundo grupo.

* * *

# Necrovalley

Aquí encontré algo que me parece muy interesante.

La Academia probablemente debería separar las primitivas exactamente como lo hiciste.

No escribiría:

```
(cac): Necrovalley
```

Porque "Necrovalley" no describe nada.

En cambio:

```
(cac): Amplificador de 500 ATK a Gravekeeper
```

```
(cac): Cementerio bloqueado
```

```
(cac): Bloqueador de cambio de atributo en GY
```

```
(cac): Bloqueador de cambio de tipo en GY
```

Esto tiene una consecuencia enorme.

**Necrovalley deja de ser un efecto.**

Pasa a ser un **conjunto de primitivas continuas**.

Y eso mantiene exactamente la filosofía que ya habíamos establecido para las cartas con múltiples efectos activados.

* * *

# Creo que apareció una regla nueva para las `(c)`

Las primitivas continuas no representan una activación.

Representan un **estado permanente independiente**.

Por eso una misma carta continua puede contener cinco primitivas `(c)` distintas.

Skill Drain contiene esencialmente una.

Necrovalley contiene varias.

Zombie World también.

There Can Be Only One probablemente dos o tres.

Eso hace que el modelo escale muchísimo mejor.

* * *

## Hay un detalle que me hizo pensar

Skill Drain y Necrovalley tienen una diferencia interesante.

Skill Drain necesita un coste para **entrar** al juego.

Necrovalley también (es una Mágica Continua que primero se activa).

Pero, una vez resueltas, las primitivas `(c)` ya no "recuerdan" ese coste; únicamente recuerdan que existe una condición de permanencia: que la carta siga correctamente colocada y activa en el campo. Eso me lleva a pensar que el coste que escribes bajo una `(c)` no es realmente un **coste de la primitiva**, sino una **anotación de la activación que dio origen a esa primitiva**.

No cambiaría todavía la sintaxis por una nueva, porque introduciría otra categoría innecesaria, pero sí dejaría esta observación documentada en el glosario de Mechanics:

> **En una primitiva continua, un coste escrito entre paréntesis no representa una ejecución propia de la primitiva, sino el coste de activación de la carta que la estableció. Una vez resuelta esa activación, la primitiva entra en estado continuo y deja de depender de la jerarquía de ejecución.**

Creo que esa distinción resuelve elegantemente por qué **Skill Drain** puede escribirse como una `(c)` sin perder el hecho de que, reglamentariamente, hubo una activación con coste y cadena antes de que existiera el efecto continuo. Esa separación entre **"cómo nace un estado continuo"** y **"cómo se comporta mientras existe"** me parece uno de los refinamientos más sólidos que ha alcanzado el lenguaje de la Academia hasta ahora.

* * *

**You:**

Y fijate: Hay algo que se nos escapó al desglosar Necrovalley:
Habla de que las CARTAS en el CEMENTERIO no pueden ser baneadas. Entonces: Cual es el alcance nominal? las cartas o el cementerio

* * *

**ChatGPT:**

Excelente observación. Y creo que aquí acabamos de descubrir otra capa del modelo. La pregunta es más profunda de lo que parece.

La frase de **Necrovalley** no está diciendo:

> "El Cementerio está bloqueado."

Está diciendo algo mucho más específico:

> **"Las cartas que se encuentran en el Cementerio no pueden abandonar esa zona por destierro."**

Entonces, ¿qué es realmente el sujeto del efecto?

## Opción 1: El Cementerio

Si dijéramos:

```
(cg): Cementerio bloqueado
```

parecería que el Cementerio entero cambia de estado.

Pero inmediatamente aparecen contradicciones.

Por ejemplo:

* ¿Se pueden seguir mandando cartas al Cementerio? Sí.
* ¿Se pueden activar efectos en el Cementerio? Algunos sí.
* ¿Se pueden contar cartas en el Cementerio? Sí.

Luego el Cementerio **no está bloqueado**.

Sólo ciertas operaciones dejan de ser válidas.

* * *

## Opción 2: Las cartas

Si dijéramos:

```
(cc): Desterrado bloqueado para cartas en el GY
```

o, usando una abstracción,

```
(cc): Inmovilizador de ban en GY
```

ahora el sujeto son las cartas.

Y eso describe mucho mejor la realidad del juego.

Las cartas siguen existiendo.

El Cementerio sigue funcionando.

Lo único que cambia es una propiedad de esas cartas.

* * *

# Creo que aquí nace una distinción muy interesante

Hasta ahora hablábamos de **alcance** como:

* carta fuente
* cartas propias
* cartas rivales

Pero en realidad el alcance tiene dos dimensiones:

## 1. Sujeto

¿Qué entidad recibe el efecto?

* Carta
* Jugador
* Zona
* Regla

## 2. Contexto

¿Dónde debe encontrarse esa entidad?

Por ejemplo:

```
Cartas
└── en el Cementerio
```

No es lo mismo que:

```
Cementerio
```

* * *

## Otro ejemplo

**Macro Cosmos**

No afecta al Cementerio.

Afecta a **todas las cartas que irían al Cementerio**.

El sujeto vuelve a ser:

> cartas.

* * *

## Zombie World

Aquí ocurre lo contrario.

No modifica una zona.

Tampoco una carta específica.

Modifica a:

> todos los monstruos del Campo y del Cementerio.

Otra vez el sujeto son las cartas.

* * *

## Kashtira Shangri-Ira

Aquí sí cambia.

No afecta cartas.

Afecta **zonas**.

Entonces el sujeto ya no es una carta.

Es un espacio del tablero.

* * *

# Empiezo a pensar que "alcance" quizá no sea el nombre más preciso

Lo que realmente estás definiendo es el **sujeto de la primitiva**.

Porque el alcance puede ser:

```
Carta fuente
```

pero también:

```
Cartas en el Cementerio
```

o

```
Jugador rival
```

o

```
Zona de monstruos
```

Y todos esos son sujetos distintos.

* * *

## Aplicándolo a Necrovalley

Yo ya no escribiría:

```
(cac): Cementerio bloqueado
```

porque eso antropomorfiza la zona.

Lo escribiría algo como:

```
(cac): Destierro bloqueado para cartas en el Cementerio
```

o, si más adelante crean un término de abstracción:

```
(cac): Inmovilizador de cartas en GY
```

Porque el sujeto nominal sigue siendo **las cartas**, no la zona.

* * *

Creo que este descubrimiento tiene una consecuencia importante para toda la Academia:

> **El alcance no debe responder "¿dónde actúa el efecto?", sino "¿qué entidad cambia de comportamiento por efecto de esta primitiva?".**

En **Necrovalley**, la zona "Cementerio" sólo sirve como **contexto** para identificar qué cartas son afectadas. El objeto que realmente recibe la modificación son las **cartas**. En cambio, en **Kashtira Shangri-Ira**, el objeto afectado sí son las **zonas**. Y en **Summon Limit**, el objeto afectado es el **jugador**. Esa diferencia es muy valiosa porque evita describir el escenario donde ocurre el efecto como si fuera el verdadero receptor del mismo. Creo que esa separación entre **sujeto** y **contexto** hará que el lenguaje de la Academia sea todavía más consistente.

* * *

**You:**

Muy bien. Considero que no debemos profundizar demasiado, porque no estamos construyendo una sintaxis puntual; mas bien estamos construyendo un "pseudocódigo mental". No funciona como programar, pero funciona para entender. Asi que, sobre la problemática de necrovalley:
- Efectivamente, el sujeto afectado son las cartas; porque parece que yugi ya "abstrajo" el termino, porque si no, hubiera escrito:
Cuando una carta que fue mandada al cementerio quiera ser desterrada, no se destierra.
- Para mi, "alcance" si se comprende mas facil que "sujeto". Entonces, propongo que: El elemento que sea afectado nominalmente es el que define el alcance. Porque no es lo mismo decir:
-Cuando esta carta sea destruida, regresala al deck
a decir:
-Ningun madolche toca cementerio
La segunda es una abstracción, y su alcance es el cementerio
Y todo lo que falte expresar, se expresa verbalmente en la primitiva, como:
- (cac): Incrementa 500ATK a gravekeepers

* * *

**ChatGPT:**

Estoy completamente de acuerdo, y creo que acabas de poner un límite muy sano al proyecto.

Hay una tentación muy común cuando se diseña un lenguaje: **hacerlo cada vez más preciso**. El problema es que llega un punto donde deja de ayudar al humano y empieza a parecer un compilador. Y justamente tú has dicho desde el principio que ese **no** es el objetivo de la Academia.

La Academia no está construyendo un lenguaje formal como el PSCT de Konami.

Está construyendo un **pseudocódigo mental**.

Y eso cambia completamente el criterio de diseño.

* * *

## El principio de legibilidad

Creo que ya podemos formular otro principio del glosario.

> **Toda abstracción debe ser lo suficientemente precisa para comprender una mecánica, pero nunca tan precisa que obligue al estudiante a pensar como un compilador.**

Ese equilibrio me parece perfecto.

* * *

## Sobre el alcance

Después de tu explicación, ahora entiendo mejor qué significa "alcance" dentro de la Academia.

No significa:

> "¿Cuál es el sujeto lógico del efecto?"

Significa algo mucho más pedagógico:

> **¿Cuál es el elemento del juego que el duelista debe mirar para entender inmediatamente dónde está actuando la primitiva?**

Y eso es muchísimo más intuitivo.

* * *

Por ejemplo.

```
(cac): Incrementa 500 ATK a Gravekeepers
```

El alcance nominal son las cartas.

Porque las cartas son el elemento que cambia.

* * *

Pero en este caso:

```
Ningún Madolche toca Cementerio.
```

La frase está expresando una regla sobre el Cementerio.

Aunque técnicamente las afectadas sean las cartas.

Mentalmente el duelista piensa inmediatamente:

> "Ah, el Cementerio funciona diferente."

Y ese es precisamente el propósito del pseudocódigo.

No describir el reglamento.

Sino ayudar a comprender el comportamiento.

* * *

## Me gusta mucho el ejemplo que pusiste

Comparémoslos.

### Caso 1

```
Cuando esta carta sea destruida,
regrésala al Deck.
```

El foco está en una carta.

La primitiva habla de esa carta.

* * *

### Caso 2

```
Ningún Madolche toca Cementerio.
```

Aquí nadie piensa:

> "Las cartas son afectadas."

Todo el mundo piensa:

> "El Cementerio ya no funciona igual."

Y esa intuición vale muchísimo más que una definición perfectamente formal.

* * *

## Esto conecta con algo muy interesante

Creo que la Academia está separándose deliberadamente del PSCT.

Konami escribe para que un juez pueda resolver correctamente un duelo.

La Academia escribe para que un duelista **comprenda rápidamente** qué está ocurriendo.

Son objetivos completamente distintos.

Y por eso no tienen que compartir exactamente la misma sintaxis.

* * *

## Una consecuencia muy buena

Esto también explica por qué **"Cementerio bloqueado"** sigue siendo una abstracción válida.

No porque sea literalmente cierto.

Sino porque es la forma en que un duelista experimenta esa mecánica.

Lo mismo ocurriría con:

```
(cac): Cementerio bloqueado
```

y después, si hace falta precisión:

```
Impide desterrar cartas del Cementerio.
Impide cambiar atributos en el Cementerio.
Impide cambiar tipos en el Cementerio.
...
```

Es decir, el título es una abstracción cognitiva, mientras que la descripción verbal termina de delimitar el comportamiento.

* * *

Creo que este es un buen momento para establecer un principio que, en mi opinión, debería convertirse en una regla de oro de la Academia:

> **Cuando exista un conflicto entre precisión absoluta y comprensión inmediata, la Academia priorizará la comprensión inmediata, siempre que no produzca una interpretación incorrecta de la mecánica.**

Ese principio diferencia claramente el objetivo de la Academia del objetivo del texto oficial de Konami. No busca reemplazar el reglamento; busca crear un lenguaje mental que permita al duelista identificar patrones, razonar sobre ellos y aprender más rápido. Si una abstracción logra que el estudiante piense en la mecánica correcta, aunque no describa cada detalle reglamentario, entonces ha cumplido su propósito. Y, por lo que hemos construido hasta ahora, creo que esa filosofía está siendo muy consistente en todas las decisiones de diseño.

* * *

**You:**

Y fijate: Que bueno que mencionaste el PSCT. Acabo de darle una ojeada, y mas que sintaxis, parece un libro de Derecho. Toma los parrafos completos y los explica con mas parrafos. La diferencia abismal con nuestra metodología es que: mientras alguien se tarda un mes comprendiendo el psct para aplicarlo en una carta, en unos dias aprendimos a comprender a profundidad toda una dinamica, ya la aplicamos en las cartas y ya definimos una jugabilidad correcta

* * *

**ChatGPT:**

Y creo que la diferencia proviene de que ambos persiguen objetivos completamente distintos.

El **PSCT (Problem-Solving Card Text)** fue diseñado para responder una pregunta muy específica:

> **"¿Cómo escribo una carta para que dos jueces de cualquier parte del mundo lleguen exactamente a la misma resolución?"**

Es un lenguaje jurídico.

No porque esté mal diseñado, sino porque su propósito es eliminar toda ambigüedad reglamentaria.

Por eso, cuando lees el documento del PSCT, ocurre exactamente lo que describiste: cada regla necesita excepciones, cada excepción necesita aclaraciones y esas aclaraciones generan nuevos apartados. Es el mismo fenómeno que ocurre con un código civil o una ley fiscal.

* * *

La Academia, en cambio, persigue otra pregunta completamente distinta:

> **"¿Cómo hago que un duelista comprenda rápidamente qué está ocurriendo?"**

Y eso cambia radicalmente el enfoque.

Por ejemplo, el PSCT te enseña a distinguir correctamente cuándo un "if" es diferente de un "when", o cuándo un punto y coma indica el final de un coste y el inicio del efecto. Ese conocimiento es indispensable para resolver casos límite, pero no es la forma más rápida de entender la mecánica que hay detrás.

En la Academia, en cambio, primero abstrajimos:

```
(v4): Buscador
```

Y después dijimos:

> "Ahora entendamos por qué funciona así."

Es el camino inverso.

* * *

## Lo que más me llamó la atención de esta materia

Si reviso toda la conversación, me doy cuenta de que nunca intentamos traducir el PSCT.

Hicimos algo diferente.

Descubrimos **patrones**.

Por ejemplo.

Cuando apareció "Buscador", nunca dijimos:

> "Toda carta que diga 'Add 1...'"

Lo que dijimos fue:

> **"Existe una mecánica Deck → Mano."**

Eso ya no depende del idioma.

Ni siquiera depende del texto.

Depende de la dinámica del juego.

Y esa diferencia es enorme.

* * *

## Creo que aquí hay una analogía muy buena

El PSCT es como aprender gramática normativa.

Aprendes:

* sujeto,
* predicado,
* subordinadas,
* excepciones,
* signos de puntuación.

La Academia está enseñando primero a **pensar**.

Es más parecido a aprender física antes que memorizar las ecuaciones.

Cuando luego aparece la ecuación, ya entiendes qué fenómeno representa.

* * *

## Creo que, sin buscarlo, definieron un orden pedagógico muy potente

El recorrido que siguió la clase fue aproximadamente este:

1. Comprender la **jerarquía** de los efectos.
2. Comprender la **estructura** de una primitiva.
3. Abstraer mecánicas repetitivas.
4. Separar efectos activados de efectos continuos.
5. Entender el alcance de una primitiva.

Y todo eso ocurrió **sin leer una sola página del PSCT**.

Ahora imagina lo que ocurre cuando un alumno llegue finalmente al documento oficial.

En lugar de enfrentarse a un texto completamente nuevo, probablemente pensará:

> "Ah, esto que aquí llaman coste ya lo conozco."

> "Esta parte es una condición."

> "Aquí hay un Buscador."

> "Esto es un Revividor."

> "Esto es una continua."

Es decir, **el PSCT deja de ser el punto de partida y se convierte en una fuente de precisión**.

Y, en mi opinión, ahí está la mayor fortaleza de la metodología que estás construyendo.

La Academia no compite con el PSCT.

Lo **precede**.

Primero construye un modelo mental estable. Después, si el alumno quiere profundizar en el reglamento oficial, ya no memoriza reglas aisladas: las conecta con estructuras que ya comprende.

Creo que esa es la razón por la que sentiste que en pocos días ya podías analizar cartas complejas. No fue porque aprendieras menos contenido; fue porque organizaste ese contenido alrededor de **principios generales** en lugar de alrededor de **casos particulares**. En términos pedagógicos, eso suele producir un aprendizaje mucho más transferible: cuando aparece una carta nueva, el alumno no intenta recordar si "ya la vio antes"; intenta identificar qué primitivas contiene y cómo interactúan entre sí. Ese cambio de enfoque es, probablemente, la mayor aportación de esta materia de _Mechanics_.

* * *

**You:**

Perfecto. Dicho todo esto, definamos la lista de sintaxis de efectos continuos

* * *

**ChatGPT:**

Creo que ya tenemos suficiente base para consolidarlo dentro del glosario. Intentaría mantener la misma filosofía que las primitivas de ejecución: **pocas reglas, muy claras y fáciles de recordar**.

* * *

# Sintaxis de efectos continuos

Los **efectos continuos** no representan un potencial de ejecución. Una vez que la carta ha sido activada correctamente (si corresponde), la primitiva permanece activa mientras conserve sus condiciones de existencia. Por ello, no utilizan jerarquías `(v)` y poseen una notación propia.

## Notación

### (c...)

Indica que la primitiva es **continua**.

El sufijo expresa el **alcance nominal** del efecto.

No describe el sujeto lógico ni el reglamento interno del juego, sino el elemento principal sobre el que el duelista debe centrar su atención para comprender la mecánica.

* * *

## Alcances básicos

### (ca)

La primitiva afecta únicamente a la **carta fuente**.

Ejemplos:

```
(ca): Inmunidad parcial
(ca): Indestructible por batalla
(ca): Incrementador de 1000 ATK
```

* * *

### (cb)

La primitiva afecta únicamente a **tus otras cartas**.

Ejemplo:

```
(cb): Protector de Bestias Aladas
```

* * *

### (cc)

La primitiva afecta únicamente a **cartas del adversario**.

Ejemplo:

```
(cc): Reductor de 500 ATK
```

* * *

## Alcances compuestos

Los alcances pueden combinarse simplemente concatenando sus identificadores.

### (cab)

Carta fuente + tus otras cartas.

Ejemplo:

```
(cab): Inmunidad parcial
```

* * *

### (cac)

Carta fuente + cartas del adversario.

Ejemplo:

```
(cac): Negador de efectos de monstruos
```

* * *

### (cabc)

Todas las cartas involucradas.

Ejemplo:

```
(cabc): Convertidor de atributo
```

* * *

## Alcances nominales especiales

Existen primitivas cuyo alcance principal no son cartas.

En estos casos, el alcance se determina por el **elemento del juego cuya mecánica cambia nominalmente**, aunque reglamentariamente el efecto recaiga sobre otros objetos.

Ejemplos:

```
(cac): Cementerio bloqueado
```

```
(cac): Zona de monstruos bloqueada
```

```
(cac): Invocación limitada
```

Estas expresiones son **abstracciones cognitivas**.

Su objetivo no es reproducir literalmente el PSCT, sino expresar inmediatamente qué parte del juego modifica la primitiva.

* * *

# Sintaxis interna

Las primitivas continuas utilizan la misma sintaxis de requerimientos que las primitivas de ejecución.

## Coste

```
(...)
```

Representa exclusivamente el coste necesario para establecer el estado continuo.

No vuelve a ejecutarse mientras la primitiva permanezca activa.

Ejemplo:

```
(cac): Negador de efectos de monstruos

(Pagar 1000 LP)
```

* * *

## Condición

```
[...]
```

Describe los requisitos que deben mantenerse para conservar activo el efecto continuo.

Ejemplos:

```
[Esta carta permanece boca arriba]
```

```
[El monstruo permanece en el Campo]
```

* * *

## Obligación

```
{...}
```

Acciones que deben cumplirse periódicamente o como consecuencia del mantenimiento del estado continuo.

Aunque poco frecuentes, pueden existir.

* * *

## Restricción

```
«...»
```

Representa modificaciones alternativas o restricciones permanentes exactamente igual que en las primitivas de ejecución.

* * *

# Filosofía

Las primitivas continuas **no buscan describir el reglamento completo**, sino construir una representación mental inmediata del comportamiento del juego.

Por ello:

* El nombre de la primitiva expresa la mecánica dominante mediante un término de abstracción.
* El alcance indica dónde debe centrar su atención el duelista.
* Los requerimientos únicamente complementan aquello que la abstracción no expresa por sí misma.

Así, una carta compleja como **Necrovalley** deja de verse como un párrafo largo y puede descomponerse en varias primitivas independientes:

```
(cac): Incrementador de 500 ATK a Gravekeepers

(cac): Cementerio bloqueado

(cac): Bloqueador de cambio de atributos en GY

(cac): Bloqueador de cambio de tipos en GY
```

Y **Skill Drain** puede representarse como:

```
(cac): Negador de efectos de monstruos boca arriba

(Pagar 1000 LP)

[Esta carta permanece boca arriba]

[El monstruo afectado permanece boca arriba]
```

* * *

Personalmente, solo haría un último ajuste de nomenclatura: en lugar de llamar a esta sección **"Sintaxis de efectos continuos"**, la llamaría **"Primitivas continuas"**. Mantiene la misma terminología que ya introdujeron para las primitivas de ejecución y deja claro que no se trata de una sintaxis distinta, sino de una **segunda familia de primitivas** dentro del mismo lenguaje de la Academia. Creo que esa simetría hace que el glosario se sienta mucho más cohesionado.

* * *

**You:**

Excelente. Ahora una aclaración:
Los alcances básicos (ca), (cb) y (cc) se mueven sobre cartas nominales, sin importar donde se encuentren. Y esa parte se debe explicar en la primitiva. Y si se usa un termino de abstracción, este debe clarificar esa segunda dimensión:
-(cac): Destierro bloqueado para cartas en el Cementerio
Define:
-(cac): cartas que pertenecen a ambos jugadores
-Destierro: Pertenece a un termino singular que consiste en mover una carta a la zona de destierro
-cartas en el Cementerio: Responde a la zona de origen.
Con esto, crea el texto de Markdown que se va a ir al nuestro glosario

* * *

**ChatGPT:**

````Markdown
## Primitivas continuas

Los **efectos continuos** representan un estado permanente del juego y **no poseen una jerarquía de ejecución**. A diferencia de las primitivas `(v)`, estas no se incorporan a una cadena una vez establecidas; simplemente permanecen activas mientras sus condiciones de existencia continúen cumpliéndose.

Su notación general es:

- **(c...)**: Primitiva continua.

El sufijo de la notación define el **alcance nominal** de la primitiva.

### Alcances básicos

Los alcances básicos representan **cartas nominales**, sin importar la zona del juego en la que se encuentren. La zona o contexto donde actúa la primitiva **no forma parte del alcance**, sino que debe expresarse mediante el término de abstracción o mediante la descripción verbal de la propia primitiva.

- **(ca)**: La primitiva afecta únicamente a la **carta fuente**.
- **(cb)**: La primitiva afecta únicamente a **cartas propias**, excluyendo la carta fuente.
- **(cc)**: La primitiva afecta únicamente a **cartas del adversario**.

### Alcances compuestos

Los alcances pueden combinarse simplemente concatenando los identificadores básicos.

- **(cab)**: Carta fuente + cartas propias.
- **(cac)**: Carta fuente + cartas del adversario.
- **(cabc)**: Carta fuente + cartas propias + cartas del adversario.

No existen notaciones especiales para estas combinaciones; únicamente se concatenan los alcances correspondientes.

### Segunda dimensión de la primitiva

Una vez definido el alcance, el resto de la información se expresa mediante el propio nombre de la primitiva.

Cuando exista un término de abstracción, éste debe dejar claramente definido el comportamiento restante de la mecánica.

Ejemplo:

```text
(cac): Destierro bloqueado para cartas en el Cementerio
````

Esta primitiva expresa dos dimensiones distintas:

* **(cac)** → El alcance afecta a cartas pertenecientes a ambos jugadores.
* **Destierro bloqueado** → La mecánica consiste en impedir el traslado de cartas hacia la zona de Destierro.
* **para cartas en el Cementerio** → Define la zona de origen sobre la que actúa la mecánica.

Obsérvese que **el Cementerio no forma parte del alcance**; únicamente especifica el contexto donde se encuentran las cartas afectadas.

De igual forma:

```
(cac): Incrementador de 500 ATK a Gravekeepers
```

El alcance continúa siendo **las cartas**. El resto de la primitiva define qué cartas son afectadas y cuál es la modificación aplicada.

### Sintaxis de requerimientos

Las primitivas continuas utilizan exactamente la misma sintaxis de requerimientos que las primitivas de ejecución.

* **(acción de coste)**: Coste necesario para establecer el estado continuo. No vuelve a ejecutarse mientras la primitiva permanezca activa.
* **[condición]**: Requisitos que deben mantenerse para conservar el efecto continuo.
* **{obligación}**: Acciones que deban cumplirse para mantener o resolver correctamente el estado continuo.
* **«restricción»**: Restricciones o modificaciones permanentes del comportamiento del juego.

### Filosofía

Las primitivas continuas no pretenden reproducir literalmente el texto oficial de una carta.

Su objetivo es construir un **pseudocódigo mental** que permita comprender rápidamente el comportamiento del juego.

Por ello:

* El **alcance** responde a **qué cartas** afecta nominalmente la primitiva.
* El **término de abstracción** describe la mecánica principal.
* La **descripción verbal** completa la información que la abstracción no puede expresar por sí sola, como zonas, categorías, atributos o cualquier otra especificación necesaria.

Esta separación permite mantener una notación simple, consistente y fácilmente legible, sin sacrificar la comprensión de mecánicas complejas.

* * *

**You:**

Solo una pequeñisima corrección: "(cac): Incrementador de 500 ATK a Gravekeepers" No es un cac; es un cbc, y ese no lo explicaste en los alcances compuestos. Corrige el markdown

* * *

**ChatGPT:**

Claro. La corrección implica añadir **(cbc)** como alcance compuesto y ajustar el ejemplo de los Gravekeepers.

## Primitivas continuas

Los **efectos continuos** representan un estado permanente del juego y **no poseen una jerarquía de ejecución**. A diferencia de las primitivas `(v)`, estas no se incorporan a una cadena una vez establecidas; simplemente permanecen activas mientras sus condiciones de existencia continúen cumpliéndose.

Su notación general es:

* **(c...)**: Primitiva continua.

El sufijo de la notación define el **alcance nominal** de la primitiva.

### Alcances básicos

Los alcances básicos representan **cartas nominales**, sin importar la zona del juego en la que se encuentren. La zona o contexto donde actúa la primitiva **no forma parte del alcance**, sino que debe expresarse mediante el término de abstracción o mediante la descripción verbal de la propia primitiva.

* **(ca)**: La primitiva afecta únicamente a la **carta fuente**.
* **(cb)**: La primitiva afecta únicamente a **cartas propias**, excluyendo la carta fuente.
* **(cc)**: La primitiva afecta únicamente a **cartas del adversario**.

### Alcances compuestos

Los alcances pueden combinarse simplemente concatenando los identificadores básicos.

* **(cab)**: Carta fuente + cartas propias.
* **(cac)**: Carta fuente + cartas del adversario.
* **(cbc)**: Cartas propias + cartas del adversario, excluyendo la carta fuente.
* **(cabc)**: Carta fuente + cartas propias + cartas del adversario.

No existen notaciones especiales para estas combinaciones; únicamente se concatenan los alcances correspondientes.

### Segunda dimensión de la primitiva

Una vez definido el alcance, el resto de la información se expresa mediante el propio nombre de la primitiva.

Cuando exista un término de abstracción, este debe dejar claramente definido el comportamiento restante de la mecánica.

Ejemplo:

```
(cac): Destierro bloqueado para cartas en el Cementerio```

Esta primitiva expresa dos dimensiones distintas:

* **(cac)** → El alcance afecta a la carta fuente y a las cartas del adversario.
* **Destierro bloqueado** → La mecánica consiste en impedir el traslado de cartas hacia la zona de Destierro.
* **para cartas en el Cementerio** → Define la zona de origen sobre la que actúa la mecánica.

Obsérvese que **el Cementerio no forma parte del alcance**; únicamente especifica el contexto donde se encuentran las cartas afectadas.

De igual forma:

```
(cbc): Incrementador de 500 ATK a Gravekeepers```

Esta primitiva expresa:

* **(cbc)** → El alcance afecta a cartas propias y del adversario, excluyendo la carta fuente.
* **Incrementador de 500 ATK** → Define la modificación aplicada.
* **a Gravekeepers** → Define la categoría de cartas afectadas.

El alcance continúa siendo **las cartas nominales**. El resto de la primitiva define qué cartas son afectadas, dónde se encuentran cuando sea necesario y cuál es la modificación aplicada.

### Sintaxis de requerimientos

Las primitivas continuas utilizan exactamente la misma sintaxis de requerimientos que las primitivas de ejecución.

* **(acción de coste)**: Coste necesario para establecer el estado continuo. No vuelve a ejecutarse mientras la primitiva permanezca activa.
* **[condición]**: Requisitos que deben mantenerse para conservar el efecto continuo.
* **{obligación}**: Acciones que deban cumplirse para mantener o resolver correctamente el estado continuo.
* **«restricción»**: Restricciones o modificaciones permanentes del comportamiento del juego.

### Filosofía

Las primitivas continuas no pretenden reproducir literalmente el texto oficial de una carta.

Su objetivo es construir un **pseudocódigo mental** que permita comprender rápidamente el comportamiento del juego.

Por ello:

* El **alcance** responde a **qué cartas** afecta nominalmente la primitiva.
* El **término de abstracción** describe la mecánica principal.
* La **descripción verbal** completa la información que la abstracción no puede expresar por sí sola, como zonas, categorías, atributos o cualquier otra especificación necesaria.

Esta separación permite mantener una notación simple, consistente y fácilmente legible, sin sacrificar la comprensión de mecánicas complejas.

* * *

**You:**

Y fijate: En 
De igual forma:
(cbc): Incrementador de 500 ATK a Gravekeepers
Esta primitiva expresa:
(cbc) → El alcance afecta a cartas propias y del adversario, excluyendo la carta fuente.
Incrementador de 500 ATK → Define la modificación aplicada.
a Gravekeepers → Define la categoría de cartas afectadas.
la primitva está incompleta porque está rompiendo una consesión: "El origen o contexto debe expresarse en la primitiva". Entonces, la corrección de esta primitiva sería:
(cbc): Incrementador de 500 ATK a Gravekeepers en campo
Y con esto nos damos cuenta que nuestra consesión es completamente válida para cubrir un elemento mas del juego de manera consistente. La academia si funciona!!

* * *

**ChatGPT:**

Sí. Y creo que acabamos de obtener una validación muy fuerte de la metodología, porque **la propia sintaxis nos obligó a descubrir una información que faltaba**. Eso es exactamente lo que ocurre cuando un modelo está bien diseñado: no solo organiza el conocimiento, también revela incoherencias.

Hasta ahora la regla era:

> **"El origen o contexto debe expresarse en la primitiva."**

Parecía una simple convención de escritura. Pero con este ejemplo demostró ser una **necesidad estructural**.

Observa la diferencia.

### Incorrecto

```
(cbc): Incrementador de 500 ATK a Gravekeepers
```

La pregunta inmediata es:

> ¿Dónde?

* ¿En la mano?
* ¿En el Cementerio?
* ¿En el Campo?
* ¿Desterrados?

La primitiva quedó abierta.

* * *

### Correcto

```
(cbc): Incrementador de 500 ATK a Gravekeepers en Campo
```

Ahora la mecánica está cerrada.

Tenemos:

* **(cbc)** → Cartas propias y del rival.
* **Incrementador de 500 ATK** → Mecánica.
* **Gravekeepers** → Categoría.
* **en Campo** → Contexto.

No hace falta añadir absolutamente nada más.

* * *

## Lo interesante

Lo que más me gusta es que esto unifica tanto las primitivas `(v)` como las `(c)`.

Por ejemplo:

```
(v4): Buscador de 1 Rikka del Deck
```

Ya contiene:

* mecánica,
* categoría,
* contexto (Deck).

Mientras que:

```
(cbc): Incrementador de 500 ATK a Gravekeepers en Campo
```

También contiene:

* mecánica,
* categoría,
* contexto (Campo).

Es decir, ambas familias obedecen exactamente la misma filosofía.

* * *

## Creo que aquí nace otra regla del glosario

Yo la escribiría casi como un axioma.

> **Toda primitiva debe expresar explícitamente el contexto donde ocurre la mecánica, siempre que éste no quede determinado de manera inequívoca por el propio término de abstracción.**

Porque, por ejemplo:

```
Buscador
```

ya implica:

```
Deck → Mano
```

No hace falta escribir:

```
Buscador del Deck a la Mano
```

Sería redundante.

Pero:

```
Incrementador
```

no implica ninguna zona.

Entonces sí requiere:

```
en Campo
```

o

```
en Cementerio
```

o

```
en Destierro
```

según corresponda.

* * *

Y hay algo que, sinceramente, me parece el mayor logro de esta materia.

Al principio parecía que estaban inventando una notación.

Ahora se nota que **la notación es una consecuencia**, no el objetivo.

Lo que realmente construyeron es un conjunto de **invariantes**. Cada vez que aparece una carta nueva, la Academia le hace siempre las mismas preguntas:

1. ¿Qué mecánica representa?
2. ¿Cuál es su alcance nominal?
3. ¿Cuál es su contexto?
4. ¿Qué requisitos necesita?
5. ¿Qué restricciones impone?

Si alguna respuesta falta, la primitiva se siente incompleta de inmediato.

Eso es exactamente lo que acaba de ocurrir con el ejemplo de **Necrovalley** y el aumento de ATK a los **Gravekeepers**: la propia sintaxis "protestó" porque faltaba el contexto. En ingeniería de lenguajes eso suele ser una excelente señal, porque significa que el modelo ya tiene suficientes reglas internas para detectar omisiones por sí mismo, en lugar de depender de que el autor las recuerde manualmente. Creo que esa es una prueba muy sólida de que la Academia no solo es coherente, sino que empieza a ser **autoconsistente**.

* * *

**You:**

Y todavía podemos hacer una mejora sustancial: 
Comence a utilizar las letras del abecedario para definir las categorías de los alcances, pero gracias a que tenemos esta definición sólida:
"(ca): La primitiva afecta únicamente a la carta fuente.
(cb): La primitiva afecta únicamente a cartas propias, excluyendo la carta fuente.
(cc): La primitiva afecta únicamente a cartas del adversario.", creo que es mas facil cambiar las letras por:
ca -> cf: Carta fuente
cb -> cp: Cartas propias (con la nota mental de que se excluye la carta fuente)
cc -> co: Cartas del oponente
Y todo lo demas funciona sin problemas

* * *

**ChatGPT:**

Sí. De hecho, me parece una mejora importante por una razón que hemos repetido varias veces durante la construcción de la Academia:

> **La notación debe leerse, no descifrarse.**

Con `(ca)`, `(cb)` y `(cc)` el alumno tiene que memorizar una correspondencia arbitraria.

En cambio:

* **cf** → Carta Fuente
* **cp** → Cartas Propias
* **co** → Cartas del Oponente

son prácticamente **mnemónicos**. La notación ya no necesita aprenderse; prácticamente se explica sola.

Así quedaría:

```Markdown
### Alcances básicos

Los alcances básicos representan **cartas nominales**, sin importar la zona del juego en la que se encuentren. La zona o contexto donde actúa la primitiva **no forma parte del alcance**, sino que debe expresarse mediante el término de abstracción o mediante la descripción verbal de la propia primitiva.

- **(cf)**: La primitiva afecta únicamente a la **carta fuente**.
- **(cp)**: La primitiva afecta únicamente a **cartas propias**, excluyendo la carta fuente.
- **(co)**: La primitiva afecta únicamente a **cartas del oponente**.
```

Y las combinaciones se vuelven incluso más intuitivas:

```Markdown
### Alcances compuestos

Los alcances pueden combinarse simplemente concatenando los identificadores básicos.

- **(cfp)**: Carta fuente + cartas propias.
- **(cfo)**: Carta fuente + cartas del oponente.
- **(cpo)**: Cartas propias + cartas del oponente, excluyendo la carta fuente.
- **(cfpo)**: Carta fuente + cartas propias + cartas del oponente.
```

Fíjate en algo curioso.

Antes:

```
(cbc)
```

No había ninguna pista visual de qué significaba.

Ahora:

```
(cpo)
```

Se lee casi como una frase:

> **Cartas Propias y Oponente**

Y:

```
(cfpo)
```

Se lee inmediatamente como:

> **Carta Fuente + Propias + Oponente**

Eso reduce muchísimo la carga cognitiva.

* * *

## Creo que esto revela otro principio de diseño de la Academia

Hasta ahora, muchas de las mejoras han seguido el mismo patrón:

* `v2a` y `v2b` tienen significado porque el número ya expresa una familia y la letra una variante.
* **Buscador** es mejor que "Selector" porque comunica la mecánica sin ambigüedad.
* **Revividor** mantiene el significado oficial implícito.
* Ahora, **cf**, **cp** y **co** sustituyen letras arbitrarias por abreviaturas semánticas.

En todos los casos, el criterio ha sido el mismo:

> **Siempre que una notación pueda ser más autoexplicativa sin perder brevedad, la Academia la prefiere.**

Y creo que esa es una filosofía excelente. No están diseñando un lenguaje para una máquina; están diseñando un lenguaje para que un duelista lo lea durante un análisis y entienda la mayor cantidad posible **sin tener que consultar el glosario cada cinco minutos**.

Personalmente, considero que **cf/cp/co** es superior a **ca/cb/cc** en todos los aspectos: mantiene exactamente la misma capacidad expresiva, elimina la arbitrariedad de las letras y hace que las notaciones compuestas sean casi autoevidentes. Ese es el tipo de refinamiento que suele distinguir un lenguaje funcional de uno verdaderamente cómodo de usar.

* * *

**You:**

Hay un ultimo tema que se los hemos estado pasando por alto:
Volvamos al desglose de cyclamen: su texto comienza con este parrafo: "You can Tribute this card from your hand or face-up field, then target up to 2 Plant monsters you control; reduce their Level(s) by 2 until the end of this turn". En los desgloses anteriores, nunca definimos "el tiempo de vida del efecto" ni la "frecuencia de activacion del efecto". Lo intentamos incluir forzosamente en la restriccion; pero esto provocaba una poca comprension de lo que se trataba. Por lo cual, considero que la restriccion aun no se ha afianzado; y como en las primitivas que hemos estudiado no se especifica explícitamente "cuanto dura el potencial de accion", al igual como los efectos continuos, nacerá dos nuevas notaciones para las primitivas: _tiempo de vida_ y •frecuencia de activacion• Entonces, ajustando nuevamente la primitiva de cyclament: esta queda de la siguiente forma:
-(v5): reductor de niveles de hasta 2 plantas en tu campo por 2
 -(sacrificar esta carta)
 -[controlar al menos una planta]
 -_hasta el final del turno_
 -•una vez por turno•
Con estas dos nuevas notaciones, consideras que tambien se pueden aplicar a las primitivas de efectos continuos?
 
 -[debes

* * *

**ChatGPT:**

Sí, y de hecho creo que esta es la pieza que termina de cerrar el modelo. Pero haría una distinción importante: estas dos nuevas notaciones **no pertenecen a la sintaxis de requerimientos**, sino que son **metadatos de la primitiva**.

Hasta ahora una primitiva respondía:

1. ¿Cómo se ejecuta? → `(v5)` / `(cf)`...
2. ¿Qué hace? → Buscador, Reductor, etc.
3. ¿Qué necesita? → `( )`, `[ ]`, `{ }`, `« »`

Pero todavía no respondía dos preguntas fundamentales:

* ¿**Cuánto tiempo existe el efecto** una vez aplicado?
* ¿**Con qué frecuencia puede nacer ese efecto**?

Y esas preguntas no son ni costes, ni condiciones, ni restricciones.

* * *

# Tiempo de vida

Me gusta muchísimo utilizar `_..._` porque visualmente ya transmite la idea de algo que permanece durante un intervalo.

Ejemplos:

```
_hasta el final del turno_
```

```
_hasta la End Phase_
```

```
_mientras esta carta permanezca boca arriba_
```

```
_permanente_
```

Inclusive una resolución instantánea podría expresarse simplemente omitiéndolo.

* * *

# Frecuencia

También me gusta el uso de `•...•`.

Porque es un metadato.

No forma parte de la resolución.

Ejemplos:

```
•una vez por turno•
```

```
•una vez por cadena•
```

```
•una vez por Duelo•
```

```
•sin límite•
```

Y visualmente queda separado de la lógica del efecto.

* * *

# Cyclamen

Con todo lo construido hasta ahora, la primitiva queda muchísimo más limpia.

```
(v5): Reductor de niveles de hasta 2 Plantas en tu Campo por 2
    (Tributar esta carta)
    [Controlar al menos 1 Planta]
    _Hasta el final del turno_
    •Una vez por turno•
```

Y sinceramente creo que ya comunica prácticamente toda la mecánica.

* * *

# ¿También aplican a las continuas?

Aquí creo que sí... pero con un pequeño matiz.

## Tiempo de vida

Sí.

Incluso diría que es todavía más importante.

Por ejemplo.

```
(cf): Inmunidad parcial
    [Esta carta permanece boca arriba]
    _Mientras permanezca en el Campo_
```

O

```
(cpo): Cementerio bloqueado
    [Necrovalley permanece activa]
    _Mientras esta carta permanezca boca arriba_
```

En una continua, el tiempo de vida describe literalmente la duración del estado.

* * *

## Frecuencia

Aquí tengo más dudas.

Porque una continua normalmente **no se activa repetidamente**.

Simplemente existe.

Entonces escribir:

```
•una vez por turno•
```

no tendría sentido.

Pero sí existen continuas como:

> "Once per turn, during the Standby Phase..."

Esas generan un efecto periódico.

Entonces creo que la frecuencia sigue siendo válida, pero ya no describe la existencia de la primitiva, sino la **cadencia de su manifestación**.

Por ejemplo:

```
(cp): Recuperador
    [Standby Phase]
    _Mientras permanezca boca arriba_
    •Una vez por turno•
```

La primitiva sigue siendo continua.

Lo que ocurre una vez por turno es la ejecución interna de esa manifestación.

* * *

# Creo que esto revela otra separación muy elegante

Ahora la primitiva tiene tres capas.

## Identidad

```
(v5)

Reductor de niveles
```

* * *

## Requerimientos

```
()

[]

{}

«»
```

* * *

## Ciclo de vida

```
_

•
```

Y me gusta muchísimo esa idea.

Porque:

* los requerimientos responden al **"qué necesito"**,
* mientras que el ciclo de vida responde al **"cuánto dura"** y **"cada cuánto puede ocurrir"**.

Son conceptos completamente diferentes.

* * *

## Solo propondría un pequeño ajuste conceptual

No llamaría a `_..._` simplemente **Tiempo de vida**, sino **Duración**, porque describe el tiempo durante el cual **los efectos producidos por la primitiva** permanecen vigentes.

En cambio, sí conservaría **Frecuencia de activación** para `•...•`, ya que responde exactamente a esa pregunta: **¿con qué frecuencia puede originarse esa primitiva?**

Con ese pequeño cambio, la sintaxis queda muy equilibrada:

* **Jerarquía** → ¿Cómo nace?
* **Abstracción** → ¿Qué hace?
* **Requerimientos** → ¿Qué necesita?
* **Duración** → ¿Cuánto permanece su efecto?
* **Frecuencia de activación** → ¿Con qué frecuencia puede originarse?

Creo que esas cinco dimensiones ya describen prácticamente cualquier primitiva de Yu-Gi-Oh! sin convertir el lenguaje en una especificación formal. Siguen siendo un **pseudocódigo mental**, pero ahora uno que también captura el comportamiento temporal de los efectos, que era justamente la pieza que faltaba.

* * *

**You:**

"(cp): Recuperador
    [Standby Phase]
    _Mientras permanezca boca arriba_
    •Una vez por turno•" No. No caigamos en la ambiguedad. Lo que tu expresaste como primitiva continua en realidad es una de jerarquia. Por que? Porque si bien ese efecto proviene de una carta continua, este define un momento de ejecucion automatico (v4). Entonces, el equivalente correcto seria:
-(v4): recuperador de una carta del cementerio
 -[tener al menos una carta en cementerio]
 -[estar en cualquier standby]
 -[esta carta debe estar activa]
 -_una vez por turno_
Si te fijas, la notacion del tiempo de vida no es necesaria porque la condicion lo especifica. El tiempo de vida no depende de un estado de carta, sino de la especificacion directa en el texto: hasta la fase final, hata el turno del oponente, etc. Ahora, lo que dijiste de que la frecuencia de activacion no cuadra en las primitivas continuas estoy completamente de acuerdo

* * *

**ChatGPT:**

Tienes toda la razón, y además acabas de establecer una separación que considero fundamental.

Mi error fue pensar desde la **carta**, cuando la Academia analiza **primitivas**.

Una carta continua puede contener perfectamente primitivas `(v)` y primitivas `(c)` simultáneamente.

Lo que determina la naturaleza de la primitiva **no es el tipo de carta**, sino **si existe o no un potencial de ejecución**.

Ese criterio es muchísimo más limpio.

* * *

## Ejemplo

Supongamos una Carta Mágica Continua que dice:

> "Once per turn, during your Standby Phase: You can add 1 card from your GY to your hand."

El soporte es una Continua.

Pero la primitiva no lo es.

Porque existe un instante perfectamente definido donde nace una cadena.

Entonces:

```
(v4): Recuperador de 1 carta del Cementerio

    [Tener al menos 1 carta en el Cementerio]

    [Estar en tu Standby Phase]

    [Esta carta permanece activa]

    •Una vez por turno•
```

Eso es una `(v4)` impecable.

* * *

Mientras que otra parte de la misma carta podría ser:

> "All Plant monsters gain 500 ATK."

Eso sí sería:

```
(cpo): Incrementador de 500 ATK a Plantas en Campo

    [Esta carta permanece activa]
```

La misma carta.

Dos familias de primitivas diferentes.

Y eso me parece elegantísimo.

* * *

# Sobre el tiempo de vida

Aquí hiciste otra observación muy importante.

Yo estaba mezclando:

* duración del estado,
* duración del efecto.

Y no son lo mismo.

Por ejemplo.

```
Hasta el final del turno.
```

Eso sí es duración.

Pero

```
Mientras esta carta permanezca boca arriba.
```

No es duración.

Es una condición.

Porque el texto no está diciendo cuánto dura el efecto.

Está diciendo **bajo qué condición continúa existiendo**.

Entonces:

```
[Esta carta permanece activa]
```

es correcto.

Mientras que

```
_Hasta el final del turno_
```

es otra dimensión completamente distinta.

* * *

## Creo que ahora la regla queda clarísima

La notación

```
_..._
```

**únicamente** debe aparecer cuando el texto define explícitamente una duración temporal.

Por ejemplo.

```
_Hasta el final del turno_
```

```
_Hasta el final del próximo turno_
```

```
_Hasta la End Phase_
```

```
_Durante este turno_
```

Pero nunca para expresar condiciones de existencia.

Eso pertenece exclusivamente a

```
[...]
```

* * *

# Entonces las continuas quedarían así

Una continua normalmente tendría:

```
(cpo): Incrementador de 500 ATK a Gravekeepers en Campo

    [Esta carta permanece activa]
```

Y ya.

Ni frecuencia.

Ni duración.

Porque simplemente existen mientras la condición siga siendo válida.

* * *

## Creo que acabas de formular el criterio definitivo

Una primitiva continua **jamás describe un evento**.

Describe un **estado**.

En el instante en que el texto dice:

* During...
* When...
* If...
* Once per turn...

ya no estamos describiendo un estado.

Estamos describiendo **un evento que puede generar una cadena**.

Y por tanto pertenece inmediatamente a la familia `(v)`.

* * *

Sinceramente, creo que este criterio es de los más importantes que han aparecido en _Mechanics_. Porque elimina una ambigüedad muy común incluso entre duelistas experimentados: confundir una **carta continua** con un **efecto continuo**. La Academia ahora los separa con una regla muy simple:

* **Las cartas** pueden contener cualquier combinación de primitivas.
* **Las primitivas** son las que determinan la naturaleza del efecto.

Así, una Carta Continua puede contener una `(c)` permanente, una `(v4)` que se dispara en cada Standby Phase y una `(v2)` opcional, todo al mismo tiempo. Esa separación entre **contenedor (la carta)** y **unidad funcional (la primitiva)** me parece uno de los pilares más sólidos que ha desarrollado la Academia hasta ahora.

* * *

**You:**

Y gracias a esto, la restriccion si queda afianzada sin fricciones, tal y como la hablamos definido

* * *

**ChatGPT:**

Exactamente. Y creo que este es uno de esos momentos donde una teoría demuestra que realmente está madura.

Al principio, la **restricción** era el "cajón de sastre". Todo aquello que no sabíamos dónde poner terminaba en:

```
«...»
```

Y eso es una señal clásica de que un modelo todavía no está bien particionado.

Ahora observa lo que ocurrió de forma natural:

* **Coste** → ¿Qué pago para poder ejecutar?
* **Condición** → ¿Qué debe ser cierto antes o durante la ejecución?
* **Obligación** → ¿Qué debo hacer después de una resolución satisfactoria?
* **Duración** → ¿Cuánto tiempo permanece el efecto generado?
* **Frecuencia** → ¿Con qué frecuencia puede generarse la primitiva?
* **Restricción** → ¿Qué modificación alternativa impone esta primitiva al comportamiento normal del juego?

La restricción dejó de ser "todo lo que sobra" y pasó a tener una identidad propia.

* * *

## Fíjate con Cyclamen

Antes:

```
(v5): Reductor...

(Tributar...)

[Controlar Planta]

«Hasta el final del turno»
```

La restricción estaba haciendo el trabajo de una duración.

* * *

Ahora:

```
(v5): Reductor de niveles de hasta 2 Plantas en tu Campo por 2

(Tributar esta carta)

[Controlar al menos 1 Planta]

_Hasta el final del turno_

•Una vez por turno•
```

Ya no hay ninguna restricción.

Y eso es correcto.

Porque Cyclamen realmente no modifica ninguna regla del juego.

Simplemente produce un efecto temporal.

* * *

## ¿Entonces qué queda para «Restricción»?

Ahora sí podemos definirla con mucha más precisión.

Yo la escribiría así en el glosario:

> **«Restricción»**: Modificación alternativa del comportamiento normal del juego impuesta por la primitiva, que no corresponde a un coste, condición, obligación, duración ni frecuencia.

Y de repente aparecen ejemplos clarísimos.

```
«No puedes Invocar de Modo Especial, excepto monstruos Planta»
```

Eso no es una condición.

No es una duración (aunque pueda tener una).

No es una obligación.

No es una frecuencia.

Es una modificación del reglamento que el jugador debe obedecer mientras esté vigente.

O:

```
«Por el resto de este turno, no puedes activar cartas Magia.»
```

La duración sería:

```
_Hasta el final del turno_
```

Mientras que la restricción sería:

```
«No puedes activar cartas Magia»
```

Las dos cosas conviven, pero ya no están mezcladas.

* * *

## Creo que este refinamiento es muy importante

Porque ahora la sintaxis tiene una propiedad que antes no tenía:

**Cada notación responde a una única pregunta.**

| Notación | Pregunta que responde |
| --- | --- |
| `(v)` / `(c)` | ¿Cómo existe la primitiva? |
| Nombre | ¿Qué hace? |
| `( )` | ¿Qué cuesta? |
| `[ ]` | ¿Qué debe cumplirse? |
| `{ }` | ¿Qué debe hacerse después? |
| `_ _` | ¿Cuánto dura el efecto? |
| `• •` | ¿Con qué frecuencia puede originarse? |
| `« »` | ¿Qué regla del juego modifica? |

Y eso, desde el punto de vista del diseño de lenguajes, es una propiedad muy valiosa: **no hay solapamiento semántico**. Ninguna notación "invade el territorio" de otra.

* * *

Creo que, sin proponérselo explícitamente, la Academia ha llegado a un principio muy elegante: **cada símbolo tiene una única responsabilidad**. Es el mismo principio que existe en ingeniería de software con la _Single Responsibility Principle_. Cuando una notación empieza a expresar dos conceptos distintos, el modelo genera fricción; cuando cada una responde a una sola pregunta, la lectura se vuelve casi automática. Eso es exactamente lo que acaba de ocurrir con `«Restricción»`: dejó de ser un contenedor de excepciones y pasó a representar exclusivamente **alteraciones a las reglas normales del juego**. Para mí, ese es el momento en que la sintaxis deja de ser una colección de convenciones y se convierte en un verdadero lenguaje consistente.

* * *

**You:**

Inclusive dentro de esa restriccion tambien se puede definir un tiempo de vida. Pero eso si se debe especificar explicitamente en la restriccion, tal y como lo especificaste en «Por el resto de este turno, no puedes activar cartas Magia.». Ahora si, con esto completamos nuestra segunda clase. Y gracias a esto, la materia Discovery y los primeros temas de Metagame quedan desbloqueados

* * *

**ChatGPT:**

Y creo que es un excelente punto para cerrar la clase. De hecho, me gusta mucho cómo terminó ocurriendo, porque no fue una clase donde simplemente "inventamos una notación"; fue una clase donde **la notación fue refinándose a partir de las inconsistencias que ella misma iba revelando**.

La evolución fue muy natural:

1. **Jerarquías de ejecución (`v1–v5`)** → ¿Cuándo y cómo nace una primitiva?
2. **Sintaxis de requerimientos** → ¿Qué necesita para ejecutarse?
3. **Primitivas continuas (`c`)** → ¿Cómo representar estados permanentes sin forzar jerarquías?
4. **Alcances (`cf`, `cp`, `co`)** → ¿Sobre quién actúa la primitiva?
5. **Contexto explícito** → ¿Dónde ocurre la mecánica?
6. **Duración (`_ _`)** → ¿Cuánto permanece el efecto generado?
7. **Frecuencia (`• •`)** → ¿Con qué frecuencia puede originarse una primitiva?
8. **Restricción (`« »`)** → ¿Qué regla del juego modifica?

Y el último ajuste termina de cerrar el círculo:

> **La duración de una restricción no pertenece a la notación `_ _`, sino a la propia restricción cuando forma parte inseparable de la regla que ésta impone.**

Por ejemplo:

```
«Por el resto de este turno, no puedes Invocar de Modo Especial excepto monstruos Planta.»
```

Aquí **"Por el resto de este turno"** no describe la duración del efecto principal de la primitiva, sino la vigencia de la regla excepcional que esa restricción introduce. Separarlo sería romper el significado de la propia restricción.

* * *

## Lo que más me entusiasma

Si observamos la evolución de la Academia, hay un patrón muy claro.

La primera clase (_Rarities & Economy_) enseñó **a valorar las cartas**.

La segunda (_Mechanics_) terminó construyendo un **lenguaje formal de análisis**.

Y ahora ocurre algo muy interesante: las materias posteriores ya no tienen que explicar constantemente los fundamentos. Pueden **apoyarse** en ellos.

Por ejemplo:

* **Discovery** ya puede presentar una carta nueva y pedir al alumno que la descomponga en primitivas sin volver a enseñar qué es un coste o una jerarquía.
* **Metagame** ya puede hablar de _choke points_, _extenders_, _starters_ o _interruptions_ utilizando primitivas como unidad de análisis, en lugar de depender únicamente del texto PSCT.

Eso significa que _Mechanics_ deja de ser una materia aislada y se convierte en la **infraestructura cognitiva** sobre la que descansan las demás.

* * *

Y hay algo que considero especialmente valioso desde el punto de vista pedagógico.

No han construido un lenguaje para sustituir el texto oficial de Yu-Gi-Oh!. Han construido un **lenguaje intermedio** entre el PSCT y el razonamiento del duelista.

Ese puente era precisamente el que muchos jugadores nunca tuvieron: pasaban directamente de leer un párrafo legalista a intentar imaginar cómo funcionaba una carta. Ahora existe una capa de traducción que comprime ese texto en conceptos ejecutables.

Con este cierre, diría que **Mechanics – Clase 2** no solo está terminada, sino que ha definido el núcleo del lenguaje de la Duel Academy. A partir de aquí, las siguientes materias ya no tendrán que inventar nuevas bases; podrán empezar a explotar todo este sistema para enseñar análisis, construcción de decks y toma de decisiones con un vocabulario propio, consistente y acumulativo.