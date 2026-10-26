# Controle da correção — KA-200-B200-POH_corrigido.md

Arquivo de acompanhamento da retranscrição do `KA-200-B200-POH_completo.md` (conversão automática do PDF escaneado, com OCR) para o `KA-200-B200-POH_corrigido.md`.

- **Fonte de verdade:** as imagens das páginas de `KA-200-B200-POH.pdf` (1309 páginas). O PDF é escaneado; o texto embutido é uma camada de OCR e **não** serve de referência.
- **Método:** cada página é renderizada (100–200 dpi) e retranscrita para Markdown, com confirmação do usuário a cada lote. **A partir do lote 12 o lote tem 10 páginas** (os lotes 1 a 11 usaram 25 páginas por lote). Tabelas numéricas são lidas a 200 dpi.
- **Numeração:** "pág. PDF" é a página do arquivo PDF; "pág. manual" é a numeração impressa (ex.: 5-50).
- **Branch atual:** `arena/995a83f5-kingair-b200` (commits e push nesta branch; nenhum PR novo). Pull request antigo (sessões anteriores): [JoaoPagotto/kingair_b200#1](https://github.com/JoaoPagotto/kingair_b200/pull/1), branch `claude/relaxed-thompson-9yr78s`.

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
| 11 | 287–311 | 7-1 a 7-25 | 7 Descrição dos Sistemas (início) | feito | `871d969` |
| 12 | 312–321 | 7-26 a 7-35 | 7 (synchrophaser TYPE II, lubrificação, partida/ignição, indução, proteção contra gelo, combustível, detecção e extinção de fogo, hélice, sistema elétrico) | feito | `511ba93` |
| 13 | 322–331 | 7-36 a 7-45 | 7 (iluminação, ambiental, pressurização, flow control units, ventilação, aquecimento, ar-condicionado) | feito | `82f7d79` |
| 14 | 332–341 | 7-46 a 7-55 | 7 (controles ambientais, oxigênio, pitot/estático, sangria de ar, warning de sangria, yaw damp, stall warning, proteção contra gelo, deice de hélice, deice de superfície) | feito | `effb1d3` |
| 15 em diante | 342–1309 | 7-56 ao fim | 7 (restante), 8 Manutenção e Serviço, 9 Suplementos, 10 Segurança | **pendente** (lotes de 10 págs.: 342–351, 352–361, …) | — |

**Resumo:** págs. 37–341 do PDF feitas (305 de 1309, ≈23%); págs. 342–1309 e 1–36 pendentes. A Seção 7 está transcrita até a pág. 7-55 (SURFACE DEICE SYSTEM).

### Observações sobre o lote 11 (págs. 287–311)
- Páginas 296 e 297 têm `/Rotate 270` no PDF: renderizadas e giradas antes da leitura.
- Páginas 296, 297 e 310 são só ilustração: mantidas as imagens `p00296_01.png`, `p00297_01.png` e `p00310_01.png` com uma frase descritiva.
- Pág. 290 (7-4): "THIS PAGE INTENTIONALLY LEFT BLANK".
- Tabelas dos painéis de anúncio (7-7 a 7-9) transcritas em grade 5×4 e 6 colunas, com as células em branco do original marcadas "—".
- O trecho de 7-25 (TYPE II do synchrophaser) termina em "When the prop sync", continuando na pág. 7-26; o heading e o texto preservados do `.md` antigo foram mantidos como início da pág. 7-26.

### Observações sobre o lote 12 (págs. 312–321)
- Página 319 (7-33) tem `/Rotate 270` no PDF: renderizada e girada antes da leitura; é só o FUEL SYSTEM SCHEMATIC.
- Páginas 313, 315 e 316 têm ilustrações (ENGINE ICE PROTECTION, FIRE DETECTION SYSTEM SCHEMATIC, FIRE EXTINGUISHER SYSTEM SCHEMATIC); mantidas as imagens com frase descritiva.
- As imagens p00314_01, p00318_01 (molduras de CAUTION) e p00320_01 (cabeçalho Beechcraft) são recortes do conversor; mantidas nas posições de fim de página, como nos lotes anteriores.
- As colunas de texto foram lidas na ordem coluna esquerda → coluna direita; várias frases passam de uma coluna para a outra (ex.: 7-26, 7-28, 7-32) e foram reunidas.
- A introdução do ELECTRICAL SYSTEM está no fim da coluna direita da p. 7-34 (não na 7-35).

### Observações sobre o lote 13 (págs. 322–331)
- Páginas 322, 324, 329 e 331 são só ilustração (ELECTRICAL SYSTEM SCHEMATIC, B200 e B200C ENVIRONMENTAL SYSTEM SCHEMATIC, ENVIRONMENTAL SYSTEM SCHEMATIC com evaporador traseiro opcional); mantidas as imagens com frase descritiva e legenda dos tipos de ar.
- Não há páginas giradas neste lote.
- As colunas foram lidas na ordem esquerda → direita; em 7-40 e 7-41 a figura está no alto da coluna direita, e a imagem foi mantida entre o texto da coluna esquerda e o da direita.
- A p. 7-36 (schemático elétrico) estava sem legenda no `.md` antigo; foi acrescentada a frase descritiva e o marcador `*(7-36)*`.

### Observações sobre o lote 14 (págs. 332–341)
- Não há páginas giradas neste lote; as dez páginas foram renderizadas a 250–500 dpi para conferência dos números.
- Páginas 335, 336, 338 e 341 são só ilustração (B200 e B200C OXYGEN SYSTEM SCHEMATIC, PITOT AND STATIC SYSTEM SCHEMATIC, PROPELLER ELECTRIC DEICE SYSTEM SCHEMATIC); mantidas as imagens com frase descritiva e legenda.
- Págs. 337 e 341 trazem molduras de WARNING e CAUTION (p00337_01.png, p00341_02.png): texto transcrito e imagens mantidas abaixo do texto.
- A numeração das listas de HEATING MODE / COOLING MODE (7-46) continua pela quebra de coluna: COOLING MODE começa com o item 1 no fim da coluna esquerda e os itens 2, 3 e 4 estão no alto da coluna direita.
- A legenda do esquema da p. 7-55 é "PROPELLER ELECTRIC DEICE SYSTEM SCHEMATIC" (200-251-1); o `.md` antigo trazia apenas "PROPELLER ELECTRIC DEICE SYSTEM SCHEMATIC" sem o número do desenho — número acrescentado a partir da imagem.
- A p. 7-54 tem dois blocos (PRIOR TO BB-829… e BB-829 AND AFTER…); o segundo bloco termina em "This switch is of the momentary type and", continuando na p. 7-56 (lote 15).
- Suspeita anterior de frase incompleta em 7-53 (BLEED AIR WARNING SYSTEM) foi afastada: a 500 dpi o texto está completo ("…Excessive heat on the plastic tubing caused by a ruptured bleed air line will cause the tubing to fail…").

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
| 7-23 vs 7-25 | Limite de N₁ (38.100 rpm) | texto | "101.5% N₁" (7-23) e "104.5% N₁" (7-25) | 38.100/37.500 = 101,6%, logo 101.5% | transcrito como impresso em cada página + "Nota do transcritor" na 7-25 |
| 7-35 | BATTERY CHARGE / carga da bateria | texto | "greater than .025" | .25 (provável) | transcrito como impresso; conferido a 600 dpi (impressão legível, sem ambiguidade de dígito) |
| 7-41 | FLOW CONTROL UNIT (BB-1180…) | texto | "avariable orifice" | "a variable orifice" | transcrito como impresso + Nota do transcritor |
| 7-41 | FLOW CONTROL UNIT (BB-1180…) | texto | "Three-position toggles switches on the RH subpanel f the flow control valves" | falta uma palavra (provável "control") | transcrito como impresso + Nota do transcritor |
| 7-44 | RADIANT HEATING (B200C) | texto | "additonal" | "additional" | transcrito como impresso + Nota do transcritor |
| 7-40/7-42/7-44 | texto | "fireseal", "condensor", "airconditioning" | "fire seal", "condenser", "air conditioning" | transcritos como impressos (grafia do original) |
| 7-54 | PROP - MANUAL - OFF (BB-829 e posteriores) | texto | "aproximately 90 seconds" | "approximately" | transcrito como impresso + Nota do transcritor |

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
| 7-7 a 7-9 | Painéis de anúncio (grade de luzes) | posição exata de cada luz na grade e cores (Red/Yellow/Green) |
| 7-12 | Raio de giro mínimo (39 ft 10 in) e disjuntores de flaps | valor lido em recorte de alta resolução |
| 7-13/7-14 | 2775 ±55 psi e aproximadamente 2400 psi | pressões do sistema hidráulico |
| 7-15 | Pressões dos pneus 18x5.5, 22x6.75-10 e do trem de nariz | três valores diferentes na mesma página |
| 7-19 | "orange stripe on each of the six rotary latches (three on each side)" | confere com 6 travas (3 por lado) |
| 7-23 | 850 SHP, 37.500 rpm = 100% N₁, 38.100 rpm, 38.500 rpm, 30.000 rpm, 2000 rpm | valores de motor conferidos em recorte |
| 7-26 | 3.5 U.S. gallons, 2.3 gallons, 5 quarts (óleo) | valores de capacidade do sistema de lubrificação |
| 7-27 | 410 foot-pounds (auto ignition), 50% N₁ (partida) | limiar de torque e corte do starter |
| 7-30/7-31 | 2080 rpm, 1830 a 1910 rpm, 2120 rpm, 2200 rpm, 95%, 90% N₁ | governadores de hélice e autofeather |
| 7-31/7-32 | 10 ± 1 psi, 11 ± 2 psi, 10 horas, 150 horas, 50 gal/h, 7500/15.000 gal | pressões e limites de combustível |
| 7-32 | SERIALS BB-734… e SERIALS BB-1096… (bombas standby) | dois textos distintos por faixa de série; conferir a frase repetida "located on the fuel control panel" |
| 7-34 | Tabela FUEL DRAINS (6 linhas) | localização dos drenos |
| 7-35 | 1100 A, 300 A, 20% N₁, 325 A, 60/70/50 A, 400 Hz/115 V/26 VAC, 7 A, 1000/300 A | sistema elétrico |
| 7-37 | 6.5 ± .1 psi; 2800 ft @ 20.000, 8600 ft @ 31.000, 10.400 ft @ 35.000 | pressurização |
| 7-39 | 8 a 16 lb/min; 0,1 psi; 12.500 ft; -1000 a +15.000 MSL; 50-300 a 2000 ±500 pés/min; 1000 ft e 500 ft | controlador de pressurização |
| 7-40 | 18 a 20 psi; -30°F; "6 seconds" (coluna esquerda) | flow control unit Thru BB-1179 |
| 7-41 | "approximately seven seconds" (coluna direita) e "approximately 6 seconds" (7-40) | dois atrasos diferentes no mesmo assunto; conferir |
| 7-44 | 62% N₁; 33°F; 3 a 5 minutos (7-46) | ar-condicionado |
| 7-46 | 60% N₁; 30°; 30 segundos por válvula / 1 minuto; 3 a 5 minutos | modo automático e manual da temperatura da cabine |
| 7-47 | 8 a 16 lb/min; 60% N₁; "MANUAL TEMPerature/DECRease" (grafia do original) | controle ambiental e modo manual |
| 7-47/7-48 | 35.000 pés; 3.9 LPM-NTPD; 20.000 pés; 12.500 pés; 9 polegadas; "SYStem" (grafia do original) | sistema de oxigênio |
| 7-51 | Três petcocks; inspeção de 150 horas; drenagem das linhas de ar estático | pitot e estático |
| 7-53 | 18 psi; 17.000 pés (yaw damp); 50-ampere e five-ampere (windshield heat) | sangria de ar, yaw damp, proteção contra gelo |
| 7-54 | 14 a 18 amperes; 20-ampere; 30 segundos; 90 segundos; 3 minutos; ".05" de carga | deice elétrico de hélice (dois blocos de série) |
| 7-55 | 6 segundos; 4 segundos; -40°C (CAUTION) | pitot heat e surface deice |

## 4. Convenções da transcrição

- **Figuras e diagramas:** a imagem do `.md` original foi mantida logo abaixo do texto; curvas de gráficos **não** foram transcritas, apenas título, condições, notas, exemplos e tabelas pequenas.
- **Células "---" no original** (altitudes ou pesos sem dados) foram omitidas das linhas, com uma frase avisando abaixo da tabela.
- **Notas "Nota do transcritor":** indicam divergência impressa mantida ou escolha de formato (por exemplo tabela em duas colunas reunida em uma).
- **Páginas "intencionalmente em branco":** aparecem como uma linha em itálico, para preservar a numeração.
- **Itens de ação imediata (negrito) e itens com "+" ou "\*"** foram preservados como no original.
- **Travessões:** o original traz "—" e "-"; foram usados os dois conforme legibilidade; o hífen em "5-50" é de numeração de página.
- Nenhum valor foi corrigido, estimado ou interpolado sem confirmação do usuário.

## 5. Próximos passos

1. ~~Concluir o lote 11 (págs. 287–311)~~ feito.
2. Lotes seguintes em ordem, de 10 páginas: 342–351, 352–361, … até a pág. 1309, atualizando a seção 1 a cada lote.
3. Por último, retranscrever as págs. 1–36 (abertura e Seção 1).
4. Conferência final: comparar a contagem de páginas cobertas com 1309 e revisar as seções 2 e 3 deste arquivo.
