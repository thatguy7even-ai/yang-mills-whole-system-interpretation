# Yang-Mills Whole System Interpretation

This repository holds the proton model code — tests 5 through 10 — and this
README is the explanation layer the code alone cannot carry. The code runs
the numbers. This file says what the numbers are *of*: the Yang-Mills
interpretation of the **entire system**, not the interpretation of one proton.

## What this is, and what it is not

**Claim, stated plainly:** this is a working interpretation — a model built
by Dakota Higgins in dialogue with AI, tested in small toy scripts against a
handful of calibration targets (the proton charge radius and the high-end
form-factor hardening). It is **not** a verified result of mainstream physics
and it is **not** a proof of anything about Yang-Mills theory.

**The bridge is open.** The top missing piece of the whole interpretation is
the bridge: motion / medium / dilation giving the gap value. Until the bridge
is closed, the gap value is a computed number inside the model, not a
derivation. Everything in this README is marked, where it matters, as
*framing* (Dakota's understanding, held in his words), *computed* (a number
a script produced), or *assumption* (a free parameter put in by hand).

**Scope:** the model covers a regional bubble — from the first spark to the
point where proto-galaxies start to form. It does **not** model the whole
current expansive medium. The 3D picture is a grid centred on "true 0" with
four pillars of 0 longitude/latitude.

## The model (filed starting point, INN-165 — taken as given, not re-derived)

- **Potential:** V = σ · L_min, σ = 0.94 GeV/fm. The Y-ansatz: the junction
  sits at the Fermat point, each leg carries the same σ, one leg's pull
  equals the other two combined, opposite. F_i = −σ · n̂_i, with n̂_i from
  the junction outward to quark i.
- **Mass budget** (of 938 MeV): quark 32% + gluon 36% + anomaly 23% +
  condensate 9%. Valence quark rest masses are ~9 MeV total, ~1% — more
  than 90% of the mass is dynamics.
- **Field energy:** E_field = internal motion + external motion +
  displacement. Pressure P(0) ~ 1e35 Pa, outward at the centre, inward
  beyond ~0.6 fm.
- **Gap:** ~1.73 GeV computed inside the model. The Clay proof is unsolved.
  The bridge — motion / medium / dilation giving the gap value — is the top
  missing piece, open for all ten council seats.

## The two framings the code cannot carry

**Gravity.** Gravity is the emission star — the body the light travels by.
The particle does **not** emit gravitational force; it **feels** it.

**Glue force.** The glue force is what links a particle to its own kind.
It lives in the after-image — the trail left behind — and it is **inside
the proton AND emitted beyond it**: an interior part, contained within the
proton, holding it together; and an exterior part, emitted out to a certain
distance beyond the proton, which is the after-image trail that reaches the
next proton and keeps the chain breathing. (Test 10 re-models this split
formally; see below.)

## Calibration shared by all tests

- Scale a0 = 0.24 fm; bare radius R0 = √12 · a0 = 0.8314 fm.
- Dipole form factor F(q) = 1/(1 + (q·a)²)²; high end at q·a0 = 3,
  F_single = 0.01.
- **Targets:** R = 0.840 fm, high-end hardening +6%.
- **Breathing** (test 2): AR(1) ln a, φ = 0.7, stationary s = 0.10,
  innovation σ_ε = 0.0714 → R = 0.8395 fm, hardening ~+6%.
- **Aura alternative** (test 3): w = 0.0081 at a0/2, tail z = 0.0089 at
  2a0, s = 0 → R = 0.8396 fm, +6.10%. Discriminator: along the chain.
- **CMB as a plain layer** (test 4): **CLEAN NULL.** u_CMB/u_p ~ 1e-48
  today, uniform to 1e-5, cannot drive breathing, no epoch trace.
  The CMB as raw energy density cannot do the job — which is why test 5
  treats it as a *regulated mode*, not an energy-density scaling.

## Test 5 — birth-to-proto bubble

`test5_birth_to_proto.py`

**Dakota's understanding (his words, held exactly):**

- The CMB is not a negligible layer. It is a field helper and a
  strengthening aspect: part of the medium itself. Light emits from its
  source as a continuous chain throughout space and time, so the first
  light is still present as the medium the new light travels through.
