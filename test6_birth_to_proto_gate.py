"""Test 6: birth-to-proto bubble WITH the breathing gate.

Dakota's test-5 extensions 1, 2, 5 (his words, held exactly):
1. BREATHING GATE: the breathing flips ON at star creation -- the medium's
   breathing mode IS stars themselves, not merely triggered by them.
2. STARS AS LIVING SYSTEMS: a star is a living system that consumes and
   produces its own necessity; 'living' needs redefining -- everything is a
   food chain at no matter what level.
5. STELLAR SECOND STAGE: the sun creates light at different levels through
   to its core; denser, darker light is kept inside by something at the
   surface level -- there may be a second stage to the proton that only
   exists inside the pressurization of a star.

Builds on test5_birth_to_proto.py (same calibration, same functions).
New vs test 5: test 5 gated breathing SPATIALLY (on where u_new > u_old).
Here the gate is TEMPORAL and LIVING: breathing is OFF everywhere before
first stars (t < t_sf = 0.5), and after star creation it is the star's own
metabolism that runs the mode -- it ramps as the star forms, and it follows
the star's life (with a possible medium memory after the star dies).
The stellar second stage is added as a layer for protons INSIDE a star.
"""
import math

import numpy as np

rng = np.random.default_rng(11)

# ---- calibration (same as test 5) ----
a0 = 0.24
R0 = math.sqrt(12) * a0
q = 3.0 / a0
F_single = 1.0 / (1.0 + (q * a0) ** 2) ** 2
S_MAX = 0.10
PHI = 0.7
S_FLOOR = 1e-5
T_SF = 0.5          # first stars
F_LIT_T1 = 0.30     # test-5 lit fraction at t=1


def radius(a):
    return np.sqrt(12 * np.mean(np.asarray(a) ** 2))


def ff(a):
    return np.mean(1.0 / (1.0 + (q * np.asarray(a)) ** 2) ** 2)


def hard(f):
    return f / F_single - 1.0


def breathing_chain(n_real, n_links, s, base=a0, phi=PHI):
    sig = s * math.sqrt(1 - phi ** 2)
    eps = rng.normal(0, sig, (n_real, n_links))
    x = np.zeros((n_real, n_links))
    x[:, 0] = rng.normal(0, s, n_real)
    for i in range(1, n_links):
        x[:, i] = phi * x[:, i - 1] + eps[:, i]
    return base * np.exp(x)


# ---- Block 0: re-baseline the lit and void proton (same MC as test 5) ----
print("BLOCK 0 -- RE-BASELINE (400 chains x 2000 links, same as test 5)")
n_real, n_links = 400, 2000
a_lit = breathing_chain(n_real, n_links, S_MAX)
a_void = breathing_chain(n_real, n_links, S_FLOOR)
R_lit, H_lit = radius(a_lit), hard(ff(a_lit))
R_void, H_void = radius(a_void), hard(ff(a_void))
print(f"  LIT  (s=0.10): R = {R_lit:.4f} fm  hardening = {100 * H_lit:+.2f}%")
print(f"  VOID (s=1e-5): R = {R_void:.4f} fm  hardening = {100 * H_void:+.2f}%")

# ---- Block A: the gate is a metabolism ramp, not a switch ----
print("\nBLOCK A -- THE GATE IS A METABOLISM RAMP, NOT A SWITCH")
print("  after star creation the breathing mode ramps as the star forms:")
print("  s(t) = s_max * (1 - exp(-(t - t_sf)/tau)); 2nd-generation stars are")
print("  primed by the debris medium (tau/priming). Before t_sf, s = 0 everywhere.")
print("  tau    priming  s(t=1)   R_lit(t=1)   H(t=1, MC)")
for tau in (0.05, 0.10, 0.20):
    for priming in (1.0, 3.0):
        s1 = S_MAX * (1 - math.exp(-(1 - T_SF) / (tau / priming)))
        a = breathing_chain(200, 2000, s1)
        print(f"  {tau:.2f}   {priming:.0f}x      {s1:.4f}    {radius(a):.4f} fm   {100 * hard(ff(a)):+.2f}%")
print("  before t_sf: every proton in the bubble is bare (R = 0.8314 fm) --")
print("  same as test 5's f_lit = 0, but now it is a TEMPORAL gate, not a")
print("  spatial one: there is no lit region at all until stars exist.")
print("  the ramp only matters for slow 1st-generation formation (tau = 0.20):")
print("  s reaches only ~0.092 by t=1, R ~0.838 instead of 0.8398. Primed")
print("  2nd-generation stars (priming 3x) are fully on by t=1 at any tau.")

