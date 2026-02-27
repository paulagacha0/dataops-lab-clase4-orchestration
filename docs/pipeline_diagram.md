# Diagrama del Pipeline

El pipeline de datos está compuesto por los siguientes elementos:

## Fuentes de Datos
- Archivo CSV de ventas (sales_data.csv)
- Archivo CSV de catálogo de productos (product_catalog.csv)

## Procesos
1. Validación de datos
2. Procesamiento (limpieza y transformación)
3. Enriquecimiento con catálogo
4. Validación de calidad
5. Generación de reporte

## Destinos
- Archivo procesado
- Reporte JSON de ejecución

## Controles
- Logging en archivo logs/pipeline_execution.log
- Validación de esquema
- Verificación de calidad antes de generar reporte

Flujo general:

Fuentes → Validación → Procesamiento → Enriquecimiento → Calidad → Reporte
