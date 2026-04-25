import Lake
open Lake DSL

package «GoldbachHelfgott» where

require mathlib from git
  "https://github.com/leanprover-community/mathlib4.git" @ "v4.30.0-rc1"

@[default_target]
lean_lib GoldbachHelfgott where
  roots := #[`GoldbachHelfgott.Basic, `GoldbachHelfgott.Statement,
             `GoldbachHelfgott.Reduction, `GoldbachHelfgott.Certificate,
             `GoldbachHelfgott.Main]
