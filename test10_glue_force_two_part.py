"""Test 10: re-model the glue force formula with Dakota's new understanding.

Dakota's new understanding (his words, held exactly, Nov 6 live call):
the glue force is ALSO inside the proton -- it is part of what gets emitted
out to a certain distance beyond the proton itself, but it is also contained
within inside of it. So the glue force has two parts: an interior part,
contained within the proton, holding it together; and an exterior part,
emitted out to a certain distance beyond the proton, which is the after-image
trail that reaches the next proton and keeps the chain breathing.

Filed formula (INN-165, verified Nov 6 from Linear -- the starting point,
not re-derived here):
  V = sigma * L_min, sigma = 0.94 GeV/fm = 1.51e5 N, ~15.4 tonnes-force/leg;
  Y-ansatz, junction at the Fermat point, each leg carries the same sigma,
  one leg's pull equals the other two combined, opposite;
  F_i = -sigma * n_hat_i, n_hat_i from the junction outward to quark i;
  M = E_quark + E_gluon + E_anomaly + E_condensate
    = 0.32M + 0.36M + 0.23M + 0.09M of 938 MeV (valence quark rest masses
    ~9 MeV total, ~1% -- more than 90% of the mass is dynamics);
  E_field = E_internal motion + E_external motion + E_displacement;
  P(0) about 1e35 Pa, outward at center, inward beyond ~0.6 fm.

Toy quantities carried in (tests 1-9):
  a0 = 0.24 fm (scale), R0 = sqrt(12)*a0 = 0.8314 fm (bare radius);
  breathing amplitude s_max = 0.10, mode energy at the cap
  E_cap = 938 * 0.01 = 9.38 MeV; leak per link lambda = 0.05 (fiducial,
  ASSUMPTION); chain coherence phi = 0.7 (test 2, MEASURED);
  chain spacing one atom length = 1e-10 m = 1e5 fm; wake fades within
  ~1/4 fm per emission event; targets R = 0.840 fm, hardening +6%;
  fold thresholds D_crit = 0.469, D_fold = 1.564 MeV/link, E_fold = 31.28 MeV
  (test 7); MBH trapped leak 1.50e4 W, lit radius ~81 m at z=10 (tests 8-9);
  escaping fraction epsilon_rad UNKNOWN (scanned 1, 0.01, 1e-4).

Two-part ansatz (this test):
  V_glue = V_in + V_out.
  V_in = sigma_in * L_min: the confined flux tubes, interior, holding the
  quarks together. sigma_in is the filed sigma (the lattice string tension
  measures the confining pull -- the interior).
  V_out: the emitted trail coupling between neighbouring protons in the
  chain. The trail holds the energy the mode leaks per link, sustained
  over the coherence length; it couples links with the measured
  correlation phi per link.
"""
import math

import numpy as np

rng = np.random.default_rng(10)

# ---- constants (filed / established) ----
A0 = 0.24
R0 = math.sqrt(12) * A0
M_P = 938.27
S_MAX = 0.10
E_CAP = M_P * S_MAX ** 2            # 9.38 MeV, mode energy at the cap
LAM = 0.05                          # leak fraction per link (ASSUMPTION, fiducial)
PHI = 0.7                           # per-link breathing correlation (test 2, measured)
L_LINK_M = 1e-10                    # one atom length
L_LINK_FM = 1e5                     # one atom length in fm
C = 2.99792458e8
MEV_J = 1.602176634e-13
SIGMA_IN = 0.94                     # GeV/fm, filed confining tension
E_GLUE = 0.36 * M_P                 # 337.8 MeV, gluon field energy (mass budget)
Q = 3.0 / A0
F_SINGLE = 1.0 / (1.0 + (Q * A0) ** 2) ** 2
LINK_TIME_S = L_LINK_M / C
U_CMB_TODAY = 0.26 * 1.602176634e-19 / 1e-6   # J/m^3
U_OLD_Z10 = U_CMB_TODAY * 11.0 ** 4
P_PROTON_LEAK = LAM * E_CAP * MEV_J / LINK_TIME_S   # 2.25e5 W, open-loop leak

