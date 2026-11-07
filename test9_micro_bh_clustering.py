"""Test 9: the micro black hole as a light source that seeds clusters.

Dakota's addition (his words, held exactly): the micro black hole sits
inside the emission field taking the place of one of the light sources.
Because the micro black hole actually emits light to an accretion disc, it
should also pull in neighboring protons next to it, so it should also be a
region that then forms bigger clusters.

This run folds that in: the MBH is a light source WITHIN the emission field
(it replaces one link in the chain), it emits to its accretion disc (the
infalling shell of protons its light lands on), it pulls in neighbouring
protons, and it seeds larger cluster formation.

Inputs from tests 5-8 (fiducial):
- MBH trapped leak at the fold: 0.031 MeV/link = 1.50e4 W (test 8 B2).
- MBH lit radius (breathing gate ON, u_new > u_old): 81 m at z=10 (test 8).
- Mode energy at the regulated cap: E_cap = 9.38 MeV (tests 2/5/7).
- A single lit proton's open-loop leak: lambda * E_cap per link
  = 0.469 MeV/link = 2.25e5 W -- but most of that is RECYCLED into the
  chain (the emission field is local), not radiated to infinity. The
  fraction that escapes as free light is epsilon_rad, UNKNOWN: scanned
  (1, 0.01, 1e-4). The MBH's trapped leak is treated as escaping (it is
  new emission by construction, test 8 B2).
- Epoch: proto-galaxy, z=10 (test 5 t=1). u_old = u_CMB_today * 11^4.
  Gas temperature for thermal motion: T_gas = 1e4 K (ASSUMPTION, proto-galaxy
  gas; the CMB at z=10 is 30 K). kT/E_cap sets the smooth-gate capture edge.
- Chain spacing: one atom length = 1e-10 m (base model).
- Standing corrections kept: NO spin / NO external rotation -- so the
  "disc" in this toy is a spherical infall shell, not a rotating disc.
"""
import math

# ---- constants ----
C = 2.99792458e8
G = 6.67430e-11
M_P_KG = 1.67262192e-27
M_P_MEV = 938.27
M_SUN_KG = 1.98847e30
MEV_J = 1.602176634e-13
K_B = 1.380649e-23
E_CAP = M_P_MEV * 0.10 ** 2          # 9.38 MeV
LAM = 0.05                            # open-loop leak fraction per link
LAM_TRAP = 0.001                      # trapped-mode leak per link
L_LINK_M = 1e-10                      # one atom length
LINK_TIME_S = L_LINK_M / C            # 3.34e-19 s
U_CMB_TODAY = 0.26 * 1.602176634e-19 / 1e-6   # J/m^3
U_OLD_Z10 = U_CMB_TODAY * 11.0 ** 4   # J/m^3 at z=10
T_GAS = 1e4                           # K, proto-galaxy gas (ASSUMPTION)
KT_OVER_ECAP = K_B * T_GAS / (E_CAP * MEV_J)
P_MBH_FOLD = LAM_TRAP * 31.28 * MEV_J / LINK_TIME_S   # 1.50e4 W
P_PROTON_LEAK = LAM * E_CAP * MEV_J / LINK_TIME_S     # 2.25e5 W
V_TH = math.sqrt(K_B * T_GAS / M_P_KG)                # thermal speed
V_TYP = 1e7                           # typical infall speed, m/s (ASSUMPTION:
                                      # fraction of max sqrt(2*E_cap/m_p) = 4.2e7)


def r_gate(P):
    """Radius where a source of power P dominates the bath (u_new = u_old)."""
    return math.sqrt(P / (4 * math.pi * C * U_OLD_Z10))


def r_capture_smooth(P):
    """Radius where the smooth-gate mode energy falls to kT (weak outer edge)."""
    return math.sqrt(P / (4 * math.pi * C * KT_OVER_ECAP * U_OLD_Z10))


def n_3d(r, n_p):
    return 4.0 / 3.0 * math.pi * r ** 3 * n_p


def n_chain(r):
    """Protons of the MBH's own chain within radius r (chain passes through it)."""
    return 2 * r / L_LINK_M


def packed_radius(N):
    """Radius if N protons pack at one atom length (1e-30 m^3 each)."""
    return (3 * N * 1e-30 / (4 * math.pi)) ** (1.0 / 3.0)


