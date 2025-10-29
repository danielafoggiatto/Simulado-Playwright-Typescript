Gerador de Simulado Playwright + TypeScript

Este script gera automaticamente um simulado de perguntas objetivas sobre Playwright e TypeScript em formato HTML interativo, com respostas ocultas que podem ser exibidas ao clicar em um botão.

Conteúdo

gerar_simulado_playwright.py → Script Python que cria o HTML.

simulado_playwright.html → Arquivo HTML gerado com todas as perguntas e respostas.

Requisitos

Python 3.x

Nenhuma biblioteca externa necessária (usa apenas biblioteca padrão)

Como usar

Abra o terminal na pasta onde está o arquivo gerar_simulado_playwright.py.

Execute o script Python:

python gerar_simulado_playwright.py


Se estiver usando Python 3 especificamente, em alguns sistemas pode ser necessário:

python3 gerar_simulado_playwright.py


O script irá gerar um arquivo HTML:

simulado_playwright.html


Abra o HTML no navegador:

Windows: clique duas vezes no arquivo ou use start simulado_playwright.html no terminal.

Mac: open simulado_playwright.html

Linux: xdg-open simulado_playwright.html

Como funciona

Cada pergunta aparece com um botão “Verificar resposta”.

Ao clicar no botão, a resposta correspondente será exibida.

Perguntas podem ser facilmente editadas ou adicionadas diretamente na lista perguntas do script.

Personalizações possíveis

Alterar cores de borda, botões e fontes diretamente no <style> do HTML.

Adicionar novas perguntas ao final da lista perguntas.

Ajustar timeout ou efeitos de exibição, se necessário.