- Light is everywhere in the known conceivable universe. An emission
  source in one region couples with emission sources in other portions
  of that region. Regions with no stellar bodies are the void pockets
  (no local emission).
- The CMB is emitted light from the very first light source — an echo of
  the first source, with no source behind it anymore. New light (from
  stars) now rides on top of it, coming through the medium of first
  light.
- The first emission may NOT be the same type of light as what stars emit
  now — different waveforms/types. Model old light and new light as
  potentially different kinds.
- The breathing (the fluctuation that fixes the fit) is driven by the
  source of the NEW light: the star/proton's local emission region. New
  light is produced behind each proton in the chain. At the first spark
  there was no new emission until stars / proto-galaxies / proto-clusters
  formed.
- The present universe is oversaturated with waveforms from countless
  stellar bodies inside galaxies and clustered galaxies. Between galaxies
  there is no emission on the galactic disc itself, but refractive light
  from particle emission above and below the plane of the discs lets the
  internal structure of a galaxy be perceived from inside it.
- Model scope: from the first spark to the point where proto-galaxies
  start to form — a REGIONAL bubble, a contained expanding space-time.
  Do NOT model the whole current expansive medium.
- Center/epicenter logic (his): the NEWEST forming galaxies are probably
  the epicenter — the first explosion threw the oldest stuff farthest
  out, and the newer settling stuff is how you extrapolate the beginning.
  The apparent edge line is actually the new cooling area: a fluctuation
  of CMB inside a density that is nowhere else. Measure
  CIRCUMFERENTIALLY — around the bubble's circumference, not across the
  whole universe.

**Structure:** bubble t in [0,1], spark (t=0, 1+z = 1100) to proto-galaxy
epoch (t=1, 1+z = 11). (1+z) = 1100^(1−t) · 11^t. First stars at
t_sf = 0.5. Old light: uniform bath, u_old(t) = u_CMB_today · (1+z)^4.
New light: local stellar emission, anchored at (a) the solar constant at
1 AU near a star and (b) the collective galactic field, standard
interstellar radiation field u_ISRF ~ 1 eV/cm³ (literature anchor, solar
neighbourhood — NOT measured by us). Breathing gate: the medium's
breathing mode is ON (s = 0.10) where new light is present above the bath,
OFF (s = s_floor = 1e-5, CMB anisotropy) in void pockets. This is a
switch, not an energy-density scaling: test 4 showed raw energy-density
coupling needs amplification ~1e45 (u) to move anything, so the medium
must be a REGULATED mode that the new light triggers locally. The gate
boundary is where u_new = u_old.

**Found (computed):** fit radius **0.8398 fm** (local-medium value);
void pockets bare **0.8314 fm**. The medium must self-cap — the breathing
mode is regulated, not driven by raw energy density.

**Dakota's extensions from test 5** (his words, held exactly):

1. **Breathing gate:** the breathing flips ON at star creation — the
   medium's breathing mode IS stars themselves, not merely triggered
   by them.
2. **Stars as living systems:** a star is a living system that consumes
   and produces its own necessity; "living" needs redefining — everything
   is a food chain at no matter what level.
3. **Black hole = scaled-up proton:** the accretion disc looks the same
   from any angle because light bends — in reality infinite layered
   discs around the outer event horizon; the emission field is
   everywhere at once because the gravitational weight of the field
   itself collapses the comet shape; when spherical, expansion is those
   layers stacking outward.
4. **Micro-black-hole trigger:** a moving proton experiencing
   deceleration; deceleration feeds inside the energy loop, increasing
   the proton's overall size, and at a certain size mass develops inside
   the core, the core region compressed no matter the dimensions of the
   outer folds — folds inward = micro black hole.
5. **Stellar second stage:** the sun creates light at different levels
   through to its core; denser, darker light is kept inside by something
   at the surface level — there may be a second stage to the proton that
   only exists inside the pressurization of a star.

## Test 6 — birth-to-proto bubble WITH the breathing gate

`test6_birth_to_proto_gate.py` — extensions 1, 2, 5.