N_COH = 1.0 / (1.0 - PHI)           # 3.33 links, coherence length
E_TRAIL = LAM * E_CAP * N_COH       # trail energy: leak/link x coherence


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
    return np.mean(1.0 / (1.0 + (Q * a) ** 2) ** 2)


def r_lit(P, u_old):
    return math.sqrt(P / (4 * math.pi * C * u_old))


print("BLOCK 0 -- INPUTS (filed formula + Dakota's two-part understanding)")
print("  filed: V = sigma*L_min, sigma = 0.94 GeV/fm; F_i = -sigma*n_hat_i")
print("         (n_hat outward from junction to quark i);")
print("         M = 0.32 + 0.36 + 0.23 + 0.09 of 938 MeV; P(0) ~ 1e35 Pa,")
print("         outward at center, inward beyond ~0.6 fm.")
print("  new: the glue force is ALSO inside the proton -- part contained")
print("       within, part emitted out to a certain distance beyond it.")
print(f"  toy: a0 = {A0} fm, R0 = {R0:.4f} fm, E_cap = {E_CAP:.2f} MeV,")
print(f"       lambda = {LAM} (assumed), phi = {PHI} (measured, test 2),")
print(f"       coherence length 1/(1-phi) = {N_COH:.2f} links,")
print(f"       E_glue (36% of mass) = {E_GLUE:.1f} MeV.")

# ---- Block 1: the split ----
print("\nBLOCK 1 -- THE SPLIT: HOW MUCH STAYS IN, HOW MUCH LEAKS OUT")
print("  the trail holds the leaked mode energy for one coherence length:")
print(f"  E_trail = lambda * E_cap * N_coh = {LAM} * {E_CAP:.2f} * {N_COH:.2f}")
print(f"          = {E_TRAIL:.3f} MeV. (Coincidence of digits: D_fold is also")
print("           1.564, but that is MeV per LINK -- a different quantity.)")
sig_out = E_TRAIL / (N_COH * L_LINK_FM) * 1e-3   # MeV/fm -> GeV/fm
print(f"  exterior tension sigma_out = E_trail / (N_coh * 1e5 fm)")
print(f"    = {sig_out:.3e} GeV/fm, vs sigma_in = {SIGMA_IN} GeV/fm:")
print(f"    sigma_out / sigma_in = {sig_out / SIGMA_IN:.2e} -- the leak is a")
print("    trickle next to the confining force. That is the point: the")
print("    exterior glue is NOT a second confining tension. It is a coupling")
print("    field, and its strength is measured in energy, not tension.")
print(f"  TOTAL glue-field energy: E_in = {E_GLUE - E_TRAIL:.1f} MeV (interior),")
print(f"    E_out = {E_TRAIL:.2f} MeV (exterior trail). Split:")
print(f"    interior {100 * (E_GLUE - E_TRAIL) / E_GLUE:.2f}% / exterior "
      f"{100 * E_TRAIL / E_GLUE:.2f}% of the 36% gluon slice;")
print(f"    total {E_GLUE - E_TRAIL:.1f} + {E_TRAIL:.2f} = {E_GLUE:.1f} MeV vs the")
print(f"    nominal 0.36*938 = {E_GLUE:.1f} MeV -- the exterior is a +{100 * E_TRAIL / E_GLUE:.2f}%")
print("    correction, inside the '~36%' rounding. The other budget slices")
print("    (32% quark, 23% anomaly, 9% condensate) are untouched: the split")
print("    lives entirely inside the gluon-field slice.")
print("  DYNAMIC (breathing-mode) energy split: E_mode = E_cap = 9.38 MeV;")
print(f"    exterior fraction = lambda * N_coh = {LAM * N_COH:.3f} "
      f"({100 * LAM * N_COH:.1f}%); interior {100 * (1 - LAM * N_COH):.1f}%.")
