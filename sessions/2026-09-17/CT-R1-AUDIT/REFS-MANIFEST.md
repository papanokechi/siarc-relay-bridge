# `refs/` manifest — hashes, not bytes

*Built at R21. This is the artefact the "manifest route" has until now only
named: `REFS-LICENCE-REVIEW.md` **recommended** committing a manifest instead
of the files, and the recommendation was adopted in prose, but no manifest
file existed and nothing excluded `refs/` from a commit.*

A hash proves a later reader fetched the same bytes. The bytes themselves
stay out of the repository under the standing hold (review #15).

## What a commit would have staged before this round

`sessions/2026-09-17/` was, and remains, untracked. There was **no**
`.gitignore` anywhere above `CT-S1-THEOREM/lean/`, so `git add sessions/`
would have staged **all 69** files below — including the whole-page AIF
renders and the Gautschi page image, the two items the review names
explicitly as DO NOT COMMIT. That is now prevented mechanically by
`sessions/2026-09-17/.gitignore`.

## Inventory

`in review?` records whether the file has a row in `REFS-LICENCE-REVIEW.md`.
**No licence determination is made here.** Every third-party row is
**NOT CHECKED**, which is what the review says and what the deposit-day pass
is for.

| file | bytes | sha256 | class | in review? | licence |
|---|---|---|---|---|---|
| `CT-R1-AUDIT/refs/dlmf_5.11.html` | 212100 | `929045c7b1cd72f35e8d6e2c966340e30d2c3b990245d44e42f5de8c1caea28e` | third-party | yes | redistribution permission **NOT CHECKED** |
| `CT-R1-AUDIT/refs/dlmf_bib_W.html` | 301692 | `2a90b9f01153541fe38f804d5ef07a3274d565cd8672e81e9c9a91cc5dab640d` | third-party | yes | redistribution permission **NOT CHECKED** |
| `CT-R1-AUDIT/refs/gautschi_p34_bot.png` | 154297 | `e6728427ef0bb80c16d30c9cf260134f2027fdb07befedb1ccfebd678b28f468` | third-party | yes | redistribution permission **NOT CHECKED** |
| `CT-R1-AUDIT/refs/parse_dlmf.py` | 1163 | `8058738bfc665bd7ed45094941650f892357088c9df45a5f52e7869d3e400d00` | session-produced | **no row** | written in this run; not third-party material |
| `CT-R1-AUDIT/refs/vanderPut-Saito-AIF-2009-59-7-2611.pdf` | 1058380 | `1666bd6be824a99fc0b48adbe48233a9b2a520fd7e8adf187e98d22525473605` | third-party | yes | redistribution permission **NOT CHECKED** |
| `CT-R1-AUDIT/refs/vquad_resurgence_v1.0_zenodo-20455090.pdf` | 538588 | `c07c97d6fcd4d65bb888f951e853c85d21897a55190290fa3e32f38410ff1601` | operator's own | **no row** | operator's own deposit; deposit licence field **NOT CHECKED** |
| `CT-R1-AUDIT/refs/vquad_resurgence_v1.1_zenodo-20480603.pdf` | 606008 | `e07c1ddab16ffe22e2a118a1f8c97f45c9b959148af01933c9a4a50bc2a790a1` | operator's own | **no row** | operator's own deposit; deposit licence field **NOT CHECKED** |
| `CT-R1-AUDIT/refs/vquad_resurgence_v1.2_zenodo-20481592.pdf` | 612719 | `a5d9e264699e6397030f0512e17f0cd503fcf2eafd57db9b00b57523fcc88d85` | operator's own | yes | operator's own deposit; deposit licence field **NOT CHECKED** |
| `CT-S16-MEMBERSHIP-C/pages/arxiv_v5_p34_B1_LOOK.png` | 129975 | `cc0c0a7288ebb49c16de6b77da1a909185e15c6ce29d2fc8e77ffade8cac1fe4` | third-party | **no row** | redistribution permission **NOT CHECKED** |
| `CT-S16-MEMBERSHIP-C/pages/arxiv_v5_p34_bz_LOOK.png` | 285295 | `294f4e3e93210b4901ff88b641e4963061779de4205c457434be92493089b400` | third-party | **no row** | redistribution permission **NOT CHECKED** |
| `CT-S16-MEMBERSHIP-C/pages/vdps_j2655_B1_LOOK.png` | 79753 | `30bd48636e954107a941a58780758725a10bfe220a545fe7c4a4c61694e30716` | third-party | **no row** | redistribution permission **NOT CHECKED** |
| `CT-S16-MEMBERSHIP-C/pages/vdps_j2655_B1_top_LOOK.png` | 89996 | `671605d290fb0fa3eac158861f42d739c4e8f98ff946d1d61f8ef9c3432e4b29` | third-party | **no row** | redistribution permission **NOT CHECKED** |
| `CT-S16-MEMBERSHIP-C/pages/vdps_j2655_bz_LOOK.png` | 293661 | `7b15033a8fc42e9aea1afbde29a7f2ce75208a54e7de71c5f050705bf098bead` | third-party | **no row** | redistribution permission **NOT CHECKED** |
| `CT-S16-MEMBERSHIP-C/pages/vdps_p2635.png` | 278080 | `56194f2639b0aa20d6e96863373e92ee599165e357b6b4b8c9221474b070da6b` | third-party | yes | redistribution permission **NOT CHECKED** |
| `CT-S16-MEMBERSHIP-C/pages/vdps_p2637.png` | 290342 | `07356a233e946cb2a78678950aab34383fa02716391a2de3ad545fb3fa0ae8c3` | third-party | **no row** | redistribution permission **NOT CHECKED** |
| `CT-S16-MEMBERSHIP-C/pages/vdps_p2638.png` | 353044 | `4015bd1255fee38b030034274a74700df37ba9a7a0ff881fda640b6e76a085f9` | third-party | **no row** | redistribution permission **NOT CHECKED** |
| `CT-S16-MEMBERSHIP-C/pages/vdps_p2639.png` | 277779 | `9e240fa48d47d487ed9bc329c47c60c1d2a61e3a8756ae2ce55840539351f02b` | third-party | **no row** | redistribution permission **NOT CHECKED** |
| `CT-S16-MEMBERSHIP-C/pages/vdps_p2651.png` | 378511 | `60911c95cfafc201378b4480857628f10e433eab14040c9ea6ead6505ac78f05` | third-party | **no row** | redistribution permission **NOT CHECKED** |
| `CT-S16-MEMBERSHIP-C/pages/vdps_p2654.png` | 182136 | `10d85bd285c53ebe11f84b78438bfad9e8689e9cf646e9c7465545e1ab9e457b` | third-party | **no row** | redistribution permission **NOT CHECKED** |
| `CT-S16-MEMBERSHIP-C/pages/vdps_p2655.png` | 251192 | `39adb22ade511808ae5114f895c954f438f483fd90178b338dedb07bdbede663` | third-party | **no row** | redistribution permission **NOT CHECKED** |
| `CT-S16-MEMBERSHIP-C/pages/vdps_p2655_bz.png` | 118690 | `25f45755944bcd61929c4c9859bbd765fed798e0e357966a1095a48bd15deca5` | third-party | **no row** | redistribution permission **NOT CHECKED** |
| `CT-S16-MEMBERSHIP-C/pages/vdps_p2656.png` | 209454 | `13f543394daaa84b2a5a55c96155c0fa1c210c9d779114ca1b54dbd9b9a5bff6` | third-party | **no row** | redistribution permission **NOT CHECKED** |
| `CT-S16-MEMBERSHIP-C/pages/vdps_p2656_HV.png` | 234932 | `fb09f759647ed28244ac5055be85b9899d72a41fff526cca8900ec583fd5eaef` | third-party | **no row** | redistribution permission **NOT CHECKED** |
| `CT-S16-MEMBERSHIP-C/pages/vdps_titlepage_LOOK.png` | 112042 | `07de04c18e26d472c3d88145686239696b839376139296b07c90ee7e43760eaa` | third-party | **no row** | redistribution permission **NOT CHECKED** |
| `CT-S16-MEMBERSHIP-C/pages/vdps_titlepage_vol_LOOK.png` | 126825 | `32dfb794e1c5c4e4c3de194727d945abd5055f8d559e85b201566cf023b4f2a0` | third-party | yes | redistribution permission **NOT CHECKED** |
| `CT-S16-MEMBERSHIP-C/refs/vdPS-arXiv-0902.1702v5.pdf` | 536955 | `1d4be8e4526f6ca834506a976a6ffc999e9659acc2da08753b87e1f59d006e47` | third-party | yes | redistribution permission **NOT CHECKED** |
| `CT-S18-COLDREAD-C3/packet/pages/companion_v12_p2.png` | 680111 | `ff72fcacfe49d1ddc2d99690f2bba12e99b4fa0155f9e756b12f0b69fa9b641b` | operator's own | yes | operator's own deposit; deposit licence field **NOT CHECKED** |
| `CT-S18-COLDREAD-C3/packet/pages/companion_v12_p5.png` | 555635 | `725d3d8cad9e9a04af2bc0c0e3205b15d3c97e056bd4b6b269d32175b8421ecb` | operator's own | yes | operator's own deposit; deposit licence field **NOT CHECKED** |
| `CT-S18-COLDREAD-C3/packet/pages/companion_v12_p6.png` | 760460 | `82ab083680d31121fcf5a73364cb887a6c71edb628966d67bda1b6a346a5d6cb` | operator's own | yes | operator's own deposit; deposit licence field **NOT CHECKED** |
| `CT-S18-COLDREAD-C3/packet/pages/vdPS_p2634.png` | 512973 | `346bc9edeccf959785601e001d1ca31889c745736b85cc5e642f1d5af3499a14` | third-party | yes | redistribution permission **NOT CHECKED** |
| `CT-S18-COLDREAD-C3/packet/pages/vdPS_p2635.png` | 398195 | `ee55119f1d6936db5d11f82a2e4a8edbead0013ce1128ef4b8abfae8a72e5bd2` | third-party | yes | redistribution permission **NOT CHECKED** |
| `CT-S18-COLDREAD-C3/packet/pages/vdPS_p2636.png` | 259943 | `0ec031e95943324dff7c3ff0a750a40406c48c6a448c591756e9ffa072df72d1` | third-party | yes | redistribution permission **NOT CHECKED** |
| `CT-S18-COLDREAD-C3/packet/pages/vdPS_p2637.png` | 411631 | `e62876c658f7e9f5b3fe11f7cf6f84a103e3434fb6211a6aebf069863179b673` | third-party | yes | redistribution permission **NOT CHECKED** |
| `CT-S18-COLDREAD-C3/packet/pages/vdPS_p2655.png` | 353708 | `efcd4d792befac8e6c131b240f00272e9bef6c479a94ec7ebede623501fafca2` | third-party | yes | redistribution permission **NOT CHECKED** |
| `CT-S19-COLDREAD-MEMBERSHIP/packet/pages/companion_v12_p2.png` | 680111 | `ff72fcacfe49d1ddc2d99690f2bba12e99b4fa0155f9e756b12f0b69fa9b641b` | operator's own | yes | operator's own deposit; deposit licence field **NOT CHECKED** |
| `CT-S19-COLDREAD-MEMBERSHIP/packet/pages/companion_v12_p5.png` | 555635 | `725d3d8cad9e9a04af2bc0c0e3205b15d3c97e056bd4b6b269d32175b8421ecb` | operator's own | yes | operator's own deposit; deposit licence field **NOT CHECKED** |
| `CT-S19-COLDREAD-MEMBERSHIP/packet/pages/companion_v12_p6.png` | 760460 | `82ab083680d31121fcf5a73364cb887a6c71edb628966d67bda1b6a346a5d6cb` | operator's own | yes | operator's own deposit; deposit licence field **NOT CHECKED** |
| `CT-S19-COLDREAD-MEMBERSHIP/packet/pages/vdPS_p2634.png` | 512973 | `346bc9edeccf959785601e001d1ca31889c745736b85cc5e642f1d5af3499a14` | third-party | yes | redistribution permission **NOT CHECKED** |
| `CT-S19-COLDREAD-MEMBERSHIP/packet/pages/vdPS_p2635.png` | 398195 | `ee55119f1d6936db5d11f82a2e4a8edbead0013ce1128ef4b8abfae8a72e5bd2` | third-party | yes | redistribution permission **NOT CHECKED** |
| `CT-S19-COLDREAD-MEMBERSHIP/packet/pages/vdPS_p2636.png` | 259943 | `0ec031e95943324dff7c3ff0a750a40406c48c6a448c591756e9ffa072df72d1` | third-party | yes | redistribution permission **NOT CHECKED** |
| `CT-S19-COLDREAD-MEMBERSHIP/packet/pages/vdPS_p2637.png` | 411631 | `e62876c658f7e9f5b3fe11f7cf6f84a103e3434fb6211a6aebf069863179b673` | third-party | yes | redistribution permission **NOT CHECKED** |
| `CT-S19-COLDREAD-MEMBERSHIP/packet/pages/vdPS_p2654.png` | 263325 | `0393167af585813a5d618434e30dc6f4c60a750cb73b5144efd63a954ee8b58e` | third-party | yes | redistribution permission **NOT CHECKED** |
| `CT-S19-COLDREAD-MEMBERSHIP/packet/pages/vdPS_p2655.png` | 353708 | `efcd4d792befac8e6c131b240f00272e9bef6c479a94ec7ebede623501fafca2` | third-party | yes | redistribution permission **NOT CHECKED** |
| `CT-S19-COLDREAD-MEMBERSHIP/packet/pages/vdPS_p2656.png` | 302891 | `ae165007dfb5ebf98f4d9482195073e8bb26b951e4d00c7a002d77faf8a8a128` | third-party | yes | redistribution permission **NOT CHECKED** |
| `CT-S8-LITCHECK/refs/bt1933.pdf` | 3411000 | `dcd7e3c6b2a12ae1ce917d322763ff9dde5ec69ab5f23080d043699822d68fe6` | third-party | **no row** | redistribution permission **NOT CHECKED** |
| `CT-S8-LITCHECK/refs/bt1933.txt` | 139026 | `63595af76698ff2389945f29ebadb1bd0bc8bb273a200042aa5c28c549a54368` | third-party | **no row** | redistribution permission **NOT CHECKED** |
| `CT-S8-LITCHECK/refs/dlmf_2_9.html` | 115078 | `ee9d443f560c33e209cd46cd93c2005c3083f50f91f62c1abbf70c879a05a8ea` | third-party | **no row** | redistribution permission **NOT CHECKED** |
| `CT-S8-LITCHECK/refs/dlmf_2_9.txt` | 11524 | `72d6a344c2d04dc3564d95212091c40f1258f2369ec5062cc29daa6dc2c44f42` | third-party | **no row** | redistribution permission **NOT CHECKED** |
| `CT-S8-LITCHECK/refs/dlmf_3_6.html` | 195226 | `354c39b7e7d7b943df83169a7f225a012fa8518fb6094b866525c4ed4495c14b` | third-party | **no row** | redistribution permission **NOT CHECKED** |
| `CT-S8-LITCHECK/refs/dlmf_3_6.txt` | 21262 | `f6e2559307f5ac5fe7f9c909c5c71a95cdd986bd0b843e74843fc1c773a3dc86` | third-party | **no row** | redistribution permission **NOT CHECKED** |
| `CT-S8-LITCHECK/refs/g1967_p35_mid.png` | 142574 | `e8389dab5af6abbcdee993b8d899d3bf7d266c563d2dd2b9a9a5642ecc74e049` | third-party | **no row** | redistribution permission **NOT CHECKED** |
| `CT-S8-LITCHECK/refs/g_p58_bot.png` | 192674 | `eac04bac6a13e77bb4572978fa6ba82a8a9a6ee411fd8f14feb98d11278c8255` | third-party | **no row** | redistribution permission **NOT CHECKED** |
| `CT-S8-LITCHECK/refs/g_p58_top.png` | 191265 | `fb88dfba029409ca4a220bcf350e04a7d5b468ecdb6cecaa53fff014fbf7f5e1` | third-party | **no row** | redistribution permission **NOT CHECKED** |
| `CT-S8-LITCHECK/refs/gautschi1967.pdf` | 4970327 | `47ed9dffc00a52b7cfb7f3943d7ba3f2a3d398284ec6a00926ced315ec1c5173` | third-party | **no row** | redistribution permission **NOT CHECKED** |
| `CT-S8-LITCHECK/refs/gautschi1967.txt` | 103355 | `24233f36fd1b5ed9b2ec3bdd897062afe183e548b2441a1bcf8f6fe7f55191d7` | third-party | **no row** | redistribution permission **NOT CHECKED** |
| `CT-S8-LITCHECK/refs/nemes2025.pdf` | 618289 | `7f848c5bc15a792559442176477d609a861d9cf78b2f37d158a265c0d5511145` | third-party | **no row** | redistribution permission **NOT CHECKED** |
| `CT-S8-LITCHECK/refs/nemes2025.txt` | 96407 | `62a650030c3d2791b3de83ab888240e5af67e804ef62b5c12bde691b854d0a36` | third-party | **no row** | redistribution permission **NOT CHECKED** |
| `CT-S8-LITCHECK/refs/p1913_4.png` | 781945 | `cdefa1e3ba37e2e551cd7efab939a5b32054d33d71aaf1052de0f06c3d9ab19f` | third-party | **no row** | redistribution permission **NOT CHECKED** |
| `CT-S8-LITCHECK/refs/p1913_title.png` | 127371 | `83db3922a0315103653663d9a622ccb45a7e3578365591bfa4edcea30dbc747b` | third-party | **no row** | redistribution permission **NOT CHECKED** |
| `CT-S8-LITCHECK/refs/perron1913.pdf` | 13015509 | `dd8dbb5a15b83c9794976cf882dcbecb527111f61880b50796562f0cf4d9b809` | third-party | **no row** | redistribution permission **NOT CHECKED** |
| `CT-S8-LITCHECK/refs/perron1913.txt` | 13197 | `20ddb3629b479127779d12d511c4867fd5e8c1e6eb9811b7b657c749c043b9a5` | third-party | **no row** | redistribution permission **NOT CHECKED** |
| `CT-S8-LITCHECK/refs/polycf.pdf` | 207704 | `6a05e08c64c2f3d0b86d9e3e5c2e08a1ea0032ae47337bbd23dd135bee9a8f80` | third-party | **no row** | redistribution permission **NOT CHECKED** |
| `CT-S8-LITCHECK/refs/polycf.txt` | 36168 | `5ba9185392a926a125e04457aea528fd42b71aa55263feb90de31f5b380cc9e3` | third-party | **no row** | redistribution permission **NOT CHECKED** |
| `CT-S8-LITCHECK/refs/wang_jat2014.pdf` | 268982 | `1dca5c9a7d1f880c19f9854926ff78fdc85e3a30bc61ceb8c48f40b189517626` | third-party | **no row** | redistribution permission **NOT CHECKED** |
| `CT-S8-LITCHECK/refs/wang_jat2014.txt` | 38887 | `f6433d59a4da99edc6ee47c2d57c55d1df19a8c2d7bdfffa2870e56e0f0ea2be` | third-party | **no row** | redistribution permission **NOT CHECKED** |
| `CT-S9-PVPARAMS/refs/B02_003.pdf` | 675298 | `2f8efc754f4bcd9e4fb12cd53f8f92f72af9d2d027858602e25a9c7709599aa6` | third-party | **no row** | redistribution permission **NOT CHECKED** |
| `CT-S9-PVPARAMS/refs/DLMF_32.2.E5.tex` | 291 | `613250e4ac93f60736348bbe063d535d3e3e790d7f7689e885483e043ed4943f` | third-party | **no row** | redistribution permission **NOT CHECKED** |
| `CT-S9-PVPARAMS/refs/DLMF_32.4.html` | 99731 | `14142eab5790e69b765ecfe19aed3bea014b3c8e66989e9d29121cf0af57fceb` | third-party | **no row** | redistribution permission **NOT CHECKED** |
| `CT-S9-PVPARAMS/refs/jimbo_1982_prims.pdf` | 1623475 | `255d4f079767fb050cb462dc91204afaf09507bba74789ade1da10dce4f18815` | third-party | **no row** | redistribution permission **NOT CHECKED** |

## Finding: the inventory was incomplete

The standing hold reads *"everything under any `refs/` directory"*, so the
files below **are** covered by it. But the review's inventory table has no
row for any of them, so nothing had ever been enumerated or hashed:

- `CT-S16-MEMBERSHIP-C/pages/arxiv_v5_p34_B1_LOOK.png`
- `CT-S16-MEMBERSHIP-C/pages/arxiv_v5_p34_bz_LOOK.png`
- `CT-S16-MEMBERSHIP-C/pages/vdps_j2655_B1_LOOK.png`
- `CT-S16-MEMBERSHIP-C/pages/vdps_j2655_B1_top_LOOK.png`
- `CT-S16-MEMBERSHIP-C/pages/vdps_j2655_bz_LOOK.png`
- `CT-S16-MEMBERSHIP-C/pages/vdps_p2637.png`
- `CT-S16-MEMBERSHIP-C/pages/vdps_p2638.png`
- `CT-S16-MEMBERSHIP-C/pages/vdps_p2639.png`
- `CT-S16-MEMBERSHIP-C/pages/vdps_p2651.png`
- `CT-S16-MEMBERSHIP-C/pages/vdps_p2654.png`
- `CT-S16-MEMBERSHIP-C/pages/vdps_p2655.png`
- `CT-S16-MEMBERSHIP-C/pages/vdps_p2655_bz.png`
- `CT-S16-MEMBERSHIP-C/pages/vdps_p2656.png`
- `CT-S16-MEMBERSHIP-C/pages/vdps_p2656_HV.png`
- `CT-S16-MEMBERSHIP-C/pages/vdps_titlepage_LOOK.png`
- `CT-S8-LITCHECK/refs/bt1933.pdf`
- `CT-S8-LITCHECK/refs/bt1933.txt`
- `CT-S8-LITCHECK/refs/dlmf_2_9.html`
- `CT-S8-LITCHECK/refs/dlmf_2_9.txt`
- `CT-S8-LITCHECK/refs/dlmf_3_6.html`
- `CT-S8-LITCHECK/refs/dlmf_3_6.txt`
- `CT-S8-LITCHECK/refs/g1967_p35_mid.png`
- `CT-S8-LITCHECK/refs/g_p58_bot.png`
- `CT-S8-LITCHECK/refs/g_p58_top.png`
- `CT-S8-LITCHECK/refs/gautschi1967.pdf`
- `CT-S8-LITCHECK/refs/gautschi1967.txt`
- `CT-S8-LITCHECK/refs/nemes2025.pdf`
- `CT-S8-LITCHECK/refs/nemes2025.txt`
- `CT-S8-LITCHECK/refs/p1913_4.png`
- `CT-S8-LITCHECK/refs/p1913_title.png`
- `CT-S8-LITCHECK/refs/perron1913.pdf`
- `CT-S8-LITCHECK/refs/perron1913.txt`
- `CT-S8-LITCHECK/refs/polycf.pdf`
- `CT-S8-LITCHECK/refs/polycf.txt`
- `CT-S8-LITCHECK/refs/wang_jat2014.pdf`
- `CT-S8-LITCHECK/refs/wang_jat2014.txt`
- `CT-S9-PVPARAMS/refs/B02_003.pdf`
- `CT-S9-PVPARAMS/refs/DLMF_32.2.E5.tex`
- `CT-S9-PVPARAMS/refs/DLMF_32.4.html`
- `CT-S9-PVPARAMS/refs/jimbo_1982_prims.pdf`

That is 40 third-party files, among them complete third-party articles
rather than page regions. The hold's wording covered them; the inventory did
not. Wording is not a mechanism — this is the same lesson as the `.gitignore`
above, one level up.

## Counts

- 69 files total under `refs/` or `pages/`
- 9 operator's own deposits or renders of them
- 1 session-produced scripts (kept in the commit by an explicit negation)
- 59 third-party files with **no** licence determination

## Rule

No row here moves from **NOT CHECKED** except by reading the licence on the
item itself — the article's own title page, or the arXiv abstract page for
that submission, or the Zenodo record's `metadata.rights`. The status of a
publisher, a venue, or a neighbouring row clears nothing.


## CT-S21 deposit-day pass - re-fetch, 2026-09-18

Every external source the v1.3 notice cites was re-fetched on this date to a
temp directory **outside the repository**: a re-fetch is a verification, not an
acquisition, and copying more third-party bytes into the tree would enlarge the
population under the licence hold.

| source | URL | retrieved | bytes | sha256 | matches local copy |
|---|---|---|---|---|---|
| van der Put & Saito, Ann. Inst. Fourier 59 (2009) 7, 2611-2667 | `https://aif.centre-mersenne.org/item/AIF_2009__59_7_2611_0.pdf` | 2026-09-18 | 1058380 | `1666bd6be824a99fc0b48adbe48233a9b2a520fd7e8adf187e98d22525473605` | **yes, byte-identical** |
| arXiv:0902.1702v5, p. 34 | `https://arxiv.org/pdf/0902.1702v5` | 2026-09-18 | 536955 | `1d4be8e4526f6ca834506a976a6ffc999e9659acc2da08753b87e1f59d006e47` | **yes, byte-identical** |
| Jimbo, Publ. RIMS 18 (1982), p. 1152 | `https://ems.press/doi/pdf/10.2977/prims/1195183300` | 2026-09-18 | 1623475 | `255d4f079767fb050cb462dc91204afaf09507bba74789ade1da10dce4f18815` | **yes, byte-identical** |
| V_quad companion v1.2 (Zenodo) | `https://zenodo.org/api/records/20481592` | 2026-09-18 | 10877 | `666c955e78c7e9e83e51b80152fdf12b4c63b2d9bd4306163252ebf8105109e4` | no |
| DLMF section 32.2 (PV normalisation cited by v1.2) | `https://dlmf.nist.gov/32.2` | 2026-09-18 | 268803 | `8daba4033293b9fc1fc7d3f7133d3ed57f5e0a6e7595cddb1ce98a574585d84c` | n/a |

### Companion v1.2 - the record, not just the file

| field | value |
|---|---|
| record id | `20481592` |
| **version** DOI | `10.5281/zenodo.20481592` |
| **concept** DOI | `10.5281/zenodo.20455089` |
| `metadata.version` | `1.2` |
| publication date | 2026-06-01 |
| file | `vquad_resurgence.pdf`, 612719 bytes |
| Zenodo checksum | `md5:4d1e4d59072cad0db8edc86280af45a1` |
| local md5 | `4d1e4d59072cad0db8edc86280af45a1` |
| PDF re-fetched | `https://zenodo.org/api/records/20481592/files/vquad_resurgence.pdf/content` |
| PDF sha256 | `a5d9e264699e6397030f0512e17f0cd503fcf2eafd57db9b00b57523fcc88d85` |
| **byte-identical to the local copy** | **True** |

The concept DOI is **not** the version DOI and the two differ here. Any citation
of the exact text the notice corrects must use the **version** DOI
`10.5281/zenodo.20481592`; the concept DOI resolves to whatever is newest.

### DLMF - a URL is not a citation

| field | value |
|---|---|
| section | https://dlmf.nist.gov/32.2 |
| page title | DLMF: §32.2 Differential Equations ‣ Properties ‣ Chapter 32 Painlevé Transcendents |
| **version** | **Version 1.2.8** |
| **release date** | **2026-09-15** |
| sha256 of the page as served | `8daba4033293b9fc1fc7d3f7133d3ed57f5e0a6e7595cddb1ce98a574585d84c` |

v1.2 cites DLMF **section 32.2** and, for the PV->PIII degeneration, **32.2(vi),
Eq. 32.2.33**; both were read on the page image of v1.2 p. 6. The DLMF is a
living document, so the version and release date above must travel with the
citation.

### Licences - as printed on the source, or NOT CHECKED

| target | source read | licence as printed |
|---|---|---|
| companion v1.0 (zenodo 20455090) | `https://zenodo.org/api/records/20455090` | cc-by-4.0 |
| companion v1.1 (zenodo 20480603) | `https://zenodo.org/api/records/20480603` | cc-by-4.0 |
| companion v1.2 (zenodo 20481592) | `https://zenodo.org/api/records/20481592` | cc-by-4.0 |
| CT-S16-MEMBERSHIP-C/refs/vdPS-arXiv-0902.1702v5.pdf | `https://arxiv.org/abs/0902.1702` | http://arxiv.org/licenses/nonexclusive-distrib/1.0/ |
| CT-S9-PVPARAMS/refs/jimbo_1982_prims.pdf | `https://ems.press/journals/prims/articles/1195183300` | NOT CHECKED |
| CT-R1-AUDIT/refs/vanderPut-Saito-AIF-2009-59-7-2611.pdf | `https://aif.centre-mersenne.org/item/AIF_2009__59_7_2611_0/` | NOT CHECKED - no CC licence string on the item page |
| DLMF sections 32.2 / 2.9 / 3.6 / 5.11 (html, tex) | `https://dlmf.nist.gov/about/notices` | see quote - NIST notices page, verbatim |

**The arXiv row is the consequential one.** The abstract page for
`arXiv:0902.1702` carries `http://arxiv.org/licenses/nonexclusive-distrib/1.0/`
- arXiv's **default** licence, which grants arXiv the right to distribute and
grants third parties **no redistribution right at all**. The arXiv PDF therefore
may not be committed or deposited. Quoting from it is a separate question that
this row does not decide.

**Not cleared, and not guessed:** the Annales de l'Institut Fourier item page
carries no Creative Commons string, and the journal PDF title page prints
*tous droits reserves*; the EMS Press article page for Jimbo could not be read
(HTTP failure), so that row stays **NOT CHECKED**. Every other row of the
69-file census above is untouched by this pass and remains **NOT CHECKED**.


### CT-S21 addendum - two CC-BY references acquired for v1.7

Acquired 2026-09-18. Both carry **CC-BY-4.0 as printed on the arXiv abstract
page**, which grants a redistribution right - unlike arXiv:0902.1702, whose
default `nonexclusive-distrib/1.0` licence grants none. These two are therefore
the first third-party files in `refs/` cleared for redistribution on evidence.
The blanket media exclusion still applies until the operator re-admits them by
name; the licence is recorded here so that decision rests on evidence.

**Provenance and version-pinning of these two licence strings.** The licence was
read **from the arXiv abstract page, not from the PDF**. arXiv licences are
per-submission **and per-version**, so a bare "CC-BY-4.0" is not a determination
about any particular file. Each PDF's version was therefore taken from the
arXiv stamp printed in the margin of its own page 1 - i.e. from the bytes on
disk, not from an API answer about the current version - and the licence was
then re-read from the **versioned** abstract page:

| file version, per its own page-1 stamp | versioned abstract page read | licence as printed |
|---|---|---|
| `arXiv:2204.09305v1 [math.CA] 20 Apr 2022` | `https://arxiv.org/abs/2204.09305v1` | `http://creativecommons.org/licenses/by/4.0/` |
| `arXiv:2306.05930v2 [cs.SC] 3 Nov 2023` | `https://arxiv.org/abs/2306.05930v2` | `http://creativecommons.org/licenses/by/4.0/` |

Saved at `CT-S21-DEPOSIT-PREP/outputs/abs_2204.09305v1.html` and
`abs_2306.05930v2.html`. Both agree with the unversioned page, so the earlier
reading stands - but it now stands **for the versions actually held**, which is
what the per-version rule requires. A later version of either paper may carry a
different licence and would need re-checking before redistribution.

| file | source | licence | bytes | sha256 |
|---|---|---|---|---|
| `CT-R1-AUDIT/refs/wong_zhao_2022_recent_advances_arxiv-2204.09305.pdf` | `https://arxiv.org/pdf/2204.09305` | **http://creativecommons.org/licenses/by/4.0/** | 464879 | `123ab322619c723c26f3669b248f3986c731a1969c8265d88ad65d4fddc1a50b` |
| `CT-R1-AUDIT/refs/ibrahim_salvy_2023_positivity_certificates_arxiv-2306.05930.pdf` | `https://arxiv.org/pdf/2306.05930` | **http://creativecommons.org/licenses/by/4.0/** | 720492 | `36e9d025c89b6fa042e99888513f6554a43956eb247f0e25643efec1567be627` |

| arXiv | citation |
|---|---|
| `2204.09305` | R. Wong; Yu-Qiu Zhao. *Recent Advances in Asymptotic Analysis*. Anal. Appl., 20 (2022) 1103--1146. DOI `10.1142/S0219530522400012` |
| `2306.05930` | Alaa Ibrahim; Bruno Salvy. *Positivity certificates for linear recurrences*. Proceedings of the 2024 Annual ACM-SIAM Symposium on Discrete Algorithms (SODA), 2024. DOI `10.1137/1.9781611977912.37` |

**Purchase target, citation confirmed today by DOI content negotiation:**
R. Wong and H. Li, *Asymptotic Expansions for Second-Order Linear Difference
Equations, II*, **Stud. Appl. Math. 87(4) (1992), 289-324**, DOI
`10.1002/sapm1992874289`, issued 1992-11. This matches the citation table in
`P0-CITATION-RULE.md` exactly, including the "II" and the word "linear" whose
omission was the trap recorded at `R1-61`.

---

## Own deposit: companion v1.3 (published 2026-09-18, retrieved 2026-09-18T23:16:42+09:00)

Version DOI `10.5281/zenodo.22831933` · record `22831933` · concept DOI `10.5281/zenodo.20455089`.
This is the deposit's own CC-BY work, not a third-party reference: it is
redistributable, unlike the paywalled and all-rights-reserved entries above.
Sizes and sha256 are of the local copies in
`CT-S21-DEPOSIT-PREP/upload/`, each verified equal in size and md5 to the
published file entry of the same key.

| file | source | licence | bytes | sha256 |
|---|---|---|---|---|
| `vquad_resurgence.pdf` | `https://zenodo.org/records/22831933` | **cc-by-4.0** | 612719 | `a5d9e264699e6397030f0512e17f0cd503fcf2eafd57db9b00b57523fcc88d85` |
| `vquad_resurgence_v1.3_correction_notice.md` | `https://zenodo.org/records/22831933` | **cc-by-4.0** | 35918 | `c936662f61be8625d69b7f8efce8a8684b33569c6a033e88f510a3050b89948c` |


## Wong & Li II: NOT OBTAINED (decided 2026-09-19)

The purchase target recorded above was **not purchased and not obtained**. The
article is paywalled (Wiley HTTP 403); no mirror was used. Its status in this
corpus is therefore fixed, and stated rather than left implicit:

> Whether the exponent formula `s = beta_{d-1}/beta_d + (d-1)/2` appears in
> R. Wong and H. Li, Asymptotic Expansions for Second-Order Linear Difference Equations, II, Stud. Appl. Math. 87(4) (1992), 289-324, DOI `10.1002/sapm1992874289`, was **NOT ESTABLISHED**: the article is paywalled
> (Wiley HTTP 403) and was not obtained. The contribution is stated relative to
> what was read.

| item | status |
|---|---|
| exponent `s` stated in Wong-Li II? | NOT ESTABLISHED - article not obtained |
| connection constant in closed form there? | NOT ESTABLISHED - article not obtained |
| exponent `s` derived independently here | yes, CT-S8-LITCHECK and CT-S2 |
| `r_infinity` framing depends on Wong-Li? | no - see AUDIT R35 |

The citation is retained in full, including the numeral **II** and the word
**linear**, because omitting either retrieves a different paper (`R1-61`). It
enters no `refs/` table: there is no file, so there is nothing to license.
