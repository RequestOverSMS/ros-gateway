# ROS-GATEWAY

Proyecto desarrollado para el hackit-ba 2022 por Maximiliano Zitelli, Tobias Lifschitz y Santiago Ivulich.

## Resumen

Este gateway permite la interacción por SMS utilizando el protocólo ROS para habilitar 
consultas HTTP a través de SMS.


## Arquitectura
Nuestro SDK se integra directamente con la app de los clientes y deriva las
consultas por el medio adecuado. 

En el caso de tener internet las consultas son enviadas por HTTP 
tradicional al servidor del cliente.

En el caso de no poseer internet las consultas son transmitidas por el protocolo
ROS a nuestros servidores y luego enviadas al servidor del cliente.

![image](documentation/Arquitectura.jpg)

## Protocolo ROS
El protocolo ROS permite serializar los datos y transmitirlos por mensaje
siguiendo los siguientes pasos:

 1) Se compila el JSON a protobuf.
 2) Se comprime el binario del protobuf.
 3) Se encriptan los datos comprimidos.
 4) Se codifican en base64.
 5) Se envían los datos por SMS.

Para de-codificar el protooclo:

 1) Se recibe el SMS.
 2) Se convierte base64 a binario.
 3) Se desencriptan los datos.
 4) Se descomprimen los datos.
 5) Se convierte el protobuf a JSON.

Los datos enviados al servidor son interpretados para generar una consulta
al servidor de destino.

![image](documentation/Datos.jpg)

## Features
Los features del gateway son:
 
 - D - Recibir SMS 
 - D - Interpretación de protocolo ROS
 - D - Realizar consultas en el servidor del cliente
 - N - Response por SMS

Referencia:
 - D: Implementado
 - N: No Implementado 

## Validacion

Se utilizó el servicio de SMS Twilio para validar el funcionamiento del servicio.

Para ello se envió un request por SMS para realizar una consulta a la API de 
Coindesk que devuelve el precio del BTC en 
USD, EUR y GBP.


![image](documentation/EntradaSalida.png)

Los resultados incluyen los watermarks de la cuenta trial de Twilio.

## Futuras mejoras

Se plantean como futuras mejoras:
 - Separación en tareas asincrónicas para implementar pipeline de procesamiento resiliente y eficiente.
 - Manejo de usuarios con permisos para distintas APIs.
 - Manejo de errores y autodetección de formato.