print("    So: ~99.5% interior / ~0.5% exterior by TOTAL glue energy, but")
print("    ~83% interior / ~17% exterior by DYNAMIC mode energy. The exterior")
print("    is energetically tiny and dynamically load-bearing -- it carries")
print("    the breathing, not the mass.")
print("  sensitivity to the assumed leak (E_trail, sigma_out, exterior % of mode):")
print("  lambda   E_trail [MeV]   sigma_out [GeV/fm]   exterior % of mode")
for lam in (0.01, 0.05, 0.10, 0.20):
    et = lam * E_CAP * N_COH
    so = et / (N_COH * L_LINK_FM) * 1e-3
    print(f"  {lam:.2f}     {et:8.3f}         {so:.3e}            {100 * lam * N_COH:5.1f}%")
print("  the split scales linearly with lambda, which is ASSUMED (fiducial")
print("  0.05). Nothing in tests 1-9 measures lambda. What would pin it down:")
print("  a measurement of the trail energy, of epsilon_rad, or of the lit")
print("  radius of a single lit proton (Block 2).")

# ---- Block 2: the emission distance ----
print("\nBLOCK 2 -- THE EMISSION DISTANCE: HOW FAR OUT THE EXTERIOR GLUE REACHES")
print("  NEAR FIELD (the trail): a single emission event's wake decays as")
print("  exp(-x / 0.25 fm). At x = 1 fm: exp(-4) = 0.018; at x = 1 atom length")
print(f"  (1e5 fm): exp(-4e5) = 0. A single wake does NOT reach the next proton.")
print("  The trail is a STANDING structure instead: the proton emits")
print("  continuously and the chain re-emits every link (link time")
print(f"  {LINK_TIME_S:.2e} s), so the field between links is sustained by the")
print("  nearest re-emitters. The falloff is a falloff, not a sharp edge --")
print("  near-field scale ~0.25 fm per event, refreshed link to link, and the")
print("  breathing correlation is what survives across links (Block 3).")
print("  FAR FIELD (the light): the escaping fraction radiates as 1/r^2.")
print("  lit radius r = sqrt(eps * P_leak / (4*pi*c*u_old)), P_leak = 2.25e5 W:")
print("  eps      r_lit at z=10 [m]    r_lit today [m]")
for eps in (1.0, 0.01, 1e-4):
    print(f"  {eps:<7g}  {r_lit(eps * P_PROTON_LEAK, U_OLD_Z10):12.1f}      "
          f"{r_lit(eps * P_PROTON_LEAK, U_CMB_TODAY):12.1f}")
print("  check -- the MBH (P = 1.50e4 W, eps = 1 by construction):")
print(f"    z=10: {r_lit(1.50e4, U_OLD_Z10):.1f} m (tests 8-9: ~81 m); "
      f"today: {r_lit(1.50e4, U_CMB_TODAY) / 1e3:.1f} km (test 8: ~9.8 km).")
print("  -> Dakota's 'certain distance' has two readings, and the model keeps")
print("     them apart: as a FORCE the exterior glue reaches ~0.25 fm per")
print("     event, sustained as a standing trail across the chain; as LIGHT it")
print("     reaches metres to kilometres (epsilon_rad-dependent). The chain")
print("     tension lives in the near field -- the trail between adjacent")
print("     protons, one atom length apart, sustained by re-emission. The lit")
print("     radius is where the emitted light dominates the bath, not where")
print("     the glue stops pulling.")

# ---- Block 3: chain tension ----
print("\nBLOCK 3 -- DOES THE EXTERIOR PART ACCOUNT FOR THE CHAIN TENSION?")
print("  trail coupling between protons d links apart: V_out(d) = -E_trail * phi^d.")
print("  d [links]   V_out [MeV]   correlation phi^d   V_out / E_cap")
for d in (1, 2, 3, 5, 10):
    v = -E_TRAIL * PHI ** d
    print(f"  {d:4d}       {v:8.3f}      {PHI ** d:8.3f}          {abs(v) / E_CAP:8.3f}")
