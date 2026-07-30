---
title: "THE YU-GI-OH! DUEL ACADEMY - Mechanics (clase 2)"
source: "https://chatgpt.com/g/g-p-6a629ec826208191925517eb500ea14a-the-yu-gi-oh-duel-academy/c/6a6305c6-923c-83e8-9089-1b00f2f6c96a"
---

**You:**

Bien. Ahora entraremos a la clase 1 de Mechanics.
El profesor llega, se presenta y advierte: Esta materia es una de las dos mas dificiles del curso (la otra es Pilotage). Que aprenderemos en esta materia? Aprenderemos como jugar el formato avanzado a nivel competitivo. Aqui es donde encontraremos grietas en las mecanicas mas dificiles, descubriremos el ciclo de vida de un combo, la sinergia entre cartas, las erratas, en fin, todo lo mas hype que yugi puede ofrecer.
Primero entraremos en materia revisando nuestro glosario. Analizaremos la explicacion de las velocidades de efectos, su nomenclatura, y veremos si es una definicion valida o si se nos esta escapando algo, y despues bajaremos la conceptualización de un efecto a acciones. El objetivo de esto es tener un glosario y una sintaxis correcta para definir las primitivas de forma precisa. Esto nos ayudara a una comprension mas rapida de combos y efectos y nos permitirá hacer un analisis mas profundo

* * *

**ChatGPT:**

Me gusta mucho el enfoque que está tomando esta materia. De hecho, creo que hace una distinción importante que rara vez se hace cuando alguien enseña Yu-Gi-Oh! competitivo:

* **Pilotage** responde a _"¿Qué decisión tomo?"_
* **Mechanics** responde a _"¿Por qué esa decisión existe?"_

Es una diferencia enorme. Un jugador puede memorizar un combo sin entenderlo. Pero si entiende las mecánicas que lo forman, puede reconstruirlo incluso cuando cambian las cartas.

Tomando como base el documento de la academia, la primera clase podría quedar estructurada así.

* * *

# Mechanics I

## Introducción

> _"Bienvenidos a Mechanics."_

Esta es una de las dos materias más complejas de toda la academia (junto con **Pilotage**).

Aquí dejaremos de aprender **cartas** para comenzar a estudiar **el funcionamiento interno del juego**.

No aprenderemos simplemente qué hace una carta.

Aprenderemos:

* por qué un combo funciona,
* cuándo deja de funcionar,
* cómo extenderlo,
* cómo romperlo,
* cómo reconocer el mismo patrón en arquetipos completamente distintos.

En otras palabras:

> Mechanics estudia la ingeniería del formato avanzado.

* * *

# Objetivo de la materia

Al finalizar esta materia el alumno deberá ser capaz de observar cualquier carta y descomponerla en sus primitivas.

No importa si pertenece a:

* Six Samurai
* Snake-Eyes
* Branded
* Dragon Link
* Plunder Patrol
* Sky Striker

Todas obedecen las mismas reglas fundamentales.

Cuando comprendemos esas reglas, los arquetipos dejan de parecer "memorización" y comienzan a verse como sistemas.

* * *

# Primera unidad

## El lenguaje de Yu-Gi-Oh!

Antes de estudiar efectos debemos asegurarnos de que todos hablamos exactamente el mismo idioma.

Para ello revisaremos dos herramientas fundamentales:

* Glosario de velocidades
* Sintaxis de efectos

El objetivo no es aprender nombres.

El objetivo es crear un lenguaje suficientemente preciso para describir cualquier carta del juego.

* * *

# Parte 1

## Las velocidades de efectos

En el glosario actual encontramos la siguiente clasificación:

* (v0) Chain
* (v1) Counter
* (v2) Quick Effect
* (v3) Conditional Auto
* (v4) Conditional Manual
* (v5) Manual

Aquí aparece la primera advertencia de la materia.

* * *

## ¿Esta clasificación es oficial?

No.

Y eso es completamente intencional.

La clasificación oficial de Konami habla de:

* Spell Speed 1
* Spell Speed 2
* Spell Speed 3

Sin embargo...

Esa clasificación resulta insuficiente cuando queremos analizar un combo.

Porque dos efectos que oficialmente pertenecen a Spell Speed 1 pueden comportarse de manera totalmente distinta.

Por ejemplo:

* Un efecto obligatorio.
* Un efecto opcional.
* Un efecto de Ignition.
* Un Trigger.

Todos son Spell Speed 1.

Pero estratégicamente no funcionan igual.

* * *

## Entonces...

El glosario de la academia no intenta reemplazar el reglamento.

Intenta ofrecer una clasificación **funcional**.

Es decir:

> "¿Cómo se comporta este efecto cuando analizamos un combo?"

No:

> "¿Qué nombre oficial le dio Konami?"

Esa diferencia será muy importante durante toda la materia.

* * *

# Parte 2

## ¿Qué es realmente un efecto?

Esta probablemente sea la idea más importante de toda la unidad.

Cuando un jugador principiante lee una carta ve un párrafo.

Un jugador competitivo ve una secuencia de acciones.

Por ejemplo:

```
Descarta 1 carta;
Invoca especialmente 1 monstruo...
```

No es un texto.

Es una cadena de operaciones.

Cada operación tiene:

* requisitos
* costos
* acciones
* consecuencias
* restricciones

Y cada una puede estudiarse por separado.

* * *

# Nuestro objetivo

Durante Mechanics aprenderemos a dejar de leer cartas como texto.

Comenzaremos a leerlas como algoritmos.

Porque un combo no es otra cosa que una composición de algoritmos que interactúan entre sí.

* * *

## La siguiente clase

Con el glosario establecido, la siguiente lección consistirá en responder una pregunta aparentemente sencilla:

> **¿Qué es exactamente un efecto?**

No desde el reglamento.

Sino desde la perspectiva de la ingeniería del juego.

Ahí comenzaremos a descomponer un efecto en **acciones primitivas**, que serán los "átomos" con los que construiremos el resto de la materia.

* * *

## Una observación sobre el glosario

Hay un detalle que me parece especialmente prometedor en tu enfoque: has creado una nomenclatura orientada al **análisis**, no al reglamento.

De hecho, sospecho que conforme avance la materia, algunas categorías evolucionarán. Por ejemplo, **(v0) Chain** no parece ser una velocidad de efecto en sí, sino un concepto relacionado con la inserción o construcción de la cadena. Del mismo modo, **Counter** podría redefinirse como una categoría ligada a _Spell Speed 3_ y **Quick Effect** a _Spell Speed 2_. No es un problema; al contrario, es una buena señal. Significa que el glosario está vivo y puede refinarse conforme descubramos una sintaxis más rigurosa para describir las primitivas del juego. Creo que esa evolución será parte natural del desarrollo de la academia.

* * *

**You:**

Muy bien. En si, el glosario de velocidades no solo habla de velocidades como tal, sino de "permisos de ejecución". Y estos permisos se catalogan bajo una jerarquia, cuya jerarquia es sinonimo de velocidad. Y estos permisos de ejecucion estan fuera de los conceptos de costo, obligacion, condicion, etc. Ya que estos definen como se construye el stack de una cadena. Entonces dicho esto, quiero saber si este glosario de velocidades puede ser valido para definir el reglamento de ese stack, o si hay algo que no cuadra

* * *

**ChatGPT:**

Creo que estás tocando un punto muy interesante. De hecho, la clave está en dejar de pensar en "velocidad" como un atributo temporal y empezar a verla como un **permiso de inserción en la cadena**.

Esa idea es bastante sólida.

Pero al revisar tu glosario veo dos cosas distintas mezcladas:

1. **Permisos para construir la cadena.**
2. **Forma en que un efecto obtiene el derecho de activarse.**

Y esas dos cosas no siempre coinciden.

* * *

## Lo que sí me parece correcto

Tu definición implícita sería algo así:

