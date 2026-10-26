# Prompt para continuar a correção do KA-200-B200-POH_corrigido.md em outra sessão

Cole o texto abaixo (a partir de "Contexto") como primeira mensagem da nova sessão.

---

## Contexto

Estou revisando a conversão automática (OCR/Docling) de um manual de voo escaneado para Markdown. Repositório `JoaoPagotto/kingair_b200`, branch atual `arena/995a83f5-kingair-b200` (em sessões anteriores foi usada a branch `claude/relaxed-thompson-9yr78s`, PR https://github.com/JoaoPagotto/kingair_b200/pull/1; não crie outro PR nem mude de branch — apenas commit e push na branch atual).

Arquivos em `docs/`:
- `KA-200-B200-POH.pdf` — manual original (1309 páginas), **escaneado**: o texto embutido é só uma camada de OCR e **não** serve de referência.
- `KA-200-B200-POH_completo.md` — conversão automática, com muitos erros (tabelas vazias, palavras trocadas, frases cortadas, tabelas só como imagem).
- `KA-200-B200-POH_corrigido.md` — meu arquivo de trabalho: cópia do `_completo.md` em que substituo, lote a lote, o trecho de cada página pela retranscrição feita a partir da imagem da página.
- `KA-200-B200-POH_controle.md` — **leia primeiro**: cobertura por lote, divergências do original mantidas como impressas, itens para conferência humana e convenções.
- `KA-200-B200-POH_imagens/` — imagens recortadas pelo conversor (`pNNNNN_MM.png`, NNNNN = página do PDF).
- `KA-200-B200-PTM_*` — outro manual, já tratado; ignore.

## Tarefa

Continuar a retranscrição do `KA-200-B200-POH_corrigido.md`, **em lotes de 10 páginas do PDF**, parando ao fim de cada lote para eu confirmar. (Os lotes 1 a 10 e o lote 11 foram feitos com 25 páginas por lote, quando o volume ainda era suportável; a partir daqui o lote é de 10 páginas.) Estado atual (ver `_controle.md` para o detalhe):
- **Feito:** págs. 37–361 do PDF (Seções 2 a 7 completas; Seção 8 completa até a p. 8-16; Seção 9 começa na p. 9-1).
- **Próximo:** lote 17 = págs. **362–371** (continuação da Seção 9 Suplementos: LOG OF SUPPLEMENTS e os suplementos), sempre em lotes de 10 páginas até 1309 (restante da Seção 9, Seção 10 Segurança).
- **Por último:** págs. 1–36 (capa, listas de páginas, logs de revisão, introdução, Seção 1). Uma tentativa anterior foi descartada; nada gravado.

## Método (siga igual aos lotes anteriores)

1. Renderize as páginas do lote: `pdftoppm -r 120 -f A -l B -gray -png docs/KA-200-B200-POH.pdf <dir>/k` para texto corrido; **`-r 200`** para páginas com tabelas numéricas. Use como diretório de trabalho o scratchpad da sessão. Leia as imagens com a ferramenta Read.
2. Retranscreva **a partir da imagem**, nunca do OCR do `.md` nem do texto do PDF. Preserve: numeração dos passos, negrito dos itens de ação imediata, `+` e `*` de notas, avisos (WARNING/CAUTION/NOTE) e notas de rodapé.
3. Tabelas em Markdown (cabeçalho completo, uma linha por linha do original). Células vazias sem dados no original ("---") podem ser omitidas, com uma frase avisando abaixo da tabela. Em índices (TOC) com recuos hierárquicos, preserve o nível com `&nbsp;` (2 por nível), como feito no lote 15. Páginas giradas em 90°: recorte e gire a faixa de texto (PIL) antes de ler.
4. Figuras, desenhos e curvas de gráfico **não** são transcritos: mantenha a imagem do `.md` original (`![Image](KA-200-B200-POH_imagens/pNNNNN_MM.png)`) logo abaixo do texto da página e transcreva só título, condições, notas, exemplos e tabelas pequenas. Painéis e diagramas: descreva em uma frase.
5. Páginas "THIS PAGE INTENTIONALLY LEFT BLANK": uma linha em itálico com o número da página do manual, para preservar a numeração.
6. **Nunca corrija, estime ou interpole um número.** Se um valor impresso parece erro do próprio manual (fora da tendência, total ≠ 2 × por motor, título errado), transcreva exatamente como impresso, escreva "Nota do transcritor" abaixo da tabela e registre em `_controle.md`. Se estiver em dúvida entre dois dígitos, releia em resolução maior e, persistindo, **pare e pergunte**.
7. Valide cada tabela numérica com script (nº de colunas por linha, totais, tendências) antes de gravar.
8. Para substituir um trecho do `_corrigido.md`, localize pelo nome da imagem: no `.md` original, o texto de uma página aparece **depois** das tags de imagem dessa página, e páginas só de texto não têm imagem (o texto vem depois da última imagem da página anterior). Confira os limites (primeira e última linha substituída) antes de gravar.
9. Ao fim de cada lote: atualize `_controle.md` (tabela de cobertura, divergências, itens de conferência), faça `git add` dos dois arquivos, commit com mensagem `POH: batch N (Section X ...; PDF pp. A-B) ...` e `git push origin arena/995a83f5-kingair-b200`. Depois responda com: o que entrou, divergências impressas, o que eu devo conferir e o que falta.

## Regras

- Qualquer coisa anormal (valor que não bate, página ilegível, trecho que não sei se é figura ou texto, divergência entre versões B200/B200C): **pare e peça decisão** antes de seguir.
- Salve o trabalho no repositório a cada lote; arquivos temporários do scratchpad se perdem se a sessão acabar.
- Não use `rm` com variável de shell (`rm $S/...`); o sistema bloqueia. Use caminho literal ou nem apague.
- Responda em português.
- Não crie PR nem mude de branch.

## Primeira ação

Leia `docs/KA-200-B200-POH_controle.md`, confirme em uma frase onde estamos e comece o lote 17 (págs. 362–371).
