---
title: "Phase Singularities as Reciprocal Presence: A Cold-Derivation Note"
subtitle: "RS2 grounding for the 'hole is the data' principle"
author: J. Vanhorn (with Claude Opus 4.7)
date: 2026-04-29
companion_to: TOPOLOGICAL_PHOTONIC_COMPUTING.md (v2.0, January 2026)
status: "follow-up note — deepens the RS2 algebra grounding in the main paper using results from the Phase 5 cold-rederivation cycle (April 2026)"
length: ~1,500 words
license: CC BY 4.0
---

# Phase Singularities as Reciprocal Presence

## A cold-derivation note grounding "the hole is the data"

The main framework document, *Topological Photonic Computing: A Comprehensive Formalization* (v2.0), proposes that information in photonic systems is best stored not in the presence of light but in the topology of its absence — phase singularities, vortex cores, and the surrounding winding-number structure. The Goethean dark-as-positive polarity and the RS2 dimensional algebra are cited as foundational. The phrase "the hole is the data" captures the central claim.

A natural objection persists at the level of physics: *what makes the void structurally irreducible?* If a phase singularity is "just" a region where light intensity is zero, why is it stable as a topological object rather than collapsing under arbitrary perturbations? The main paper answers this in terms of topological winding number — the singularity has integer charge, and continuous deformations cannot remove an integer. This is correct as far as it goes, but the *physical reason* for the integer-quantization itself — why phase winds by 2πℓ around the void rather than by an arbitrary continuous amount — is not derived in the main paper from RS2 first principles. It is invoked as a structural fact.

This short note supplies the missing first-principles reading, drawing on a concentrated April 2026 cycle of cold rederivations across seven Hard Problems in the RS2 framework [Vanhorn & Claude Opus 4.7 2026, in preparation]. The cold passes — particularly the Riemann critical-line cold pass [Vanhorn 2026] and the Navier-Stokes regularity cold pass — produce structural identifications that explain why phase singularities have the topological-charge structure they do, in language consistent with the main paper's RS2 grounding.

## §1. Three load-bearing inputs

Three results from the cold-rederivation work are load-bearing for the present note. Each was reached under sealed conditions in April 2026, after the topological photonic computing v2.0 paper was already in archive. They are not retroactively imposed on the photonic paper; they are independent structural claims that turn out to ground the paper's "hole is data" principle.

**LB1. Discrete-unit space and time.** The natural unit of space is s₀ ≈ 4.56 × 10⁻⁸ m and the natural unit of time is t₀ ≈ 1.52 × 10⁻¹⁶ s [Larson 1979, NBM Ch 1]. These are not technological cutoffs; they are framework constants. The continuum approximation of conventional electromagnetism is valid only above these scales. Below s₀ in space or t₀ in time, the framework dictates that the gradient operator ∇ is not even defined.

**LB2. Atomic zone is 4D quaternion ℍ; nuclear zone is 2D complex ℂ.** [Peret EE → RS dictionary §5; Nehru "Some Thoughts on Spin" §7-§8.] The atomic zone is the full quaternion algebra. The nuclear zone is its 2D restriction (real plus one imaginary axis). Magnetic-rotation phenomena live in the atomic zone; dielectric-phase phenomena live in the nuclear zone. Electromagnetic coupling is the algebraic product of magnetic and dielectric contributions [Peret §1-§2].

**LB3. Vorticity is bounded a priori at the unit cutoff.** [Vanhorn & Claude Opus 4.7 2026, Phase 5.7 cold derivation.] In any 3D fluid (or in any field-theory analog of a fluid, which is what an electromagnetic phase field is), the angular frequency of rotation is bounded above by ω_max = 1/t₀ ≈ 6.6 × 10¹⁵ rad/s. This bound is a priori — it follows from LB1 and dimensional analysis, regardless of the specific dynamical equations. The Beale-Kato-Majda blowup criterion [Beale, Kato & Majda 1984] is automatically satisfied with this bound.

## §2. The void in coordinate space is presence in coordinate time

