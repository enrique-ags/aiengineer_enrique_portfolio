# Análisis de Sentimientos - Sentiment Analysis

Este proyecto utiliza un modelo de inteligencia artificial pre-entrenado para analizar el sentimiento de textos en español.

## Requisitos

- Python 3.11
- Conda (recomendado para gestionar el entorno)

## Instalación de Dependencias

### Paso 1: Crear el entorno conda

```bash
conda create -n sentiment_nlp python=3.11
conda activate sentiment_nlp
```

### Paso 2: Instalar las dependencias

En **macOS**, ejecuta:

```bash
conda install -n sentiment_nlp pytorch::pytorch -y
pip install 'transformers<4.41'
pip install huggingface_hub
pip install 'numpy<2'
```

En **Linux/Windows**, ejecuta:

```bash
pip install torch
pip install transformers<4.41
pip install huggingface_hub
pip install 'numpy<2'
```

## Uso

Asegúrate de que el entorno conda esté activado:

```bash
conda activate sentiment_nlp
```

Luego ejecuta el script:

```bash
python sentiment_analysis.py
```

## Dependencias Principales

| Paquete | Versión | Descripción |
|---------|---------|-------------|
| **transformers** | <4.41 | Librería para modelos de NLP pre-entrenados |
| **torch** | 2.2.2+ | Framework de aprendizaje profundo |
| **huggingface_hub** | - | Herramientas para descargar modelos de Hugging Face |
| **numpy** | <2 | Librería para computación numérica |

## Notas Importantes

- Se requiere la versión de `transformers` < 4.41 para compatibilidad con PyTorch 2.2.2
- `numpy` debe ser versión 1.x (< 2) para evitar incompatibilidades
- En macOS, se recomienda instalar PyTorch desde conda en lugar de pip
- El modelo `nlptown/bert-base-multilingual-uncased-sentiment` se descargará automáticamente la primera vez

## Solución de Problemas

### Error: "PyTorch was not found"

Si ves este error, asegúrate de que PyTorch está instalado:

```bash
conda activate sentiment_nlp
python -c "import torch; print(torch.__version__)"
```

### Error de versión de NumPy

Si tienes problemas con NumPy 2.x, downgrade a versión 1.x:

```bash
pip install 'numpy<2' --upgrade
```