> Una velocidad no indica qué tan rápido ocurre un efecto, sino qué prioridad tiene para solicitar un nuevo Chain Link.

Eso me gusta mucho más que la explicación tradicional de Konami.

Porque realmente la cadena funciona así.

Cuando ocurre un evento, el juego pregunta continuamente:

> "¿Quién tiene permiso para agregar el siguiente eslabón?"

No pregunta:

> "¿Quién es más rápido?"

En ese sentido, podríamos incluso hablar de una **jerarquía de permisos**.

* * *

## Donde encuentro el primer problema

Veamos tu lista.

```
(v0) Chain
(v1) Counter
(v2) Quick
(v3) Conditional Auto
(v4) Conditional Manual
(v5) Manual
```

Los dos primeros niveles son permisos para responder.

Los últimos tres son permisos para iniciar.

Es decir, mezclan dos dimensiones distintas.

* * *

Por ejemplo:

Un Trigger obligatorio (tu v3) no es "más lento" que un Quick Effect.

Simplemente **no pertenece al mismo momento del reglamento**.

Uno solicita entrar cuando ocurre un evento.

El otro puede solicitar entrar mientras la cadena sigue abierta.

Son mecanismos distintos.

* * *

## El segundo problema

(v0) Chain.

Aquí es donde creo que deberíamos detenernos.

La cadena no es un permiso.

La cadena es el objeto que recibe permisos.

Una analogía:

Si una autopista recibe vehículos,

los vehículos tienen permisos de circulación.

La autopista no es un permiso.

* * *

Por eso creo que:

```
(v0) Chain
```

No encaja como una velocidad.

Encaja como el entorno donde viven todas las velocidades.

* * *

## El tercer problema

Conditional Auto  
Conditional Manual

Aquí sí creo que estás descubriendo algo importante.

Porque estas categorías no hablan de velocidad.

Hablan del **origen del permiso**.

Es decir:

¿Cómo obtuvo el efecto permiso para intentar activarse?

Hay varias posibilidades.

Por ejemplo:

Manual

"Yo decido activarlo."

Trigger

"El juego me dio permiso porque ocurrió X."

Quick

"El reglamento me permite interrumpir."

Counter

"El reglamento me permite responder incluso a Quick."

Observa que estas cuatro categorías describen el origen del permiso.

No su prioridad.

* * *

## Creo que el modelo tiene otra forma

Si yo intentara formalizar tu idea, probablemente separaría completamente ambas dimensiones.

### Dimensión 1

**Origen del permiso**

```
Manual

Trigger obligatorio

Trigger opcional

Quick

Counter
```

* * *

### Dimensión 2

**Jerarquía dentro de la cadena**

```
Spell Speed 1

Spell Speed 2

Spell Speed 3
```

Entonces cada efecto tendría dos etiquetas.

Ejemplo.

Ash Blossom

```
Origen:
Quick Response

Jerarquía:
Spell Speed 2
```

Monster Reborn

```
Origen:
Manual

Jerarquía:
Spell Speed 1
```

Mirror Force

```
Origen:
Trigger

Jerarquía:
Spell Speed 2
```

Solemn Judgment

```
Origen:
Counter

Jerarquía:
Spell Speed 3
```

Aquí ya no mezclamos conceptos.

* * *

## Sin embargo...

Hay algo que me hace pensar que tu modelo puede ir todavía más lejos.

Has dicho una frase muy importante:

> "estos permisos están fuera de costo, obligación, condición, etc."

Y creo que tienes razón.

Porque si algún día quieres descomponer un efecto en primitivas, probablemente cada efecto pueda describirse con cinco componentes completamente independientes:

```
Permiso de ejecución
↓
Condición
↓
Costo
↓
Acción
↓
Restricciones posteriores
```

Es decir, el permiso sería simplemente la primera pregunta del motor del juego:

> **¿Este efecto tiene derecho a intentar entrar a la cadena?**

Si la respuesta es no, todo lo demás deja de importar.

Si la respuesta es sí, entonces recién evaluamos condición, costo, resolución y restricciones.

* * *

### Mi única modificación importante

No cambiaría la idea de "permisos de ejecución"; me parece más potente que hablar de "velocidades". Lo que sí haría es separar rigurosamente dos ejes:

1. **El origen del permiso** (manual, disparado, quick, counter, etc.).
2. **La prioridad reglamentaria** con la que ese permiso puede ocupar un Chain Link (Spell Speed 1, 2 o 3).

Con esa separación, tu modelo deja de competir con el reglamento oficial y pasa a describir una capa más profunda: **cómo el motor del juego concede y ordena el derecho a construir una cadena**. Desde una perspectiva de ingeniería, esa abstracción me parece muy prometedora para el resto de la materia.

* * *

**You:**

Muy bien. Comenzare explicandote porque decidi mezclar conceptos:
-realmente no tenia claro sobre como konami estaba puliendo estas problematicas, y realmente no me molesto en leer documentacion oficial. Yugi siempre trata de ser "autoaprendible", y por eso creo que la mejor opcion para ellos fue escribir texto en prosa, como un manual para cada carta. Entonces, esta mezcla surgio porque estaba tratando de incluir conceptos que difícilmente se pueden separar de manera concreta, y son cosas que terminan asumiendose.
-el v0: chain: lo asumi por Apollousa. Esa cosa especifica "Once per chain". Que asumi? Justo lo que describe. Realmente nunca he visto como resuelve un apollousa dentro de una cadena larga de Master duel, y por lo cual asumi que: Si el stack ya tiene una secuencia consolidada, entonces apollousa puede colar su efecto en cualquier espacio de la secuencia.
Ahora, tu correccion es aceptable, pero el separar esas dos dimensiones hace que se vuelva mas borroso identificar que carta domina sobre otra. Si desglosamos Apollousa con mi glosario, inmediatamente identifico que tiene un efecto V0: osea el mas puerco que existe!. Entonces como podriamos devolverle esa claridad con tu nueva propuesta?

* * *

**ChatGPT:**

Creo que aquí está ocurriendo algo muy interesante: tu objetivo **no es modelar el reglamento**, sino **crear un lenguaje de análisis**.

Y eso cambia completamente los criterios.

Un ejemplo: en electrónica hablamos de "tierra", pero la tierra no existe físicamente como un objeto. Es una abstracción útil. Mientras la abstracción prediga correctamente el comportamiento del circuito, es válida.

Con tu glosario pasa lo mismo.

* * *

## El problema de mi propuesta

Tienes razón en una cosa.

Si digo:

```
Origen: Quick
Spell Speed: 2
```

he sido más correcto...

...pero perdí información visual.

Ya no veo inmediatamente quién domina a quién.

Y esa jerarquía es precisamente la información que buscas transmitir.

* * *

## Entonces quizá el error es asumir que la jerarquía debe ser oficial

Quizá no.

Quizá necesitas una jerarquía **pedagógica**.

Algo así:

```
Nivel de autoridad
```

No:

```
Spell Speed
```

Porque en realidad no estás clasificando velocidad.

Estás clasificando **quién puede imponerse sobre quién**.

Eso es distinto.

* * *

## Me hizo pensar en compiladores

Cuando un compilador analiza código existen operadores con prioridad.

```
2 + 3 * 4
```

El asterisco "domina" al signo +.

No porque sea más rápido.

Sino porque tiene mayor prioridad.

Tal vez tu glosario está intentando describir exactamente eso.

Una jerarquía de prioridad.

* * *

## Entonces cambiaría completamente la definición

En vez de llamarlo:

> Velocidades

Lo llamaría:

> **Jerarquía de ejecución**

o

> **Prioridad de ejecución**

Entonces tus niveles ya no hablan de tiempo.

Hablan de autoridad.

* * *

## Pero todavía queda Apollousa...

Aquí sí quiero detenerme.

Porque creo que descubriste algo... pero el ejemplo no es el correcto.

Apollousa dice:

