# Research notes: language popularity indices (collected 2026-09-11)

## TIOBE — September 2026 (via TechRepublic, 2026-09-07)
1. Python 17.76% (declining through 2026; peaked 26.98% Jul 2025)
2. C 10.28%
3. C++ 8.67%
4. Java 7.54%
5. C# 4.22%
6. JavaScript 2.76%
7. Visual Basic 2.55%
8. SQL 2.16%
9. R 1.69%
10. Rust 1.34% (3rd month in top 10 — first ever run)
11. Fortran 1.24%
20. COBOL; 21. Julia 0.74% (taking MATLAB share; MATLAB fell to #27)
Perl and Ruby dropped out of top 20 earlier in 2026; Ada and Objective-C re-entered.

## Stack Overflow Developer Survey 2025 (published Jul 29 2025; ~49k respondents)
Most used (all respondents): JavaScript 66%, HTML/CSS 61.9%, SQL 58.6%, Python 57.9%, Bash/Shell 48.7%, TypeScript ~43%, Java ~29%, C# ~27%
Python +7 pts YoY (largest jump in a decade).
Most admired: Rust 72%, Gleam 70%, Elixir 66%, Zig 64%
Most desired (want to work with next year): Python top; Go also strongly desired
Cargo most admired build tool (71%). FastAPI +5 pts YoY. Docker +17 pts YoY.
Redis +8%.

## GitHub Octoverse 2025 (Oct 28 2025)
- TypeScript #1 by contributors in Aug 2025 (overtook Python by ~42k contributors), +1.05M contributors, +66.6% YoY
- Python #2, 2.6M contributors, +48.8% YoY (AI/data science)
- JavaScript #3, 2.15M, +24.8%
- Java #4 +20.7%; C# #5 +22.2%; then PHP, Shell, C++, HCL, Go in top 10
- JS+TS combined still bigger than Python
- 180M+ developers; 36M joined in 2025; India +5.2M; 1.1M repos use an LLM SDK
- Top OSS projects by contributors: vllm, vscode, openai/codex, transformers, godot, home-assistant, ollama, llama.cpp, verl, expo
- Fastest growing: zen-browser, cline, vllm, uv (Rust-written Python tool), ...
- Thesis: typed languages favoured because AI-assisted coding is more reliable with types

## IEEE Spectrum Top Programming Languages 2025 (Sep 23 2025)
- Spectrum ranking: Python #1; JavaScript dropped from #3 to #6
- Jobs ranking: Python #1 (up from #2), SQL remains extremely valuable
- Stack Exchange questions in 2025 were only 22% of 2024 volume (AI effect) — public signals weakening
- Essay thesis: AI reduces importance of language choice; LLMs weaker in low-data languages -> harder for new languages to emerge

## JetBrains State of Developer Ecosystem 2025 (Oct 15 2025; 24,534 devs, 194 countries)
- Primary languages: Python 35%, Java 33%, JavaScript 26%, TypeScript 22%, HTML/CSS 16%
- Want to adopt next: Go 11%, Rust 10%, Python 7%, Kotlin 6%, TypeScript 5%
- 85% use AI tools regularly; 68% expect AI proficiency to become job requirement
- 61% of juniors find job market challenging vs 34% seniors
- AWS 43%, GCP 22%, Azure 22%
- TypeScript saw most dramatic migration gains (language migration analysis)

## Salary signals (mixed sources, US-centric; treat as directional)
- Aggregators (2026): Rust/Go/Scala/Erlang/Elixir/Clojure/Solidity cluster at top of median pay; niche + scarcity effect
- Go ~$147k median (one aggregator), TypeScript ~$132k, Python ~$126k US average
- SO salary-by-language historically: Erlang, Clojure, Elixir, F#, Rust, Scala, Go top; PHP, Dart, Java lower medians
- Caveat: language salary medians track *seniority of the typical user*, not the language itself
