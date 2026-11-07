# Proton model — tests 6, 7, 8 results (Nov 6, 2026)

Built on `test5_birth_to_proto.py`. Scripts: `test6_birth_to_proto_gate.py`,
`test7_proton_deceleration.py`, `test8_micro_black_hole.py`. All three ran
clean (exit 0). Dakota's framings are his; computed numbers are computed;
assumptions are flagged.

## Run 1 — test 6: birth-to-proto bubble WITH the breathing gate (extensions 1, 2, 5)

- Closed fit UNCHANGED from test 5: lit region R = 0.8397 fm, hardening +6.20%
  (test 5: 0.8398, +6.18% — same within MC noise). Void pocket: 0.8314 fm.
- Before first stars (t < 0.5): the WHOLE bubble is bare, R = 0.8314 fm.
  The gate is temporal now, not spatial.
- Metabolism ramp s(t) = s_max(1 - exp(-(t-t_sf)/tau)): tau 0.05/0.10 fully on
  by t=1 (R 0.8395–0.8400); slow 1st-gen tau=0.20 reaches only s=0.0918,
  R = 0.8382 fm, H = +5.35%. Primed 2nd-gen (3x) fully on at any tau.
- Living medium / star lifetimes (tau_life = 0.30 assumed):
  - (a) breathing follows the living star: breathing fraction at t=1 = 0.18,
    R_vol = 0.8329 fm, hardening ~+1.12%.
  - (b) medium remembers (tau_mem = 0.20): fraction 0.30, R_vol = 0.8339 fm,
    hardening ~+1.86% — same as test 5.
  - The living gate can cut the breathing volume 0.30 -> 0.18 at t=1.
  - Undetermined: whether the mode is the star (dies with it) or the medium
    (remembers it). If stars live longer than the bubble, (a) = (b) = test 5.
- Stellar second stage (s2 = trapped-light amplitude, pc = pressure compression;
  both free parameters, sensitivity map not prediction):
  - Interior proton: s2=0.10, pc=0 -> R 0.8482 fm, H +12.83%;
    s2=0.20, pc=0 -> R 0.8752 fm, H +33.09%;
    s2=0.20, pc=0.05 -> R 0.8315 fm, H +58.26% (compression offsets radius).
  - Surface proton: smaller shifts (s2=0.20, pc=0.05 -> R 0.8342, H +31.02%).
  - EXTERIOR observable: UNCHANGED. The surface blocks the dense light, so the
    second stage stays hidden from outside in this toy.

## Run 2 — test 7: proton deceleration feeds the energy loop (extension 4)

