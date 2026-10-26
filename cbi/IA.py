import re


class AnalisisSentimiento:
    def __init__(self):
        self.palabras_positivas = [
            "bueno", "buena", "excelente", "maravilloso", "maravillosa",
            "recomendable", "gustó", "gusto", "genial", "fantastico",
            "fantastica", "mejor", "interesante"
        ]
        self.palabras_negativas = [
            "malo", "mala", "horrible", "pésimo", "pesimo", "nada",
            "no", "mal", "feo", "fea", "terrible", "peor", "odioso"
        ]

    def _normalizar_texto(self, texto):
        texto = texto.lower()
        texto = re.sub(r"[^a-zA-Záéíóúüñ\s]", " ", texto)
        return texto.strip()

    def _contar_positivas(self, texto):
        texto_normalizado = self._normalizar_texto(texto)
        palabras = texto_normalizado.split()
        total = 0

        for palabra in self.palabras_positivas:
            total += palabras.count(palabra)

        return total

    def _contar_negativas(self, texto):
        texto_normalizado = self._normalizar_texto(texto)
        palabras = texto_normalizado.split()
        total = 0

        for palabra in self.palabras_negativas:
            total += palabras.count(palabra)

        return total

    def fit(self, palabras_positivas, palabras_negativas):
        for palabra in palabras_positivas:
            if palabra.lower() not in self.palabras_positivas:
                self.palabras_positivas.append(palabra.lower())

        for palabra in palabras_negativas:
            if palabra.lower() not in self.palabras_negativas:
                self.palabras_negativas.append(palabra.lower())

    def predict(self, texto):
        positivas = self._contar_positivas(texto)
        negativas = self._contar_negativas(texto)

        if positivas > negativas:
            return "positiva"
        elif negativas > positivas:
            return "negativa"
        else:
            return "neutral"


if __name__ == "__main__":
    modelo = AnalisisSentimiento()

    opiniones = [
        "Me ha parecido una película muy buena",
        "La música es mala, pero la fotografía es buena",
        "No me ha gustado nada, no la recomiendo",
        "El dobleje es pésimo y la trama es muy mala",
        "Excelente película, 100% recomendable",
        "La banda sonora es maravillosa y la trama me gustó"
    ]

    for opinion in opiniones:
        print(f"{opinion} -> {modelo.predict(opinion)}")

    modelo.fit(["maravilloso", "genial"], ["pesimo", "horrible"])

    print("\nDespués de actualizar el modelo:\n")
    for opinion in opiniones:
        print(f"{opinion} -> {modelo.predict(opinion)}")
