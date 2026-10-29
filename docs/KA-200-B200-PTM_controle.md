# Controle de revisão — KA-200-B200-PTM

## 1. Identificação da fonte

- **PDF:** [KA-200-B200-PTM.pdf](KA-200-B200-PTM.pdf)
- **Páginas físicas:** 382
- **SHA-256 esperado e observado:** `6835a8102c8f600c3b39aa34d2b53f9a848790321447136ec2cd821af245986d` — conferem.
- **Tamanho:** 32.274.925 bytes.
- **Transcrição:** [KA-200-B200-PTM.md](KA-200-B200-PTM.md)
- **Manifesto:** [KA-200-B200-PTM_manifesto.json](KA-200-B200-PTM_manifesto.json)
- **Branch:** `arena/25936ceb-kingair-b200`.
- **Datas:** lote 1 e lote 2 em 2026-10-29.
- **Escopo:** comparação documental, não validação operacional nem aprovação para voo.

## 2. Trabalho anterior preservado

PDF, POH e conversões automáticas anteriores do PTM permanecem inalterados. O lote 1 foi preservado byte a byte nos trechos 1–100; apenas o cabeçalho de estado e os trechos pendentes 101–200 foram atualizados. Verificação adicional comparou todos os arquivos rastreados antes do lote 2: somente `PTM.md`, `PTM_controle.md`, `PTM_manifesto.json` e testes foram alterados, além dos novos assets do lote 2.

## 3. Progresso por lote

| Lote | Páginas físicas | Estado | Revisadas no lote | Commit |
|---|---|---|---:|---|
| 1 | 1–100 | Concluído e publicado | 100 | `2c02f6f54990c9a3afac5cd9ebbe85f3d5669e2e` |
| 2 | 101–200 | Concluído; aguardando confirmação para o lote 3 | 100 | A publicar neste lote |
| 3 | 201–300 | Pendente; não iniciar sem confirmação | 0 | — |
| 4 | 301–382 | Pendente; não iniciar sem confirmação | 0 | — |

**Total revisado:** 200/382 (52.36%). **Pendentes:** 182 páginas.

## 4. Método empregado

### Lote 1 (1–100)
Renderização 144 dpi; detalhes 200–220 dpi; texto nativo apenas como apoio; tabelas Markdown; imagens de apoio; divergências mantidas; hashes por trecho.
### Lote 2 (101–200)
1. Reconfirmados hash do PDF, 382 páginas, branch, Git limpo e 19 testes do lote 1 antes de editar.
2. Conferência visual sequencial das páginas 101–200 a 144 dpi; tabelas críticas e gráficos a 240 dpi; esquemas girados a 200 dpi.
3. Texto nativo usado apenas como apoio. Trechos foram montados somente nos marcadores pendentes 101–200; marcadores 1–100 e 201–382 preservados.
4. Tabelas 5-1, 7-1, 7-2, 7-3, 7-4 e 8-1 reconstruídas em Markdown, com cabeçalhos, células vazias, notas e continuações. Tabelas de limites foram conferidas em detalhe.
5. Figuras e esquemas preservados em `docs/assets/ptm/`; detalhes girados apenas para leitura, com fac-símile original.
6. Nenhuma leitura de gráfico foi interpolada; nenhuma linha ausente de tabela foi completada; questões sem gabarito.
7. Cada página revisada tem marcador, link PDF, hash SHA-256 e fac-símile.

## 5. Principais ressalvas e divergências mantidas

| Página física | Página impressa | Ressalva |
|---:|---|---|
| 3 | Copyright | Grafia “Famborough” mantida como impressa. |
| 4 | Lista de páginas efetivas | Lista de páginas efetivas reconstruída; entrada “10-1—22” mantida como impressa. |
| 11 | 1-2 | Mantidos “24-volt. 42-ampere”, “BB-1 632” e “startergenerators”; parênteses em itálico na fonte. |
| 12 | 1-3 | Confirmadas visualmente e mantidas as grafias “baltery”, “interconnecled”, “buttery” e “SO-amp”. |
| 13 | 1-4 | Mantidos “This switch control” e “Prior·to”. Continua na página física 14. |
| 15 | 1-6 | Mantido “threestage”; N1 representado com subscrito. |
| 17 | 1-8 | Texto de proteção contra gelo remete à Figure 1-9; mantido como impresso. Continua na página física 18. Continuação da página física 16. |
| 20 | 1-11 | Mantida a quebra “control-ler”. Continua na página física 21. |
| 21 | 1-12 | Mantido “selfcentered”. Continuação da página física 20. |
| 24 | 1-15 | Mantidos “certificated”, “constantflow” e capitalização “SYStem”. Continua na página física 25. |
| 25 | 1-16 | Texto informa 43 ft 9 in; figuras 1-23/1-24 distinguem configurações (1) e (2). Não harmonizado. Continuação da página física 24. |
| 26 | 1-17 | Cotas e configurações preservadas no desenho; não convertidas em tabela para não perder a associação das setas. |
| 27 | 1-18 | Cotas diferem da figura 1-23 conforme configuração; preservadas sem correção. |
| 28 | 1-19 | Legenda da Figure 1-25 diz “Airplane Dimensions”, embora o desenho seja de disposição de cabine; mantida. |
| 31 | 1-22 | Mantido “EXITPULL” sem espaço. Continuação da página física 30. |
| 33 | 1-24 | Mantido “Ushaped”. |
| 35 | 2-iii | Mantida a grafia “Nickel Cadium” na lista de ilustrações. |
| 37 | 2-1 | Camada nativa extrai “SYSTEMES”; a imagem mostra “SYSTEMS”. Transcrito conforme a imagem. |
| 40 | 2-4 | Legenda da Figure 2-5 diz “BATTERY CHG”; a lente fotografada diz “BATTERY CHARGE”. Ambas preservadas. Continua na página física 41. |
| 44 | 2-8 | Texto cita BB-1098 (excluding BB-1096); página 12 cita prior to BB-1096. Divergência mantida. Continua na página física 45. Continuação da página física 43. |
| 48 | 2-12 | Legenda “B-2 THROUGH BB-1443, EXCEPT 1439” mantida como impressa. Continuação da página física 47. |
| 50 | 2-14 | Rótulo “AVONICS” no diagrama preservado na imagem. |
| 52 | 2-16 | Diagrama girado para leitura; nota de serialidade preservada no detalhe. |
| 53 | 2-17 | Diagrama girado para leitura; notas de serialidade preservadas no detalhe. |
| 54 | 2-18 | Faixa de seriais da legenda mantida, inclusive “BB-1449”. |
| 58 | 2-22 | Tabela 2-1: o segundo grupo não traz a linha “70 to 75%”; ausência mantida, sem interpolação. |
| 60 | 2-24 | Mantidas as formas “BB 1-162” e “BB 163” como impressas. Continua na página física 61. |
| 61 | 2-25 | Mantidas as faixas “BB 1-450” e “BB 450 AND SUBSEQUENT” como impressas. Continua na página física 62. Continuação da página física 60. |
| 63 | 2-27 | Tabela 2-4: “STALL WARN” associado a “FIREWALL VALVE SWITCH” como impresso; não corrigido. |
| 78 | 4-iii | Lista de ilustrações mantém a ordem impressa 4-9 antes de 4-8. |
| 83 | 4-5 | Tabela 4-1 reconstruída; lentes vermelhas preservadas em imagem de apoio. |
| 84 | 4-6 | Tabela 4-3 mantém pares impressos incomuns: DOOR UNLOCKED→altitude de cabine; ALT WARN→fogo motor direito. Não corrigido. |
| 87 | 4-9 | Mantido “deengergized”; introdução fala em warning annunciators, mas a tabela é caution advisory. |
| 88 | 4-10 | Mantidos “deengergized” e “B-200”. |
| 89 | 4-11 | Mantido “deengergized”. |
| 94 | 5-1 | Totais de combustível mantidos como impressos (386/158/544 gal; 2.586/1.058/3.644 lb). |
| 96 | 5-3 | Esquema colorido girado para leitura; legenda, símbolos e notas preservados no detalhe. Continuação da página física 95. |
| 97 | 5-4 | Esquema colorido girado para leitura; legenda, símbolos e notas preservados no detalhe. |
| 98 | 5-5 | Capacidades por célula preservadas no desenho; totais do texto não foram redistribuídos. Continua na página física 99. |
| 99 | 5-6 | Mantida a referência “Service Bulletin 0703-286”. Continuação da página física 98. |
| 101 | 5-8 | Figura 5-6 mostra lente “L FUEL PRESS LO”; texto usa FUEL PRESS. Mantido. |
| 102 | 5-9 | Faixas de seriais e alimentação dos medidores de fluxo mantidas; continua na p. 103. |
| 103 | 5-10 | Aquecedor de combustível 70° a 90°F; nota da figura sobre BB-1401 preservada. Continua na página física 104. Continuação da página física 102. |
| 104 | 5-11 | Crossfeed apenas com um motor inoperante conforme texto; continua na p. 105. Continuação da página física 103. |
| 105 | 5-12 | Capitalização “FUEL PRESSure” mantida. Continuação da página física 104. |
| 106 | 5-13 | Tabela 5-1 reconstruída; “Aft” maiúsculo mantido. Continua na página física 107. |
| 107 | 5-14 | Gráfico preservado em imagem; nenhuma leitura foi interpolada. Concentração de aditivo 0.10%–0.15% mantida. Continua na página física 108. Continuação da página física 106. |
| 108 | 5-15 | Referência “MEL-T-5624” mantida como impressa; pesos zero-fuel 10.400/11.000 lb. Continuação da página física 107. |
| 109 | 5-16 | Questões preservadas sem indicar respostas. |
| 110 | 6-i | Capítulo 6 declara informação não aplicável; apenas página 6-i presente, sem 6-ii no PDF. |
| 114 | 7-v | Índice mantém 7-14 antes de 7-13; página impressa 7-v (7-iv não presente no PDF). |
| 115 | 7-vi | Índice mantém 7-34 antes de 7-33 e Table 7-2 antes de 7-1; títulos de aplicabilidade mantidos. |
| 116 | 7-1 | Valores declarados ilustrativos; não substituem o manual de voo aprovado. |
| 118 | 7-3 | Figura 7-2 usa N<sub>G</sub>/N<sub>F</sub>; texto usa N<sub>1</sub>/NP. Ambas as notações preservadas. |
| 119 | 7-4 | Figura girada para leitura; orientação original no fac-símile. |
| 120 | 7-5 | Válvulas de sangria fecham acima de aproximadamente 90% N1. |
| 123 | 7-8 | Sistema de óleo e detecção de partículas preservados. |
| 124 | 7-9 | Figura 7-7 mostra CHIP DETECT em âmbar/vermelho conforme série. |
| 125 | 7-10 | Esquema de óleo girado para leitura; legenda e cores preservadas. |
| 127 | 7-12 | Esquema de combustível girado; notas BB-1401/BB-666 preservadas. |
| 128 | 7-13 | Início “aDownstream” mantido como impresso; texto continua após a figura da p. 129, na p. 130. |
| 129 | 7-14 | Esquema FCU girado para leitura. |
| 130 | 7-15 | Continuação do texto da p. 128; fuel topping 106%/95% e autoignition 400 ft-lb mantidos. |
| 131 | 7-16 | Texto continua após a figura da p. 132, na p. 133. |
| 133 | 7-18 | Grafia “B-1192” mantida; ângulos de pá por fabricante/série preservados. Continua na página física 134. Continuação da página física 131. |
| 134 | 7-19 | Overspeed 2.120/2.080 rpm e teste 1.830–1.910 rpm mantidos. Continua na página física 135. Continuação da página física 133. |
| 135 | 7-20 | Limite de reverso 1.900 rpm e comandos 83%±5%, –9°/–10°, 95% mantidos. Continuação da página física 134. |
| 138 | 7-23 | LOW IDLE 61%/56%/52% conforme série/motor; mantido. Continua na página física 140. |
| 140 | 7-25 | Figura 7-23 mostra 2.080 rpm normal e ~1.870 rpm em teste; não harmonizado com o texto. Continuação da página física 138. |
| 141 | 7-26 | Texto remete ITT a “Figure 7-27”, mas a figura dos gages ITT é 7-26; mantido. |
| 142 | 7-27 | Torque limiter 2.368–2.447 ft-lb e máximo certificado 2.230 ft-lb mantidos. |
| 143 | 7-28 | Redação sobre alimentação dos gages N1 “prior to BB-1484 including BB-1485” mantida. |
| 147 | 7-32 | Texto de indicação remete a “Figure 7-35”, mas as luzes aparecem na Figure 7-36; mantido. |
| 148 | 7-33 | Autofeather: limiares 400/200 ft-lb preservados. |
| 149 | 7-34 | Nota sobre LOW IDLE e teste; desbandeiramento ~18° preservado. |
| 150 | 7-35 | Tabelas 7-1/7-2 reconstruídas; título da 7-2 (“PRIOR TO BB-1439, 1444 AND SUBSEQUENT”) mantido como impresso. |
| 151 | 7-36 | Tabela 7-3 e 13 notas preservadas; nota 12 sem marcador visível nas tabelas; óleo 0–99°C em cruise climb mantido. |
| 152 | 7-37 | Diâmetros de hélice e limites de partida preservados; repetição “Rotational Speed Limits” mantida. |
| 153 | 7-38 | Tabela 7-4: terceiro grupo tem apenas ITT e torquímetro; “extends form” mantido como impresso. |
| 154 | 7-39 | Questões preservadas sem indicar respostas. |
| 155 | 7-40 | Questões preservadas sem indicar respostas. |
| 157 | 8-iii | Índice do capítulo 8; página 8-ii não presente no PDF. |
| 159 | 8-2 | Rótulo “DETAL B” mantido na imagem. |
| 160 | 8-3 | Rótulo “DETAL B” mantido na imagem. |
| 161 | 8-4 | Agente CBrF3 e alimentação pelo hot battery bus preservados. |
| 162 | 8-5 | Rótulo “DETAL B” mantido na imagem. |
| 163 | 8-6 | Tabela 8-1 reconstruída; pares temperatura/pressão conferidos em detalhe. |
| 165 | 8-8 | Questões preservadas sem indicar respostas. |
| 167 | 9-iii | Índice mantém Figure 9-6 antes de 9-5; página 9-ii não presente no PDF. |
| 170 | 9-3 | Efeitos de vazamento de sangria em torque/ITT mantidos como impressos. |
| 172 | 9-5 | Nota: anunciador de sangria não apaga após fechar válvulas; mantida. |
| 173 | 9-6 | Diagrama girado para leitura; temporização 6–8 s preservada. |
| 174 | 9-7 | Limites pneumáticos 12–20 psi e faixas de vácuo preservados. |
| 175 | 9-8 | Questões preservadas sem indicar respostas. |
| 180 | 10-2 | Aviso sobre botas insufladas e OAT abaixo de –40°C preservado. |
| 183 | 10-5 | Ciclo SINGLE: 6 s asas, 4 s estabilizador; preservado. |
| 184 | 10-6 | Brake deice: 85% N1 e.timer 10 min preservados. Continua na página física 185. |
| 185 | 10-7 | Windshield heat +95°F a +105°F preservado. Continuação da página física 184. |
| 186 | 10-8 | Figura 10-6 mostra sensor “95° TO 105°” sem unidade F; texto usa °F. |
| 187 | 10-9 | Sequências de aquecimento 90 s/30 s e redação “prior to BB-2 through...” mantidas. Continua na página física 188. |
| 188 | 10-10 | PROP AMPS 18–24 A (4 pás) / 14–18 A (3 pás); modo manual não registra no amperímetro. Continuação da página física 187. |
| 189 | 10-11 | Avisos sobre pitot/stall warning heat no solo preservados; continua na p. 190. |
| 190 | 10-12 | Aquecimento de vent e FCU preservados; continua na p. 191. Continuação da página física 189. |
| 191 | 10-13 | Ice vanes: 15 s, 160 knots; aviso continua após figuras 10-11/10-12, na p. 194. Continuação da página física 190. |
| 194 | 10-16 | Continuação do aviso da p. 191; +5°C/+15°C e perda de torque preservados. |
| 195 | 10-17 | Wipers não operar em vidro seco; limitações de gelo continuam na p. 196. |
| 196 | 10-18 | Limites 140 KIAS mínimo e 226 KIAS máximo efetivo preservados. Continua na página física 197. Continuação da página física 195. |
| 197 | 10-19 | Avisos de gelo, wipers e hélice estática preservados. Continua na página física 198. Continuação da página física 196. |
| 198 | 10-20 | NOTES de backup manual 90 s/30 s e deflexão ~5% preservadas. Continuação da página física 197. |
| 199 | 10-21 | Questões preservadas sem indicar respostas. |
| 200 | 10-22 | Questão 12 alternativa D termina em “Indication speeds” como impresso; nada acrescentado. |