> Once per Chain.

Eso no significa que pueda entrar donde quiera.

Significa algo muchísimo más simple:

```
Dentro de una misma cadena,
este efecto sólo puede activarse una vez.
```

Nada más.

No rompe las reglas de construcción de cadenas.

No tiene prioridad especial.

No puede colarse entre CL2 y CL3.

No puede esperar a ver la resolución para decidir.

Simplemente tiene una restricción de frecuencia.

Por eso creo que **Apollousa no debería ser el ejemplo de V0**.

* * *

## Pero... ¿y si el V0 sí existe?

Aquí viene lo interesante.

Creo que sí existe un concepto parecido.

Sólo que no se llama "Once per Chain".

Lo llamaría algo como:

## Permiso inmediato

Ejemplos:

* activar Judgment sobre una activación
* activar un Counter Trap
* responder a un Quick
* responder a un Trigger

Todos estos tienen una propiedad común:

**No generan una nueva ventana.**

Aprovechan una ventana ya abierta.

Eso sí es una categoría.

* * *

## Entonces creo que el V0 debería redefinirse

No como:

```
Once per Chain
```

Sino como algo más general.

Por ejemplo:

```
V0
Permiso interno de cadena
```

Es decir:

> Este permiso sólo existe mientras una cadena ya está siendo construida.

Mientras que:

```
V5
```

requiere una ventana abierta.

* * *

## Pero creo que hay una idea todavía mejor

Mientras leía tu mensaje tuve otra sensación.

Quizá estás intentando construir algo parecido a una **escala de agresividad**.

Es decir:

```
V5
Yo inicio.
```

↓

```
V4
El juego me permitió iniciar.
```

↓

```
V3
El juego me obliga.
```

↓

```
V2
Puedo interrumpirte.
```

↓

```
V1
Puedo interrumpir incluso tu interrupción.
```

↓

```
V0
Tengo una regla especial que modifica cómo participa mi efecto en la cadena.
```

Eso ya no es una clasificación del reglamento.

Es una clasificación de **qué tan dominante es un efecto sobre el flujo normal del juego**.

Y, curiosamente, esa escala sí resulta muy intuitiva para analizar cartas.

* * *

## Mi propuesta

No abandonaría tu numeración. De hecho, me gusta porque transmite una jerarquía visual inmediata.

Lo que cambiaría es **qué representa el número**.

En lugar de decir:

> "V0 es la velocidad más alta."

Diría:

> **"V representa el nivel de autoridad que tiene un efecto sobre el flujo normal de construcción de la cadena."**

Así:

* **V5** → Actúa sólo cuando el jugador decide y el juego le abre una ventana.
* **V4** → Actúa cuando un evento le concede permiso, pero el jugador elige si usarlo.
* **V3** → Actúa cuando el juego le concede permiso y además obliga a usarlo.
* **V2** → Puede insertarse como respuesta durante una cadena (Quick Effects y Trampas Normales).
* **V1** → Puede responder incluso a respuestas (Counter Traps / Spell Speed 3).
* **V0** → **Reserva este nivel para excepciones reales del motor del juego**, es decir, efectos que alteran las reglas normales de construcción o participación en la cadena. Hoy quizá no tengas un ejemplo definitivo, y eso está bien; es preferible dejar el nivel como "reservado" que llenarlo con un caso que no encaja, como Apollousa.

Eso preserva exactamente la claridad que buscas ("esta carta tiene más autoridad que aquella") sin atarte a una interpretación incorrecta del reglamento oficial. Además, deja espacio para que, si durante la materia descubres una mecánica verdaderamente excepcional del motor, tengas un lugar natural donde ubicarla. Creo que esa flexibilidad será muy valiosa para el glosario de la academia.

* * *

**You:**

Brillante! Entonces no estaba tan errado como pensaba. Con tu definicion de v2 y v1 me acabas de corregir algo que asumi erróneamente: Un quick effect tiene la misma jerarquia que una trampa counter, y veo que no: la trampa counter es mas "rapida" que un quick effect. Ahora una observacion: el v4 y v5 asumo que tienen exactamente la misma naturaleza, tan solo porque uno puede elejir no hacerlo y el otro debe hacerse "en automatico". Entonces, la jerarquia entre esos dos es por conveniencia: por sentido comun, tener la capacidad de elejir hacer algo es mejor que obligarte a hacerlo

* * *

**ChatGPT:**

Sí. De hecho, acabas de encontrar algo que me parece una mejora muy elegante para el glosario.

Y además me hizo darme cuenta de otra cosa: **tu jerarquía no es una jerarquía de poder absoluto**, sino una jerarquía de **libertad de ejecución**.

Hay una diferencia sutil.

* * *

Veamos V4 y V5.

Desde el punto de vista del motor del juego, ambos pertenecen prácticamente al mismo nivel.

Los dos son Spell Speed 1.

Los dos esperan una ventana válida.

Los dos no pueden responder a una cadena.

Hasta ahí, son equivalentes.

La diferencia aparece en quién toma la decisión.

## V4

El motor dice:

> "Ya puedes hacerlo."

Y el jugador responde:

> "Quiero."

o

> "No quiero."

Existe decisión.

* * *

## V5

El motor dice:

> "Debes hacerlo."

El jugador ya no participa.

La decisión desaparece.

* * *

Y aquí es donde me gusta mucho tu interpretación.

Porque, efectivamente, desde un punto de vista competitivo:

**tener opciones siempre es mejor que no tenerlas.**

No porque el efecto sea más fuerte.

Sino porque posee mayor libertad táctica.

* * *

## Me gusta pensar en ello así

No estás clasificando efectos.

Estás clasificando **el grado de control que el jugador conserva sobre ellos.**

Entonces:

```
V5
El jugador tiene el menor control.

↓

V4
El jugador decide.

↓

V2
El jugador además puede esperar y responder.

↓

V1
El jugador puede responder incluso a las respuestas.
```

Eso ya forma una escala muy coherente.

* * *

## Incluso creo que cambiaría los nombres

Porque "Conditional Auto" y "Conditional Manual" describen el origen del efecto.

Pero la diferencia real es otra.

Por ejemplo:

```
V5
Obligatorio

V4
Opcional
```

O incluso

```
V5
Mandatory

V4
Optional
```

Son términos que Yu-Gi-Oh! utiliza constantemente.

* * *

## Hay algo más interesante todavía

Creo que sin darte cuenta estás construyendo una métrica.

No una clasificación.

Una **métrica de flexibilidad**.

Es decir:

¿Cuánto control conserva el jugador sobre la ejecución de este efecto?

Y esa pregunta es extremadamente útil cuando analizas cartas.

Por ejemplo.

Dos cartas dicen:

```
Cuando esta carta es destruida...
```

Una dice:

```
Puedes robar 1 carta.
```

La otra dice:

```
Roba 1 carta.
```

El jugador novato dice:

> "Son iguales."

Tu glosario diría inmediatamente:

```
Primera:
V4

Segunda:
V5
```

Y eso comunica algo importantísimo:

> **La primera permite estrategia; la segunda impone comportamiento.**

* * *

## Creo que descubrimos una regla de diseño

Si esta academia pretende analizar cartas desde un punto de vista mecánico y competitivo, entonces el criterio no debería ser:

> "¿Qué tan rápido es?"

Ni siquiera:

> "¿Qué Spell Speed tiene?"

Sino:

> **¿Cuánta autoridad y cuánta libertad tiene este efecto sobre el flujo del duelo?**

Con esa definición, toda la escala empieza a tener un hilo conductor:

* **V5:** El efecto existe, pero el jugador casi no tiene control sobre su ejecución.
* **V4:** El jugador recupera el control de decidir.
* **V2:** El jugador además puede elegir el momento de responder dentro de las ventanas que permite el reglamento.
* **V1:** El jugador puede responder incluso a otras respuestas gracias a una autoridad reglamentaria superior.
* **V0 (si llegara a existir como categoría):** El efecto modifica o trasciende alguna regla normal de construcción de la cadena.

