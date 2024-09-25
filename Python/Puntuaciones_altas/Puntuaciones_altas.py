## https://www.codewars.com/kata/5962bbea6878a381ed000036/train/python

class HighScoreTable:
    def __init__(self, limit: int):
        self.limit = limit
        self.scores = []
        
    def update(self, score: int):
         # Asumimos que el score no ha sido insertado aún
        inserted = False

        # Recorre e inserta el score en la posición adecuada
        for i in range(len(self.scores)):
            if score >= self.scores[i]:
                self.scores.insert(i, score)
                inserted = True
                break

         # Si no fue insertado en el bucle, añadirlo al final
        if not inserted:
            self.scores.append(score)
        
        # Limitar la lista al tamaño máximo definido (self.limit)
        self.scores = self.scores[:self.limit]
    
    def reset(self):
        # Reinicia la lista de puntuaciones a vacía
        self.scores = []

# Test Cases
table = HighScoreTable(3)
table.update(10)
table.update(10)
table.update(12)
print(table.scores)