# ---- Block B: living medium -- does the breathing outlive the star? ----
print("\nBLOCK B -- LIVING MEDIUM: DOES THE BREATHING OUTLIVE THE STAR?")
print("  stars form continuously t_sf..1; each lives tau_life (ASSUMPTION 0.30")
print("  bubble-time units). Variant (a): breathing follows the living star.")
print("  Variant (b): the medium remembers -- breathing persists tau_mem = 0.20")
print("  after the star dies. Formation rate = 0.30/0.50 = 0.60 per unit t.")
TAU_LIFE = 0.30
TAU_MEM = 0.20
rate = F_LIT_T1 / (1 - T_SF)
f_a = rate * min(TAU_LIFE, 1 - T_SF)
f_b = rate * min(TAU_LIFE + TAU_MEM, 1 - T_SF)
for name, f in (("(a) follows the star", f_a),
                ("(b) medium memory", f_b),
                ("test 5 (all star regions breathe)", F_LIT_T1)):
    R_vol = math.sqrt(f * R_lit ** 2 + (1 - f) * R_void ** 2)
    H_vol = f * H_lit + (1 - f) * H_void
    print(f"  {name}: breathing fraction at t=1 = {f:.2f}  "
          f"R_vol = {R_vol:.4f} fm  hardening ~ {100 * H_vol:+.2f}%")
print("  -> with finite star lifetimes, the LIVING gate cuts the breathing")
print("     volume at t=1 from 0.30 (test 5) to 0.18, and R_vol drops with it.")
print("     The medium-memory variant restores test 5's 0.30. Which is right is")
print("     undetermined: it is the question of whether the mode is the star")
print("     (dies with it) or the medium (remembers it). If stars live longer")
print("     than the bubble (tau_life > 0.5), (a) = (b) = test 5.")

# ---- Block C: stellar second stage -- protons INSIDE a star ----
print("\nBLOCK C -- STELLAR SECOND STAGE (protons INSIDE a star)")
print("  interior proton: trapped dense light adds a second breathing channel")
print("  s_tot^2 = s^2 + s2^2 (s2 = trapped-light amplitude, scanned -- NOT")
print("  measured), and stellar pressure compresses the link scale")
print("  a0_int = a0*(1 - pc) (pc = pressure compression, scanned). The surface")
print("  blocks the dense light: transmission = 0, so the EXTERIOR sees none")
print("  of this. Surface proton: one-sided, s2/sqrt(2), pc/2.")
print("  s2     pc     R_interior   H_interior   R_surface    H_surface")
for s2 in (0.0, 0.05, 0.10, 0.20):
    s_tot = math.sqrt(S_MAX ** 2 + s2 ** 2)
    for pc in (0.0, 0.05):
        a_int = breathing_chain(200, 2000, s_tot, base=a0 * (1 - pc))
        R_int, H_int = radius(a_int), hard(ff(a_int))
        s_surf = math.sqrt(S_MAX ** 2 + (s2 / math.sqrt(2)) ** 2)
        a_surf = breathing_chain(200, 2000, s_surf, base=a0 * (1 - pc / 2))
        print(f"  {s2:.2f}  {pc:.2f}   {R_int:.4f} fm   {100 * H_int:+6.2f}%    "
              f"{radius(a_surf):.4f} fm   {100 * hard(ff(a_surf)):+6.2f}%")
print("  the second stage moves the INTERIOR proton (up to ~+0.02 fm at s2=0.20,")
print("  partly offset by pressure compression), but the exterior observable is")
print("  UNCHANGED: the dense light cannot escape the surface, so no outside")
print("  measurement sees it. The second stage stays hidden in this toy unless")
print("  a probe reaches the interior (a neutrino could, in principle -- not modeled).")
print("  NOTE: s2 and pc are free parameters. Nothing in tests 1-5 fixes them;")
print("  the table is a sensitivity map, not a prediction.")

# ---- Block D: does the gate change the fit vs test 5? ----
print("\nBLOCK D -- DOES THE GATE CHANGE THE FIT vs TEST 5?")
print(f"  closed fit in a lit region, breathing fully on: R = {R_lit:.4f} fm, "
      f"hardening = {100 * H_lit:+.2f}% -- UNCHANGED from test 5.")
print("  the gate changes WHEN and WHERE the fit closes, not the closed value:")
print("  - before first stars: the whole bubble is bare, R = 0.8314 fm.")
print("  - after: lit regions close to 0.8398 fm on the star's formation ramp;")
print("    void pockets stay bare at 0.8314 fm.")
print("  - with finite star lifetimes the breathing VOLUME at t=1 is smaller")
print("    than test 5 assumed (0.18 vs 0.30) unless the medium remembers.")
print("  - the stellar second stage is a hidden interior layer: it moves")
print("    interior-proton numbers only, and no exterior observable in the toy.")

print("\nBOTTOM LINE -- TEST 6")
print("  The breathing gate (extension 1+2) does not move the closed fit.")
print("  It moves the PATTERN: breathing is off everywhere before star creation,")
print("  ramps with each star's formation, and -- if the mode is the star and")
print("  not the medium -- dies with the star, shrinking the breathing volume")
print("  at the proto-galaxy epoch. The second stage (extension 5) stays hidden")
print("  from the outside by construction: the surface blocks the dense light.")
print("  Open: tau (formation ramp), tau_life / tau_mem (does the mode outlive")
print("  the star), s2 and pc (second-stage amplitude and pressure compression).")