Esa progresión ya no es arbitraria. Es una escala donde, conforme disminuye el número, **aumenta la capacidad del jugador para influir en el desarrollo del duelo**. Y, desde el punto de vista de una materia como _Mechanics_, esa es una abstracción mucho más útil que limitarse a repetir la terminología oficial de Konami. Creo que es precisamente el tipo de lenguaje que facilitará el análisis de combos y la identificación de patrones comunes entre arquetipos.

* * *

**You:**

Excelente. Entonces consolidemos el glosario de velocidades. En primera: No son velocidades. Es muy comodo utilizar esa definicion porque existe en el vocabulario oficial de yugi. Pero asi como lo hemos corregido, no suena a velocidad. Porque? Porque cuando estas jugando un duelo real, no tienes porque ser mas rapido. Puedes pedir que rebobine lo que ya ha hecho, y por reglamento siempre debes permitir el espacio de respuesta entre interacciones (armando el stack). Por lo cual podremos llamarlo: Jerarquias de ejecucion. Si, el nombre es como un marciano, pero podriamos decir que es el nombre tecnico. Entonces quiero que consolides cada item. Y por ahora, eliminamos el v0. Lo dejamos como el nivel 256 de pacman, donde todo se corrompe. La maxima jerarquia por ahora es el v1. Y me encanta que sea de mayor a menor porque asi es como los sistemas clasifican las prioridades de ejecucion

* * *

**ChatGPT:**

Me gusta mucho cómo terminó evolucionando la idea. Ya no estamos intentando competir con la terminología de Konami, sino construyendo un **modelo de ingeniería** para analizar el motor del juego. Eso le da una identidad propia a la academia.

Yo consolidaría el glosario así:

* * *

# Glosario

## Jerarquías de ejecución

Las **Jerarquías de ejecución (V)** describen el nivel de autoridad que posee un efecto para participar en la construcción de una cadena.

No representan la velocidad con la que un jugador debe reaccionar, sino el **permiso reglamentario** que posee un efecto para solicitar un nuevo Chain Link.

Su objetivo es facilitar el análisis mecánico de cartas, combos y ventanas de interacción.

La jerarquía se enumera de mayor a menor autoridad, siendo **V1** la máxima jerarquía conocida dentro del reglamento normal.

* * *

### (V1) Counter

**Máxima jerarquía de ejecución.**

Puede responder incluso a efectos de respuesta de menor jerarquía.

Representa los efectos con la mayor autoridad para incorporarse a una cadena.

El ejemplo clásico son las **Counter Traps**.

**Propiedades**

* Máxima prioridad de ejecución conocida.
* Diseñado para responder a otros efectos.
* Domina sobre cualquier jerarquía inferior.

* * *

### (V2) Quick

**Jerarquía de respuesta.**

Permite que un efecto se incorpore durante la construcción de una cadena como respuesta a una interacción válida.

Es la jerarquía utilizada por los **Quick Effects** y las **Normal Traps**.

**Propiedades**

* Puede responder a acciones del juego.
* No puede imponerse sobre una activación de jerarquía V1.
* Constituye la principal herramienta de interrupción durante el duelo.

* * *

### (V3) Obligatorio

**Jerarquía automática.**

Cuando ocurre el evento especificado por el efecto, el reglamento obliga a incorporarlo a la siguiente cadena válida.

El jugador no posee capacidad de decisión sobre su activación.

**Propiedades**

* Requiere que ocurra un evento específico.
* La activación es obligatoria.
* El jugador no puede omitirla si el efecto puede activarse.

* * *

### (V4) Opcional

**Jerarquía condicional.**

Cuando ocurre el evento especificado, el reglamento concede al jugador el permiso para activar el efecto.

La decisión pertenece completamente al jugador.

**Propiedades**

* Requiere que ocurra un evento específico.
* El jugador decide si utiliza o no el efecto.
* Posee mayor flexibilidad estratégica que V3.

* * *

### (V5) Manual

**Jerarquía de iniciativa.**

El efecto depende completamente de la decisión del jugador y únicamente puede activarse durante una ventana permitida por el reglamento.

No necesita que un evento previo le conceda permiso.

**Propiedades**

* Activación completamente voluntaria.
* Requiere una ventana legal de activación.
* Es la forma más básica de iniciar una interacción.

* * *

## Observaciones

Las Jerarquías de ejecución son **independientes** de los demás componentes de un efecto.

No describen:

* Costos.
* Condiciones.
* Objetivos.
* Resolución.
* Restricciones posteriores.

Únicamente responden a la siguiente pregunta:

> **¿Con qué autoridad puede este efecto solicitar formar parte de una cadena?**

* * *

## Una pequeña sugerencia

Hay un detalle que me gustó mucho de tu idea de eliminar el V0.

No lo eliminaría del todo. Lo declararía como **"reservado"**.

Algo así:

> **V0 — Reservado.**
> 
> Nivel reservado para futuras excepciones del motor del juego o mecánicas que modifiquen las reglas normales de construcción de cadenas. Actualmente no existe una categoría consolidada que justifique su utilización.

Es un guiño elegante al "nivel 256 de Pac-Man". Además, mantiene la numeración intacta. Si algún día descubres una mecánica que realmente merezca romper el modelo (como una excepción reglamentaria muy particular), ya tendrás un lugar natural donde ubicarla sin tener que renumerar todo el glosario. Creo que es una buena decisión de diseño dejar ese "espacio de expansión" desde el principio.

* * *

**You:**

Sublime. Me gusta mucho la descripcion ampliada de cada item. Pero me gustaria que agregaras una descripcion mas compacta, tal y como lo hice al principio. Recuerda que estamos creando un pseudocodigo para potenciar el analisis y la comprension

* * *

**ChatGPT:**

Creo que ahí está precisamente el valor del glosario. El texto largo explica el concepto, pero el **resumen debe ser una primitiva**: una línea que el cerebro identifique al instante mientras analiza una carta.

Intentaría que todas las definiciones sigan el mismo patrón sintáctico. Algo como:

* * *

# Glosario

## Jerarquías de ejecución (V)

Las **Jerarquías de ejecución (V)** describen el nivel de autoridad que posee un efecto para participar en la construcción de una cadena.

No representan la velocidad del jugador, sino el permiso reglamentario con el que un efecto puede solicitar un nuevo **Chain Link**.

Se enumeran de mayor a menor autoridad.

* * *

## (V1) Counter

> **Puede responder incluso a otra respuesta.**

**Descripción técnica**

Máxima jerarquía de ejecución conocida.

Puede incorporarse a una cadena incluso cuando ésta ya contiene efectos de respuesta de menor jerarquía.

**Propiedades**

* Máxima autoridad de ejecución.
* Responde a otros efectos.
* Domina sobre cualquier jerarquía inferior.

* * *

## (V2) Quick

> **Puede responder a una interacción.**

**Descripción técnica**

Permite incorporar un efecto durante la construcción de una cadena como respuesta a una interacción válida.

**Propiedades**

* Interrumpe el flujo normal.
* No supera a V1.
* Principal herramienta de respuesta del juego.

* * *

## (V3) Obligatorio

> **Si ocurre el evento, debe ejecutarse.**

**Descripción técnica**

Cuando ocurre el evento especificado, el reglamento obliga a incorporar el efecto a la siguiente cadena válida.

**Propiedades**

* Requiere un evento.
* No existe elección.
* El motor fuerza su activación.

* * *

## (V4) Opcional

> **Si ocurre el evento, puedes ejecutarlo.**

**Descripción técnica**

Cuando ocurre el evento especificado, el reglamento concede al jugador el permiso para decidir si incorpora el efecto a la cadena.

**Propiedades**

* Requiere un evento.
* Existe elección.
* Mayor flexibilidad estratégica.