def r_schwarzschild(N):
    return 2 * G * N * M_P_KG / C ** 2


print("BLOCK 0 -- INPUTS (from tests 5-8)")
print(f"  MBH leak power at the fold: {P_MBH_FOLD:.2e} W")
print(f"  single lit proton open-loop leak: {P_PROTON_LEAK:.2e} W (mostly recycled;")
print(f"    escaping fraction epsilon_rad scanned: 1, 0.01, 1e-4)")
print(f"  u_old at z=10 = {U_OLD_Z10:.2e} J/m^3; kT/E_cap = {KT_OVER_ECAP:.2e}")
print(f"  thermal speed at T_gas = {T_GAS:.0e} K: v_th = {V_TH:.2e} m/s")
print(f"  max infall speed sqrt(2*E_cap/m_p) = {math.sqrt(2 * E_CAP * MEV_J / M_P_KG):.2e} m/s")
print(f"  ambient proton density: cosmic mean at z=10 = {0.25 * 11.0**3:.0f} /m^3")

# ---- Block 1: the MBH as a light source in the field ----
print("\nBLOCK 1 -- THE MBH AS A LIGHT SOURCE IN THE FIELD")
print("  lit radius (gate ON, u_new > u_old) and smooth capture radius (mode")
print("  energy = kT), and the protons inside each, at three densities.")
print("  density [/m^3]   r_gate [m]   N in r_gate   N_chain in r_gate   r_capture [m]   N in r_capture")
for label, n_p in (("mean z=10 (330)", 0.25 * 11.0 ** 3),
                   ("100x overdense (3.3e4)", 3.3e4),
                   ("proto-galaxy (1e7)", 1e7)):
    rg = r_gate(P_MBH_FOLD)
    rc = r_capture_smooth(P_MBH_FOLD)
    print(f"  {label:22s} {rg:10.1f}  {n_3d(rg, n_p):12.2e}  {n_chain(rg):12.2e}  "
          f"{rc:12.2e}  {n_3d(rc, n_p):12.2e}")
print("  the ROBUST capture is the lit radius (~81 m): inside it the breathing")
print("  is switched ON and the mode well is deep (E_cap = 9.38 MeV >> kT).")
print("  the smooth capture radius (~270 km) is the weak outer edge: out there")
print("  the pull is only ~kT deep and thermal motion competes -- an upper bound,")
print("  not a firm capture. The MBH's own chain contributes 2r/1e-10 protons")
print("  (a subset of the 3D count, not additional): its nearest neighbours are")
print("  an atom-length away and fall in first. The chain BREAKS at the MBH")
print("  (test 8 firewall): downstream links go bare unless lit by another source.")
print("  the MBH also BRIGHTENS as its interior fills (test 8 B):")
for n_links, E_int in ((0, 31.28), (100, 218.7), (1000, 1564.0), (10000, 1996.0)):
    P = LAM_TRAP * E_int * MEV_J / LINK_TIME_S
    print(f"    after {n_links:6d} links (D=2 MeV/link): E_int = {E_int:7.1f} MeV, "
          f"P_MBH = {P:.2e} W, solo lit radius = {r_gate(P):7.1f} m")
print("  the MBH alone brightens ~64x as its interior fills (1.5e4 -> 9.6e5 W),")
print("  extending its solo lit radius 81 m -> ~650 m. The cluster's collective")
print("  power overtakes it once N > P_MBH/(eps*P_proton): immediately for")
print("  eps=1, at N > 667 for eps=1e-4.")

# ---- Block 2: the accretion disc ----
print("\nBLOCK 2 -- THE ACCRETION DISC (the infall shell)")
print("  the MBH's light lands on the shell of infalling protons at r_gate.")
print("  that shell IS the disc in this toy: the MBH emits to it, and its light")
print("  switches the shell protons' breathing ON (the gate). Disc radius = r_gate,")
print("  so it grows with the cluster. The disc is SPHERICAL in the toy -- the")
print("  model has no spin / no rotation (standing correction), so there is no")
print("  rotating disc plane; the infall comes from all directions. No layered")
print("  discs (test 8 D verdict stands: no photon sphere, no lensed images).")
print(f"  at the fold: disc radius = {r_gate(P_MBH_FOLD):.1f} m, intercepted power =")
print(f"  P_MBH = {P_MBH_FOLD:.2e} W (the shell absorbs the MBH's light and its")
print("  protons light up). The disc's own re-emission = N_shell * eps * P_proton;")
print("  once the shell holds more than ~100 protons (eps=1) it outshines the MBH")
print("  and the disc becomes self-lit -- the cluster lights itself.")

