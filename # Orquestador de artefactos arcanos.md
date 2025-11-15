# Orquestador de artefactos arcanos

Implementar una mini-plataforma modular para gestionar “artefactos arcanos” en un museo secreto. La aplicación debe permitir definir artefactos, cargarlos dinámicamente y ejecutar rituales sobre ellos, garantizando trazabilidad y reglas de seguridad. Todo debe escribirse en Python.

## Requisitos funcionales

1. **Artefactos registrados automáticamente**
   - Cada artefacto concreto debe registrarse en un catálogo global inmediatamente al definirse.
   - El catálogo mantiene metadatos del artefacto (nombre, nivel de riesgo, etiquetas).
   - No se aceptan clases duplicadas ni artefactos sin metadatos obligatorios.

2. **Rituales encadenados**
   - Un ritual es una secuencia de “pasos” que operan sobre un artefacto.
   - Cada paso puede mutar el estado del artefacto o generar eventos.
   - Se deben soportar pasos síncronos y pasos que devuelvan un generador/iterador (p. ej. inspecciones paso a paso).

3. **Contexto de seguridad**
   - Antes de ejecutar un ritual, debe abrirse un contexto que valide permisos.
   - El contexto debe registrar los pasos ejecutados, tiempos y cualquier incidente.
   - Si ocurre un error, el contexto debe revertir las mutaciones aplicadas durante el ritual.

4. **Motor modular**
   - Los rituales se construyen a partir de mezclas (“mixins”) que aportan capacidades (ej: Iluminación, Contención, Limpieza).
   - Los mixins no pueden ejecutarse sin que el artefacto declare compatibilidad explícita.
   - Se debe poder extender el motor creando nuevos mixins sin tocar el núcleo.

5. **Sistema de auditoría**
   - Toda interacción relevante debe generar eventos que se envían a un bus de auditoría.
   - El bus debe permitir suscripción dinámica y procesar eventos en diferido, respetando el orden de emisión.
   - Los eventos deben ser inmutables y llevar estampillas de tiempo coherentes.

## Requisitos técnicos obligatorios
- Uso de **metaclases** para el registro automático de artefactos.
- Empleo de **descriptores** para validar los metadatos de los artefactos (nombre, riesgo, etiquetas).
- Implementación de **mixins** y **herencia múltiple controlada** para construir rituales.
- Uso de **ABC/Protocol/typing** para definir contratos formales.
- Implementación de al menos un **context manager** para el contexto de seguridad.
- Uso de **generadores** o **iteradores personalizados** en algunos pasos del ritual.
- Registro de eventos basado en estructuras inmutables (por ejemplo `dataclasses` con `frozen=True`).
- Manejo de errores personalizado con excepciones propias.

## Restricciones y aclaraciones
- El objetivo NO es crear una librería real, sino demostrar manejo experto de OOP en Python.
- Debes separar claramente el núcleo del motor, los mixins y los ejemplos de artefactos.
- La solución debe incluir pruebas mínimas (aunque sean auto-contenidas) que demuestren el flujo completo.
- Se valoran comentarios y docstrings que expliquen decisiones de diseño sin perder el toque humorístico.

## Entregables
1. `motor.py`: contiene la solución completa (puedes subdividir internamente en clases, funciones, excepciones, etc.).
2. Pruebas al final del archivo (`if __name__ == "__main__":`) o en una sección dedicada.
3. No se aceptan dependencias externas: usa solo la librería estándar.

**¡Que los artefactos sobrevivan a tus rituales!**