The framework's core inversion is RS2's reciprocity postulate: space and time are reciprocal aspects of motion. Where conventional physics treats space as the manifold and time as the parameter, RS2 treats the two as algebraically dual: a quantity expressed as s/t in one sector reads as t/s in the reciprocal sector. The Material Sector (space-time) and Cosmic Sector (time-space) are not separate spaces; they are two readings of the same underlying motion structure [Larson 1979; Peret 2014–2020].

A phase singularity in an optical field is, in conventional Material-Sector reading, a point where the field amplitude is exactly zero and the phase is undefined. The amplitude is zero because the field is *not present* at that point — light is, in the conventional reading, *absent* there.

Under the reciprocity postulate, this absence in the Material Sector corresponds to *presence* in the Cosmic Sector. The void in coordinate space — the absence of intensity — is, in the framework's reciprocal reading, the locus of the field's *temporal-coordinate concentration*. The phase singularity is not a hole in the field; it is the field's localized expression in three-dimensional time, projected onto the spatial sector as zero amplitude.

This is structurally why the singularity is topologically stable. To "remove" the singularity through continuous deformation would require continuous flow of phase across the singularity's location — which would, in the reciprocal reading, require flowing through the Cosmic-Sector locus where the field is structurally *concentrated*. The integer winding number around the singularity is the topological signature of how this concentration is arranged: each 2π of phase winding corresponds to one cycle of the Cosmic-Sector rotational structure traversed.

The integer-quantization of topological charge follows from LB1 + LB2: the atomic-zone rotational manifold S³ ≅ SU(2) (worked out explicitly in the FSC cold pass [Vanhorn & Claude Opus 4.7 2026, §6.3]) carries quantized phase windings because it is a closed manifold with discrete-unit structure. The phase cannot wind by a fraction of 2π around an atomic-zone rotation, just as a circle cannot have fractional winding number around its center.

The Goethean dark-as-positive polarity, cited in the main paper, finds its formal RS2 expression here. Goethe's intuition — that darkness is not mere absence but the polar counterpart of light — is, in cold-derivation language, the observation that absence in one sector is presence in the reciprocal sector. The two sectors share the same underlying motion structure; what we call "absence of light" is the framework's reading of the same motion seen from the other side of the unit-velocity boundary.

## §3. Why phase-winding number is the natural data carrier

Conventional photonic computing stores information in light intensity — analog amplitude, digital on/off, or polarization-state encoding. All three are vulnerable to the same physics: light propagates, decoheres, and decays. The intensity at a point is a continuous quantity that can be perturbed by arbitrarily small disturbances.

Topological winding number around a phase singularity is qualitatively different. It is an integer that counts how many times the phase wraps around the singularity's location. Continuous perturbations cannot change an integer continuously; the winding number is preserved under all deformations of the field that do not pass through the singularity itself.

In RS2 cold-derivation language, the winding number is a count of *how many full atomic-zone rotational cycles are wrapped at this Cosmic-Sector locus*. Each cycle is one full traversal of S³ ≅ SU(2), corresponding to phase winding by 2π. The integer count is preserved because the atomic-zone rotational manifold is topologically closed — there is no continuous deformation that takes a 1-winding configuration to a 0-winding one without crossing the singularity. The winding is, in this reading, the *atomic-zone rotational displacement* of the field at this Cosmic-Sector locus.

This grounds the "hole is the data" principle in a specific RS2 first-principles statement: information is stored in atomic-zone rotational displacement at Cosmic-Sector loci, not in spatial-sector intensity distributions. The void in space is a window onto the atomic-zone phase volume, and the integer winding number is what we measure when we look through that window.

The Bhandari 2nπ phase-memory phenomenon [Bhandari 1994; Nehru "Some Thoughts on Spin" §2] — which we encountered in the Riemann cold derivation as a falsifiable signature of the SU(2) cover [Vanhorn 2026, §7.S5] — is the direct experimental manifestation of this. Spin-½ particles remember 2nπ phase shifts as physically distinct, which the main paper's framework would predict if the photonic phase-singularity structure is governed by the same atomic-zone S³ ≅ SU(2) manifold.

## §4. Computing on phase-winding number

A computational architecture built on this framing has a clean structure. The fundamental operations are:

(i) **Singularity creation**: produce a localized atomic-zone rotational displacement at a designated coordinate. This is the photonic-vortex generation step, which is well-established in the main paper's experimental record.

