# Ejercicio 14

## Dado el siguiente gráfico, y según los datos brindados, para cada segmento de red, responda:

![Diagrama Ejercicio 14](../Recursos-practica2/Ejercicio14-Diagrama.png)

## Dirección y Clase (A,B o C) de Red. Dirección y Máscara de Subred. Dirección de Broadcast. Cantidad de direcciones utilizables en cada subred.

---------------------

### Un Segmento de Red
Es un conjunto de dispositivos que comparten el mismo medio de comunicación:

- Cable Ethernet compartido
- Switch
- VLAN
- Enlace punto a punto entre routers

Cuando dos dispositivos están en el **mismo segmento**, pueden comunicarse **sin pasar por un router**.

--------------------

### ¿Qué significan eth0, eth1, eth2?

En redes simuladas o en routers basados en Linux (como los de GNS3, Netlab, Packet Tracer, etc.), 
cada **interfaz de red** se llama así:

eth0 → primera interfaz de red (Ethernet 0)

eth1 → segunda interfaz

eth2 → tercera interfaz

... y así

📌 **Cada interfaz conecta a una red distinta**, y por eso reciben direcciones IP distintas.
------------------------


🧠 **ROUTER vs SWITCH**
| Característica      | Switch                                   | Router                                 |
|---------------------|------------------------------------------|----------------------------------------|
| Función             | Conecta dispositivos en la **misma red** | Conecta **redes diferentes** entre sí      |
| Capa OSI            | Capa 2                                   | Capa 3                                 |
| Dirección usada     | MAC                                      | IP                                     |
| Dominios            | Mantiene **un** dominio de broadcast     | Cada interfaz es un dominio distinto   |
| Toma decisiones por | MAC de destino                           | IP de destino                          |
| Salida a Internet   | ❌ No                                    | ✔ Sí (usa rutas y puede hacer NAT)    |

-----------------------

### 172.16.2.1/27

- Red de Clase B.
- Dirección de Red -> 172.16.0.0/16
- Dirección de Subred -> 172.16.2.0/27
- Máscara de Subred -> 255.255.255.224 ó /27
- Dirección de Broadcast -> 172.16.2.31/27
- Direcciones utilizables en cada subred (**5 bits restantes para hosts**) -> $2^{5}$ - 2 = 30 

---

### 192.168.10.6/30

- Red de Clase C.
- Dirección de Red -> 192.168.10.0/24
- Dirección de Subred -> 192.168.10.4/30
- Máscara de Subred -> 255.255.255.252 ó /30
- Dirección de Broadcast -> 192.168.10.7/30
- Direcciones utilizables en cada subred -> $2^{2}$ - 2 = 2

---

### 10.10.10.43/24

- Red de Clase A.
- Dirección de Red -> 10.0.0.0/8
- Dirección de Subred -> 10.10.10.0/24
- Máscara de Subred -> 255.255.255.0 ó /24
- Dirección de Broadcast -> 10.10.10.255/24
- Direcciones utilizables en cada subred -> $2^{8}$ - 2 = 254

---

### 192.168.10.1/30

- Red de Clase C.
- Dirección de Red -> 192.168.10.0/24 
- Dirección de Subred -> 192.168.10.0/30
- Máscara de Subred -> 255.255.255.252 ó /30
- Dirección de Broadcast -> 192.168.10.3/30
- Direcciones utilizables en cada subred -> $2^{2}$ - 2 = 2

---

### 200.16.5.9/30 (ISP-Internet Service Provider)

- Red de Clase C.
- Dirección de Red -> 200.16.5.0/24
- Dirección de Subred -> 200.16.5.8/30
- Máscara de Subred -> 255.255.255.252 ó /30
- Dirección de Broadcast -> 200.16.5.11/30
- Direcciones utilizables en cada subred -> $2^{2}$ - 2 = 2

---

### 192.168.10.17/30

- Red de Clase C.
- Dirección de Red -> 192.168.10.0/24
- Dirección de Subred -> 192.168.10.16/30
- Máscara de Subred -> 255.255.255.252 ó /30
- Dirección de Broadcast -> 192.168.10.19/30
- Direcciones utilizables en cada subred -> $2^{2}$ - 2 = 2

---

### 192.168.1.69/26

- Red de Clase C.
- Dirección de Red -> 192.168.1.0/24
- Dirección de Subred -> 192.168.1.64/26
- Máscara de Subred -> 255.255.255.192 ó /26
- Dirección de Broadcast -> 192.168.1.127/26
- Direcciones utilizables en cada subred -> $2^{6}$ - 2 = 62

---

## ¿Cuántos DOMINIOS DE COLISIÓN y de BROADCAST encuentra en el gráfico?.

### Dominios de colisión 

