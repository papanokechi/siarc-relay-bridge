# Next steps — H2

1. **Library verification.** Obtain the full Chowla--Selberg 1967 paper and the correct Yu CM-period/IMRN source. Record theorem/page numbers for the exact CM eta/period formula.

2. **T2 modular regression recipe (no computation run here).** For each nonsingular cubic, compute canonical \(\tau_b\), then compare residuals \(R_b=A_{\mathrm{fit}}-6\) against:
   - \(M_j=\log|j(\tau_b)|\),
   - \(M_4=\log\|E_4(\tau_b)\|\),
   - \(M_\Delta=\log\|\Delta(\tau_b)\|=\log((\operatorname{Im}\tau_b)^6|\eta(\tau_b)|^{24})\),
   - \(M_6=\log\|E_6(\tau_b)\|\) or \(\log|j(\tau_b)-1728|\).

3. **Residual discriminator test.** Fit/subtract the best \(M_j\) term, then test whether \(M_\Delta\) explains the remaining rank structure. If not, test the order-2 elliptic-point term \(M_6\).

4. **Exact CM cell test.** Treat exact \(j=0\) as a special zero, not as \(\log|j|=-\infty\). Verify from closed-form/deep-WKB asymptotics that \(A-6=0\) and that any \(\Gamma(1/3)\) term appears only in intercept/amplitude parameters.

5. **j=1728 search.** Identify cubic families with \(j=1728\) or near it. H2 predicts a possible secondary \(E_6\)-controlled residual, not an automatic zero of \(A-6\).

6. **Cross-degree caution.** Do not promote the cubic j=0 law to a sharp quartic theorem without a separate moduli explanation; the R13-D quartic result already argues against a naive cross-degree lift.
