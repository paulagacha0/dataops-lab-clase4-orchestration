# Reflexión Final

## 1. Diseño de Pipelines
Dividí el pipeline en componentes (validación, procesamiento, enriquecimiento, calidad y reporte) porque así es más fácil entender qué hace cada paso y detectar errores, definí las dependencias pensando en el orden lógico: primero validar, luego procesar, después enriquecer y al final revisar calidad antes de generar el reporte

## 2. Orquestación vs Ejecución
Ejecutar componentes es correr cada script por separado, orquestar es tener un flujo que los ejecuta en el orden correcto, controlando que un paso solo se ejecute si el anterior salió bien.

## 3. Manejo de Fallos
- Reintentos automáticos: intentaría correr de nuevo un paso si falla por algo temporal
- Continuación desde el punto de fallo: guardaría resultados intermedios para no empezar desde cero
- Notificaciones escalonadas: primero dejaría el error en logs y, si se repite, enviaría una alerta

## 4. Monitoreo
Monitorearía: si el pipeline termina o falla, cuánto se demora, cuántos registros procesa, y si genera el reporte de salida

## 5. Costos
Para optimizar costos, primero lo correría local o en un entorno pequeño. Si el volumen crece, lo movería a la nube y lo ejecutaría solo cuando sea necesario, evitando correr más veces de las requeridas