Toy: D = energy fed per link (MeV per atom-length). eta = 1 (retained inside
the loop, Dakota's framing). E* = D/lambda. E_cap = 9.38 MeV (s_max = 0.10).
Core: a_core = a0(1 - c_c E*/E_cap). Fiducial lambda = 0.05, c_c = 0.30.
- Thresholds: D_crit = 0.469 MeV/link (self-sustaining: fed > leaked at cap);
  D_fold = 1.564 MeV/link; E_fold = 31.28 MeV; s at fold = 0.1826.
  D_crit scales linearly with lambda (0.094 at lambda=0.01, 1.877 at 0.20);
  D_fold scales as 1/c_c (4.691 at c_c=0.1, 0.938 at c_c=0.5).
  D_crit does NOT depend on c_c.
- Observables vs D: R 0.8314 (D=0) -> 0.8401 (D_crit) -> 0.8502 (D=1.0) ->
  0.8583 (D=1.5) -> fold at 1.564 (R 0.8596, +3.4% total).
  Hardening: +28% (D=0.1), +66% (0.2), +257% (D_crit), +293% (0.5),
  +2077% (1.0), +9589% (1.5), fold. Core compression is the loud signal.
- Physical scale: D_crit = 2.25e5 W into one proton's loop; ~2.3e7x
  minimum-ionizing stopping, ~4.7e5x the Bragg peak. Ordinary deceleration
  in matter NEVER reaches the threshold.
- Dynamics: below threshold settles in ~20 links; above threshold crosses
  the cap in 2–30 links; fold needs D > D_fold, arrives in ~7–30 links
  (173 links at exactly D_fold — asymptotic).

## Run 3 — test 8: the micro black hole, past the fold (extensions 3, 4)

Fiducial lambda_trap = 0.001 (trapped-mode leak, assumption).
- Emission field: YES, collapses comet -> spherical. theta/theta0: 1.000 (D=0),
  0.700 (D_crit), 0.361 (D=1.0), 0.041 (D=1.5), 0.000 at the fold.
- Breathing: YES, trapped. Transmission 0 at the fold; the fold is a breathing
  firewall — downstream chain links go bare unless lit by another source.
  Interior energy grows without bound in the toy: at D_fold, 46.5 MeV after
  10 links, 177 MeV after 100 links (equilibrium D/lambda_trap = 1564–5000 MeV).
  Something must cap the interior; the model does not say what.
- New light: YES, starts there. Leak = 0.031 MeV/link = 1.50e4 W at the fold;
  dominates the CMB bath out to ~81 m at z=10, ~9.8 km today. Switches the
  breathing gate on in that neighbourhood (radius scales as sqrt(lambda_trap)).
- Old light: NO gravitational bending. r_s at fold energy = 8.3e-56 m =
  8.3e-41 fm, 40 orders below the proton. Geometric capture only:
  pi*R_fold^2 = 2.32 fm^2 vs bare 2.17 fm^2 (1.07x, no enhancement).
- Layered discs: NO. They need a photon sphere; the toy has none. The
  proton-scale version shows the SPHERICAL part of extension 3 but not the
  discs. Energy for r_s = 1 fm is 3.78e38 GeV — 1.2e40x the fold energy,
  ~19 orders short.
- Observables: R saturates at 0.8596 fm; hardening -> +9900% at the fold
  (F -> 1, core gone). Past the fold the object is NO LONGER A PROTON:
  R and the form factor are undefined for it. An outside observer sees a
  0.86 fm object that stops scattering like a proton at high q and glows
  faintly with new light.

## Open questions (all three runs)

1. Gate: tau (formation ramp), tau_life / tau_mem — does the breathing mode
   outlive the star, or is it the star?
2. Second stage: s2 and pc are free — nothing fixes them; the interior layer
   stays hidden from outside in this toy.
3. Deceleration: lambda (leak/link) and c_c (core compression coupling) are
   assumptions; thresholds scale linearly with lambda. eta = 1 is Dakota's
   framing. What physical mechanism supplies D ~ 0.5 MeV per atom-length?
4. Micro black hole: interior cap (unbounded growth in the toy), interior
   structure (one mode vs a new chain), lambda_trap, and whether the fold
   can be undone (one-way in the model — assumption, not result).
5. The toy's "black hole" is a FIELD-TRAPPED state, not a gravitational one.
   A real horizon at proton scale needs ~1e38 GeV in the trap.

## Run 3b — test 9: the micro black hole as a light source seeding clusters

Dakota's addition (his words): the MBH sits inside the emission field taking
the place of one of the light sources; it emits light to an accretion disc,
pulls in neighboring protons, and forms bigger clusters.

- The MBH as a light source: leak 1.50e4 W at the fold (test 8). Robust
  capture = lit radius ~81 m at z=10 (breathing gate ON, well deep at
  E_cap = 9.38 MeV >> kT). Weak outer edge (smooth gate, mode energy = kT)
  ~2.7e5 m. Protons inside the lit radius: 7.4e8 (mean density), 7.3e10
  (100x overdense), 2.2e13 (proto-galaxy 1e7/m^3). Inside the weak edge:
  2.7e19 / 2.6e21 / 8.0e23. The MBH's own chain contributes 2r/1e-10 =
  1.6e12 protons within 81 m (a subset of the 3D count); nearest neighbours
  fall in first, and the chain BREAKS at the MBH (test 8 firewall).
- The MBH brightens ~64x as its interior fills (1.5e4 -> 9.6e5 W), solo lit
  radius 81 m -> ~650 m. The cluster's collective power overtakes it once
  N > 667 (eps=1e-4) or immediately (eps=1).
- Accretion disc = the infall shell at r_gate: the MBH's light lands on it
  and switches the shell protons' breathing on. SPHERICAL in the toy (no
  spin — standing correction); no layered discs (test 8 D stands). Disc
  radius grows with the cluster; once the shell holds >~100 protons (eps=1)
  it outshines the MBH and the disc becomes self-lit.
