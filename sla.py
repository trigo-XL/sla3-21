def jogo_de_adivinhacao():
  """
  Um jogo simples de adivinhação onde o jogador tem 5 tentativas
  para adivinhar um número secreto.
  """
  numero_secreto = 42
  tentativas_maximas = 5

  print("Bem-vindo ao jogo de adivinhação!")
  print(f"Tente adivinhar o número secreto entre 1 e 100. Você tem {tentativas_maximas} tentativas.")

  for tentativa in range(1, tentativas_maximas + 1):
    try:
      palpite = int(input(f"Tentativa {tentativa}: Digite seu palpite: "))

      if palpite == numero_secreto:
        print("Parabéns! Você acertou!")
        return  # Sai da função e encerra o jogo

      elif palpite > numero_secreto:
        print("O seu palpite foi maior que o número secreto.")
      else:
        print("O seu palpite foi menor que o número secreto.")

    except ValueError:
      print("Entrada inválida. Por favor, digite apenas um número inteiro.")
      
  # Este bloco só é executado se o loop 'for' terminar (todas as tentativas esgotadas)
  print("\nVocê esgotou todas as suas tentativas.")
  print(f"O número secreto era {numero_secreto}.")

# Chama a função para iniciar o jogo
jogo_de_adivinhacao()