"""Test 5: birth-to-proto bubble.

Dakota's new understanding (his words, held exactly):
- The CMB is not a negligible layer. It is a field helper and a strengthening
  aspect: part of the medium itself. Light emits from its source as a
  continuous chain throughout space and time, so the first light is still
  present as the medium the new light travels through.
- Light is everywhere in the known conceivable universe. An emission source in
  one region couples with emission sources in other portions of that region.
  Regions with no stellar bodies are the void pockets (no local emission).
- The CMB is emitted light from the very first light source -- an echo of the
  first source, with no source behind it anymore. New light (from stars) now
  rides on top of it, coming through the medium of first light.
- The first emission may NOT be the same type of light as what stars emit now
  -- different waveforms/types. Model old light and new light as potentially
  different kinds.
- The breathing (the fluctuation that fixes the fit) is driven by the source
  of the NEW light: the star/proton's local emission region. New light is
  produced behind each proton in the chain. At the first spark there was no
  new emission until stars / proto-galaxies / proto-clusters formed.
- The present universe is oversaturated with waveforms from countless stellar
  bodies inside galaxies and clustered galaxies. Between galaxies there is no
  emission on the galactic disc itself, but refractive light from particle
  emission above and below the plane of the discs lets the internal structure
  of a galaxy be perceived from inside it.
- Model scope: from the first spark to the point where proto-galaxies start to
  form -- a REGIONAL bubble, a contained expanding space-time. Do NOT model
  the whole current expansive medium.
- Center/epicenter logic (his): the NEWEST forming galaxies are probably the
  epicenter -- the first explosion threw the oldest stuff farthest out, and the
  newer settling stuff is how you extrapolate the beginning. The apparent edge
  line is actually the new cooling area: a fluctuation of CMB inside a density
  that is nowhere else. Measure CIRCUMFERENTIALLY -- around the bubble's
  circumference, not across the whole universe.

Calibration (same as tests 1-4):
- Exponential leak per link, R = sqrt(12)*a, a0 = 0.24 fm -> R0 = 0.8314 fm.
- Dipole F(q) = 1/(1+(q*a)^2)^2; high end at q*a0 = 3; F_single = 0.01.
- Targets: R = 0.840 fm, high-end hardening +6%.
- Breathing (test 2): AR(1) ln a, phi = 0.7, stationary s = 0.10,
  innovation sig_eps = 0.0714 -> R = 0.8395, hardening ~+6%.
- Aura alternative (test 3): w = 0.0081 at a0/2, tail z = 0.0089 at 2a0,
  s = 0 -> R = 0.8396, +6.10%. Discriminator: along the chain.
- CMB as plain layer (test 4): CLEAN NULL. u_CMB/u_p ~ 1e-48 today,
  uniform to 1e-5, cannot drive breathing, no epoch trace.

Test 5 structure:
- Bubble: t in [0,1], spark (t=0, 1+z = 1100) to proto-galaxy epoch
  (t=1, 1+z = 11). (1+z) = 1100^(1-t) * 11^t. First stars at t_sf = 0.5.
- Old light: uniform bath, u_old(t) = u_CMB_today * (1+z)^4.
- New light: local stellar emission. Two anchors: (a) near a star,
  solar constant at 1 AU; (b) collective galactic field, standard
  interstellar radiation field u_ISRF ~ 1 eV/cm^3 (literature anchor,
  solar neighbourhood -- NOT measured by us).
- Breathing gate: the medium's breathing mode is ON (s = 0.10) where new
  light is present above the bath, OFF (s = s_floor = 1e-5, CMB anisotropy)
  in void pockets. This is a switch, not an energy-density scaling: test 4
  showed raw energy-density coupling needs amplification ~1e45 (u) to move
  anything, so the medium must be a REGULATED mode that the new light
  triggers locally. The gate boundary is where u_new = u_old.
- Circumference: shell r in [0.9, 1], the newest cooling front. CMB
  fluctuation there delta_shell = delta_0 * (1 + D), D = density contrast
  of the cooling front (scanned; D is NOT given by the model). Adiabatic
  variant delta_0 * (1 + D/3).
- Old vs new type: lambda_old(z) = 2898/T(z) um; lambda_new = 0.5 um
  (optical starlight). Both >> a0. Direct-component weight limits
  (test-4 Block 1 method) for each.
"""
import math