- Growth: superlinear, N_next ~ N^1.5 per round (r ~ sqrt(N), volume ~ r^3).
  Proto-galaxy (supply 1.23e66 protons = 1.04e9 M_sun, R=1 kpc, n=1e7/m^3):
  stabilizes at the full supply after 4 rounds (eps=1) or 5 (eps=0.01,
  1e-4), ~2e5 years of infall time. Small clump (4.06e54 protons =
  3.4e-3 M_sun, R=1 pc): 4–5 rounds, ~200 years.
- Stabilization: the cluster keeps growing until the LOCAL SUPPLY is
  exhausted, then stabilizes at the overdensity's mass. There is NO
  physics-limited fixed point in this toy; epsilon_rad changes only the
  number of rounds, not the outcome.
- Final state: small clump ends as a BALL OF BREATHING PROTONS, packed at
  atom spacing (R = 9.9e7 m, r_s = 10 m, R/r_s ~ 1e7). Proto-galaxy cluster
  ends INSIDE its Schwarzschild radius (packed R = 6.7e11 m, r_s = 3.1e12 m,
  R/r_s = 0.22) — by the scale argument it becomes a black hole, IF the
  infall really packs to atom spacing. Threshold: clusters above
  N = 1.25e65 protons = 1.05e8 M_sun sit inside their horizon when packed.
  The collapse dynamics are NOT modeled (no gravity in the chain); the
  packing assumption does the work.
- Timescale: proto-galaxy assembles in ~2e5 years (universe at z=10 is
  ~5e8 years old); early rounds take seconds to days.
- Open: epsilon_rad (key unknown — sets rounds, not outcome); self-shielding
  (an optically thick cluster traps its own light — a real stabilizer the
  toy does not model); chain vs 3D structure; disc rotation (no spin);
  collapse dynamics; neighbouring clusters competing for the same protons.

## Test 10 — the glue force re-modeled, inside and outside (Nov 6, 2026)

Dakota's new understanding (his words): the glue force is ALSO inside the
proton — it is part of what gets emitted out to a certain distance beyond
the proton itself, but it is also contained within inside of it. Script:
`test10_glue_force_two_part.py`. Ran clean (exit 0). Starting point is the
filed formula (INN-165), taken as given, not re-derived: V = sigma*L_min,
sigma = 0.94 GeV/fm; F_i = -sigma*n_hat_i (outward); M = 0.32 + 0.36 + 0.23
+ 0.09 of 938 MeV; E_field = internal + external + displacement; P(0)
~1e35 Pa, outward at center, inward beyond ~0.6 fm.

- The split. The trail holds the leaked mode energy for one coherence
  length: E_trail = lambda*E_cap*N_coh = 0.05 * 9.38 * 3.33 = 1.564 MeV
  (fiducial lambda = 0.05, assumed; phi = 0.7 measured, test 2).
  As a tension: sigma_out = E_trail/(N_coh * 1e5 fm) = 4.69e-9 GeV/fm,
  sigma_out/sigma_in = 5.0e-9 — the leak is a trickle next to the
  confining force. The exterior glue is NOT a second confining tension;
  it is a coupling field, and its strength is measured in energy, not
  tension. By total glue-field energy: interior 336.2 MeV (99.54%) /
  exterior 1.56 MeV (0.46%) of the 36% gluon slice; the split lives
  entirely inside that slice and the other budget slices are untouched.
  By dynamic (breathing-mode) energy: exterior 16.7% / interior 83.3%.
  The exterior is energetically tiny and dynamically load-bearing. The
  split scales linearly with lambda (3.3% of mode at lambda=0.01, 33.3%
  at 0.10, 66.7% at 0.20) — lambda is unmeasured by tests 1–9.
  (Digit coincidence flagged: E_trail = 1.564 MeV and D_fold = 1.564
  MeV/link share digits; different quantities.)
