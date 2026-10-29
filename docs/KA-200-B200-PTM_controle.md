# Controle de revisão — KA-200-B200-PTM

## 1. Identificação da fonte

- **PDF:** [KA-200-B200-PTM.pdf](KA-200-B200-PTM.pdf)
- **Páginas físicas:** 382
- **SHA-256 esperado e observado:** `6835a8102c8f600c3b39aa34d2b53f9a848790321447136ec2cd821af245986d` — conferem.
- **Tamanho:** 32.274.925 bytes.
- **Transcrição:** [KA-200-B200-PTM.md](KA-200-B200-PTM.md)
- **Manifesto de hashes/metadados:** [KA-200-B200-PTM_manifesto.json](KA-200-B200-PTM_manifesto.json)
- **Branch da sessão:** `arena/25936ceb-kingair-b200`.
- **Data da revisão do lote 1:** 2026-10-29.
- **Escopo:** comparação documental, não validação operacional nem aprovação para voo.

## 2. Trabalho anterior preservado

Foram preservados sem sobrescrita: `KA-200-B200-PTM.pdf`, todos os arquivos do POH, `KA-200-B200-PTM_completo.md`, `KA-200-B200-PTM_corrigido.md`, `KA-200-B200-PTM_docling/` e `KA-200-B200-PTM_imagens/`. Esses materiais são conversões/edições automáticas anteriores, **sem revisão visual atestada neste trabalho**. O novo arquivo revisado é separado e usa marcadores físicos; conversores não devem escrever nele.

## 3. Progresso por lote

| Lote | Páginas físicas | Estado | Revisadas no lote | Commit |
|---|---|---|---:|---|
| 1 | 1–100 | Concluído; aguardando confirmação para o lote 2 | 100 | A publicar neste lote |
| 2 | 101–200 | Pendente; não iniciar sem confirmação | 0 | — |
| 3 | 201–300 | Pendente; não iniciar sem confirmação | 0 | — |
| 4 | 301–382 | Pendente; não iniciar sem confirmação | 0 | — |

**Total revisado:** 100/382 (26.18%). **Pendentes:** 282 páginas.

## 4. Método empregado no lote 1

1. Conferência de hash, contagem de páginas, branch e estado inicial do Git.
2. Renderização das 100 páginas a 144 dpi para conferência visual sequencial; detalhes, tabelas e esquemas a 200–220 dpi.
3. Texto nativo do PDF usado apenas como apoio; palavras e números confirmados visualmente. A camada nativa apresentou pelo menos uma divergência relevante (`SYSTEMES` na p. 37, enquanto a imagem mostra `SYSTEMS`).
4. Tabelas reconstruídas em Markdown, preservando linhas, colunas, cabeçalhos, notas e continuações. Células mescladas foram representadas por células vazias ou cabeçalhos repetidos, com imagem de apoio.
5. Figuras, fotos, diagramas e esquemas coloridos preservados em `docs/assets/ptm/`. Esquemas girados receberam detalhe rotacionado apenas para leitura; o fac-símile mantém a orientação original.
6. Divergências aparentes do próprio manual foram mantidas e registradas; nenhum valor foi corrigido, estimado ou interpolado.
7. Cada página revisada tem marcador `PTM:PAGE:NNN`, link para o PDF, hash SHA-256 do trecho e fac-símile. Páginas 101–382 permanecem como pendentes, sem conteúdo automático.

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

## 6. Limitações

- Rótulos muito pequenos de diagramas e esquemas não foram linearizados em texto; devem ser consultados nas imagens de apoio em alta resolução.
- Cores, símbolos, setas e relações espaciais de diagramas são preservados por imagem, não por descrição textual exaustiva.
- A revisão não confirma atualidade operacional, aplicabilidade a aeronaves específicas nem procedimentos de voo.
- Questões foram transcritas sem indicar respostas ou gabarito.

## 7. Inventário por página física