New vs test 5: test 5 gated breathing SPATIALLY (on where u_new > u_old).
Here the gate is TEMPORAL and LIVING: breathing is OFF everywhere before
first stars (t < t_sf = 0.5), and after star creation it is the star's own
metabolism that runs the mode — it ramps as the star forms, and it follows
the star's life (with a possible medium memory after the star dies). The
stellar second stage is added as a layer for protons INSIDE a star.

**Found (computed):**

- Closed fit UNCHANGED from test 5: lit region R = 0.8397 fm,
  hardening +6.20% (test 5: 0.8398, +6.18% — same within MC noise).
  Void pocket: 0.8314 fm.
- Before first stars (t < 0.5): the WHOLE bubble is bare, R = 0.8314 fm.
  The gate is temporal now, not spatial.
- Metabolism ramp s(t) = s_max(1 − exp(−(t−t_sf)/τ)): τ 0.05/0.10 fully
  on by t=1 (R 0.8395–0.8400); slow 1st-gen τ=0.20 reaches only
  s=0.0918, R = 0.8382 fm, H = +5.35%. Primed 2nd-gen (3x) fully on at
  any τ.
- Living medium / star lifetimes (τ_life = 0.30 assumed):
  (a) breathing follows the living star: breathing fraction at t=1 =
  0.18, R_vol = 0.8329 fm, hardening ~+1.12%.
  (b) medium remembers (τ_mem = 0.20): fraction 0.30, R_vol = 0.8339 fm,
  hardening ~+1.86% — same as test 5.
  The living gate can cut the breathing volume 0.30 → 0.18 at t=1.
- **Undetermined:** whether the mode is the star (dies with it) or the
  medium (remembers it). If stars live longer than the bubble,
  (a) = (b) = test 5.
- Stellar second stage (s2 = trapped-light amplitude, pc = pressure
  compression; both free parameters, sensitivity map not prediction):
  interior proton s2=0.10, pc=0 → R 0.8482 fm, H +12.83%; s2=0.20,
  pc=0 → R 0.8752 fm, H +33.09%; s2=0.20, pc=0.05 → R 0.8315 fm,
  H +58.26% (compression offsets radius). Surface proton: smaller
  shifts (s2=0.20, pc=0.05 → R 0.8342 fm, H +31.02%).
  **EXTERIOR observable: UNCHANGED.** The surface blocks the dense
  light, so the second stage stays hidden from outside in this toy.

## Test 7 — proton deceleration feeds the energy loop

`test7_proton_deceleration.py` — extension 4 (the hypothesis).