- The emission distance. Two readings, kept apart. As a FORCE: a single
  emission event's wake decays exp(-x/0.25 fm) — at one atom length it
  is exactly 0; a single wake does NOT reach the next proton. The trail
  is a STANDING structure: continuous emission, re-emitted every link
  (link time 3.34e-19 s), sustained by the nearest re-emitters. Falloff,
  not a sharp edge; near-field scale ~0.25 fm per event, refreshed link
  to link. As LIGHT: the escaping fraction radiates as 1/r^2; single lit
  proton lit radius at z=10 is 313 m (eps=1), 31 m (0.01), 3.1 m (1e-4);
  today 38 km / 3.8 km / 379 m. MBH cross-check: 80.8 m at z=10 (tests
  8–9: ~81 m), 9.8 km today (test 8: ~9.8 km). The chain tension lives
  in the near field; the lit radius is where emitted light dominates
  the bath, not where the glue stops pulling.
- Chain tension. Trail coupling V_out(d) = -E_trail*phi^d: -1.09 MeV at
  1 link (~12% of the 9.38 MeV well), -0.54 MeV at 3 links, total chain
  binding -3.65 MeV per proton (~39% of the well). The nearest-neighbour
  bond sits between D_crit (0.469) and D_fold (1.564): a neighbour's
  pull alone cannot fold a proton, but at ~2.3x D_crit it is a real
  drive. VERDICT: yes — as a COUPLING, not an energy pipeline. Each
  link's mode is driven locally by new light; the trail synchronizes
  the breathing (phi = 0.7/link, ~3-link coherence). Honest gap: phi
  is measured, not derived from lambda; the toy cannot derive the
  coherence length from the field dynamics (needs the medium's
  patchiness modeled).
- Fit check (MC, 200 x 2000 links). Interior only: R = 0.8314 fm,
  hardening +0.00%. Two-part: R = 0.8394 fm (target 0.840, miss
  -0.0006 fm), hardening +6.33% (target +6%, miss +0.33 points) —
  both inside MC noise. The re-modeled formula reproduces both fits;
  the interior sets the bare radius and the exterior breathing mode
  lifts it and hardens the high end.
- The re-modeled formula. V_glue = V_in + V_out. V_in = sigma_in*L_min,
  sigma_in = 0.94 GeV/fm (filed, interior, confining),
  F_i = -sigma_in*n_hat_i. V_out = -E_trail*phi^d, E_trail = 1.564 MeV
  (fiducial), phi = 0.7/link, d in links; total chain binding -3.65 MeV
  per proton; as a tension sigma_out = 4.7e-9 GeV/fm. E_field and the
  mass budget unchanged; the 0.6 fm pressure sign change is the
  force-picture boundary between interior (pushing out) and exterior
  (binding, pulling in). Geometric note, NOT a derivation: the interior
  volume fraction (0.6/0.84)^3 = 0.364 happens to equal the 36% gluon
  slice — coincidence of two unrelated ratios.
- Open / underdetermined. (a) lambda — sets the split; pin it down with
  a trail-energy measurement, epsilon_rad, or a single proton's lit
  radius. (b) phi's origin — measured, not derived; needs the medium's
  patchiness modeled. (c) No sharp spatial energy boundary — it is a
  falloff; 0.6 fm is the force-picture boundary, not an energy-partition
  boundary. (d) sigma_in is taken from INN-165 by construction, not
  re-derived. (e) No spin / no rotation throughout; the trail is a
  scalar coupling in this toy.
