# Dependencias del Pipeline

El pipeline tiene las siguientes dependencias entre etapas:

- Validación: requiere esquema definido y archivos presentes
- Procesamiento: depende de validación exitosa
- Enriquecimiento: depende de procesamiento exitoso
- Validación de calidad: depende de enriquecimiento exitoso
- Reporte: depende de validación de calidad exitosa

Si una etapa falla, el pipeline se detiene