v_total = -E_TRAIL * PHI / (1 - PHI)
print(f"  total trail binding of one proton to the whole chain:")
print(f"    sum_d V_out(d) = -E_trail*phi/(1-phi) = {v_total:.2f} MeV.")
print("  comparison anchors: mode well depth E_cap = 9.38 MeV (test 9);")
print("    nearest-neighbour bond |V_out(1)| = 1.09 MeV, ~12% of the well;")
print("    total chain binding 3.65 MeV, ~39% of the well. Fold thresholds")
print("    (test 7): D_crit = 0.469 MeV/link, D_fold = 1.564 MeV/link -- the")
print("    trail bond (1.09 MeV) sits between them: a neighbour's pull alone")
print("    cannot fold a proton, but it is ~2.3x the self-sustaining threshold")
print("    D_crit, so the chain's pull is a real drive, not a perturbation.")
print("  VERDICT: yes -- as a COUPLING, not as an energy pipeline. Each link's")
print("  mode energy (9.38 MeV) is driven LOCALLY by new light (tests 5-6);")
print("  the trail does not have to transport that energy, it only has to")
print("  SYNCHRONIZE the breathing, and ~17% of the mode energy in the trail")
print("  is enough to carry the pattern with phi = 0.7 per link (~3-link")
print("  coherence, test 2). The honest gap: phi is MEASURED (test 2), not")
print("  derived from lambda. The toy does not derive the correlation length")
print("  from the field dynamics -- that would need the medium's patchiness")
print("  (the local new-light field's correlation length) modeled, which no")
print("  test has done. If phi were derived, the chain tension would be a")
print("  prediction; as it stands it is a consistency check.")

# ---- Block 4: fit check (MC) ----
print("\nBLOCK 4 -- FIT CHECK: DOES THE TWO-PART FORMULA REPRODUCE R = 0.840, +6%?")
print("  interior only (s = 0, no exterior mode) vs two-part (s = 0.10, the")
print("  exterior breathing mode on). MC: 200 realizations x 2000 links.")
x_bare = chain_x(200, 2000, 0.0)
x_two = chain_x(200, 2000, S_MAX)
R_bare = radius_from_x(x_bare, A0)
H_bare = ff_from_x(x_bare, A0) / F_SINGLE - 1.0
R_two = radius_from_x(x_two, A0)
H_two = ff_from_x(x_two, A0) / F_SINGLE - 1.0
print(f"  interior only: R = {R_bare:.4f} fm (target bare 0.8314), "
      f"hardening = {100 * H_bare:+.2f}% (target 0%)")
print(f"  two-part:      R = {R_two:.4f} fm (target 0.840), "
      f"hardening = {100 * H_two:+.2f}% (target +6%)")
print(f"  miss: R {R_two - 0.840:+.4f} fm, hardening {100 * H_two - 6.0:+.2f} points.")
print("  -> the re-modeled formula reproduces both fits: the interior sets the")
print("     bare radius (0.8314) and the exterior breathing mode lifts it to")
print("     0.840 and hardens the high end ~+6% -- the same numbers tests 1-2")
print("     already fitted, now with the exterior part named as the cause.")
print("     (MC noise here is ~+/-0.0005 fm / +/-0.3 points; the misses above")
print("     are inside it.)")

