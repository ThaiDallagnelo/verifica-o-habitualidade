#!/usr/bin/env python3
"""
Calcula as janelas de tempo da analise de habitualidade (CAC - atirador desportivo).
Usa apenas a biblioteca padrao do Python. Datas no formato DD/MM/AAAA.

USO
  # Analise B (aquisicao de arma):
  python apoio/calcular_periodos.py aquisicao --cr 10/12/2024 --solicitacao 16/10/2026

  # Analise A (progressao de nivel):
  python apoio/calcular_periodos.py progressao --solicitacao 16/10/2026

REGRAS IMPLEMENTADAS (ver apoio/regras_habitualidade.md)
  - Soma de meses preserva o dia; se o dia nao existir no mes de destino, usa o ultimo dia (29/02 -> 28/02).
  - Janela e INCLUSIVA nas duas pontas (como no enunciado do usuario: 10/12/2024 a 10/12/2025).
  - CR concedido antes de 27/12/2023 => inicio do 1o periodo = 27/12/2023.
"""
import argparse
import calendar
from datetime import date, datetime

MARCO_PORTARIA_166 = date(2023, 12, 27)


def parse(s: str) -> date:
    return datetime.strptime(s, "%d/%m/%Y").date()


def fmt(d: date) -> str:
    return d.strftime("%d/%m/%Y")


def add_months(d: date, n: int) -> date:
    m = d.month - 1 + n
    y = d.year + m // 12
    m = m % 12 + 1
    last = calendar.monthrange(y, m)[1]
    return date(y, m, min(d.day, last))


def aquisicao(cr: date, solicitacao: date):
    inicio = cr if cr >= MARCO_PORTARIA_166 else MARCO_PORTARIA_166
    pre_portaria = cr < MARCO_PORTARIA_166
    print(f"CR concedido em ........ {fmt(cr)}"
          + ("  (ANTES da Portaria 166 -> inicio ajustado para 27/12/2023)" if pre_portaria else ""))
    print(f"Inicio do 1o periodo ... {fmt(inicio)}")
    print(f"Data da solicitacao .... {fmt(solicitacao)}")
    periodos = []
    k = 0
    while True:
        ini = add_months(inicio, 12 * k)
        fim = add_months(inicio, 12 * (k + 1))
        if fim > solicitacao:
            proximo = (ini, fim)
            break
        periodos.append((ini, fim))
        k += 1
    print()
    if not periodos:
        print("RESULTADO: nenhum periodo de 12 meses foi concluido ate a solicitacao.")
        print(f"          Habitualidade NAO exigivel (1o periodo so termina em {fmt(proximo[1])}).")
        return
    print("Periodos completos (do mais antigo ao mais recente):")
    for i, (a, b) in enumerate(periodos, 1):
        marca = "  <== PERIODO ANALISADO (ultimo completo)" if i == len(periodos) else "  (informativo)"
        print(f"  P{i}: {fmt(a)} a {fmt(b)}{marca}")
    print(f"Periodo em andamento ... {fmt(proximo[0])} a {fmt(proximo[1])}  (NAO analisado)")
    ini, fim = periodos[-1]
    print()
    print(f"PERIODO ANALISADO: {fmt(ini)} a {fmt(fim)} (inclusive nas duas pontas)")


def progressao(solicitacao: date):
    ini = add_months(solicitacao, -12)
    print(f"Data da solicitacao de alteracao de nivel .. {fmt(solicitacao)}")
    print(f"JANELA ANALISADA: {fmt(ini)} a {fmt(solicitacao)} (inclusive nas duas pontas)")


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="modo", required=True)
    a = sub.add_parser("aquisicao")
    a.add_argument("--cr", required=True)
    a.add_argument("--solicitacao", required=True)
    p = sub.add_parser("progressao")
    p.add_argument("--solicitacao", required=True)
    args = ap.parse_args()
    if args.modo == "aquisicao":
        aquisicao(parse(args.cr), parse(args.solicitacao))
    else:
        progressao(parse(args.solicitacao))
