# Ejercicio 9

## ¿Cuáles de las siguientes no son direcciones IPv6 válidas, cuáles asignables a un host?

1) **Reglas para saber si una IPv6 es válida**

Una dirección IPv6 válida debe cumplir:

- **8 grupos** (hextetos) de 16 bits

    Cada grupo es **hexadecimal**: solo 0–9 y A–F.
    Cada grupo puede tener de **1 a 4 dígitos hex**.

- Puede abreviarse con 

**::** → solo una vez en toda la dirección.

    Ejemplo sin abreviar:

        2001:0db8:0000:0000:0000:0000:0000:1

    Con abreviación:

        2001:db8::1

2) **Errores comunes:**

- Usar caracteres NO hexadecimales → g, h, i…

- Usar :: más de una vez.

- Poner más de 4 hexadecimales por grupo.

- Dar como resultado más de 8 grupos luego de expandir.

3) **¿Cuándo es asignable a un host?**

Una dirección válida no siempre es asignable.

### No asignables a un host:

- :: → dirección no especificada

- ::1 → loopback

- fe80::/10 → link-local

- ff00::/8 → multicast

- Cualquier dirección reservada o con prefijo especial

### Asignables:

- Cualquier dirección global unicast → típicamente 2000::/3

- Direcciones **ULA** → **fc00::/7**
    Las direcciones ULA **(Unique Local Address)** en IPv6 son el equivalente aproximado a las direcciones privadas en IPv4 
    Son direcciones **válidas dentro de una red local**, pero **no se enrutan en Internet**.

    ✔ Prefijo fijo: fc00::/7
    Esto cubre:

        fc00::/8
        fd00::/8

    En la práctica, se usan únicamente las de **fd00::/8**, 
    porque especifican un **bloque generado aleatoriamente para evitar colisiones** entre redes locales.

- Cualquier otra válida que no esté en rangos reservados

-------------------
## Entonces.. clasificamos:

### 2001:0:1019:afde::1
- Dirección **válida**.
- Puede ser asignada.

### 2001::1871::4
- Dirección **inválida**.
- Repite " :: " más de una vez para abreviar los ceros consecutivos dentro de la dirección IP.

### 3ffg:8712:0:1:0000:aede:aaaa:1211
- Dirección **inválida**.
- Contiene una " g " lo cual no pertenece al sistema hexadecimal.

### 3::1
- Dirección **válida**.
- Puede ser asignada.

### 3ffe:1080:1212:56ed:75da:43ff:fe90:affe
- Dirección **válida**.
- **No asignable** a un host (**bloque 6Bone 3FFE::/16, retirado en 2006**).

### ::
- Dirección **válida**.
- **No asignable** a un host. Se usa como **dirección no especificada**.

### 2001::
- Dirección **válida**.
- **No asignable** a un host. Es una **dirección de red**.

### 3ffe:1080:1212:56ed:75da:43ff:fe90:affe:1001
- Dirección **inválida**.
- Tiene **9 grupos** de 8 bits, (debería tener **128 bits de dirección**)