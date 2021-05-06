 def normalize(s):  # It removes the accents of a string
      replacements = (
           ("á", "a"),
            ("é", "e"),
            ("í", "i"),
            ("ó", "o"),
            ("ú", "u"),
           )
       for a, b in replacements:
            s = s.replace(a, b).replace(a.upper(), b.upper())
        return s

        
sentence = "Mi mamá le compró un balón de fútbol a mi hermano"

new_sentence = sentence.maketrans('áéíóú', 'aeiou')
n_sentence = sentence.translate(new_sentence)
print(n_sentence)
