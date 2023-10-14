from functools import reduce
from algorithms.select_bfprt import select_bfprt_factory

select_bfprt = select_bfprt_factory(5)

def sorted_fractional_knapsack(items, W):
    v1 = 0
    w1 = 0

    # Ordena os itens pelo ratio
    items = sorted(items, key=lambda item: item.ratio, reverse=True)

    # Percorre os itens na ordem decrescente do ratio
    for item in items:
        # Se o item cabe na mochila
        if item.peso + w1 <= W:
            w1 += item.peso
            v1 += item.valor
        # Se o item não cabe na mochila
        else:
            # Calcula o valor fracionado do item
            v1 += item.valor * ((W - w1) / item.peso)
            break
    
    return v1

from utils.logger import logger

def median_of_medians_fractional_knapsack(items, W):
    if W == 0 or len(items)==0:
        return 0

    if len(items) == 1 and items[0].peso > W:
        return W * items[0].ratio

    k = len(items) // 2

    mid = select_bfprt(items, k)
    items_right = items[mid:]

    w1 = 0
    v1 = 0

    for item in items_right:
        w1 += item.peso
        v1 += item.valor
    
    # Não cabe na mochila
    if(w1 > W):
        return median_of_medians_fractional_knapsack(items_right, W)

    # Cabe na mochila
    items_left = items[:mid]
    return v1 + median_of_medians_fractional_knapsack(items_left, W - w1)

def partition_by_mean(items, inicio, fim):
    k = len(items)
    pivot = 1 / k * sum([item.ratio for item in items])
    i = inicio - 1

    for j in range(inicio, fim):
        if items[j].ratio >= pivot:
            i += 1

            items[i], items[j] = items[j], items[i]

    items[i + 1], items[fim] = items[fim], items[i + 1]
    return i + 1

def mean_partition_fractional_knapsack(items, W):
    if W == 0 or len(items) == 0:
        return 0

    if len(items) == 1 and items[0].peso > W:
        return W * items[0].ratio


    mid = partition_by_mean(items, 0, len(items) - 1)
    items_right = items[: mid]

    w1 = 0
    v1 = 0

    for item in items_right:
        w1 += item.peso
        v1 += item.valor

    # Não cabe na mochila
    if(w1 > W):
        return mean_partition_fractional_knapsack(items_right, W)

    # Cabe na mochila
    items_left = items[mid : ]
    return v1 + mean_partition_fractional_knapsack(items_left, W - w1)
