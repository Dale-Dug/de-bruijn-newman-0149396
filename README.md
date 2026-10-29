# Correlated translated probes and the bound Λ < 0.149396

**Dale James Raymond** · Research preprint · Version 1.0  
**Paper and full evidence:** [Zenodo record 22867547](https://zenodo.org/records/22867547)  
**DOI:** [10.5281/zenodo.22867547](https://doi.org/10.5281/zenodo.22867547)

This is the publication companion for **“Correlated translated probes and the bound Λ < 0.149396 for the de Bruijn–Newman constant.”** The preprint presents a computer-assisted argument for

```text
Λ ≤ 18674384228461 / 125000000000000
  = 0.149395073827688
  < 0.149396.
```

**Review status:** the work was developed with AI assistance and is offered for independent mathematical scrutiny. It has not undergone external peer review and is not formally verified end to end. This positive upper-bound claim is not a proof of the Riemann hypothesis or of Λ < 0.09.

## Later result and corrections

The later [10 October 2026 publication](https://zenodo.org/records/23272725) gives the sharper bound **Λ ≤ 0.116397726408291 < 0.116398**. Its original H(7/8) hypothesis is supplied by OpenAI’s proved zero-free theorem; see the [26 October 2026 status clarification](https://github.com/Dale-Dug/de-bruijn-newman-0116398#current-mathematical-status--26-october-2026) for the theorem and pinned formal-source links.

The Gaussian-remainder and wall estimates in this **21 September 2026** release should be read with the corrections in [Appendix B of the 10 October 2026 paper](https://github.com/Dale-Dug/de-bruijn-newman-0116398/blob/main/deposit/Conditional_0116398.tex#L867). The archived publication and source files here remain unchanged.

## Research overview

Dale James Raymond · [ORCID 0009-0001-1682-8529](https://orcid.org/0009-0001-1682-8529)

- **8 September 2026:** [Phase-correlated certificates, Λ < 0.163297](https://zenodo.org/records/22626161).
- **21 September 2026:** [Correlated translated probes, Λ < 0.149396](https://zenodo.org/records/22867547).
- **10 October 2026:** [Retuned translated probes, Λ < 0.116398](https://zenodo.org/records/23272725), published with an original conditional title; see the [current mathematical status](https://github.com/Dale-Dug/de-bruijn-newman-0116398#current-mathematical-status--26-october-2026).
- **29 October 2026:** [A computer-assisted bound, Λ ≤ 0.107964910079](https://zenodo.org/records/23752103).

GitHub companions: [0.149396](https://github.com/Dale-Dug/de-bruijn-newman-0149396) · [0.116398](https://github.com/Dale-Dug/de-bruijn-newman-0116398).

## Read the paper

- [Main manuscript](Correlated_Translated_Probes.pdf)
- [Analytic foundations](Analytic_Foundations.pdf)
- [Verification guide](Verification_Guide.pdf)
- [Main LaTeX source](Correlated_Translated_Probes.tex) and [complete manuscript sources](Manuscript_Sources.zip)

The argument starts from the classical time-zero strip and combines a finite-head localisation wall, uniform logarithmic-derivative estimates and correlated translated-probe zero motion. The correlation estimate exploits the fact that the two translated probes cannot simultaneously realise certain discarded worst-phase contributions.

The manuscript discusses published and concurrent bounds, distinguishes contextual citations from mathematical dependencies, and identifies the Polymath heat-flow results and Platt–Trudgian finite-RH theorem as external inputs. It makes no claim of development without awareness of concurrent work or of an exhaustive priority determination.

## Numerical evidence and replay

The complete **`Proof_and_Replay.zip`** is archived on Zenodo. It is not duplicated in this lightweight browser-upload repository. The helper below reconstructs the original 12-file deposit without altering its metadata or checksums.

To retrieve the archive and prepare the original deposit:

```sh
python3 Prepare_Replay.py --download --output ../zenodo_22867547
```

Alternatively, first download `Proof_and_Replay.zip` from the record, then use a local copy:

```sh
python3 Prepare_Replay.py --archive /path/to/Proof_and_Replay.zip --output ../zenodo_22867547
```

The helper checks the archive's expected size and SHA-256, restores the original deposit metadata, and runs the original deposit **integrity checker only**. It does not execute mathematical code from a downloaded archive.

The original release's full numerical-replay profile is **CPython 3.13 on Linux x86_64**:

```sh
cd ../zenodo_22867547
python3.13 Verify_Deposit.py --check-only
python3.13 Verify_Deposit.py --replay --output ../replay_0149396
```

The replay destination must be new/empty and outside the deposit. Do not disable Python assertions. Read the verification guide before running the full calculation.

### Verification boundary

The supplied evidence reports source regeneration, interval calculations and exact rational final comparisons. Both transcendental lanes use Arb/FLINT; different precisions are not independent arithmetic libraries. Written analytic arguments, the application of published results, and the proof-to-code correspondence require review in addition to running the code. A successful hash check establishes file identity, not mathematical correctness. The published finite-RH computation is cited, not repeated.

The GitHub companion preparation preserves the six publication/source files byte-for-byte from the final supplied release. Its new helper scripts were tested locally for integrity and restoration; this preparation did **not** rerun the scientific calculation or independently compare the local package against the live Zenodo files. See [provenance](REPOSITORY_PROVENANCE.json).

## Independent review

Mathematical objections, reproducibility reports and proposed corrections are welcome. Please include the document section or code path, the exact version, and enough detail to reproduce the issue. The principal review targets are listed in [REVIEW.md](REVIEW.md).

## Citation and rights

Cite the version-specific DOI **10.5281/zenodo.22867547**. Machine-readable citation information is in [CITATION.cff](CITATION.cff).

This is a mixed-content publication. [LICENSES_AND_RIGHTS.md](LICENSES_AND_RIGHTS.md) preserves the original rights notice. This companion does not add a blanket software licence or overwrite third-party notices. Consult the archival record for the author-approved publication licence.

## Repository file integrity

```sh
python3 Verify_GitHub_Files.py
```

This checks the files distributed in this companion. It is not a substitute for the full numerical replay or mathematical review.