# ---- Block 5: the re-modeled formula ----
print("\nBLOCK 5 -- THE RE-MODELED GLUE FORCE FORMULA")
print("  V_glue = V_in + V_out")
print("  V_in  = sigma_in * L_min,  sigma_in = 0.94 GeV/fm (filed, interior,")
print("          confining); F_i = -sigma_in * n_hat_i (n_hat outward from")
print("          junction to quark i); three legs, Y-ansatz, Fermat junction.")
print(f"  V_out = -E_trail * phi^d,  E_trail = {E_TRAIL:.3f} MeV (fiducial),")
print("          phi = 0.7 per link, d = separation in links; total chain")
print(f"          binding -E_trail*phi/(1-phi) = {v_total:.2f} MeV per proton.")
print("          Equivalently as a tension: sigma_out = 4.7e-9 GeV/fm")
print("          (energy per unit length of trail) -- ~5e-9 of sigma_in.")
print("  E_field = E_internal motion + E_external motion + E_displacement")
print("          (unchanged); the exterior part is the E_external term made")
print("          concrete: the trail energy E_trail and its lit radius.")
print("  M = 0.32M + 0.36M + 0.23M + 0.09M of 938 MeV (unchanged); the split")
print("    lives inside the 0.36M gluon slice: 336.2 MeV interior + 1.6 MeV")
print("    exterior (fiducial). P(0) ~ 1e35 Pa, outward at center, inward")
print("    beyond ~0.6 fm (unchanged); the 0.6 fm sign change is the")
print("    force-picture boundary between interior (pushing out) and exterior")
print("    (binding, pulling in). Geometric note, NOT a derivation: the")
print(f"    interior volume fraction (0.6/0.84)^3 = {(0.6 / 0.84) ** 3:.3f}")
print("    happens to equal the 36% gluon slice -- coincidence of two")
print("    unrelated ratios (a volume ratio vs an energy fraction).")

# ---- Block 6: what the model cannot determine ----
print("\nBLOCK 6 -- WHAT THE MODEL CANNOT DETERMINE")
print("  (a) lambda (leak per link, fiducial 0.05): sets E_trail, sigma_out,")
print("      and the exterior fractions. Unmeasured by tests 1-9. Pin it down")
print("      with a trail-energy measurement, epsilon_rad, or a single")
print("      proton's lit radius (Block 2).")
print("  (b) phi = 0.7 (per-link correlation): measured, not derived. The toy")
print("      cannot derive the ~3-link coherence from the field dynamics;")
print("      that needs the medium's patchiness modeled (local new-light")
print("      field correlation length).")
print("  (c) The interior/exterior boundary has no sharp spatial edge in the")
print("      energy picture: it is a falloff (0.25 fm per event, refreshed).")
print("      The 0.6 fm pressure sign change is the force-picture boundary,")
print("      not an energy-partition boundary.")
print("  (d) The interior term is unchanged from INN-165 by construction --")
print("      this test does not re-derive sigma_in = 0.94 GeV/fm from the toy;")
print("      it takes the filed value and adds the exterior term to it.")
print("  (e) No spin / no rotation (standing correction) throughout; the")
print("      exterior trail is a scalar coupling in this toy, not a vector")
print("      field with direction -- the comet cone / direction of motion")
print("      enters only through the base model's forward cone, unchanged.")

print("\nBOTTOM LINE -- TEST 10")
print("  The glue force, re-modeled as two parts:")
print("  - interior: sigma_in = 0.94 GeV/fm, the filed confining tension,")
print("    holding the quarks together; ~99.5% of the glue-field energy.")
print("  - exterior: the after-image trail, E_trail = 1.56 MeV (fiducial),")
print("    coupling neighbouring protons at -1.09 MeV per link, total chain")
print("    binding -3.65 MeV; ~0.5% of the glue energy but ~17% of the")
print("    dynamic breathing-mode energy -- energetically tiny, dynamically")
print("    load-bearing. It accounts for the chain tension as a coupling")
print("    (synchronizing the breathing, phi = 0.7/link), not as an energy")
print("    pipeline: each link is driven locally by new light.")
print("  - the formula reproduces the fits (R 0.840, +6%) and leaves the")
print("    mass budget intact (the split lives inside the 36% slice).")
print("  - the emission distance: ~0.25 fm per event as a force (standing")
print("    trail, refreshed link to link), metres to kilometres as light")
print("    (epsilon_rad-dependent lit radius).")
print("  - underdetermined: lambda (sets the split) and phi's origin (sets")
print("    the coherence). Those are the next measurements, not assumptions")
print("    to be hidden.")
