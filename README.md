1. En app.py, hicimos que cuando un filtro estuviera vacío se mostraran todos los datos, porque así era más fácil quitar un filtro. Sin embargo, en la versión de referencia, si se quitan todas las opciones, aparece un aviso y se detiene la ejecución. Consideramos que debemos cambiar esta parte porque era un requisito de la actividad que nos faltó implementar.

2. En loaders.py, nos enfocamos en corregir los formatos y eliminar filas con datos importantes inválidos. Dejamos el ingreso como venía en el CSV, sin recalcularlo. La versión de referencia también elimina duplicados y unidades negativas, y calcula nuevamente el ingreso. Pero al revisar nuestros datos, vimos que no había duplicados ni unidades negativas y que los ingresos ya estaban calculados correctamente, por lo que no hubo diferencias en los resultados.

3. En charts.py, ambas versiones muestran las mismas gráficas, por lo que consideramos que nuestra implementación está bien y la dejaríamos como está.