# ---- Block 3: cluster growth iteration ----
print("\nBLOCK 3 -- CLUSTER GROWTH: DOES IT KEEP GROWING?")
print("  iteration: P(N) = P_MBH + N*eps*P_proton; r_gate from P(N);")
print("  N_next = protons inside r_gate (capped at the overdensity supply).")
print("  N_next ~ N^1.5 per round (r ~ sqrt(N), volume ~ r^3) -- superlinear.")


def grow(supply, n_p, eps, label, R_od):
    N = 1.0
    print(f"  --- {label} (supply {supply:.2e} protons, eps={eps:g}) ---")
    print("  round   N              P [W]        r_gate [m]    N_next")
    t_total = 0.0
    for k in range(12):
        # (N-1): the MBH itself is not a lit proton; it does not also radiate
        # the open-loop leak. Only the N-1 captured protons do.
        P = P_MBH_FOLD + max(0.0, N - 1) * eps * P_PROTON_LEAK
        rg = r_gate(P)
        N_next = min(supply, n_3d(rg, n_p))
        # infall time counts only the reach inside the overdensity: the
        # lit radius past R_od pulls nothing more in.
        t_total += min(rg, R_od) / V_TYP
        print(f"  {k:3d}    {N:12.3e}  {P:10.2e}  {rg:12.2e}  {N_next:12.3e}")
        if N_next <= N * 1.001:
            print(f"  STABILIZED at N = {N_next:.3e} after {k + 1} rounds, "
                  f"~{t_total:.2e} s ({t_total / 3.154e7:.2e} years) of infall time.")
            return N_next, t_total
        N = N_next
    print(f"  still growing after 12 rounds at N = {N:.3e} (supply not reached).")
    return N, t_total


SUPPLY_PG = 4.0 / 3.0 * math.pi * (3.086e19) ** 3 * 1e7      # 1 kpc, 1e7/m^3
SUPPLY_PC = 4.0 / 3.0 * math.pi * (3.086e16) ** 3 * 3.3e4    # 1 pc, 3.3e4/m^3
print(f"  fiducial proto-galaxy supply: {SUPPLY_PG:.2e} protons "
      f"= {SUPPLY_PG * M_P_KG / M_SUN_KG:.2e} M_sun (R=1 kpc, n=1e7/m^3)")
print(f"  small clump supply: {SUPPLY_PC:.2e} protons "
      f"= {SUPPLY_PC * M_P_KG / M_SUN_KG:.2e} M_sun (R=1 pc, n=3.3e4/m^3)")
for eps in (1.0, 0.01, 1e-4):
    grow(SUPPLY_PG, 1e7, eps, "proto-galaxy", 3.086e19)
for eps in (1.0, 1e-4):
    grow(SUPPLY_PC, 3.3e4, eps, "small clump", 3.086e16)
print("  -> the cluster keeps growing until the local supply is exhausted.")
print("     epsilon_rad changes only the number of rounds (3-4 for the")
print("     proto-galaxy), not the outcome: N_next ~ N^1.5 always outruns N.")
print("     There is NO physics-limited fixed point in this toy.")

# ---- Block 4: the final cluster -- what does it look like? ----
print("\nBLOCK 4 -- THE FINAL CLUSTER")
print("  supply            N_final         mass [M_sun]   packed R [m]   r_s [m]   R/r_s")
for label, supply in (("proto-galaxy", SUPPLY_PG), ("small clump", SUPPLY_PC)):
    Rpack = packed_radius(supply)
    rs = r_schwarzschild(supply)
    print(f"  {label:14s} {supply:12.2e}  {supply * M_P_KG / M_SUN_KG:10.2e}  "
          f"{Rpack:11.2e}  {rs:9.2e}  {Rpack / rs:8.2e}")
N_BH = (6.2e-11 / 2.48e-54) ** 1.5
print(f"  threshold: a cluster packed at atom spacing sits inside its own")
print(f"  Schwarzschild radius above N = {N_BH:.2e} protons "
      f"= {N_BH * M_P_KG / M_SUN_KG:.2e} M_sun.")