## 6. Limitações

- Rótulos pequenos, cores, setas e relações espaciais de diagramas permanecem nas imagens de apoio.
- Gráfico 5-11 preservado sem interpolação de valores.
- Tabela 7-4, grupo PT6A-41, contém apenas ITT e torquímetro na fonte; nada foi acrescentado.
- Questão 12 da página 200 termina em “Indication speeds” na alternativa D; final ausente não foi inventado.
- Revisão não confirma atualidade operacional nem aplicabilidade a aeronaves específicas.

## 7. Inventário por página física

Hash do trecho: SHA-256 do conteúdo entre marcadores, excluindo linhas de marcador e status. `—` indica trecho pendente.

| Página física | Página impressa | Seção | Status | Hash do trecho | Marcador | Observações |
|---:|---|---|---|---|---|---|
| [1](KA-200-B200-PTM.pdf#page=1) | Cover | Abertura | Revisada | `6e5ff437601608ce22e0807a9541e0cb858449681f51b7e961b6507eee3d7eb2` | `PTM:PAGE:001` | Texto conferido com a imagem. |
| [2](KA-200-B200-PTM.pdf#page=2) | Notice | Abertura | Revisada | `3c9fd1d1675f635de17d2641bb017ae7e3cffd970f36e72cbfce4b3afd13bc82` | `PTM:PAGE:002` | Texto conferido com a imagem. |
| [3](KA-200-B200-PTM.pdf#page=3) | Copyright | Abertura | Revisada | `f635c48694622d290a7d7a5fe87f71b2c5e3c30b45c52ff5fdf39d24f58e2a61` | `PTM:PAGE:003` | Grafia “Famborough” mantida como impressa. |
| [4](KA-200-B200-PTM.pdf#page=4) | Lista de páginas efetivas | Abertura | Revisada | `dd9591f5b763bfdaa54d29fc7b17fc5cd3130c3ef55dbc378aa5ea15a42e1983` | `PTM:PAGE:004` | Lista de páginas efetivas reconstruída; entrada “10-1—22” mantida como impressa. |
| [5](KA-200-B200-PTM.pdf#page=5) | Contents | Abertura | Revisada | `7b75089bb8140f370bfca6a19995f64c1f7dc8ae1c63be8f698a9a19c15629b8` | `PTM:PAGE:005` | Texto conferido com a imagem. |
| [6](KA-200-B200-PTM.pdf#page=6) | 1-i | 1 Aircraft General | Revisada | `fc839a20bee6cb65d39ff9949f26e1c8316f49ec62f4c5bcc84b054a3c1c08c4` | `PTM:PAGE:006` | Texto conferido com a imagem. |
| [7](KA-200-B200-PTM.pdf#page=7) | 1-ii | 1 Aircraft General | Revisada | `5662bae3da5d8baaa1db326d47d7b5ac1f9340f7453838896424596ab43675da` | `PTM:PAGE:007` | Texto conferido com a imagem. |
| [8](KA-200-B200-PTM.pdf#page=8) | 1-iii | 1 Aircraft General | Revisada | `ef90f2f761263cc5316c1b961edd40c2e82d943492d0e670b8074d9d8d17c21b` | `PTM:PAGE:008` | Texto conferido com a imagem. |
| [9](KA-200-B200-PTM.pdf#page=9) | 1-iv | 1 Aircraft General | Revisada | `bb622b385faca2e3eb288da532791028ebb26da5d4803274ae909941cbf50557` | `PTM:PAGE:009` | Texto conferido com a imagem. |
| [10](KA-200-B200-PTM.pdf#page=10) | 1-1 | 1 Aircraft General | Revisada | `9862c3cf36c097c440fb03ce4a90c40b3ec3d1696f2fa50592d49342ddf9e43e` | `PTM:PAGE:010` | Figuras preservadas em imagem de apoio. |
| [11](KA-200-B200-PTM.pdf#page=11) | 1-2 | 1 Aircraft General | Revisada | `717f752e16e9fbf2602d22d2f6a39661021ffbe42ba2dafc584dd5ed18807070` | `PTM:PAGE:011` | Mantidos “24-volt. 42-ampere”, “BB-1 632” e “startergenerators”; parênteses em itálico na fonte. |
| [12](KA-200-B200-PTM.pdf#page=12) | 1-3 | 1 Aircraft General | Revisada | `898913f363b1f29ae4ace590087f8105fa37dfeafaff0639da133a7203fde02f` | `PTM:PAGE:012` | Confirmadas visualmente e mantidas as grafias “baltery”, “interconnecled”, “buttery” e “SO-amp”. |
| [13](KA-200-B200-PTM.pdf#page=13) | 1-4 | 1 Aircraft General | Revisada | `71fbf9b9347e864b737a74ec76de30cb1887641a5e6c5d403c2ef5715a145a18` | `PTM:PAGE:013` | Mantidos “This switch control” e “Prior·to”. Continua na página física 14. |
| [14](KA-200-B200-PTM.pdf#page=14) | 1-5 | 1 Aircraft General | Revisada | `68c6c9970866651355ad038976d6bea0a2bbae7229efcc6c0ed1a1748db1c3b6` | `PTM:PAGE:014` | Continuação da página física 13. |
| [15](KA-200-B200-PTM.pdf#page=15) | 1-6 | 1 Aircraft General | Revisada | `7995e1ab097465513f8d2de03e2834169e7ab3d629b908c6a746bdc115bfd31d` | `PTM:PAGE:015` | Mantido “threestage”; N1 representado com subscrito. |
| [16](KA-200-B200-PTM.pdf#page=16) | 1-7 | 1 Aircraft General | Revisada | `222dcbbb12d6a05231388dc26985f7f039eea7451e57ce267ac8c72d2c375d83` | `PTM:PAGE:016` | Continua na página física 17. |
| [17](KA-200-B200-PTM.pdf#page=17) | 1-8 | 1 Aircraft General | Revisada | `44e64a7aaabfeeb8814c31cb45e37541675334d0641676a5c5fb533b5799a235` | `PTM:PAGE:017` | Texto de proteção contra gelo remete à Figure 1-9; mantido como impresso. Continua na página física 18. Continuação da página física 16. |
| [18](KA-200-B200-PTM.pdf#page=18) | 1-9 | 1 Aircraft General | Revisada | `0a03d6d0e8573548e5c76b9ec9343af266a049b132fca0dd90718048fbda6acb` | `PTM:PAGE:018` | Continuação da página física 17. |
| [19](KA-200-B200-PTM.pdf#page=19) | 1-10 | 1 Aircraft General | Revisada | `b08e536503aeca85facea4eac2796c881fb48976d7800f8c956b387bca76dafe` | `PTM:PAGE:019` | Tabela 1-1 reconstruída; valores e tolerâncias ± conferidos. |
| [20](KA-200-B200-PTM.pdf#page=20) | 1-11 | 1 Aircraft General | Revisada | `ee32b10f178621dcc5e19c84a0024149d2b594bcd4e03194c6bf12bdac2a6e39` | `PTM:PAGE:020` | Mantida a quebra “control-ler”. Continua na página física 21. |
| [21](KA-200-B200-PTM.pdf#page=21) | 1-12 | 1 Aircraft General | Revisada | `52e36b37d4e3c2b0e7d5642a3edd76447fe1577008a0e705e95b148f0fed1f93` | `PTM:PAGE:021` | Mantido “selfcentered”. Continuação da página física 20. |
| [22](KA-200-B200-PTM.pdf#page=22) | 1-13 | 1 Aircraft General | Revisada | `3b4436dd1e47c0dead5f01ae607eb641112d4b9acb87a90b972cceb538f46ad1` | `PTM:PAGE:022` | Figuras preservadas em imagem de apoio. |
| [23](KA-200-B200-PTM.pdf#page=23) | 1-14 | 1 Aircraft General | Revisada | `0107019988c4a7998a61ddbc09b84679de83bd0f4fe4c5a9e0a01505a5e47d5b` | `PTM:PAGE:023` | Figuras preservadas em imagem de apoio. |
| [24](KA-200-B200-PTM.pdf#page=24) | 1-15 | 1 Aircraft General | Revisada | `f21dd27a0c40fda3fb6f2e1c6df9fe25953b3165436ef18538cd1048f9f301cd` | `PTM:PAGE:024` | Mantidos “certificated”, “constantflow” e capitalização “SYStem”. Continua na página física 25. |
| [25](KA-200-B200-PTM.pdf#page=25) | 1-16 | 1 Aircraft General | Revisada | `4f818a83e1263baaa87b47d8a935d5ce5c42ea6d81fb7744fcc90d8933a755d5` | `PTM:PAGE:025` | Texto informa 43 ft 9 in; figuras 1-23/1-24 distinguem configurações (1) e (2). Não harmonizado. Continuação da página física 24. |
| [26](KA-200-B200-PTM.pdf#page=26) | 1-17 | 1 Aircraft General | Revisada | `d9deea10a8252a55160cabf34373131836c2c3cd409bbf2317d0f70a77994d36` | `PTM:PAGE:026` | Cotas e configurações preservadas no desenho; não convertidas em tabela para não perder a associação das setas. |
| [27](KA-200-B200-PTM.pdf#page=27) | 1-18 | 1 Aircraft General | Revisada | `df3839a0cfb02ce545bca841d178968120bfc7efeb2e92f98a12d785e0fb505d` | `PTM:PAGE:027` | Cotas diferem da figura 1-23 conforme configuração; preservadas sem correção. |
| [28](KA-200-B200-PTM.pdf#page=28) | 1-19 | 1 Aircraft General | Revisada | `decbdf72f52bd3683ea65383b2213d74590fb8cf040c776712138b5e7ae0c983` | `PTM:PAGE:028` | Legenda da Figure 1-25 diz “Airplane Dimensions”, embora o desenho seja de disposição de cabine; mantida. |
| [29](KA-200-B200-PTM.pdf#page=29) | 1-20 | 1 Aircraft General | Revisada | `8bc7c3db7f428af3c58f5a52fee3b4b5f13176215a7940da2d16bf17ebf8433a` | `PTM:PAGE:029` | Figuras preservadas em imagem de apoio. |
| [30](KA-200-B200-PTM.pdf#page=30) | 1-21 | 1 Aircraft General | Revisada | `4e6671168dcc4cea928785bbabd2f41422079ca69d7b87060db73a6692969be4` | `PTM:PAGE:030` | Continua na página física 31. |
| [31](KA-200-B200-PTM.pdf#page=31) | 1-22 | 1 Aircraft General | Revisada | `c1b4fdacda41ce733b0a3d18fbc35537fee94c230170bbabf76d0b38f7527688` | `PTM:PAGE:031` | Mantido “EXITPULL” sem espaço. Continuação da página física 30. |
| [32](KA-200-B200-PTM.pdf#page=32) | 1-23 | 1 Aircraft General | Revisada | `b20a5440407350cc99d362701296e778db21361db6bc50d8693c13a412e40357` | `PTM:PAGE:032` | Figuras preservadas em imagem de apoio. |
| [33](KA-200-B200-PTM.pdf#page=33) | 1-24 | 1 Aircraft General | Revisada | `ee7c95e1f1211a345285940c85aed701b02a1ad41cac00f9db6b39d7e01cdfaa` | `PTM:PAGE:033` | Mantido “Ushaped”. |
| [34](KA-200-B200-PTM.pdf#page=34) | 2-i | 2 Electrical Power Systems | Revisada | `917c0635308c9bcc9cdc808f74ba51f58368148e5d417eba9b3051687eb06d73` | `PTM:PAGE:034` | Texto conferido com a imagem. |
| [35](KA-200-B200-PTM.pdf#page=35) | 2-iii | 2 Electrical Power Systems | Revisada | `802404ee578c40844b819a9117cf02e1d2371a23f7a36d51cd63bb11cc2a001a` | `PTM:PAGE:035` | Mantida a grafia “Nickel Cadium” na lista de ilustrações. |
| [36](KA-200-B200-PTM.pdf#page=36) | 2-iv | 2 Electrical Power Systems | Revisada | `3edcd2532e8a6f178aec975ec5abdf7de89ba594d1dbb22bb2b4be7ef65aa0e8` | `PTM:PAGE:036` | Texto conferido com a imagem. |
| [37](KA-200-B200-PTM.pdf#page=37) | 2-1 | 2 Electrical Power Systems | Revisada | `e3533515f20e600ffb77749b819c8730a2370cf3cfe05d8fa2f1b64677b4c648` | `PTM:PAGE:037` | Camada nativa extrai “SYSTEMES”; a imagem mostra “SYSTEMS”. Transcrito conforme a imagem. |
| [38](KA-200-B200-PTM.pdf#page=38) | 2-2 | 2 Electrical Power Systems | Revisada | `654a3833cfbc4c87c9f6a2b8afa0f9944e4dd52af6e3cc2af5eb6dacad12e4ff` | `PTM:PAGE:038` | Continua na página física 39. |
| [39](KA-200-B200-PTM.pdf#page=39) | 2-3 | 2 Electrical Power Systems | Revisada | `c09052895b293f49ea1f11f08ac7cc94727efc831b0008c6b3946c446f7110de` | `PTM:PAGE:039` | Continuação da página física 38. |
| [40](KA-200-B200-PTM.pdf#page=40) | 2-4 | 2 Electrical Power Systems | Revisada | `38b3e06d73ab86efc129f2e411528f7045634372b0ba0a402d3e9bffb9c4bc5f` | `PTM:PAGE:040` | Legenda da Figure 2-5 diz “BATTERY CHG”; a lente fotografada diz “BATTERY CHARGE”. Ambas preservadas. Continua na página física 41. |
| [41](KA-200-B200-PTM.pdf#page=41) | 2-5 | 2 Electrical Power Systems | Revisada | `17dd185571b340cdae2be83846dfba0837427682adca4ba4d5bd07e24dc6fef7` | `PTM:PAGE:041` | Continuação da página física 40. |
| [42](KA-200-B200-PTM.pdf#page=42) | 2-6 | 2 Electrical Power Systems | Revisada | `0bf887e16751b3288486fc98d02e5088f0308144bd195ab5b5101b12498f80d5` | `PTM:PAGE:042` | Figuras preservadas em imagem de apoio. |
| [43](KA-200-B200-PTM.pdf#page=43) | 2-7 | 2 Electrical Power Systems | Revisada | `b56b25a252cb30859a6b70facb3703bc21db4ea5e8d10aa19d9e4a123b4dca61` | `PTM:PAGE:043` | Continua na página física 44. |
| [44](KA-200-B200-PTM.pdf#page=44) | 2-8 | 2 Electrical Power Systems | Revisada | `ae2d488f85cb605ad7e62172d86e1c3e4f23212a629c754c162d146bc7c6f57b` | `PTM:PAGE:044` | Texto cita BB-1098 (excluding BB-1096); página 12 cita prior to BB-1096. Divergência mantida. Continua na página física 45. Continuação da página física 43. |
| [45](KA-200-B200-PTM.pdf#page=45) | 2-9 | 2 Electrical Power Systems | Revisada | `2bc6d6243c4e16bfe9d82c25fb2ee1850a007711ffaa7f062af5285541709374` | `PTM:PAGE:045` | Continuação da página física 44. |
| [46](KA-200-B200-PTM.pdf#page=46) | 2-10 | 2 Electrical Power Systems | Revisada | `80ac8fb6a0613fa01744f6f72107b0a8f6b9b57bdbcfb6aa032e4adf8efc18b6` | `PTM:PAGE:046` | Figuras preservadas em imagem de apoio. |
| [47](KA-200-B200-PTM.pdf#page=47) | 2-11 | 2 Electrical Power Systems | Revisada | `189569ce6d3825b96d2f8378a0190b7a387147aa7393c474838bf86c71075f85` | `PTM:PAGE:047` | Continua na página física 48. |
| [48](KA-200-B200-PTM.pdf#page=48) | 2-12 | 2 Electrical Power Systems | Revisada | `ded39adb165530d7a6c79480ef2eea4b00e1a1832ffae81938465ad5d9b6a9c0` | `PTM:PAGE:048` | Legenda “B-2 THROUGH BB-1443, EXCEPT 1439” mantida como impressa. Continuação da página física 47. |
| [49](KA-200-B200-PTM.pdf#page=49) | 2-13 | 2 Electrical Power Systems | Revisada | `b15296fef710cd4996ed2a8e3f9069fed298b2527427b203d4db7a4fdbc6ea6d` | `PTM:PAGE:049` | Figuras preservadas em imagem de apoio. |
| [50](KA-200-B200-PTM.pdf#page=50) | 2-14 | 2 Electrical Power Systems | Revisada | `6ba5a7722d2807e2b46d3b0966ad9f18e8370ae125b884f020e5ea089d38d676` | `PTM:PAGE:050` | Rótulo “AVONICS” no diagrama preservado na imagem. |
| [51](KA-200-B200-PTM.pdf#page=51) | 2-15 | 2 Electrical Power Systems | Revisada | `8abc27534e49e1e4a9ed640777a0764d791b0bd402267f3fc8695c04538ecb27` | `PTM:PAGE:051` | Figuras preservadas em imagem de apoio. |
| [52](KA-200-B200-PTM.pdf#page=52) | 2-16 | 2 Electrical Power Systems | Revisada | `1135a97e374b1f9475af12eb34060407d0500259eff696003bd969c97eaf8026` | `PTM:PAGE:052` | Diagrama girado para leitura; nota de serialidade preservada no detalhe. |
| [53](KA-200-B200-PTM.pdf#page=53) | 2-17 | 2 Electrical Power Systems | Revisada | `bfc3ba1fc547191d0dca5271165dca1e8bde5508b1e5867aad8673af55fbaa27` | `PTM:PAGE:053` | Diagrama girado para leitura; notas de serialidade preservadas no detalhe. |
| [54](KA-200-B200-PTM.pdf#page=54) | 2-18 | 2 Electrical Power Systems | Revisada | `caac40d6e3c059ff837149bc441feb5fa76b201d433e18e194fe6b1aae2aa7f8` | `PTM:PAGE:054` | Faixa de seriais da legenda mantida, inclusive “BB-1449”. |
| [55](KA-200-B200-PTM.pdf#page=55) | 2-19 | 2 Electrical Power Systems | Revisada | `2e05cf86c9aac5ee66ab6d96abf8eb1a22e294773a342f8e612c0f45f4112aa6` | `PTM:PAGE:055` | Figuras preservadas em imagem de apoio. |
| [56](KA-200-B200-PTM.pdf#page=56) | 2-20 | 2 Electrical Power Systems | Revisada | `24f79730b6474488b967a2709056d44df8a2a87aa9dcc66c82d19c4c604ebd01` | `PTM:PAGE:056` | Figuras preservadas em imagem de apoio. |
| [57](KA-200-B200-PTM.pdf#page=57) | 2-21 | 2 Electrical Power Systems | Revisada | `76c4158f90469e4a698e3c3e2b7db3f91682718c22d44e8e37fb5b9c0d0b3f59` | `PTM:PAGE:057` | Figuras preservadas em imagem de apoio. |
| [58](KA-200-B200-PTM.pdf#page=58) | 2-22 | 2 Electrical Power Systems | Revisada | `60e54dcef673bbe5040cc0bd8040648254b3b3effbd1636fe182454164fe9043` | `PTM:PAGE:058` | Tabela 2-1: o segundo grupo não traz a linha “70 to 75%”; ausência mantida, sem interpolação. |
| [59](KA-200-B200-PTM.pdf#page=59) | 2-23 | 2 Electrical Power Systems | Revisada | `7fdb2b4edcf6c089f0457da97dff3570f296ac76db84dd805986765bf0ed061b` | `PTM:PAGE:059` | Texto conferido com a imagem. |
| [60](KA-200-B200-PTM.pdf#page=60) | 2-24 | 2 Electrical Power Systems | Revisada | `644c3a4bf56c1eb9ba3d6d14bae4edc2764cd17198bb44f4a9f39e154f37daf5` | `PTM:PAGE:060` | Mantidas as formas “BB 1-162” e “BB 163” como impressas. Continua na página física 61. |
| [61](KA-200-B200-PTM.pdf#page=61) | 2-25 | 2 Electrical Power Systems | Revisada | `16deb9aa01a937c43acaa211d6fc2a8e618975c3156ab9ed7ee0036775de8d33` | `PTM:PAGE:061` | Mantidas as faixas “BB 1-450” e “BB 450 AND SUBSEQUENT” como impressas. Continua na página física 62. Continuação da página física 60. |
| [62](KA-200-B200-PTM.pdf#page=62) | 2-26 | 2 Electrical Power Systems | Revisada | `e77a646f9d9df0f6a76884ba451c772baffe34085103587dcb2a08e4ba50229d` | `PTM:PAGE:062` | Continuação da página física 61. |
| [63](KA-200-B200-PTM.pdf#page=63) | 2-27 | 2 Electrical Power Systems | Revisada | `caede2adf6f77eb8cf4e8a9c7f7e2e6dca1ba713020c0a96a3a131164de58a2b` | `PTM:PAGE:063` | Tabela 2-4: “STALL WARN” associado a “FIREWALL VALVE SWITCH” como impresso; não corrigido. |
| [64](KA-200-B200-PTM.pdf#page=64) | 2-28 | 2 Electrical Power Systems | Revisada | `d4f570ae2c25e0b9352470b4deb069b270d0c93b7828c45ebfaf30c73bdb9768` | `PTM:PAGE:064` | Questões preservadas sem indicar respostas. |
| [65](KA-200-B200-PTM.pdf#page=65) | 2-29 | 2 Electrical Power Systems | Revisada | `318d1dd4e9da01d802a95d266d6172621c2086f024045c7f3fcd8bf47aa6b1ed` | `PTM:PAGE:065` | Questões preservadas sem indicar respostas. |
| [66](KA-200-B200-PTM.pdf#page=66) | 3-i | 3 Lighting | Revisada | `2ca7714fad46ea94f20bfa3231e21c49388286d14ee623d9cda4788493c0c89e` | `PTM:PAGE:066` | Texto conferido com a imagem. |
| [67](KA-200-B200-PTM.pdf#page=67) | 3-iii | 3 Lighting | Revisada | `7a3cc96766714c8093dc6b404c7e2ed45397259e62bbeed3cfd18b51d31e0838` | `PTM:PAGE:067` | Texto conferido com a imagem. |
| [68](KA-200-B200-PTM.pdf#page=68) | 3-1 | 3 Lighting | Revisada | `a9c837a9cdd2312bce5f379857e3583e9101d7cd3ad4a6fc10fe67e82cdadfa9` | `PTM:PAGE:068` | Figuras preservadas em imagem de apoio. |
| [69](KA-200-B200-PTM.pdf#page=69) | 3-2 | 3 Lighting | Revisada | `57bca3a6cb158736e97169f3de5c27d1ad9aa56b6cd7e69a59fe4562a771e9d2` | `PTM:PAGE:069` | Figuras preservadas em imagem de apoio. |
| [70](KA-200-B200-PTM.pdf#page=70) | 3-3 | 3 Lighting | Revisada | `c72b861cf35fc548e46daec28c136124a96cb8965105d4ca169987076bb41a94` | `PTM:PAGE:070` | Figuras preservadas em imagem de apoio. |
| [71](KA-200-B200-PTM.pdf#page=71) | 3-4 | 3 Lighting | Revisada | `059ffe0220e71998fe4c2eb3c07a66a76aa24649ac55a5bcb717f030f7d0407c` | `PTM:PAGE:071` | Figuras preservadas em imagem de apoio. |
| [72](KA-200-B200-PTM.pdf#page=72) | 3-5 | 3 Lighting | Revisada | `66319614211061148289e142432ee87222268114116efe62030b2c0ef0318bde` | `PTM:PAGE:072` | Figuras preservadas em imagem de apoio. |
| [73](KA-200-B200-PTM.pdf#page=73) | 3-6 | 3 Lighting | Revisada | `585f719788c2bc8bca498be0f846d9d4cb1205d6c4bb126ffb31668140515905` | `PTM:PAGE:073` | Figuras preservadas em imagem de apoio. |
| [74](KA-200-B200-PTM.pdf#page=74) | 3-7 | 3 Lighting | Revisada | `40a65168fc5be352c96745c7c386b99456dbb95b66e55de82ab068693107bc40` | `PTM:PAGE:074` | Figuras preservadas em imagem de apoio. |
| [75](KA-200-B200-PTM.pdf#page=75) | 3-8 | 3 Lighting | Revisada | `0bd6394978dcf24af202d86a3110aa6189cf3ccdf10a5a71ed2d4cc1198cf634` | `PTM:PAGE:075` | Figuras preservadas em imagem de apoio. |
| [76](KA-200-B200-PTM.pdf#page=76) | 3-9 | 3 Lighting | Revisada | `edbaffce1fe37584ecfcbaf179032c467a038a7c3e998b2779d4d385a35cc27d` | `PTM:PAGE:076` | Questões preservadas sem indicar respostas. |
| [77](KA-200-B200-PTM.pdf#page=77) | 4-i | 4 Master Warning Systems | Revisada | `a8bcc0bd03f6d3f2175c3d9f3f5810128cb083e00569203040ce43945e802796` | `PTM:PAGE:077` | Texto conferido com a imagem. |
| [78](KA-200-B200-PTM.pdf#page=78) | 4-iii | 4 Master Warning Systems | Revisada | `4dee2ef0437ecd1038dfe0149b764558bf52ca6dcc269b5be37c8b2097513d04` | `PTM:PAGE:078` | Lista de ilustrações mantém a ordem impressa 4-9 antes de 4-8. |
| [79](KA-200-B200-PTM.pdf#page=79) | 4-1 | 4 Master Warning Systems | Revisada | `7fe118055c8979aa5b7ffc4159ac31b558b4d105095a382b9eb5f06719e127f3` | `PTM:PAGE:079` | Figuras preservadas em imagem de apoio. |
| [80](KA-200-B200-PTM.pdf#page=80) | 4-2 | 4 Master Warning Systems | Revisada | `5d9ab86f747ff8dca06ef87a064340b431da4766ad5d7fbeb8c8a8b9aa738445` | `PTM:PAGE:080` | Figuras preservadas em imagem de apoio. |
| [81](KA-200-B200-PTM.pdf#page=81) | 4-3 | 4 Master Warning Systems | Revisada | `305c581d118b57f600f627f6c78f884a102bef8f024756be24eb5e1bcb4f71c6` | `PTM:PAGE:081` | Continua na página física 82. |
| [82](KA-200-B200-PTM.pdf#page=82) | 4-4 | 4 Master Warning Systems | Revisada | `ef541e0d9b624d8c12374f2907364f1d3b8683a9fb82472421da9d416af0e294` | `PTM:PAGE:082` | Continuação da página física 81. |
| [83](KA-200-B200-PTM.pdf#page=83) | 4-5 | 4 Master Warning Systems | Revisada | `e2b56f4b0b4697041d3acca4373081375f74f67539ea7ce632cb0e62118f67e9` | `PTM:PAGE:083` | Tabela 4-1 reconstruída; lentes vermelhas preservadas em imagem de apoio. |
| [84](KA-200-B200-PTM.pdf#page=84) | 4-6 | 4 Master Warning Systems | Revisada | `77be34aa7eb673bb829ee914060090de8490e19a27eeede5442e3add993988d2` | `PTM:PAGE:084` | Tabela 4-3 mantém pares impressos incomuns: DOOR UNLOCKED→altitude de cabine; ALT WARN→fogo motor direito. Não corrigido. |
| [85](KA-200-B200-PTM.pdf#page=85) | 4-7 | 4 Master Warning Systems | Revisada | `a51f2a4b5999137ef02daccfdb55158998921255df450b588923c9850ff65373` | `PTM:PAGE:085` | Continua na página física 86. |
| [86](KA-200-B200-PTM.pdf#page=86) | 4-8 | 4 Master Warning Systems | Revisada | `224291fc42eb72d76279a1cfa0ea054275a43d3c7c81ccf4eb2a02bcde090e92` | `PTM:PAGE:086` | Continuação da página física 85. |
| [87](KA-200-B200-PTM.pdf#page=87) | 4-9 | 4 Master Warning Systems | Revisada | `0d8fb78561ff80fe713b7f6a6f8dcd7d3ab07a2c49c62fd1916ba5762647fcb2` | `PTM:PAGE:087` | Mantido “deengergized”; introdução fala em warning annunciators, mas a tabela é caution advisory. |
| [88](KA-200-B200-PTM.pdf#page=88) | 4-10 | 4 Master Warning Systems | Revisada | `002a9825fa1f1ba5901357b79133c8f98c943a5dd54911bb0450ed82e5d067cc` | `PTM:PAGE:088` | Mantidos “deengergized” e “B-200”. |
| [89](KA-200-B200-PTM.pdf#page=89) | 4-11 | 4 Master Warning Systems | Revisada | `31a95548f468dc3b52d4b96bec69ec45bb00b3109cc84ffe63af835aa2eda5ee` | `PTM:PAGE:089` | Mantido “deengergized”. |
| [90](KA-200-B200-PTM.pdf#page=90) | 4-12 | 4 Master Warning Systems | Revisada | `2259c4d7811b9d397e59280d018562dc4e263f4e6c4f2e02216b0cd427ed087f` | `PTM:PAGE:090` | Questões preservadas sem indicar respostas. |
| [91](KA-200-B200-PTM.pdf#page=91) | 5-i | 5 Fuel System | Revisada | `a8953f8d3e00fe0e4e99bd8d41bc30d74db8e8624ed61b2fd22b9ddbc0028a27` | `PTM:PAGE:091` | Texto conferido com a imagem. |
| [92](KA-200-B200-PTM.pdf#page=92) | 5-ii | 5 Fuel System | Revisada | `4c9826b1d94733515974114f86ccb381860f7c57127db4caf548ee22367c085e` | `PTM:PAGE:092` | Texto conferido com a imagem. |
| [93](KA-200-B200-PTM.pdf#page=93) | 5-iii | 5 Fuel System | Revisada | `26b2d83316dbab7650db5fccf47bab48a4f62e71d402312d119f1039e55f89c7` | `PTM:PAGE:093` | Texto conferido com a imagem. |
| [94](KA-200-B200-PTM.pdf#page=94) | 5-1 | 5 Fuel System | Revisada | `93bdfc385790ec42069cbef26305e6f69d1fcf8209141383233ccc21ba63d101` | `PTM:PAGE:094` | Totais de combustível mantidos como impressos (386/158/544 gal; 2.586/1.058/3.644 lb). |
| [95](KA-200-B200-PTM.pdf#page=95) | 5-2 | 5 Fuel System | Revisada | `6f7babadad7c593bea262762099b37abcb3ab383dadbe490497ee069927c1ee5` | `PTM:PAGE:095` | Continua na página física 96. |
| [96](KA-200-B200-PTM.pdf#page=96) | 5-3 | 5 Fuel System | Revisada | `9724be69fd061d5e43af95c974c3947033c9bdc69a2bf9353a86eabe8dfc1142` | `PTM:PAGE:096` | Esquema colorido girado para leitura; legenda, símbolos e notas preservados no detalhe. Continuação da página física 95. |
| [97](KA-200-B200-PTM.pdf#page=97) | 5-4 | 5 Fuel System | Revisada | `073bb224b0a16f56182165bee0962e0f6a68c245c5862c2226ea888eba34530a` | `PTM:PAGE:097` | Esquema colorido girado para leitura; legenda, símbolos e notas preservados no detalhe. |
| [98](KA-200-B200-PTM.pdf#page=98) | 5-5 | 5 Fuel System | Revisada | `80f05d248034875c7a5763186b09f5728231f2bf6a3d090caffee856926556f7` | `PTM:PAGE:098` | Capacidades por célula preservadas no desenho; totais do texto não foram redistribuídos. Continua na página física 99. |
| [99](KA-200-B200-PTM.pdf#page=99) | 5-6 | 5 Fuel System | Revisada | `e8f456d435c572a92865c4c8c625ce58554938a6e317dec5f39ff5ef490084df` | `PTM:PAGE:099` | Mantida a referência “Service Bulletin 0703-286”. Continuação da página física 98. |
| [100](KA-200-B200-PTM.pdf#page=100) | 5-7 | 5 Fuel System | Revisada | `a11bd53408e495f010a54dbd730303805a57336f2b9bf295d4744545db1738de` | `PTM:PAGE:100` | Figuras preservadas em imagem de apoio. |
| [101](KA-200-B200-PTM.pdf#page=101) | 5-8 | 5 Fuel System | Revisada | `db132d1787d549c19362747d39cd04a9fee0488f6a700fa7641e422e67e6a119` | `PTM:PAGE:101` | Figura 5-6 mostra lente “L FUEL PRESS LO”; texto usa FUEL PRESS. Mantido. |
| [102](KA-200-B200-PTM.pdf#page=102) | 5-9 | 5 Fuel System | Revisada | `6d162fb1fa161f580d1e3498bc03f8170ceee7df33c131bbe2df91e4e6a6cc42` | `PTM:PAGE:102` | Faixas de seriais e alimentação dos medidores de fluxo mantidas; continua na p. 103. |
| [103](KA-200-B200-PTM.pdf#page=103) | 5-10 | 5 Fuel System | Revisada | `c85d9247f073f61c10fb8712779fcaf3ee54393353cf434a2252d78a6d165019` | `PTM:PAGE:103` | Aquecedor de combustível 70° a 90°F; nota da figura sobre BB-1401 preservada. Continua na página física 104. Continuação da página física 102. |
| [104](KA-200-B200-PTM.pdf#page=104) | 5-11 | 5 Fuel System | Revisada | `2d4b8dc8bfe197e820245bbaeff204b7375210dd4b7d19e6e456e2f2af525ed0` | `PTM:PAGE:104` | Crossfeed apenas com um motor inoperante conforme texto; continua na p. 105. Continuação da página física 103. |
| [105](KA-200-B200-PTM.pdf#page=105) | 5-12 | 5 Fuel System | Revisada | `832e5430e416f0614adcf941bdc1e11d46ef2dea2ebf4fb0df8e1203739dc33d` | `PTM:PAGE:105` | Capitalização “FUEL PRESSure” mantida. Continuação da página física 104. |
| [106](KA-200-B200-PTM.pdf#page=106) | 5-13 | 5 Fuel System | Revisada | `2a91de1f0c3afa36b9fa8e861abbbbd743557fae59481bccf5253689657c4b45` | `PTM:PAGE:106` | Tabela 5-1 reconstruída; “Aft” maiúsculo mantido. Continua na página física 107. |
| [107](KA-200-B200-PTM.pdf#page=107) | 5-14 | 5 Fuel System | Revisada | `41687b5acb9a96392f5525bef948c8bbe3549927eb33c5566759de648692e9cc` | `PTM:PAGE:107` | Gráfico preservado em imagem; nenhuma leitura foi interpolada. Concentração de aditivo 0.10%–0.15% mantida. Continua na página física 108. Continuação da página física 106. |
| [108](KA-200-B200-PTM.pdf#page=108) | 5-15 | 5 Fuel System | Revisada | `e0a0613f304be06a91d3d71cff537645375c1c9770ca92f8edae5a6dedcfa1b6` | `PTM:PAGE:108` | Referência “MEL-T-5624” mantida como impressa; pesos zero-fuel 10.400/11.000 lb. Continuação da página física 107. |
| [109](KA-200-B200-PTM.pdf#page=109) | 5-16 | 5 Fuel System | Revisada | `53fc4d3872800855f1eea40226e783f06a140f8053e88a89b3fc64fedaf086bd` | `PTM:PAGE:109` | Questões preservadas sem indicar respostas. |
| [110](KA-200-B200-PTM.pdf#page=110) | 6-i | 6 Auxiliary Power Systems | Revisada | `06a87612f1e98b39afe94d27f5cae8a2fa0020dc4c5eaded846845a412bdce5d` | `PTM:PAGE:110` | Capítulo 6 declara informação não aplicável; apenas página 6-i presente, sem 6-ii no PDF. |
| [111](KA-200-B200-PTM.pdf#page=111) | 7-i | 7 Powerplant | Revisada | `a6734f53c539c8156c4a0c69c3a516f9a99064b06df0dbcb77bd8825d2a6fe12` | `PTM:PAGE:111` | Texto conferido com a imagem. |
| [112](KA-200-B200-PTM.pdf#page=112) | 7-ii | 7 Powerplant | Revisada | `c6b26c8c320619c77e213973498bf0312da75c0c0b6fa475395579b1ac075004` | `PTM:PAGE:112` | Texto conferido com a imagem. |
| [113](KA-200-B200-PTM.pdf#page=113) | 7-iii | 7 Powerplant | Revisada | `21fc417ed1da7f24e9dba7aab4b15cd8226e98471c8a78776b1d351f48bdbbb6` | `PTM:PAGE:113` | Texto conferido com a imagem. |
| [114](KA-200-B200-PTM.pdf#page=114) | 7-v | 7 Powerplant | Revisada | `1623273f4cdc9232e59d89d6ae6395ca7e8c4540b715f4855f49441909d466aa` | `PTM:PAGE:114` | Índice mantém 7-14 antes de 7-13; página impressa 7-v (7-iv não presente no PDF). |
| [115](KA-200-B200-PTM.pdf#page=115) | 7-vi | 7 Powerplant | Revisada | `a2b4ddbdf18fe176de723054f747734a0606d673f489eaa01a818b056ba5b6ee` | `PTM:PAGE:115` | Índice mantém 7-34 antes de 7-33 e Table 7-2 antes de 7-1; títulos de aplicabilidade mantidos. |
| [116](KA-200-B200-PTM.pdf#page=116) | 7-1 | 7 Powerplant | Revisada | `e4d7ce8e285d4bb91ca7a90d01b4c6aaf06356e46354fbeea02e78e137651220` | `PTM:PAGE:116` | Valores declarados ilustrativos; não substituem o manual de voo aprovado. |
| [117](KA-200-B200-PTM.pdf#page=117) | 7-2 | 7 Powerplant | Revisada | `1a3cc914ae878cc7a1ff5004829a32da730265ee7a9d76ce812ba82f35c14756` | `PTM:PAGE:117` | Figuras preservadas em imagem de apoio. |
| [118](KA-200-B200-PTM.pdf#page=118) | 7-3 | 7 Powerplant | Revisada | `9364024b06ec011c7227684c4e7fcc3b6bcef2951cbc0d7cf172f46fe65ce70c` | `PTM:PAGE:118` | Figura 7-2 usa N<sub>G</sub>/N<sub>F</sub>; texto usa N<sub>1</sub>/NP. Ambas as notações preservadas. |
| [119](KA-200-B200-PTM.pdf#page=119) | 7-4 | 7 Powerplant | Revisada | `f7301e756d74e869f6e1442d9fff4b0babd7820affdf1d56cf154787a270019a` | `PTM:PAGE:119` | Figura girada para leitura; orientação original no fac-símile. |
| [120](KA-200-B200-PTM.pdf#page=120) | 7-5 | 7 Powerplant | Revisada | `c0635feeafb3e30fd93da933f04604cbd194dcaa08d896ae3082073ecbd68e26` | `PTM:PAGE:120` | Válvulas de sangria fecham acima de aproximadamente 90% N1. |
| [121](KA-200-B200-PTM.pdf#page=121) | 7-6 | 7 Powerplant | Revisada | `6eec4d6c2f6e3170631bca1687ff973ed28e6f2ecdfb3cd1d36118981f535f28` | `PTM:PAGE:121` | Texto conferido com a imagem. |
| [122](KA-200-B200-PTM.pdf#page=122) | 7-7 | 7 Powerplant | Revisada | `a57dd6fab44571cdf847b1f7d34c06c419c4e4724298ad928d44d7ec683dc144` | `PTM:PAGE:122` | Figuras preservadas em imagem de apoio. |
| [123](KA-200-B200-PTM.pdf#page=123) | 7-8 | 7 Powerplant | Revisada | `af5717ff493e724149217c1df2e06a96f274fe3552eb870e8261647527ee162b` | `PTM:PAGE:123` | Sistema de óleo e detecção de partículas preservados. |
| [124](KA-200-B200-PTM.pdf#page=124) | 7-9 | 7 Powerplant | Revisada | `210a9dc78454fe42170399a6811de93e13d08408c1aaed108208d026cd9851de` | `PTM:PAGE:124` | Figura 7-7 mostra CHIP DETECT em âmbar/vermelho conforme série. |
| [125](KA-200-B200-PTM.pdf#page=125) | 7-10 | 7 Powerplant | Revisada | `c41434cf880cc9110e68be339573183b2e699c74954c3cec7b7fc5b3a0f76e72` | `PTM:PAGE:125` | Esquema de óleo girado para leitura; legenda e cores preservadas. |
| [126](KA-200-B200-PTM.pdf#page=126) | 7-11 | 7 Powerplant | Revisada | `730edab8107874d83540151c45e5050943d1313f6482a08e7fe7df40770da717` | `PTM:PAGE:126` | Figuras preservadas em imagem de apoio. |
| [127](KA-200-B200-PTM.pdf#page=127) | 7-12 | 7 Powerplant | Revisada | `daba8040a073dd7264b73cca27205d520bcd995d278f5fe41bc20ed7b339a249` | `PTM:PAGE:127` | Esquema de combustível girado; notas BB-1401/BB-666 preservadas. |
| [128](KA-200-B200-PTM.pdf#page=128) | 7-13 | 7 Powerplant | Revisada | `d6f65b54c12263a3ac75be00fa3c46673e70eaa184c6ed2fe8e5ce4629011483` | `PTM:PAGE:128` | Início “aDownstream” mantido como impresso; texto continua após a figura da p. 129, na p. 130. |
| [129](KA-200-B200-PTM.pdf#page=129) | 7-14 | 7 Powerplant | Revisada | `fb45cfa0df85c8b3658b79c14815d5902c3f5848cb6260c76edb6bb1465c4109` | `PTM:PAGE:129` | Esquema FCU girado para leitura. |
| [130](KA-200-B200-PTM.pdf#page=130) | 7-15 | 7 Powerplant | Revisada | `f5ec25b9c2eb09ab7e7a3db39d340f1a0cfd679b29b2005d939c08f39797df4d` | `PTM:PAGE:130` | Continuação do texto da p. 128; fuel topping 106%/95% e autoignition 400 ft-lb mantidos. |
| [131](KA-200-B200-PTM.pdf#page=131) | 7-16 | 7 Powerplant | Revisada | `c35bfcf6eda7add9b3f59cea7877fb9370726528d3017953c2db5460e412b78c` | `PTM:PAGE:131` | Texto continua após a figura da p. 132, na p. 133. |
| [132](KA-200-B200-PTM.pdf#page=132) | 7-17 | 7 Powerplant | Revisada | `1ae276698000342cee7407dc7e0695e3ec1103aed8635ca9eabad86005d1b233` | `PTM:PAGE:132` | Figuras preservadas em imagem de apoio. |
| [133](KA-200-B200-PTM.pdf#page=133) | 7-18 | 7 Powerplant | Revisada | `982b408b36a5f77d59c906157c775c07dd927f09bd73148dcf7e6a886af27345` | `PTM:PAGE:133` | Grafia “B-1192” mantida; ângulos de pá por fabricante/série preservados. Continua na página física 134. Continuação da página física 131. |
| [134](KA-200-B200-PTM.pdf#page=134) | 7-19 | 7 Powerplant | Revisada | `f17b783d5e19da19e484361c4541e5c809e6f3bf4554ab4343aa5c30acafc27e` | `PTM:PAGE:134` | Overspeed 2.120/2.080 rpm e teste 1.830–1.910 rpm mantidos. Continua na página física 135. Continuação da página física 133. |
| [135](KA-200-B200-PTM.pdf#page=135) | 7-20 | 7 Powerplant | Revisada | `a0eec0cb5795bb47e644941210111daa6c64965cf3c5704c71c56ba4019529e8` | `PTM:PAGE:135` | Limite de reverso 1.900 rpm e comandos 83%±5%, –9°/–10°, 95% mantidos. Continuação da página física 134. |
| [136](KA-200-B200-PTM.pdf#page=136) | 7-21 | 7 Powerplant | Revisada | `e48a79f89ac53db5cdae9f0bff5046b107d4805b4bc811923a16977a91f18631` | `PTM:PAGE:136` | Texto conferido com a imagem. |
| [137](KA-200-B200-PTM.pdf#page=137) | 7-22 | 7 Powerplant | Revisada | `58dadd655e5383b7fce865f445fdab1f13c8a3ee33b678d94aadec79d04f91b6` | `PTM:PAGE:137` | Figuras preservadas em imagem de apoio. |
| [138](KA-200-B200-PTM.pdf#page=138) | 7-23 | 7 Powerplant | Revisada | `893473058ebc262a89b9d6c5a4d5df461eb61639227e04131fad946489207a84` | `PTM:PAGE:138` | LOW IDLE 61%/56%/52% conforme série/motor; mantido. Continua na página física 140. |
| [139](KA-200-B200-PTM.pdf#page=139) | 7-24 | 7 Powerplant | Revisada | `89ca65b0b65a603e0848a8674ceed864093118f8f462b5b555bdf017db7199dc` | `PTM:PAGE:139` | Figuras preservadas em imagem de apoio. |
| [140](KA-200-B200-PTM.pdf#page=140) | 7-25 | 7 Powerplant | Revisada | `f8412f22ed247aadfa493fe34f854e6f107f369ba9e91f59f3c1ccad4eb7f179` | `PTM:PAGE:140` | Figura 7-23 mostra 2.080 rpm normal e ~1.870 rpm em teste; não harmonizado com o texto. Continuação da página física 138. |
| [141](KA-200-B200-PTM.pdf#page=141) | 7-26 | 7 Powerplant | Revisada | `1cef05787c0fad41bc818cdeba71645c077060915fee7a0e222965b89ee7d4e3` | `PTM:PAGE:141` | Texto remete ITT a “Figure 7-27”, mas a figura dos gages ITT é 7-26; mantido. |
| [142](KA-200-B200-PTM.pdf#page=142) | 7-27 | 7 Powerplant | Revisada | `9962030ca07e2913d77c5d5eec5b777de63afe62a2e13d11fc998eee5d9e6b58` | `PTM:PAGE:142` | Torque limiter 2.368–2.447 ft-lb e máximo certificado 2.230 ft-lb mantidos. |
| [143](KA-200-B200-PTM.pdf#page=143) | 7-28 | 7 Powerplant | Revisada | `b93b07abe96a07d6a7ffaba9896f60f1b00b4e37c0986f05392901ab49828a51` | `PTM:PAGE:143` | Redação sobre alimentação dos gages N1 “prior to BB-1484 including BB-1485” mantida. |
| [144](KA-200-B200-PTM.pdf#page=144) | 7-29 | 7 Powerplant | Revisada | `87aba73d73ff90975d34974518092db8eb44b4fae57a3a0a175963efbae8ac5c` | `PTM:PAGE:144` | Figuras preservadas em imagem de apoio. |
| [145](KA-200-B200-PTM.pdf#page=145) | 7-30 | 7 Powerplant | Revisada | `775b1a4c8630d7b07b5db1ba42858dfbaa0067233341b8c874a47fd78d35d084` | `PTM:PAGE:145` | Figuras preservadas em imagem de apoio. |
| [146](KA-200-B200-PTM.pdf#page=146) | 7-31 | 7 Powerplant | Revisada | `ed72ae2c37063477a588cb290b5c7d1aa96da144f46c60d27d13eb39caf0e06c` | `PTM:PAGE:146` | Figuras preservadas em imagem de apoio. |
| [147](KA-200-B200-PTM.pdf#page=147) | 7-32 | 7 Powerplant | Revisada | `5b1ae1efb3f127e5cec4264c546fea9249d273cea303ac1072364a8a89961c9b` | `PTM:PAGE:147` | Texto de indicação remete a “Figure 7-35”, mas as luzes aparecem na Figure 7-36; mantido. |
| [148](KA-200-B200-PTM.pdf#page=148) | 7-33 | 7 Powerplant | Revisada | `c93d489aedf40c1b359e28a9488e5e40714d637ef3d64398612f9bbfd8c0ba9f` | `PTM:PAGE:148` | Autofeather: limiares 400/200 ft-lb preservados. |
| [149](KA-200-B200-PTM.pdf#page=149) | 7-34 | 7 Powerplant | Revisada | `b6f1b8834d6e850454c4617092ccddfebf7087547508f3a226a7c4a3cfb80016` | `PTM:PAGE:149` | Nota sobre LOW IDLE e teste; desbandeiramento ~18° preservado. |
| [150](KA-200-B200-PTM.pdf#page=150) | 7-35 | 7 Powerplant | Revisada | `a0f63153ae88934cb82674ce438478b6c0100722373677205ec997bd09faee1f` | `PTM:PAGE:150` | Tabelas 7-1/7-2 reconstruídas; título da 7-2 (“PRIOR TO BB-1439, 1444 AND SUBSEQUENT”) mantido como impresso. |
| [151](KA-200-B200-PTM.pdf#page=151) | 7-36 | 7 Powerplant | Revisada | `8ee5e766d9c156e4f32e39a783bd0a278e1f9cb9fe0ea50d02fffaf4ce091e45` | `PTM:PAGE:151` | Tabela 7-3 e 13 notas preservadas; nota 12 sem marcador visível nas tabelas; óleo 0–99°C em cruise climb mantido. |
| [152](KA-200-B200-PTM.pdf#page=152) | 7-37 | 7 Powerplant | Revisada | `b8b47d784ceb5f6f46777554fd95275231c4df3076427ade7198f9b46bf6ee29` | `PTM:PAGE:152` | Diâmetros de hélice e limites de partida preservados; repetição “Rotational Speed Limits” mantida. |
| [153](KA-200-B200-PTM.pdf#page=153) | 7-38 | 7 Powerplant | Revisada | `a0f5d709d588a1b7cdaf128e4fa043d198b79193d326a11b06f74b3dd2455800` | `PTM:PAGE:153` | Tabela 7-4: terceiro grupo tem apenas ITT e torquímetro; “extends form” mantido como impresso. |
| [154](KA-200-B200-PTM.pdf#page=154) | 7-39 | 7 Powerplant | Revisada | `6fed3dcdc530677f3f20bca819c0ebd6504f120d6800b130cea1190e26325f75` | `PTM:PAGE:154` | Questões preservadas sem indicar respostas. |
| [155](KA-200-B200-PTM.pdf#page=155) | 7-40 | 7 Powerplant | Revisada | `7e8284170850c7be144bc20ba7180b2854b327e58a744387f08dcee111804338` | `PTM:PAGE:155` | Questões preservadas sem indicar respostas. |
| [156](KA-200-B200-PTM.pdf#page=156) | 8-i | 8 Fire Protection | Revisada | `f059ea86738f0cdda305cb3ab82cee6dddf3f8215ce29fe6a03fb7f535975c1f` | `PTM:PAGE:156` | Texto conferido com a imagem. |
| [157](KA-200-B200-PTM.pdf#page=157) | 8-iii | 8 Fire Protection | Revisada | `8bbe3f152dc69c923319f1c93f9c7c8903756b008302c05ff2490d51a4423a7d` | `PTM:PAGE:157` | Índice do capítulo 8; página 8-ii não presente no PDF. |
| [158](KA-200-B200-PTM.pdf#page=158) | 8-1 | 8 Fire Protection | Revisada | `742159df4a5c8933037be11d951d931a7932284317377fdd9246dcd0d4510fc6` | `PTM:PAGE:158` | Figuras preservadas em imagem de apoio. |
| [159](KA-200-B200-PTM.pdf#page=159) | 8-2 | 8 Fire Protection | Revisada | `4ddd473dee010d136adc95e14d20d34b28b44bdd5c2e767d18fb09d559155ed0` | `PTM:PAGE:159` | Rótulo “DETAL B” mantido na imagem. |
| [160](KA-200-B200-PTM.pdf#page=160) | 8-3 | 8 Fire Protection | Revisada | `dbfd45dd7f5e5e00af000790c202310ce7ba3c8b380dbf3bac42b00041d1af76` | `PTM:PAGE:160` | Rótulo “DETAL B” mantido na imagem. |
| [161](KA-200-B200-PTM.pdf#page=161) | 8-4 | 8 Fire Protection | Revisada | `85c3b3712ca09e82278755f16604ee04498095afcece31fe040052d2c5e08afe` | `PTM:PAGE:161` | Agente CBrF3 e alimentação pelo hot battery bus preservados. |
| [162](KA-200-B200-PTM.pdf#page=162) | 8-5 | 8 Fire Protection | Revisada | `5b80a14a57d2f3d1147ae0e553a5bc26170143455df788fcf9ad8dcbca53f501` | `PTM:PAGE:162` | Rótulo “DETAL B” mantido na imagem. |
| [163](KA-200-B200-PTM.pdf#page=163) | 8-6 | 8 Fire Protection | Revisada | `31a862c8b1dd685dc6ecfc5004109075ea23a2c67b98465c9384210672fdd30b` | `PTM:PAGE:163` | Tabela 8-1 reconstruída; pares temperatura/pressão conferidos em detalhe. |
| [164](KA-200-B200-PTM.pdf#page=164) | 8-7 | 8 Fire Protection | Revisada | `29a7ec58aa5e60221a30208c74d892a0b1b121c17f0b489360e14858ef03c7e3` | `PTM:PAGE:164` | Figuras preservadas em imagem de apoio. |
| [165](KA-200-B200-PTM.pdf#page=165) | 8-8 | 8 Fire Protection | Revisada | `cb1bddad566bd2ea766b088b5c1c8c3d7a328d283a2214f72be910a167b95647` | `PTM:PAGE:165` | Questões preservadas sem indicar respostas. |
| [166](KA-200-B200-PTM.pdf#page=166) | 9-i | 9 Pneumatics | Revisada | `ea9ad6779bdbfb82fb0cade784b905009a85165a0093be97a311ef6488ee5c38` | `PTM:PAGE:166` | Texto conferido com a imagem. |
| [167](KA-200-B200-PTM.pdf#page=167) | 9-iii | 9 Pneumatics | Revisada | `a3c008721d28e07dec5f5959f23d9791d2bb6a4e0716087e066c00bba89f046f` | `PTM:PAGE:167` | Índice mantém Figure 9-6 antes de 9-5; página 9-ii não presente no PDF. |
| [168](KA-200-B200-PTM.pdf#page=168) | 9-1 | 9 Pneumatics | Revisada | `bfad808003dd32d5c999a5acaa6434e315db8ae077e029ad6102cf64e6166fa9` | `PTM:PAGE:168` | Figuras preservadas em imagem de apoio. |
| [169](KA-200-B200-PTM.pdf#page=169) | 9-2 | 9 Pneumatics | Revisada | `38b54d97ebd2308424faa47e145f117f9c764fd3ae7425c74a617472eea9da1e` | `PTM:PAGE:169` | Figuras preservadas em imagem de apoio. |
| [170](KA-200-B200-PTM.pdf#page=170) | 9-3 | 9 Pneumatics | Revisada | `32386fede22d54c03bf479a17526a6107d8751490cfeb235d853ca16b19757d2` | `PTM:PAGE:170` | Efeitos de vazamento de sangria em torque/ITT mantidos como impressos. |
| [171](KA-200-B200-PTM.pdf#page=171) | 9-4 | 9 Pneumatics | Revisada | `481957ae513623405dd984504f6d63cf4f67a5fca8a9ab9c0c73b3d4d8d2e84b` | `PTM:PAGE:171` | Figuras preservadas em imagem de apoio. |
| [172](KA-200-B200-PTM.pdf#page=172) | 9-5 | 9 Pneumatics | Revisada | `9a857ead1cd435812e3b6fa307e729c06d1840745b69365fcb74323eabe5bd42` | `PTM:PAGE:172` | Nota: anunciador de sangria não apaga após fechar válvulas; mantida. |
| [173](KA-200-B200-PTM.pdf#page=173) | 9-6 | 9 Pneumatics | Revisada | `94af11379f78b9f3cdd5c6d0784ba2193fd8a3b570b2dfa2b47cdd8ed6681e09` | `PTM:PAGE:173` | Diagrama girado para leitura; temporização 6–8 s preservada. |
| [174](KA-200-B200-PTM.pdf#page=174) | 9-7 | 9 Pneumatics | Revisada | `8bb304b60d037602fb9ac19fc6d09132c6d5a025e068832e7e2753c6a20e35cc` | `PTM:PAGE:174` | Limites pneumáticos 12–20 psi e faixas de vácuo preservados. |
| [175](KA-200-B200-PTM.pdf#page=175) | 9-8 | 9 Pneumatics | Revisada | `ea517b36b6124f576b1d5f823bb00d0adc6b69195756750e5e4a863adfc22312` | `PTM:PAGE:175` | Questões preservadas sem indicar respostas. |
| [176](KA-200-B200-PTM.pdf#page=176) | 10-i | 10 Ice and Rain Protection | Revisada | `4598adb9dafaf26573c92cf7a5308d3001ec9222bc93107ea2337c2ef1c21935` | `PTM:PAGE:176` | Texto conferido com a imagem. |
| [177](KA-200-B200-PTM.pdf#page=177) | 10-ii | 10 Ice and Rain Protection | Revisada | `749d04b84a2fab40106737313661756b8939300dfa03c4221dfbccd83a6b7513` | `PTM:PAGE:177` | Texto conferido com a imagem. |
| [178](KA-200-B200-PTM.pdf#page=178) | 10-iii | 10 Ice and Rain Protection | Revisada | `a9d618ad98384cc34cc6fa83afdae5fdf30904bcb6307b8980c564b417c002ef` | `PTM:PAGE:178` | Texto conferido com a imagem. |
| [179](KA-200-B200-PTM.pdf#page=179) | 10-1 | 10 Ice and Rain Protection | Revisada | `4337ce6168f7c74610e8e3e03de410a6baa14c2e7ab5a693392d5f05cfa8add8` | `PTM:PAGE:179` | Figuras preservadas em imagem de apoio. |
| [180](KA-200-B200-PTM.pdf#page=180) | 10-2 | 10 Ice and Rain Protection | Revisada | `6d29d9dea82a3dd01135f17f872b1a948db78376efc149986917c026dca7cafc` | `PTM:PAGE:180` | Aviso sobre botas insufladas e OAT abaixo de –40°C preservado. |
| [181](KA-200-B200-PTM.pdf#page=181) | 10-3 | 10 Ice and Rain Protection | Revisada | `c4f4b717cce173d20726ac76d3053d3794e1567616df1d4b8d8d87c9d7ddf1f0` | `PTM:PAGE:181` | Figuras preservadas em imagem de apoio. |
| [182](KA-200-B200-PTM.pdf#page=182) | 10-4 | 10 Ice and Rain Protection | Revisada | `ca77878e919e94e884c252b2473e9daccb55baa276f81254ef4b20d44f3f16d9` | `PTM:PAGE:182` | Figuras preservadas em imagem de apoio. |
| [183](KA-200-B200-PTM.pdf#page=183) | 10-5 | 10 Ice and Rain Protection | Revisada | `4c197a694668663e1b516979e70acf4c2506628e9bcebe603dfbf5cdadc894c6` | `PTM:PAGE:183` | Ciclo SINGLE: 6 s asas, 4 s estabilizador; preservado. |
| [184](KA-200-B200-PTM.pdf#page=184) | 10-6 | 10 Ice and Rain Protection | Revisada | `d37c859508a717604d47081cec0136c5b7742a42689d55f2db984ccec5d19c4b` | `PTM:PAGE:184` | Brake deice: 85% N1 e.timer 10 min preservados. Continua na página física 185. |
| [185](KA-200-B200-PTM.pdf#page=185) | 10-7 | 10 Ice and Rain Protection | Revisada | `9737bfad72cc4d1de5e7206060cd45e259d5c3296c73e3225ff8f34e606e185e` | `PTM:PAGE:185` | Windshield heat +95°F a +105°F preservado. Continuação da página física 184. |
| [186](KA-200-B200-PTM.pdf#page=186) | 10-8 | 10 Ice and Rain Protection | Revisada | `d4b6498807dd445b7d2767657cbf4ac1ebb548a6136baadcb1ccfed091621798` | `PTM:PAGE:186` | Figura 10-6 mostra sensor “95° TO 105°” sem unidade F; texto usa °F. |
| [187](KA-200-B200-PTM.pdf#page=187) | 10-9 | 10 Ice and Rain Protection | Revisada | `3e26c985197a708cff55e85d68623000bde56e393f05c335e4926e648f101533` | `PTM:PAGE:187` | Sequências de aquecimento 90 s/30 s e redação “prior to BB-2 through...” mantidas. Continua na página física 188. |
| [188](KA-200-B200-PTM.pdf#page=188) | 10-10 | 10 Ice and Rain Protection | Revisada | `42af4b8c34a932dd1668f895888d3b989bb91178d389db7f8272eda7a6d2717f` | `PTM:PAGE:188` | PROP AMPS 18–24 A (4 pás) / 14–18 A (3 pás); modo manual não registra no amperímetro. Continuação da página física 187. |
| [189](KA-200-B200-PTM.pdf#page=189) | 10-11 | 10 Ice and Rain Protection | Revisada | `79636dddc8f01303fd6052466c84128d4839fbbd05313ff9033cc132fc6096b1` | `PTM:PAGE:189` | Avisos sobre pitot/stall warning heat no solo preservados; continua na p. 190. |
| [190](KA-200-B200-PTM.pdf#page=190) | 10-12 | 10 Ice and Rain Protection | Revisada | `31aa5ec7f83a23797f3cb61711931aa7d665cda42fd66c0939a6ddfec0e6f55d` | `PTM:PAGE:190` | Aquecimento de vent e FCU preservados; continua na p. 191. Continuação da página física 189. |
| [191](KA-200-B200-PTM.pdf#page=191) | 10-13 | 10 Ice and Rain Protection | Revisada | `76c1a952242e9c5913a4b988800c37c92c5ff46ae661fda3d8bb90e46110c792` | `PTM:PAGE:191` | Ice vanes: 15 s, 160 knots; aviso continua após figuras 10-11/10-12, na p. 194. Continuação da página física 190. |
| [192](KA-200-B200-PTM.pdf#page=192) | 10-14 | 10 Ice and Rain Protection | Revisada | `7881c1c1ac499808b10f27c86a575276bf47d734055f408b77928d7197d54048` | `PTM:PAGE:192` | Figuras preservadas em imagem de apoio. |
| [193](KA-200-B200-PTM.pdf#page=193) | 10-15 | 10 Ice and Rain Protection | Revisada | `1dd7d7fe19cf45f3ad9e7129a94e8fd28af1ac61b30589afac2017caec609402` | `PTM:PAGE:193` | Figuras preservadas em imagem de apoio. |
| [194](KA-200-B200-PTM.pdf#page=194) | 10-16 | 10 Ice and Rain Protection | Revisada | `2ac4237262f97f5341096307c8d466efc2babb14edc81acfdbe083f977a994a8` | `PTM:PAGE:194` | Continuação do aviso da p. 191; +5°C/+15°C e perda de torque preservados. |
| [195](KA-200-B200-PTM.pdf#page=195) | 10-17 | 10 Ice and Rain Protection | Revisada | `663dcb6db93eb61ebd30d0da44ff9439700b56ff2c4f34b7271239a06a4ade48` | `PTM:PAGE:195` | Wipers não operar em vidro seco; limitações de gelo continuam na p. 196. |
| [196](KA-200-B200-PTM.pdf#page=196) | 10-18 | 10 Ice and Rain Protection | Revisada | `0c85e602cff6d9b25ac482447ffa6649da130952b93d3dcafede5cd433f47d28` | `PTM:PAGE:196` | Limites 140 KIAS mínimo e 226 KIAS máximo efetivo preservados. Continua na página física 197. Continuação da página física 195. |
| [197](KA-200-B200-PTM.pdf#page=197) | 10-19 | 10 Ice and Rain Protection | Revisada | `c59a4f05aff99a2d14e1c4cab5b4f95104ddb78357ef34ce9f3d390d9c397ba8` | `PTM:PAGE:197` | Avisos de gelo, wipers e hélice estática preservados. Continua na página física 198. Continuação da página física 196. |
| [198](KA-200-B200-PTM.pdf#page=198) | 10-20 | 10 Ice and Rain Protection | Revisada | `2a1632d6139943e3e8e2b2c738ad2415619608ceb41e1b1356b457b978a7e3e9` | `PTM:PAGE:198` | NOTES de backup manual 90 s/30 s e deflexão ~5% preservadas. Continuação da página física 197. |
| [199](KA-200-B200-PTM.pdf#page=199) | 10-21 | 10 Ice and Rain Protection | Revisada | `a7db154a9b8730639a5bdbab99f7c747b442c10d0223c8ecb65858b23645e7bc` | `PTM:PAGE:199` | Questões preservadas sem indicar respostas. |
| [200](KA-200-B200-PTM.pdf#page=200) | 10-22 | 10 Ice and Rain Protection | Revisada | `0bd82cbf613d1892eb18f8365e959b08ada106291ead55868321e96705d15f70` | `PTM:PAGE:200` | Questão 12 alternativa D termina em “Indication speeds” como impresso; nada acrescentado. |
| [201](KA-200-B200-PTM.pdf#page=201) | — | 11 Air-Conditioning System | Pendente | `—` | `PTM:PAGE:201` | Aguardando lote autorizado. |
| [202](KA-200-B200-PTM.pdf#page=202) | — | 11 Air-Conditioning System | Pendente | `—` | `PTM:PAGE:202` | Aguardando lote autorizado. |
| [203](KA-200-B200-PTM.pdf#page=203) | — | 11 Air-Conditioning System | Pendente | `—` | `PTM:PAGE:203` | Aguardando lote autorizado. |
| [204](KA-200-B200-PTM.pdf#page=204) | — | 11 Air-Conditioning System | Pendente | `—` | `PTM:PAGE:204` | Aguardando lote autorizado. |
| [205](KA-200-B200-PTM.pdf#page=205) | — | 11 Air-Conditioning System | Pendente | `—` | `PTM:PAGE:205` | Aguardando lote autorizado. |
| [206](KA-200-B200-PTM.pdf#page=206) | — | 11 Air-Conditioning System | Pendente | `—` | `PTM:PAGE:206` | Aguardando lote autorizado. |
| [207](KA-200-B200-PTM.pdf#page=207) | — | 11 Air-Conditioning System | Pendente | `—` | `PTM:PAGE:207` | Aguardando lote autorizado. |
| [208](KA-200-B200-PTM.pdf#page=208) | — | 11 Air-Conditioning System | Pendente | `—` | `PTM:PAGE:208` | Aguardando lote autorizado. |
| [209](KA-200-B200-PTM.pdf#page=209) | — | 11 Air-Conditioning System | Pendente | `—` | `PTM:PAGE:209` | Aguardando lote autorizado. |
| [210](KA-200-B200-PTM.pdf#page=210) | — | 11 Air-Conditioning System | Pendente | `—` | `PTM:PAGE:210` | Aguardando lote autorizado. |
| [211](KA-200-B200-PTM.pdf#page=211) | — | 11 Air-Conditioning System | Pendente | `—` | `PTM:PAGE:211` | Aguardando lote autorizado. |
| [212](KA-200-B200-PTM.pdf#page=212) | — | 11 Air-Conditioning System | Pendente | `—` | `PTM:PAGE:212` | Aguardando lote autorizado. |
| [213](KA-200-B200-PTM.pdf#page=213) | — | 11 Air-Conditioning System | Pendente | `—` | `PTM:PAGE:213` | Aguardando lote autorizado. |
| [214](KA-200-B200-PTM.pdf#page=214) | — | 11 Air-Conditioning System | Pendente | `—` | `PTM:PAGE:214` | Aguardando lote autorizado. |
| [215](KA-200-B200-PTM.pdf#page=215) | — | 11 Air-Conditioning System | Pendente | `—` | `PTM:PAGE:215` | Aguardando lote autorizado. |
| [216](KA-200-B200-PTM.pdf#page=216) | — | 12 Pressurization | Pendente | `—` | `PTM:PAGE:216` | Aguardando lote autorizado. |
| [217](KA-200-B200-PTM.pdf#page=217) | — | 12 Pressurization | Pendente | `—` | `PTM:PAGE:217` | Aguardando lote autorizado. |
| [218](KA-200-B200-PTM.pdf#page=218) | — | 12 Pressurization | Pendente | `—` | `PTM:PAGE:218` | Aguardando lote autorizado. |
| [219](KA-200-B200-PTM.pdf#page=219) | — | 12 Pressurization | Pendente | `—` | `PTM:PAGE:219` | Aguardando lote autorizado. |
| [220](KA-200-B200-PTM.pdf#page=220) | — | 12 Pressurization | Pendente | `—` | `PTM:PAGE:220` | Aguardando lote autorizado. |
| [221](KA-200-B200-PTM.pdf#page=221) | — | 12 Pressurization | Pendente | `—` | `PTM:PAGE:221` | Aguardando lote autorizado. |
| [222](KA-200-B200-PTM.pdf#page=222) | — | 12 Pressurization | Pendente | `—` | `PTM:PAGE:222` | Aguardando lote autorizado. |
| [223](KA-200-B200-PTM.pdf#page=223) | — | 12 Pressurization | Pendente | `—` | `PTM:PAGE:223` | Aguardando lote autorizado. |
| [224](KA-200-B200-PTM.pdf#page=224) | — | 12 Pressurization | Pendente | `—` | `PTM:PAGE:224` | Aguardando lote autorizado. |
| [225](KA-200-B200-PTM.pdf#page=225) | — | 12 Pressurization | Pendente | `—` | `PTM:PAGE:225` | Aguardando lote autorizado. |
| [226](KA-200-B200-PTM.pdf#page=226) | — | 12 Pressurization | Pendente | `—` | `PTM:PAGE:226` | Aguardando lote autorizado. |
| [227](KA-200-B200-PTM.pdf#page=227) | — | 12 Pressurization | Pendente | `—` | `PTM:PAGE:227` | Aguardando lote autorizado. |
| [228](KA-200-B200-PTM.pdf#page=228) | — | 13 Hydraulic Power Systems | Pendente | `—` | `PTM:PAGE:228` | Aguardando lote autorizado. |
| [229](KA-200-B200-PTM.pdf#page=229) | — | 14 Landing Gear and Brakes | Pendente | `—` | `PTM:PAGE:229` | Aguardando lote autorizado. |
| [230](KA-200-B200-PTM.pdf#page=230) | — | 14 Landing Gear and Brakes | Pendente | `—` | `PTM:PAGE:230` | Aguardando lote autorizado. |
| [231](KA-200-B200-PTM.pdf#page=231) | — | 14 Landing Gear and Brakes | Pendente | `—` | `PTM:PAGE:231` | Aguardando lote autorizado. |
| [232](KA-200-B200-PTM.pdf#page=232) | — | 14 Landing Gear and Brakes | Pendente | `—` | `PTM:PAGE:232` | Aguardando lote autorizado. |
| [233](KA-200-B200-PTM.pdf#page=233) | — | 14 Landing Gear and Brakes | Pendente | `—` | `PTM:PAGE:233` | Aguardando lote autorizado. |
| [234](KA-200-B200-PTM.pdf#page=234) | — | 14 Landing Gear and Brakes | Pendente | `—` | `PTM:PAGE:234` | Aguardando lote autorizado. |
| [235](KA-200-B200-PTM.pdf#page=235) | — | 14 Landing Gear and Brakes | Pendente | `—` | `PTM:PAGE:235` | Aguardando lote autorizado. |
| [236](KA-200-B200-PTM.pdf#page=236) | — | 14 Landing Gear and Brakes | Pendente | `—` | `PTM:PAGE:236` | Aguardando lote autorizado. |
| [237](KA-200-B200-PTM.pdf#page=237) | — | 14 Landing Gear and Brakes | Pendente | `—` | `PTM:PAGE:237` | Aguardando lote autorizado. |
| [238](KA-200-B200-PTM.pdf#page=238) | — | 14 Landing Gear and Brakes | Pendente | `—` | `PTM:PAGE:238` | Aguardando lote autorizado. |
| [239](KA-200-B200-PTM.pdf#page=239) | — | 14 Landing Gear and Brakes | Pendente | `—` | `PTM:PAGE:239` | Aguardando lote autorizado. |
| [240](KA-200-B200-PTM.pdf#page=240) | — | 14 Landing Gear and Brakes | Pendente | `—` | `PTM:PAGE:240` | Aguardando lote autorizado. |
| [241](KA-200-B200-PTM.pdf#page=241) | — | 14 Landing Gear and Brakes | Pendente | `—` | `PTM:PAGE:241` | Aguardando lote autorizado. |
| [242](KA-200-B200-PTM.pdf#page=242) | — | 14 Landing Gear and Brakes | Pendente | `—` | `PTM:PAGE:242` | Aguardando lote autorizado. |
| [243](KA-200-B200-PTM.pdf#page=243) | — | 14 Landing Gear and Brakes | Pendente | `—` | `PTM:PAGE:243` | Aguardando lote autorizado. |
| [244](KA-200-B200-PTM.pdf#page=244) | — | 14 Landing Gear and Brakes | Pendente | `—` | `PTM:PAGE:244` | Aguardando lote autorizado. |
| [245](KA-200-B200-PTM.pdf#page=245) | — | 14 Landing Gear and Brakes | Pendente | `—` | `PTM:PAGE:245` | Aguardando lote autorizado. |
| [246](KA-200-B200-PTM.pdf#page=246) | — | 14 Landing Gear and Brakes | Pendente | `—` | `PTM:PAGE:246` | Aguardando lote autorizado. |
| [247](KA-200-B200-PTM.pdf#page=247) | — | 14 Landing Gear and Brakes | Pendente | `—` | `PTM:PAGE:247` | Aguardando lote autorizado. |
| [248](KA-200-B200-PTM.pdf#page=248) | — | 14 Landing Gear and Brakes | Pendente | `—` | `PTM:PAGE:248` | Aguardando lote autorizado. |
| [249](KA-200-B200-PTM.pdf#page=249) | — | 14 Landing Gear and Brakes | Pendente | `—` | `PTM:PAGE:249` | Aguardando lote autorizado. |
| [250](KA-200-B200-PTM.pdf#page=250) | — | 14 Landing Gear and Brakes | Pendente | `—` | `PTM:PAGE:250` | Aguardando lote autorizado. |
| [251](KA-200-B200-PTM.pdf#page=251) | — | 14 Landing Gear and Brakes | Pendente | `—` | `PTM:PAGE:251` | Aguardando lote autorizado. |
| [252](KA-200-B200-PTM.pdf#page=252) | — | 14 Landing Gear and Brakes | Pendente | `—` | `PTM:PAGE:252` | Aguardando lote autorizado. |
| [253](KA-200-B200-PTM.pdf#page=253) | — | 14 Landing Gear and Brakes | Pendente | `—` | `PTM:PAGE:253` | Aguardando lote autorizado. |
| [254](KA-200-B200-PTM.pdf#page=254) | — | 14 Landing Gear and Brakes | Pendente | `—` | `PTM:PAGE:254` | Aguardando lote autorizado. |
| [255](KA-200-B200-PTM.pdf#page=255) | — | 14 Landing Gear and Brakes | Pendente | `—` | `PTM:PAGE:255` | Aguardando lote autorizado. |
| [256](KA-200-B200-PTM.pdf#page=256) | — | 14 Landing Gear and Brakes | Pendente | `—` | `PTM:PAGE:256` | Aguardando lote autorizado. |
| [257](KA-200-B200-PTM.pdf#page=257) | — | 14 Landing Gear and Brakes | Pendente | `—` | `PTM:PAGE:257` | Aguardando lote autorizado. |
| [258](KA-200-B200-PTM.pdf#page=258) | — | 14 Landing Gear and Brakes | Pendente | `—` | `PTM:PAGE:258` | Aguardando lote autorizado. |
| [259](KA-200-B200-PTM.pdf#page=259) | — | 15 Flight Controls | Pendente | `—` | `PTM:PAGE:259` | Aguardando lote autorizado. |
| [260](KA-200-B200-PTM.pdf#page=260) | — | 15 Flight Controls | Pendente | `—` | `PTM:PAGE:260` | Aguardando lote autorizado. |
| [261](KA-200-B200-PTM.pdf#page=261) | — | 15 Flight Controls | Pendente | `—` | `PTM:PAGE:261` | Aguardando lote autorizado. |
| [262](KA-200-B200-PTM.pdf#page=262) | — | 15 Flight Controls | Pendente | `—` | `PTM:PAGE:262` | Aguardando lote autorizado. |
| [263](KA-200-B200-PTM.pdf#page=263) | — | 15 Flight Controls | Pendente | `—` | `PTM:PAGE:263` | Aguardando lote autorizado. |
| [264](KA-200-B200-PTM.pdf#page=264) | — | 15 Flight Controls | Pendente | `—` | `PTM:PAGE:264` | Aguardando lote autorizado. |
| [265](KA-200-B200-PTM.pdf#page=265) | — | 15 Flight Controls | Pendente | `—` | `PTM:PAGE:265` | Aguardando lote autorizado. |
| [266](KA-200-B200-PTM.pdf#page=266) | — | 15 Flight Controls | Pendente | `—` | `PTM:PAGE:266` | Aguardando lote autorizado. |
| [267](KA-200-B200-PTM.pdf#page=267) | — | 15 Flight Controls | Pendente | `—` | `PTM:PAGE:267` | Aguardando lote autorizado. |
| [268](KA-200-B200-PTM.pdf#page=268) | — | 15 Flight Controls | Pendente | `—` | `PTM:PAGE:268` | Aguardando lote autorizado. |
| [269](KA-200-B200-PTM.pdf#page=269) | — | 15 Flight Controls | Pendente | `—` | `PTM:PAGE:269` | Aguardando lote autorizado. |
| [270](KA-200-B200-PTM.pdf#page=270) | — | 15 Flight Controls | Pendente | `—` | `PTM:PAGE:270` | Aguardando lote autorizado. |
| [271](KA-200-B200-PTM.pdf#page=271) | — | 15 Flight Controls | Pendente | `—` | `PTM:PAGE:271` | Aguardando lote autorizado. |
| [272](KA-200-B200-PTM.pdf#page=272) | — | 15 Flight Controls | Pendente | `—` | `PTM:PAGE:272` | Aguardando lote autorizado. |
| [273](KA-200-B200-PTM.pdf#page=273) | — | 15 Flight Controls | Pendente | `—` | `PTM:PAGE:273` | Aguardando lote autorizado. |
| [274](KA-200-B200-PTM.pdf#page=274) | — | 15 Flight Controls | Pendente | `—` | `PTM:PAGE:274` | Aguardando lote autorizado. |
| [275](KA-200-B200-PTM.pdf#page=275) | — | 16 Avionics | Pendente | `—` | `PTM:PAGE:275` | Aguardando lote autorizado. |
| [276](KA-200-B200-PTM.pdf#page=276) | — | 16 Avionics | Pendente | `—` | `PTM:PAGE:276` | Aguardando lote autorizado. |
| [277](KA-200-B200-PTM.pdf#page=277) | — | 16 Avionics | Pendente | `—` | `PTM:PAGE:277` | Aguardando lote autorizado. |
| [278](KA-200-B200-PTM.pdf#page=278) | — | 16 Avionics | Pendente | `—` | `PTM:PAGE:278` | Aguardando lote autorizado. |
| [279](KA-200-B200-PTM.pdf#page=279) | — | 16 Avionics | Pendente | `—` | `PTM:PAGE:279` | Aguardando lote autorizado. |
| [280](KA-200-B200-PTM.pdf#page=280) | — | 16 Avionics | Pendente | `—` | `PTM:PAGE:280` | Aguardando lote autorizado. |
| [281](KA-200-B200-PTM.pdf#page=281) | — | 16 Avionics | Pendente | `—` | `PTM:PAGE:281` | Aguardando lote autorizado. |
| [282](KA-200-B200-PTM.pdf#page=282) | — | 16 Avionics | Pendente | `—` | `PTM:PAGE:282` | Aguardando lote autorizado. |
| [283](KA-200-B200-PTM.pdf#page=283) | — | 16 Avionics | Pendente | `—` | `PTM:PAGE:283` | Aguardando lote autorizado. |
| [284](KA-200-B200-PTM.pdf#page=284) | — | 16 Avionics | Pendente | `—` | `PTM:PAGE:284` | Aguardando lote autorizado. |
| [285](KA-200-B200-PTM.pdf#page=285) | — | 16 Avionics | Pendente | `—` | `PTM:PAGE:285` | Aguardando lote autorizado. |
| [286](KA-200-B200-PTM.pdf#page=286) | — | 16 Avionics | Pendente | `—` | `PTM:PAGE:286` | Aguardando lote autorizado. |
| [287](KA-200-B200-PTM.pdf#page=287) | — | 16 Avionics | Pendente | `—` | `PTM:PAGE:287` | Aguardando lote autorizado. |
| [288](KA-200-B200-PTM.pdf#page=288) | — | 16 Avionics | Pendente | `—` | `PTM:PAGE:288` | Aguardando lote autorizado. |
| [289](KA-200-B200-PTM.pdf#page=289) | — | 16 Avionics | Pendente | `—` | `PTM:PAGE:289` | Aguardando lote autorizado. |
| [290](KA-200-B200-PTM.pdf#page=290) | — | 16 Avionics | Pendente | `—` | `PTM:PAGE:290` | Aguardando lote autorizado. |
| [291](KA-200-B200-PTM.pdf#page=291) | — | 16 Avionics | Pendente | `—` | `PTM:PAGE:291` | Aguardando lote autorizado. |
| [292](KA-200-B200-PTM.pdf#page=292) | — | 16 Avionics | Pendente | `—` | `PTM:PAGE:292` | Aguardando lote autorizado. |
| [293](KA-200-B200-PTM.pdf#page=293) | — | 16 Avionics | Pendente | `—` | `PTM:PAGE:293` | Aguardando lote autorizado. |
| [294](KA-200-B200-PTM.pdf#page=294) | — | 16 Avionics | Pendente | `—` | `PTM:PAGE:294` | Aguardando lote autorizado. |
| [295](KA-200-B200-PTM.pdf#page=295) | — | 16 Avionics | Pendente | `—` | `PTM:PAGE:295` | Aguardando lote autorizado. |
| [296](KA-200-B200-PTM.pdf#page=296) | — | 16 Avionics | Pendente | `—` | `PTM:PAGE:296` | Aguardando lote autorizado. |
| [297](KA-200-B200-PTM.pdf#page=297) | — | 16 Avionics | Pendente | `—` | `PTM:PAGE:297` | Aguardando lote autorizado. |
| [298](KA-200-B200-PTM.pdf#page=298) | — | 16 Avionics | Pendente | `—` | `PTM:PAGE:298` | Aguardando lote autorizado. |
| [299](KA-200-B200-PTM.pdf#page=299) | — | 16 Avionics | Pendente | `—` | `PTM:PAGE:299` | Aguardando lote autorizado. |
| [300](KA-200-B200-PTM.pdf#page=300) | — | 16 Avionics | Pendente | `—` | `PTM:PAGE:300` | Aguardando lote autorizado. |
| [301](KA-200-B200-PTM.pdf#page=301) | — | 16 Avionics | Pendente | `—` | `PTM:PAGE:301` | Aguardando lote autorizado. |
| [302](KA-200-B200-PTM.pdf#page=302) | — | 16 Avionics | Pendente | `—` | `PTM:PAGE:302` | Aguardando lote autorizado. |
| [303](KA-200-B200-PTM.pdf#page=303) | — | 16 Avionics | Pendente | `—` | `PTM:PAGE:303` | Aguardando lote autorizado. |
| [304](KA-200-B200-PTM.pdf#page=304) | — | 17 Miscellaneous Systems | Pendente | `—` | `PTM:PAGE:304` | Aguardando lote autorizado. |
| [305](KA-200-B200-PTM.pdf#page=305) | — | 17 Miscellaneous Systems | Pendente | `—` | `PTM:PAGE:305` | Aguardando lote autorizado. |
| [306](KA-200-B200-PTM.pdf#page=306) | — | 17 Miscellaneous Systems | Pendente | `—` | `PTM:PAGE:306` | Aguardando lote autorizado. |
| [307](KA-200-B200-PTM.pdf#page=307) | — | 17 Miscellaneous Systems | Pendente | `—` | `PTM:PAGE:307` | Aguardando lote autorizado. |
| [308](KA-200-B200-PTM.pdf#page=308) | — | 17 Miscellaneous Systems | Pendente | `—` | `PTM:PAGE:308` | Aguardando lote autorizado. |
| [309](KA-200-B200-PTM.pdf#page=309) | — | 17 Miscellaneous Systems | Pendente | `—` | `PTM:PAGE:309` | Aguardando lote autorizado. |
| [310](KA-200-B200-PTM.pdf#page=310) | — | 17 Miscellaneous Systems | Pendente | `—` | `PTM:PAGE:310` | Aguardando lote autorizado. |
| [311](KA-200-B200-PTM.pdf#page=311) | — | 17 Miscellaneous Systems | Pendente | `—` | `PTM:PAGE:311` | Aguardando lote autorizado. |
| [312](KA-200-B200-PTM.pdf#page=312) | — | 17 Miscellaneous Systems | Pendente | `—` | `PTM:PAGE:312` | Aguardando lote autorizado. |
| [313](KA-200-B200-PTM.pdf#page=313) | — | 17 Miscellaneous Systems | Pendente | `—` | `PTM:PAGE:313` | Aguardando lote autorizado. |
| [314](KA-200-B200-PTM.pdf#page=314) | — | 17 Miscellaneous Systems | Pendente | `—` | `PTM:PAGE:314` | Aguardando lote autorizado. |
| [315](KA-200-B200-PTM.pdf#page=315) | — | 17 Miscellaneous Systems | Pendente | `—` | `PTM:PAGE:315` | Aguardando lote autorizado. |
| [316](KA-200-B200-PTM.pdf#page=316) | — | 18 Weight and Balance | Pendente | `—` | `PTM:PAGE:316` | Aguardando lote autorizado. |
| [317](KA-200-B200-PTM.pdf#page=317) | — | 18 Weight and Balance | Pendente | `—` | `PTM:PAGE:317` | Aguardando lote autorizado. |
| [318](KA-200-B200-PTM.pdf#page=318) | — | 18 Weight and Balance | Pendente | `—` | `PTM:PAGE:318` | Aguardando lote autorizado. |
| [319](KA-200-B200-PTM.pdf#page=319) | — | 18 Weight and Balance | Pendente | `—` | `PTM:PAGE:319` | Aguardando lote autorizado. |
| [320](KA-200-B200-PTM.pdf#page=320) | — | 18 Weight and Balance | Pendente | `—` | `PTM:PAGE:320` | Aguardando lote autorizado. |
| [321](KA-200-B200-PTM.pdf#page=321) | — | 18 Weight and Balance | Pendente | `—` | `PTM:PAGE:321` | Aguardando lote autorizado. |
| [322](KA-200-B200-PTM.pdf#page=322) | — | 18 Weight and Balance | Pendente | `—` | `PTM:PAGE:322` | Aguardando lote autorizado. |
| [323](KA-200-B200-PTM.pdf#page=323) | — | 18 Weight and Balance | Pendente | `—` | `PTM:PAGE:323` | Aguardando lote autorizado. |
| [324](KA-200-B200-PTM.pdf#page=324) | — | 18 Weight and Balance | Pendente | `—` | `PTM:PAGE:324` | Aguardando lote autorizado. |
| [325](KA-200-B200-PTM.pdf#page=325) | — | 18 Weight and Balance | Pendente | `—` | `PTM:PAGE:325` | Aguardando lote autorizado. |
| [326](KA-200-B200-PTM.pdf#page=326) | — | 18 Weight and Balance | Pendente | `—` | `PTM:PAGE:326` | Aguardando lote autorizado. |
| [327](KA-200-B200-PTM.pdf#page=327) | — | 18 Weight and Balance | Pendente | `—` | `PTM:PAGE:327` | Aguardando lote autorizado. |
| [328](KA-200-B200-PTM.pdf#page=328) | — | 18 Weight and Balance | Pendente | `—` | `PTM:PAGE:328` | Aguardando lote autorizado. |
| [329](KA-200-B200-PTM.pdf#page=329) | — | 18 Weight and Balance | Pendente | `—` | `PTM:PAGE:329` | Aguardando lote autorizado. |
| [330](KA-200-B200-PTM.pdf#page=330) | — | 18 Weight and Balance | Pendente | `—` | `PTM:PAGE:330` | Aguardando lote autorizado. |
| [331](KA-200-B200-PTM.pdf#page=331) | — | 18 Weight and Balance | Pendente | `—` | `PTM:PAGE:331` | Aguardando lote autorizado. |
| [332](KA-200-B200-PTM.pdf#page=332) | — | 18 Weight and Balance | Pendente | `—` | `PTM:PAGE:332` | Aguardando lote autorizado. |
| [333](KA-200-B200-PTM.pdf#page=333) | — | 18 Weight and Balance | Pendente | `—` | `PTM:PAGE:333` | Aguardando lote autorizado. |
| [334](KA-200-B200-PTM.pdf#page=334) | — | 18 Weight and Balance | Pendente | `—` | `PTM:PAGE:334` | Aguardando lote autorizado. |
| [335](KA-200-B200-PTM.pdf#page=335) | — | 18 Weight and Balance | Pendente | `—` | `PTM:PAGE:335` | Aguardando lote autorizado. |
| [336](KA-200-B200-PTM.pdf#page=336) | — | General Pilot Information | Pendente | `—` | `PTM:PAGE:336` | Aguardando lote autorizado. |
| [337](KA-200-B200-PTM.pdf#page=337) | — | General Pilot Information | Pendente | `—` | `PTM:PAGE:337` | Aguardando lote autorizado. |
| [338](KA-200-B200-PTM.pdf#page=338) | — | General Pilot Information | Pendente | `—` | `PTM:PAGE:338` | Aguardando lote autorizado. |
| [339](KA-200-B200-PTM.pdf#page=339) | — | General Pilot Information | Pendente | `—` | `PTM:PAGE:339` | Aguardando lote autorizado. |
| [340](KA-200-B200-PTM.pdf#page=340) | — | General Pilot Information | Pendente | `—` | `PTM:PAGE:340` | Aguardando lote autorizado. |
| [341](KA-200-B200-PTM.pdf#page=341) | — | General Pilot Information | Pendente | `—` | `PTM:PAGE:341` | Aguardando lote autorizado. |
| [342](KA-200-B200-PTM.pdf#page=342) | — | General Pilot Information | Pendente | `—` | `PTM:PAGE:342` | Aguardando lote autorizado. |
| [343](KA-200-B200-PTM.pdf#page=343) | — | General Pilot Information | Pendente | `—` | `PTM:PAGE:343` | Aguardando lote autorizado. |
| [344](KA-200-B200-PTM.pdf#page=344) | — | General Pilot Information | Pendente | `—` | `PTM:PAGE:344` | Aguardando lote autorizado. |
| [345](KA-200-B200-PTM.pdf#page=345) | — | General Pilot Information | Pendente | `—` | `PTM:PAGE:345` | Aguardando lote autorizado. |
| [346](KA-200-B200-PTM.pdf#page=346) | — | General Pilot Information | Pendente | `—` | `PTM:PAGE:346` | Aguardando lote autorizado. |
| [347](KA-200-B200-PTM.pdf#page=347) | — | General Pilot Information | Pendente | `—` | `PTM:PAGE:347` | Aguardando lote autorizado. |
| [348](KA-200-B200-PTM.pdf#page=348) | — | General Pilot Information | Pendente | `—` | `PTM:PAGE:348` | Aguardando lote autorizado. |
| [349](KA-200-B200-PTM.pdf#page=349) | — | General Pilot Information | Pendente | `—` | `PTM:PAGE:349` | Aguardando lote autorizado. |
| [350](KA-200-B200-PTM.pdf#page=350) | — | General Pilot Information | Pendente | `—` | `PTM:PAGE:350` | Aguardando lote autorizado. |
| [351](KA-200-B200-PTM.pdf#page=351) | — | General Pilot Information | Pendente | `—` | `PTM:PAGE:351` | Aguardando lote autorizado. |
| [352](KA-200-B200-PTM.pdf#page=352) | — | General Pilot Information | Pendente | `—` | `PTM:PAGE:352` | Aguardando lote autorizado. |
| [353](KA-200-B200-PTM.pdf#page=353) | — | General Pilot Information | Pendente | `—` | `PTM:PAGE:353` | Aguardando lote autorizado. |
| [354](KA-200-B200-PTM.pdf#page=354) | — | General Pilot Information | Pendente | `—` | `PTM:PAGE:354` | Aguardando lote autorizado. |
| [355](KA-200-B200-PTM.pdf#page=355) | — | General Pilot Information | Pendente | `—` | `PTM:PAGE:355` | Aguardando lote autorizado. |
| [356](KA-200-B200-PTM.pdf#page=356) | — | General Pilot Information | Pendente | `—` | `PTM:PAGE:356` | Aguardando lote autorizado. |
| [357](KA-200-B200-PTM.pdf#page=357) | — | General Pilot Information | Pendente | `—` | `PTM:PAGE:357` | Aguardando lote autorizado. |
| [358](KA-200-B200-PTM.pdf#page=358) | — | General Pilot Information | Pendente | `—` | `PTM:PAGE:358` | Aguardando lote autorizado. |
| [359](KA-200-B200-PTM.pdf#page=359) | — | General Pilot Information | Pendente | `—` | `PTM:PAGE:359` | Aguardando lote autorizado. |
| [360](KA-200-B200-PTM.pdf#page=360) | — | General Pilot Information | Pendente | `—` | `PTM:PAGE:360` | Aguardando lote autorizado. |
| [361](KA-200-B200-PTM.pdf#page=361) | — | General Pilot Information | Pendente | `—` | `PTM:PAGE:361` | Aguardando lote autorizado. |
| [362](KA-200-B200-PTM.pdf#page=362) | — | General Pilot Information | Pendente | `—` | `PTM:PAGE:362` | Aguardando lote autorizado. |
| [363](KA-200-B200-PTM.pdf#page=363) | — | Walkaround | Pendente | `—` | `PTM:PAGE:363` | Aguardando lote autorizado. |
| [364](KA-200-B200-PTM.pdf#page=364) | — | Walkaround | Pendente | `—` | `PTM:PAGE:364` | Aguardando lote autorizado. |
| [365](KA-200-B200-PTM.pdf#page=365) | — | Walkaround | Pendente | `—` | `PTM:PAGE:365` | Aguardando lote autorizado. |
| [366](KA-200-B200-PTM.pdf#page=366) | — | Walkaround | Pendente | `—` | `PTM:PAGE:366` | Aguardando lote autorizado. |
| [367](KA-200-B200-PTM.pdf#page=367) | — | Walkaround | Pendente | `—` | `PTM:PAGE:367` | Aguardando lote autorizado. |
| [368](KA-200-B200-PTM.pdf#page=368) | — | Walkaround | Pendente | `—` | `PTM:PAGE:368` | Aguardando lote autorizado. |
| [369](KA-200-B200-PTM.pdf#page=369) | — | Walkaround | Pendente | `—` | `PTM:PAGE:369` | Aguardando lote autorizado. |
| [370](KA-200-B200-PTM.pdf#page=370) | — | Walkaround | Pendente | `—` | `PTM:PAGE:370` | Aguardando lote autorizado. |
| [371](KA-200-B200-PTM.pdf#page=371) | — | Walkaround | Pendente | `—` | `PTM:PAGE:371` | Aguardando lote autorizado. |
| [372](KA-200-B200-PTM.pdf#page=372) | — | Walkaround | Pendente | `—` | `PTM:PAGE:372` | Aguardando lote autorizado. |
| [373](KA-200-B200-PTM.pdf#page=373) | — | Walkaround | Pendente | `—` | `PTM:PAGE:373` | Aguardando lote autorizado. |
| [374](KA-200-B200-PTM.pdf#page=374) | — | Walkaround | Pendente | `—` | `PTM:PAGE:374` | Aguardando lote autorizado. |
| [375](KA-200-B200-PTM.pdf#page=375) | — | Walkaround | Pendente | `—` | `PTM:PAGE:375` | Aguardando lote autorizado. |
| [376](KA-200-B200-PTM.pdf#page=376) | — | Walkaround | Pendente | `—` | `PTM:PAGE:376` | Aguardando lote autorizado. |
| [377](KA-200-B200-PTM.pdf#page=377) | — | Appendix | Pendente | `—` | `PTM:PAGE:377` | Aguardando lote autorizado. |
| [378](KA-200-B200-PTM.pdf#page=378) | — | Annunciator Panels | Pendente | `—` | `PTM:PAGE:378` | Aguardando lote autorizado. |
| [379](KA-200-B200-PTM.pdf#page=379) | — | Annunciator Panels | Pendente | `—` | `PTM:PAGE:379` | Aguardando lote autorizado. |
| [380](KA-200-B200-PTM.pdf#page=380) | — | Annunciator Panels | Pendente | `—` | `PTM:PAGE:380` | Aguardando lote autorizado. |
| [381](KA-200-B200-PTM.pdf#page=381) | — | Annunciator Panels | Pendente | `—` | `PTM:PAGE:381` | Aguardando lote autorizado. |
| [382](KA-200-B200-PTM.pdf#page=382) | — | Annunciator Panels | Pendente | `—` | `PTM:PAGE:382` | Aguardando lote autorizado. |

## 8. Histórico de lotes

| Data | Lote | Intervalo | Método | Resultado | Ressalvas |
|---|---|---|---|---|---|
| 2026-10-29 | 1 | 1–100 | Visual 144 dpi + detalhes; tabelas Markdown; imagens | 100 revisadas; commit `2c02f6f` | Divergências mantidas |
| 2026-10-29 | 2 | 101–200 | Visual 144 dpi + tabelas/gráficos 240 dpi; esquemas girados 200 dpi; inserção apenas em marcadores pendentes | 100 revisadas; 182 pendentes; commit a publicar | Lote 1 preservado; tabelas e gráficos sem interpolação |

## 9. Verificações executadas

- Hash do PDF e 382 páginas: conferidos.
- Marcadores 1–382 em ordem: conferidos.
- Hashes dos 200 trechos revisados: conferidos.
- Links, imagens PNG e tabelas Markdown: conferidos.
- Arquivos protegidos e baseline de todos os rastreados: sem alterações inesperadas.
- Testes: `python -m pytest tests/test_ptm_integrity.py -q` → **22 passed**.
- Nenhuma página do lote 1 foi alterada; não houve necessidade de correção retroativa.

## 10. Próximos passos

1. Aguardar confirmação antes do lote 3 (201–300).
2. Não executar conversores sobre o Markdown revisado; inserir apenas nos marcadores pendentes.
3. Ao concluir lote futuro, atualizar controle, testes, commit e push na branch da sessão.
4. Qualquer alteração retroativa deve ser registrada e justificada.