* * *

## (V5) Manual

> **Se ejecuta cuando el jugador lo decide.**

**Descripción técnica**

El efecto depende únicamente de la decisión del jugador y de una ventana legal de activación.

**Propiedades**

* No necesita un evento disparador.
* Requiere una ventana válida.
* Es la forma básica de iniciar una interacción.

* * *

## V0

> **Reservado.**

Nivel reservado para futuras excepciones del motor del juego.

* * *

## Creo que podemos llevarlo todavía más lejos

Mientras escribía esto me di cuenta de una característica muy elegante: todas las descripciones pueden seguir exactamente la misma gramática. Eso hará que el cerebro las memorice como instrucciones de un lenguaje.

Por ejemplo:

```
(V1) Responde incluso a una respuesta.
(V2) Responde a una interacción.
(V3) Debe responder a un evento.
(V4) Puede responder a un evento.
(V5) Inicia una interacción.
```

¿Notas el patrón?

No hablamos de monstruos, trampas, Spell Speed ni cartas. Todo está expresado únicamente en términos de **acciones del motor**:

* **Inicia**
* **Puede responder**
* **Debe responder**
* **Responde incluso a una respuesta**

Eso se parece mucho más a un pseudocódigo que a un glosario tradicional, y además deja muy clara la jerarquía. Si dentro de seis meses analizas una carta nueva, bastará con preguntarte: **"¿Cuál de estas cinco frases describe mejor cómo obtiene permiso para ejecutarse?"** y tendrás su clasificación casi de inmediato. Creo que esa simplicidad será uno de los mayores aciertos de la academia.

* * *

**You:**

Entonces, con esto consolidado, ya no tendremos que comprender como konami explica los speed 1, speed 2, etc. Porque asi como veo, su glosario es extremadamente generico. Y supongo que es asi para disfrazarlo como un juego sencillo. Pero sabemos 0erfectamente que no lo es en absoluto

* * *

**ChatGPT:**

Estoy de acuerdo **con un matiz importante**.

No creo que deban olvidar cómo funciona **Spell Speed 1, 2 y 3**, porque eso **sí es el reglamento oficial**. Lo que sí creo es que **no necesitan usarlo como herramienta de análisis**.

Es una diferencia parecida a ésta:

* Un programador sabe que la CPU ejecuta instrucciones máquina.
* Pero cuando diseña un algoritmo, piensa en funciones, objetos y estructuras de datos.

No está ignorando el funcionamiento real; simplemente trabaja en un nivel de abstracción más útil.

Creo que con las **Jerarquías de ejecución** pasa exactamente eso.

* * *

## El problema del glosario oficial

Konami tiene un objetivo muy distinto al tuyo.

Ellos necesitan que cualquier persona pueda abrir un sobre, leer una carta y jugar.

Por eso simplifican muchísimo.

Por ejemplo, el reglamento dice algo parecido a:

> "Spell Speed 2 puede responder a Spell Speed 1 y Spell Speed 2."

Eso es correcto...

...pero no responde las preguntas que realmente se hace un jugador competitivo.

Por ejemplo:

* ¿Quién inicia la cadena?
* ¿Quién obtiene prioridad?
* ¿Cuándo el juego decide por mí?
* ¿Cuándo puedo esperar?
* ¿Qué efectos me obligan?
* ¿Qué efectos puedo reservar?
* ¿Qué nivel de libertad tengo?

Todo eso queda oculto detrás de "Spell Speed".

* * *

## Lo que hace tu glosario

Tu glosario responde precisamente esas preguntas.

No habla de cartas.

Habla del **motor del juego**.

Por ejemplo:

```
V5
Inicia una interacción.
```

Ya sabes inmediatamente:

* no responde a nada;
* necesita una ventana;
* depende del jugador.

No tuviste que pensar en Spell Speed.

* * *

```
V3
Debe responder a un evento.
```

Ya sabes:

* existe un trigger;
* el jugador no decide;
* el motor construirá la cadena por él.

Nuevamente, no necesitaste hablar de Spell Speed.

* * *

## Creo que descubrimos la verdadera diferencia

El glosario oficial clasifica efectos.

El glosario de la academia clasifica **comportamientos**.

Eso es muchísimo más útil para analizar un combo.

* * *

## De hecho...

Creo que ya puedes escribir una nota muy importante para la materia.

> **Las Jerarquías de ejecución no sustituyen el reglamento oficial. Lo abstraen.**
> 
> El objetivo de este glosario no es reemplazar los Spell Speeds de Konami, sino ofrecer un lenguaje de análisis que describa el comportamiento de un efecto desde la perspectiva del motor del juego y facilite el estudio de combos, cadenas e interacciones.

Esa frase protege a la academia de una crítica muy común: _"Eso no es como lo llama Konami."_

Y la respuesta sería:

> **Exacto. Porque no estamos enseñando terminología oficial; estamos construyendo un lenguaje técnico para estudiar el juego.**

* * *

Y hay algo que me entusiasma especialmente.

Cuando comenzamos esta conversación pensé que estábamos simplemente renombrando conceptos oficiales. Ahora veo que no. Lo que estás haciendo es algo más parecido a lo que ocurre en ciencias de la computación: crear una **capa intermedia de abstracción**.

Un compilador no habla en voltajes eléctricos; habla en instrucciones. Un ingeniero de redes no piensa en electrones; piensa en paquetes. Del mismo modo, la _Duel Academy_ no necesita pensar primero en _Spell Speed 1, 2 y 3_ para analizar un combo; puede pensar en **Jerarquías de ejecución**, porque describen mejor el comportamiento que interesa estudiar.

Si esa abstracción se mantiene consistente durante toda la materia, puede convertirse en uno de los elementos distintivos de la academia: un lenguaje propio que haga que analizar un deck se parezca más a leer pseudocódigo que a descifrar párrafos escritos en prosa. Creo que ese era el objetivo desde el principio, y esta primera pieza ya apunta exactamente en esa dirección.

* * *

**You:**

En efecto: No puedes interactuar sin saber el lenguaje, y eso es lo que estamos consolidando. Si no se comprende el lenguaje de interaccion no se puede arrancar la materia.
Con esto cerramos la clase de hoy. No alcanzamos a diagnosticar la sintaxis de costos, condiciones, obligaciones, etc. Pero no importa porque aun no hemos terminado el tema actual (que sutilmente fue una correccion, pero en realidad era una definicion desde cero): Jerarquias de ejecucion.

* * *

**ChatGPT:**

Me gusta mucho cómo cerró esta primera clase, y creo que vale la pena hacer una observación desde el punto de vista didáctico.

En apariencia, la clase trató sobre un glosario.

En realidad, trató sobre **cómo piensa la academia**.

Eso es muchísimo más importante.

* * *

## Lo que realmente ocurrió hoy

El objetivo inicial era revisar el glosario existente.

Sin embargo, conforme comenzó el análisis apareció una pregunta más profunda:

> **¿Qué estamos clasificando realmente?**

Y la respuesta terminó siendo:

> **No estamos clasificando velocidades.**

Estamos clasificando la **autoridad reglamentaria** con la que un efecto puede participar en la construcción de una cadena.

Ese cambio parece pequeño.

No lo es.

Es el tipo de definición que cambia toda una materia.

* * *

## Lo aprendido

Al finalizar la clase queda consolidado que:

* El término **"Velocidades de efectos"** deja de utilizarse dentro de la academia como herramienta de análisis.
* Se adopta el término técnico **Jerarquías de ejecución (V)**.
* Las Jerarquías de ejecución describen el **permiso reglamentario** con el que un efecto puede solicitar un nuevo Chain Link.
* Son independientes de costos, condiciones, objetivos, restricciones y resolución.
* Su propósito es proporcionar un lenguaje técnico para analizar efectos y combos.

También quedó consolidada la escala actual:

* **V1** — Puede responder incluso a otra respuesta.
* **V2** — Puede responder a una interacción.
* **V3** — Si ocurre el evento, debe ejecutarse.
* **V4** — Si ocurre el evento, puede ejecutarse.
* **V5** — Se ejecuta cuando el jugador lo decide.
* **V0** — Reservado.

* * *

## Lo que me parece más elegante

Esta clase demuestra exactamente la filosofía que querías para la academia.

No se trata de memorizar.

Se trata de **desmontar una abstracción**.

Eso me recordó mucho a cómo enseñan arquitectura de computadoras.

Nadie empieza diciendo:

> "Hoy aprenderemos ensamblador."

Primero se define:

> ¿Qué es una instrucción?

> ¿Qué es un registro?

> ¿Qué significa ejecutar?

Aquí pasó exactamente lo mismo.

Antes de estudiar cartas era necesario responder:

> **¿Qué significa que un efecto pueda ejecutarse?**

* * *

## La siguiente clase

Y creo que ahora sí existe un orden natural.

No pasaría todavía a costos.

La siguiente pregunta lógica sería:

> **¿Qué es un efecto?**

Porque ya definimos **quién tiene permiso para ejecutarse**.

Ahora toca definir **qué es exactamente aquello que se ejecuta**.

Y ahí es donde, muy probablemente, nacerá la otra gran pieza del lenguaje de la academia: la sintaxis de **condiciones**, **costos**, **acciones**, **obligaciones** y **restricciones**.

En otras palabras, hoy definimos el **sistema operativo** que decide cuándo un efecto puede correr. La siguiente clase comenzará a definir el **contenido del proceso** que ese sistema operativo ejecuta.

Creo que es un excelente punto de corte para cerrar la primera sesión de _Mechanics_.

* * *

**You:**

No. Eso que dices pertenece al tema 2: Abstraccion del efecto.el siguiente tema es: Como transformar texto a primitivas. Hagamos un ejemplo sencillo:
La carta dice: When this card is destroyed by battle (quick effect) you can draw 1 card.
Inmediatamente cuando dice: When is destroyed by battle se asume que es un v4, pero tambien dice quick effect. Peor aun: tambien suena a una condicion. Terminas revuelto.
La solucion es la siguiente: es un v2. Da la impresion que no porque la condicion fue escrita antes. Entonces, para definir la primitiva, debes comprender el axioma del efecto: que es lo que termina haciendo, o mejor dicho: el resultado final. Entonces la primitiva luciria asi:
-(v2): roba una carta
 -[presente en el campo boca arriba]
 -[recibir ataque y destruirse]
Ahora, pregunta de profesor: y que pasa si el efecto dice: When this card is destroyed by battle (quick effect): draw 1 card? Tiene caracteristicas de v3 pero tambien de v2. Como se escribiria la primitiva? Se debe agregar algo mas? Es por eso que en mi glosario inicial decia: "con o sin restriccion". No es muy explicativo, pero hablaba de eso

* * *

**ChatGPT:**

Creo que acabas de descubrir el siguiente paso lógico del lenguaje, y además explica por qué tu sintaxis empieza por el **resultado** y no por el texto de la carta.

Hay una idea muy fuerte detrás de esto:

> **Una primitiva no representa cómo está escrita la carta. Representa cómo la interpreta el motor del juego.**

Eso cambia completamente la perspectiva.

* * *

## El problema de leer en orden

Tomemos tu ejemplo.

> When this card is destroyed by battle (Quick Effect): You can draw 1 card.

Si lo lees como humano:

```
When...
↓
Destroyed...
↓
Quick Effect...
↓
Draw
```

Todo parece mezclado.

Pero el motor del juego no lo interpreta así.

Primero identifica **qué tipo de permiso tiene el efecto**.

Después verifica si existen las condiciones.

Finalmente ejecuta la acción.

Es decir:

```
Jerarquía
↓
Acción
↓
Condiciones
↓
(Costos)
↓
(Restricciones)
```

Por eso tu primitiva empieza por el V.

No porque esté primero en la carta.

Sino porque es el primer dato que el motor necesita conocer.

* * *

## Tu ejemplo

Carta:

> When this card is destroyed by battle (Quick Effect): You can draw 1 card.

La primitiva sería:

```
(V2): Roba 1 carta
    [esta carta debe estar boca arriba en el campo]
    [es destruida por batalla]
```

Observa que ya no existe el "When".

Porque "When" no es una acción.

Es simplemente la condición que concede permiso para ejecutar el efecto.

* * *

## Ahora viene la pregunta interesante

Cambiamos una palabra.

Antes decía:

```
You can draw 1 card.
```

Ahora dice:

```
Draw 1 card.
```

Ya no aparece el "You can".

* * *

Aquí creo que encontraste una limitación de la sintaxis actual.

Porque ahora tenemos:

* V2
* obligatorio

* * *

Pero...

**No son la misma clase de información.**

Una dice:

> ¿Cuándo puede entrar?

La otra dice:

> ¿Existe elección?

Son ejes distintos.

* * *

## Creo que aquí falta una nueva propiedad

Yo no la metería dentro del V.

Porque romperíamos la definición que acabamos de consolidar.

El V ya significa:

> **Jerarquía de ejecución.**

Y debe seguir significando únicamente eso.

* * *

En cambio agregaría una segunda etiqueta.

Por ejemplo:

```
(V2)(M)
```

o

```
(V2)(O)
```

Donde

```
M = Mandatory
O = Optional
```

Entonces tendríamos:

* * *

Quick opcional

```
(V2)(O): Roba 1 carta
    [destruida por batalla]
```

* * *

Quick obligatorio

```
(V2)(M): Roba 1 carta
    [destruida por batalla]
```

* * *

## ¿Por qué me gusta esto?

Porque mantiene completamente pura la definición de V.

V sigue respondiendo solamente una pregunta.

> ¿Qué autoridad tiene este efecto?

Y la segunda etiqueta responde otra.

> ¿Existe decisión?

* * *

## Pero creo que podemos ir todavía más lejos

Mientras escribía esto me di cuenta de que tu sintaxis ya se está pareciendo muchísimo a un AST (_Abstract Syntax Tree_) de un compilador.

En un compilador nunca mezclas:

* tipo de nodo
* modificadores
* atributos

Todo va separado.

Entonces un efecto podría terminar representándose así:

```
(V2)(O): Roba 1 carta
    [destruida por batalla]
```

Donde:

* **V2** → jerarquía de ejecución.
* **O** → modalidad (opcional).
* **Roba 1 carta** → acción primitiva.
* **[...]** → precondiciones.
* **(...)** → costos (si existen).
* **{...}** → consecuencias obligatorias posteriores.
* **«...»** → restricciones persistentes o alternativas.

* * *

Y aquí es donde creo que aparece una idea que puede cambiar bastante la materia.

En realidad, **V3 y V4 ya no son necesarias como jerarquías independientes**.

¿Por qué?

Porque la diferencia entre ellas no es la autoridad de ejecución, sino la modalidad de activación.

Con este modelo podrías expresar ambos casos de forma más general:

```
(V5)(M)
```

o

```
(V5)(O)
```

o

```
(V2)(M)
```

o

```
(V2)(O)
```

Y de repente el sistema se vuelve **ortogonal**: cada etiqueta describe una sola dimensión.

Eso evita ambigüedades como la que acabas de encontrar con el _Quick Effect_ que puede ser obligatorio u opcional.

### Sin embargo, aquí haría una pausa.

No cambiaría todavía el glosario. Al contrario, usaría este ejemplo exactamente como lo planteaste en clase. Es un excelente **caso de estrés** para la sintaxis. Si un solo efecto puede obligarte a decir "esto es V2, pero también parece V3", significa que el lenguaje aún necesita una dimensión adicional. Ese descubrimiento no invalida el glosario; demuestra que el proceso de diseñar un lenguaje técnico consiste precisamente en encontrar estos casos límite y refinar las primitivas hasta que cada una describa **una sola propiedad del motor del juego**. Ese, en sí mismo, sería un magnífico cierre para este segundo tema de _Mechanics_.

