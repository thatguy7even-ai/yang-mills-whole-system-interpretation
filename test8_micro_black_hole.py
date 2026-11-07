"""Test 8: the micro black hole -- past the fold threshold.

Dakota's extension 3 (his words, held exactly):
BLACK HOLE = SCALED-UP PROTON: the accretion disc looks the same from any
angle because light bends -- in reality infinite layered discs around the
outer event horizon; the emission field is everywhere at once because the
gravitational weight of the field itself collapses the comet shape; when
spherical, expansion is those layers stacking outward.

And extension 4 (the hypothesis): folds inward = micro black hole.

This run takes test 7 past D_fold and asks, in the toy:
- does the emission field collapse the comet shape (extension 3)?
- does the breathing get trapped?
- does old light bend around it?
- does new light start there?
- what happens to the radius and hardening observables?
- does the proton-scale version show the layered-disc structure?

Inputs from test 7 (fiducial lambda=0.05, c_c=0.30, eta=1):
  E_cap = 9.38 MeV, E_fold = 31.27 MeV, D_crit = 0.469 MeV/link,
  D_fold = 1.564 MeV/link, R_fold = 0.8596 fm.
New assumption: the trapped mode leaks slowly, lambda_trap = 0.001 per link
(30-50x slower than the open loop -- the trap holds the mode in).
"""
import math

G = 6.67430e-11
C = 2.99792458e8
MEV_J = 1.602176634e-13
M_P = 938.27
E_CAP = M_P * 0.10 ** 2        # 9.38 MeV
C_C = 0.30
E_FOLD = E_CAP / C_C           # 31.27 MeV
LAM = 0.05
D_FOLD = LAM * E_FOLD          # 1.564 MeV/link
R_FOLD = math.sqrt(12) * 0.24 * math.exp(E_FOLD / M_P)   # 0.8596 fm
LAM_TRAP = 0.001               # slow leak of the trapped mode (ASSUMPTION)
U_CMB_TODAY_J_M3 = 0.26 * 1.602176634e-19 / 1e-6   # 0.26 eV/cm^3 -> J/m^3
L_LINK_M = 1e-10
A0 = 0.24
Q = 3.0 / A0
F_SINGLE = 1.0 / (1.0 + (Q * A0) ** 2) ** 2


def r_schwarzschild(E_mev):
    return 2 * G * E_mev * MEV_J / C ** 4   # metres


# ---- Block A: the emission field collapses the comet shape ----
print("BLOCK A -- THE EMISSION FIELD COLLAPSES THE COMET SHAPE")
print("  the forward cone of non-emission is fixed to the direction of motion")
print("  in the base model. Toy: cone half-angle fraction theta/theta0 =")
print("  max(0, 1 - E*/E_fold) -- the field's own weight closes the cone as")
print("  the mode energy approaches the fold. (theta0 itself is a parameter;")
print("  the toy reports the FRACTION, not an absolute angle.)")
print("  D        E* [MeV]   theta/theta0   emission shape")
for D in (0.0, 0.469, 1.0, 1.5, 1.564, 2.0, 5.0):
    E_star = D / LAM
    frac = max(0.0, 1 - E_star / E_FOLD)
    shape = "comet (cone open)" if frac > 0.5 else ("collapsing" if frac > 0 else "SPHERICAL -- cone closed")
    print(f"  {D:5.3f}  {E_star:8.2f}   {frac:8.3f}      {shape}")
print("  -> YES, in the toy's terms: past the fold the comet shape is gone and")
print("     the emission field is spherical -- everywhere at once, as extension 3")
print("     describes. The collapse is driven by the mode energy, not by gravity:")
print("     the field closes on itself because the loop's own weight (its trapped")
print("     energy) overwhelms the directional cone. The toy cannot say whether")
print("     a real gravitational field would do the same at these energies (see C).")

