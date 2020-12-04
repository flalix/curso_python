#!/usr/bin/env python

import os, sys
from scipy import stats
import numpy as np
import pandas as pd

from scipy import stats

colors = ['yellow', 'blue', 'red']

def stat_asteristics(pval, NS='NS'):
    if pval >= 0.05: return NS
    if pval > 0.01:  return '*'
    if pval > 0.001:  return '**'
    return '***'

def test_normality_desc(series, alpha = 0.05):
    # teste de normalidade de Shapiro-Wilkis
    stat, pvalue = stats.shapiro(series)

    if pvalue > alpha:
        text = 'A distribuição se assemelha a uma distriuição normal (não se rejeita a H0)'
        ret = True
    else:
        text = 'A distribuição não se assemelha a uma distriuição normal (rejeita-se a H0)'
        ret = False

    text_stat = 'p-value %.2e (%s)'%(pvalue, stat_asteristics(pvalue))

    return ret, text, text_stat, stat, pvalue

def test_one_way_ANOVA (samp1, samp2, alpha = 0.05):
    # teste de variancias de Fisher - one way ANOVA (analysis of variance)
    stat, pvalue = stats.f_oneway(samp1, samp2)

    if pvalue > alpha:
        text = 'As distribuições tem variâncias similares (não se rejeita a H0)'
        ret = True
    else:
        text = 'As distribuições não têm variâncias similares (rejeita-se a H0)'
        ret = False

    text_stat = 'p-value %.2e (%s)'%(pvalue, stat_asteristics(pvalue))

    return ret, text, text_stat, stat, pvalue

def test_one_way_ANOVA3 (samp1, samp2, samp3, alpha = 0.05):
    # teste de variancias de Fisher - one way ANOVA (analysis of variance)
    stat, pvalue = stats.f_oneway(samp1, samp2, samp3)

    if pvalue > alpha:
        text = 'As distribuições tem variâncias similares (não se rejeita a H0)'
        ret = True
    else:
        text = 'As distribuições não têm variâncias similares (rejeita-se a H0)'
        ret = False

    text_stat = 'p-value %.2e (%s)'%(pvalue, stat_asteristics(pvalue))

    return ret, text, text_stat, stat, pvalue


def ttest(samp1, samp2, alpha = 0.05, equal_var=False):

    stat, pvalue = stats.ttest_ind(samp1, samp2, equal_var = equal_var)

    if pvalue > alpha:
        text = 'As distribuições são similares (não se rejeita a H0)'
        ret = True
    else:
        text = 'As distribuições não são similares (rejeita-se a H0)'
        ret = False

    text_stat = 'p-value %.2e (%s)'%(pvalue, stat_asteristics(pvalue))

    return ret, text, text_stat, stat, pvalue


def calc_fi(dof, is_normal=False, alpha=.05):

    alpha /= 2
    if is_normal:
        fi_inf = stats.norm.ppf(alpha, 0, 1)
        fi_sup = stats.norm.ppf(1-alpha, 0, 1)
    else:
        fi_inf = stats.t.ppf( alpha, dof)
        fi_sup = stats.t.ppf( (1-alpha), dof)

    return np.array( [fi_inf, fi_sup])

# samp1 = controle
# samp2 = case
def calc_intervalo_confianca(samp1, samp2, alpha=.05):

    n1 = len(samp1); n2 = len(samp2)
    if n1 >= n2:
        N = n1
    else:
        N = n2
    dof = N-1

    x = np.linspace(stats.t.ppf(0.01, dof), stats.t.ppf(0.99, dof), 100)

    muc1 = np.mean(samp1); sdvc1 = np.std(samp1)
    muc2 = np.mean(samp2); sdvc2 = np.std(samp2)

    diff = muc2 - muc1
    sd_diff = np.sqrt(sdvc1**2 + sdvc2**2)

    effect_size = diff / sd_diff

    fis = calc_fi(dof, alpha=alpha, is_normal=False)
    SEM = np.sqrt(sdvc1**2/n1 + sdvc2**2/n2)
    CI = (fis * SEM) + diff

    return CI, SEM, n1, n2, effect_size, diff
