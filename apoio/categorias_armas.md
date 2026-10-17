# Categorias de armas para fins de habitualidade

Base: Decreto nº 11.615/2023, **arts. 11 e 12** (e art. 35 e 38-B). Ver os textos em `legislacao_aplicavel.md`.

## 1. Atiradores de nível 1, 2 e 3 → **3 categorias** (por tipo de arma)

Para os níveis 1 a 3, **não há separação entre uso permitido e uso restrito**: o que define a categoria é o **tipo** da arma. O art. 35 do Decreto manda comprovar a habitualidade "por arma representativa de cada um dos tipos de arma de que tratam o art. 11, incisos I, II e III, e o art. 12, incisos III, IV e V", que se agrupam assim:

| Código da categoria | Tipo de arma | Uso permitido (art. 11) | Uso restrito (art. 12) |
|---|---|---|---|
| `porte` | Arma de fogo de porte (pistola, revólver, garrucha) | inciso I | inciso III |
| `longa_raiada` | Arma de fogo portátil longa, de alma raiada | inciso II (repetição) | inciso IV |
| `longa_lisa` | Arma de fogo portátil longa, de alma lisa | inciso III (repetição, calibre 12 ou inferior) | inciso V (a: calibre superior a 12; b: semiautomática de qualquer calibre) |

**Consequência prática:** uma pistola de uso permitido e uma pistola de uso restrito pertencem à **mesma** categoria `porte` para um atirador N1–N3. A habitualidade é contada **por categoria**, somando os eventos realizados com qualquer arma do acervo daquela categoria.

## 2. Atirador de **alto rendimento** → **2 categorias** (por uso)

Para o atirador desportivo de alto rendimento, a separação passa a ser entre **uso permitido** e **uso restrito** (Decreto, art. 38-B; IN 311, art. 71, § 3º):

| Código da categoria | Descrição |
|---|---|
| `permitido` | armas de fogo de uso permitido registradas em nome do titular |
| `restrito` | armas de fogo de uso restrito registradas em nome do titular |

Nesse caso o **tipo** (porte, longa raiada, longa lisa) **deixa de ser** o critério de separação.

> ⚠️ Os textos anexados **não informam** qual quantidade de treinamentos/competições se aplica ao alto rendimento (se a do nível 3 ou outra). Por isso o campo "nível-base de habitualidade do alto rendimento" é **obrigatório** nos dados do atirador; se estiver vazio, o agente **não conclui** e encaminha ao responsável humano.

## 3. O que **NÃO** tem categoria própria na habitualidade (encaminhar ao humano)

O agente **não deve** enquadrar sozinho nem contar para habitualidade:

| Situação | Motivo |
|---|---|
| Arma de fogo portátil longa, alma raiada, **semiautomática ≤ .22 LR** (art. 11, IV) | O art. 35 do Decreto e o art. 71 da IN 311 **não listam** o art. 11, IV entre os tipos que exigem habitualidade. |
| Arma automática (art. 12, I) e arma de fogo não portátil (art. 12, VI) | Não listadas no art. 35 / art. 71. |
| Arma de pressão / airsoft / paintball | Não são armas de fogo para este fim. |
| Arma sem categoria ou uso preenchido nos dados | O agente **não classifica por conta própria** (a classificação vem do CRAF/apostila). |
| Arma cujo enquadramento dependa de energia/calibre ("ato conjunto" Exército–PF) | O ato conjunto **não foi anexado**. |

## 3.1 Como o agente deve ler o acervo

- Use **apenas** os campos `categoria` e `uso` já preenchidos em `atiradores_ficticios.md`.
- Se `categoria`/`uso` estiverem vazios, ambíguos ou fora da tabela acima → **EXCEÇÃO** (encaminhar ao humano).
