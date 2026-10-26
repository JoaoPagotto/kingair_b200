# Controle da correção — KA-200-B200-POH_corrigido.md

Arquivo de acompanhamento da retranscrição do `KA-200-B200-POH_completo.md` (conversão automática do PDF escaneado, com OCR) para o `KA-200-B200-POH_corrigido.md`.

- **Fonte de verdade:** as imagens das páginas de `KA-200-B200-POH.pdf` (1309 páginas). O PDF é escaneado; o texto embutido é uma camada de OCR e **não** serve de referência.
- **Método:** cada página é renderizada (100–200 dpi) e retranscrita para Markdown, em lotes de 25 páginas (lotes 1–10) e, a partir do lote 11, de 10 páginas, com confirmação do usuário a cada lote. Tabelas numéricas são lidas a 200 dpi.
- **Numeração:** "pág. PDF" é a página do arquivo PDF; "pág. manual" é a numeração impressa (ex.: 5-50).
- **Pull request:** [JoaoPagotto/kingair_b200#1](https://github.com/JoaoPagotto/kingair_b200/pull/1), branch de trabalho atual `claude/festive-pascal-0x6h5q` (a anterior, `claude/relaxed-thompson-9yr78s`, já mergeada).

> Ao concluir cada lote, atualizar a tabela da seção 1, a seção 2 (divergências) e a seção 3 (conferências pendentes).

## 1. Cobertura por lote

Estados: **feito** (transcrito e enviado), **em andamento** (parte já escrita, não enviada), **pendente**.

| Lote | Págs. PDF | Págs. manual | Seção | Estado | Commit |
|---|---|---|---|---|---|
| — | 1–36 | capa, listas de páginas, logs de revisão, introdução, Seção 1 (Geral) | abertura e Seção 1 | **pendente** (uma tentativa no início foi descartada; nada gravado) | — |
| 1 | 37–61 | 2-1 a 2-19 | 2 Limitações | feito | `8121352` |
| 2 | 62–86 | 2-20 a 3A-6 | 2 (fim), 3 Emergência, 3A (início) | feito | `fb61ef9` |
| 3 | 87–111 | 3A-7 a 4-19 | 3A (fim), 4 Procedimentos Normais (início) | feito | `8d5b117` |
| 4 | 112–136 | 4-20 a 5-12 | 4 (fim), 5 Desempenho (introdução e exemplos) | feito | `aa15539` |
| 5 | 137–161 | 5-13 a 5-37 | 5 Desempenho (gráficos) | feito | `39fc81d` |
| 6 | 162–186 | 5-38 a 5-62 | 5 Desempenho (tabelas de cruzeiro) | feito | `c060260` |
| 7 | 187–211 | 5-63 a 5-87 | 5 Desempenho (tabelas de cruzeiro) | feito | `d5de67d` |
| 8 | 212–236 | 5-88 a 5-112 | 5 Desempenho (alcance, 1 motor) | feito | `495f2d6` |
| 9 | 237–261 | 5-113 a 6-13 | 5 (fim), 6 Peso e Balanceamento (início) | feito | `56c7a6a` |
| 10 | 262–286 | 6-14 a 6-38 | 6 Peso e Balanceamento (B200 e B200C) | feito | `92ce9f4` |
| 11 | 287–296 | 7-1 a 7-10 | 7 Descrição dos Sistemas (índice, estrutura, comandos de voo, painel e anunciadores) | feito | (ver commit do lote 11) |
| 12 em diante | 297–1309 (10 em 10) | 7-11 ao fim | 7 (restante), 8 Manutenção e Serviço, 9 Suplementos, 10 Segurança | **pendente** | — |

**Resumo:** págs. 37–286 do PDF feitas (250 de 1309, ≈19%); págs. 37–296 feitas (260 de 1309, ≈20%); págs. 1–36 e 297–1309 pendentes.

### Pontos de atenção sobre o que falta
- **Págs. 1–36:** o `.md` original tem erros de OCR em quase todo parágrafo e tabelas vazias (Lista de Páginas Efetivas, Logs de Revisão, índices).
- **Seção 9 (Suplementos):** é a mais longa do PDF (grande parte das páginas restantes); cada suplemento tem suas próprias seções de limitações, emergência, normal e desempenho.
- **Seção 8:** contém tabelas de lubrificantes e lâmpadas; ler a 200 dpi.
- Há seções iniciais fora de ordem no `.md` original (ex.: blocos da Seção 9 repetidos); verificar ao chegar nelas.

## 2. Divergências do original mantidas como impressas

Valores que parecem erro de impressão no próprio manual. Foram **transcritos como estão**, com nota abaixo da tabela. Se houver o AFM atualizado, informar os valores corretos para corrigir.

| Pág. manual | Tabela | Linha / célula | Impresso | Esperado | Estado |
|---|---|---|---|---|---|
| 5-50 | Cruzeiro normal 1700 RPM, ISA +10°C | IAS @10.000 lb em 29.000, 31.000, 33.000 e 35.000 ft | 270, 262, 253, 242 | fora da tendência | confirmado pelo usuário como impresso |
| 5-51 | Cruzeiro normal 1700 RPM, ISA +20°C | 22.000 ft, fluxo total | 616 | 626 | mantido |
| 5-52 | Cruzeiro normal 1700 RPM, ISA +30°C | 33.000 ft, fluxo total | 286 | 386 | mantido |
| 5-60 | Cruzeiro máximo 1700 RPM, ISA -10°C | 29.000 ft, fluxo total | 560 | 520 | mantido |
| 5-70 | Cruzeiro normal 1800 RPM, ISA -30°C | SL, fluxo total | 976 | 966 | mantido |
| 5-82 | Cruzeiro máximo 1800 RPM, ISA -30°C | 8.000 ft, fluxo total | 884 | 874 | mantido |
| 5-87 | Cruzeiro máximo 1800 RPM | subtítulo | "IAS + 20°C" | "ISA + 20°C" | mantido |
| 5-89 | Cruzeiro máximo 1800 RPM, ISA +37°C | 33.000 ft, TAS @12.000 lb | "226:7" | 226 ou 227 | mantido |
| 5-94 | Alcance máximo 1700 RPM, ISA -30°C | 12.000 ft, 12.000 lb, fluxo total | 496 | 492 | mantido |
| 5-96 | Alcance máximo 1700 RPM, ISA -10°C | SL, 10.000 lb, fluxo total | 746 | 756 | mantido |
| 5-98 | Alcance máximo 1700 RPM, ISA +10°C | 14.000 ft, 11.000 lb, fluxo total | 596 | 496 | mantido |
| 5-115 | 1 motor inoperante 1900 RPM | subtítulo | "IAS + 37°C" | "ISA + 37°C" | mantido |
| 5-1 a 5-3 | Índice da Seção 5 | "Normal Cruise 1800 RPM ISA -10°C" | 5-60 | 5-72 (provável) | mantido, marcado "as printed" |
| 5-1 a 5-3 | Índice da Seção 5 | "Climb - Balked Landing" | 5-105 | 5-119 (provável) | mantido, marcado "as printed" |
| 6-25 | Dados de carga (B200C) | nota 5 | "SQUARE FOOR" | "SQUARE FOOT" | mantido |
| 6-19 | Índice do B200C | título | "Baisc Empty Weight" | "Basic" | mantido |
| 6-1 | Índice da Seção 6 (B200) | "Usable Fuel 6-10" | 6-10 | 6-11 (no corpo, o combustível está na 6-11 e a carga na 6-10) | nota no texto |
| 7-6 | Sistema de anunciadores | "wil be selected" (wil) | mantido como impresso |
| 7-5 | Compensador elétrico | "annnciator" | mantido como impresso |

Checagens automáticas aplicadas às tabelas de cruzeiro e alcance: 12 ou 15 valores por linha e fluxo total = 2 × fluxo por motor (nas tabelas de um motor, igual ao por motor). Na tabela de limites de momento (6-17 e 6-36): momento máximo = peso × 196,4 / 100 e momento mínimo conforme os limites de C.G., sem divergências.

## 3. Itens para conferência humana

Pontos onde recomendo uma segunda leitura, por serem números críticos ou por terem sido só descritos.

| Pág. manual | Item | Motivo |
|---|---|---|
| 2-3 | Tabela de limites de velocidade | valores de voo (VA, VFE, VLO, VLE, VMCA, VMO) |
| 2-5 | Tabela de limites do motor | torque, ITT, pressão de óleo e 11 notas |
| 2-11 | Pesos e limites de C.G. | valores de carregamento |
| 2-23 a 2-25 | Lista de equipamentos exigidos por tipo de operação | muitos 0/1/2/3 em colunas estreitas |
| 3-3 | Velocidades de emergência | VXSE 115, VYSE 121, VMCA 86, descida 181, planeio 135 |
| 4-3 e 4-13 | Velocidades de operação segura e testes de governador/autofeather | valores numéricos |
| 5-5 | Tabela de rota Denver–Reno | índices ⁴ nas distâncias 143 e 146 |
| 5-35 | Accelerate-Go (exemplo) | 10.950 ft lido entre 10.950 e 10.960 |
| 5-31 | Tabela de trajetória de decolagem | 3116 e 4336 não aparecem no texto do manual |
| 5-84 | Cruzeiro máximo 1800 RPM, ISA -10°C | OAT -1 a 2.000 ft (outras tabelas mostram 1) |
| 6-11 | Combustível utilizável (4 densidades, 55 linhas) | momentos lidos coluna a coluna |
| 6-14 a 6-18, 6-26, 6-37 | Formulários e diagramas | só descritos em texto; desenhos não transcritos |
| 7-1 a 7-3 | Índice da Seção 7 | números de página de cada tópico (84 linhas) | conferir contra o corpo nos lotes seguintes; nenhum numeral foi alterado |
| 7-8 | Painel de cautela/aviso (ilustração) | posições 6×6 e marcas †, ††, \* | marcas lidas a 200 dpi |
| 7-10 | Painel de instrumentos | figura girada, só descrita | desenho não transcrito |

### Divergência a confirmar (lido, ainda não gravado — pág. 7-25, lote 12)
- 7-23: "Maximum continuous speed of the engine is 38,100 rpm, which equals 101.5% N1" (37.500 rpm = 100%) × 7-25: "Maximum continuous gas generator speed is limited to 38,100 rpm or 104.5% N1". 38.100/37.500 ≈ 101,6%. Será transcrito como impresso, com nota do transcritor.

## 4. Convenções da transcrição

- **Figuras e diagramas:** a imagem do `.md` original foi mantida logo abaixo do texto; curvas de gráficos **não** foram transcritas, apenas título, condições, notas, exemplos e tabelas pequenas.
- **Células "---" no original** (altitudes ou pesos sem dados) foram omitidas das linhas, com uma frase avisando abaixo da tabela.
- **Notas "Nota do transcritor":** indicam divergência impressa mantida ou escolha de formato (por exemplo tabela em duas colunas reunida em uma).
- **Páginas "intencionalmente em branco":** aparecem como uma linha em itálico, para preservar a numeração.
- **Itens de ação imediata (negrito) e itens com "+" ou "\*"** foram preservados como no original.
- **Travessões:** o original traz "—" e "-"; foram usados os dois conforme legibilidade; o hífen em "5-50" é de numeração de página.
- **Imagens pequenas do `.md` original** (logos "Beechcraft Super King Air" e ícones CAUTION/WARNING) foram omitidas a partir do lote 11; mantidas só figuras reais.
- Nenhum valor foi corrigido, estimado ou interpolado sem confirmação do usuário.

## 5. Próximos passos

1. Lote 11 (págs. 287–296), do zero.
2. Lotes seguintes de 10 páginas em ordem: 297–306, 307–316, … até a pág. 1309, atualizando a seção 1 a cada lote.
3. Por último, retranscrever as págs. 1–36 (abertura e Seção 1).
4. Conferência final: comparar a contagem de páginas cobertas com 1309 e revisar as seções 2 e 3 deste arquivo.