import numpy as np

rng = np.random.default_rng(7)

# ---- calibration ----
a0 = 0.24
R0 = math.sqrt(12) * a0
q = 3.0 / a0
F_single = 1.0 / (1.0 + (q * a0) ** 2) ** 2
R_TARGET = 0.840
H_TARGET = 0.06
S_MAX = 0.10          # breathing amplitude, test 2
PHI = 0.7
SIG_EPS = S_MAX * math.sqrt(1 - PHI ** 2)   # 0.0714
S_FLOOR = 1e-5        # CMB anisotropy dT/T -- floor where no new light
DELTA0 = 1e-5         # CMB anisotropy, interior

# ---- measured / standard anchors ----
T0 = 2.725            # K, CMB today
SIGMA = 5.670374419e-8
C = 2.99792458e8
EV_PER_J = 6.241509074e18
u_cmb_today_J_m3 = 4 * SIGMA * T0 ** 4 / C
u_cmb_today = u_cmb_today_J_m3 * EV_PER_J / 1e6   # eV/cm^3
u_p = 378e6 / 1e-39                                # 378 MeV/fm^3 -> eV/cm^3
SOLAR_CONST = 1361.0                               # W/m^2 at 1 AU
u_star_1AU = SOLAR_CONST / C * EV_PER_J / 1e6      # eV/cm^3
U_ISRF = 1.0                                       # eV/cm^3, standard ISRF anchor
LAM_NEW_UM = 0.5                                   # optical starlight

print("ANCHORS")
print(f"  u_CMB today = {u_cmb_today:.3f} eV/cm^3; u_p = {u_p:.3e} eV/cm^3")
print(f"  u_CMB/u_p today = {u_cmb_today / u_p:.3e}")
print(f"  u_star at 1 AU = {u_star_1AU:.3e} eV/cm^3; u_star/u_CMB today = {u_star_1AU / u_cmb_today:.3e}")
print(f"  u_star(1AU)/u_p = {u_star_1AU / u_p:.3e}")
print(f"  u_ISRF (standard anchor) = {U_ISRF:.1f} eV/cm^3; u_ISRF/u_CMB today = {U_ISRF / u_cmb_today:.2f}")

# ---- Block 1: bubble timeline, bath vs new light ----
print("\nBLOCK 1 -- BUBBLE TIMELINE (spark t=0 to proto-galaxy epoch t=1)")
print("  t     1+z    T_CMB[K]  u_old/u_p    u_old/u_ISRF   u_star(1AU)/u_old   r_eq[AU]")
for t in (0.0, 0.25, 0.5, 0.6, 0.8, 1.0):
    omz = 1100.0 ** (1 - t) * 11.0 ** t
    T = T0 * omz
    u_old = u_cmb_today * omz ** 4
    r_eq = math.sqrt(u_star_1AU / u_old)   # AU where starlight = bath
    print(f"  {t:.2f}  {omz:7.1f}  {T:8.1f}  {u_old / u_p:.3e}  {u_old / U_ISRF:9.3e}  "
          f"{u_star_1AU / u_old:10.3e}  {r_eq:9.1f}")
# when does the collective starlight field overtake the bath?
z_cross = (U_ISRF / u_cmb_today) ** 0.25 - 1
print(f"  collective starlight (ISRF) overtakes CMB at 1+z = {(U_ISRF / u_cmb_today) ** 0.25:.3f}, z = {z_cross:.2f}")
print(f"  at t=1 (z=10): u_old/u_ISRF = {(11.0 ** 4) * u_cmb_today / U_ISRF:.0f} -- bath still dominates the VOLUME;")
print(f"  new light wins only inside ~{math.sqrt(u_star_1AU / (u_cmb_today * 11.0 ** 4)):.0f} AU of a forming star.")
print(f"  today: bath vs ISRF = {u_cmb_today / U_ISRF:.2f}; starlight wins out to "
      f"{math.sqrt(u_star_1AU / u_cmb_today):.0f} AU from a star.")


def radius(a):
    return np.sqrt(12 * np.mean(np.asarray(a) ** 2))


