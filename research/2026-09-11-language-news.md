# Research notes: per-language state of play (collected 2026-09-11)

## Python
- 3.14 (Oct 2025): free-threaded build officially supported (PEP 779), no longer experimental; concurrent interpreters; ecosystem compat tracking at py-free-threading.github.io. 3.15 due Oct 2026.
- uv (Astral, written in Rust) became dominant package/project manager; among fastest-growing GitHub repos 2025.
- FastAPI +5pts YoY in SO survey. Jupyter repos +75% YoY.
- TIOBE: peaked 26.98% Jul 2025, sliding to 17.76% Sep 2026 (still #1 by 7+ pts).

## TypeScript / JavaScript
- Octoverse 2025: TS #1 by contributors (Aug 2025). +66% YoY. Frameworks scaffold TS by default.
- Bun acquired by Anthropic (Dec 2025). Jul 2026: Bun ported ~535k lines Zig -> Rust in 11 days with 64 Claude agents (~$165k API cost); Zig creator called it "unreviewed slop". Bun has 22M monthly downloads; Claude Code depends on it.
- IEEE Spectrum: JS fell from #3 to #6 (attributed to vibe-coding / fewer public signals).

## Java
- JDK 25 LTS (16 Sep 2025), 18 JEPs; compact source files, instance main methods, etc. JDK 27 due 15 Sep 2026. Next LTS presumably JDK 29 (Sep 2027) under 2-year LTS cadence.
- JetBrains 2025: Java #2 primary language (33%). Octoverse: +20.7% contributors.

## C#/.NET
- .NET 10 LTS + C# 14 (11 Nov 2025), supported to Nov 2028. File-based apps (`dotnet run app.cs`), extension members. .NET 11 previews from Feb 2026.
- TIOBE Language of the Year 2025 (largest rise, +2.94pts to 7.39%). 2nd time in 3 years.

## C / C++
- C++26 finalized technically at March 2026 London WG21 meeting; formal publication late 2026. Static reflection, contracts, std::execution, SIMD types, hardened std lib ("memory safety just by recompiling").
- WG21 rejected Safe C++ (borrow checker) in favor of Profiles; whitepaper pending, criticized as unimplemented.
- Herb Sutter stepped down; Guy Davidson convenor.
- GCC 15 defaults to C23. GCC 16 Apr 2026.
- CISA/FBI: memory-safety roadmaps recommended by 1 Jan 2026. Microsoft engineer's "remove C/C++ by 2030" was research goal, not commitment.
- TIOBE Sep 2026: C #2 10.28%, C++ #3 8.67%.

## Rust
- TIOBE top 10 for first time (Jul-Sep 2026, #10, 1.34%).
- 2025 State of Rust (7,156 responses): 48.8% of orgs make non-trivial use of Rust (38.7% in 2023); hiring trend up; concerns: complexity, compile times; Zed editor surging.
- SO 2025 most admired 72% (down from 83% in 2024 but still #1). Cargo most admired build tool 71%.
- JetBrains 2025: #2 most wanted to adopt (10%).
- Linux kernel and Windows kernel both contain Rust; Android prioritizes Rust+Java for new native code; zero memory safety vulns in Android Rust code.
- Matt Welsh (Mar 2026) "Revisiting Rust": LLMs make Rust much easier to learn; hiring Rust devs still hard; still wouldn't pick it for early-stage startup unless domain demands.
- Rust blog Mar 2026 "What we heard about Rust's challenges": complexity, learning curve, compile times, async.

## Go
- Go 1.25 (Aug 2025): Green Tea GC experimental; Go 1.26 (Feb 2026): Green Tea default, 10-40% less GC overhead; testing/synctest. Go 1.27 due Aug 2026.
- JetBrains 2025: #1 most wanted to adopt (11%). SO 2025: high desire.
- Salary aggregators: Go ~$147k median US (one source).

## Kotlin
- Kotlin 2.3.0 (Dec 2025): Swift export improvements. Compose Multiplatform iOS stable since 1.8.0 (May 2025); now 1.11.0 (May 2026). KMP officially supported by Google for shared logic.
- Google I/O 2026: Kotlin remains recommended Android language; AI Studio "vibe code" Android with Kotlin.
- JetBrains: #4 most wanted to adopt (6%).

## Swift
- Swift 6.3 (Mar 2026): official Android SDK/support. Swift 6.2 (Sep 2025) approachable concurrency.
- Swift-on-Android judged "late to party" vs KMP; Kotlin still overwhelming Android choice.

## Dart/Flutter
- Impeller default renderer (Skia removed on iOS); Flutter 3.44 (May 2026); Wasm target; quarterly stable train; used in Toyota RAV4 infotainment, LG webOS SDK.
- Mobile cross-platform share (one 2026 survey): React Native 43%, Flutter 35%, KMP rising from 7%.

## Zig
- 0.15 (Aug 2025), 0.16 (13 Apr 2026) with new std.Io interface — major breaking changes. Not 1.0; JetBrains blog (Jun 2026) "Why Zig isn't 1.0 yet". Official stance: not stable for serious work, yet TigerBeetle, Ghostty in production. Bun left Zig for Rust (Jul 2026).
- SO 2025 admired 64% (#4).

## Mojo
- Mojo 1.0 (Aug 2026), compiler open-sourced Apache 2.0 (18 Aug 2026). No longer aiming to be a Python superset; own language optimized for GPU programming with Pythonic syntax.

## PHP
- PHP 8.5 (Nov 2025); 8.5.9 Jul 2026. Only 8.2-8.5 supported. Laravel 64% among PHP devs, Symfony 23%, WordPress 25%; PHPStan 36%. WordPress ~43% of websites. TIOBE PHP ~#13.

## Ruby
- Dropped out of TIOBE top 20 in 2026 (with Perl). Rails 8 (Nov 2024) "no PaaS required" push; still strong in startups (Shopify, GitHub).

## Julia / R / MATLAB
- Julia #21 TIOBE Sep 2026 (0.74%), taking share from MATLAB (#27). R #9 (1.69%).

## Elixir / Gleam / Erlang
- SO 2025: Gleam #2 admired (70%), Elixir #3 (66%); Phoenix most admired web framework 3 years running. Historically top-paying in SO surveys.

## COBOL
- TIOBE #20. US avg COBOL dev ~$115k; mainframe dev median total ~$118k. Shortage narrative persists; salaries decent but not extraordinary.

## Game dev
- Unity (C#) ships most games by volume (~51% of 2024 Steam releases per one source); Unreal (C++) dominates AA/AAA (~42% of studios per GDC 2026 report); Godot (GDScript/C#) ~11% of new indie, rising; Godot #5 OSS project by contributors 2025.

## Data engineering
- SQL + Python dominant; Scala/Java "outsiders" now. DuckDB standard single-node SQL analytics; Polars (Rust-based) for transformations; Ibis; pandas losing ground.

## AI effect on languages (cross-cutting)
- Stack Exchange questions in 2025 = 22% of 2024 volume.
- JetBrains: 85% use AI tools; 68% expect AI proficiency required.
- Octoverse: typed languages favored for agentic coding; 80% of new GitHub devs use Copilot in week 1.
- IEEE: LLMs perform worse in low-data languages -> moat for incumbents; harder for new languages.
- Junior market: 61% juniors find market challenging vs 34% seniors (JetBrains).
