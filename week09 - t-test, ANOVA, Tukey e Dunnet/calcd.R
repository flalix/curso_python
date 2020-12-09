suppressMessages(suppressWarnings(library(multcomp)))

calc_dunnet <- function(fname='table.tsv', path = '../tmp/',
                        groups=c("ctrl-pos", "control", "ctrl-neg", 'drg1', 'drg2', 'drg3')) {
    
    df <- read.delim(paste0(path,fname), sep='\t')
    
    df$group <- factor(df$group, levels = groups)
    
    fit <- aov(val ~ group, df)
    dunnet <- glht(fit, linfct=mcp(group="Dunnett"))
    
    summ <- summary(dunnet)
    
    dfr <- data.frame(summ$test$coefficients, summ$test$tstat, summ$test$pvalues)
    colnames(dfr) <- c("estimate", "tstat", "pvalue")

    fname = 'dunnet_result.tsv'
    filefull = paste0(path,fname)
    
    write.table(dfr, file=filefull, quote=FALSE, sep='\t')
    print(paste('file saved at', filefull))
}

calc_dunnet()