def ff(a):
    return np.mean(1.0 / (1.0 + (q * np.asarray(a)) ** 2) ** 2)


def hard(f):
    return f / F_single - 1.0


def breathing_chain(n_real, n_links, s, phi=PHI):
    sig = s * math.sqrt(1 - phi ** 2)
    eps = rng.normal(0, sig, (n_real, n_links))
    x = np.zeros((n_real, n_links))
    x[:, 0] = rng.normal(0, s, n_real)
    for i in range(1, n_links):
        x[:, i] = phi * x[:, i - 1] + eps[:, i]
    return a0 * np.exp(x)


def window_R(a, w=5):
    n = a.shape[1] // w * w
    aw = a[:, :n].reshape(a.shape[0], -1, w)
    return np.sqrt(12 * np.mean(aw ** 2, axis=2))


# ---- Block 2: lit region vs void pocket (the fit is LOCAL) ----
print("\nBLOCK 2 -- LIT REGION vs VOID POCKET (MC, 400 chains x 2000 links)")
n_real, n_links = 400, 2000
a_lit = breathing_chain(n_real, n_links, S_MAX)
a_void = breathing_chain(n_real, n_links, S_FLOOR)
R_lit, H_lit = radius(a_lit), hard(ff(a_lit))
R_void, H_void = radius(a_void), hard(ff(a_void))
print(f"  LIT  (new light present, s=0.10): R = {R_lit:.4f} fm  hardening = {100 * H_lit:+.2f}%  (target 0.840, +6%)")
print(f"  VOID (no local emission, s=1e-5): R = {R_void:.4f} fm  hardening = {100 * H_void:+.2f}%  (bare proton)")
print(f"  lit-void radius gap = {R_lit - R_void:.4f} fm ({100 * (R_lit / R_void - 1):+.2f}%)")
Rw_lit = window_R(a_lit)
Rw_void = window_R(a_void)
print(f"  along-chain discriminator, lit: local 5-link R std = {100 * Rw_lit.std() / Rw_lit.mean():.2f}% "
      f"(breathing: coherent ~3-link breaths)")
print(f"  along-chain discriminator, void: local 5-link R std = {100 * Rw_void.std() / Rw_void.mean():.2f}% (uniform)")
print(f"  analytic lit R = R0*exp(s^2) = {R0 * math.exp(S_MAX ** 2):.4f} fm; "
      f"void R = {R0 * math.exp(S_FLOOR ** 2):.4f} fm")

# volume average over the bubble at t=1, lit fraction f_lit (parameter)
print("\n  VOLUME AVERAGE over the bubble at t=1 (lit fraction f_lit -- parameter, proto-galaxies are clustered):")
for f_lit in (0.1, 0.3, 0.5):
    R_vol = math.sqrt(f_lit * R_lit ** 2 + (1 - f_lit) * R_void ** 2)
    H_vol = f_lit * H_lit + (1 - f_lit) * H_void   # approx., hardening ~ linear in f for small values
    print(f"    f_lit={f_lit:.1f}: R_vol = {R_vol:.4f} fm, hardening ~ {100 * H_vol:+.2f}%")
print("  -> the measured 0.840 is the LIT-region value, not a cosmic average.")
print("     A proton in a void pocket measures the bare 0.831 fm in this toy.")

# ---- Block 3: time evolution of the fit across the bubble ----
print("\nBLOCK 3 -- FIT vs TIME (lit fraction grows after first stars, t_sf = 0.5)")
print("  t     1+z    f_lit   R_lit    R_void   R_vol    hardening_vol")
for t in (0.0, 0.25, 0.5, 0.6, 0.8, 1.0):
    omz = 1100.0 ** (1 - t) * 11.0 ** t
    f_lit = 0.0 if t < 0.5 else 0.3 * (t - 0.5) / 0.5
    R_vol = math.sqrt(f_lit * R_lit ** 2 + (1 - f_lit) * R_void ** 2)
    H_vol = f_lit * H_lit
    print(f"  {t:.2f}  {omz:7.1f}  {f_lit:.2f}   {R_lit:.4f}   {R_void:.4f}   {R_vol:.4f}    {100 * H_vol:+.2f}%")
print("  before first stars (t < 0.5): no new light anywhere -> every proton is bare, R = 0.8314.")
print("  the fit CLOSES only where new light has switched the breathing mode on.")

