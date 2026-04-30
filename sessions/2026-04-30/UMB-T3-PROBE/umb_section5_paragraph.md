# Paragraph for UMB §5 update -- Higher-stratum desert sweep (P-09 / UMB-T3-PROBE)

**Working draft for §5 of the Universal-Mu-Barrier (UMB) manuscript.**

> **§5.x Higher-stratum (T3) desert sweep.**  Addressing UMB OP-5, we
> conducted an empirical probe for T3 candidates -- convergent, irrational
> PCFs whose limits resist identification by every basis tier we can build
> with closed-form constants of conductor $\le 200$ and weight $\le 6$.
> The input pool comprised the named T2A R1 family
> ($a=[1,0,-1,-1,-1]$, $b=[-1,1,-1]$ leading-first), $30$ representative
> CMAX$=1$ "trans_hard" $F(4,2)$ families (sampled from the 1162-family
> survivor cohort of [T2A-DEGREE42-DEEP-VALIDATE](#)), and $10$
> randomly-sampled members of the 482-irrationals quadratic-denominator
> catalog -- $41$ families in total.  Each was probed against a 5-tier
> nested basis (cardinalities $7 \to 15 \to 20 \to 24 \to 29$) including
> $\pi$, $\log\{2,3,5\}$, $\zeta(3)$, $\zeta(5)$, Catalan's $G$,
> $\operatorname{Li}_n(1/2)$ for $n\in\{2,3\}$, $L(2,\chi_{-3})$,
> $\Gamma(1/3),\Gamma(1/4),\Gamma(1/6)$ and squares,
> $1/\operatorname{AGM}(1,\sqrt 2)$, the lemniscate constant
> $\omega = \Gamma(1/4)^2/(2\sqrt{2\pi})$, $e$, $e^{\pi}-1$, plus the
> bilinear products $\pi\!\cdot\!\log p$, $\pi\!\cdot\! G$,
> $\log 2\!\cdot\!\log 3$, $\pi\!\cdot\!\zeta(3)$.
>
> PSLQ was run at $\operatorname{dps}=1500$ with $\operatorname{hmax}=10^{10}$
> and the standard *phantom-trap* (relation rejected unless the $L$-coefficient
> is non-zero).  All $41$ families produced no hit at any tier.  Two
> demotion checks were applied to every all-tier-NULL family:
> (i) a M\"{o}bius/inverse probe (PSLQ on $1/L$ against Tier 1 and Tier 3),
> and (ii) an algebraic-degree-$\le 4$ probe (PSLQ on
> $\{1,L,L^{2},L^{3},L^{4}\}$ with $\operatorname{hmax}=10^{8}$).
> Both checks returned $0/41$ hits.  Five representative survivors
> (T2A R1, three trans_hard families with distinct
> $b$-shapes including the smallest-$|L|$ instance $L\approx -0.0349$
> and the largest-$|L|$ instance $L\approx 18.49$, one alternate
> $a$-shape, and the sampled member IRR482\_277 with
> $L\approx 7.1415$) were escalated to $\operatorname{dps}=3000$,
> where the basis-NULL persists at every tier and the weak-PSLQ residual
> slope $\mu_{\mathrm{res}} = d\log_{10}|R|/d\,\mathrm{dps}$ is $0$
> across $\mathrm{dps}\in\{500,1000,1500,3000\}$ for all $5$ -- the
> coefficient-magnitude growth is also $0$, since weak PSLQ with
> $\operatorname{hmax}=10^{\mathrm{dps}/3}$ returns no relation
> at any tested precision.  See [`mu_slope_plot.png`](mu_slope_plot.png).
>
> Per the relay HALT directive, "any candidate with slope$\to 0$ at
> $\operatorname{dps}\ge 3000$ escalates to a formal barrier-stratum
> analysis."  We therefore mark these $5$ as **provisional T3
> candidates** -- *not* proven T3 (the basis omits modular forms,
> theta values, $_2F_1$ at non-trivial algebraic arguments, and
> Chowla-Selberg CM-periods of weight $\ge 2$, so basis-NULL is
> *necessary* but not *sufficient* for genuine T3 membership) -- and
> recommend a follow-on barrier-stratum paper that derives the
> generating-function ODE for the trans_hard $a$-shape
> $\{1,-1,-1,-1,-1\}$ at CMAX$=1$, computes its Frobenius monodromy at
> all punctures, and tests for $\mathrm{Heun}/\mathrm{Painlev\'{e}}/\,_2F_1$
> period closed forms outside the elementary basis.  The fact that
> $100\%$ of our input pool produced T3 candidates under this basis
> argues *against* the strong reading of "T3 = $\emptyset$ at low
> degree" and *in favour* of "the elementary-constant basis is
> insufficient to explain the deg-$(4,2)$ trans_hard cohort."

---

### Suggested citations / cross-references for §5

- T2A-DEGREE42-DEEP-VALIDATE (2026-04-26) -- 1162 trans_hard cohort.
- T2A-R1-IDENTIFY (2026-04-30) -- R1 mystery constant, 30-element basis NULL.
- 482-Irrationals census (P02 / Cohen-Schwarz tradition).
- This session's `t3_candidates.json` and `mu_slope_plot.png`.
