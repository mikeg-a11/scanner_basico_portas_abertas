# scanner_basico_portas_abertas
Scanner básico feito em python com o objetivo de compreender como funciona o escaneamento de portas abertas

## Parâmetros
- A variável tamanho_percorrido_por_loop determinará quantos sockets serão criadas ao mesmo tempo. 
- O valor padrão da variável é de 100 para garantir que não ocorra erro de criação excessiva de sockets.

- O ultimo parâmetro de select.select deve ser alterado conforme o tempo de resposta de sua rede
- Quanto mais lento for o tempo de resposta da rede, maior deve ser o timeout, quanto mais rápido o tempo de resposta da rede, menor o timeout.