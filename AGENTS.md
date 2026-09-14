# AGENTS.md

Personal course materials for the SJTU IEEE Honors Program. This is a collection, not an app: each top-level `CODE-Course-Name/` directory is self-contained (notes, assignments, exams, projects). There is no root build, test, lint, or CI setup.

## Repo conventions

- Folder format is `CODE-Course-Name`; an `H` suffix means honors. `README.md` has per-semester tables but is stale: `CS2602-Data-Structure` and `MATH1207-Probability-and-Statistics` are not listed.
- Keep content limited to personal work: no instructor slides, textbooks, or build artifacts (per README).
- `*.pdf` is gitignored, but many PDFs are already tracked (past exams, compiled reports). Do not delete them; `git add -f` only to intentionally update one. Newly compiled PDFs stay untracked.
- Many paths contain Chinese characters. The PowerShell console garbles them and `git ls-files` octal-escapes them (`core.quotepath`). Prefer the file tools; when shell is unavoidable, use `git -c core.quotepath=false`.

## LaTeX

- All `.tex` files need XeLaTeX (`ctex`/`xeCJK`/`unicode-math`), e.g. `latexmk -xelatex <file>.tex`; pdfLaTeX fails.
- `EST2501-Digital-Fundamentals/final_tex/` is the compilable Digital Circuits project; see its README. `assets/` must stay next to `Digital_Circuits.tex` (relative figure paths). `final/tex/digital_circuits_source/` is an older duplicate whose `README_compile.txt` says pdflatex; don't follow it.
- `PHY1251H-College-Physics/exp/2/`: `calc.py` writes `calc_results.json`, `plot.py` produces the fit figure, and `report.tex` `\lstinputlisting`s both scripts, so run them before compiling.

## Verifying code

- No unit tests. CS1604 assignments ship local graders that compile with `g++ -std=c++11` and diff against expected output under `data/`:
  - `python judger.py -T 1_length -I data/1_length/1.in -O <expected.out> -S .` from `assignment1/` (single input pair)
  - `python judger_batch.py -T 1_matrix` from `assignment5/` (defaults to `data/<task>/`, all five cases)
  - Expected `.out` files are not committed, so supply your own reference output.
- `MATH1409-Linear-Algebra-for-AI/program_solution/matlibrary.py` is the library documented in `program_solution/README.md`; `python_solution/` holds older per-homework copies of the same code.