* * *

**You:**

Aclaremos dos cosas:
-Mas elegante que (v2)(M): v2a, v2b (mayusculas o minusculas). A siempre sera mejor (puedes elejir) que B (no puedes elejir)
-v3 y v4 siguen igual, porque ya esta consolidad en mi cabeza. Se le podrán agregar mas notaciones como el v2 si se encuentran otras excepciones. Para mi es mejor acomodar que destruir y volver a empezar.
Dicho esto, modifica el glosario nuevamente (todavia no incluyas la sintaxis de los costos y condiciones)

* * *

**ChatGPT:**

Me gusta la decisión. Desde el punto de vista del diseño de lenguajes, estás aplicando un principio muy sano: **evolución incremental**. No estás rompiendo la sintaxis que ya aprendiste; simplemente la enriqueces cuando aparecen casos límite. Eso hará que la academia tenga continuidad y que el alumno no sienta que "todo cambió" a mitad del curso.

Yo consolidaría el glosario así:

* * *

# Glosario

## Jerarquías de ejecución (V)

Las **Jerarquías de ejecución (V)** describen el nivel de autoridad que posee un efecto para participar en la construcción de una cadena.

No representan la velocidad con la que un jugador debe reaccionar, sino el permiso reglamentario con el que un efecto puede solicitar un nuevo **Chain Link**.

Las Jerarquías de ejecución son independientes de los costos, condiciones, obligaciones, restricciones y resolución del efecto.

Su objetivo es ofrecer un lenguaje técnico que permita analizar cartas, efectos y combos mediante primitivas.

Las jerarquías se enumeran de mayor a menor autoridad, siendo **V1** la máxima jerarquía conocida dentro del reglamento normal.

* * *

## (V1) Counter

> **Puede responder incluso a otra respuesta.**

Máxima jerarquía de ejecución conocida.

Representa los efectos con mayor autoridad para incorporarse a una cadena.

### Variantes

* **V1a** — Activación opcional.
* **V1b** — Activación obligatoria _(reservado para futuras excepciones, si llegaran a existir)._

### Propiedades

* Responde a otros efectos.
* Domina sobre cualquier jerarquía inferior.
* Constituye la máxima autoridad reglamentaria conocida.

* * *

## (V2) Quick

> **Puede responder a una interacción.**

Permite incorporar un efecto durante la construcción de una cadena como respuesta a una interacción válida.

### Variantes

* **V2a** — El jugador decide si activa el efecto.
* **V2b** — El efecto debe activarse cuando su condición se cumple.

### Propiedades

* Puede responder durante una cadena.
* No puede imponerse sobre V1.
* Es la principal herramienta de interrupción del juego.

* * *

## (V3) Obligatorio

> **Si ocurre el evento, debe ejecutarse.**

Cuando ocurre el evento especificado, el reglamento obliga a incorporar el efecto a la siguiente cadena válida.

### Variantes

* **V3a** — Reservado.
* **V3b** — Comportamiento normal.

### Propiedades

* Requiere un evento disparador.
* No existe elección por parte del jugador.
* El motor del juego fuerza su activación.

* * *

## (V4) Opcional

> **Si ocurre el evento, puede ejecutarse.**

Cuando ocurre el evento especificado, el reglamento concede al jugador el permiso para decidir si incorpora el efecto a la cadena.

### Variantes

* **V4a** — Comportamiento normal.
* **V4b** — Reservado.

### Propiedades

* Requiere un evento disparador.
* Existe decisión por parte del jugador.
* Ofrece mayor flexibilidad estratégica que V3.

* * *

## (V5) Manual

> **Se ejecuta cuando el jugador lo decide.**

Representa los efectos cuya activación depende únicamente de la decisión del jugador y de una ventana legal de activación.

### Variantes

* **V5a** — Activación manual convencional.
* **V5b** — Reservado para futuras excepciones.

### Propiedades

* No requiere un evento disparador.
* Necesita una ventana válida de activación.
* Constituye la forma básica de iniciar una interacción.

* * *

## (V0)

> **Reservado.**

Nivel reservado para futuras excepciones del motor del juego o mecánicas que alteren las reglas normales de construcción de cadenas.

Actualmente no existe una categoría consolidada que justifique su utilización.

* * *

## Observaciones

Las **Jerarquías de ejecución** responden únicamente a una pregunta:

> **¿Con qué autoridad puede este efecto incorporarse a una cadena?**

No describen:

* Costos.
* Condiciones.
* Objetivos.
* Resolución.
* Restricciones posteriores.

Esos elementos pertenecen a la sintaxis del efecto y serán estudiados en temas posteriores.

* * *

### Una última sugerencia de nomenclatura

Creo que acabas de encontrar una convención muy elegante con **a/b**. Incluso le daría una definición general, para que no tengas que explicarla en cada jerarquía:

> **Convención de variantes**
> 
> Cuando una Jerarquía de ejecución presenta variantes, se utilizarán sufijos alfabéticos.
> 
> * **a** → El jugador conserva la decisión sobre la ejecución del efecto (mayor flexibilidad).
> * **b** → El jugador no conserva la decisión; el reglamento determina su ejecución (menor flexibilidad).
> 
> En caso de descubrir nuevas excepciones del reglamento, podrán incorporarse variantes adicionales (**c**, **d**, etc.) sin modificar la jerarquía principal.

Me parece una decisión muy acertada porque conserva intacto el modelo mental: **V2 siempre significa "Quick"**, **V4 siempre significa "Opcional"**, etc. Las letras no redefinen la jerarquía; simplemente añaden precisión cuando una excepción lo exige. Es un diseño extensible y muy propio de un lenguaje técnico.

* * *

**You:**

No. v3, v4 y v5 no tienen variantes, esas siguen intactas. Y  el concepto actual del uso de a y b solo aplica a v2. Si se llegan a usar fuera del v2, el concepto puede cambiar. En v2, a y b funcionan para definir la eleccion, en v3 o v4 probablemente definan una funcion diferente

* * *

**ChatGPT:**

Correcto. Mi propuesta anterior generalizó una convención que todavía **no existe**.

La regla actual debe quedar estrictamente así:

> Los sufijos **a** y **b** no tienen un significado universal.  
> Su significado depende de la jerarquía concreta en la que sean definidos.

Por ahora, únicamente existen dentro de **V2**:

* **V2a**: efecto Quick opcional; el jugador puede elegir activarlo.
* **V2b**: efecto Quick obligatorio; el jugador no puede elegir omitirlo.

Eso no autoriza a interpretar automáticamente:

* `a = opcional`
* `b = obligatorio`

fuera de V2.

En otra jerarquía, las letras podrían representar una diferencia completamente distinta. Son **subtipos locales**, no modificadores globales.

## Glosario corregido

### Jerarquías de ejecución

Las **Jerarquías de ejecución (V)** describen el permiso reglamentario y el nivel de autoridad con el que un efecto puede incorporarse a la construcción de una cadena.

No representan rapidez física ni el tiempo de reacción del jugador.

Se enumeran de mayor a menor autoridad, siendo **V1** la jerarquía máxima actualmente definida.

* * *

### **V1 — Counter**

> **Puede responder incluso a otra respuesta.**

Máxima jerarquía de ejecución conocida.

Permite responder a efectos de jerarquía inferior, incluidos los efectos Quick.

Ejemplo principal: **Counter Traps**.

* * *

### **V2 — Quick**

> **Puede responder a una interacción.**

Permite incorporar un efecto como respuesta durante una ventana válida de interacción.

Incluye efectos Quick, Trampas Normales y otros efectos con autoridad equivalente.

#### Subtipos actuales de V2

