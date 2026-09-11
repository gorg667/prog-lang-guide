# The Definitive Guide to Which Programming Language to Learn — For What (2026 Edition)

> **Last researched:** 11 September 2026
> **Scope:** 30+ languages, 30+ application domains, 8 learner profiles, and the data behind every recommendation.
> **How to read this:** If you have 5 minutes, read §0 (the decision table) and jump to your domain in Part III. If you have an hour, read Parts I–III. If you're making a multi-year career decision, read it all — that's what it's for.

---

## Table of Contents

- [§0 — The 60-second answer](#0--the-60-second-answer)
- [Part I — How to think about choosing a language](#part-i--how-to-think-about-choosing-a-language)
  - [1.1 The only question that matters](#11-the-only-question-that-matters)
  - [1.2 Seven myths that waste beginners' time](#12-seven-myths-that-waste-beginners-time)
  - [1.3 The AI factor: what changed in 2024–2026 and what didn't](#13-the-ai-factor-what-changed-in-20242026-and-what-didnt)
  - [1.4 A framework: the five axes of language choice](#14-a-framework-the-five-axes-of-language-choice)
  - [1.5 Learn the paradigm, not just the syntax](#15-learn-the-paradigm-not-just-the-syntax)
- [Part II — The 2026 data landscape](#part-ii--the-2026-data-landscape)
  - [2.1 The five big indices and what each actually measures](#21-the-five-big-indices-and-what-each-actually-measures)
  - [2.2 Cross-index scoreboard](#22-cross-index-scoreboard)
  - [2.3 Salary: what the numbers say and why they lie](#23-salary-what-the-numbers-say-and-why-they-lie)
  - [2.4 Momentum: who's rising, who's falling](#24-momentum-whos-rising-whos-falling)
  - [2.5 The junior-market problem](#25-the-junior-market-problem)
- [Part III — Domain-by-domain: what to learn for what](#part-iii--domain-by-domain-what-to-learn-for-what)
- [Part IV — Language profiles](#part-iv--language-profiles)
- [Part V — Roadmaps by learner profile](#part-v--roadmaps-by-learner-profile)
- [Part VI — Sequencing: your second, third, and fourth language](#part-vi--sequencing-your-second-third-and-fourth-language)
- [Part VII — How to actually learn a language in 2026](#part-vii--how-to-actually-learn-a-language-in-2026)
- [Part VIII — Anti-recommendations](#part-viii--anti-recommendations)
- [Part IX — FAQ](#part-ix--faq)
- [Appendix A — Sources & methodology](#appendix-a--sources--methodology)
- [Appendix B — Glossary](#appendix-b--glossary)

---

## §0 — The 60-second answer

If you refuse to read further, use this table. Each row gives the **default** choice — the one that will be right for the largest number of people — plus the strongest alternative and the one-sentence reason.

| I want to… | Learn this | Strong alternative | Why (one line) |
|---|---|---|---|
| **Just start programming, no specific goal** | **Python** | JavaScript/TypeScript | Gentlest syntax, biggest tutorial ecosystem, useful in the most domains; #1 on TIOBE, IEEE, and JetBrains. |
| **Get a job as fast as possible (web)** | **TypeScript** (+ React) | Python (+ FastAPI/Django) | Most job listings, most new repos on GitHub (#1 in Octoverse 2025), and it covers both frontend and backend. |
| **Build websites / web apps (frontend)** | **TypeScript** | — (JavaScript is a strict prerequisite, not an alternative) | The browser only runs JS; TS is what professionals write it in. Nearly every framework scaffolds in TS by default. |
| **Build backend APIs / services** | **TypeScript (Node/Bun)** or **Python** | Go, Java, C# | TS/Python for speed of delivery and hiring pool; Go for cloud-native infra; Java/C# for large enterprises. |
| **Do data analysis / data science** | **Python** | R (academia/statistics), SQL (mandatory anyway) | pandas/Polars/scikit-learn/PyTorch are the industry standard; 57.9% of all developers used Python in 2025. |
| **Do machine learning / AI / LLM apps** | **Python** | TypeScript (for AI product UIs), C++/CUDA/Mojo (for kernels) | PyTorch, Hugging Face, vLLM, LangChain — the entire AI stack is Python-first. |
| **Work with data at scale (data engineering)** | **SQL + Python** | Scala (legacy Spark shops), Rust (tool building) | SQL is 58.6% usage and the most-wanted job skill; Python drives orchestration (Airflow, dbt, Polars, DuckDB). |
| **Build iOS apps** | **Swift** | Kotlin Multiplatform, Dart/Flutter, TS/React Native | Apple's platform language; SwiftUI is the future of Apple UI. Swift 6.3 also officially targets Android. |
| **Build Android apps** | **Kotlin** | Java (legacy), Dart/Flutter | Google's recommended language; Jetpack Compose is Kotlin-only. Java for maintaining older apps. |
| **Build one app for iOS + Android** | **Dart (Flutter)** or **TypeScript (React Native)** | Kotlin Multiplatform | RN if you already know React; Flutter for pixel-identical UIs; KMP if you're a Kotlin team sharing logic. |
| **Build games (indie / hobby)** | **C# (Unity or Godot)** | GDScript (Godot), Lua (Love2D/Roblox/Defold) | Unity ships the most games by volume; C# is transferable to enterprise work if gamedev doesn't pan out. |
| **Build games (AAA / engine work)** | **C++** | Rust (niche), C# | Unreal Engine and every AAA engine is C++; ~42% of AA/AAA studios use Unreal (GDC 2026). |
| **Do systems programming (OS, drivers, DBs, browsers)** | **Rust** | C, C++, Zig | Now in the Linux and Windows kernels; 48.8% of orgs make non-trivial use (State of Rust 2025); memory-safety mandates from CISA/NSA. You still need to *read* C. |
| **Do embedded / firmware / IoT** | **C** | C++, Rust (rising), MicroPython (prototyping) | C is still ~universal on microcontrollers and in vendor SDKs. Rust is the growth edge. |
| **Do DevOps / cloud / platform / SRE** | **Go** + **Bash** + **Python** | HCL (Terraform), YAML literacy | Kubernetes, Docker, Terraform, Prometheus — the cloud-native stack is written in Go; Go is the #1 "want to adopt" language (JetBrains 2025). |
| **Do cybersecurity / pentesting / reverse engineering** | **Python** + **C** | Bash, Go, Assembly (x86-64/ARM), Rust | Python for tooling and exploits; C to understand what you're exploiting; Go for red-team implants. |
| **Work in a large enterprise / bank / insurer** | **Java** | C#, Kotlin, SQL | Java is the #2 primary language worldwide (JetBrains 2025, 33%) and dominates Fortune 500 backends; JDK 25 LTS shipped Sep 2025. |
| **Work in the Microsoft ecosystem / .NET shops** | **C#** | F#, TypeScript | TIOBE Language of the Year 2025; .NET 10 LTS; spans web, desktop, cloud, and Unity games. |
| **Do quantitative finance / HFT** | **C++** + **Python** | Rust, OCaml (Jane Street), Java, KDB/q | Python for research, C++ for the execution path. |
| **Do scientific computing / HPC / simulation** | **Python** (+NumPy/JAX) | Julia, Fortran (legacy), C++ | Julia is rising (TIOBE #21, eating MATLAB's share) but Python's ecosystem is unmatched. |
| **Program GPUs / write AI kernels** | **C++ (CUDA)** | Triton (Python), Mojo, Rust (wgpu) | CUDA C++ is the incumbent; Mojo 1.0 went open-source (Aug 2026) and is the most interesting challenger. |
| **Write smart contracts / blockchain** | **Solidity** | Rust (Solana, Polkadot, Near), Move (Aptos/Sui) | Ethereum/EVM dominates deployed value; Rust dominates non-EVM chains. |
| **Automate my job (non-programmer)** | **Python** | Google Apps Script (JS), PowerShell, Excel/VBA | Python scripts + AI assistants solve 90% of office automation. |
| **Build desktop apps** | **C#** (Windows), **Swift** (macOS), **TypeScript** (cross-platform via Electron/Tauri) | Rust (Tauri backend), C++ (Qt), Kotlin/Java (JVM), Dart (Flutter) | Depends entirely on target OS; Electron/Tauri are how most cross-platform desktop apps ship today. |
| **Build CLI tools / developer tooling** | **Go** or **Rust** | Python, TypeScript | Single static binaries, fast startup; the 2025 breakout tools (uv, ruff, Zed, Ghostty) are Rust/Zig. |
| **Maintain legacy / mainframe systems** | **COBOL** + **JCL** + **SQL (DB2)** | Java (for modernization), PL/I, RPG | Real, steady demand; salary is solid (~$115–120k US median) but not the mythical goldmine. |
| **Understand how computers actually work** | **C** | Assembly (RISC-V or x86-64), Rust | C is the lingua franca of computing; everything else is built on it. |
| **Become a better programmer (not for a job)** | **A Lisp (Racket/Clojure), Haskell, or Rust** | OCaml, Elixir, Prolog, Smalltalk | Languages that force a new mental model make you better in every other language. |
| **Teach a child (8–12)** | **Scratch** → **Python** | Roblox Lua, MakeCode | Block-based first, then text; Python has the most kid-oriented material. |
| **Teach a teen (13–17)** | **Python** or **JavaScript** | Lua (Roblox), C# (Unity), Java (AP CS A) | Pick the one connected to something they already care about — games, websites, Discord bots. |

**The three-language "complete developer" set for 2026:** **Python + TypeScript + SQL.** Together these cover web frontend, web backend, data, AI, automation, and scripting, and they appear in more job postings than any other combination. Add **one** of Go / Rust / Java / C# / Kotlin / Swift depending on your domain and you're set for a decade.

---

## Part I — How to think about choosing a language

### 1.1 The only question that matters

"Which programming language should I learn?" is, on its own, unanswerable — it's like asking "which vehicle should I buy?" without saying whether you're commuting in Tokyo, hauling gravel, or racing at Le Mans.

The question that *has* an answer is:

> **"What do I want to build, for whom, in what environment, and what constraints do I have?"**

Every recommendation in this document flows from that framing. Languages are tools optimized for particular problems, teams, and runtimes. The "best" language is the one whose ecosystem is where your problem already lives.

A useful heuristic: **find the ten open-source projects or ten job postings closest to what you want to do, and count the languages.** Whatever appears most is your answer. Everything else in this guide is a shortcut to that exercise.

### 1.2 Seven myths that waste beginners' time

**Myth 1: "I need to pick the *right* language or I'll waste years."**
False. Your first language is the only one that takes real effort to learn. The second takes a fraction of the time, the third less still. Programming concepts — variables, control flow, functions, data structures, abstraction, debugging — transfer almost entirely. Pick something reasonable and *start*. The cost of a wrong first choice is measured in weeks, not years. The cost of indecision is measured in years.

**Myth 2: "Language X is dying."**
Almost never true in any useful time frame. COBOL was "dying" in 1990 and still runs the world's banks. Perl and Ruby left the TIOBE top 20 in 2026, yet Ruby on Rails still powers Shopify and GitHub, and Rails jobs pay well. PHP has been "dead" for fifteen years and runs ~75% of the server-side web (mostly WordPress). Languages decline in *mindshare* and *new-project share* long before they decline in *jobs*. What matters is whether the language is losing ground **in the specific domain you care about**.

**Myth 3: "The highest-paying language is the one to learn."**
Salary-by-language data mostly measures the **seniority of the typical developer using it**, not the language. Erlang, Clojure, Scala, F#, and Elixir top salary charts because almost nobody learns them as a first language — you only meet them after years of experience. Learning Clojure as a beginner does not get you a Clojure salary; it gets you a small pool of jobs that all require experience you don't have. See §2.3.

**Myth 4: "Fast languages are better."**
Raw runtime speed matters in maybe 10% of software. For the other 90% — CRUD apps, dashboards, automation, most data pipelines — the bottleneck is network, disk, or the database, and developer speed is worth far more than CPU speed. When performance *does* matter (game engines, trading, kernels, inference), you'll know, and this guide tells you what to use.

**Myth 5: "AI will make learning to code pointless."**
The evidence from 2025–2026 points the opposite way: more people are coding than ever (36 million new GitHub accounts in 2025, over one per second), AI-assisted developers merge more code, and the *demand for people who can judge whether generated code is correct* has gone up. What AI has changed is **which** skills matter — reading, reviewing, architecture, and testing are worth more; memorizing syntax is worth less. See §1.3.

**Myth 6: "Real programmers use C / Rust / Haskell / [insert hard language]."**
Gatekeeping. Real programmers ship software that people use. Most of the world's most valuable software is written in Java, Python, JavaScript, C#, and — yes — PHP. Learning a hard language *later* will make you a better programmer; learning it *first* mostly makes you quit.

**Myth 7: "I should learn a language, then decide what to build."**
Backwards. Pick something small you actually want to exist — a Discord bot, a budget tracker, a game, a data plot of your running times — and learn whatever language gets you there fastest. Motivation is the scarcest resource in learning to program; a real project is how you protect it.

### 1.3 The AI factor: what changed in 2024–2026 and what didn't

This is the first edition of a guide like this where AI coding assistance is not a footnote but a structural force. Here is what the data says.

**What changed:**

1. **Typed languages gained a structural advantage.** GitHub's Octoverse 2025 report attributes TypeScript's jump to #1 (overtaking both Python and JavaScript in August 2025, +66% contributors YoY) partly to AI: static types give agents and reviewers a fast, mechanical check on generated code. "Developers are shifting toward typed languages that make agent-assisted coding more reliable in production." Expect this to keep favoring TypeScript over JavaScript, Kotlin over Groovy, and to modestly help Rust, Go, Java, C#, and Swift.

2. **Popular languages got a compounding moat.** LLMs are trained on public code. A language with a huge corpus (Python, JS/TS, Java) gets excellent AI support; a language with a small one (Zig, Gleam, Nim, Odin) gets noticeably worse suggestions — hallucinated APIs, outdated idioms. IEEE Spectrum's 2025 analysis argues this makes it structurally harder for *new* languages to reach critical mass. For a learner, this means: **the mainstream choice is now even safer than it used to be.**

3. **Public Q&A signals collapsed.** Stack Exchange question volume in 2025 was ~22% of 2024's. People ask Claude/ChatGPT instead. This matters for you in two ways: (a) popularity indices built on those signals (TIOBE, PYPL, IEEE) are getting noisier; (b) the traditional "search Stack Overflow" learning loop has been partly replaced by conversational debugging — which is *better* for learners, but only if you learn to verify.

4. **Learning curves flattened — for languages with big corpora.** Matt Welsh's widely read 2026 "Revisiting Rust" essay is representative: Rust, notorious for its learning curve, became dramatically more approachable because a learner can ask "all the dumb questions" to an LLM instead of a coworker. The same applies to C++, Haskell, and other traditionally intimidating languages. **A hard language is now a medium-hard language if it's popular.**

5. **Rewrites became feasible.** In July 2026, Bun's creator ported ~535,000 lines of Zig to Rust in 11 days using 64 parallel Claude agents (~$165k in API cost). Whatever you think of the result (Zig's creator called it "unreviewed slop"), migrations that were economically impossible in 2023 are now a budget line. Long-term, this weakens lock-in and modestly *reduces* the stakes of language choice for organizations.

6. **Junior hiring got harder.** JetBrains 2025: 61% of junior developers find the job market challenging vs. 34% of seniors. AI has compressed demand for "translate this ticket into code" work, which was the traditional junior on-ramp. This raises the bar for what a first job requires — and makes *shipping real projects in a mainstream stack* more important than ever.

**What did *not* change:**

- **Someone still has to decide what to build and know when it's wrong.** The IEEE essay's provocative claim that languages will become "as obscure as railway gauges" is a long-range speculation; in 2026, humans still read, review, debug, and own the code. 72.6% of developers say AI code review improved their effectiveness — but they are still doing the review.
- **Domain ecosystems didn't move.** AI didn't make PyTorch run in Java or Unreal Engine accept Python. The domain → language mapping in Part III is essentially unchanged from what a well-informed person would have told you in 2023, with the edges (TypeScript up, Rust up, Zig down, Mojo now real) adjusted.
- **Fundamentals got *more* valuable.** Data structures, algorithms, systems knowledge, networking, databases, and testing are the skills that let you supervise an AI. Every reputable observer — from GitHub's own report to IEEE — concludes that CS fundamentals rise in value relative to syntax knowledge.

**Practical implications for choosing a language in 2026:**

- Prefer languages with large public corpora (better AI help): Python, JS/TS, Java, C#, C/C++, Go, Rust, Kotlin, Swift, PHP, Ruby, SQL.
- Prefer static types where the domain allows (TypeScript over JavaScript; type hints in Python; consider Kotlin/Go/Rust/C# for backends).
- Learn to *read* code and *test* code from day one — it's now the core skill.
- Don't pick an obscure language for your first job hunt; the AI tailwind goes to the mainstream.
- Do use an AI assistant to learn — but type the code yourself for the first few months. People who only paste never build the mental model.

### 1.4 A framework: the five axes of language choice

Rate any candidate language on these five axes for *your* situation. This is the rubric used throughout Part III.

| Axis | The question | Why it matters |
|---|---|---|
| **1. Domain fit** | Is the ecosystem for *my* problem already here (libraries, frameworks, tooling, community)? | This dominates everything else. A mediocre language with the right libraries beats a great language without them. |
| **2. Employability** | How many jobs, where, at what seniority, and is the trend up or down? | Determines how quickly you can get paid and how much choice you'll have. |
| **3. Learnability** | How long to first useful program? How good are the error messages, docs, and AI support? | Determines whether you'll actually finish learning it. |
| **4. Transferability** | What does learning this teach me that carries to other languages? | A first language should teach the most general concepts. |
| **5. Longevity & governance** | Who controls it? Is it stable? Is it still evolving? Would you bet a 10-year system on it? | Matters most for organizations and for people building deep specialization. |

Weights differ by person. A career switcher weights employability at 40%; a hobbyist building a game weights domain fit and learnability; a CTO weights longevity and hiring pool.

### 1.5 Learn the paradigm, not just the syntax

Languages cluster into families. Learning one member of a family makes the others cheap. Knowing this lets you plan a curriculum instead of collecting random languages.

| Family / paradigm | Members | What it teaches you |
|---|---|---|
| **C-family imperative/OOP** | C, C++, Java, C#, Kotlin, Swift, Go (partly), Dart, JavaScript/TypeScript (syntax), PHP | Curly-brace syntax, static typing, classes/interfaces, manual or GC memory. The industrial mainstream. |
| **Dynamic scripting** | Python, Ruby, JavaScript, PHP, Lua, Perl | Speed of iteration, duck typing, REPL-driven development, "batteries included." |
| **Systems / manual memory** | C, C++, Rust, Zig, Odin | How the machine works: pointers, stack vs. heap, layout, UB, ownership. |
| **Functional (typed)** | Haskell, OCaml, F#, Scala, Elm, Gleam, PureScript | Immutability, algebraic data types, pattern matching, type inference, purity. Makes you better at *everything*. |
| **Functional (dynamic) / Lisp** | Clojure, Racket, Scheme, Common Lisp, Elixir/Erlang (also actor-based) | Code-as-data, macros, REPL, homoiconicity; Erlang/Elixir add fault-tolerant concurrency (the actor model). |
| **Logic / constraint** | Prolog, Datalog, MiniZinc | Declarative problem specification; unification and search. |
| **Array / data languages** | R, Julia, MATLAB, APL/J/K/q, NumPy (as a sub-language) | Vectorized thinking; whole-array operations. |
| **Query / declarative** | SQL, GraphQL, Cypher, SPARQL | Set-based thinking; describing *what* rather than *how*. |
| **Shell / glue** | Bash, PowerShell, Nushell | Composing programs; the operating system as a programming environment. |
| **Hardware description** | Verilog, VHDL, SystemVerilog, Chisel | Describing circuits, not instructions; parallel-by-default. |

**The ideal long-term set** touches at least four families: one mainstream OOP/imperative language (for work), one dynamic scripting language (for speed), one systems language (to understand the machine), one functional language (to reshape how you think), plus SQL (because data). A person who knows Python, TypeScript, Rust, and one of Haskell/OCaml/Clojure — plus SQL — can learn anything else in a weekend.

---

## Part II — The 2026 data landscape

No single ranking tells the truth. Each index measures a different proxy, has a different bias, and is useful for a different question. The honest approach is to look at all of them and understand *why* they disagree.

### 2.1 The five big indices and what each actually measures

| Index | What it measures | Biased toward | Good for answering | Latest |
|---|---|---|---|---|
| **TIOBE** | Search-engine hit counts for `"<language> programming"` across ~25 engines | Old, widely documented languages; languages with lots of courses; over-represents C/VB/Fortran | "How much *total documentation and interest* exists?" Long-term trend lines. | Sep 2026 |
| **Stack Overflow Developer Survey** | ~49k self-selected developers' *usage* and *sentiment* ("admired", "desired") | Western, English-speaking, web-heavy professional developers; over-represents JS | "What do working developers actually use, and what do they *want* to use?" | Jul 2025 (2026 edition pending) |
| **GitHub Octoverse** | Contributor counts on public + private GitHub repos | Open-source and web/AI activity; under-represents enterprise Java/C#/COBOL behind firewalls | "Where is *new* code being written?" Momentum. | Oct 2025 |
| **JetBrains State of Developer Ecosystem** | ~24.5k developers, 194 countries; "primary language", "want to adopt" | Global (China 20%, US 13%, India 12%); JetBrains IDE users (Java/Kotlin/Python heavy) | "What's the *global* professional picture, including Asia?" Adoption intent. | Oct 2025 |
| **IEEE Spectrum Top Programming Languages** | Composite of 11 metrics from 8 sources, with a separate **Jobs** ranking | Engineering/academic (IEEE members); explicit jobs lens | "What do *employers* ask for?" | Sep 2025 |
| **PYPL** | Google Trends for "<language> tutorial" | Learners; what people are trying to *learn right now* | Beginner interest | Monthly |
| **RedMonk** | GitHub + Stack Overflow rank correlation | Open-source developer community | Long-run "tier" membership | Semi-annual |

**Key insight:** TIOBE says C is #2 and Rust barely cracked the top 10; GitHub says TypeScript is #1 and C isn't in the top 10; Stack Overflow says JavaScript is #1. **None of them is wrong.** They're measuring documentation volume, new-code activity, and working-developer usage respectively. For a *learner*, the most relevant signals are (1) job postings in your target domain, (2) Octoverse (where new code is written), and (3) the SO/JetBrains "want to use" numbers (where the profession is heading).

### 2.2 Cross-index scoreboard

Rankings as of the most recent edition of each source. "—" means outside the reported top list.

| Language | TIOBE Sep 2026 (share) | Octoverse 2025 (contributors) | SO 2025 (% used) | JetBrains 2025 (primary lang) | IEEE 2025 (Spectrum / Jobs) |
|---|---|---|---|---|---|
| **Python** | #1 (17.76%) | #2 (2.6M, +48.8%) | #4 (57.9%) | #1 (35%) | #1 / #1 |
| **C** | #2 (10.28%) | — | ~20% | mid | top 10 |
| **C++** | #3 (8.67%) | #8 | ~22% | mid | top 5 |
| **Java** | #4 (7.54%) | #4 (+20.7%) | ~29% | #2 (33%) | top 5 / top 3 |
| **C#** | #5 (4.22%) — *Language of the Year 2025* | #5 (+22.2%) | ~27% | mid | top 10 |
| **JavaScript** | #6 (2.76%) | #3 (2.15M, +24.8%) | **#1 (66%)** | #3 (26%) | #6 (was #3) / top 5 |
| **TypeScript** | ~#25-30 | **#1 (+1.05M, +66.6%)** | ~43% | #4 (22%) | top 10 |
| **SQL** | #8 (2.16%) | n/a (not a repo language) | #3 (58.6%) | (not asked as primary) | top 3 on Jobs |
| **Go** | ~#12 | #10 | ~14% | ~7% | top 10 |
| **Rust** | **#10 (1.34%)** — first-ever top-10 run | ~#12 | ~13% | ~4% | top 15 |
| **Kotlin** | ~#20 | ~#12 | ~10% | ~7% | top 15 |
| **Swift** | ~#22 | ~#15 | ~5% | ~3% | top 15 |
| **PHP** | ~#13 | #6 | ~18% | ~8% | top 15 |
| **Ruby** | left top 20 (2026) | ~#15 | ~5% | ~2% | top 20 |
| **R** | #9 (1.69%) | — | ~4% | ~2% | top 10 (Spectrum) |
| **Visual Basic** | #7 (2.55%) | — | ~3% | — | — |
| **Fortran** | #11 (1.24%) | — | <1% | — | — |
| **Dart** | ~#28 | ~#14 | ~6% | ~3% | — |
| **Scala** | ~#30 | ~#20 | ~2.5% | ~1% | — |
| **Julia** | #21 (0.74%) — rising, eating MATLAB | — | <1% | <1% | — |
| **COBOL** | #20 | — | <1% | — | — |
| **Zig** | — | — | ~1% | — | — |
| **Elixir** | — | — | ~2.5% | ~1% | — |

**Sentiment layer (the "would use again" and "want to learn" signals):**

| Metric | Top results |
|---|---|
| **SO 2025 "Most admired"** (used it, want to keep using it) | Rust 72%, Gleam 70%, Elixir 66%, Zig 64%, then Go, TypeScript, Python, Kotlin, Swift |
| **SO 2025 "Most desired"** (want to use next year) | Python, JavaScript, TypeScript, SQL, Go, Rust |
| **JetBrains 2025 "Plan to adopt next"** | Go 11%, Rust 10%, Python 7%, Kotlin 6%, TypeScript 5% |
| **JetBrains 2025 biggest migration gains** | TypeScript (most dramatic), Python, Go |
| **SO 2025 most admired build tool** | Cargo (Rust) 71% |
| **SO 2025 most admired web framework** | Phoenix (Elixir), 3rd year running |

### 2.3 Salary: what the numbers say and why they lie

**What the numbers say (US, 2025–2026, aggregated across Stack Overflow 2025, Levels.fyi, and several 2026 job-posting scrapes; treat as ±15%):**

| Tier | Languages | Typical US median (experienced) |
|---|---|---|
| **Scarcity premium** | Erlang, Elixir, Clojure, Scala, F#, OCaml, Solidity | $145k–$170k |
| **High-demand systems / cloud** | Rust, Go | $140k–$155k |
| **Mainstream-high** | Kotlin, Swift, TypeScript, C++, Ruby | $125k–$145k |
| **Mainstream** | Python, Java, C#, JavaScript, SQL | $115k–$135k |
| **Mainstream-lower / high-volume** | PHP, Dart, Visual Basic, COBOL | $95k–$120k |

Outside the US, multiply by roughly: Western Europe 0.5–0.7, UK 0.55–0.7, Canada 0.65–0.8, Australia 0.7–0.85, Eastern Europe 0.3–0.5, India 0.12–0.25, LATAM 0.25–0.45 — with large variance by city and remote-for-US-company arrangements that can flatten the gap entirely.

**Why they lie:**

1. **Selection effect.** Nobody's first language is Erlang. The Erlang median reflects 10-year veterans. Learning Erlang doesn't make you a veteran.
2. **Small samples.** Clojure and F# medians are computed from a few hundred respondents; a handful of hedge-fund salaries swing the number.
3. **Domain confound.** "Scala pays well" mostly means "big-data engineers at large companies pay well." "Solidity pays well" means "crypto paid well in the bull market and had few practitioners."
4. **Language ≠ role.** The highest-paid Python users are ML engineers at frontier labs; the lowest-paid are QA scripters. The spread *within* Python (~$80k to $500k+) dwarfs the difference *between* Python's and Go's medians.
5. **Survivorship.** People still writing COBOL are those who stayed; the number says nothing about how easy it is to *enter*.

**How to actually use salary data:**

- Pick your **domain** first (Part III). Salary follows domain and seniority, not syntax.
- Within a domain, prefer the language with **more openings** over the one with a slightly higher median. Optionality compounds; a 5% median difference doesn't.
- Treat the "scarcity premium" tier as a **third or fourth language** to learn once you're senior and want to move into a niche — not as a first language.
- Rust and Go are the exceptions that partly justify the hype: they combine above-mainstream pay with *growing* demand (JetBrains' #1 and #2 "want to adopt" languages), and both are learnable as a second language.

### 2.4 Momentum: who's rising, who's falling

**Rising (2024 → 2026):**

| Language | Evidence | Read |
|---|---|---|
| **TypeScript** | #1 on GitHub (Aug 2025), +66% contributors; frameworks default to TS; JetBrains' biggest migration winner | The new default for anything web. JavaScript-without-TypeScript is now a legacy skill. |
| **Python** | +7 pts usage YoY in SO 2025 (largest jump in a decade); +48.8% GitHub contributors; free-threading officially supported in 3.14 | The AI boom's native language. TIOBE share has *fallen* from its 27% peak (Jul 2025) to 17.8%, but that reflects TIOBE's search-based methodology being disrupted by AI, not Python losing users. |
| **Rust** | First-ever TIOBE top 10 (Jul–Sep 2026); 48.8% of surveyed orgs use it non-trivially (up from 38.7% in 2023); in Linux and Windows kernels; government memory-safety guidance; Bun migrated to it | Crossed from "admired" to "adopted." Still a small job market in absolute terms but the fastest-growing systems language. |
| **Go** | JetBrains' #1 "want to adopt" (11%); Green Tea GC (Go 1.26) cut GC overhead 10–40%; entire cloud-native stack | Quietly became the default for infrastructure. Boring in the best way. |
| **C#** | TIOBE Language of the Year 2025 (+2.94 pts); .NET 10 LTS; Unity + Godot; TS-like ergonomics | The most under-rated mainstream language; Microsoft's cross-platform bet has fully paid off. |
| **Kotlin** | Compose Multiplatform iOS stable (May 2025); Google-backed KMP; Swift export | The Android language is now a credible full-stack and cross-platform language. |
| **Julia** | TIOBE #21 and climbing; explicitly taking MATLAB share (MATLAB fell to #27) | Winning the scientific-computing niche, not going general-purpose. |
| **Mojo** | 1.0 shipped Aug 2026; compiler open-sourced under Apache 2.0 | Just became a real language. Watch for GPU/AI-kernel work; too early for a career bet. |

**Stable / plateaued:**

| Language | Notes |
|---|---|
| **Java** | Steady 20% YoY GitHub growth, #2 primary language globally. JDK 25 LTS (Sep 2025) modernizes the language (compact source files, instance `main`). Not exciting, not going anywhere. |
| **C / C++** | TIOBE #2/#3. C++26 finalized (Mar 2026) with reflection, contracts, hardened std lib. Under pressure from Rust and government memory-safety guidance; WG21 rejected the "Safe C++" borrow-checker proposal in favor of "Profiles" — controversial. Demand in gamedev, embedded, HFT, and HPC is unchanged. |
| **JavaScript** | Still #1 in usage (66%) but growth has shifted to TypeScript. IEEE Spectrum dropped it from #3 to #6. You must still learn it — TypeScript *is* JavaScript. |
| **Swift** | Swift 6.3 (Mar 2026) brought official Android support. Apple-platform demand steady; cross-platform ambition arrived late vs. KMP/Flutter. |
| **PHP** | Stable deployment share; Laravel dominates new PHP (64% of PHP devs); PHP 8.5. Declining in *new-project mindshare*, not in jobs. |
| **SQL** | Eternal. #3 usage, top-3 in every Jobs ranking. Not optional. |

**Declining (in mindshare; jobs lag by 5–10 years):**

| Language | Notes |
|---|---|
| **Ruby** | Left TIOBE top 20 in 2026. Rails 8 is excellent, Shopify/GitHub/Stripe still hire, but few new companies start in Ruby. Good *second* language for a web dev who wants a productive, well-paid niche; poor first language for job hunting outside specific hubs. |
| **Perl** | Left TIOBE top 20 in 2026. Legacy sysadmin/bioinformatics only. |
| **Objective-C** | Legacy iOS maintenance only. Learn to *read* if you do iOS. |
| **MATLAB** | Losing to Julia and Python in research; still entrenched in some engineering firms and academia. |
| **Scala** | Spark shops moved to PySpark/SQL; Scala 3 is technically excellent but the market shrank. |
| **Visual Basic** | TIOBE #7 (a methodology artifact) but no new development. Maintenance only. |
| **Zig** | SO "admired" 64%, but still pre-1.0 with breaking releases (0.16 in Apr 2026 rewrote I/O), officially "not stable for serious work," and lost its flagship project (Bun) to Rust. Fascinating language, not a 2026 career bet. |

### 2.5 The junior-market problem

This deserves its own section because it changes the advice.

**The data:** JetBrains 2025 found 61% of junior developers describe the job market as challenging vs. 34% of seniors. Anecdotal reports across 2025–2026 describe entry-level postings down sharply from 2021–2022 peaks while senior/staff demand held. Meanwhile the *supply* of new developers exploded: GitHub added 36 million accounts in 2025 alone (India +5.2M).

**The mechanism:** AI compressed the value of "junior work" (well-specified tickets, boilerplate, glue code) faster than it created new junior roles. Companies are hiring fewer people who need supervision and more people who can supervise — including supervising AI.

**What this means for language choice:**

1. **Pick the language with the *largest* entry-level market, not the coolest one.** That's TypeScript/JavaScript (web), Python (data/AI/backend), Java/C# (enterprise). Rust and Go are excellent *second* languages; junior Rust jobs are rare.
2. **Depth beats breadth.** One language + one framework + one database, known well enough to ship and debug a real application, beats five languages at tutorial level.
3. **Ship things people can see.** A deployed app with users, a merged open-source PR, a published package — these are the new "junior credentials." Certificates and bootcamp completions are heavily discounted.
4. **Learn the parts AI is bad at:** debugging production issues, reading unfamiliar codebases, testing, security basics, performance profiling, and *asking the right questions*. Languages with strong tooling (TypeScript, Rust, Go, C#, Java, Kotlin) make these skills easier to practice.
5. **Consider adjacent on-ramps:** QA automation (Python/TypeScript), data analysis (SQL/Python), IT/DevOps (Bash/Python/Go), technical writing, support engineering. Each has a lower entry bar and a path to software engineering.

---

## Part III — Domain-by-domain: what to learn for what

Each domain below follows the same structure: **the verdict**, **the stack you'll actually use**, **the runners-up and when they win**, **what to learn alongside the language**, and **a first project**. Ratings use the five axes from §1.4 (★ = weak, ★★★★★ = dominant) *for that domain*.

### 3.1 Web frontend

**Verdict: TypeScript. Non-negotiable.**

The browser executes JavaScript (and WebAssembly). Every frontend framework — React, Vue, Svelte, Angular, Solid, Qwik — is written in and scaffolds in TypeScript. In 2025, TypeScript became the #1 language on GitHub by contributors, with +1.05M new contributors (+66% YoY). JavaScript-without-types is now a legacy skill; you learn JS *as the runtime semantics of TS*, not as a separate language.

| Language | Domain fit | Jobs | Learnability | Notes |
|---|---|---|---|---|
| **TypeScript** | ★★★★★ | ★★★★★ | ★★★★ | The answer. |
| JavaScript (plain) | ★★★★★ | ★★★★ | ★★★★ | You'll learn it implicitly. Required knowledge, not a separate choice. |
| Dart (Flutter Web) | ★★ | ★★ | ★★★★ | Only if you're already a Flutter shop. Poor SEO, large bundles. |
| Rust (Leptos/Yew/Dioxus via Wasm) | ★★ | ★ | ★★ | Niche. Wasm can't touch the DOM directly; excellent for compute-heavy widgets (Figma-style), not for typical apps. |
| C# (Blazor) | ★★★ | ★★ | ★★★ | Viable inside .NET shops; .NET 10 improved Blazor Wasm preloading. Not a general choice. |
| Elm / PureScript / ReScript / Gleam (Lustre) | ★★ | ★ | ★★★ | Beautiful, tiny job markets. Learn for enlightenment, not employment. |
| Kotlin/JS, Scala.js, ClojureScript | ★★ | ★ | ★★ | Only if your team already lives in that language. |

**The stack (2026):** TypeScript → React (still ~60%+ of frontend job postings) with Next.js or Vite + TanStack; or Vue/Nuxt (strong in Asia/Europe); or Svelte/SvelteKit (rising, beloved). CSS via Tailwind. State via TanStack Query + Zustand/Signals. Testing via Vitest + Playwright. Runtime: Node.js (default) or Bun (Anthropic-owned since Dec 2025; now Rust-based).

**Learn alongside:** HTML semantics and accessibility (ARIA), CSS (Flexbox, Grid, container queries), HTTP and REST, browser DevTools, Git, a component library, basic design principles. Know how bundlers work (Vite/esbuild/Rolldown).

**First project:** A personal dashboard that pulls from 2–3 public APIs, with client-side routing, a dark-mode toggle, and deployment on Vercel/Netlify/Cloudflare Pages.

### 3.2 Web backend / APIs

**Verdict: it depends on your context more than any other domain — but for most people, TypeScript (Node/Bun) or Python.**

| Language | Domain fit | Jobs | Learnability | Perf | Best when |
|---|---|---|---|---|---|
| **TypeScript (Node/Bun/Deno)** | ★★★★★ | ★★★★★ | ★★★★ | ★★★ | You also do frontend (one language, shared types); startups; serverless/edge; real-time. Frameworks: Hono, Fastify, NestJS, Express, Next.js API routes, tRPC. |
| **Python** | ★★★★★ | ★★★★★ | ★★★★★ | ★★ | Data/AI adjacent; rapid prototyping; teams with data scientists. FastAPI (+5 pts YoY, the modern default), Django (batteries-included, admin, ORM), Flask, Litestar. Free-threading (3.14+) is closing the concurrency gap. |
| **Go** | ★★★★★ | ★★★★ | ★★★★ | ★★★★★ | Microservices, high-throughput APIs, cloud infra, anything that ships as a single binary. stdlib `net/http` + chi/echo/gin; sqlc; gRPC. |
| **Java** | ★★★★★ | ★★★★★ | ★★★ | ★★★★ | Large enterprises, banking, telecom, anything needing 15-year support. Spring Boot dominates; Quarkus/Micronaut for cloud-native. JDK 25 LTS with virtual threads makes concurrency easy. |
| **C#** | ★★★★★ | ★★★★ | ★★★★ | ★★★★★ | Microsoft-centric orgs, Azure, gaming backends, anything Windows. ASP.NET Core is one of the fastest mainstream frameworks (TechEmpower). .NET 10 LTS. |
| **Kotlin** | ★★★★ | ★★★ | ★★★★ | ★★★★ | JVM shops wanting modern ergonomics; Android teams going full-stack. Spring Boot or Ktor. |
| **Rust** | ★★★★ | ★★ | ★★ | ★★★★★ | Performance-critical services, proxies, anything where a crash costs money, teams that already know Rust. Axum/Actix. Slower to build features; excellent for the hot path. |
| **PHP** | ★★★★ | ★★★★ | ★★★★★ | ★★★ | Agencies, WordPress/WooCommerce ecosystem, cheap hosting, small-business SaaS. Laravel is genuinely excellent (64% of PHP devs). PHP 8.5. |
| **Ruby** | ★★★★ | ★★ | ★★★★★ | ★★ | Rails 8 for solo founders and small teams shipping fast; a well-paid niche (Shopify, GitHub, Stripe-adjacent). Shrinking new-project share. |
| **Elixir** | ★★★★ | ★★ | ★★★ | ★★★★ | Real-time (chat, live dashboards, IoT fleets), fault tolerance, Phoenix LiveView (most-admired web framework 3 years running). Small but passionate, well-paid market. |
| Scala / Clojure / F# / Haskell / OCaml | ★★★ | ★ | ★★ | ★★★★ | Specific shops (fintech, ad-tech, Jane Street-style). Not a first backend language. |

**Decision rule:**
- Solo dev or startup, also doing frontend → **TypeScript**.
- Data/ML-adjacent, or you want the gentlest curve → **Python**.
- Cloud infra / high throughput / you like simple languages → **Go**.
- You want to work at a bank, insurer, government, or Fortune 500 → **Java** (or **C#** if Microsoft-centric).
- Real-time or must-not-go-down → **Elixir** (or Go/Rust).

**Learn alongside:** SQL and one relational DB (PostgreSQL — the default), HTTP semantics, REST and OpenAPI, auth (OAuth2/OIDC, JWT, sessions), caching (Redis, +8% usage in 2025), queues, Docker (+17 pts YoY — now near-universal), basic Linux, testing, observability (logs/metrics/traces), one cloud (AWS 43% share, then GCP and Azure at 22% each).

**First project:** A REST + WebSocket API for a to-do/notes app with users, auth, Postgres, Redis caching, a Dockerfile, CI that runs tests, and deployment to Fly.io/Railway/Render.

### 3.3 Full-stack web

**Verdict: TypeScript end to end.** Next.js/Remix/SvelteKit/Nuxt/Astro + a TS backend (or the framework's own server functions) + Postgres via Drizzle/Prisma + Tailwind. One language, shared types, one package manager, one deploy. This is the single most employable stack for a generalist in 2026.

**Alternative:** Python (Django or FastAPI) + HTMX/Alpine for server-rendered apps with minimal JS — a strong, underrated choice for solo builders and internal tools. Or **Rails 8** / **Laravel** / **Phoenix LiveView** for the "one framework does everything" experience.

### 3.4 Mobile — iOS

**Verdict: Swift.** SwiftUI is Apple's future; UIKit is the present you'll still need to read. Swift 6.2/6.3 made concurrency approachable and (6.3, Mar 2026) added official Android support — interesting for shared logic, not yet a reason to skip Kotlin.

- **Objective-C:** learn to *read* it; large legacy codebases still exist. Don't write new code in it.
- **Cross-platform alternatives:** see 3.6.

**Learn alongside:** Xcode, SwiftUI + UIKit interop, Combine/async-await, Core Data/SwiftData, App Store process, HIG, TestFlight, Instruments profiling.

### 3.5 Mobile — Android

**Verdict: Kotlin.** Google's recommended language since 2019; Jetpack Compose is Kotlin-only; Google I/O 2026 doubled down (Kotlin in AI Studio for app generation). Java is for maintaining older apps — you'll read plenty of it.

**Learn alongside:** Android Studio, Compose, coroutines/Flow, Room, Hilt, Gradle (Kotlin DSL), Play Store process, Material 3.

### 3.6 Mobile — cross-platform

**Verdict: no single winner; choose by what you already know.**

| Option | Language | Choose when | 2026 status |
|---|---|---|---|
| **React Native (Expo)** | TypeScript | You know React/web; you want max code sharing with a web app; large hiring pool | ~43% of cross-platform devs (one 2026 survey). New Architecture default; Expo is the standard. Expo is a top-10 GitHub project by contributors. |
| **Flutter** | Dart | You want pixel-identical UIs on both platforms, strong animation, one team; desktop/embedded too | ~35%. Impeller renderer default (Skia removed on iOS); Wasm web target; quarterly stable train; used in Toyota RAV4 infotainment and LG webOS. Dart is only useful for Flutter — a real cost. |
| **Kotlin Multiplatform (+ Compose Multiplatform)** | Kotlin | You're an Android team wanting to share logic (and optionally UI) with iOS while keeping native feel | Compose Multiplatform iOS stable since May 2025 (now 1.11); officially Google-supported for shared logic; fastest-growing option (from ~7%). Best for teams already in Kotlin. |
| **.NET MAUI** | C# | You're a .NET shop | Viable, smaller community. |
| **Swift (via Skip / Swift for Android)** | Swift | iOS-first team, curious | Official Android SDK as of Swift 6.3; early days. |

**Decision rule:** Web developer → React Native. Designer-heavy consumer app, or you want one codebase for mobile + desktop + embedded → Flutter. Android team → KMP. Enterprise .NET → MAUI. **If you only ever want to build for one platform, go native (3.4/3.5).**

### 3.7 Desktop applications

**Verdict: pick by target OS; cross-platform means TypeScript (Electron/Tauri) in practice.**

| Target | Language | Framework |
|---|---|---|
| Windows | **C#** | WinUI 3 / WPF / .NET MAUI; Avalonia for cross-platform |
| macOS | **Swift** | SwiftUI / AppKit |
| Linux | **C / C++ / Rust / Python** | GTK4 (C, with Python/Rust bindings), Qt (C++/Python) |
| Cross-platform, web-tech UI | **TypeScript** | **Electron** (VS Code, Slack, Discord) or **Tauri** (Rust backend, smaller binaries; v2 stable) |
| Cross-platform, native-feel | **C++** (Qt), **Dart** (Flutter), **Kotlin** (Compose Multiplatform), **C#** (Avalonia) | Qt 6.10 LTS; Flutter desktop is solid; Compose Desktop is mature |
| Terminal UIs | **Go** (Bubble Tea), **Rust** (ratatui), **Python** (Textual) | The TUI renaissance is real |

### 3.8 Data analysis & data science

**Verdict: Python. SQL is mandatory alongside it. R if you're in academia/biostatistics.**

| Language | Domain fit | Jobs | Notes |
|---|---|---|---|
| **Python** | ★★★★★ | ★★★★★ | pandas → **Polars** (Rust-based, the modern default for new work) → **DuckDB** (in-process SQL analytics, now standard for single-node), NumPy, scikit-learn, matplotlib/plotly, Jupyter (repos +75% YoY). uv for environments. |
| **SQL** | ★★★★★ | ★★★★★ | 58.6% of all developers use it. You will write more SQL than Python in many analyst roles. Learn PostgreSQL dialect, window functions, CTEs; then a warehouse dialect (BigQuery/Snowflake/Databricks). |
| **R** | ★★★★ | ★★★ | Tidyverse, ggplot2, RStudio/Positron, Shiny, Quarto. Dominant in biostatistics, epidemiology, social science, pharma (regulatory submissions), some finance. TIOBE #9. Learn *second* if your field uses it. |
| **Julia** | ★★★ | ★ | Rising in scientific computing and simulation (TIOBE #21, taking MATLAB's share). Not a data-analyst job language yet. |
| Scala | ★★ | ★★ | Legacy Spark. PySpark won. |
| MATLAB | ★★ | ★★ | Entrenched in some engineering firms and courses; declining. Learn if your employer/school mandates it. |
| SAS / Stata / SPSS | ★★ | ★★ | Legacy in pharma, government, social science. Learn on the job if required. |

**Learn alongside:** statistics (seriously — regression, hypothesis testing, Bayesian basics), data visualization principles, Excel (still the lingua franca of business), a BI tool (Tableau/Power BI/Looker/Metabase), Git, dbt, a cloud warehouse.

**First project:** Pull a public dataset (city open data, Kaggle), clean it with Polars, store it in DuckDB, answer five questions with SQL, chart them, and publish a Quarto/Jupyter report.

### 3.9 Machine learning, AI, and LLM applications

**Verdict: Python, overwhelmingly. TypeScript for AI product frontends. C++/CUDA/Triton/Mojo for the kernel layer.**

Python's 2025 surge (+7 pts SO usage, +48.8% GitHub contributors) is the AI boom. Six of the ten fastest-growing GitHub projects in 2025 were AI infrastructure — vLLM, Ollama, llama.cpp, Transformers, SGLang, ComfyUI — and their user-facing layer is Python. Over 1.1M public repos use an LLM SDK.

| Layer | Language | Tools |
|---|---|---|
| **Research / training** | **Python** | PyTorch (dominant), JAX (Google/DeepMind, TPUs), Hugging Face Transformers/Datasets/PEFT, Lightning, Weights & Biases |
| **Inference / serving** | **Python** (orchestration) + **C++/CUDA** (engines) + **Rust** (new servers) | vLLM, SGLang, TensorRT-LLM, llama.cpp (C++), Ollama (Go), candle/mistral.rs (Rust) |
| **LLM application layer ("AI engineering")** | **Python** or **TypeScript** | OpenAI/Anthropic SDKs, LangChain/LangGraph, LlamaIndex, Pydantic AI, Vercel AI SDK (TS), MCP servers (TS/Python), vector DBs |
| **Kernels / GPU programming** | **C++ (CUDA)**, **Triton** (Python DSL), **Mojo** | CUDA is the incumbent. Triton for custom PyTorch kernels without C++. Mojo 1.0 (Aug 2026, Apache 2.0) targets exactly this layer with Pythonic syntax; promising, early. |
| **Edge / on-device ML** | **C++**, **Swift** (Core ML), **Kotlin** (LiteRT/ML Kit), **Rust** | llama.cpp, ONNX Runtime, ExecuTorch |
| **Classical ML / tabular** | **Python** | scikit-learn, XGBoost/LightGBM/CatBoost |
| **Data pipelines for ML** | **Python + SQL** | see 3.10 |

**Decision rule:**
- Want to *train or fine-tune* models, do research, or be an "ML engineer" → **Python**, plus enough C++ to read CUDA kernels and enough math (linear algebra, probability, calculus) to read papers.
- Want to *build products on top of* LLMs ("AI engineer") → **Python or TypeScript** — TS if the product is a web app, Python if it's a pipeline/agent/backend. Many teams use both.
- Want to make models *run fast* → **C++ and CUDA**, then Triton, then watch Mojo.

**Learn alongside:** linear algebra, probability, calculus basics; how transformers work; evaluation methodology; prompt/context engineering; vector search; GPUs and memory bandwidth basics; MLOps (experiment tracking, model registries, serving); cost management.

**First project:** A retrieval-augmented Q&A app over your own documents, with evals that measure answer quality, deployed with a simple TS or Streamlit/Gradio frontend.

### 3.10 Data engineering

**Verdict: SQL + Python. Everything else is context-dependent.**

- **SQL** is the primary language of data engineering. dbt made SQL the transformation layer; warehouses (Snowflake, BigQuery, Databricks SQL, Redshift) and lakehouse engines (Trino, DuckDB, Spark SQL) all speak it.
- **Python** for orchestration (Airflow, Dagster, Prefect), ingestion (dlt, Airbyte connectors), transformation (Polars, PySpark, Ibis), and glue.
- **Scala/Java**: legacy Spark and Flink shops, Kafka internals. Declining for new work; learn on the job if required.
- **Rust**: the *tooling* is increasingly Rust (Polars, DataFusion, Arrow, Delta-rs, uv, ruff). You don't need Rust to use them; you need it to *build* them — a strong niche for a senior DE.
- **Go**: streaming and infra components.

**Learn alongside:** data modeling (Kimball, Data Vault, one-big-table), Apache Arrow/Parquet/Iceberg, Kafka, Spark fundamentals, cloud storage, IaC (Terraform/HCL — HCL is a top-10 GitHub language), cost optimization, data quality/testing.

### 3.11 Systems programming (operating systems, databases, browsers, runtimes, networking)

**Verdict: Rust for new projects; C to understand everything; C++ because the incumbents are written in it.**

The 2024–2026 shift is decisive. Rust is in the Linux kernel (as a second implementation language), the Windows kernel, Android (which prioritizes Rust and Java for all new native code, with zero memory-safety vulnerabilities found in its Rust code), Chromium, Firefox, AWS (Firecracker, S3 components), Cloudflare, and Microsoft's core. CISA, NSA, and FBI guidance asked vendors to publish memory-safety roadmaps by 1 Jan 2026. 48.8% of organizations in the State of Rust 2025 survey make non-trivial use of Rust, up from 38.7% in 2023. Rust entered TIOBE's top 10 for the first time in mid-2026. Bun — one of the flagship Zig projects — migrated to Rust in July 2026 citing memory bugs.

| Language | Domain fit | Jobs | Learnability | Notes |
|---|---|---|---|---|
| **Rust** | ★★★★★ | ★★★ (growing) | ★★ (★★★ with LLM help) | The choice for new systems code. Cargo is the most-admired build tool (71%). Costs: compile times, learning curve, async complexity. Hiring pool still thin. |
| **C** | ★★★★★ | ★★★★ | ★★★ | Still the lingua franca: Linux, embedded, every FFI. GCC 15 defaults to C23. You must be able to read and write C to work in this domain regardless of your primary language. |
| **C++** | ★★★★★ | ★★★★★ | ★★ | The incumbents (Chromium, LLVM, databases, game engines, HFT) are C++. C++26 (finalized Mar 2026) adds reflection, contracts, hardened std lib. WG21 chose "Profiles" over a borrow checker — controversial and unproven. Enormous existing job market; slowly shrinking new-project share. |
| **Zig** | ★★★★ | ★ | ★★★ | Elegant "better C" with comptime and a superb cross-compiler. Pre-1.0; 0.16 (Apr 2026) rewrote I/O; official stance "not stable for serious work"; Bun left. Learn for insight or if you work on TigerBeetle/Ghostty-style projects. Not a 2026 career bet. |
| **Go** | ★★★ | ★★★★ | ★★★★ | Not "systems" in the kernel sense, but the language of infrastructure software (Docker, Kubernetes, etcd, Prometheus, Terraform, Ollama). If your "systems" means "distributed systems," Go is the answer. |
| **Odin / Hare / Carbon / Jai** | ★★ | ★ | ★★ | Experiments. Carbon (Google) still explicitly experimental. |
| **Assembly (x86-64, ARM64, RISC-V)** | ★★★★ | ★★ | ★★ | Read it; write it rarely. Essential for debugging, perf, security, compilers. |

**Learn alongside:** computer architecture, OS concepts (processes, memory, scheduling, file systems), networking (TCP/IP, sockets), concurrency, compilers basics, Linux internals, debuggers (gdb/lldb), profilers (perf, VTune), sanitizers, `unsafe` discipline.

**First project:** Write a shell in C. Then rewrite it in Rust and compare. Then write a toy key-value store with a write-ahead log.

### 3.12 Embedded, firmware, IoT, robotics

**Verdict: C. Then C++. Rust is the growth edge. MicroPython/CircuitPython for prototyping.**

| Language | Notes |
|---|---|
| **C** | Universal on microcontrollers; every vendor SDK (STM32 HAL, ESP-IDF, Zephyr, FreeRTOS, nRF) is C. Non-negotiable for a firmware career. |
| **C++** | Larger embedded systems, automotive (AUTOSAR), drones (PX4/ArduPilot), robotics (ROS 2), Arduino. Use a constrained subset (no exceptions/RTTI, careful allocation). |
| **Rust** | Embedded Rust (embassy, RTIC, probe-rs) is production-viable on ARM Cortex-M, ESP32, RISC-V. Adoption up ~28% in two years; certification (ISO 26262 via Ferrocene) exists. Still gaps in vendor support. Best as a second embedded language. |
| **MicroPython / CircuitPython** | Fast prototyping, education, low-volume products. Not for production firmware with tight constraints. |
| **Python** | Robotics tooling, ROS 2 nodes (with C++ for hot paths), test automation, data processing from devices. |
| **Assembly** | Startup code, ISRs, DSP inner loops. Read fluently, write rarely. |
| **Ada / SPARK** | Safety-critical aerospace/defense/rail. Small, stable, well-paid niche. Ada re-entered TIOBE's top 20 in 2026. |
| **Lua** | Scripting layer in some embedded products (NodeMCU, OpenResty). |
| **VHDL / Verilog / SystemVerilog** | Not programming languages — hardware description. Learn if you do FPGA/ASIC. |

**Learn alongside:** electronics basics, reading datasheets, RTOS concepts, interrupts/DMA, communication protocols (UART, SPI, I2C, CAN, BLE, MQTT), debuggers (JTAG/SWD), oscilloscopes/logic analyzers, power management, bare-metal boot process.

**First project:** Blink an LED on an STM32 or ESP32 in C without the Arduino framework. Then read a sensor over I2C and send the data over Wi-Fi/MQTT. Then do the same in Rust with embassy.

### 3.13 Game development

**Verdict: C# for most people (Unity or Godot); C++ if you want AAA or engine work; GDScript or Lua for the fastest possible start.**

| Path | Language | Engine | 2026 reality |
|---|---|---|---|
| **Indie / mobile / most studios** | **C#** | **Unity** | Ships the most games by volume (~half of Steam releases). Huge job market. Unity's 2023 pricing debacle dented trust but the ecosystem held. C# skills transfer to enterprise work — a real safety net. |
| **AAA / AA / engine programming** | **C++** | **Unreal Engine 5** | ~42% of AA/AAA studios (GDC 2026). Blueprints for scripting, C++ for everything serious. Also every proprietary engine (Frostbite, Decima, id Tech, Source 2). The hardest path, the highest ceiling. |
| **Open-source indie / 2D / learning** | **GDScript** (Python-like) or **C#** | **Godot 4** | Fastest-growing engine; ~11% of new indie projects; #5 GitHub project by contributors in 2025; top-10 for first-time contributors. GDScript is delightful and only useful in Godot; C# is the transferable choice. |
| **Roblox** | **Luau** (Lua dialect) | Roblox Studio | Enormous youth platform; real money for top creators; skills partly transfer. |
| **Small 2D / jams / learning** | **Lua** (Love2D, Defold, PICO-8), **Python** (Pygame), **JavaScript** (Phaser, PixiJS, Three.js) | — | Web games in TS are a legit path (io games, browser MMOs, casual). |
| **Custom engine / graphics programming** | **C++** (+ Vulkan/DirectX 12/Metal) or **Rust** (wgpu, Bevy) | — | Rust gamedev (Bevy) is exciting but has no shipped-hit track record and few jobs. C++ + graphics APIs is the employable path. Shader languages (HLSL/GLSL/WGSL/Slang) are required. |
| **Gameplay scripting in big studios** | **Lua**, **Python**, **C#**, proprietary | — | Many studios embed Lua for designers. |

**Decision rule:** Want a job at a studio → C# (Unity) or C++ (Unreal), depending on whether you're aiming indie/mobile or AAA. Want to ship your own game fastest → Godot (GDScript) or Unity (C#). Want to build engines → C++ + graphics APIs + math. Kid/teen who loves Roblox → Luau.

**Learn alongside:** linear algebra (vectors, matrices, quaternions), game loops and fixed timesteps, physics basics, rendering pipeline concepts, ECS, a version-control system that handles binaries (Git LFS/Perforce), profiling, level design basics, and how to *finish* a project (the actual hard part).

### 3.14 DevOps, cloud, platform engineering, SRE

**Verdict: Bash + Python + Go, plus config languages (YAML, HCL).**

| Language | Role |
|---|---|
| **Bash** | Glue, CI scripts, container entrypoints, incident response. 48.7% of all developers use shell. Learn it properly (quoting, pipes, `set -euo pipefail`, shellcheck). |
| **Python** | Automation, tooling, cloud SDKs (boto3), Ansible modules, data munging, scripts that outgrow Bash. |
| **Go** | The language of the platform itself: Docker, Kubernetes, Terraform, Prometheus, Grafana agents, etcd, Consul, Vault, Argo, Helm, Ollama. Writing operators, controllers, CLIs, and custom tooling means Go. JetBrains' #1 "want to adopt." Single static binaries, fast builds, simple concurrency. |
| **HCL (Terraform/OpenTofu)** | Infrastructure-as-code. A top-10 GitHub language by activity. Not general-purpose but essential. |
| **YAML** | You will write a shocking amount of it (Kubernetes, GitHub Actions, Ansible, Compose). Learn its gotchas. |
| **PowerShell** | Windows-centric orgs and Azure. |
| **Rust** | Newer infra tooling (Vector, some CNCF projects, eBPF via aya). Second language for platform engineers. |
| **TypeScript / Python (Pulumi, CDK)** | IaC in a real language; growing alternative to HCL. |
| **Nix** | Reproducible builds and environments; steep, cultish, increasingly valued. |

**Learn alongside:** Linux administration, networking (DNS, TLS, load balancing, VPCs), containers and Kubernetes, CI/CD, one major cloud (AWS is 43% share), observability (OpenTelemetry, Prometheus/Grafana), security basics (IAM, secrets), incident management, cost management.

**First project:** Containerize a web app, deploy it to a Kubernetes cluster (kind/k3s locally, then a cloud), provision the infra with Terraform, add CI/CD with GitHub Actions, and set up Prometheus/Grafana dashboards. Then write a small Go CLI that automates one annoying step.

### 3.15 Cybersecurity, penetration testing, reverse engineering, malware analysis

**Verdict: Python + C, then Bash, Go, Assembly, and JavaScript depending on specialty.**

| Specialty | Languages |
|---|---|
| **Pentesting / red team** | **Python** (tooling, exploits, Impacket, Scapy), **Bash**, **PowerShell** (Windows AD), **Go** (implants, C2 — single binaries, cross-compiling, evasion), **C/C++** (custom loaders, shellcode), **JavaScript** (web/XSS/browser) |
| **Web app security / bug bounty** | **JavaScript/TypeScript** (you must read frontend and Node code), **Python** (automation), **SQL** (injection), **PHP/Java/C#** (reading target code) |
| **Reverse engineering / malware analysis** | **C** (to recognize compiled patterns), **Assembly** (x86-64, ARM64), **Python** (Ghidra/IDA/Binary Ninja scripting, angr, pwntools), **C++** (modern malware), **Rust/Go** (increasingly used by malware — learn to reverse them) |
| **Exploit development / vulnerability research** | **C**, **Assembly**, **Python** (pwntools), **Rust** (fuzzing harnesses, safe tooling) |
| **Security engineering / AppSec / detection** | **Python**, **Go**, **SQL/KQL/SPL** (SIEM queries), **YAML/Sigma**, **Rust** (secure tooling) |
| **Smart-contract auditing** | **Solidity**, **Rust**, **Move** |

**Learn alongside:** networking deeply, Linux and Windows internals, web protocols and the OWASP Top 10 (Broken Access Control is now the #1 CodeQL alert, up 172% YoY, partly from AI-scaffolded code), cryptography fundamentals, Active Directory, cloud security (IAM), CTFs (picoCTF → HackTheBox → real CVEs), certifications your target employer values (OSCP, Security+, etc.).

### 3.16 Scientific computing, HPC, simulation, computational science

**Verdict: Python for the interface, C++/Fortran for the kernels, Julia as the rising alternative to both.**

| Language | Role |
|---|---|
| **Python** | The front-end to everything: NumPy/SciPy, JAX, CuPy, Numba, xarray, Dask. Most researchers write Python that calls compiled code. |
| **C++** | Performance kernels, HPC frameworks (Kokkos, RAJA), simulation codes (LAMMPS, OpenFOAM), CUDA/HIP/SYCL. |
| **Fortran** | Still alive in climate, weather, CFD, nuclear, quantum chemistry codes. TIOBE #11. Learn to read and modify; new codes rarely start in it. |
| **Julia** | Designed for exactly this domain: fast, expressive, differentiable, GPU-capable, great for DifferentialEquations.jl, SciML. TIOBE #21 and climbing; explicitly taking MATLAB share. Best modern choice for a *new* simulation code you control. Small job market outside academia/national labs. |
| **MATLAB** | Entrenched in engineering departments, Simulink, control systems, signal processing. Declining but not gone. Learn if required. |
| **R** | Statistics-heavy sciences (biostat, ecology, econometrics). |
| **CUDA / OpenMP / MPI** | Not languages so much as the parallelism layer you must learn regardless of host language. |
| **Mojo** | Newly open-source (Aug 2026), aimed at GPU kernels with Python syntax. Watch. |

### 3.17 Quantitative finance, trading, fintech

| Role | Languages |
|---|---|
| **Quant researcher** | **Python** (pandas/Polars, NumPy, statsmodels, PyTorch), **SQL**, **R** (some shops), **KDB+/q** (tick data at banks/HFTs — small, extremely well-paid niche) |
| **Quant developer / low-latency trading systems** | **C++** (the standard; C++20/23, lock-free, kernel bypass), **Rust** (growing — some HFTs and crypto market makers), **Java** (some exchanges and banks — LMAX-style low-GC Java) |
| **Jane Street–style shops** | **OCaml** — a famous outlier; excellent for functional-programming lovers; a handful of employers |
| **Fintech / payments / banking backend** | **Java** (Spring), **Kotlin**, **Go**, **C#**, **Python**; **COBOL** on the mainframe core |
| **Risk / actuarial / pricing** | **Python**, **C++** (QuantLib), **R**, **Excel/VBA** (still, yes) |
| **Crypto / DeFi** | **Solidity** (EVM), **Rust** (Solana, Polkadot, Near, Cosmos), **Move** (Aptos, Sui), **Go** (node software), **TypeScript** (dApp frontends, ethers/viem) |

### 3.18 Blockchain and smart contracts

**Verdict: Solidity for EVM chains (where most deployed value lives), Rust for everything else, TypeScript for the frontend/tooling.** Move (Aptos/Sui) is a strong technical design with a smaller market. Vyper is a Pythonic EVM alternative. Cairo (Starknet) for ZK rollups. The sector is volatile; treat as a specialty layered on solid general skills (TS + Rust), not a first language. Salaries were among the highest in 2021–2022 and 2024–2025 bull phases and cratered in between.

### 3.19 Automation, scripting, and "I'm not a programmer but…"

**Verdict: Python.** It's the closest thing to a universal automation language, has libraries for everything (Excel via openpyxl, PDFs, email, web scraping via Playwright/httpx, APIs), and AI assistants are exceptionally good at writing Python scripts from plain-English descriptions.

- **Google Workspace users:** Google Apps Script (JavaScript).
- **Microsoft 365 / Windows admins:** PowerShell; Office Scripts (TypeScript); VBA for legacy Excel macros (still everywhere; don't start new ones).
- **macOS:** Shell + Python; AppleScript/JXA/Shortcuts for app automation.
- **Low-code glue:** n8n, Make, Zapier — then Python when you hit their limits.
- **Browser automation:** Python or TypeScript with Playwright.

### 3.20 Enterprise software (banks, insurers, government, Fortune 500, SAP shops)

**Verdict: Java. C# in Microsoft-centric orgs. SQL always. Plus the platform-specific language of your employer.**

| Language | Notes |
|---|---|
| **Java** | #2 primary language worldwide (33%); Spring Boot is the enterprise default; JDK 25 LTS with virtual threads and modern syntax. 20% YoY GitHub growth. The most reliable "get a stable well-paid job anywhere on Earth" language. |
| **C#** | Language of the Year 2025 (TIOBE). .NET 10 LTS. Dominant in healthcare, government (esp. US/UK/Nordics), manufacturing, and anywhere Microsoft licensing runs deep. |
| **Kotlin** | Modern JVM alternative; many Java shops adopt it incrementally. |
| **SQL (Oracle PL/SQL, T-SQL, DB2)** | Deep database skills are disproportionately valued in enterprise. |
| **COBOL / JCL / PL/I / RPG** | Mainframe cores at banks, insurers, airlines, government. Steady demand, decent pay (~$115–120k US median), aging workforce. Not a mythical goldmine — see §3.21. |
| **ABAP** | SAP shops. Extremely stable niche; SAP is moving toward "clean core" with side-by-side extensions in Java/Node (BTP). |
| **Salesforce Apex** | Java-like; a large, specific ecosystem with its own certifications. |
| **ServiceNow JavaScript, Pega, Mendix, OutSystems, Power Platform** | Low-code platforms with real (if unglamorous) careers. |
| **Go / Python / TypeScript** | Increasingly present in enterprise "digital" teams, cloud migrations, and internal tooling. |

### 3.21 Legacy systems and mainframes

**Verdict: COBOL + JCL + DB2/SQL + (increasingly) Java for modernization.**

**The reality vs. the myth:** There is a persistent story that COBOL programmers earn fortunes because nobody knows COBOL. The data says: US COBOL/mainframe developers earn roughly $105–125k median, with senior contractors higher during crises (e.g., 2020 unemployment-system surges). That's *good*, and demand is *steady*, but it's not above a senior Java engineer. The work is stable, often remote-unfriendly, concentrated in finance/insurance/government, and increasingly involves *modernization* (wrapping COBOL in APIs, migrating to Java, AI-assisted translation — a very active area in 2025–2026). Learn COBOL if you value stability and don't mind legacy; pair it with Java, SQL, and cloud skills to be the person who bridges old and new.

### 3.22 Compilers, language design, developer tooling

**Verdict: Rust or C++ (or OCaml/Haskell for the theory-heavy path).**

- **Rust:** the language of modern tooling. ruff, uv (fastest-growing GitHub projects), Zed, Turbopack, SWC, Biome, Deno's core, Tauri, Wasmtime, rust-analyzer. If you want to *build* the tools developers use, Rust is where the action is.
- **C++:** LLVM/Clang, GCC, V8, MSVC, JavaScriptCore, most existing compilers. Required to work on the incumbents.
- **OCaml:** The classic compiler-writer's language (Rust's first compiler, Flow, Hack, Coq/Rocq). Small, elite community.
- **Haskell:** GHC, type-theory research, Pandoc. For the theory path.
- **Go:** simpler tooling (esbuild, gopls, many linters), CLI tools.
- **Zig:** the Zig compiler itself and a few tools; excellent cross-compiler and build system for C/C++ projects.
- **TypeScript:** language servers, VS Code extensions, web-based tooling.

**Learn alongside:** parsing, type systems, IR design, SSA, optimization passes, code generation, LLVM, the Dragon Book or *Crafting Interpreters* (start here), Wasm.

### 3.23 Hardware description and FPGA/ASIC

Not programming in the usual sense, but often asked: **SystemVerilog** (industry ASIC/verification), **Verilog**, **VHDL** (aerospace/defense/Europe), with **Python** (cocotb, Amaranth), **Chisel** (Scala, RISC-V ecosystem), and **C++** (SystemC, HLS) for modern flows. **Tcl** for tool scripting, unavoidably.

### 3.24 Education and teaching

| Learner | Language | Why |
|---|---|---|
| **Ages 6–10** | Scratch / ScratchJr | Visual blocks, immediate feedback, MIT-designed. |
| **Ages 10–14** | Scratch → **Python**; Roblox **Luau**; MakeCode (blocks→JS) for micro:bit | Python has the most kid-oriented material; Roblox has the most motivation. |
| **Ages 14–18** | **Python** or **JavaScript**; **Java** (AP CS A in the US); **C#** (Unity) or **Lua** for game-motivated teens | Match the language to what they want to build. |
| **University CS intro** | **Python** (most common), **Java**, **C** (systems-first schools), **Racket/Scheme** (HtDP/SICP tradition), **OCaml** (some), **Haskell** (some) | Any of these works; the *course* matters more than the language. |
| **Adult career switchers** | **Python** or **TypeScript** | See Part V. |

### 3.25 "Enlightenment" languages — learning to think better

These will not get you a job directly (usually). They will make you a dramatically better programmer in whatever language you use for work. Pick one after you're comfortable in a mainstream language.

| Language | What it rewires |
|---|---|
| **Haskell** | Purity, laziness, algebraic data types, type classes, monads. Once you understand these, you see them everywhere (Rust's `Option`/`Result`, TypeScript's discriminated unions). |
| **OCaml** | Pragmatic typed FP; the type inference is a revelation; modules as a first-class concept. Used at Jane Street, in the original Rust compiler, in Coq. |
| **Racket / Scheme (via SICP or HtDP)** | Code as data, recursion as the primary tool, building languages inside languages. |
| **Clojure** | Lisp on the JVM with immutable data structures and a REPL-driven workflow; a real (small) job market, high salaries. |
| **Elixir / Erlang** | The actor model, "let it crash," supervision trees — a fundamentally different theory of reliability. Elixir #3 most admired; Phoenix most-admired web framework. |
| **Rust** | Ownership and borrowing make you think about lifetimes and aliasing in *every* language afterward. |
| **Prolog** | Logic programming: state facts and rules, let the engine search. Unification will change how you think about pattern matching. |
| **Forth** | Stack machines, radical minimalism; you can build the whole language in a weekend. |
| **APL / BQN / Uiua** | Array thinking with extreme terseness; you'll never look at loops the same way. |
| **Smalltalk (Pharo)** | What "everything is an object" and "live programming" actually mean. |
| **Gleam** | Small, friendly typed FP on the Erlang VM; #2 most admired language 2025. A gentler on-ramp to both typed FP and BEAM. |
| **Assembly** | What the machine really does. Pick RISC-V (cleanest) or x86-64 (most useful). |

---

## Part IV — Language profiles

One profile per language a reader might realistically be deciding about. Same fields for each so you can compare. Data points are from Part II sources unless noted.

### 4.1 Python

- **What it is:** Dynamically typed, interpreted, multi-paradigm, famously readable. 1991, Guido van Rossum; governed by the PSF and a Steering Council. Current 3.14 (Oct 2025); 3.15 due Oct 2026.
- **Dominates:** data science, ML/AI, scripting/automation, scientific computing, education, backend APIs (FastAPI/Django), DevOps glue.
- **2026 status:** #1 on TIOBE (17.8%; down from a 27% peak as AI disrupted search-based metrics), IEEE (both rankings), and JetBrains (35% primary). #2 on GitHub (2.6M contributors, +48.8%). SO usage +7 pts YoY — the largest jump in a decade. Free-threaded (no-GIL) build officially supported since 3.14; ecosystem compatibility still catching up. `uv` (Rust-based) is now the de-facto package manager.
- **Strengths:** shallowest learning curve of any mainstream language; largest library ecosystem for data/AI; best AI-assistant support of any language (huge corpus); superb glue.
- **Weaknesses:** slow for CPU-bound work (mitigated by NumPy/Polars/Numba/Rust extensions and free-threading); dynamic typing hurts at scale (use type hints + pyright); awkward for browsers/mobile.
- **Salary (US median, experienced):** ~$120–135k; ML engineers far higher.
- **Time to productivity:** 2–4 weeks for scripts; 3–6 months for professional backend work.
- **Learn it if:** you're a beginner without a specific goal; you want data/AI/automation; you're a scientist, analyst, or non-programmer who needs to code.
- **Skip it if:** your sole goal is frontend web, iOS/Android, game engines, or firmware.
- **Pairs with:** SQL (mandatory), TypeScript (web), Rust/C++ (performance), Bash.
- **Verdict:** the best first language for most people and the single most useful language in 2026.

### 4.2 JavaScript

- **What it is:** The browser's language (1995, Brendan Eich); dynamic, prototype-based, event-driven; standardized as ECMAScript with annual releases. Server-side via Node.js, Bun, Deno.
- **2026 status:** still #1 in SO usage (66%) but growth has moved to TypeScript; IEEE dropped it from #3 to #6. Every serious JS codebase is becoming a TS codebase.
- **Strengths:** runs everywhere; npm is the largest package ecosystem; async model fits I/O; instant visual feedback for learners.
- **Weaknesses:** infamous quirks (`==`, `this`, coercion); dynamic typing at scale; ecosystem churn; competing runtimes and bundlers.
- **Verdict:** required knowledge if you touch the web — but learn it *through* TypeScript.

### 4.3 TypeScript

- **What it is:** Microsoft's statically typed superset of JavaScript (2012, Anders Hejlsberg); strips to JS. The compiler was ported to Go in 2025–26 for ~10× speed.
- **Dominates:** web frontend, Node backends, full-stack frameworks (Next.js, SvelteKit, Nuxt), React Native, Electron/Tauri, VS Code extensions, AI-product frontends, MCP servers.
- **2026 status:** **#1 language on GitHub** by contributors since Aug 2025 (+1.05M, +66.6% YoY); #4 primary in JetBrains (22%) and the "most dramatic" migration winner. GitHub attributes part of the rise to AI: types make agent-generated code verifiable. Bun (Anthropic-owned since Dec 2025, now Rust-based) and Deno compete with Node; Node remains default.
- **Strengths:** one language across the stack; best-in-class tooling; expressive structural typing; enormous job market; gradual adoption.
- **Weaknesses:** deliberately unsound type system (escape hatches); build-step complexity; runtime is still JavaScript; framework churn; type-golf can become a time sink.
- **Salary:** ~$125–140k US median.
- **Time to productivity:** if you know JS, days; from zero, 2–3 months to a first deployed app.
- **Learn it if:** you want the most job openings for one language; web apps; AI product UIs; React Native.
- **Verdict:** the most employable single language of 2026 and the default for anything with a UI.

### 4.4 Java

- **What it is:** Statically typed, GC'd, JVM OOP language (1995). Six-month cadence; LTS every two years — **JDK 25 LTS (Sep 2025)**; JDK 27 Sep 2026.
- **Dominates:** enterprise backends (Spring Boot), banking/insurance/telecom, legacy Android, big-data infrastructure (Kafka, Elasticsearch, Cassandra, Flink), exchanges.
- **2026 status:** #4 TIOBE, #4 GitHub (+20.7%), #2 JetBrains primary (33%), top-3 IEEE Jobs. Modern Java (records, sealed types, pattern matching, virtual threads, compact source files) is a far better language than its 2010 reputation.
- **Strengths:** vast job market everywhere on Earth; mature tooling and ops knowledge; excellent JVM performance; backward compatibility; Spring covers everything.
- **Weaknesses:** verbose (improving); startup/memory footprint (GraalVM native image helps); ceremony-heavy culture; Oracle licensing anxiety (use Temurin/Corretto).
- **Salary:** ~$115–135k US median.
- **Learn it if:** you want a stable, well-paid job at a large organization in any country; JVM data infrastructure; your CS program teaches it.
- **Skip it if:** you're a solo founder or early startup (TS/Python/Go iterate faster); frontend or data science.
- **Verdict:** the safest career language on the planet; boring is a feature.

### 4.5 C#

- **What it is:** Microsoft's typed, GC'd, multi-paradigm language (2000). .NET is open-source and cross-platform. **.NET 10 LTS + C# 14 (Nov 2025)**, supported to Nov 2028.
- **Dominates:** Windows desktop, enterprise backends in Microsoft shops, Unity games, Azure, healthcare/government IT; strong in Godot and MAUI.
- **2026 status:** **TIOBE Language of the Year 2025** (+2.94 pts). #5 TIOBE, #5 GitHub (+22.2%). C# 14 extension members; .NET 10 file-based apps (`dotnet run app.cs`). ASP.NET Core is among the fastest mainstream web frameworks.
- **Strengths:** arguably the best-designed mainstream OOP language (LINQ, async/await pioneered here, records, patterns, nullable reference types); superb tooling; one language from web to desktop to games to cloud.
- **Weaknesses:** lingering "Microsoft-only" perception; smaller startup/OSS mindshare than TS/Python; MAUI less polished than competitors.
- **Salary:** ~$115–135k US median.
- **Learn it if:** game development (Unity/Godot) with a transferable skill; Microsoft-centric enterprise; you want a very well-designed typed backend language.
- **Verdict:** the most under-rated mainstream language.

### 4.6 Go

- **What it is:** Google's typed, GC'd, compiled minimalist language (2009). Goroutines/channels; single static binaries. **Go 1.26 (Feb 2026)** made the Green Tea GC default (10–40% less GC overhead).
- **Dominates:** cloud-native infrastructure (Docker, Kubernetes, Terraform, Prometheus, etcd, Vault, Argo, Helm), CLIs, network services, DevOps tooling, some backends (Uber, Cloudflare), Ollama.
- **2026 status:** **#1 "want to adopt" (JetBrains, 11%)**; top-10 GitHub; ~$147k US median in one 2026 aggregate — among the highest for a mainstream language.
- **Strengths:** learnable in a week if you know any C-family language; fast compile; trivial deploy; excellent stdlib; first-class concurrency; codebases look alike, which is great for teams.
- **Weaknesses:** deliberately limited expressiveness (modest generics, no sum types, `if err != nil`); GC unsuitable for hard real-time; weaker domain modeling than Rust/Kotlin/C#.
- **Learn it if:** DevOps/platform/cloud/SRE; servers, CLIs, infra tooling; you want a fast, simple compiled language.
- **Skip it if:** it's your first language *and* you want web UI or data science — start with TS or Python, add Go later.
- **Verdict:** the best second language for backend and infrastructure people.

### 4.7 Rust

- **What it is:** Mozilla-born (1.0 in 2015), now Rust Foundation. Compiled, no GC, memory-safe via ownership/borrowing. Six-week releases; 2024 edition current.
- **Dominates:** new systems software, developer tooling (uv, ruff, Zed, Turbopack, SWC, Biome, Deno core, Tauri), browser components, cloud infra (Firecracker, parts of AWS/Cloudflare/Azure), embedded (growing), Wasm, blockchain (Solana, Polkadot), data tools (Polars, DataFusion, Arrow).
- **2026 status:** **first-ever TIOBE top 10 (#10, Jul–Sep 2026)**. Most admired language 10 years running (72%). #2 "want to adopt" (10%). 48.8% of surveyed orgs use it non-trivially (State of Rust 2025; 38.7% in 2023). In the Linux and Windows kernels; Android's preferred native language; US government memory-safety guidance; Bun migrated from Zig to Rust (Jul 2026). The project's own Mar 2026 report names complexity, learning curve, compile times, and async as the top challenges.
- **Strengths:** C++-class performance with compile-time memory and thread safety; Cargo (most-admired build tool, 71%); best-in-class error messages; growing, well-paid market; LLMs have dramatically flattened the curve.
- **Weaknesses:** steep learning curve (ownership, lifetimes, traits, async); slow compiles; thin hiring pool ("Rust developers are still hard to find" — Welsh, Mar 2026); slower feature velocity than GC'd languages; GUI ecosystem gaps.
- **Salary:** ~$140–155k US median.
- **Time to productivity:** 2–4 months to comfortable; 6–12 to fluent.
- **Learn it if:** systems programming, dev tooling, performance-critical services, safe embedded, Wasm, blockchain; or you know one language and want to become much better.
- **Skip it if:** it would be your first language; you're at an early-stage startup where iteration speed is everything; you need many junior openings *now*.
- **Verdict:** the most important language of the decade for systems work and the best "second-plus" language; not a first language.

### 4.8 C

- **What it is:** The 1972 systems language everything is built on. C23 current; GCC 15 defaults to it.
- **Dominates:** OS kernels, embedded/firmware (nearly universal), language runtimes (CPython), databases (SQLite, PostgreSQL), networking stacks, every FFI boundary.
- **2026 status:** TIOBE #2 (10.3%). Not growing, not going anywhere. Pressure from Rust for *new* code; utterly entrenched in existing code and embedded.
- **Strengths:** tiny language, learnable in weeks; maps directly to hardware; ultimate portability; teaches how computers actually work.
- **Weaknesses:** no memory safety (~70% of serious vulnerabilities in large codebases); undefined behavior; minimal stdlib.
- **Verdict:** learn to *read* it no matter what; learn to *write* it for embedded, systems, and security.

### 4.9 C++

- **What it is:** C with classes, templates, and forty years of power (1985). ISO standard every three years — **C++26 technically finalized Mar 2026** (static reflection, contracts, `std::execution`, hardened standard library, SIMD).
- **Dominates:** game engines (Unreal, every AAA engine), browsers, compilers (LLVM, GCC), HFT, HPC/simulation, databases, CAD/graphics/VFX, larger embedded, automotive, CUDA, ML inference engines (llama.cpp, TensorRT), audio.
- **2026 status:** TIOBE #3 (8.7%), top-5 IEEE, #8 GitHub. Enormous stable job market. Strategic pressure: government memory-safety guidance; WG21 rejected "Safe C++" (borrow checker) in favor of "Profiles" (criticized as unimplemented); Herb Sutter stepped down as convenor. Industry adoption lags standards by 3–5 years.
- **Strengths:** maximum performance with high-level abstractions; the incumbents are written in it; C++20/23/26 is far more pleasant than C++98.
- **Weaknesses:** the largest, most complex mainstream language; legacy idioms coexist with modern ones; memory unsafety; slow compiles; no standard package manager.
- **Salary:** ~$125–150k US median; HFT far higher.
- **Learn it if:** AAA games, engines, graphics, HFT, HPC, compilers, browsers, automotive.
- **Verdict:** still essential where it's essential; no longer the default for new systems code.

### 4.10 Kotlin

- **What it is:** JetBrains' typed JVM language (1.0 in 2016) with null safety, coroutines, concise syntax; compiles to JVM, JS, Wasm, native (KMP). Current 2.3 (Dec 2025).
- **Dominates:** Android (Google-recommended; Jetpack Compose is Kotlin-only); growing in JVM backends (Spring, Ktor) and cross-platform (Compose Multiplatform iOS stable since May 2025).
- **2026 status:** #4 "want to adopt" (6%). Google I/O 2026 reaffirmed Kotlin-first and added Kotlin generation in AI Studio. KMP is the fastest-growing cross-platform option.
- **Strengths:** Java's ecosystem with far less ceremony; seamless interop; excellent coroutines; credible multiplatform story.
- **Weaknesses:** compile times; smaller non-Android market than Java; KMP tooling still maturing.
- **Verdict:** the Android language and a top-tier JVM language; the natural upgrade for Java developers.

### 4.11 Swift

- **What it is:** Apple's typed, compiled language (2014) with value semantics, optionals, protocols, structured concurrency. **Swift 6.3 (Mar 2026)** added an official Android SDK; 6.2 made strict concurrency approachable.
- **Dominates:** iOS, macOS, watchOS, visionOS. SwiftUI is the future; UIKit/AppKit remain in every real codebase.
- **Strengths:** modern, safe, fast; lucrative platform for indies.
- **Weaknesses:** effectively single-vendor; Xcode is the only real IDE; requires a Mac; strict-concurrency migration was painful; smaller market than Kotlin outside the US/Western Europe.
- **Salary:** ~$130–145k US median.
- **Verdict:** mandatory for Apple platforms; not a general-purpose choice.

### 4.12 Dart

- **What it is:** Google's typed, GC'd language (2011) that found its purpose as Flutter's language.
- **2026 status:** Flutter is healthy — Impeller default renderer, Wasm web target, quarterly stable releases (3.44 May 2026), ~35% of cross-platform mobile, embedded wins (Toyota, LG). Dart has essentially zero use outside Flutter.
- **Weaknesses:** every hour learning Dart is an hour not learning TS/Kotlin/Swift; dependency on Google's continued investment.
- **Verdict:** a means to Flutter, not an end. Learn it only after choosing Flutter.

### 4.13 PHP

- **What it is:** The server-side web language (1995). Modern PHP (8.x; **8.5 Nov 2025**) has types, JIT, fibers, enums — a different language from PHP 5.
- **Dominates:** WordPress/WooCommerce (~43% of all websites), Laravel (64% of PHP devs), Symfony, Drupal, Magento; small-business and agency web.
- **2026 status:** TIOBE ~#13, #6 GitHub. Deployment share stable; new-project mindshare slowly declining. Very large market in agencies, e-commerce, Europe/LATAM/South Asia.
- **Strengths:** deployable anywhere; Laravel is one of the best web frameworks in any language; endless maintenance work; low barrier to freelancing.
- **Weaknesses:** reputation lag; lower average pay than TS/Python; WordPress work can be low-margin.
- **Salary:** ~$95–120k US median; high variance.
- **Verdict:** pragmatic, employable, unglamorous; Laravel makes it genuinely enjoyable.

### 4.14 Ruby

- **What it is:** Dynamic, elegant "programmer happiness" language (1995). Rails 8 (Nov 2024) emphasizes deploying without PaaS; Ruby 3.4+ has YJIT.
- **2026 status:** left the TIOBE top 20 in 2026. Shopify, GitHub, Stripe and many startups still run large Rails apps and pay well; few new companies start in Ruby.
- **Strengths:** unmatched ergonomics for CRUD apps; a solo founder ships fastest in Rails; well-paid senior market.
- **Weaknesses:** shrinking new-project share; market concentrated in specific companies/cities; risky as a *first* job-hunting language.
- **Verdict:** excellent language in a slowly shrinking market; a second-language niche, not a first.

### 4.15 SQL

- **2026 status:** #3 in SO usage (58.6%), top-3 in every jobs ranking, TIOBE #8. dbt made it the transformation language of modern data; DuckDB made it the standard for local analytics.
- **What to learn:** SELECT/JOIN/GROUP BY → CTEs → window functions → indexes and EXPLAIN → transactions and isolation → one dialect deeply (PostgreSQL recommended).
- **Verdict:** not optional for any programmer. Highest ROI per hour in this guide.

### 4.16 Bash / Shell

- **2026 status:** 48.7% of developers use shell. PowerShell on Windows; Nushell/Fish for interactive use, but write scripts in Bash for portability.
- **What to learn:** pipes, redirection, quoting, conditionals/loops, `find`/`grep`/`sed`/`awk`/`xargs`/`jq`, `set -euo pipefail`, shellcheck. Switch to Python past ~100 lines.
- **Verdict:** a required tool, not a career.

### 4.17 Zig

- **What it is:** Andrew Kelley's "better C" (2016): manual memory with explicit allocators, `comptime` metaprogramming, no hidden control flow, a world-class cross-compiler and C/C++ build system. **0.16 (Apr 2026)** introduced a new `std.Io` interface — a major breaking change; 1.0 has no date.
- **2026 status:** #4 most admired (64%) but the project's official stance is "not stable for serious work." TigerBeetle and Ghostty ship in production on it; Bun — the flagship — left for Rust in Jul 2026 citing continuous memory bugs. LLM support is weak (small corpus, fast-moving APIs).
- **Learn it if:** you love C, want to understand allocators and comptime, or work on a project that uses it. Also excellent purely as a C/C++ cross-compilation toolchain.
- **Skip it if:** you need a stable career language or strong AI assistance.
- **Verdict:** a fascinating language to *learn from*; not a 2026 career bet.

### 4.18 Elixir (and Erlang, Gleam)

- **What it is:** Ruby-flavored functional language (2011, José Valim) on the Erlang VM (BEAM): lightweight processes, supervision trees, "let it crash," hot code reloading. Phoenix (web) and LiveView (server-rendered real-time UI). Gleam (2019; 1.0 in 2024) is a typed, friendlier BEAM language.
- **2026 status:** Elixir #3 most admired (66%), Gleam #2 (70%); Phoenix the most-admired web framework three years running. Small job market (~2–3% usage), well-paid, concentrated in real-time products, fintech, IoT, and consultancies. Discord, WhatsApp (Erlang), Pinterest, and many chat/telemetry systems run on BEAM.
- **Strengths:** the best concurrency and fault-tolerance model in mainstream use; LiveView lets one dev ship real-time apps without JS; superb docs and community; Nx/Livebook for ML.
- **Weaknesses:** small hiring pool both ways; dynamic typing (a gradual type system is arriving); not for CPU-heavy numeric work.
- **Verdict:** the best language for real-time and must-not-go-down systems; an excellent second or third language; a tough first.

### 4.19 Scala

- **What it is:** Typed OOP+FP on the JVM (2004, Odersky). Scala 3 (2021) simplified the language considerably.
- **2026 status:** ~2.5% usage, shrinking. Spark's user base moved to PySpark and SQL; Kotlin took the "better Java" slot. Still used at Twitter/X, Databricks internals, some banks, and Akka/Pekko shops. High salaries (scarcity).
- **Verdict:** learn on the job if hired into it; not a language to pursue cold in 2026.

### 4.20 Haskell, OCaml, F#

- **Haskell:** pure, lazy, the reference point for typed FP. Tiny job market (finance, blockchain — Cardano, a few startups). Learn it to understand type classes, monads, and purity; you'll write better Rust, TypeScript, and Kotlin afterward.
- **OCaml:** pragmatic typed FP; Jane Street's language; the original Rust compiler; Coq/Rocq; excellent for compilers and tooling. OCaml 5 added multicore and effects. Small elite market.
- **F#:** OCaml's ideas on .NET; used in finance and data-heavy .NET shops. Small but well-paid. Learn if you're already in .NET and want FP.
- **Verdict:** enlightenment languages with a handful of lucrative niches; none is a first language for job hunting.

### 4.21 Clojure and other Lisps

- **Clojure:** dynamic Lisp on the JVM (and JS via ClojureScript) with immutable data structures and a REPL-driven workflow. Consistently one of the highest-paid languages in SO surveys (selection effect), with a real if small job market (Nubank — the largest, Walmart historically, many consultancies).
- **Racket / Scheme / Common Lisp:** teaching and research (Racket, HtDP/SICP), and a small hard-core industrial Lisp community. Common Lisp still has paying niches (Grammarly, some aerospace/defense).
- **Verdict:** learn a Lisp to understand code-as-data and REPL programming; Clojure is the one with jobs.

### 4.22 Julia

- **What it is:** Dynamic, JIT-compiled, multiple-dispatch language for numerical computing (2012; 1.0 in 2018). Solves the "two-language problem" — write high-level code that runs at C speed.
- **2026 status:** TIOBE #21 and climbing, explicitly taking MATLAB's share (MATLAB fell to #27). Strong in scientific ML (SciML), differential equations, climate modeling, pharma (Pumas), some finance. Small job market outside academia and national labs.
- **Strengths:** speed with expressiveness; best-in-class DiffEq and autodiff; excellent for simulation and modeling.
- **Weaknesses:** "time to first plot" (compile latency, improving); smaller ecosystem than Python; few jobs advertise it.
- **Verdict:** the right choice for a *new* scientific code you control; a complement to Python, not a replacement.

### 4.23 R

- **2026 status:** TIOBE #9 (1.7%), ~4% usage. Dominant in biostatistics, epidemiology, pharma (FDA submissions), social sciences, ecology; strong in some finance/economics. Tidyverse, ggplot2, Shiny, Quarto; Positron (VS Code–based) is the new IDE alongside RStudio.
- **Verdict:** essential if your field runs on it; otherwise Python covers the same ground with broader employability. Many analysts know both.

### 4.24 Lua

- **What it is:** Tiny, fast, embeddable scripting language (1993, Brazil). Luau is Roblox's typed dialect.
- **Dominates:** game scripting (Roblox, Love2D, Defold, PICO-8, World of Warcraft, many AAA studios' tooling), Neovim configuration, Redis scripting, OpenResty/nginx, embedded scripting layers.
- **Verdict:** learnable in a weekend; an excellent first language for game-motivated kids via Roblox; a useful utility language for everyone else. Not a career on its own.

### 4.25 Solidity, Move, and blockchain languages

- **Solidity:** the EVM contract language; where most deployed value lives; heavy security culture (audits, formal verification). Vyper is a Pythonic alternative.
- **Rust:** Solana, Polkadot, Near, Cosmos (CosmWasm), most ZK tooling.
- **Move:** Aptos and Sui; resource-oriented design; smaller market.
- **Cairo:** Starknet ZK rollups.
- **Verdict:** volatile, cyclical sector; layer it on top of TS + Rust rather than making it your foundation.

### 4.26 COBOL (and mainframe languages)

- **2026 status:** TIOBE #20. ~$105–125k US median for COBOL/mainframe developers; steady demand at banks, insurers, airlines, and governments; increasingly *modernization* work (API wrapping, Java migration, AI-assisted translation).
- **Verdict:** a stable niche with decent pay, not a goldmine. Pair with Java, SQL (DB2), JCL, and cloud skills.

### 4.27 Mojo

- **What it is:** Modular's Python-syntax systems language for GPU/AI programming (Chris Lattner, 2023). **Mojo 1.0 shipped Aug 2026 and the compiler was open-sourced under Apache 2.0** (18 Aug 2026). No longer aims to be a Python superset — it's its own language optimized for writing kernels and high-performance code with familiar syntax.
- **Verdict:** the most interesting *new* language of 2026 for the AI-kernel layer; too early for a career bet, worth a weekend if you work near CUDA/Triton.

### 4.28 Assembly (x86-64, ARM64, RISC-V)

- **Verdict:** read fluently, write rarely. Required for reverse engineering, exploit development, compilers, performance work, and embedded boot code. RISC-V is the cleanest to *learn*; x86-64 and ARM64 are what you'll *meet*.

### 4.29 Visual Basic, Perl, Objective-C, MATLAB, Fortran, Ada, Delphi/Pascal

Legacy or niche languages that appear on rankings (VB is TIOBE #7, Fortran #11, Ada re-entered the top 20) mainly because of installed base and documentation volume. **Learn them on the job if required; do not pursue them cold** — with two exceptions: **Fortran** if you're entering climate/weather/CFD/nuclear codes, and **Ada/SPARK** if you're targeting safety-critical aerospace, rail, or defense (small, stable, well-paid).

### 4.30 Quick-comparison matrix

| Language | Learnability | Jobs (volume) | Jobs (growth) | Pay | Perf | AI-assist quality | First language? | Best second language for… |
|---|---|---|---|---|---|---|---|---|
| Python | ★★★★★ | ★★★★★ | ★★★★★ | ★★★ | ★★ | ★★★★★ | **Yes** | anyone who started with TS/Java/C# |
| TypeScript | ★★★★ | ★★★★★ | ★★★★★ | ★★★★ | ★★★ | ★★★★★ | **Yes** | Python people who need a UI |
| Java | ★★★ | ★★★★★ | ★★★ | ★★★ | ★★★★ | ★★★★★ | Yes (CS programs) | enterprise-bound devs |
| C# | ★★★★ | ★★★★ | ★★★★ | ★★★ | ★★★★ | ★★★★ | Yes | gamedev, Microsoft shops |
| Go | ★★★★ | ★★★★ | ★★★★★ | ★★★★ | ★★★★ | ★★★★ | Possible | backend/DevOps people |
| Rust | ★★ | ★★★ | ★★★★★ | ★★★★★ | ★★★★★ | ★★★★ | No | systems, tooling, anyone wanting mastery |
| C | ★★★ | ★★★★ | ★★ | ★★★ | ★★★★★ | ★★★★ | Possible (CS) | embedded, security, systems |
| C++ | ★★ | ★★★★★ | ★★ | ★★★★ | ★★★★★ | ★★★★ | No | games, HFT, HPC |
| Kotlin | ★★★★ | ★★★ | ★★★★ | ★★★★ | ★★★★ | ★★★★ | Possible | Android, Java devs |
| Swift | ★★★ | ★★★ | ★★★ | ★★★★ | ★★★★ | ★★★★ | Possible (Apple-only goal) | iOS |
| SQL | ★★★★ | ★★★★★ | ★★★ | ★★★ | n/a | ★★★★★ | Alongside first | everyone |
| PHP | ★★★★★ | ★★★★ | ★★ | ★★ | ★★★ | ★★★★★ | Possible | freelancers |
| Ruby | ★★★★★ | ★★ | ★ | ★★★★ | ★★ | ★★★★ | No | solo founders |
| Dart | ★★★★ | ★★ | ★★★ | ★★★ | ★★★★ | ★★★ | No | Flutter |
| Elixir | ★★★ | ★★ | ★★★ | ★★★★★ | ★★★★ | ★★★ | No | real-time systems |
| Zig | ★★★ | ★ | ★★ | ★★★★ | ★★★★★ | ★★ | No | C lovers |
| Julia | ★★★★ | ★ | ★★★ | ★★★ | ★★★★★ | ★★★ | Possible (scientists) | Python scientists |
| R | ★★★★ | ★★★ | ★★ | ★★★ | ★★ | ★★★★ | Possible (statisticians) | data analysts |

---

## Part V — Roadmaps by learner profile

Eight archetypes. Find the closest match; adjust the domain choice using Part III. Timelines assume ~10–15 focused hours per week; halve them for full-time study, double them for "an hour when I can."

### 5.1 The absolute beginner with no specific goal

**Goal:** discover whether you like programming and what kind, while building a foundation that transfers anywhere.

| Phase | Duration | Learn | Build |
|---|---|---|---|
| 1 | Weeks 1–6 | **Python** basics: variables, control flow, functions, lists/dicts, files, errors. Use an AI assistant to *explain*, not to *write*. | A CLI tool you actually want: expense tracker, flashcard quizzer, file organizer. |
| 2 | Weeks 7–12 | Modules, virtual environments (uv), `requests`/`httpx`, JSON, a tiny web app (Flask or FastAPI), **Git** and GitHub. | A web app that calls a public API and stores results in SQLite. |
| 3 | Months 4–5 | **SQL** basics; testing (pytest); reading other people's code; debugging with a real debugger. | Contribute a documentation fix or small bug fix to an open-source project. |
| 4 | Month 6 | Sample the domains: one weekend each of (a) TypeScript + a tiny React page, (b) a Pygame or Godot mini-game, (c) a pandas/Polars notebook on a dataset you care about, (d) a Bash script that automates something. | Pick the domain that made you lose track of time. Go to its Part III section. |

**Why Python first:** gentlest syntax, best beginner material, best AI-tutor support, useful in the most domains. **Why not JavaScript first:** the browser is a great motivator, but JS's quirks and the tooling maze (bundlers, frameworks, TS config) confuse beginners; come to TS in month 6 with concepts already in hand. **Exception:** if you *know* you want to build websites, start with TypeScript (5.3).

### 5.2 The career switcher (6–12 months to a first job)

**Goal:** employment in the largest possible market, as fast as possible, with a portfolio that survives a 2026 junior market.

**Path A — Web (largest market):**

| Phase | Duration | Learn | Build / prove |
|---|---|---|---|
| 1 | Months 1–2 | HTML/CSS, **JavaScript fundamentals through TypeScript**, Git. | Three static sites, one with real interactivity. |
| 2 | Months 3–4 | **React** (or Vue/Svelte if the local market prefers), TanStack Query, Tailwind, Vitest. | A CRUD app against a public API, deployed. |
| 3 | Months 5–6 | **Node/Bun backend** (Hono/Fastify/Next.js API), **PostgreSQL + SQL**, auth, Docker, one cloud deploy. | Full-stack app with users, deployed, with tests and CI. |
| 4 | Months 7–9 | Testing depth, accessibility, performance, security basics (OWASP), one "second stack" taste (Python/FastAPI). Open-source contributions. | Two more substantial projects; a merged OSS PR; a blog post or two explaining something you learned. |
| 5 | Months 9–12 | Interview prep: DSA basics in TS (arrays, hash maps, trees, BFS/DFS), system-design basics, behavioral. | Apply widely; target junior/associate, apprenticeships, and adjacent roles (QA automation, support engineering). |

**Path B — Data/AI-adjacent (second-largest, strong for people with domain expertise in finance/health/marketing/ops):**
Python → SQL (deep) → pandas/Polars → statistics → visualization/BI → one cloud warehouse → FastAPI + a small ML or LLM project → dbt/Airflow basics. Roles: data analyst → analytics engineer → data engineer or ML engineer. Your prior domain expertise is the differentiator.

**Path C — Enterprise (stable, global, less startup-flavored):**
Java (or C#) → SQL → Spring Boot (or ASP.NET Core) → testing → Docker → one cloud → Kotlin taste. Roles: junior backend developer at consultancies, banks, insurers, government contractors. More structured hiring, more certifications, more predictable.

**Rules for switchers in 2026:**
- One stack, deep. Recruiters and hiring managers screen for *evidence of shipping*, not language count.
- Deploy everything. A URL beats a repo.
- Use AI to move faster, but be able to explain every line in an interview.
- Network locally; the junior market is relationship-driven now.
- Consider the adjacent on-ramps (§2.5). QA automation and analytics engineering hire juniors more readily than "software engineer I."

### 5.3 The student (CS or adjacent degree)

Your program will pick your first language (Python, Java, or C). Fine — the course matters more than the language. Use your degree's time to do what switchers can't afford:

1. **Go deep on fundamentals:** data structures, algorithms, OS, networks, databases, compilers, distributed systems. These are the skills that supervise AI.
2. **Learn C properly** (if your program doesn't force it) and **one functional language** (OCaml, Haskell, or Racket). These are cheap to learn now and expensive later.
3. **Pick one industrial language and get employable in it** before internship season: TypeScript or Python for most; Java/C# for enterprise-heavy regions; C++ for games/HFT/systems.
4. **Learn Rust in your third or fourth year** if you're at all systems-inclined. It's the language most likely to be *asked about* in the next decade that your program probably won't teach.
5. **Ship something every semester.** Internships are the on-ramp that still works; portfolio projects get them.

### 5.4 The working developer adding a second (or third) language

You know one language well. Which next? Use this table — rows are what you know, columns are what you want.

| You know → want | Web UI | Backend/infra | Data/AI | Systems | Mobile | Games | "Level up my thinking" |
|---|---|---|---|---|---|---|---|
| **Python** | TypeScript | Go | (SQL deeper, Rust for perf) | Rust | Kotlin or Swift | C# | OCaml or Haskell |
| **JavaScript/TS** | — | Go or Python | Python | Rust | Kotlin/Swift (or stay TS w/ RN) | C# | Elixir or Haskell |
| **Java** | TypeScript | Kotlin or Go | Python | Rust or C++ | Kotlin | C# or C++ | Clojure or Scala |
| **C#** | TypeScript | Go | Python | Rust or C++ | Kotlin/Swift (or MAUI) | C++ (Unreal) | F# |
| **C / C++** | TypeScript | Go or Rust | Python | Rust | Kotlin/Swift | (you're set) | Rust or OCaml |
| **Go** | TypeScript | Rust | Python | Rust or C | Kotlin/Swift | C# | Elixir or OCaml |
| **Rust** | TypeScript | Go | Python | (C/C++ to read) | Kotlin/Swift | C++ | Haskell or Lean |
| **PHP / Ruby** | TypeScript | Go or Python | Python | Rust | Kotlin/Swift | C# | Elixir |
| **Kotlin / Swift** | TypeScript | Go | Python | Rust | (the other one) | C# | Haskell |

**Pattern:** TypeScript for anything with a UI; Go for backend/infra; Python for data/AI; Rust for systems; Kotlin/Swift for native mobile; C# for games. The "level up" column is where the FP languages live.

### 5.5 The scientist, analyst, or domain expert who needs to code

**Goal:** use programming as a tool for your actual work — not to become a software engineer.

- **Start:** Python (or R if your field runs on it — biostatistics, epidemiology, ecology, social science). Jupyter/Quarto notebooks. Polars or pandas. Plotting.
- **Add quickly:** **SQL** (you will spend more time with data than with algorithms). Git (for reproducibility). uv/conda for environments.
- **Add later:** a bit of Bash (HPC clusters), a cloud console, one visualization tool (Streamlit/Shiny/Dash), and AI-assistant fluency (you are the ideal user — you know what the answer should look like).
- **Only if needed:** Julia (new simulation code), C++/Fortran (modifying legacy codes), MATLAB (if mandated).
- **Don't bother with:** frontend frameworks, mobile, systems languages.

### 5.6 The kid or teen (and the parent choosing for them)

| Age | Path | Why it works |
|---|---|---|
| 6–9 | ScratchJr → **Scratch** | Visual, immediate, creative; no syntax errors. |
| 9–12 | Scratch → **Python** (via Turtle, then simple games) or **Roblox Luau** if they already play Roblox; **MakeCode** with a micro:bit for hardware fun | Text programming with immediate payoff; motivation from things they already love. |
| 12–15 | **Python** (Pygame, Discord bots, automation), **JavaScript** (p5.js creative coding, small web games), **Luau** (Roblox — some teens earn real money), **Godot/GDScript** | Projects they can show friends. |
| 15–18 | Whatever they want to build: **TypeScript** (websites), **C#** (Unity), **Python** (AI/data), **Java** (AP CS A — the exam matters for US college credit), **C++** (competitive programming/USACO) | Align with college plans and interests; competitive programming is a legitimate path to strong fundamentals. |

**Principles:** motivation over curriculum; finished small projects over unfinished big ones; pair programming with an adult who is *also* learning beats a lecturing adult; AI tutors are excellent but supervise — kids will paste.

### 5.7 The senior engineer or lead choosing a stack for a team

Different question: *what should we build this in?* The five axes shift toward hiring pool, longevity, and operational maturity.

| Situation | Default | Notes |
|---|---|---|
| Early-stage startup, web product | **TypeScript** end-to-end (Next.js/SvelteKit + Postgres) | Largest hiring pool, fastest iteration, one language. Python backend if the product is AI/data-heavy. |
| Early-stage startup, AI/ML product | **Python** (FastAPI) + **TypeScript** frontend | The AI stack is Python; keep the UI in TS. |
| Infrastructure / platform / high-throughput services | **Go** | Simple, fast, huge ecosystem, easy to hire and onboard. Rust for the specific hot paths or where correctness is existential. |
| Performance-critical or safety-critical systems | **Rust** (new) / **C++** (existing ecosystem) | Welsh's 2026 caution still applies: Rust slows early iteration; adopt when robustness > velocity, or when the domain (embedded, security, infra) demands it. |
| Enterprise line-of-business | **Java** (Spring Boot) or **C#** (ASP.NET Core) | Depends on the org's existing platform. Kotlin as the incremental modernization for Java shops. |
| Mobile | Native (**Swift** + **Kotlin**) for consumer apps where quality is the product; **React Native** if the team is web; **Flutter** for a small team needing identical UIs everywhere; **KMP** for an Android-first team | Don't choose cross-platform to save money if the app *is* the business. |
| Data platform | **SQL** (dbt) + **Python** | Scala only if you inherit it. |
| Games | **C#**/Unity or **C++**/Unreal by scope; **Godot** for small teams and 2D | — |
| Internal tools | Whatever the team already knows; **Python** + Streamlit or **TypeScript** + Retool-style | Speed matters more than anything. |

**Team-level rules:**
- The best stack is the one your team can hire for and operate at 3 a.m.
- Prefer boring technology for the 90%; spend your "innovation tokens" on the 10% that's your actual differentiator.
- Typed languages pay off faster now that AI writes a share of the code — reviewers need the compiler's help.
- Migration cost has fallen (AI-assisted rewrites are real), so the "we're locked in forever" fear is weaker than it was — but so is the excuse to pick something exotic.

### 5.8 The hobbyist / lifelong learner

You don't need a job from this; you want joy, insight, and things that work.

- **For making things:** Python (anything), TypeScript (web things), Godot/GDScript or Lua/Love2D (games), MicroPython/Arduino C++ (hardware), Swift (if you love your Mac/iPhone).
- **For insight:** Rust (ownership), Haskell or OCaml (types), Racket/Scheme via SICP (computation), Elixir (concurrency), Prolog (logic), Forth (minimalism), an APL-family language (arrays), Assembly (the machine), Zig (allocators and comptime).
- **For fun communities:** Elixir, Rust, Zig, Gleam, Clojure, Nim, Odin — small, welcoming, intellectually lively.
- **Pace:** one new language per year, each with a real project, is a wonderful decade-long curriculum. Advent of Code in December is the traditional way to try a new language.

---

## Part VI — Sequencing: your second, third, and fourth language

### 6.1 The principle: maximize *conceptual distance*, minimize *career distance*

Your first language should be chosen for employability and learnability. Every language after that should be chosen to teach you something the previous ones couldn't — **while staying close enough to your career that you'll actually use it.**

Learning Python then Ruby teaches you almost nothing new (both dynamic, GC'd, OOP-ish scripting languages). Learning Python then Rust teaches you ownership, static types, traits, zero-cost abstractions, and how memory actually works. Learning Python then Haskell teaches you purity, laziness, and algebraic types. The second pair is worth ten of the first.

### 6.2 Recommended sequences

**The generalist web/product engineer**
1. **TypeScript** (job) → 2. **Python** (data/AI/automation, second job market) → 3. **Go** (backend/infra, concurrency, compiled) → 4. **Rust** or **Elixir** (mastery: ownership, or the actor model)

**The data/AI engineer**
1. **Python** (job) → 2. **SQL** deeply (it's a language; treat it as one) → 3. **TypeScript** (ship UIs for your models) → 4. **Rust** (build fast data tools; read Polars/DataFusion source) or **C++/CUDA** (kernels)

**The systems engineer**
1. **C** (foundation) → 2. **Rust** (modern systems) → 3. **C++** (the incumbents) → 4. **Go** (distributed systems) or **Zig** (allocators/comptime, insight) → 5. **Assembly** (throughout, as needed)

**The enterprise engineer**
1. **Java** or **C#** (job) → 2. **SQL** deeply → 3. **Kotlin** (if Java) / **F#** (if C#) → 4. **TypeScript** (frontends) → 5. **Go** or **Python** (cloud tooling)

**The mobile engineer**
1. **Kotlin** or **Swift** (job) → 2. the other one (you'll need to read it) → 3. **TypeScript** (React Native, web dashboards, backends) → 4. **Rust** (shared cross-platform cores via FFI — a growing pattern) or **Go** (backends)

**The game developer**
1. **C#** (Unity/Godot; ship things) → 2. **C++** (Unreal, engines, the industry standard) → 3. **Lua** (scripting layers) → 4. shader languages (HLSL/GLSL/WGSL — not optional) → 5. **Rust** (Bevy, tooling) for curiosity

**The security engineer**
1. **Python** (tooling) → 2. **C** (understand targets) → 3. **Bash** + **PowerShell** → 4. **Assembly** (x86-64, ARM64) → 5. **Go** (implants/tooling) → 6. **Rust** (secure tooling) and **JavaScript** (web targets)

**The "become excellent" path (for anyone, after year two)**
Pick one from each: a **systems** language (Rust or C), a **typed functional** language (OCaml or Haskell), a **Lisp** (Racket or Clojure), and an **actor/concurrency** language (Elixir/Erlang). Spend three months on each with a real project. You'll emerge a different programmer.

### 6.3 What *not* to do

- **Don't learn two similar languages back-to-back** (Python → Ruby, Java → C#, JS → Dart) unless a job requires it. Marginal learning is near zero.
- **Don't collect languages at tutorial depth.** Five languages at "hello world + a to-do app" is worth less than one at "shipped and maintained for a year."
- **Don't learn a language "for the salary"** without the domain to go with it (see §2.3).
- **Don't chase the language of the month.** If it's still relevant in three years, it'll still be there.
- **Don't skip SQL and Bash.** They're not glamorous; they're load-bearing.

### 6.4 How long does each additional language take?

Rough figures for someone who already programs professionally in one language:

| Transition type | Example | Time to productive | Time to idiomatic |
|---|---|---|---|
| Same family, same paradigm | Java → C#, JS → TS, Python → Ruby | days | weeks |
| Same paradigm, new type discipline | Python → Go, JS → Java | 1–2 weeks | 2–3 months |
| New memory model | Python → C, Java → Rust | 1–2 months | 6–12 months |
| New paradigm | Java → Haskell, Python → Clojure, anything → Prolog | 1–3 months to think in it | 6–12 months |
| New everything | JS → Rust, Python → APL | 2–4 months | 12+ months |

LLM assistance roughly halves the "productive" column for popular languages and does little for the "idiomatic" column — idiom comes from reading good code and getting reviewed.

---

## Part VII — How to actually learn a language in 2026

Language choice is 20% of the outcome. Method is the other 80%. This section is short because the advice is simple; it's just rarely followed.

### 7.1 The loop that works

1. **Pick a project you want to exist** before you start. Not a tutorial project — yours. Small enough to finish in 2–4 weeks.
2. **Learn the minimum** to start it: syntax basics, the standard library's most-used parts, how to run and debug. One good book or course, skimmed; not five, completed.
3. **Build, get stuck, unstick yourself.** This is where learning happens. Use docs first, an AI assistant second, a human third.
4. **Type the code yourself** for the first few months. Autocomplete and agents are fine *after* you can write it unassisted; before that, they build a false sense of competence.
5. **Read code you didn't write** — the standard library, popular open-source projects, your AI assistant's output (critically). This is the fastest way to learn idiom.
6. **Get reviewed.** Post to a community, open a PR, pair with someone. Feedback is the compression algorithm for experience.
7. **Ship it.** Deploy, publish, share. Then start the next one, slightly bigger.

### 7.2 Using AI assistants well

AI coding tools are now used by 85% of developers (JetBrains 2025) and ~80% of new GitHub users in their first week. They are extraordinary learning tools *if used correctly*, and career-limiting if used as a substitute for understanding.

**Do:**
- Ask *why* — "explain this error," "why is this idiomatic," "what are three ways to do this and their trade-offs."
- Ask for critiques of *your* code.
- Use it as a tireless, patient tutor for hard languages (this is exactly how Rust's learning curve got flattened).
- Generate test cases and edge cases you didn't think of.
- Have it explain unfamiliar codebases.

**Don't:**
- Paste generated code you can't explain line by line. Interviewers will ask; production will break.
- Let it pick your architecture. It's biased toward the median of its training data.
- Trust it on obscure languages, fast-moving APIs, or anything version-specific — hallucinated APIs are common (Welsh, IEEE both flag this). Verify against docs.
- Skip fundamentals because "the AI knows them." The AI needs *you* to know when it's wrong.

**Rule of thumb:** for your first ~200 hours in a language, use AI to *explain* and *review*, not to *write*. After that, use it to write boilerplate and *always* read what it wrote.

### 7.3 Resources by language (starting points, not exhaustive)

| Language | Start here | Then |
|---|---|---|
| Python | *Python Crash Course* (Matthes), or the official tutorial; *Automate the Boring Stuff* for non-programmers | *Fluent Python* (Ramalho); Real Python; exercism.org |
| JavaScript/TypeScript | javascript.info; *The TypeScript Handbook*; Total TypeScript (Pocock) | *Effective TypeScript*; the React docs (react.dev); Frontend Masters |
| Java | *Head First Java* (3rd ed.) or *Core Java* (Horstmann); dev.java | *Effective Java* (Bloch); Spring guides; Baeldung |
| C# | Microsoft Learn C# path; *C# in Depth* (Skeet) | *Pro ASP.NET Core*; Nick Chapsas / Tim Corey videos |
| Go | *A Tour of Go*; *Go by Example*; *Learning Go* (Bodner) | *100 Go Mistakes*; Effective Go; the standard library source |
| Rust | *The Rust Programming Language* ("the Book"); Rustlings; *Rust by Example* | *Programming Rust* (Blandy); *Rust for Rustaceans* (Gjengset); Zero To Production |
| C | *C Programming: A Modern Approach* (King) or *Effective C* (Seacord); *Beej's Guides* | *Computer Systems: A Programmer's Perspective*; *Expert C Programming* |
| C++ | *A Tour of C++* (Stroustrup, 3rd ed.); learncpp.com | *Effective Modern C++*; C++ Core Guidelines; CppCon talks |
| Kotlin | Kotlin docs + Koans; *Kotlin in Action* (2nd ed.) | Android Developers courses; KotlinConf talks |
| Swift | *The Swift Programming Language* (Apple); Hacking with Swift (Hudson) | *Swift Concurrency*; WWDC sessions; Point-Free |
| SQL | *SQL for Data Scientists*; sqlbolt.com; pgexercises.com | *Designing Data-Intensive Applications* (Kleppmann) for context; *SQL Performance Explained* |
| Bash | *The Linux Command Line* (Shotts); Bash Guide (mywiki.wooledge.org) | shellcheck everything |
| Elixir | *Programming Elixir* (Thomas); Elixir School; Exercism | *Designing Elixir Systems with OTP*; Phoenix LiveView docs |
| Haskell | *Learn You a Haskell*; *Haskell Programming from First Principles*; *Programming in Haskell* (Hutton) | *Parallel and Concurrent Programming in Haskell* |
| OCaml | *OCaml Programming: Correct + Efficient + Beautiful* (Cornell CS3110); *Real World OCaml* | Jane Street tech blog |
| Lisp/Scheme | *How to Design Programs* (Racket); *SICP*; *Clojure for the Brave and True* | *The Little Schemer* |
| Zig | ziglang.org docs; Ziglings; zig.guide | Read TigerBeetle/Ghostty source |
| Julia | *Think Julia*; official docs; MIT 18.S191 (Computational Thinking) | SciML tutorials |
| Anything | *Crafting Interpreters* (Nystrom) — build a language, understand all languages | Advent of Code; exercism.org; Project Euler; The Odin Project (web) |

### 7.4 Time budgets that are honest

| Milestone | Full-time (40h/wk) | Serious part-time (15h/wk) | Casual (5h/wk) |
|---|---|---|---|
| Hello world → first useful script | 1 week | 2–3 weeks | 2 months |
| First deployed project | 1 month | 2–3 months | 6–9 months |
| Job-ready in a mainstream stack (from zero) | 4–6 months | 9–15 months | 3+ years |
| Comfortable in a second language | 2–4 weeks | 1–3 months | 6 months |
| Senior-level judgment | 3–5 years of shipping, regardless of hours | | |

---

## Part VIII — Anti-recommendations

Blunt advice about what *not* to do, because it's as useful as the positive advice and rarer.

### 8.1 Don't learn these as your *first* language (in 2026)

| Language | Why not first | When it becomes right |
|---|---|---|
| **Rust** | Ownership and lifetimes are hard without knowing *why* they exist; you'll fight the compiler without understanding the problem it's solving. Junior Rust jobs are rare. | Second or third language, after C or after a GC'd language. |
| **C++** | The largest, most footgun-laden mainstream language; forty years of idioms coexist; error messages are hostile. | When your domain (games, HFT, engines) requires it, ideally after C. |
| **Haskell / OCaml / Clojure / Elixir** | Wonderful for insight, poor for first-job hunting; small hiring pools; mental overhead before you've internalized basic programming. | Second-plus, for enlightenment or a specific employer. |
| **Zig, Nim, Odin, Gleam, Mojo, Carbon** | Pre-1.0 or tiny ecosystems; poor AI-assistant support; few jobs; APIs change under you. | Hobby or when your specific project needs them. |
| **Dart** | Only useful for Flutter; if you don't yet know you want Flutter, it's a dead end. | After deciding on Flutter. |
| **Scala** | Shrinking market; complexity; Kotlin and Python took its niches. | If hired into it. |
| **Ruby** | Excellent language, shrinking new-project share; risky for a 2026 job hunt outside specific hubs. | As a second language for a web dev targeting a known Rails employer or founding a startup. |
| **PHP** *(conditional)* | Fine as a first language if you're targeting agencies/WordPress/freelance. Not first if you're targeting startups, big tech, or data. | Depends entirely on your target market. |
| **COBOL** | You'd be optimizing for a myth; the real market is steady and pays fine but requires mainframe context you won't have. | Mid-career, deliberately, for stability. |
| **Solidity** | Domain-specific, sector-volatile, security-critical (mistakes lose real money). | On top of TS + Rust, when you've decided on the sector. |
| **Assembly** | Not a productive first language; teaches the machine but not programming. | Alongside C, for systems/security. |
| **Java** *(mild)* | Perfectly fine and many CS programs start here. The mild caution: ceremony can obscure concepts for self-learners, and beginner material often teaches 2010-era Java. If self-teaching, Python or TypeScript first; if in a program that uses Java, it's fine. | — |

### 8.2 Don't do these things

- **Don't pick a language because of a salary chart.** (§2.3 — the chart measures seniority, not syntax.)
- **Don't pick a language because a YouTuber said it's "dying" or "the future."** Check the job boards in your city and the indices in Part II.
- **Don't learn JavaScript without TypeScript** in 2026. You'll have to relearn habits.
- **Don't skip SQL** because it's "not a real language." It's in more job postings than almost anything else.
- **Don't learn a framework before the language.** React before JavaScript, Django before Python, Spring before Java — this produces people who can't debug.
- **Don't learn five languages shallowly** before getting one job. Depth is what hires in 2026.
- **Don't let AI write your first 10,000 lines.** You'll be unemployable at the exact moment you need to demonstrate competence.
- **Don't ignore your local market.** If every job in your city is Java and C#, the global TypeScript trend is less relevant than you think. Remote work loosens this, but juniors are hired locally more than seniors.
- **Don't wait for the perfect choice.** The cost of a suboptimal first language is weeks. The cost of not starting is years.

### 8.3 Languages this guide is deliberately lukewarm about, and why

- **Zig:** admired, elegant, and — per its own maintainers — not stable for serious work. Bun's departure (Jul 2026) and 0.16's breaking I/O rewrite illustrate the risk. A superb thing to *learn from*; a poor thing to *bet on* right now. Revisit at 1.0.
- **Scala:** a technically excellent language whose market shrank as Spark went Python/SQL and Kotlin took the JVM-modernization slot. Not dead; not growing.
- **Dart:** Flutter is healthy, but a language with exactly one use is a real cost in a world where TypeScript, Kotlin, and Swift each cover mobile *and* other things.
- **Ruby:** the productivity is real and the senior salaries are good, but left the TIOBE top 20 in 2026 and few new companies start in it. A niche, not a foundation.
- **COBOL:** the shortage narrative is overstated; the pay is fine; the work is stable modernization, not a goldmine.
- **MATLAB:** losing to Julia and Python; entrenched only where institutional inertia keeps it.
- **Visual Basic:** TIOBE #7 by search volume, essentially zero new development.
- **Carbon:** still explicitly experimental after four years; Google's own guidance says to use Rust if you can.

---
