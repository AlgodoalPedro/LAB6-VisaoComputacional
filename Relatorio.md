# Relatório de Processamento de Imagens

## Alunos
Guilherme Couto Gomes RA 22122035-3
Pedro H. Algodoal Pinto RA 22122072-6
Samir Oliveira da Costa RA 22122030-4

---

## Etapas do Processo

Cada imagem passa pelas seguintes etapas:

1. Leitura e conversão para RGB e escala de cinza
2. Aplicação de binarização, com limiar fixo ou proporcional à intensidade máxima da imagem
3. (Opcional) Operações morfológicas: fechamento, dilatação e abertura para redução de ruídos e união de regiões
4. Desfoque (blur) para suavização
5. Detecção de bordas com o algoritmo de Canny (na imagem original e borrada)
6. Extração de contornos
7. Filtro opcional por área dos contornos
8. Desenho dos contornos sobre a imagem original
9. Exibição e salvamento das imagens intermediárias e finais

---

## GIRAFA.jpeg

**Parâmetros utilizados:**

- limiar_binarizacao: 10% da intensidade máxima
- tamanho_kernel: 5  
- canny_threshold1 e canny_threshold2: 0.5  
- Sem filtro de área  
- Morfologia: desativada

**Resultados:**

A imagem foi processada sem uso de morfologia, e todos os contornos encontrados foram desenhados. O resultado mostra objetos em destaque com contornos sobre a imagem original.

**Imagens:**

![passoapasso_girafa](https://github.com/user-attachments/assets/9ba97cb8-a820-4ba7-8720-e18b26e73f26)

![final_girafa](https://github.com/user-attachments/assets/2263b0a8-90c4-4809-9c9a-d17426ee02e8)


---

## AVIAO.jpeg

**Parâmetros utilizados:**

- limiar_binarizacao: 40% da intensidade máxima
- tamanho_kernel: 5  
- canny_threshold1 e canny_threshold2: 0.5  
- Filtro de área: entre 5.000 e 100.000  
- Morfologia: ativada

**Resultados:**

A aplicação das operações morfológicas melhorou a segmentação da imagem. Apenas os contornos com área dentro do intervalo definido foram mantidos e desenhados.

**Imagens:**

![passoapasso_aviao](https://github.com/user-attachments/assets/b3342991-7df8-4160-8725-95779b8a6df3)

![final_aviao](https://github.com/user-attachments/assets/a925f181-c0e2-4c05-86c5-cc159aa86da3)


---

## SATELITE.jpeg

**Parâmetros utilizados:**

- limiar_binarizacao: função baseada na intensidade máxima (`(a * 50) * 0.3`)  
- tamanho_kernel: 5  
- canny_threshold1 e canny_threshold2: 0.5  
- Filtro de área: entre 500 e 20.000  
- Morfologia: desativada

**Resultados:**

A limiarização foi personalizada por uma função que ajusta o limiar dinamicamente. Foram removidos contornos pequenos, deixando apenas os objetos mais relevantes.

**Imagens:**

![passoapasso_satelite](https://github.com/user-attachments/assets/0592d0f8-a441-4bfd-85af-59604c9d586c)

![final_satelite](https://github.com/user-attachments/assets/e4a555ee-558a-4f87-8f42-f78e490e7f08)


---