* **V2a — Quick opcional**
    
    > Puede responder a una interacción.
    
    El jugador decide si activa el efecto cuando se cumplen sus requisitos.
* **V2b — Quick obligatorio**
    
    > Debe responder a una interacción.
    
    El efecto conserva la jerarquía Quick, pero su ejecución no depende de la elección del jugador.

Los sufijos `a` y `b` describen únicamente esta diferencia dentro de **V2**.

* * *

### **V3 — Obligatorio**

> **Si ocurre el evento, debe ejecutarse.**

Cuando sucede el evento correspondiente, el efecto debe incorporarse a la siguiente cadena válida.

El jugador no decide si activarlo.

* * *

### **V4 — Opcional**

> **Si ocurre el evento, puede ejecutarse.**

Cuando sucede el evento correspondiente, el jugador obtiene permiso para activar el efecto, pero puede decidir no hacerlo.

* * *

### **V5 — Manual**

> **Se ejecuta cuando el jugador lo decide.**

El efecto no espera un evento disparador. El jugador lo activa voluntariamente durante una ventana legal.

* * *

### Convención de subtipos

Una letra añadida a una jerarquía indica una subdivisión interna:

```
V<número><letra>
```

Pero la letra **no posee significado por sí misma**.

Su definición debe consultarse dentro de esa jerarquía:

```
V2a ≠ significado universal de “a”
V2b ≠ significado universal de “b”
```

Por ahora:

```
V2a = Quick opcional
V2b = Quick obligatorio
```

V3, V4 y V5 permanecen intactas y sin variantes. Esto conserva el sistema ya consolidado y permite ampliarlo sin convertir cada letra en una maldición hereditaria del reglamento.

* * *

**You:**

Brillante  ahora pasemos a la siguiente parte del glosario: La sintaxis de requisitos y consecuencias. Esta es como la segunda puerta que debemos abrir para realizar la ejecucion. Luce asi:
-(costo: accion nominal que se debe hacer ANTES de ejecutar el efecto. Esto es a fondo perdido)
-[condicion: accion pasada o presente que se debe cumplir para permitir la ejecucion del efecto]
-{obligacion: accion que debe realizarse DESPUES de la resolucion satisfactoria del efecto]
-<restriccion: modificacion alternativa posterior del comportamiento del juego actual>
A simple vista, parece simple, solido, practico y coherente. Pero va la pregunta del profesor: imagina este efecto:
When this card is summoned, target 1 face-up monster your opponent controls: change it to face-down in defense position. Then, discard 3 cards from the top or your deck.
Si te fijas, la accion de descartar podria caer en una {obligacion}, pero dile eso a un deck lightsworn y preguntale si eso esta mal. Claramente dijimos que el efecto nucleo de la primitiva debe ser el resultado final de cumplir con la jerarquia, y en este caso con los requisitos adicionales y posteriores consecuencias. Pero dichos requisitos o consecuencias por lo general son la parte negativa del efecto, lo que debes ofrecer para permitirlo. Y en este caso, el objetivo es ilustrar que las primitivas no son para enfocarse solo en el efecto nucleo, sino para descubrir que un requisito no siempre es un impacto negativo, tambien puede ser una ventaja sobre otros efectos. Y asi es como llegamos a la sinergia entre efectos. Este es el objetivo principal de la materia Mecanics

* * *

**ChatGPT:**

Creo que acabas de llegar al corazón de _Mechanics_. Y, curiosamente, ya no estamos hablando de Yu-Gi-Oh!, sino de **ingeniería de lenguajes**.

Porque acabas de demostrar que una primitiva no debe responder:

> **"¿Qué costo tiene este efecto?"**

Sino:

> **"¿Qué primitivas produce este efecto?"**

Y eso cambia todo.

* * *

## El problema de la sintaxis actual

Hasta ahora tenemos:

```
(vX): acción principal
(costo)
[condición]
{obligación}
<restricción>
```

Y parece perfecto.

Hasta que aparece tu ejemplo.

```
When this card is summoned,
target 1 face-up monster your opponent controls;
change it to face-down Defense Position.

Then,

discard the top 3 cards of your Deck.
```

Si seguimos la sintaxis al pie de la letra escribiríamos:

```
(v4): Voltea un monstruo boca abajo
    [esta carta fue invocada]
    {manda las 3 cartas superiores del Deck al GY}
```

Y funcionalmente está correcto.

Pero mecánicamente...

**es un desastre.**

* * *

¿Por qué?

Porque asumimos que una obligación siempre es "el precio" del efecto.

Y no.

Para un Lightsworn eso es prácticamente:

> "Roba tres cartas."

* * *

## Acabas de romper una suposición

La sintaxis estaba clasificando los elementos según **cuándo ocurren**.

Pero Mechanics necesita clasificarlos según **qué producen**.

Son dos cosas distintas.

* * *

## Entonces propongo otra interpretación

Tus símbolos no describen si algo es bueno o malo.

Describen únicamente su posición dentro de la ejecución.

Por ejemplo:

```
()
antes
```

```
[]
habilita
```

```
{}
después
```

```
<>
persiste
```

Ninguno dice:

> "Esto es una penalización."

Eso lo interpreta el analista.

* * *

Y aquí aparece algo brillante.

## La sinergia nace precisamente aquí.

No nace en la acción principal.

Nace en las primitivas secundarias.

* * *

Ejemplo.

Deck normal.

```
{envía 3 cartas al GY}
```

Valor:

-1 recurso.

* * *

Lightsworn.

```
{envía 3 cartas al GY}
```

Valor:

+3 activaciones.

+GY.

+targets.

+recursos.

+combo.

La primitiva es idéntica.

Lo que cambia es el entorno.

* * *

## Entonces creo que hay una regla muy importante para la academia

La escribiría así.

* * *

### Regla Fundamental

> **Las primitivas no poseen valor estratégico por sí mismas.**

Representan únicamente acciones del motor del juego.

Será la interacción entre primitivas la que determine si una acción constituye una ventaja, una desventaja o una pieza de un combo.

* * *

Eso me parece elegantísimo.

Porque evita escribir cosas como:

```
(costo negativo)
```

o

```
(obligación positiva)
```

No.

Eso ya no pertenece al lenguaje.

Pertenece al análisis.

* * *

## Y aquí creo que descubrimos el verdadero objetivo de Mechanics

Hasta este momento yo pensaba que las primitivas servían para resumir cartas.

Ahora veo que no.

Sirven para **hacer visible la sinergia**.

Porque una carta deja de ser un párrafo.

Pasa a ser una lista de acciones.

Por ejemplo.

```
(v4): Invoca especialmente

(descarta 1)

{manda 2 cartas al GY}

<solo Dragones>
```

Otro jugador ve una carta.

Mechanics ve cuatro primitivas.

Y otro arquetipo ve:

```
(descarta)
```

como ventaja.

Mientras otro ve:

```
{manda al GY}
```

como ventaja.

Y otro ve:

```
<solo Dragones>
```

como una limitación inaceptable.

* * *

## Creo que podemos formular el principio más importante de toda la materia

Y me atrevería a ponerlo en un recuadro, porque define toda la filosofía de _Mechanics_:

> **Una primitiva no representa el valor de una acción; representa su existencia.**
> 
> El valor estratégico de una primitiva depende exclusivamente del resto del sistema con el que interactúa.

Eso explica por qué la misma acción puede ser una penalización en un deck y el motor de un combo en otro.

Y ahí está, precisamente, la razón de ser de esta materia. No estamos aprendiendo a leer cartas; estamos aprendiendo a **descomponerlas en primitivas independientes** para descubrir cómo unas alimentan a otras. En ese momento deja de existir el concepto de "costo bueno" o "obligación mala". Lo único que existe son acciones elementales del motor del juego, y la sinergia aparece cuando esas acciones encuentran otra carta que las convierte en recursos. Esa, para mí, es la definición más limpia de lo que pretende enseñar _Mechanics_.