# ---- Block 4: CMB as MEDIUM (not layer) -- coupling of new light through the bath ----
print("\nBLOCK 4 -- CMB AS MEDIUM: does the bath set the coupling g between new light and chain?")
print("  model: innovation sigma_eps ~ g, g ~ u_old^alpha; u_old falls by (1100/11)^4 = 1e8 across the bubble.")
print("  alpha   s_early (t=0)   R_early (no cap)   R_early (capped at s_max=0.10)")
u_ratio = (1100.0 / 11.0) ** 4
for alpha in (0.0, 0.01, 0.014, 0.05, 0.25, 0.5, 1.0):
    s_early = S_MAX * u_ratio ** alpha
    R_nocap = R0 * math.exp(min(s_early, 3.0) ** 2) if s_early < 3 else float("inf")
    R_cap = R0 * math.exp(min(s_early, S_MAX) ** 2)
    print(f"  {alpha:.3f}   {s_early:12.3f}   {R_nocap:>10.4f} fm        {R_cap:.4f} fm")
alpha_max = math.log(1.3) / math.log(u_ratio)
print(f"  without the cap, alpha must be < ~{alpha_max:.3f} or the early bubble overshoots R > 0.845.")
print("  -> the medium MUST be regulated (self-capping, as test 2 found). With the cap,")
print("     the CMB-as-medium changes NOTHING about the fit at any alpha: test 4's null stands")
print("     in its medium form too. The bath is the road, not the driver.")

# ---- Block 5: circumferential measure -- the newest cooling front ----
print("\nBLOCK 5 -- CIRCUMFERENTIAL MEASURE (shell r in [0.9, 1]: newest formations, new cooling area)")
print("  delta_shell = delta_0 * (1 + D), D = density contrast of the cooling front (scanned; D not given by model).")
print("  Adiabatic variant: delta_0 * (1 + D/3). s_cmb_shell = delta_shell (CMB-driven part only).")
print("  D        delta_shell   s_cmb    dR/R from CMB part   visible in proton?")
for D in (0, 1, 10, 100, 1000, 3200, 10000):
    d_lin = DELTA0 * (1 + D)
    d_adi = DELTA0 * (1 + D / 3.0)
    dR_lin = math.exp(d_lin ** 2) - 1
    print(f"  {D:>6}   {d_lin:.3e}    {d_lin:.3e}   {100 * dR_lin:.3e}%          {'NO' if dR_lin < 0.001 else 'YES (0.1%)'}")
print("  threshold for a 0.1% proton-radius shift at the circumference: s_cmb = 0.032 ->")
print("  delta ~ 3.2e-2 -> D ~ 3200 (linear) / ~9600 (adiabatic). Standard anisotropy is 1e-5.")
print("  -> the circumferential signature lives in the BATH (delta_T/T contrast ~ 1+D), NOT in the chain.")
print("     A proton at the circumference measures the same lit-region 0.8395 fm as one in the interior,")
print("     unless the cooling front amplifies the CMB fluctuation by ~3000x. The contrast delta_shell/delta_0")
print("     = 1+D is the number to look for in the sky, and D is an input the model does not supply.")
print("  note: the shell is lit (newest formations ARE the new light), so s_new = 0.10 there regardless;")
print("  the CMB part adds in quadrature: s_total^2 = 0.10^2 + delta^2 -- invisible until delta ~ 0.03.")

