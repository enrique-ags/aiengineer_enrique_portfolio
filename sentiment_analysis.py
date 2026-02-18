
#conda create -n sentiment_nlp python=3.11
#conda activate sentiment_nlp
#despues de crear el entorno, instalar las dependencias necesarias para ejecutar el código
#Instalar estas dependencias antes de ejecutar el código
#pip install transformers torch huggingface_hub
#para mac usar conda install -n sentiment_nlp pytorch::pytorch -y
'''
Documentacion de este ejemplo
La escala de estrellas (label):

1 star = muy negativo
2 stars = negativo
3 stars = neutral
4 stars = positivo
5 stars = muy positivo
La confianza (score):
Es la probabilidad de que esa etiqueta sea correcta. Rango 0-1 (o 0-100%):

0.95 (95%) = el modelo está muy seguro de su predicción
0.60 (60%) = el modelo tiene menos seguridad, texto ambiguo
0.50 (50%) = prácticamente no sabe (podría ir para cualquier lado)
'''


from transformers import pipeline

analizador = pipeline("sentiment-analysis",
                      model="nlptown/bert-base-multilingual-uncased-sentiment")
try:
    # Análisis 1
    resultado1 = analizador("Me encanto el producto, llegó muy rapido")[0]
    print(f"Texto 1: {resultado1['label']} (Confianza: {resultado1['score']:.2%})")

    # Análisis 2
    resultado2 = analizador("Pesimo servicio, nunca regreso a comprar")[0]
    print(f"Texto 2: {resultado2['label']} (Confianza: {resultado2['score']:.2%})")
except OSError:
    print("Error, no se pudo cargar el modelo")

except Exception as e:
    print(f"Error inesperado, {e}")
