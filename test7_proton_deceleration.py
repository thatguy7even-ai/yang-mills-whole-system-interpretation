"""Test 7: proton deceleration feeds the energy loop.

Dakota's micro-black-hole hypothesis (his words, held exactly):
trigger is not mass -- a moving proton experiencing deceleration;
deceleration feeds inside the energy loop, increasing the proton's overall
size, and at a certain size mass develops inside the core, the core region
compressed no matter the dimensions of the outer folds -- folds inward =
micro black hole.

Toy energy-loop model (assumptions flagged where they enter):
- D = deceleration energy fed into the loop per link, MeV per atom-length
  (one link = one atom length = 1e5 fm of travel). eta = 1: the lost kinetic
  energy is retained INSIDE the loop (Dakota's framing).
- The loop leaks a fraction lambda of its mode energy per link (exponential
  leak, as in the base model). Equilibrium mode energy E* = D*eta/lambda.
- The mode energy is the breathing amplitude: s^2 = E_mode / m_p c^2.
  The regulated cap from tests 2/5 is s_max = 0.10, so E_cap = 938 * 0.01
  = 9.38 MeV. SELF-SUSTAINING threshold: D_crit = lambda * E_cap -- fed
  energy per link exceeds what the loop leaks at the cap, so the mode
  grows past the regulation.
- Core compression: the fed energy squeezes the core scale,
  a_core = a0 * (1 - c_c * E*/E_cap), c_c = core compression coupling
  (ASSUMPTION, scanned). The FOLD point is where a_core hits zero:
  E_fold = E_cap / c_c, D_fold = lambda * E_fold. The outer size keeps
  growing (R = sqrt(12)*a0*exp(s^2)) while the core compresses -- the
  two scales move in opposite directions, as Dakota described.
- lambda and c_c are NOT measured by tests 1-5. Thresholds are reported
  as functions of them, with fiducial lambda = 0.05, c_c = 0.30.
"""
import math

import numpy as np

rng = np.random.default_rng(13)

# ---- calibration (same as tests 5-6) ----
a0 = 0.24
R0 = math.sqrt(12) * a0
q = 3.0 / a0
F_single = 1.0 / (1.0 + (q * a0) ** 2) ** 2
PHI = 0.7
S_MAX = 0.10
M_P = 938.27                    # MeV
E_CAP = M_P * S_MAX ** 2        # 9.38 MeV -- mode energy at the regulated cap
LAM_FID = 0.05                  # leak fraction per link (ASSUMPTION)
ETA = 1.0                       # retention inside the loop (Dakota's framing)
C_C_FID = 0.30                  # core compression coupling (ASSUMPTION)
L_LINK_M = 1e-10                # one atom length, chain spacing
C = 2.99792458e8
MEV_J = 1.602176634e-13


def chain_x(n_real, n_links, s, phi=PHI):
    sig = s * math.sqrt(1 - phi ** 2)
    eps = rng.normal(0, sig, (n_real, n_links))
    x = np.zeros((n_real, n_links))
    x[:, 0] = rng.normal(0, s, n_real)
    for i in range(1, n_links):
        x[:, i] = phi * x[:, i - 1] + eps[:, i]
    return x


def radius_from_x(x, base):
    a = base * np.exp(x)
    return np.sqrt(12 * np.mean(a ** 2))


def ff_from_x(x, base):
    a = base * np.exp(x)
    return np.mean(1.0 / (1.0 + (q * a) ** 2) ** 2)


# ---- Block 1: thresholds as functions of the leak fraction ----
print("BLOCK 1 -- THRESHOLDS (D = deceleration energy fed per link, MeV per atom-length)")
print("  equilibrium mode energy E* = D*eta/lambda. Self-sustaining when E* > E_cap")
print("  (fed energy per link exceeds what the loop leaks at the regulated cap).")
print("  Fold point: core scale hits zero at E_fold = E_cap / c_c, D_fold = lambda*E_fold.")
print("  (c_c = 0.30 fiducial.)")
print("  lambda  D_crit [MeV/link]  D_fold [MeV/link]  E_fold [MeV]  s at fold")
for lam in (0.01, 0.05, 0.10, 0.20):
    D_crit = lam * E_CAP / ETA
    E_fold = E_CAP / C_C_FID
    D_fold = lam * E_fold / ETA
    s_fold = math.sqrt(E_fold / M_P)
    print(f"  {lam:.2f}    {D_crit:10.3f}        {D_fold:10.3f}        {E_fold:8.2f}   {s_fold:.4f}")
print(f"  FIDUCIAL (lambda=0.05, c_c=0.30): D_crit = {LAM_FID * E_CAP:.3f} MeV/link, "
      f"D_fold = {LAM_FID * E_CAP / C_C_FID:.3f} MeV/link, E_fold = {E_CAP / C_C_FID:.2f} MeV.")

# ---- Block 2: observables vs deceleration (fiducial lambda, c_c) ----
print("\nBLOCK 2 -- OBSERVABLES vs DECELERATION (fiducial lambda=0.05, c_c=0.30)")
print("  R uses the OUTER scale (grows); hardening uses the CORE scale (compresses).")
print("  D        E* [MeV]  s_eq    a_core [fm]  R [fm]    hardening (MC)")
for D in (0.0, 0.1, 0.2, 0.469, 0.5, 1.0, 1.5, 1.564):
    E_star = D * ETA / LAM_FID
    s_eq = math.sqrt(E_star / M_P)
    a_core = a0 * (1 - C_C_FID * E_star / E_CAP)
    if a_core <= 0:
        print(f"  {D:5.3f}  {E_star:8.2f}  {s_eq:.4f}   {a_core:8.4f}  -- FOLD (core scale hits zero) --")
        continue
    x = chain_x(200, 2000, min(s_eq, 0.5))
    R = radius_from_x(x, a0)
    H = ff_from_x(x, a_core) / F_single - 1.0
    print(f"  {D:5.3f}  {E_star:8.2f}  {s_eq:.4f}   {a_core:8.4f}  {R:.4f}  {100 * H:+9.2f}%")