# ---- Block 6: old light vs new light -- different types? ----
print("\nBLOCK 6 -- OLD vs NEW LIGHT: different types, does the chain care?")
lam_old_z10_um = 2898.0 / (T0 * 11.0)
lam_old_today_um = 2898.0 / T0
a_old_z10 = lam_old_z10_um * 1e9    # fm
a_new = LAM_NEW_UM * 1e9            # fm
E0 = a0 ** 2 * math.exp(2 * S_MAX ** 2)   # <a^2> for spread s=0.10
c_old = 0.002 * E0 / (a_old_z10 ** 2 - E0)
c_new = 0.002 * E0 / (a_new ** 2 - E0)
u_old_z10 = u_cmb_today * 11.0 ** 4
print(f"  lambda_old at z=10 = {lam_old_z10_um:.1f} um ({a_old_z10:.2e} fm); lambda_old today = {lam_old_today_um:.0f} um")
print(f"  lambda_new (optical) = {LAM_NEW_UM} um ({a_new:.2e} fm); ratio lambda_old/lambda_new at z=10 = {lam_old_z10_um / LAM_NEW_UM:.0f}")
print(f"  both are >= {min(a_old_z10, a_new) / a0:.1e}x the link scale a0 = 0.24 fm -- far field for the chain.")
print(f"  max direct-component weight keeping dR < +0.1%: old light c_max = {c_old:.2e}, new light c_max = {c_new:.2e}")
print(f"  physical weights by energy density: old (z=10) = {u_old_z10 / u_p:.2e}, new (1 AU) = {u_star_1AU / u_p:.2e}")
print(f"  -> both physical weights sit ~20 orders below their c_max. The chain cannot see the TYPE.")
print("     It sees only the joint medium: energy density (which light dominates locally) plus the")
print("     regulated breathing mode the new light switches on. If the model has a type-dependent")
print("     coupling (the medium answering different waveforms differently), that coupling is a NEW")
print("     input -- this toy has none, and nothing in tests 1-4 supplies one.")

# ---- Block 7: what the bubble does NOT determine ----
print("\nBLOCK 7 -- WHAT THE BUBBLE DOES NOT DETERMINE (needs Dakota or a new rule)")
print("  (a) The gating threshold: the toy switches breathing ON wherever u_new > u_old. The true")
print("      threshold (what new-light level flips the medium's mode) is undetermined.")
print("  (b) The cooling-front density contrast D: sets the circumferential CMB signature (1+D).")
print("      No value is supplied by the model; D ~ 3200 would be needed for the proton to feel it.")
print("  (c) The lit fraction f_lit at t=1: scanned 0.1-0.5; the true clustered value at the")
print("      proto-galaxy epoch is undetermined (bath still dominates the volume at z=10, so the")
print("      breathing is on only in compact star-forming cores, not across the bubble).")
print("  (d) Whether the medium's regulated mode is really self-capping: assumed from test 2.")
print("      Block 4 shows it MUST be, or the early (hot-bath) bubble overshoots the radius.")
print("  (e) Old-vs-new type coupling: none in the toy. If different waveforms couple differently")
print("      to the medium, that is a new input, not derivable from the fit numbers.")
print("  (f) The above/below-plane refractive light (how the galaxy's inside is perceived): the toy")
print("      treats it as weak new light (halo, u ~ ISRF or less) -- enough to keep the mode on")
print("      inside a galaxy, off in intergalactic voids. Its exact energy density is undetermined.")

print("\nBOTTOM LINE -- TEST 5")
print(f"  LIT region (new light present):  R = {R_lit:.4f} fm, hardening = {100 * H_lit:+.2f}% -- FIT CLOSES, breathing present,")
print("    driven by the LOCAL new-light source, not the CMB. Breathing is the medium's regulated")
print("    mode, switched on by new light; the CMB bath is the road it travels on.")
print(f"  VOID pocket (no local emission): R = {R_void:.4f} fm, hardening = {100 * H_void:+.2f}% -- bare proton, no breathing.")
print("    PREDICTION: the measured 0.840 fm is a LOCAL-medium value. A proton in a void pocket")
print("    measures 0.831 fm in this toy.")
print("  CMB-as-medium: null stands (test 4). The bath cannot drive breathing (uniform to 1e-5) and")
print("    cannot set the coupling unless the medium is unregulated -- in which case the early hot")
print("    bubble overshoots the radius. Regulation is required, not optional.")
print("  CIRCUMFERENCE: newest formations at the apparent edge = the new cooling area. The measurable")
print("    signature is a CMB fluctuation contrast (1+D) in the bath at the shell -- NOT a proton-radius")
print("    difference. The proton at the circumference reads the same 0.8395 fm as in the interior.")
print("  OLD vs NEW type: invisible to the chain in this toy. The chain sees the joint medium only.")
print("  Breathing-vs-aura discriminator UNCHANGED: look along the chain (lit: ~3-link breaths,")
print("    local 5-link R std ~7.9%; aura: uniform links).")