print("  -> the small clump (3.4e-3 M_sun) ends as a BALL OF BREATHING PROTONS,")
print("     packed at atom spacing, lit from within, far from its horizon.")
print("     the proto-galaxy cluster (1e9 M_sun) ends INSIDE its Schwarzschild")
print("     radius (R/r_s ~ 0.3) -- by the scale argument it becomes a black")
print("     hole. BUT the toy cannot model the collapse itself: it has no")
print("     gravity in the chain, so whether the infall really packs that")
print("     tightly is undetermined. The packing assumption does the work.")
print("     (A Newtonian check misleads here: the central pressure needed is")
print("     ~1e21 Pa, far below the proton's own ~1e35 Pa -- but that estimate")
print("     breaks down at the horizon, where the required pressure diverges.)")

# ---- Block 5: timescales ----
print("\nBLOCK 5 -- TIMESCALES")
print("  infall time per round ~ r_gate / v_typ (v_typ = 1e7 m/s, a fraction of")
print("  the max 4.2e7 m/s a proton gains falling through the E_cap well).")
print("  the total is dominated by the LAST round (the largest radius):")
for label, r_last in (("proto-galaxy (last round r ~ 1 kpc)", 3.086e19),
                      ("small clump (last round r ~ 1 pc)", 3.086e16)):
    print(f"  {label}: ~{r_last / V_TYP:.2e} s = {r_last / V_TYP / 3.154e7:.2e} years")
print("  so the proto-galaxy cluster assembles in ~1e5 years -- fast on cosmic")
print("  scales (the universe at z=10 is ~5e8 years old). The early rounds")
print("  (81 m, 1e9 m) take seconds to days. The MBH's interior fills on link")
print("  timescales (100 links = 3e-17 s of chain time) -- effectively instant.")

# ---- Block 6: what the model cannot answer ----
print("\nBLOCK 6 -- WHAT THE MODEL CANNOT ANSWER")
print("  (a) epsilon_rad -- the escaping fraction of a proton's leak -- is the")
print("      key unknown. It sets the rounds-to-supply (3-4) but not the outcome.")
print("  (b) SELF-SHIELDING: once the cluster is optically thick, its own light")
print("      is trapped inside it and the pull on OUTSIDE protons saturates -- a")
print("      real stabilizer the toy does not model. The toy's runaway assumes")
print("      every proton's light escapes to pull in the next shell.")
print("  (c) Chain vs 3D structure: the toy counts protons by 3D density; the")
print("      chain structure (1D, atom spacing) is folded in only as the subset")
print("      2r/1e-10. A real chain geometry could change the early rounds.")
print("  (d) Disc rotation: the model has no spin (standing correction), so the")
print("      disc is a spherical shell. A rotating disc would change the infall")
print("      geometry and the light distribution.")
print("  (e) Collapse dynamics: the toy has no gravity in the chain, so the")
print("      black-hole endpoint for big clusters is a scale argument (R vs r_s),")
print("      not a simulated collapse. Whether the infall packs to atom spacing")
print("      is undetermined.")
print("  (f) Neighbouring clusters: the toy grows ONE cluster in isolation. In a")
print("      real bubble, neighbouring MBHs compete for the same protons, and")
print("      their lit regions overlap -- the supply splits between them.")

print("\nBOTTOM LINE -- TEST 9")
print("  The MBH, sitting in the emission field in place of one light source,")
print("  pulls in its neighbours and seeds a cluster that keeps growing until")
print("  the local supply is exhausted -- then it stabilizes at the overdensity's")
print("  mass. Robust capture is the lit radius (~81 m at the fold, growing as")
print("  the cluster brightens); the weak outer edge is ~270 km. The cluster")
print("  grows superlinearly (N_next ~ N^1.5 per round) and eats a proto-galaxy")
print("  in 3-4 rounds, ~1e5 years. Small clumps end as balls of breathing")
print("  protons; proto-galaxy-mass clusters sit inside their Schwarzschild")
print("  radius by the scale argument -- the seed grows into a black hole, if")
print("  the infall really packs to atom spacing. The accretion disc is the")
print("  infall shell at r_gate, spherical in this toy (no spin), and it grows")
print("  with the cluster.")
