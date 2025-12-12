# Ejercicio 23 de la Práctica 4

## Programar en el lenguaje de su elección mediante la API socket un servidor TCP que escuche conexiones en el puerto 9000 y que los datos que reciba los descarte. Correr en el nodo n9 y enviar datos desde otro nodo usando la herramienta nc (netcat) o telnet.

Realizamos el script [Servidor TCP](../../Recursos-TPI/tp4-23/servidor_descartador.py) con la API socket, utilizando python.
y ejecutamos lo siguiente en cada host:

### Host n9
- `python3 <ubicación del script>/servidor_descartador.py` -> ejecuta el script, crea el servidor y comienza a escuchar

### Host n13
- `nc <IP_de_n9> 9000` -> se configura la conexión TCP por defecto hacia el puerto 9000

Prueba de conexión:
![tp4-23-a](image.png)

La conexión se establece, se descartan los datos, y luego se cierra correctamente para continuar esperando.

---

## En el nodo n9 levantar con el super daemon inetd algunos servicios extras, como tcp echo, discard y otros. Chequear los servicios TCP y UDP activos.

### Host n9
Ejecutamos lo siguiente:
- `vim /etc/inetd.conf` -> abrimos el archivo y editamos en modo insert (i):
    - `echo     dgram   udp     wait    root    internal` -> descomentamos, devuelve lo que recibe
    - `discard  stream  tcp     nowait  root    internal` -> descomentamos, descarta lo que recibe
    - `daytime  stream  tcp     nowait  root    internal` -> descomentamos, devuelve fecha y hora en ASCII
    - `time  stream  tcp     nowait  root    internal`

Luego guardamos y salimos -> :wq
    stream: socket orienetado a conexión
    dgram: socket de mensajes

![tp4-23-b-inetd-conf](image-1.png)

Luego ejecutamos:
- `/etc/init.d/openbsd-inetd restart` -> iniciar el servicio
- `netstat -ant` -> verificamos que está escuchando los puertos 7 (echo), 9(discard), 13(daytime) y 37 (time)

![tp4-23-b-netstat](image-2.png)
Está escuchando en los puertos correctamente

---

## Desde el nodo n13 realizar una conexión TCP y enviar datos mediante un programa cliente de su elección al servicio discard, y al echo. Capturar el tráfico con la herramienta tcpdump o wireshark y analizar la cantidad de segmentos, los flags utilizados y las opciones extras que llevan los encabezados tcp.

### Host n13
Utilizando nc para enviar datos:

 #### servicio echo
- `nc 200.5.59.194 7` -> conexión al puerto 7 (servicio echo)
Luego enviamos un mensaje
![echo-n13-n9](image-3.png)
    Vemos que devuelve el mismo mensaje
Por último cerramos la conexión (CTRL+C)

Capturando el tráfico en n9 con Wireshark podemos observar:
![wireshark-n13-n9-echo](image-5.png)
- **Cantidad de segmentos:** se observan 3 segmentos para la apertura de la conexión (112, 113 y 114) donde se produce el three way handshake, 4 segmentos para el envío y recepción de datos bidireccional (echo request 117, 118 y response 119, 120), y 3 segmentos para el cierre de la conexión (123, 124, 125)
- **Flags utilizados:**
    - **SYN**: se utiliza al iniciar la conexión
    - **ACK**: indica la confirmación de recepción de segmentos, aparece en casi todos los segmentos
    - **PSH**: indica que el segmento contiene datos a entregarse, utilizado en el envío y recepción de datos
    - **FIN**: se utiliza al cerrar la conexión, cada extremo envía un FIN
- **Opciones extra:** En los primeros dos segmentos, se observan
    - **Maximum segment size**: indica el maximo tamaño de datos (payload) que se puede recibir en un segmento
    - **SACK permitted**: Selective Acknowledgment, indica que ambas partes lo soportan, permite recuperar pérdidas sin reenviar todos los datos intermedios
    - **Timestamps**: incluye 2 valores: TSval (timestmap del emisor) y TSecr (echo del timestamp recibido)
    - **Window scale**: permite aumentar el tamaño de ventana mas allá del limite de 65.535
    - **NOP**: este aparece en los demás encabezados también, simplemente está de relleno, no hace nada

#### servicio discard
- `nc 200.5.59.194 9` -> conexión al puerto 9 (discard)
![discard-n13-n9](image-4.png)
    Vemos que no devuelve nada (lo descarta)

Capturando el tráfico en n9 con Wireshark podemos observar:
![Wireshark-n13-n9-discard](image-6.png)
- **Cantidad de segmentos:** 3 para el inicio de la conexión (igual que el echo) 3 way handshake, 2 para el envío de datos y el discard (15, 16), ya que el servidor no le vuelve a enviar el mensaje, y solo lo descarta y le envía su ACK, y 3 para el cierre al igual que el echo.
- **Flags utilizados:** Los mismos que el anterior para cada caso.
- **Opciones extra:** Las mismas que el anterior.


## d) Sin cerrar las conexiones chequear los servicios activos y ver los Estados.
e ) Generar nuevas conexiones hacia el nodo n9 e inspeccionar los estados. Por ejemplo realizar varias conexiones simultáneas al servicio tcp echo desde el mismo origen y desde
otros nodos.
f) Intentar generar conexiones a un puerto donde no existe un proceso esperando por recibir datos. ¿Cómo notifica TCP de este hecho (ver flags)?
g ) Cerrar las conexiones y ver el estado de los servicios en ambos lados. ¿En qué estado queda el que hace el cierre activo?
h) Observando la captura indicar la cantidad de segmentos y los flags utilizados. ¿Con cuántos segmentos se cerró la conexión? ¿Existen otras variantes de cierre?
i) Hacer un diagrama de los segmentos intercambiados con los números de secuencia absolutos para una de las sesiones TCP (Se puede usar la herramienta wireshark u otra).
j ) Alternativo: Realizar una conexión mediante nc indicando un puerto específico para el cliente. Luego cerrar la conexión desde el cliente e intentar abrirla nuevamente. ¿En qué estado está el socket? Investigar valor del 2MSL en la plataforma sobre la cual está
haciendo los tests.