# ---- Block B: the breathing gets trapped ----
print("\nBLOCK B -- THE BREATHING GETS TRAPPED")
print("  breathing transmission across the folded proton T = max(0, 1 - E*/E_fold).")
print("  past the fold T = 0: the mode no longer propagates along the chain.")
print("  the fold is a BREATHING FIREWALL -- downstream links lose the drive and")
print("  revert to the bare value (s = 1e-5) unless lit by another source.")
print("  inside the trap the mode keeps the fed energy: E_int(n+1) = E_int(n) + D")
print("  - lambda_trap * E_int(n), starting at E_fold. It leaks slowly as NEW LIGHT.")
print("  D        T_breath   E_int after 10 links [MeV]   after 100 links [MeV]   new-light leak at fold [MeV/link]")
for D in (1.564, 2.0, 5.0):
    E_int = E_FOLD
    E10 = E_int
    for _ in range(10):
        E10 = E10 + D - LAM_TRAP * E10
    E100 = E10
    for _ in range(90):
        E100 = E100 + D - LAM_TRAP * E100
    leak = LAM_TRAP * E_FOLD
    print(f"  {D:5.3f}    0.000      {E10:10.2f}                {E100:10.2f}              {leak:.4f}")
print("  the interior energy grows without bound in the toy (equilibrium D/lambda_trap")
print("  = 1564-5000 MeV) -- the toy has no interior regulation. That unbounded growth")
print("  is itself a finding: something must cap the interior, and the model does not say what.")

# ---- Block B2: the trapped leak is a NEW LIGHT SOURCE ----
print("\nBLOCK B2 -- NEW LIGHT STARTS THERE")
print("  the trapped mode leaks lambda_trap * E_fold = 0.031 MeV per link at the fold.")
P_leak = LAM_TRAP * E_FOLD * MEV_J / (L_LINK_M / C)
print(f"  leak power at the fold = {P_leak:.2e} W from a proton-scale object.")
for label, u in (("today (z=0)", U_CMB_TODAY_J_M3),
                 ("proto-galaxy epoch (z=10)", U_CMB_TODAY_J_M3 * 11.0 ** 4)):
    flux = u * C
    r_lit = math.sqrt(P_leak / (4 * math.pi * flux))
    print(f"  {label}: bath flux = {flux:.2e} W/m^2; new light dominates the bath out to r = {r_lit:.2f} m")
print("  -> YES: the micro black hole becomes a local new-light source. In the")
print("     gate language of test 6 it switches the breathing mode ON in a small")
print("     neighbourhood around itself (~80 m at z=10, ~10 km today, fiducial")
print("     lambda_trap). Self-consistent with extensions 1-2: the breathing mode")
print("     IS the star, and the folded proton is a tiny star-like source.")
print("     (Radius scales as sqrt(lambda_trap); it is assumption-sensitive.)")

# ---- Block C: does old light bend around it? ----
print("\nBLOCK C -- DOES OLD LIGHT BEND AROUND IT?")
print("  gravitational bending needs a horizon. Schwarzschild radius r_s = 2GE/c^4:")
print("  E in trap [MeV]   r_s [m]        r_s [fm]      vs proton radius 0.84 fm")
for E in (E_FOLD, 40.0, 100.0, 1564.0, 5000.0):
    rs = r_schwarzschild(E)
    print(f"  {E:10.1f}      {rs:.3e}   {rs * 1e15:.3e}   {rs * 1e15 / 0.84:.1e}x")
E_for_1fm = 1e-15 * C ** 4 / (2 * G) / MEV_J
print(f"  energy needed for r_s = 1 fm: {E_for_1fm:.2e} MeV = {E_for_1fm / 1e3:.2e} GeV")
print(f"  that is {E_for_1fm / E_FOLD:.1e}x the fold energy -- ~19 orders of magnitude short.")
print("  -> NO gravitational bending in the toy: at 31 MeV the horizon would be")
print("     ~1e-40 fm, 40 orders below the proton. There is no photon sphere and")
print("     no layered-disc structure at this scale (see D). What DOES happen is")
print("     GEOMETRIC capture: old light that hits the fold region is absorbed into")
print("     the loop instead of passing through. Capture cross-section:")
R_FOLD_FM = R_FOLD
cap = math.pi * R_FOLD_FM ** 2
bare = math.pi * (math.sqrt(12) * 0.24) ** 2
print(f"     pi * R_fold^2 = {cap:.3f} fm^2 vs bare proton pi * R0^2 = {bare:.3f} fm^2")
print(f"     -- a factor {cap / bare:.2f}x. No enhancement: the fold captures old light")
print("     at the proton's ordinary geometric cross-section. Bending would need")
print("     a real horizon, which needs ~1e38 GeV concentrated in the trap.")