Toy energy-loop model (assumptions flagged where they enter): D =
deceleration energy fed into the loop per link, MeV per atom-length
(one link = one atom length = 1e5 fm of travel). η = 1: the lost kinetic
energy is retained INSIDE the loop (Dakota's framing). The loop leaks a
fraction λ of its mode energy per link (exponential leak, as in the base
model). Equilibrium mode energy E* = D·η/λ. The mode energy is the
breathing amplitude: s² = E_mode / m_p c². The regulated cap from tests
2/5 is s_max = 0.10, so E_cap = 938 · 0.01 = 9.38 MeV.
SELF-SUSTAINING threshold: D_crit = λ · E_cap — fed energy per link
exceeds what the loop leaks at the cap, so the mode grows past the
regulation. Core compression: the fed energy squeezes the core scale,
a_core = a0 · (1 − c_c · E*/E_cap), c_c = core compression coupling
(ASSUMPTION, scanned). The FOLD point is where a_core hits zero:
E_fold = E_cap / c_c, D_fold = λ · E_fold. The outer size keeps growing
(R = √12 · a0 · exp(s²)) while the core compresses — the two scales move
in opposite directions, as Dakota described. λ and c_c are NOT measured
by tests 1–5. Thresholds are reported as functions of them, with
fiducial λ = 0.05, c_c = 0.30.

**Found (computed):**

- Thresholds: D_crit = **0.469 MeV/link** (self-sustaining: fed > leaked
  at cap); D_fold = **1.564 MeV/link**; E_fold = 31.28 MeV; s at fold =
  0.1826. D_crit scales linearly with λ (0.094 at λ=0.01, 1.877 at
  0.20); D_fold scales as 1/c_c (4.691 at c_c=0.1, 0.938 at c_c=0.5).
  D_crit does NOT depend on c_c.
- Observables vs D: R 0.8314 (D=0) → 0.8401 (D_crit) → 0.8502 (D=1.0)
  → 0.8583 (D=1.5) → fold at 1.564 (R 0.8596, +3.4% total).
  Hardening: +28% (D=0.1), +66% (0.2), +257% (D_crit), +293% (0.5),
  +2077% (1.0), +9589% (1.5), fold. Core compression is the loud signal.
- Physical scale: D_crit = 2.25e5 W into one proton's loop; ~2.3e7×
  minimum-ionizing stopping, ~4.7e5× the Bragg peak. Ordinary
  deceleration in matter NEVER reaches the threshold.
- Dynamics: below threshold settles in ~20 links; above threshold
  crosses the cap in 2–30 links; fold needs D > D_fold, arrives in
  ~7–30 links (173 links at exactly D_fold — asymptotic).

## Test 8 — the micro black hole, past the fold

`test8_micro_black_hole.py` — extensions 3 and 4.

Takes test 7 past D_fold and asks, in the toy: does the emission field
collapse the comet shape (extension 3)? Does the breathing get trapped?
Does old light bend around it? Does new light start there? What happens
to the radius and hardening observables? Does the proton-scale version
show the layered-disc structure? Inputs from test 7 (fiducial λ=0.05,
c_c=0.30, η=1): E_cap = 9.38 MeV, E_fold = 31.27 MeV,
D_crit = 0.469 MeV/link, D_fold = 1.564 MeV/link, R_fold = 0.8596 fm.
New assumption: the trapped mode leaks slowly, λ_trap = 0.001 per link
(30–50× slower than the open loop — the trap holds the mode in).

**Found (computed):**

- **Emission field: YES, collapses comet → spherical.** θ/θ0: 1.000
  (D=0), 0.700 (D_crit), 0.361 (D=1.0), 0.041 (D=1.5), 0.000 at the
  fold.
- **Breathing: YES, trapped.** Transmission 0 at the fold; the fold is a
  breathing firewall — downstream chain links go bare unless lit by
  another source. Interior energy grows without bound in the toy: at
  D_fold, 46.5 MeV after 10 links, 177 MeV after 100 links (equilibrium
  D/λ_trap = 1564–5000 MeV). **Something must cap the interior; the
  model does not say what.**
- **New light: YES, starts there.** Leak = 0.031 MeV/link = **1.50e4 W**
  at the fold; dominates the CMB bath out to ~81 m at z=10, ~9.8 km
  today. Switches the breathing gate on in that neighbourhood (radius
  scales as √λ_trap).
- **Old light: NO gravitational bending.** r_s at fold energy = 8.3e-56 m
  = 8.3e-41 fm, 40 orders below the proton. Geometric capture only:
  π·R_fold² = 2.32 fm² vs bare 2.17 fm² (1.07×, no enhancement).
- **Layered discs: NO.** They need a photon sphere; the toy has none.
  The proton-scale version shows the SPHERICAL part of extension 3 but
  not the discs. Energy for r_s = 1 fm is 3.78e38 GeV — 1.2e40× the
  fold energy, ~19 orders short.
- Observables: R saturates at 0.8596 fm; hardening → +9900% at the fold
  (F → 1, core gone). **Past the fold the object is NO LONGER A
  PROTON:** R and the form factor are undefined for it. An outside
  observer sees a 0.86 fm object that stops scattering like a proton at
  high q and glows faintly with new light.

## Test 9 — the micro black hole as a light source seeding clusters

`test9_micro_bh_clustering.py`

**Dakota's addition (his words):** the MBH sits inside the emission field
taking the place of one of the light sources; it emits light to an
accretion disc, pulls in neighboring protons, and forms bigger clusters.

The MBH is a light source WITHIN the emission field (it replaces one link
in the chain), it emits to its accretion disc (the infalling shell of
protons its light lands on), it pulls in neighbouring protons, and it
seeds larger cluster formation. Inputs from tests 5–8 (fiducial): MBH
trapped leak at the fold 0.031 MeV/link = 1.50e4 W (test 8); MBH lit
radius (breathing gate ON, u_new > u_old) 81 m at z=10 (test 8); mode
energy at the regulated cap E_cap = 9.38 MeV; a single lit proton's
open-loop leak λ·E_cap per link = 0.469 MeV/link = 2.25e5 W — but most
of that is RECYCLED into the chain (the emission field is local), not
radiated to infinity; the fraction that escapes as free light is
ε_rad, UNKNOWN, scanned (1, 0.01, 1e-4); the MBH's trapped leak is
treated as escaping (it is new emission by construction, test 8).
Epoch: proto-galaxy, z=10. Gas temperature for thermal motion T_gas =
1e4 K (ASSUMPTION, proto-galaxy gas; the CMB at z=10 is 30 K). Chain
spacing: one atom length = 1e-10 m. Standing corrections kept: NO spin /
NO external rotation — so the "disc" in this toy is a spherical infall
shell, not a rotating disc.

**Found (computed):**

- The MBH as a light source: leak **1.50e4 W** at the fold. Robust
  capture = lit radius ~81 m at z=10 (breathing gate ON, well deep at
  E_cap = 9.38 MeV >> kT). Weak outer edge (smooth gate, mode energy =
  kT) ~2.7e5 m. Protons inside the lit radius: **7.4e8** (mean density),
  7.3e10 (100× overdense), **2.2e13** (proto-galaxy 1e7/m³). Inside the
  weak edge: 2.7e19 / 2.6e21 / 8.0e23. The MBH's own chain contributes
  2r/1e-10 = 1.6e12 protons within 81 m (a subset of the 3D count);
  nearest neighbours fall in first, and the chain BREAKS at the MBH
  (test 8 firewall).
- The MBH brightens ~64× as its interior fills (1.5e4 → 9.6e5 W), solo
  lit radius **81 m → ~650 m**. The cluster's collective power overtakes
  it once N > 667 (ε=1e-4) or immediately (ε=1).
- Accretion disc = the infall shell at r_gate: the MBH's light lands on
  it and switches the shell protons' breathing on. SPHERICAL in the toy
  (no spin — standing correction); no layered discs (test 8 stands).
  Disc radius grows with the cluster; once the shell holds >~100 protons
  (ε=1) it outshines the MBH and the disc becomes self-lit.
- Growth: superlinear, N_next ~ N^1.5 per round (r ~ √N, volume ~ r³).
  Proto-galaxy (supply 1.23e66 protons = 1.04e9 M_sun, R=1 kpc,
  n=1e7/m³): stabilizes at the full supply after 4 rounds (ε=1) or 5
  (ε=0.01, 1e-4), ~2e5 years of infall time. Small clump (4.06e54
  protons = 3.4e-3 M_sun, R=1 pc): 4–5 rounds, ~200 years.
- Stabilization: the cluster keeps growing until the LOCAL SUPPLY is
  exhausted, then stabilizes at the overdensity's mass. There is NO
  physics-limited fixed point in this toy; ε_rad changes only the number
  of rounds, not the outcome.
- Final state: small clump ends as a BALL OF BREATHING PROTONS, packed
  at atom spacing (R = 9.9e7 m, r_s = 10 m, R/r_s ~ 1e7). Proto-galaxy
  cluster ends INSIDE its Schwarzschild radius (packed R = 6.7e11 m,
  r_s = 3.1e12 m, **R/r_s = 0.22**) — by the scale argument it becomes a
  black hole, IF the infall really packs to atom spacing. Threshold:
  clusters above N = 1.25e65 protons = **~1e8 solar masses** sit inside
  their horizon when packed. **The collapse dynamics are NOT modeled**
  (no gravity in the chain); the packing assumption does the work.
- Timescale: proto-galaxy assembles in ~2e5 years (universe at z=10 is
  ~5e8 years old); early rounds take seconds to days.
- Open: ε_rad (key unknown — sets rounds, not outcome); self-shielding
  (an optically thick cluster traps its own light — a real stabilizer
  the toy does not model); chain vs 3D structure; disc rotation (no
  spin); collapse dynamics; neighbouring clusters competing for the same
  protons.

## Test 10 — the glue force re-modeled, inside and outside

`test10_glue_force_two_part.py`

**Dakota's new understanding (his words, held exactly, Nov 6 live call):**
the glue force is ALSO inside the proton — it is part of what gets
emitted out to a certain distance beyond the proton itself, but it is also
contained within inside of it. So the glue force has two parts: an
interior part, contained within the proton, holding it together; and an
exterior part, emitted out to a certain distance beyond the proton, which
is the after-image trail that reaches the next proton and keeps the chain
breathing.

Starting point is the filed formula (INN-165), taken as given, not
re-derived: V = σ·L_min, σ = 0.94 GeV/fm; F_i = −σ·n̂_i (outward);
M = 0.32 + 0.36 + 0.23 + 0.09 of 938 MeV; E_field = internal + external
+ displacement; P(0) ~1e35 Pa, outward at center, inward beyond ~0.6 fm.

**The split (computed).** The trail holds the leaked mode energy for one
coherence length: E_trail = λ·E_cap·N_coh = 0.05 · 9.38 · 3.33 =
**1.564 MeV** (fiducial λ = 0.05, assumed; φ = 0.7 measured, test 2).
As a tension: σ_out = E_trail/(N_coh · 1e5 fm) = 4.69e-9 GeV/fm,
σ_out/σ_in = 5.0e-9 — the leak is a trickle next to the confining
force. **The exterior glue is NOT a second confining tension; it is a
coupling field, and its strength is measured in energy, not tension.**
By total glue-field energy: interior 336.2 MeV (99.54%) / exterior
1.56 MeV (**0.46%**) of the 36% gluon slice; the split lives entirely
inside that slice and the other budget slices are untouched. By dynamic
(breathing-mode) energy: exterior **16.7%** / interior 83.3%. The
exterior is energetically tiny and dynamically load-bearing. The split
scales linearly with λ (3.3% of mode at λ=0.01, 33.3% at 0.10, 66.7% at
0.20) — λ is unmeasured by tests 1–9. (Digit coincidence flagged:
E_trail = 1.564 MeV and D_fold = 1.564 MeV/link share digits; different
quantities.)

**The emission distance.** Two readings, kept apart. As a FORCE: a
single emission event's wake decays exp(−x/0.25 fm) — at one atom length
it is exactly 0; a single wake does NOT reach the next proton. The trail
is a STANDING structure: continuous emission, re-emitted every link
(link time 3.34e-19 s), sustained by the nearest re-emitters. Falloff,
not a sharp edge; near-field scale ~0.25 fm per event, refreshed link to
link. As LIGHT: the escaping fraction radiates as 1/r²; single lit
proton lit radius at z=10 is 313 m (ε=1), 31 m (0.01), 3.1 m (1e-4);
today 38 km / 3.8 km / 379 m. MBH cross-check: 80.8 m at z=10 (tests
8–9: ~81 m), 9.8 km today (test 8: ~9.8 km). The chain tension lives in
the near field; the lit radius is where emitted light dominates the
bath, not where the glue stops pulling.

**Chain tension.** Trail coupling V_out(d) = −E_trail·φ^d: −1.09 MeV at
1 link (~12% of the 9.38 MeV well), −0.54 MeV at 3 links, total chain
binding **−3.65 MeV per proton** (~39% of the well). The nearest-neighbour
bond sits between D_crit (0.469) and D_fold (1.564): a neighbour's pull
alone cannot fold a proton, but at ~2.3× D_crit it is a real drive.
**VERDICT: yes — as a COUPLING, not an energy pipeline.** Each link's
mode is driven locally by new light; the trail synchronizes the breathing
(φ = 0.7/link, ~3-link coherence). Honest gap: φ is measured, not
derived from λ; the toy cannot derive the coherence length from the
field dynamics (needs the medium's patchiness modeled).

**Fit check (MC, 200 × 2000 links).** Interior only: R = 0.8314 fm,
hardening +0.00%. Two-part: R = **0.8394 fm** (target 0.840, miss
−0.0006 fm), hardening +6.33% (target +6%, miss +0.33 points) — both
inside MC noise. The re-modeled formula reproduces both fits; the
interior sets the bare radius and the exterior breathing mode lifts it
and hardens the high end.

**The re-modeled formula.** V_glue = V_in + V_out. V_in = σ_in·L_min,
σ_in = 0.94 GeV/fm (filed, interior, confining), F_i = −σ_in·n̂_i.
V_out = −E_trail·φ^d, E_trail = 1.564 MeV (fiducial), φ = 0.7/link, d
in links; total chain binding −3.65 MeV per proton; as a tension
σ_out = 4.7e-9 GeV/fm. E_field and the mass budget unchanged; the
0.6 fm pressure sign change is the force-picture boundary between
interior (pushing out) and exterior (binding, pulling in). Geometric
note, NOT a derivation: the interior volume fraction (0.6/0.84)³ =
0.364 happens to equal the 36% gluon slice — coincidence of two
unrelated ratios.

**Open / underdetermined.** (a) λ — sets the split; pin it down with a
trail-energy measurement, ε_rad, or a single proton's lit radius.
(b) φ's origin — measured, not derived; needs the medium's patchiness
modeled. (c) No sharp spatial energy boundary — it is a falloff;
0.6 fm is the force-picture boundary, not an energy-partition boundary.
(d) σ_in is taken from INN-165 by construction, not re-derived. (e) No
spin / no rotation throughout; the trail is a scalar coupling in this
toy.

## What is a claim vs what is computed

- **Computed (a script produced the number):** all fit radii, hardening
  percentages, thresholds (D_crit, D_fold), leak powers, lit radii,
  cluster counts, the −3.65 MeV/proton chain binding, the 0.46% / 16.7%
  exterior split, the 0.8394 fm two-part fit.
- **Framing (Dakota's understanding, held in his words):** the CMB as
  field helper and medium; new light vs old light as different kinds;
  breathing mode IS stars; stars as living systems / food chain at every
  level; black hole as scaled-up proton; deceleration folds a proton
  inward; gravity as the emission star that is felt, not emitted; glue
  force linking a particle to its own kind; the epicenter logic (newest
  galaxies as epicenter); measure circumferentially.
- **Assumptions (put in by hand, flagged in the scripts):** λ = 0.05
  (leak per link), c_c = 0.30 (core compression coupling), η = 1
  (deceleration energy retained in the loop), λ_trap = 0.001 (trapped-mode
  leak), τ_life = 0.30 (star lifetime), T_gas = 1e4 K, ε_rad unknown
  (scanned 1, 0.01, 1e-4), s2 and pc (stellar second stage, free
  parameters — sensitivity map, not prediction).
- **Bridge candidate, open:** the claim that motion / medium / dilation
  gives the gap value (~1.73 GeV). Filed as a bridge candidate (INN-177
  claim 1), NOT a verified result. The Clay proof is unsolved.
- **Standing corrections kept in the toys:** no spin / no rotation
  anywhere (the test-9 "disc" is a spherical infall shell); the test-8
  "black hole" is a FIELD-TRAPPED state, not a gravitational one (a real
  horizon at proton scale needs ~1e38 GeV in the trap); past the fold
  the object is no longer a proton.

## Files

| File | What it is |
| --- | --- |
| `test5_birth_to_proto.py` | Birth-to-proto bubble; breathing gate (spatial); fit 0.8398 fm |
| `test6_birth_to_proto_gate.py` | Bubble WITH the breathing gate (temporal, living); stellar second stage |
| `test7_proton_deceleration.py` | Proton deceleration feeds the energy loop; fold thresholds |
| `test8_micro_black_hole.py` | Micro black hole past the fold; emission collapse, trapped breathing, new light |
| `test9_micro_bh_clustering.py` | MBH as light source seeding clusters; growth to proto-galaxy scale |
| `test10_glue_force_two_part.py` | Glue force re-modeled: V_glue = V_in + V_out |
| `test6-7-8_results.md` | Full results write-up for tests 6–10 (Nov 6, 2026) |

## Running

All scripts are plain Python 3 with NumPy. Run from the repo root, e.g.
`python3 test5_birth_to_proto.py`. Each script prints its results and
exits 0 on a clean run. Tests 5–10 ran clean (exit 0) on Nov 6, 2026.

## Provenance

Model and framings by Dakota Higgins, developed in dialogue with Muse
(Nov 2026). The filed record lives in the Linear workshop (INN-165–177,
project P-INN-28); the workshop holds the dialogue and record, this repo
holds the code. GitHub is the archive for code; Linear is the archive for
record — never the other way around.