Hash do trecho: SHA-256 do conteúdo entre marcadores, excluindo as linhas de marcador e status, conforme definido no manifesto. `—` indica trecho ainda não revisado.

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
| [101](KA-200-B200-PTM.pdf#page=101) | — | 5 Fuel System | Pendente | `—` | `PTM:PAGE:101` | Aguardando lote autorizado. |
| [102](KA-200-B200-PTM.pdf#page=102) | — | 5 Fuel System | Pendente | `—` | `PTM:PAGE:102` | Aguardando lote autorizado. |
| [103](KA-200-B200-PTM.pdf#page=103) | — | 5 Fuel System | Pendente | `—` | `PTM:PAGE:103` | Aguardando lote autorizado. |
| [104](KA-200-B200-PTM.pdf#page=104) | — | 5 Fuel System | Pendente | `—` | `PTM:PAGE:104` | Aguardando lote autorizado. |
| [105](KA-200-B200-PTM.pdf#page=105) | — | 5 Fuel System | Pendente | `—` | `PTM:PAGE:105` | Aguardando lote autorizado. |
| [106](KA-200-B200-PTM.pdf#page=106) | — | 5 Fuel System | Pendente | `—` | `PTM:PAGE:106` | Aguardando lote autorizado. |
| [107](KA-200-B200-PTM.pdf#page=107) | — | 5 Fuel System | Pendente | `—` | `PTM:PAGE:107` | Aguardando lote autorizado. |
| [108](KA-200-B200-PTM.pdf#page=108) | — | 5 Fuel System | Pendente | `—` | `PTM:PAGE:108` | Aguardando lote autorizado. |
| [109](KA-200-B200-PTM.pdf#page=109) | — | 5 Fuel System | Pendente | `—` | `PTM:PAGE:109` | Aguardando lote autorizado. |
| [110](KA-200-B200-PTM.pdf#page=110) | — | 6 Auxiliary Power Systems | Pendente | `—` | `PTM:PAGE:110` | Aguardando lote autorizado. |
| [111](KA-200-B200-PTM.pdf#page=111) | — | 7 Powerplant | Pendente | `—` | `PTM:PAGE:111` | Aguardando lote autorizado. |
| [112](KA-200-B200-PTM.pdf#page=112) | — | 7 Powerplant | Pendente | `—` | `PTM:PAGE:112` | Aguardando lote autorizado. |
| [113](KA-200-B200-PTM.pdf#page=113) | — | 7 Powerplant | Pendente | `—` | `PTM:PAGE:113` | Aguardando lote autorizado. |
| [114](KA-200-B200-PTM.pdf#page=114) | — | 7 Powerplant | Pendente | `—` | `PTM:PAGE:114` | Aguardando lote autorizado. |
| [115](KA-200-B200-PTM.pdf#page=115) | — | 7 Powerplant | Pendente | `—` | `PTM:PAGE:115` | Aguardando lote autorizado. |
| [116](KA-200-B200-PTM.pdf#page=116) | — | 7 Powerplant | Pendente | `—` | `PTM:PAGE:116` | Aguardando lote autorizado. |
| [117](KA-200-B200-PTM.pdf#page=117) | — | 7 Powerplant | Pendente | `—` | `PTM:PAGE:117` | Aguardando lote autorizado. |
| [118](KA-200-B200-PTM.pdf#page=118) | — | 7 Powerplant | Pendente | `—` | `PTM:PAGE:118` | Aguardando lote autorizado. |
| [119](KA-200-B200-PTM.pdf#page=119) | — | 7 Powerplant | Pendente | `—` | `PTM:PAGE:119` | Aguardando lote autorizado. |
| [120](KA-200-B200-PTM.pdf#page=120) | — | 7 Powerplant | Pendente | `—` | `PTM:PAGE:120` | Aguardando lote autorizado. |
| [121](KA-200-B200-PTM.pdf#page=121) | — | 7 Powerplant | Pendente | `—` | `PTM:PAGE:121` | Aguardando lote autorizado. |
| [122](KA-200-B200-PTM.pdf#page=122) | — | 7 Powerplant | Pendente | `—` | `PTM:PAGE:122` | Aguardando lote autorizado. |
| [123](KA-200-B200-PTM.pdf#page=123) | — | 7 Powerplant | Pendente | `—` | `PTM:PAGE:123` | Aguardando lote autorizado. |
| [124](KA-200-B200-PTM.pdf#page=124) | — | 7 Powerplant | Pendente | `—` | `PTM:PAGE:124` | Aguardando lote autorizado. |
| [125](KA-200-B200-PTM.pdf#page=125) | — | 7 Powerplant | Pendente | `—` | `PTM:PAGE:125` | Aguardando lote autorizado. |
| [126](KA-200-B200-PTM.pdf#page=126) | — | 7 Powerplant | Pendente | `—` | `PTM:PAGE:126` | Aguardando lote autorizado. |
| [127](KA-200-B200-PTM.pdf#page=127) | — | 7 Powerplant | Pendente | `—` | `PTM:PAGE:127` | Aguardando lote autorizado. |
| [128](KA-200-B200-PTM.pdf#page=128) | — | 7 Powerplant | Pendente | `—` | `PTM:PAGE:128` | Aguardando lote autorizado. |
| [129](KA-200-B200-PTM.pdf#page=129) | — | 7 Powerplant | Pendente | `—` | `PTM:PAGE:129` | Aguardando lote autorizado. |
| [130](KA-200-B200-PTM.pdf#page=130) | — | 7 Powerplant | Pendente | `—` | `PTM:PAGE:130` | Aguardando lote autorizado. |
| [131](KA-200-B200-PTM.pdf#page=131) | — | 7 Powerplant | Pendente | `—` | `PTM:PAGE:131` | Aguardando lote autorizado. |
| [132](KA-200-B200-PTM.pdf#page=132) | — | 7 Powerplant | Pendente | `—` | `PTM:PAGE:132` | Aguardando lote autorizado. |
| [133](KA-200-B200-PTM.pdf#page=133) | — | 7 Powerplant | Pendente | `—` | `PTM:PAGE:133` | Aguardando lote autorizado. |
| [134](KA-200-B200-PTM.pdf#page=134) | — | 7 Powerplant | Pendente | `—` | `PTM:PAGE:134` | Aguardando lote autorizado. |
| [135](KA-200-B200-PTM.pdf#page=135) | — | 7 Powerplant | Pendente | `—` | `PTM:PAGE:135` | Aguardando lote autorizado. |
| [136](KA-200-B200-PTM.pdf#page=136) | — | 7 Powerplant | Pendente | `—` | `PTM:PAGE:136` | Aguardando lote autorizado. |
| [137](KA-200-B200-PTM.pdf#page=137) | — | 7 Powerplant | Pendente | `—` | `PTM:PAGE:137` | Aguardando lote autorizado. |
| [138](KA-200-B200-PTM.pdf#page=138) | — | 7 Powerplant | Pendente | `—` | `PTM:PAGE:138` | Aguardando lote autorizado. |
| [139](KA-200-B200-PTM.pdf#page=139) | — | 7 Powerplant | Pendente | `—` | `PTM:PAGE:139` | Aguardando lote autorizado. |
| [140](KA-200-B200-PTM.pdf#page=140) | — | 7 Powerplant | Pendente | `—` | `PTM:PAGE:140` | Aguardando lote autorizado. |
| [141](KA-200-B200-PTM.pdf#page=141) | — | 7 Powerplant | Pendente | `—` | `PTM:PAGE:141` | Aguardando lote autorizado. |
| [142](KA-200-B200-PTM.pdf#page=142) | — | 7 Powerplant | Pendente | `—` | `PTM:PAGE:142` | Aguardando lote autorizado. |
| [143](KA-200-B200-PTM.pdf#page=143) | — | 7 Powerplant | Pendente | `—` | `PTM:PAGE:143` | Aguardando lote autorizado. |
| [144](KA-200-B200-PTM.pdf#page=144) | — | 7 Powerplant | Pendente | `—` | `PTM:PAGE:144` | Aguardando lote autorizado. |
| [145](KA-200-B200-PTM.pdf#page=145) | — | 7 Powerplant | Pendente | `—` | `PTM:PAGE:145` | Aguardando lote autorizado. |
| [146](KA-200-B200-PTM.pdf#page=146) | — | 7 Powerplant | Pendente | `—` | `PTM:PAGE:146` | Aguardando lote autorizado. |
| [147](KA-200-B200-PTM.pdf#page=147) | — | 7 Powerplant | Pendente | `—` | `PTM:PAGE:147` | Aguardando lote autorizado. |
| [148](KA-200-B200-PTM.pdf#page=148) | — | 7 Powerplant | Pendente | `—` | `PTM:PAGE:148` | Aguardando lote autorizado. |
| [149](KA-200-B200-PTM.pdf#page=149) | — | 7 Powerplant | Pendente | `—` | `PTM:PAGE:149` | Aguardando lote autorizado. |
| [150](KA-200-B200-PTM.pdf#page=150) | — | 7 Powerplant | Pendente | `—` | `PTM:PAGE:150` | Aguardando lote autorizado. |
| [151](KA-200-B200-PTM.pdf#page=151) | — | 7 Powerplant | Pendente | `—` | `PTM:PAGE:151` | Aguardando lote autorizado. |
| [152](KA-200-B200-PTM.pdf#page=152) | — | 7 Powerplant | Pendente | `—` | `PTM:PAGE:152` | Aguardando lote autorizado. |
| [153](KA-200-B200-PTM.pdf#page=153) | — | 7 Powerplant | Pendente | `—` | `PTM:PAGE:153` | Aguardando lote autorizado. |
| [154](KA-200-B200-PTM.pdf#page=154) | — | 7 Powerplant | Pendente | `—` | `PTM:PAGE:154` | Aguardando lote autorizado. |
| [155](KA-200-B200-PTM.pdf#page=155) | — | 7 Powerplant | Pendente | `—` | `PTM:PAGE:155` | Aguardando lote autorizado. |
| [156](KA-200-B200-PTM.pdf#page=156) | — | 8 Fire Protection | Pendente | `—` | `PTM:PAGE:156` | Aguardando lote autorizado. |
| [157](KA-200-B200-PTM.pdf#page=157) | — | 8 Fire Protection | Pendente | `—` | `PTM:PAGE:157` | Aguardando lote autorizado. |
| [158](KA-200-B200-PTM.pdf#page=158) | — | 8 Fire Protection | Pendente | `—` | `PTM:PAGE:158` | Aguardando lote autorizado. |
| [159](KA-200-B200-PTM.pdf#page=159) | — | 8 Fire Protection | Pendente | `—` | `PTM:PAGE:159` | Aguardando lote autorizado. |
| [160](KA-200-B200-PTM.pdf#page=160) | — | 8 Fire Protection | Pendente | `—` | `PTM:PAGE:160` | Aguardando lote autorizado. |
| [161](KA-200-B200-PTM.pdf#page=161) | — | 8 Fire Protection | Pendente | `—` | `PTM:PAGE:161` | Aguardando lote autorizado. |
| [162](KA-200-B200-PTM.pdf#page=162) | — | 8 Fire Protection | Pendente | `—` | `PTM:PAGE:162` | Aguardando lote autorizado. |
| [163](KA-200-B200-PTM.pdf#page=163) | — | 8 Fire Protection | Pendente | `—` | `PTM:PAGE:163` | Aguardando lote autorizado. |
| [164](KA-200-B200-PTM.pdf#page=164) | — | 8 Fire Protection | Pendente | `—` | `PTM:PAGE:164` | Aguardando lote autorizado. |
| [165](KA-200-B200-PTM.pdf#page=165) | — | 8 Fire Protection | Pendente | `—` | `PTM:PAGE:165` | Aguardando lote autorizado. |
| [166](KA-200-B200-PTM.pdf#page=166) | — | 9 Pneumatics | Pendente | `—` | `PTM:PAGE:166` | Aguardando lote autorizado. |
| [167](KA-200-B200-PTM.pdf#page=167) | — | 9 Pneumatics | Pendente | `—` | `PTM:PAGE:167` | Aguardando lote autorizado. |
| [168](KA-200-B200-PTM.pdf#page=168) | — | 9 Pneumatics | Pendente | `—` | `PTM:PAGE:168` | Aguardando lote autorizado. |
| [169](KA-200-B200-PTM.pdf#page=169) | — | 9 Pneumatics | Pendente | `—` | `PTM:PAGE:169` | Aguardando lote autorizado. |
| [170](KA-200-B200-PTM.pdf#page=170) | — | 9 Pneumatics | Pendente | `—` | `PTM:PAGE:170` | Aguardando lote autorizado. |
| [171](KA-200-B200-PTM.pdf#page=171) | — | 9 Pneumatics | Pendente | `—` | `PTM:PAGE:171` | Aguardando lote autorizado. |
| [172](KA-200-B200-PTM.pdf#page=172) | — | 9 Pneumatics | Pendente | `—` | `PTM:PAGE:172` | Aguardando lote autorizado. |
| [173](KA-200-B200-PTM.pdf#page=173) | — | 9 Pneumatics | Pendente | `—` | `PTM:PAGE:173` | Aguardando lote autorizado. |
| [174](KA-200-B200-PTM.pdf#page=174) | — | 9 Pneumatics | Pendente | `—` | `PTM:PAGE:174` | Aguardando lote autorizado. |
| [175](KA-200-B200-PTM.pdf#page=175) | — | 9 Pneumatics | Pendente | `—` | `PTM:PAGE:175` | Aguardando lote autorizado. |
| [176](KA-200-B200-PTM.pdf#page=176) | — | 10 Ice and Rain Protection | Pendente | `—` | `PTM:PAGE:176` | Aguardando lote autorizado. |
| [177](KA-200-B200-PTM.pdf#page=177) | — | 10 Ice and Rain Protection | Pendente | `—` | `PTM:PAGE:177` | Aguardando lote autorizado. |
| [178](KA-200-B200-PTM.pdf#page=178) | — | 10 Ice and Rain Protection | Pendente | `—` | `PTM:PAGE:178` | Aguardando lote autorizado. |
| [179](KA-200-B200-PTM.pdf#page=179) | — | 10 Ice and Rain Protection | Pendente | `—` | `PTM:PAGE:179` | Aguardando lote autorizado. |
| [180](KA-200-B200-PTM.pdf#page=180) | — | 10 Ice and Rain Protection | Pendente | `—` | `PTM:PAGE:180` | Aguardando lote autorizado. |
| [181](KA-200-B200-PTM.pdf#page=181) | — | 10 Ice and Rain Protection | Pendente | `—` | `PTM:PAGE:181` | Aguardando lote autorizado. |
| [182](KA-200-B200-PTM.pdf#page=182) | — | 10 Ice and Rain Protection | Pendente | `—` | `PTM:PAGE:182` | Aguardando lote autorizado. |
| [183](KA-200-B200-PTM.pdf#page=183) | — | 10 Ice and Rain Protection | Pendente | `—` | `PTM:PAGE:183` | Aguardando lote autorizado. |
| [184](KA-200-B200-PTM.pdf#page=184) | — | 10 Ice and Rain Protection | Pendente | `—` | `PTM:PAGE:184` | Aguardando lote autorizado. |
| [185](KA-200-B200-PTM.pdf#page=185) | — | 10 Ice and Rain Protection | Pendente | `—` | `PTM:PAGE:185` | Aguardando lote autorizado. |
| [186](KA-200-B200-PTM.pdf#page=186) | — | 10 Ice and Rain Protection | Pendente | `—` | `PTM:PAGE:186` | Aguardando lote autorizado. |
| [187](KA-200-B200-PTM.pdf#page=187) | — | 10 Ice and Rain Protection | Pendente | `—` | `PTM:PAGE:187` | Aguardando lote autorizado. |
| [188](KA-200-B200-PTM.pdf#page=188) | — | 10 Ice and Rain Protection | Pendente | `—` | `PTM:PAGE:188` | Aguardando lote autorizado. |
| [189](KA-200-B200-PTM.pdf#page=189) | — | 10 Ice and Rain Protection | Pendente | `—` | `PTM:PAGE:189` | Aguardando lote autorizado. |
| [190](KA-200-B200-PTM.pdf#page=190) | — | 10 Ice and Rain Protection | Pendente | `—` | `PTM:PAGE:190` | Aguardando lote autorizado. |
| [191](KA-200-B200-PTM.pdf#page=191) | — | 10 Ice and Rain Protection | Pendente | `—` | `PTM:PAGE:191` | Aguardando lote autorizado. |
| [192](KA-200-B200-PTM.pdf#page=192) | — | 10 Ice and Rain Protection | Pendente | `—` | `PTM:PAGE:192` | Aguardando lote autorizado. |
| [193](KA-200-B200-PTM.pdf#page=193) | — | 10 Ice and Rain Protection | Pendente | `—` | `PTM:PAGE:193` | Aguardando lote autorizado. |
| [194](KA-200-B200-PTM.pdf#page=194) | — | 10 Ice and Rain Protection | Pendente | `—` | `PTM:PAGE:194` | Aguardando lote autorizado. |
| [195](KA-200-B200-PTM.pdf#page=195) | — | 10 Ice and Rain Protection | Pendente | `—` | `PTM:PAGE:195` | Aguardando lote autorizado. |
| [196](KA-200-B200-PTM.pdf#page=196) | — | 10 Ice and Rain Protection | Pendente | `—` | `PTM:PAGE:196` | Aguardando lote autorizado. |
| [197](KA-200-B200-PTM.pdf#page=197) | — | 10 Ice and Rain Protection | Pendente | `—` | `PTM:PAGE:197` | Aguardando lote autorizado. |
| [198](KA-200-B200-PTM.pdf#page=198) | — | 10 Ice and Rain Protection | Pendente | `—` | `PTM:PAGE:198` | Aguardando lote autorizado. |
| [199](KA-200-B200-PTM.pdf#page=199) | — | 10 Ice and Rain Protection | Pendente | `—` | `PTM:PAGE:199` | Aguardando lote autorizado. |
| [200](KA-200-B200-PTM.pdf#page=200) | — | 10 Ice and Rain Protection | Pendente | `—` | `PTM:PAGE:200` | Aguardando lote autorizado. |
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
| 2026-10-29 | 1 | 1–100 | Visual 144 dpi + detalhes 200–220 dpi; texto nativo apenas como apoio; tabelas Markdown; imagens de apoio | 100 páginas revisadas; 282 pendentes | Divergências impressas mantidas; diagramas preservados em imagem |

## 9. Verificações executadas

- Hash SHA-256 do PDF e contagem de 382 páginas: conferidos.
- Marcadores físicos 1–382 em ordem, sem lacunas: conferidos.
- Hashes dos 100 trechos revisados: conferidos contra o manifesto.
- Links locais, links de página do PDF e imagens PNG: conferidos.
- Tabelas Markdown retangulares e separadores válidos: conferidos.
- Inventário do controle com 382 páginas e hashes dos trechos revisados: conferido.
- Arquivos protegidos (PDF, POH e conversões anteriores do PTM): hashes inalterados.
- Testes automatizados: `python -m pytest tests/test_ptm_integrity.py -q` → **19 passed**.
- Nenhuma página de lote anterior foi alterada: este é o primeiro lote.

## 10. Próximos passos

1. Aguardar confirmação do usuário antes de iniciar o lote 2 (páginas 101–200).
2. Não executar conversores sobre `KA-200-B200-PTM.md`; inserir novos trechos apenas nos marcadores pendentes.
3. Ao concluir cada lote futuro, atualizar este controle, executar os testes, fazer commit e push na branch da sessão.
4. Se alguma página de lote anterior precisar de alteração, registrar e justificar nesta seção e no histórico.