| Dispositivo | ¿Cómo maneja los dominios de colisión? | Explicación |
|------------|------------------------------------------|-------------|
| **Hub**    | ❌ **Un solo** dominio de colisión           | Todos los puertos comparten el mismo medio; si dos transmiten, colisionan. |
| **Switch** | ✔ Un dominio de colisión **por puerto**      | Cada puerto es independiente; evita colisiones entre dispositivos. |
| **Router** | ✔ Un dominio de colisión **por interfaz**    | Las interfaces no comparten medio; separan completamente las colisiones. |


Se observan **12 dominios de colisión**

![Dominios de colisión](../Recursos-practica2/Ejercicio14-Dominios-Colision.png)

### Dominios de broadcast

| Dispositivo | ¿Separa dominios de broadcast? | Explicación |
|------------|--------------------------------|-------------|
| **Hub**    | ❌ No                          | Reenvía todo a todos los puertos. |
| **Switch** | ❌ No (**por defecto**)            | Todos los puertos comparten el mismo dominio; solo **se separa con VLANs**. |
| **Router** | ✔ Sí                          | Cada interfaz es un dominio de broadcast independiente. |

Se observan **7 dominios de broadcast**

![Dominios de colisión](../Recursos-practica2/Ejercicio14-Dominios-Broadcast.png)

---

## Asigne una dirección adecuada a cada interfaz de red de los routers.

    🟩 Regla de oro

    Una interfaz de router debe tener una IP válida dentro de la subred a la que está conectada.

    Si una interfaz está conectada a la red 172.16.2.0/27 → debe tener una IP entre 172.16.2.1 y 172.16.2.30
    Si está en la red 10.10.10.0/24 → debe tener una IP entre 10.10.10.1 y 10.10.10.254
    Si está en un enlace /30 → debe tener una de las dos IPs disponibles.

![IP para cada interfaz de router](../Recursos-practica2/Ejercicio14-Asignando-IP.png)

---

## Defina la tabla de ruteo para cada router de manera que todos los dispositivos en la red puedan comunicarse y, además, salir a Internet.

### Router A

| **Red destino** | **Mask**|   **Next Hop**  |**Device**| **Métrica** |
|:--------------: | :-----: | :-------------: | :------: |  :-------:  |
|    `172.16.2.0` |  `/27`  |       `-`       |  `eth0`  |      0      |
| `192.168.10.16` |  `/30`  |       `-`       |  `eth1`  |      0      |
|  `192.168.10.4` |  `/30`  |       `-`       |  `eth2`  |      0      |
|    `10.10.10.0` |  `/24`  |  `192.168.10.5` |  `eth2`  |      1      |
|  `192.168.1.64` |  `/26`  | `192.168.10.17` |  `eth1`  |      1      |
|     `0.0.0.0`   |   `/0`  | `192.168.10.17` |  `eth1`  |      0      |

---

### Router B

| Red destino     | Mask | Next Hop       | Device | Métrica |
|-----------------|------|----------------|--------|---------|
| 192.168.1.64    | /26  | -              | eth0   | 0       |
| 192.168.10.16   | /30  | -              | eth1   | 0       |
| 192.168.10.0    | /30  | -              | eth2   | 0       |
| 200.16.5.8      | /30  | -              | eth3   | 0       |
| 172.16.2.0      | /27  | 192.168.10.18  | eth1   | 1       |
| 10.10.10.0      | /24  | 192.168.10.1   | eth2   | 1       |
| 0.0.0.0         | /0   | 200.16.5.9     | eth3   | 0       |


### Router C

| Red destino     | Mask | Next Hop       | Device | Métrica |
|-----------------|------|----------------|--------|---------|
| 10.10.10.0      | /24  | -              | eth0   | 0       |
| 192.168.10.4    | /30  | -              | eth1   | 0       |
| 192.168.10.0    | /30  | -              | eth2   | 0       |
| 172.16.2.0      | /27  | 192.168.10.6   | eth1   | 1       |
| 192.168.1.64    | /26  | 192.168.10.2   | eth2   | 1       |
| 0.0.0.0         | /0   | 192.168.10.2   | eth2   | 0       |


### Router ISP

| Red destino     | Mask | Next Hop       | Device            | Métrica |
|-----------------|------|----------------|-------------------|---------|
| 200.16.5.8      | /30  | -              | eth0              | 0       |
| 192.168.1.64    | /26  | 200.16.5.10    | eth0              | 1       |
| 10.10.10.0      | /24  | 200.16.5.10    | eth0              | 2       |
| 172.16.2.0      | /27  | 200.16.5.10    | eth0              | 2       |
| 0.0.0.0         | /0   | -              | Interfaz Internet | 0       |