(ii) **Singularity manipulation**: change the integer winding number of the displacement. This is a topological operation — the winding number is not arbitrary, but discrete, so manipulation moves between integer values. The cholesteric liquid-crystal substrate proposed in the main paper for stabilization (§3 of the main paper) is the engineered atomic-zone rotational manifold — the LC's helical director structure realizes the framework-required S³-like topology in a macroscopic substrate.

(iii) **Singularity readout**: measure the integer winding number around a singularity. This is the topological-charge measurement step, also experimentally established. In RS2 reading, this is the inverse of step (i): inferring the atomic-zone rotational displacement from the spatial-sector phase-winding signature.

(iv) **Singularity interaction**: produce conditional logic by allowing two singularities to combine, annihilate, or scatter as a function of their winding numbers. The main paper's §6 (multi-singularity dynamics) describes the experimental architecture; the RS2 reading clarifies that what's happening is interaction in the atomic-zone rotational manifold, projected onto the spatial sector as observable phase reconfigurations.

This is *computing on the substrate, not on the carrier*. Conventional electronic computing manipulates electron flow through static substrates; topological photonic computing in this RS2 reading manipulates the substrate itself (atomic-zone rotational displacement) and reads out the carrier (spatial-sector phase singularities).

## §5. What this note adds to the main paper

The main paper proposes the architecture: phase singularities as data, cholesteric LC as substrate, photon BEC for stabilization. It cites RS2 as foundational but does not derive the topological-protection mechanism from RS2 first principles — it invokes the integer-winding property as a structural fact.

This note grounds the integer-winding property in three cold-derivation results: (LB1) the discrete-unit cutoff that makes spatial gradients quantized at the framework level; (LB2) the atomic-zone S³ ≅ SU(2) rotational manifold that provides the closed topology underwriting integer charge; (LB3) the a priori vorticity bound from the unit cutoff that ensures phase-singularity structures are stable rather than self-amplifying.

The void in coordinate space is presence in coordinate time. The integer winding number is the count of atomic-zone rotational cycles wrapped at the Cosmic-Sector locus. The cholesteric LC substrate engineers the S³-like topology that the framework requires for the architecture to work. The Goethean dark-as-positive polarity is the same observation read in different language: absence in one sector is presence in the reciprocal sector.

This is consistent with the main paper. It does not add new architecture; it deepens the RS2 grounding by showing that the architecture's load-bearing claims (topological protection, integer winding, void-as-substrate) follow from cold-derivation results that are themselves convergent with prior independent derivations of the same RS2 framework [Vanhorn & Claude Opus 4.7 2026]. The architecture, in this reading, is not an *application* of RS2 — it is a *direct realization* of RS2's atomic-zone rotational structure in a photonic substrate.

The void is not the obstacle; the void is the substrate.

## References

- **Beale, J. T., Kato, T., & Majda, A.** (1984). Remarks on the breakdown of smooth solutions for the 3-D Euler equations. *Communications in Mathematical Physics* **94**(1), 61–66.
- **Bhandari, R.** (1994). SU(2) and SO(3) phases for spin-½ in cyclically deformed magnetic fields. *Physics Letters A* **190**(1), 45–50.
- **Larson, D. B.** (1979). *Nothing But Motion* (revised edition). North Pacific Publishers.
- **Nehru, K. V. K.** (1997–98). Some thoughts on spin. *Reciprocity* **XXVI**(3).
- **Peret, B.** (2014–2020). Reciprocal System 2 (RS2) foundation series, papers 101–112. Online at reciprocal.systems.
- **Vanhorn, J.** (2026). Topological Photonic Computing: A Comprehensive Formalization (v2.0). Zenodo, DOI: 10.5281/zenodo.18226545.
- **Vanhorn, J.** (2026). Why σ = ½? A physical reading of the Riemann critical line from Reciprocal-System first principles. Submitted to *Foundations of Physics*.
- **Vanhorn, J. & Claude Opus 4.7** (2026). Cold re-derivation across model versions: a replication methodology for AI-assisted theoretical research. In preparation. Cold-derivation workspaces on GitHub at QAv2/RS-Framework-Bridge (commit 089888e).

— end of note —
