# Ejercicio 6

## Dada la red IP 195.200.45.0/24. Se necesitan definir 9 subredes. Indique la máscara utilizada y las nueve subredes. 
## Luego tome una de ellas e indique el rango de direcciones asignables en esa subred, dirección de red y broadcast.

### IP 195.200.45.0/24

**1100 0011.1100 1000.0010 1101**.0000 0000 -> Red **Clase C**. Primeros tres octetos reservado para dirección de red.

Para armar la máscara dejamos los primeros 3 octetos con unos (1), para no modificar la dirección de red. Posterior al último bit utilizado para la dirección de red, colocamos tantos unos (1) como sea necesario para representar las 9 subredes que necesitamos.

Se necesitan 4 bits para 9 subredes, **$2^{4}$ = 16**.

1111 1111.1111 1111.1111 1111.|**1111**| 0000 -> **Máscara** utilizada para identificar la red subneteada.

255.255.255.240 -> en decimal.

**195.200.45.0/28** -> Podemos escribir su equivalente en notación CIDR, **le sumamos 4 bits al prefijo original (/24)** 
---

### Definir 9 subredes
En este caso tomaremos las 9 subredes a partir de la primera dirección de subred, pero **podemos elegir la cualquiera de las 16** subredes disponibles dentro del rango comprendido.

Primero debemos identificar el **salto de red**, es decir, cuántos incrementos ocurren entre cada subred. Para esto nos **colocamos en los 4 bits** asignados para subredes y **sumamos uno (1)**.

195.200.45.0/28 -> **Primera dirección de subred**. 

1100 0011.1100 1000.0010 1101.0000 0000 /28 -> o en *Binario*

1100 0011.1100 1000.0010 1101.|**0001**| 0000 -> **Segunda dirección** asignable para subredes.

**Pasamos a decimal** para *visualizar mas fácilmente el salto*:

195.200.45.|**16**|/28 -> **El salto de red será de 16**.

**Primeras 9 subredes elegidas:**

- 195.200.45.0/28
- 195.200.45.16/28
- 195.200.45.32/28
- 195.200.45.48/28
- 195.200.45.64/28
- 195.200.45.80/28
- 195.200.45.95/28
- 195.200.45.112/28
- 195.200.45.128/28

---

### Subred 195.200.45.0/28

Se elige esta subred por simplicidad, es la *primera asignable*
La **dirección de red** será la que elegimos: **195.200.45.0/28**

#### Dirección de broadcast

1100 0011.1100 1000.0010 1101.0000 |**1111**|

1100 0011.1100 1000.0010 1101.0000 1111 /28 -> **Dirección de broadcast de la subred**.

195.200.45.15/28 -> **en decimal**.

---

#### Direcciones asignables

195.200.45.0/28 -> **Dirección de red**, *identifica la red*, no es posible asignarla a un host.

195.200.45.**1**/28 -> **Primera dirección de red asignable para host**.

1100 0011.1100 1000.0010 1101.0000 0000 -> en binario

1100 0011.1100 1000.0010 1101.0000 |**0001**|


195.200.45.15/28 -> Dirección de **broadcast**.

195.200.45.14/28 -> **Última dirección de red asignable para host**.


1100 0011.1100 1000.0010 1101.0000 1111 -> en binario.

1100 0011.1100 1000.0010 1101.0000 |**1110**|

**Finalmente:**

**Rango de direcciones asignables** -> 195.200.45.1 - 195.200.45.14, con 14 direcciones asignables para HOSTs