# ---- Block D: layered discs? ----
print("\nBLOCK D -- LAYERED DISCS (extension 3)?")
print("  the infinite layered discs of extension 3 are multiple IMAGES of the disc,")
print("  made by light orbiting the photon sphere at 1.5 r_s. The toy has no photon")
print("  sphere (r_s ~ 1e-40 fm), so it has no layered discs. What it DOES have:")
print("  - spherical emission field past the fold (Block A): YES, in the toy.")
print("  - expansion as layers stacking outward: the trapped leak (Block B2)")
print("    radiates shells of new light, but they are ordinary expanding shells,")
print("    NOT lensed images -- no infinite stacking, no same-disc-from-every-angle.")
print("  -> the proton-scale version shows the SPHERICAL part of extension 3 but")
print("     NOT the layered-disc part. The discs need a real horizon; the toy's")
print("     'black hole' is a FIELD-TRAPPED state, not a gravitational one.")
print("     What would be needed: a horizon at the fold scale, i.e. ~1e38 GeV in")
print("     the trap, or a different mechanism that bends light without gravity.")

# ---- Block E: radius and hardening past the threshold ----
print("\nBLOCK E -- RADIUS AND HARDENING PAST THE THRESHOLD")
print("  the outer folds freeze at the fold value (further fed energy goes INSIDE,")
print("  not outside). The core scale hits zero, so the form factor flattens: F -> 1.")
print("  D        E* [MeV]   R [fm]    a_core [fm]   hardening")
for D in (0.469, 1.0, 1.5, 1.564):
    E_star = D / LAM
    R = math.sqrt(12) * 0.24 * math.exp(E_star / M_P)
    a_core = A0 * (1 - C_C * E_star / E_CAP)
    if a_core <= 0:
        print(f"  {D:5.3f}  {E_star:8.2f}   {R:.4f}    {a_core:8.4f}     +9900% (F -> 1, core gone)")
        continue
    F_core = 1.0 / (1.0 + (Q * a_core) ** 2) ** 2
    H = F_core / F_SINGLE - 1.0
    print(f"  {D:5.3f}  {E_star:8.2f}   {R:.4f}    {a_core:8.4f}     {100 * H:+.0f}%")
print("  past the fold the object is NO LONGER A PROTON: R and the form factor are")
print("  undefined for it. The saturated values at the fold are R = 0.8596 fm and")
print("  hardening -> +9900% (the core has vanished into the trap). An outside")
print("  observer sees a 0.86 fm object that has stopped scattering like a proton")
print("  at high q, and that glows faintly with new light (Block B2).")

# ---- Block F: what the model cannot answer ----
print("\nBLOCK F -- WHAT THE MODEL CANNOT ANSWER")
print("  (a) Stability: does the trapped state evaporate, settle, or keep growing?")
print("      The toy's interior grows without bound (equilibrium D/lambda_trap is")
print("      1500-5000 MeV). Something must cap it; the model does not say what.")
print("  (b) The layered discs: need a real horizon / photon sphere. At proton")
print("      energies the toy is ~19 orders short. A gravitational micro black")
print("      hole at this scale is NOT in the model -- the fold is a field event.")
print("  (c) The interior: one trapped mode, or a new chain inside? The toy has a")
print("      single mode energy; it cannot say what the inside looks like.")
print("  (d) lambda_trap and c_c are assumptions. The lit radius (~80 m at z=10)")
print("      scales as sqrt(lambda_trap); the fold energy scales as 1/c_c.")
print("  (e) Whether the fold, once formed, can be UNDONE by removing the")
print("      deceleration. The toy has no unfolding mechanism -- the fold is")
print("      one-way in this model, and that is an assumption, not a result.")

print("\nBOTTOM LINE -- TEST 8")
print("  Past the fold, the toy's micro black hole:")
print("  - emission field: YES, collapses from comet to spherical (extension 3's shape).")
print("  - breathing: YES, trapped -- transmission 0, firewall in the chain,")
print("    downstream links go bare unless lit by another source.")
print("  - old light: NO gravitational bending; geometric capture only, at the")
print("    ordinary proton cross-section. No photon sphere, no layered discs.")
print("  - new light: YES, starts there -- the trapped mode leaks as new emission,")
print("    switching the breathing gate on in a small neighbourhood (~80 m at z=10).")
print("  - observables: R saturates at 0.8596 fm, hardening runs to +9900% at the")
print("    fold, and past it the object stops scattering like a proton at high q.")
print("  - the 'black hole' is a FIELD-TRAPPED state, not a gravitational one:")
print("    its horizon would be ~1e-40 fm. The layered discs of extension 3 do")
print("    not appear at proton scale in this toy.")
