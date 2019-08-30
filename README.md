# gemstandard
Ejemplo del formato de los modelos en git para su almacenamiento, versionado y replicación
# Entornos
Anaconda Python ( Preinstalado en la DSVM). Es necesario usar un entorno diferente por cada experimento que se realice.

conda create --name [Nombre de entorno descriptivo]
conda activate [Nombre de entorno]

Cuando el modelo está listo, exportamos el entorno para que sea reproducible:

conda activate [Nombre de entorno]
conda env export > environment.yml
Para generar un entorno a partir del .yml
conda env create --name [Nombre de entorno] -f=environment.yml
# Formato de modelos
Los modelos se guardan en un repositorio de GitHub, con el siguiente formato:

### train.py
Código necesario para entrenamiento del modelo

### model.py
Código que carga el modelo desde un archivo pkl y ejecuta una predicción

### model.pkl
Modelo en formato binario que se puede cargar por el archivo model.py

### validate.py
valida el modelo asegurando que se comporta igual que en desarrollo

### validation.data
Datos de validación que aseguran que el modelo se comporta según lo esperado

### setup.sh
ejecuta los comandos shell necesarios para generar el entorno, activarlo y validar el modelo

### environment.yml
Archivo necesario para recrear el entorno conda original

# setup.sh
conda env create --name [Nombre de entorno] -f=environment.yml
conda activate [Nombre de entorno]
python validate.py

# Cargar modelo
Primero ejecutar:
git clone https://github.com/source_code_repository y entrar al directorio.

a continuación: ./setup.sh (requiere anaconda en la máquina local)