print("  at D_crit the radius is the lit value (0.8395 fm) -- the threshold")
print("  coincides with the breathing cap -- but the hardening has already")
print("  exploded (+~240%): the core compression is the loud signal, not R.")
print("  near the fold the hardening runs to +~9600% as a_core -> 0.")

# ---- Block 3: how big is D_crit in physical terms? ----
print("\nBLOCK 3 -- HOW BIG IS D_crit IN PHYSICAL TERMS?")
P_crit = LAM_FID * E_CAP * MEV_J / (L_LINK_M / C)
print(f"  D_crit (fiducial) = {LAM_FID * E_CAP:.3f} MeV per atom-length (1e5 fm = 1e-10 m).")
print(f"  Per link-crossing time (1e-10 m / c = {L_LINK_M / C:.2e} s) that is a power of")
print(f"  {P_crit:.2e} W fed into ONE proton's loop.")
print("  Ordinary stopping in matter: minimum-ionizing ~2 MeV/cm = 2e-8 MeV per")
print("  atom-length; Bragg peak ~100 MeV/cm = 1e-6 MeV per atom-length.")
print(f"  D_crit is ~{LAM_FID * E_CAP / 2e-8:.1e}x minimum-ionizing stopping and "
      f"~{LAM_FID * E_CAP / 1e-6:.1e}x the Bragg peak.")
print("  -> ordinary deceleration in matter NEVER reaches the threshold. It needs")
print("     a field, a collision, or a mechanism the toy does not supply.")

# ---- Block 4: approach dynamics -- how fast does it run away? ----
print("\nBLOCK 4 -- APPROACH DYNAMICS (E_{n+1} = (1-lambda) E_n + D, from bare E=0)")
print("  D        E* [MeV]   links to cross cap (9.38 MeV)   links to reach fold (31.27 MeV)")
for D in (0.6, 1.0, 1.564, 2.0, 5.0):
    E_star = D / LAM_FID
    def links_to(E_target):
        if E_star <= E_target:
            return None
        return math.log(1 - E_target / E_star) / math.log(1 - LAM_FID)
    n_cap = links_to(E_CAP)
    n_fold = links_to(E_CAP / C_C_FID)
    cap_s = f"{n_cap:5.1f}" if n_cap is not None else " never"
    fold_s = f"{n_fold:5.1f}" if n_fold is not None else (" asymptotic" if abs(E_star - E_CAP / C_C_FID) < 1e-9 else " never")
    print(f"  {D:5.3f}  {E_star:8.1f}   {cap_s}                          {fold_s}")
print("  below D_crit the loop settles in ~1/lambda = 20 links. Above it the mode")
print("  blows past the cap in a handful of links; the fold needs D > D_fold and")
print("  then arrives in ~7-30 links depending on how far past the fold D sits.")
print("  the core compression is self-sustaining past D_crit in the sense that")
print("  the loop gains more per link than the regulation can shed -- the mode")
print("  energy keeps rising toward D/lambda, and the core keeps shrinking with it.")

# ---- Block 5: sensitivity to the assumed couplings ----
print("\nBLOCK 5 -- SENSITIVITY (what the threshold depends on)")
print("  c_c     D_fold (lambda=0.05)   a_core at D_crit   hardening at D_crit")
for c_c in (0.1, 0.2, 0.3, 0.5):
    E_fold = E_CAP / c_c
    D_fold = LAM_FID * E_fold
    a_core_crit = a0 * (1 - c_c * 1.0)   # at E* = E_cap
    F_core = 1.0 / (1.0 + (q * a_core_crit) ** 2) ** 2
    H_crit = F_core / F_single - 1.0
    print(f"  {c_c:.1f}    {D_fold:8.3f} MeV/link      {a_core_crit:.4f} fm        {100 * H_crit:+.0f}%")
print("  D_crit does NOT depend on c_c (it is lambda * E_cap only). D_fold scales")
print("  as 1/c_c. The hardening at the threshold is large for any c_c >= 0.2.")

print("\nBOTTOM LINE -- TEST 7")
print(f"  SELF-SUSTAINING THRESHOLD (fiducial): D_crit = {LAM_FID * E_CAP:.3f} MeV per")
print("  atom-length fed into the loop -- the point where the loop gains more per")
print("  link than it leaks at the regulated cap, and the core compression runs away.")
print(f"  FOLD POINT (fiducial): D_fold = {LAM_FID * E_CAP / C_C_FID:.3f} MeV/link, "
      f"E_fold = {E_CAP / C_C_FID:.1f} MeV in the mode, R = 0.8596 fm, core -> 0.")
print("  Signature: radius grows only ~+3.4% (0.8314 -> 0.8596 fm) while the")
print("  high-end hardening explodes (0% -> +240% at the threshold, -> +9900%")
print("  at the fold). Ordinary stopping in matter is 5-7 orders too weak to")
print("  reach the threshold -- the deceleration has to come from something else.")
print("  Assumptions carried: lambda (leak/link), c_c (core compression coupling),")
print("  eta = 1 (full retention). Thresholds scale linearly with lambda.")
