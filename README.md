# Game Dev Building Blocks [![Awesome](https://awesome.re/badge-flat.svg)](https://github.com/sindresorhus/awesome#readme)

An awesome-style index of open-source GitHub repositories that can be assembled into games. The goal is to help developers and AI agents start from proven engines, templates, tools, and systems instead of rebuilding a blank slate.

> **Start with a working base.** Pick an engine or framework, clone a starter or complete sample, then add only the systems that fit that stack. Check each repository's license, supported versions, platform targets, maintenance state, and integration requirements before adoption. A listing is a discovery aid, not a compatibility or quality guarantee.

**Repository links:** 440 unique repositories
**Last checked:** 2026-11-18  
**Metadata:** Primary language and SPDX license are GitHub-reported. `license not detected` means inspect the upstream license files before reuse.  
**Scope:** GitHub repositories with source code, tools, templates, or complete games useful in at least one stage of game development. Non-repository tutorials, asset stores, and commercial products without a GitHub code repository are out of scope.

## Contents

- [Start here: reusable foundations](#start-here-reusable-foundations)
- [Planning and game design](#planning-and-game-design)
- [Engines and frameworks](#engines-and-frameworks)
- [Starter projects, samples, and complete games](#starter-projects-samples-and-complete-games)
- [Architecture, ECS, and scripting](#architecture-ecs-and-scripting)
- [Gameplay systems, physics, and AI](#gameplay-systems-physics-and-ai)
- [Rendering, graphics, and shaders](#rendering-graphics-and-shaders)
- [Art, animation, and 3D creation](#art-animation-and-3d-creation)
- [Levels, maps, and world building](#levels-maps-and-world-building)
- [Asset pipelines and file formats](#asset-pipelines-and-file-formats)
- [Audio and music](#audio-and-music)
- [UI, input, accessibility, and localization](#ui-input-accessibility-and-localization)
- [Networking and multiplayer](#networking-and-multiplayer)
- [Persistence, backend, and live operations](#persistence-backend-and-live-operations)
- [Testing, QA, and playtesting](#testing-qa-and-playtesting)
- [Debugging, profiling, and observability](#debugging-profiling-and-observability)
- [Build, CI, packaging, and release](#build-ci-packaging-and-release)
- [Publishing, distribution, and monetization](#publishing-distribution-and-monetization)
- [Learning and reference implementations](#learning-and-reference-implementations)
- [How to assemble a reusable stack](#how-to-assemble-a-reusable-stack)
- [Contributing](CONTRIBUTING.md)

## Start here: reusable foundations

Use this path to avoid starting from an empty project:

1. Choose a foundation in [Engines and frameworks](#engines-and-frameworks).
2. Clone a maintained [starter, sample, or complete game](#starter-projects-samples-and-complete-games) that already builds with that foundation.
3. Keep the starter's working build and add one suitable subsystem at a time.
4. Use this list to find focused components; prefer packages and examples explicitly targeting your chosen engine and version.
5. Pin dependencies and platform versions. Record licenses and attribution for code, tools, and bundled assets.
6. Run a small end-to-end vertical slice on the target platform before building more content.

## Planning and game design

- [404Valentine/valentech-anvil](https://github.com/404Valentine/valentech-anvil) — GDD-to-Unity pipeline tool — loads a Game Design Document, extracts game systems with semantic category colors, and lets Claude propose feature checklists. · PowerShell · license not detected
- [Ada-Rhodes/micro-Game-Design-Document](https://github.com/Ada-Rhodes/micro-Game-Design-Document) — micro Game Design Document, a Free Tool for Teaching the Game Design Elemental Tetrad published under CC0. For details see "Evaluation Of a Novel… · CC0-1.0
- [alperunlu07/GDDForge](https://github.com/alperunlu07/GDDForge) — Next-generation Game Design Document (GDD) authoring tool for indie developers and studios. · TypeScript · license not detected
- [colin0923/Arshis-Game-Design-Pro-v1.2.3](https://github.com/colin0923/Arshis-Game-Design-Pro-v1.2.3) — Professional game design tool for generating 90% complete commercial-grade game design documents. 26 core modules covering pricing, publishing… · MIT
- [dialogic-godot/dialogic](https://github.com/dialogic-godot/dialogic) — 💬 Create Dialogs, Visual Novels, RPGs, and manage Characters with Godot to create your Game! · GDScript · MIT
- [eXGhsRBm/gdd-manager](https://github.com/eXGhsRBm/gdd-manager) — Desktop tool for managing Game Design Document projects: generate, validate, search, and navigate Markdown documentation · C++ · MIT
- [fundevme/SoloDev-Toolbox](https://github.com/fundevme/SoloDev-Toolbox) — A simple app that can help you plan and manage your game. Free forever. Built in moodboard, GDD (Game design Document) and more. App is available on… · JavaScript · MIT
- [galaxykate/tracery](https://github.com/galaxykate/tracery) — Tracery: a story-grammar generation library for javascript · JavaScript · Apache-2.0
- [inkle/ink](https://github.com/inkle/ink) — inkle's open source scripting language for writing interactive narrative. · C# · MIT
- [inkle/inky](https://github.com/inkle/inky) — An editor for ink: inkle's narrative scripting language · JavaScript · license not detected
- [miguelrsgoncalves/gdd_latex_template](https://github.com/miguelrsgoncalves/gdd_latex_template) — GDD LaTeX Template is the open source template for your Game Design Documents (GDD)! This template was built to stay out of your way while providing… · TeX · MIT
- [nathanhoad/godot_dialogue_manager](https://github.com/nathanhoad/godot_dialogue_manager) — A powerful nonlinear dialogue system for Godot · GDScript · MIT
- [patterkit/patter](https://github.com/patterkit/patter) — Editor, compiler, and runtimes for writing and running dialogue flows for videogames. · TypeScript · MIT
- [Sahib1231241242123/gdd-unity-technical-spec-agent](https://github.com/Sahib1231241242123/gdd-unity-technical-spec-agent) — CLI tool that converts Game Design Documents into production-oriented Unity technical specifications. · Python · license not detected
- [Simhyeon/gdengine](https://github.com/Simhyeon/gdengine) — Game design engine, the game design documents creation tool · Rust · license not detected
- [suvrajits/AI-GameDesign-AgenticDirector](https://github.com/suvrajits/AI-GameDesign-AgenticDirector) — AI-GameDesign-AgenticDirector is an AI-powered tool for generating and managing Game Design Documents, narratives, mechanics, and gameplay systems. It… · HTML · GPL-3.0
- [Thaelith/open-game-mechanics-dataset](https://github.com/Thaelith/open-game-mechanics-dataset) — Engine-agnostic, machine-readable dataset of game mechanics for developers, designers, researchers, students, and AI-assisted workflows. · JavaScript · NOASSERTION
- [YarnSpinnerTool/YarnSpinner](https://github.com/YarnSpinnerTool/YarnSpinner) — The core compiler and engine-agnostic components for Yarn Spinner, the friendly dialogue tool. · C# · MIT

## Engines and frameworks

- [2calucas/KSE](https://github.com/2calucas/KSE) — KSE is a modular, fully documented 3D game engine project designed to explore and replicate the internal architecture, tools, and systems used in… · C# · NOASSERTION
- [4ian/GDevelop](https://github.com/4ian/GDevelop) — 🎮 Open-source, cross-platform 2D/3D/multiplayer game engine designed for everyone. · JavaScript · NOASSERTION
- [alaingalvan/image-editor-effects](https://github.com/alaingalvan/image-editor-effects) — 💎 A WebGL example of image adjustment / effects shaders found in Photoshop, other image editors and game engines. · TypeScript · Unlicense
- [axmolengine/axmol](https://github.com/axmolengine/axmol) — Open-source C++ game engine with Lua for 2D and 3D games across mobile, desktop, WebAssembly, and Xbox (UWP). · C++ · NOASSERTION
- [bevyengine/bevy](https://github.com/bevyengine/bevy) — A refreshingly simple data-driven game engine built in Rust · Rust · Apache-2.0
- [bladecoder/bladecoder-adventure-engine](https://github.com/bladecoder/bladecoder-adventure-engine) — Classic point and click adventure game engine and editor · Java · Apache-2.0
- [boardgameio/boardgame.io](https://github.com/boardgameio/boardgame.io) — State Management and Multiplayer Networking for Turn-Based Games · TypeScript · MIT
- [bryanedds/Nu](https://github.com/bryanedds/Nu) — Repository hosting the functional Nu Game Engine and related projects. · F# · NOASSERTION
- [ChessMax/awesome-game-engines](https://github.com/ChessMax/awesome-game-engines) — The list of awesome game engines for everything😎 · Markdown · MIT
- [Circular-Studios/Dash](https://github.com/Circular-Studios/Dash) — A free and open 3D game engine written in D. · D · MIT
- [cocoatoucher/Glide](https://github.com/cocoatoucher/Glide) — Game engine for making 2d games on iOS, macOS and tvOS, with practical examples and tutorials · Swift · MIT
- [cocos/cocos-engine](https://github.com/cocos/cocos-engine) — Cocos simplifies game creation and distribution with Cocos Creator, a free, open-source, cross-platform game engine. Empowering millions of developers… · C++ · NOASSERTION
- [defold/defold](https://github.com/defold/defold) — Defold is a completely free to use game engine for development of desktop, console, mobile and web games. · C++ · NOASSERTION
- [erincatto/box2d](https://github.com/erincatto/box2d) — Box2D is a 2D physics engine for games · C · MIT
- [flame-engine/flame](https://github.com/flame-engine/flame) — A Flutter based game engine. · Dart · MIT
- [FlaxEngine/FlaxEngine](https://github.com/FlaxEngine/FlaxEngine) — Flax Engine – multi-platform 3D game engine · C++ · NOASSERTION
- [FosterFramework/Foster](https://github.com/FosterFramework/Foster) — A small C# game framework · C# · MIT
- [FyroxEngine/Fyrox](https://github.com/FyroxEngine/Fyrox) — 3D and 2D game engine written in Rust · Rust · MIT
- [godotengine/godot](https://github.com/godotengine/godot) — Godot Engine – Multi-platform 2D and 3D game engine · C++ · MIT
- [hajimehoshi/ebiten](https://github.com/hajimehoshi/ebiten) — A dead simple 2D game engine for Go · Go · Apache-2.0
- [Is-Daouda/is-Engine](https://github.com/Is-Daouda/is-Engine) — C++, SDL 2 and SFML game engine that allows to create games on Nintendo Switch, Web (HTML 5), Mobile and PC. · C · Zlib
- [JohnClarking/CoolEngines](https://github.com/JohnClarking/CoolEngines) — Awesome list for open source graphic & game engine. · GPL-3.0
- [kitao/pyxel](https://github.com/kitao/pyxel) — A retro game engine for Python · Rust · NOASSERTION
- [LambdaHack/LambdaHack](https://github.com/LambdaHack/LambdaHack) — Haskell game engine library for roguelike dungeon crawlers; please offer feedback, e.g., after trying out the sample game with the web frontend at · Haskell · BSD-3-Clause
- [love2d/love](https://github.com/love2d/love) — LÖVE is an awesome 2D game framework for Lua. · C++ · NOASSERTION
- [nem0/LumixEngine](https://github.com/nem0/LumixEngine) — 3D C++ Game Engine - yet another open source game engine · C++ · MIT
- [NeoAxis/NeoAxisEngine](https://github.com/NeoAxis/NeoAxisEngine) — A versatile game engine designed for creating video games and real-time apps. · C# · NOASSERTION
- [not-fl3/macroquad](https://github.com/not-fl3/macroquad) — Cross-platform game engine in Rust. · Rust · Apache-2.0
- [ObEngine/ObEngine](https://github.com/ObEngine/ObEngine) — 2D Game Engine with Lua Scripting made on top of SFML ! · C++ · MIT
- [OpenRA/OpenRA](https://github.com/OpenRA/OpenRA) — Open Source real-time strategy game engine for early Westwood games such as Command & Conquer: Red Alert written in C# using SDL and OpenGL. Runs on… · C# · GPL-3.0
- [OpenXRay/xray-16](https://github.com/OpenXRay/xray-16) — Improved version of the X-Ray Engine, the game engine used in the world-famous S.T.A.L.K.E.R. game series by GSC Game World. Join OpenXRay! ;) · C++ · NOASSERTION
- [phaserjs/phaser](https://github.com/phaserjs/phaser) — Phaser is a fun, free and fast 2D game framework for making HTML5 games for desktop and mobile web browsers, supporting Canvas and WebGL rendering. · JavaScript · MIT
- [Planimeter/game-engine-2d](https://github.com/Planimeter/game-engine-2d) — Planimeter Game Engine 2D - LÖVE-based game engine for Lua · Lua · MIT
- [sbiermanlytle/iioEngine](https://github.com/sbiermanlytle/iioEngine) — iio Engine: A JavaScript game engine for HTML5 Canvas · JavaScript · license not detected
- [sdslabs/Rootex](https://github.com/sdslabs/Rootex) — An advanced C++ 3D game engine powering an in-production game yet to be announced · C++ · NOASSERTION
- [skylicht-lab/skylicht-engine](https://github.com/skylicht-lab/skylicht-engine) — Skylicht Engine is C++ Game Engine based on Irrlicht 3D. And my goal is to create a high-performance and lightweight Game Framework that can seamlessly… · C++ · MIT
- [vanyle/vectarine](https://github.com/vanyle/vectarine) — A free cross-platform game engine focusing on fast prototyping and having fun with Luau scripting · Luau · MIT
- [willtobyte/carimbo](https://github.com/willtobyte/carimbo) — A 2D game engine developed in modern C++ using SDL, an Entity-Component-System (ECS) architecture, miniaudio, and Box2D. It features Lua scripting and… · C++ · MIT

## Starter projects, samples, and complete games

- [BharathVishal/Singleton-Implementation-Unity](https://github.com/BharathVishal/Singleton-Implementation-Unity) — A sample project explaining the usage of singleton object to hold global game state. · C# · Apache-2.0
- [campkitchenus-maker/godot-supply-tank](https://github.com/campkitchenus-maker/godot-supply-tank) — Godot 4 addon: SupplyTank, SupplyBar and SupplyPlan for water, fuel and food meters, with a playable example game and 47 headless tests. MIT. · GDScript · NOASSERTION
- [ChadCSong/Unity3DCarGameSample](https://github.com/ChadCSong/Unity3DCarGameSample) — This is a project for Unity3D learning. A racing car game sample. · C# · license not detected
- [chickensoft-games/GodotGame](https://github.com/chickensoft-games/GodotGame) — C# game template for Godot 4 with debug launch configurations, testing (locally and on CI/CD), code coverage, dependency update checks, and spell check… · C# · MIT
- [dmaulikr/unity-shooting-game](https://github.com/dmaulikr/unity-shooting-game) — sample project · Objective-C · license not detected
- [Ferbdi/BlissfulMaze](https://github.com/Ferbdi/BlissfulMaze) — Sample game project on Unity · C# · MIT
- [gongminmin/KlayGE](https://github.com/gongminmin/KlayGE) — KlayGE is a cross-platform open source game engine with plugin-based architecture. · C++ · GPL-2.0
- [jameswhiteman/JW-Game-Engine](https://github.com/jameswhiteman/JW-Game-Engine) — An open source game creation tools to aid in creating a Java game, giving valuable tools such as a level editor, graphics management, and sound management. · Java · license not detected
- [Jibby-Games/Flappy-Backend](https://github.com/Jibby-Games/Flappy-Backend) — The backend microservices for the open source game Flappy Race · Shell · license not detected
- [kalonlang/dreams-found-among-flowers](https://github.com/kalonlang/dreams-found-among-flowers) — ???? / Dreams Found Among Flowers - complete Godot game source · GDScript · license not detected
- [keijiro/LowLevelDigger](https://github.com/keijiro/LowLevelDigger) — Low-Level 2D Physics (Unity 6.3) mini game sample project · C# · Unlicense
- [Manick94/Game-Projects](https://github.com/Manick94/Game-Projects) — Unity Source Codes and resources for the sample game projects · license not detected
- [MAntoniS/Unity-PracticeProject-CrystalThief](https://github.com/MAntoniS/Unity-PracticeProject-CrystalThief) — A 2D sample game with basic AI behaviors. · C# · license not detected
- [mq003at/The-Return](https://github.com/mq003at/The-Return) — A sample game to test Unity framework · C# · license not detected
- [msrgo96/ProjectVR](https://github.com/msrgo96/ProjectVR) — Unity C# Scripts for VR game sample · license not detected
- [NomadWithoutAHome/Buckshot-Roulette-Decompiled](https://github.com/NomadWithoutAHome/Buckshot-Roulette-Decompiled) — Complete decompiled source code of the indie horror game Buckshot Roulette, extracted using Godot RE Tools. This project contains the full game source… · license not detected
- [opentestdriveunlimited/OpenTestDriveUnlimited](https://github.com/opentestdriveunlimited/OpenTestDriveUnlimited) — Open source port of Test Drive Unlimited (2006) · C++ · license not detected
- [Patchthesock/GSRealTimeTestTool](https://github.com/Patchthesock/GSRealTimeTestTool) — GameSparks Real Time Testing Tool · C# · MIT
- [Pico-Developer/PlatformSamples-Unity-SpaceArenaParty](https://github.com/Pico-Developer/PlatformSamples-Unity-SpaceArenaParty) — Space Arena Party is a multiplayer social game template project developed for the PICO platform. In this project, players can enter different rooms and… · C# · MIT
- [pmgl/microstudio](https://github.com/pmgl/microstudio) — Free, open source game engine online · JavaScript · MIT
- [PrimeEagle/Text101](https://github.com/PrimeEagle/Text101) — [Archived] Unity sample project from Udemy. · C# · Unlicense
- [SaiV-05-18/unity-2d-game](https://github.com/SaiV-05-18/unity-2d-game) — Sample project in Unity. · MIT
- [shhridoy/2D-Racing-Game](https://github.com/shhridoy/2D-Racing-Game) — Unity 2d racing game sample project for Android Mobile with C# · ASP · license not detected
- [shubhratchaursiya/Endless_Runner_Game_Unity](https://github.com/shubhratchaursiya/Endless_Runner_Game_Unity) — 🎮 Projects and scripts exploring game development concepts using Unity Engine and C#. Includes sample games, mechanics, and learning exercises. · C# · license not detected
- [theodorton/UFO-Game](https://github.com/theodorton/UFO-Game) — Sample project in Unity · C# · license not detected
- [tiltfive/sample-unity-brawler](https://github.com/tiltfive/sample-unity-brawler) — "Battle Brawl" sample game project for Unity with local multi-player · C# · Apache-2.0
- [trflorian/rts-selection-circle-demo](https://github.com/trflorian/rts-selection-circle-demo) — A small demo scene to showcase an RTS selection circle shader with configurable radius and thickness · GDScript · MIT
- [UnityFukuoka/UnityFukuoka05-Sample-CoinGame](https://github.com/UnityFukuoka/UnityFukuoka05-Sample-CoinGame) — Sample Project for Unity Fukuoka 05 · C# · license not detected

## Architecture, ECS, and scripting

- [aframevr/aframe](https://github.com/aframevr/aframe) — :a: Web framework for building virtual reality experiences. · JavaScript · MIT
- [ATHellboy/SampleProject-FightingGame](https://github.com/ATHellboy/SampleProject-FightingGame) — A sample project designed to demonstrate advanced C# coding practices and architectural expertise in Unity. This showcase serves as a practical example… · C# · MIT
- [BobbyAnguelov/Esoterica](https://github.com/BobbyAnguelov/Esoterica) — Esoterica Engine · C++ · NOASSERTION
- [cfnptr/garden](https://github.com/cfnptr/garden) — An open source, cross platform game engine written in C++ with Vulkan API rendering backend · C++ · Apache-2.0
- [ckendal3/Unity-ECS-Example](https://github.com/ckendal3/Unity-ECS-Example) — This repo is a testing ground for Unity's ECS as it releases. Current Entities: 0.2.0 preview.13 · C# · MIT
- [Doraku/DefaultEcs](https://github.com/Doraku/DefaultEcs) — Entity Component System framework aiming for syntax and usage simplicity with maximum performance for game development. · C# · MIT-0
- [doriaxengine/doriax](https://github.com/doriaxengine/doriax) — Game engine for 2D and 3D projects with entity component system (ECS) and data-oriented design · C++ · MIT
- [Dreaming381/lsss-wip](https://github.com/Dreaming381/lsss-wip) — Latios Space Shooter Sample - an open Unity DOTS Project using the Latios Framework · C# · MIT
- [friflo/Friflo.Engine.ECS](https://github.com/friflo/Friflo.Engine.ECS) — High-performance C# ECS · C# · MIT
- [fubark/cyber](https://github.com/fubark/cyber) — Fast and concurrent scripting. · Zig · MIT
- [genaray/Arch](https://github.com/genaray/Arch) — A high-performance C# based Archetype & Chunks Entity Component System (ECS) with optional multithreading. · C# · Apache-2.0
- [hmans/miniplex](https://github.com/hmans/miniplex) — A 👩‍💻 developer-friendly entity management system for 🕹 games and similarly demanding applications, based on 🛠 ECS architecture. · TypeScript · MIT
- [i42output/neoGFX](https://github.com/i42output/neoGFX) — Cross-platform GPU-oriented C++ application/game framework · C++ · GPL-3.0
- [increpare/PuzzleScript](https://github.com/increpare/PuzzleScript) — Open Source HTML5 Puzzle Game Engine · JavaScript · MIT
- [InvadingOctopus/octopuskit](https://github.com/InvadingOctopus/octopuskit) — 2D ECS game engine in 100% Swift + SwiftUI for iOS, macOS, tvOS · Swift · Apache-2.0
- [jmorton06/Lumos](https://github.com/jmorton06/Lumos) — Cross-Platform C++ 2D/3D game engine · C++ · MIT
- [kovacsv/VisualScriptEngine](https://github.com/kovacsv/VisualScriptEngine) — A C++ visual scripting engine designed for embedding. · C++ · MIT
- [LastOliveGames/becsy](https://github.com/LastOliveGames/becsy) — A multithreaded Entity Component System (ECS) for TypeScript and JavaScript, inspired by ECSY and bitecs. · TypeScript · MIT
- [NateTheGreatt/bitECS](https://github.com/NateTheGreatt/bitECS) — Flexible, minimal, data-oriented ECS library for Typescript · TypeScript · MPL-2.0
- [nidorx/ecs-lib](https://github.com/nidorx/ecs-lib) — Tiny and easy to use ECS (Entity Component System) library for game programming · TypeScript · MIT
- [PanosK92/SpartanEngine](https://github.com/PanosK92/SpartanEngine) — A game engine with a fully bindless, GPU-driven renderer featuring real-time path-traced global illumination, hardware ray tracing, and a physics… · C++ · NOASSERTION
- [phisko/kengine](https://github.com/phisko/kengine) — Game engine with an Entity-Component-System (ECS) architecture. Focus on ease-of-use, runtime extensibility and compile-time type safety. · C++ · MIT
- [r-lyeh-archived/scriptorium](https://github.com/r-lyeh-archived/scriptorium) — :scroll: Game Scripting Languages benchmarked · C · Unlicense
- [SanderMertens/ecs-faq](https://github.com/SanderMertens/ecs-faq) — Frequently asked questions about Entity Component Systems · license not detected
- [SanderMertens/flecs](https://github.com/SanderMertens/flecs) — A fast entity component system (ECS) for C & C++ · C · NOASSERTION
- [skypjack/entt](https://github.com/skypjack/entt) — Gaming meets modern C++ - a fast and reliable entity component system (ECS) and much more · C++ · MIT

## Gameplay systems, physics, and AI

- [antzGames/Jolt-libGDX-vs-Godot](https://github.com/antzGames/Jolt-libGDX-vs-Godot) — A simple performance test that compares Jolt Physics on libGDX and Godot. · JavaScript · license not detected
- [anuraghazra/Verly.js](https://github.com/anuraghazra/Verly.js) — :red_circle::wavy_dash::large_blue_circle::wavy_dash::black_circle: Easy to integrate Verlet physics engine. :link: · JavaScript · MIT
- [BeRo1985/kraft](https://github.com/BeRo1985/kraft) — Kraft Physics Engine is an open source Object Pascal physics engine library that can be used in 3D games. · Pascal · license not detected
- [bulletphysics/bullet3](https://github.com/bulletphysics/bullet3) — Bullet Physics SDK: real-time collision detection and multi-physics simulation for VR, games, visual effects, robotics, machine learning etc. · C++ · NOASSERTION
- [DanielChappuis/reactphysics3d](https://github.com/DanielChappuis/reactphysics3d) — Open source C++ physics engine library in 3D · C++ · Zlib
- [galacean/engine](https://github.com/galacean/engine) — A typescript interactive engine, support 2D, 3D, animation, physics, built on WebGL and glTF. · TypeScript · MIT
- [Genbox/VelcroPhysics](https://github.com/Genbox/VelcroPhysics) — High performance 2D collision detection system with realistic physics responses. · C# · MIT
- [godot-extended-libraries/navigation_server_playground](https://github.com/godot-extended-libraries/navigation_server_playground) — Testing using 3.2 Godot Engine navigation server · GDScript · MIT
- [gurkenlabs/litiengine](https://github.com/gurkenlabs/litiengine) — LITIENGINE 🕹 The Java 2D game engine. · Java · MIT
- [hugoscurti/hierarchical-pathfinding](https://github.com/hugoscurti/hierarchical-pathfinding) — Implementation of Near-Optimal Hierarchical Pathfinding (HPA*) algorithm in Unity, tested with maps from Dragon Age: Origins · C# · MIT
- [ikpil/Box2D.NET](https://github.com/ikpil/Box2D.NET) — Box2D.NET - a C# port of Box2D, is a 2D physics engine for games, .NET, Unity3D, servers · C# · MIT
- [ikpil/DotRecast](https://github.com/ikpil/DotRecast) — DotRecast - a C# port of Recast & Detour, Industry-standard navigation mesh toolset for .NET, Unity3D, games, servers · C# · Zlib
- [Ivanfs8/Navigation-Test](https://github.com/Ivanfs8/Navigation-Test) — Godot navigation tests and experiments with multiple addons · GDScript · MIT
- [jrouwe/JoltPhysics.js](https://github.com/jrouwe/JoltPhysics.js) — Port of JoltPhysics to JavaScript using emscripten · C++ · MIT
- [jrouwe/JoltPhysics](https://github.com/jrouwe/JoltPhysics) — A multi core friendly rigid body physics and collision detection library. Written in C++. Suitable for games and VR applications. Used by Horizon… · C++ · MIT
- [liabru/matter-js](https://github.com/liabru/matter-js) — a 2D rigid body physics engine for the web ▲● ■ · JavaScript · MIT
- [Mani212005/GameTester](https://github.com/Mani212005/GameTester) — Interactive 3D Game Physics & Collision Simulator built with Three.js, Cannon-es, and Playwright automated visual test runners. · TypeScript · license not detected
- [mchancan/citylearn](https://github.com/mchancan/citylearn) — Official implementation of paper "CityLearn: Diverse Real-World Environments for Sample-Efficient Navigation Policy Learning" by M. Chancán (ICRA 2020)… · C# · MIT
- [milcktoast/particulate-js](https://github.com/milcktoast/particulate-js) — Particle physics micro library. · JavaScript · MIT
- [noonat/intersect](https://github.com/noonat/intersect) — An explanation of 2D collision tests in JavaScript · TypeScript · Zlib
- [notgiven688/jitterphysics2](https://github.com/notgiven688/jitterphysics2) — Fast, simple to use, and dependency-free physics engine written in C# with a clear and user-friendly API. · C# · MIT
- [piqnt/planck.js](https://github.com/piqnt/planck.js) — 2D JavaScript Physics Engine · TypeScript · MIT
- [pmndrs/react-spring](https://github.com/pmndrs/react-spring) — ✌️ A spring physics based React animation library · TypeScript · MIT
- [projectchrono/chrono](https://github.com/projectchrono/chrono) — High-performance C++ library for multiphysics and multibody dynamics simulations · C++ · BSD-3-Clause
- [RandyGaul/cute_headers](https://github.com/RandyGaul/cute_headers) — Collection of cross-platform one-file C/C++ libraries with no dependencies, primarily used for games · C · NOASSERTION
- [rearming/circular-obstacle-pathfinding](https://github.com/rearming/circular-obstacle-pathfinding) — Implementation of Circular Obstacle Pathfinding (also with A-Star). Integration of Optimal Reciprocal Collision Avoidance. · C# · license not detected
- [recastnavigation/recastnavigation](https://github.com/recastnavigation/recastnavigation) — Industry-standard navigation-mesh toolset for games · C++ · Zlib
- [Sal93Git/Unity-Game-Physics-Engine-with-Pathfinding-and-Map-Generator](https://github.com/Sal93Git/Unity-Game-Physics-Engine-with-Pathfinding-and-Map-Generator) — This project showcases a custom-built 2D physics engine integrated with A* and Dijkstra's algorithms for optimized pathfinding. Additionally, a custom… · C# · license not detected
- [schteppe/p2.js](https://github.com/schteppe/p2.js) — JavaScript 2D physics library · JavaScript · NOASSERTION
- [timi-liuliang/echo](https://github.com/timi-liuliang/echo) — A New Cross-Platform 2D 3D Game Engine · C++ · MIT
- [vishwagw/Sky-Sim-drone-simulator-3.0](https://github.com/vishwagw/Sky-Sim-drone-simulator-3.0) — An open source drone flight simulator that runs on the web browser and test autonomous drones. Easy to use. version3.0. HITL is included with latest… · C++ · MIT
- [xissburg/edyn](https://github.com/xissburg/edyn) — Edyn is a real-time physics engine organized as an ECS. · C++ · MIT

## Rendering, graphics, and shaders

- [alaingalvan/CrossShader](https://github.com/alaingalvan/CrossShader) — ⚔️ A tool for cross compiling shaders. Convert between GLSL, HLSL, Metal Shader Language, or older versions of GLSL. · C++ · MIT
- [AntonPalmqvist/physically-based-api](https://github.com/AntonPalmqvist/physically-based-api) — A database of physically based values for CG artists. · JavaScript · CC0-1.0
- [bkaradzic/bgfx](https://github.com/bkaradzic/bgfx) — Cross-platform, graphics API agnostic, "Bring Your Own Engine/Framework" style rendering library. · C++ · BSD-2-Clause
- [CodyJasonBennett/four](https://github.com/CodyJasonBennett/four) — A tiny Three.js-style library for WebGL, WebGPU, and GPU compute. · TypeScript · MIT
- [dfranx/SHADERed](https://github.com/dfranx/SHADERed) — Lightweight, cross-platform & full-featured shader IDE · C++ · MIT
- [DiligentGraphics/DiligentEngine](https://github.com/DiligentGraphics/DiligentEngine) — A modern cross-platform low-level graphics library and rendering framework · Batchfile · Apache-2.0
- [EQMG/Acid](https://github.com/EQMG/Acid) — A high speed C++17 Vulkan game engine · C++ · MIT
- [eug/awesome-opengl](https://github.com/eug/awesome-opengl) — A curated list of awesome OpenGL libraries, debuggers and resources. · license not detected
- [gfx-rs/wgpu](https://github.com/gfx-rs/wgpu) — A cross-platform, safe, pure-Rust graphics API. · Rust · Apache-2.0
- [google/filament](https://github.com/google/filament) — Filament is a real-time physically based rendering engine for Android, iOS, Windows, Linux, macOS, WebGPU, and WebGL2 · C++ · Apache-2.0
- [gpuweb/gpuweb](https://github.com/gpuweb/gpuweb) — Where the GPU for the Web work happens! · Bikeshed · NOASSERTION
- [jonobr1/two.js](https://github.com/jonobr1/two.js) — A renderer agnostic two-dimensional drawing api for the web · JavaScript · MIT
- [jslee02/awesome-graphics-libraries](https://github.com/jslee02/awesome-graphics-libraries) — :sunglasses: A curated list of 3D graphics libraries and resources · Python · CC0-1.0
- [KhronosGroup/Vulkan-Samples](https://github.com/KhronosGroup/Vulkan-Samples) — One stop solution for all Vulkan samples · C++ · Apache-2.0
- [kool-engine/kool](https://github.com/kool-engine/kool) — A Vulkan / WebGPU / OpenGL engine for Desktop JVM, Android and Javascript written in Kotlin · Kotlin · Apache-2.0
- [KTStephano/StratusGFX](https://github.com/KTStephano/StratusGFX) — Realtime 3D rendering engine · C++ · MPL-2.0
- [lettier/3d-game-shaders-for-beginners](https://github.com/lettier/3d-game-shaders-for-beginners) — 🎮 A step-by-step guide to implementing SSAO, depth of field, lighting, normal mapping, and more for your 3D game. · C++ · license not detected
- [LukasBanana/LLGL](https://github.com/LukasBanana/LLGL) — Low Level Graphics Library (LLGL) is a thin abstraction layer for the modern graphics APIs OpenGL, Direct3D, Vulkan, and Metal · C++ · BSD-3-Clause
- [LWJGL/lwjgl3](https://github.com/LWJGL/lwjgl3) — LWJGL is a Java library that enables cross-platform access to popular native APIs useful in the development of graphics (OpenGL, Vulkan, bgfx), audio… · Java · BSD-3-Clause
- [microsoft/DirectXTK](https://github.com/microsoft/DirectXTK) — The DirectX Tool Kit (aka DirectXTK) is a collection of helper classes for writing DirectX 11.x code in C++ · C++ · MIT
- [OGRECave/ogre](https://github.com/OGRECave/ogre) — high-performance rendering backend (C++, Python, C#, Java) · C++ · MIT
- [opentk/opentk](https://github.com/opentk/opentk) — The Open Toolkit library is a fast, low-level C# wrapper for OpenGL, OpenAL & OpenCL. It also includes windowing, mouse, keyboard and joystick input… · C# · NOASSERTION
- [OxygenButBeta/Ballistic-Engine](https://github.com/OxygenButBeta/Ballistic-Engine) — A from-scratch C#/.NET 9 game engine with a DirectX 12 + hardware ray tracing renderer (Lumen-style GI, GPU-driven), a full ImGui editor, Unity-style… · C# · MIT
- [patriciogonzalezvivo/thebookofshaders](https://github.com/patriciogonzalezvivo/thebookofshaders) — Step-by-step guide through the abstract and complex universe of Fragment Shaders. · GLSL · NOASSERTION
- [pixijs/pixijs](https://github.com/pixijs/pixijs) — The HTML5 Creation Engine: Create beautiful digital content with the fastest, most flexible 2D WebGL renderer. · TypeScript · MIT
- [playcanvas/engine](https://github.com/playcanvas/engine) — Open-source web graphics engine built on WebGPU and WebGL2 · JavaScript · MIT
- [shader-park/shader-park-core](https://github.com/shader-park/shader-park-core) — A JavaScript library for creating real-time 2D and 3D shaders. JS -> Shader. https://shaderpark.com/ https://twitter.com/shaderpark · JavaScript · MIT
- [vulkano-rs/vulkano](https://github.com/vulkano-rs/vulkano) — Safe and rich Rust wrapper around the Vulkan API · Rust · Apache-2.0

## Art, animation, and 3D creation

- [a1studmuffin/SpaceshipGenerator](https://github.com/a1studmuffin/SpaceshipGenerator) — A Blender script to procedurally generate 3D spaceships · Python · NOASSERTION
- [andstor/voxelizer](https://github.com/andstor/voxelizer) — :space_invader: Voxelization of 3D models · JavaScript · MIT
- [animate-css/animate.css](https://github.com/animate-css/animate.css) — 🍿 A cross-browser library of CSS animations. As easy to use as an easy thing. · CSS · NOASSERTION
- [armory3d/armorpaint](https://github.com/armory3d/armorpaint) — Graphics Creation Tools · C · NOASSERTION
- [armory3d/armory](https://github.com/armory3d/armory) — 3D Engine with Blender Integration · C++ · Zlib
- [AssiamahS/opengym3d](https://github.com/AssiamahS/opengym3d) — Open-source 3D exercise animation library — Blender renders in CI, Three.js viewer on Pages · Python · MIT
- [Bingeljell/image-to-3dlab](https://github.com/Bingeljell/image-to-3dlab) — AssetFurnace: the most complete open-source image-to-3D pipeline (Oct 2026). Prompt or picture → textured, rigged, animated game character, locally on… · Python · Apache-2.0
- [Blackvoxel/Blackvoxel](https://github.com/Blackvoxel/Blackvoxel) — Blackvoxel Video Game · C++ · GPL-3.0
- [blender/blender](https://github.com/blender/blender) — Official mirror of Blender · C++ · NOASSERTION
- [BoQsc/world-transvoxel-sandbox-archived-superseded](https://github.com/BoQsc/world-transvoxel-sandbox-archived-superseded) — Validation sandbox for World Transvoxel Addon — voxel terrain visual, gameplay, and scale testing in Godot before game development. · C++ · NOASSERTION
- [daybrush/scenejs](https://github.com/daybrush/scenejs) — 🎬 Scene.js is JavaScript & CSS timeline-based animation library · TypeScript · MIT
- [devanshutak25/3d-resources](https://github.com/devanshutak25/3d-resources) — Curated, CC0 reference hub for 3D, VFX, and game dev. 4,800+ tools, assets, and tutorials across 12 sections. Searchable, filterable, free. · JavaScript · CC0-1.0
- [greensock/GSAP](https://github.com/greensock/GSAP) — GSAP (GreenSock Animation Platform), a JavaScript animation library for the modern web · JavaScript · license not detected
- [guillaumeblanc/ozz-animation](https://github.com/guillaumeblanc/ozz-animation) — Open source c++ skeletal animation library and toolset · C++ · NOASSERTION
- [guillaumechereau/goxel](https://github.com/guillaumechereau/goxel) — Goxel: Free and Open Source 3D Voxel Editor · C++ · GPL-3.0
- [konvajs/konva](https://github.com/konvajs/konva) — Konva.js is an HTML5 Canvas JavaScript framework for interactive graphics, design editors, whiteboards, and diagrams. Scene graph with events, drag and… · TypeScript · NOASSERTION
- [luanti-org/luanti](https://github.com/luanti-org/luanti) — Luanti (formerly Minetest) is an open source voxel game-creation platform with easy modding and game creation · C++ · NOASSERTION
- [MovingBlocks/Terasology](https://github.com/MovingBlocks/Terasology) — Terasology - open source voxel world · Java · Apache-2.0
- [openfl/actuate](https://github.com/openfl/actuate) — Actuate is a flexible, fast "tween" library for animations in Haxe · Haxe · MIT
- [Orama-Interactive/Pixelorama](https://github.com/Orama-Interactive/Pixelorama) — Unleash your creativity with Pixelorama, a powerful and accessible open-source pixel art multitool. Whether you want to create sprites, tiles… · GDScript · MIT
- [papercraftgames/folded-paper-engine](https://github.com/papercraftgames/folded-paper-engine) — A custom Blender-to-Godot addon that makes level and gameplay creation as easy as a few clicks! · GDScript · MIT
- [pawsgineer/b3d_paws_bakery](https://github.com/pawsgineer/b3d_paws_bakery) — PAWS Bakery is a Blender add-on that speeds up the Texture Baking pipeline for Game-Ready assets · Python · GPL-3.0
- [ploikmjr/tripo-claude-blender-pipeline](https://github.com/ploikmjr/tripo-claude-blender-pipeline) — Production-grade CLAUDE.md pipeline to generate, quad-retopologize, auto-rig, and validate game-ready 3D assets from 1 or 4 images using Claude, Tripo… · MIT
- [RodZill4/material-maker](https://github.com/RodZill4/material-maker) — A procedural textures authoring and 3D model painting tool based on the Godot game engine · GDScript · MIT
- [sketchpunklabs/ossos](https://github.com/sketchpunklabs/ossos) — Webbased Character Animation System · TypeScript · MIT
- [Themoyouknow13/awesome-blender-starter-suite](https://github.com/Themoyouknow13/awesome-blender-starter-suite) — Free-first Blender jump-off kit: CC0 assets, top addons, game-dev tools, and pipelines to Godot, Unity, and ComfyUI · PowerShell · CC0-1.0
- [tweenjs/tween.js](https://github.com/tweenjs/tween.js) — JavaScript/TypeScript animation engine · TypeScript · NOASSERTION
- [UPBGE/upbge](https://github.com/UPBGE/upbge) — UPBGE, the best integrated game engine in Blender · C++ · NOASSERTION

## Levels, maps, and world building

- [adrien-bon/bevy_ecs_tiled](https://github.com/adrien-bon/bevy_ecs_tiled) — Helpers for working with 2D tilemaps created with the Tiled map editor · Rust · MIT
- [Amulet-Team/Amulet-Map-Editor](https://github.com/Amulet-Team/Amulet-Map-Editor) — A Minecraft world editor and converter that supports all versions since Java 1.12 and Bedrock 1.7. · Python · NOASSERTION
- [Azgaar/Fantasy-Map-Generator](https://github.com/Azgaar/Fantasy-Map-Generator) — Web application generating interactive and highly customizable maps · TypeScript · NOASSERTION
- [Cammin/LDtkToUnity](https://github.com/Cammin/LDtkToUnity) — Unity importer for the LDtk level editor · C# · MIT
- [codereader/DarkRadiant](https://github.com/codereader/DarkRadiant) — DarkRadiant is the map editor for The Dark Mod and other idTech4/Doom3-based games · C++ · NOASSERTION
- [deepnight/ldtk](https://github.com/deepnight/ldtk) — Modern, lightweight and efficient 2D level editor · Haxe · MIT
- [Garux/netradiant-custom](https://github.com/Garux/netradiant-custom) — The open-source, cross-platform level editor for id Tech based games. · C++ · NOASSERTION
- [Ggross98/Unity-Hashi](https://github.com/Ggross98/Unity-Hashi) — Hashiwokakero (Bridges) game made with Unity. Level editor and save system are provided. · C# · license not detected
- [greysquirr3l/morgan-bevy](https://github.com/greysquirr3l/morgan-bevy) — Professional 3D level editor for Bevy game engine with procedural generation (BSP, WFC), transform gizmos, asset management, and multi-format export… · TypeScript · NOASSERTION
- [H2xDev/GodotVMF](https://github.com/H2xDev/GodotVMF) — Run Valve Hammer (VMF) maps in Godot Engine · GDScript · MIT
- [Halatnikov/linum-framework](https://github.com/Halatnikov/linum-framework) — Linum Framework is a Sonic framework for Construct 2 with level editor, online multiplayer and skins · JavaScript · license not detected
- [jbuehler23/bevy_map_editor](https://github.com/jbuehler23/bevy_map_editor) — A map/world/level editor for bevy games! · Rust · Apache-2.0
- [LogicalError/realtime-CSG-for-unity](https://github.com/LogicalError/realtime-CSG-for-unity) — Realtime-CSG, CSG level editor for Unity · C# · MIT
- [loophole-game/loophole-level-editor](https://github.com/loophole-game/loophole-level-editor) — Official level editor for Loophole, the time-bending puzzle game about working with - and against - your past selves. · TypeScript · MIT
- [lschmid83/Dragon-Island](https://github.com/lschmid83/Dragon-Island) — This is an open source 2D platform game similiar to Super Mario World written in Java and C++ with a level editor. Available for PC, Android, GP2X and… · Java · license not detected
- [mapeditor/tiled](https://github.com/mapeditor/tiled) — Flexible level editor · C++ · NOASSERTION
- [mohaneddz/q-runner](https://github.com/mohaneddz/q-runner) — 𝐐 𝐑𝐮𝐧𝐧𝐞𝐫 is a deterministic browser auto runner with cube, ship and ball modes, a level editor, endless mode and in browser reinforcement learning… · TypeScript · license not detected
- [OpenDungeons/OpenDungeons](https://github.com/OpenDungeons/OpenDungeons) — Open source game inspired by Dungeon Keeper - Dark, damp and dangerous... — *Not actively developed anymore* · C++ · NOASSERTION
- [RadicalCSG/com.chisel](https://github.com/RadicalCSG/com.chisel) — Chisel CSG Level Editor, for Unity · C# · MIT
- [ruffbuff/Levelarium](https://github.com/ruffbuff/Levelarium) — Lua&Love2D - open source game level editor, with some more features · Lua · MIT
- [SableReverie/Pryxel-GameDevLog-Godot](https://github.com/SableReverie/Pryxel-GameDevLog-Godot) — This is my first project creating a terrain using Godot extensions. I’m learning how to generate and shape environments, experiment with procedural… · license not detected
- [sirjuddington/SLADE](https://github.com/sirjuddington/SLADE) — It's a Doom editor · C++ · GPL-2.0
- [TrenchBroom/TrenchBroom](https://github.com/TrenchBroom/TrenchBroom) — Cross-Platform Level Editor · C++ · GPL-3.0
- [Trouv/bevy_ecs_ldtk](https://github.com/Trouv/bevy_ecs_ldtk) — ECS-friendly ldtk plugin for bevy, leveraging bevy_ecs_tilemap · Rust · NOASSERTION
- [Unity-Technologies/giles](https://github.com/Unity-Technologies/giles) — GILES: A Runtime Level Editor for Unity3D · C# · NOASSERTION

## Asset pipelines and file formats

- [aseprite/aseprite](https://github.com/aseprite/aseprite) — Animated sprite editor & pixel art tool (Windows, macOS, Linux) · C++ · license not detected
- [AssetRipper/AssetRipper](https://github.com/AssetRipper/AssetRipper) — GUI application to analyze game files · C# · GPL-3.0
- [bbayram-l/retrocrunch](https://github.com/bbayram-l/retrocrunch) — PS1-style asset pipeline: turn models, textures, sprites and levels into PS1-era game assets. Rust, Godot 4, CLI and MCP. · Rust · NOASSERTION
- [bogdan-cornianu/creative2d](https://github.com/bogdan-cornianu/creative2d) — Local pipeline and web app for generating 2D game assets for Phaser: characters, props, terrain tiles and backgrounds, with transparent backgrounds… · Python · MIT
- [EpicGames/BlenderTools](https://github.com/EpicGames/BlenderTools) — Blender addons that improve the game development workflow between Blender and Unreal. · Python · MIT
- [HErkanuzun/AssetForge](https://github.com/HErkanuzun/AssetForge) — AI game asset pipeline for Unreal Engine 5: text-to-3D (Meshy), text-to-motion (NVIDIA Kimodo), motion matching & blend spaces, AI sound (ElevenLabs)… · TypeScript · AGPL-3.0
- [jkuhlmann/cgltf](https://github.com/jkuhlmann/cgltf) — :diamond_shape_with_a_dot_inside: Single-file glTF 2.0 loader and writer written in C99 · C · MIT
- [KhronosGroup/glTF-Blender-IO](https://github.com/KhronosGroup/glTF-Blender-IO) — Blender glTF 2.0 importer and exporter · Python · Apache-2.0
- [KhronosGroup/KTX-Software](https://github.com/KhronosGroup/KTX-Software) — KTX (Khronos Texture) Library and Tools · C++ · NOASSERTION
- [LayrKits/Sprite-Pipeline](https://github.com/LayrKits/Sprite-Pipeline) — 2D Sprite Sheet Creation Pipeline · Python · license not detected
- [LibreSprite/LibreSprite](https://github.com/LibreSprite/LibreSprite) — Animated sprite editor & pixel art tool -- Fork of the last GPLv2 commit of Aseprite · C++ · GPL-2.0
- [logi-cmd/godot-game-studio-agent](https://github.com/logi-cmd/godot-game-studio-agent) — Codex-powered game studio skill for Godot, Unity, and Unreal with professional role routing, first-playable workflows, game-feel polish, MCP… · PowerShell · license not detected
- [maikramer/AiGameKit](https://github.com/maikramer/AiGameKit) — Game-focused asset-production tools and workflows for images, 3D models, audio, textures, rigging, and animation. · Python · license not detected
- [mrven/Blender-Asset-Creation-Toolset](https://github.com/mrven/Blender-Asset-Creation-Toolset) — Many Tools for Game Asset Creation (Import/Export FBXs, Origin Aligment Tool, Renaming, Low-Poly Art workflow tools, etc.) · Python · GPL-3.0
- [needle-mirror/com.unity.addressables](https://github.com/needle-mirror/com.unity.addressables) — Unity Addressables package for loading local or remote assets by address; this repository is a third-party UPM mirror. · C# · NOASSERTION
- [needle-mirror/com.unity.scriptablebuildpipeline](https://github.com/needle-mirror/com.unity.scriptablebuildpipeline) — The Scriptable Build Pipeline moves the asset bundle build pipeline to C#. Use the pre-defined build flows, or create your own using the divided up… · C# · NOASSERTION
- [NPC-Studio/yy-boss](https://github.com/NPC-Studio/yy-boss) — The boss Gms2 has always needed · Rust · Apache-2.0
- [openaigames/OpenAIGamesDesigner](https://github.com/openaigames/OpenAIGamesDesigner) — Skills, asset pipelines, and runtime tools for AI-assisted game development with Godot, Unity, Unreal Engine, Three.js, and Phaser. · Python · MIT
- [quinteroac/ComfyUI-GameAssetsMaker](https://github.com/quinteroac/ComfyUI-GameAssetsMaker) — Custom ComfyUI nodes for game asset preparation workflows. · Python · license not detected
- [shawn-makes-stuff/homestead](https://github.com/shawn-makes-stuff/homestead) — A Cyberpunk 2077 mod that adds the Fallout 4 style base building mechanic into the game - Includes Fallout asset import tool · Python · license not detected
- [tbosier/marchlands](https://github.com/tbosier/marchlands) — An AI-generated 3D kingdom builder whose roads are not drawn by the player — people walk, their routes wear into the ground, and the road network… · GDScript · license not detected
- [trebeljahr/sprite-tools](https://github.com/trebeljahr/sprite-tools) — Turn sprite sheets into collision polygons, pivots, tags and Godot or Unity files, in the browser, a CLI or over MCP. · TypeScript · MIT
- [udinmoInc/WindEffects](https://github.com/udinmoInc/WindEffects) — A modular, next-generation game engine built from scratch with C++23 and Vulkan. Powered by a data-oriented ECS architecture, a production-ready asset… · C++ · NOASSERTION
- [Unity-Technologies/Addressables-Sample](https://github.com/Unity-Technologies/Addressables-Sample) — Demo project using Addressables package · C# · license not detected
- [Unity-Technologies/AssetBundles-Browser](https://github.com/Unity-Technologies/AssetBundles-Browser) — Editor tool for viewing and debugging asset bundle contents before and after builds · C# · NOASSERTION

## Audio and music

- [AmplitudeAudio/sdk](https://github.com/AmplitudeAudio/sdk) — A powerful cross-platform audio engine, optimized for games. · C++ · Apache-2.0
- [chr15m/jsfxr](https://github.com/chr15m/jsfxr) — JavaScript sound effects generator. · JavaScript · Unlicense
- [CreateJS/SoundJS](https://github.com/CreateJS/SoundJS) — A Javascript library for working with Audio. It provides a consistent API for loading and playing audio on different browsers and devices. Currently… · JavaScript · MIT
- [Dn-Programming-Core-Management/Dn-FamiTracker](https://github.com/Dn-Programming-Core-Management/Dn-FamiTracker) — modifications and improvements for 0CC-FamiTracker (based on j0CC-FamiTracker 0.6.3) · C · NOASSERTION
- [faiface/beep](https://github.com/faiface/beep) — A little package that brings sound to any Go application. Suitable for playback and audio-processing. · Go · MIT
- [goldfire/howler.js](https://github.com/goldfire/howler.js) — Javascript audio library for the modern web. · JavaScript · MIT
- [increpare/bfxr2](https://github.com/increpare/bfxr2) — bfxr.net in javascript, with more things! · HTML · MIT
- [increpare/bfxr](https://github.com/increpare/bfxr) — Flash + AIR sound effects generator. Based on Sfxr. · ActionScript · license not detected
- [inexorgame/audioaugust](https://github.com/inexorgame/audioaugust) — A self made set of sounds. · CC-BY-4.0
- [jarikomppa/soloud](https://github.com/jarikomppa/soloud) — Free, easy, portable audio engine for games · C · NOASSERTION
- [KilledByAPixel/ZzFX](https://github.com/KilledByAPixel/ZzFX) — A Tiny JavaScript Sound FX System · JavaScript · MIT
- [meshula/LabMidi](https://github.com/meshula/LabMidi) — Midi IN and OUT. Standard midi file parser and player. Midi Softsynth implementation. · C++ · NOASSERTION
- [milkytracker/MilkyTracker](https://github.com/milkytracker/MilkyTracker) — A Fasttracker II compatible music editor · C++ · NOASSERTION
- [naomiaro/waveform-playlist](https://github.com/naomiaro/waveform-playlist) — Multitrack Web Audio editor and player with canvas waveform preview. Set cues, fades and shift multiple tracks in time. Record audio tracks or provide… · TypeScript · MIT
- [nicolas-van/sonant-x](https://github.com/nicolas-van/sonant-x) — Small JavaScript synthesizer library · JavaScript · Zlib
- [pixijs/sound](https://github.com/pixijs/sound) — WebAudio API playback library, with filters. Modern audio playback for modern browsers. · TypeScript · MIT
- [raysan5/rfxgen](https://github.com/raysan5/rfxgen) — A simple and easy-to-use fx sounds generator · C · Zlib
- [Theodeus/tuna](https://github.com/Theodeus/tuna) — An audio effects library for the Web Audio API. · JavaScript · license not detected
- [Tonejs/Tone.js](https://github.com/Tonejs/Tone.js) — A Web Audio framework for making interactive music in the browser. · TypeScript · MIT
- [ValveSoftware/steam-audio](https://github.com/ValveSoftware/steam-audio) — Steam Audio · C++ · Apache-2.0

## UI, input, accessibility, and localization

- [A11YTK/A11YTK](https://github.com/A11YTK/A11YTK) — The Accessibility Toolkit is an open-source Unity package for adding context-aware subtitles in VR, AR, and non-XR environments. · C# · MIT
- [AcTePuKc/uelockit](https://github.com/AcTePuKc/uelockit) — Unreal Engine Localization Toolkit - Make your own translation files + packaging simple! · Python · MIT
- [alucardx2010-hash/almurrib](https://github.com/alucardx2010-hash/almurrib) — Open-source Arabic game localization toolkit with extraction, translation, Arabic text processing, QA, and engine-specific patching. · Python · AGPL-3.0
- [anton-borodin-inr/ai-localization-checker](https://github.com/anton-borodin-inr/ai-localization-checker) — Vision-LLM localization defect detector for mobile games, evaluated against an OCR baseline · Python · MIT
- [bbepis/XUnity.AutoTranslator](https://github.com/bbepis/XUnity.AutoTranslator) — Unity game mod framework for translating in-game text through configurable translation services. · C# · MIT
- [cegui/cegui](https://github.com/cegui/cegui) — Crazy Eddie's GUI library is a versatile, fast, adjustable, multi-platform, C++ library for creating graphical user interfaces for games and rendering… · C++ · MIT
- [Firezac/ControllerInputViewer](https://github.com/Firezac/ControllerInputViewer) — A plugin for Godot 4 that allow you see and test your Inputs. · GDScript · MIT
- [GasimoCodes/Subtitler](https://github.com/GasimoCodes/Subtitler) — A simple subtitle tool for Unity3D inspired by Source Engine Closed Captions · HTML · MIT
- [irunna-ai/lqa-workbench](https://github.com/irunna-ai/lqa-workbench) — Professional Desktop Workbench for Game Localization QA · Rust · NOASSERTION
- [jonasgeiler/love2d-joystick-tester](https://github.com/jonasgeiler/love2d-joystick-tester) — 🎮 A simple LÖVE application to test joysticks and gamepads. · Lua · MIT
- [KlemensStrasser/KAP](https://github.com/KlemensStrasser/KAP) — Unity Accessibility Plugin · C# · MIT
- [Lord0fTurk/RPGMLocalizer](https://github.com/Lord0fTurk/RPGMLocalizer) — RPGMLocalizer is a powerful automated translation tool designed for RPG Maker games. It extracts text from game data, translates it using machine… · Python · GPL-3.0
- [LumioGames/LGUI](https://github.com/LumioGames/LGUI) — Game UI framework for AI agents, made by LumioGames. Build screens, logic and tests in the browser with no game engine, then export to Unity. 给 AI… · JavaScript · NOASSERTION
- [luppichristian/GameTest](https://github.com/luppichristian/GameTest) — Record/replay testing framework for C/C++ games. Deterministic input capture and injection for automated testing. · C · MIT
- [mikrima/UnityAccessibilityPlugin](https://github.com/mikrima/UnityAccessibilityPlugin) — The UI Accessibility Plugin (UAP) allows you to make your UI accessible to blind and visually impaired players on Windows, Android, iOS, Mac and WebGL. · C# · Apache-2.0
- [mtwilliams/libgamepad](https://github.com/mtwilliams/libgamepad) — :video_game: Cross-platform library for gamepad input. MIT licensed. · C · MIT
- [nezvers/Godot_input_tester](https://github.com/nezvers/Godot_input_tester) — Test inputs and learn the scripting to access it · GDScript · MIT
- [Nokorpo/gato-godot-accessibility-toolkit](https://github.com/Nokorpo/gato-godot-accessibility-toolkit) — A collection of demos and addons to promote accessibility in Godot games · GDScript · MPL-2.0
- [Noobzin14/rpg-translator-suite](https://github.com/Noobzin14/rpg-translator-suite) — Open-source localization toolkit for RPG Maker and similar game engines. · Python · MPL-2.0
- [OwlcatGames/LocalizationTool](https://github.com/OwlcatGames/LocalizationTool) — A tool for creating and maintaining game's localization resources · C# · MIT
- [RonenNess/GeonBit.UI](https://github.com/RonenNess/GeonBit.UI) — UI system for MonoGame projects. · C# · MIT
- [rouges78/GameStringer](https://github.com/rouges78/GameStringer) — Desktop app that auto-detects a game's engine, extracts the text, translates it with local or cloud AI, and re-applies the patch. 20+ engines, 20+ AI… · TypeScript · NOASSERTION
- [trudeaua21/EasyAccessibilityPackage](https://github.com/trudeaua21/EasyAccessibilityPackage) — [Archived] A Unity package designed to make accessible game development as simple as possible. · C# · MIT
- [universityofgames/unity-localization-toolkit](https://github.com/universityofgames/unity-localization-toolkit) — Localization Plugin for Unity3D · C# · LGPL-2.1

## Networking and multiplayer

- [0xFA11/MultiplayerNetworkingResources](https://github.com/0xFA11/MultiplayerNetworkingResources) — A curated list of Multiplayer Game Network Programming Resources · C · license not detected
- [albertok/godot-rocket-league](https://github.com/albertok/godot-rocket-league) — Network physics with rollback test using Godot and netfox · GDScript · MIT
- [colyseus/colyseus](https://github.com/colyseus/colyseus) — ⚔ Multiplayer Framework for Node.js · TypeScript · MIT
- [donislawdev/BeanNetworkTester](https://github.com/donislawdev/BeanNetworkTester) — Simulate bad network conditions on Windows/Linux - latency, burst packet loss, jitter, bandwidth limits, drops - to test how your app behaves on a poor… · Python · GPL-3.0
- [edgegap/netcode-game-sample-unity-ngo-3d-spaceshooter](https://github.com/edgegap/netcode-game-sample-unity-ngo-3d-spaceshooter) — This guide will help you create a headless server on Edgegap for a Unity project using Netcode for GameObjects as its networking solution. · C# · NOASSERTION
- [facebookarchive/RakNet](https://github.com/facebookarchive/RakNet) — [Archived] RakNet is a cross platform, open source, C++ networking engine for game programmers. · HTML · NOASSERTION
- [FirstGearGames/FishNet](https://github.com/FirstGearGames/FishNet) — FishNet: Unity Networking Evolved. · C# · NOASSERTION
- [GodotSteam/MultiplayerPeer](https://github.com/GodotSteam/MultiplayerPeer) — [Archived] An ecosystem of tools for Godot Engine and Valve's Steam. For the Windows, Linux, and Mac platforms. · license not detected
- [heroiclabs/nakama](https://github.com/heroiclabs/nakama) — Scalable open-source game backend server: multiplayer, matchmaking, leaderboards, chat, and social features for games. · Go · Apache-2.0
- [Kaigen-Technologies/net-crowd-stress-test](https://github.com/Kaigen-Technologies/net-crowd-stress-test) — A plaza of networked players on one server: a netcode stress test for the Kaigen Engine · C · MIT
- [kevintr303/Unity-Steam-Multiplayer-Sample](https://github.com/kevintr303/Unity-Steam-Multiplayer-Sample) — Sample Project for a Unity Multiplayer Game using Heathen Steamworks Foundation and Fish-Networking. · ShaderLab · MIT
- [lsalzman/enet](https://github.com/lsalzman/enet) — ENet reliable UDP networking library · C · MIT
- [makkaX2/DroneFlames-PC-Port](https://github.com/makkaX2/DroneFlames-PC-Port) — 🚁 DroneFlames PC Port (Windows x64) — native PC controls, WASD camera, smooth zoom, multiplayer & automated CI/CD builds by @good_boy_irl. · GDScript · license not detected
- [mas-bandwidth/netcode](https://github.com/mas-bandwidth/netcode) — Secure client/server protocol for multiplayer games built on top of UDP · C · BSD-3-Clause
- [mas-bandwidth/yojimbo](https://github.com/mas-bandwidth/yojimbo) — A network library for client/server games written in C++ · C++ · BSD-3-Clause
- [MirrorNetworking/Mirror](https://github.com/MirrorNetworking/Mirror) — #1 Open Source Unity Networking Library · C# · MIT
- [pond3r/ggpo](https://github.com/pond3r/ggpo) — Good Game, Peace Out Rollback Network SDK · C++ · MIT
- [RevenantX/LiteNetLib](https://github.com/RevenantX/LiteNetLib) — Lite reliable UDP library for Mono and .NET · C# · MIT
- [rishavnathpati/Netcode-Multiplayer](https://github.com/rishavnathpati/Netcode-Multiplayer) — This repository contains a sample project demonstrating the implementation of Netcode for Game Objects in Unity. Netcode for Game Objects is a network… · C# · license not detected
- [SirFroweey/PyDark](https://github.com/SirFroweey/PyDark) — PyDark is a 2D and Online Multiplayer video game framework written on-top of Python and PyGame. · Python · license not detected
- [Unity-Technologies/com.unity.multiplayer.samples.coop](https://github.com/Unity-Technologies/com.unity.multiplayer.samples.coop) — A small-scale cooperative game sample built on the new, Unity networking framework to teach developers about creating a similar multiplayer game. · C# · NOASSERTION
- [Unity-Technologies/com.unity.netcode.gameobjects](https://github.com/Unity-Technologies/com.unity.netcode.gameobjects) — Netcode for GameObjects is a high-level netcode SDK that provides networking capabilities to GameObject/MonoBehaviour workflows within Unity and sits… · C# · NOASSERTION
- [Unity-Technologies/com.unity.services.samples.matchplay](https://github.com/Unity-Technologies/com.unity.services.samples.matchplay) — A Matchmaking with Multiplay Unity example project. Implements the Unity Matchmaking and Multiplay SDK to create an end to end matchmaking game experience. · C# · NOASSERTION
- [ValveSoftware/GameNetworkingSockets](https://github.com/ValveSoftware/GameNetworkingSockets) — Reliable & unreliable messages over UDP. Robust message fragmentation & reassembly. P2P networking / NAT traversal. Encryption. · C++ · BSD-3-Clause
- [vklubkov/UnityNetworkTransportOverSteamworks](https://github.com/vklubkov/UnityNetworkTransportOverSteamworks) — Network transport for Unity Netcode for Entities implemented using Steamworks SDK (ISteamNetworkingSockets). · C# · MIT
- [zpl-c/librg](https://github.com/zpl-c/librg) — 🚀 Making multi-player gamedev simpler since 2017 · C · BSD-3-Clause

## Persistence, backend, and live operations

- [agones-dev/agones](https://github.com/agones-dev/agones) — Dedicated Game Server Hosting and Scaling for Multiplayer Games on Kubernetes · Go · Apache-2.0
- [eldioss21/gamebeast-api-lens](https://github.com/eldioss21/gamebeast-api-lens) — Gamebeast-Style Game Studio Analytics API Guide 2026: A/B Testing and LiveOps · HTML · license not detected
- [GameAnalytics/GA-SDK-GODOT](https://github.com/GameAnalytics/GA-SDK-GODOT) — Official GameAnalytics Godot SDK repository · Objective-C · MIT
- [GameAnalytics/GA-SDK-JAVASCRIPT](https://github.com/GameAnalytics/GA-SDK-JAVASCRIPT) — Official repository for GameAnalytics JavaScript SDK · TypeScript · MIT
- [GameAnalytics/GA-SDK-UNITY](https://github.com/GameAnalytics/GA-SDK-UNITY) — The GameAnalytics SDK for tracking events in Unity. · C# · MIT
- [GameAnalytics/GA-SDK-UNREAL](https://github.com/GameAnalytics/GA-SDK-UNREAL) — A repository containing the GameAnalytics Unreal Engine 5 Plugin including documentation. · C++ · MIT
- [GameAnalytics/gameanalytics-sdk-cpp](https://github.com/GameAnalytics/gameanalytics-sdk-cpp) — Repository for the GameAnalytics C++ SDK · C · MIT
- [giangero1/frog-lobby](https://github.com/giangero1/frog-lobby) — Open-source Node.js backend for Frog Wars: multiplayer lobby discovery, relay/NAT coordination, signed sessions, PlayFab integration, and… · JavaScript · MIT
- [googleforgames/open-match2](https://github.com/googleforgames/open-match2) — Open Match 2 core application and API/protobuf implementation for building matchmaking services. · Go · Apache-2.0
- [googleforgames/open-match](https://github.com/googleforgames/open-match) — Flexible, extensible, and scalable video game matchmaking. · Go · Apache-2.0
- [googleforgames/open-saves](https://github.com/googleforgames/open-saves) — Open Saves is a cloud native data store for game development. · Go · Apache-2.0
- [heroiclabs/hiro](https://github.com/heroiclabs/hiro) — The server interface for the Hiro game framework. · Go · Apache-2.0
- [heroiclabs/nakama-godot](https://github.com/heroiclabs/nakama-godot) — Nakama Godot Client SDK · GDScript · Apache-2.0
- [heroiclabs/nakama-js](https://github.com/heroiclabs/nakama-js) — Nakama JavaScript Client SDK · TypeScript · Apache-2.0
- [heroiclabs/nakama-unity](https://github.com/heroiclabs/nakama-unity) — Nakama Unity Client SDK · C# · NOASSERTION
- [heroiclabs/nakama-unreal](https://github.com/heroiclabs/nakama-unreal) — Nakama Unreal Client SDK · C++ · Apache-2.0
- [LEADR-official/leadr-oss](https://github.com/LEADR-official/leadr-oss) — LEADR is the open-source, cross-platform leaderboards backend for indie game devs. · Python · Apache-2.0
- [ProjectMakersDE/horizOn-simpleServer](https://github.com/ProjectMakersDE/horizOn-simpleServer) — A lightweight, self-hostable PHP game backend: the free, open-source edition of horizOn. Drop-in replacement compatible with horizOn SDKs (Unity… · PHP · MIT
- [sbox-cool/sbox-network-storage-server](https://github.com/sbox-cool/sbox-network-storage-server) — Open-source s&box game backend. Self-host saves, inventory, purchases and reward rules for player-hosted, P2P or dedicated games. SQLite/PostgreSQL. · C# · AGPL-3.0
- [supercraft-host/crux](https://github.com/supercraft-host/crux) — Open-source SDKs for Crux, a hosted game backend for player auth, cloud saves, leaderboards, economy, matchmaking, and server registry. · C# · MIT
- [TaloDev/godot](https://github.com/TaloDev/godot) — Talo's Godot plugin for open source leaderboards, stats, auth, game saves and more · GDScript · MIT
- [TaloDev/unity](https://github.com/TaloDev/unity) — Talo's Unity package for open source leaderboards, stats, auth, game saves and more · C# · MIT

## Testing, QA, and playtesting

- [aaronhg/arbor](https://github.com/aaronhg/arbor) — AI QA for canvas games — the policy layer over coir (static analysis) + copse (runtime driver): zero-LLM coverage/visual gates plus an LLM agent that… · JavaScript · license not detected
- [adam0white/GameEval](https://github.com/adam0white/GameEval) — Autonomous AI-powered game testing platform that uses browser automation and LLMs to evaluate browser-based games through a four-phase pipeline: load… · TypeScript · license not detected
- [alex-durango/qaping](https://github.com/alex-durango/qaping) — Automatic QA for your game. Your coding agent plans the checks, real playtesters run them, and every patch gets a report. · JavaScript · MIT
- [alttester/AltTester-Unity-SDK](https://github.com/alttester/AltTester-Unity-SDK) — AltTester Unity SDK is an UI driven test automation tool that helps you find objects in your game and interacts with them using tests written in C#… · C# · GPL-3.0
- [believer-oss/Untested](https://github.com/believer-oss/Untested) — Coroutine-enabled testing framework for Unreal. · C++ · MIT
- [bitwes/Gut](https://github.com/bitwes/Gut) — Godot Unit Test. Unit testing tool for Godot Game Engine. · GDScript · license not detected
- [chickensoft-games/GoDotTest](https://github.com/chickensoft-games/GoDotTest) — C# test runner for Godot. Run tests from the command line, collect code coverage, and debug tests. · C# · MIT
- [chickensoft-games/GodotTestDriver](https://github.com/chickensoft-games/GodotTestDriver) — Easy integration testing for Godot with simulated input, node drivers, and fixtures. · C# · MIT
- [DaedalicEntertainment/ue4-test-automation](https://github.com/DaedalicEntertainment/ue4-test-automation) — Facilitates setting up integration test suits with Unreal Engine 4 Gauntlet. · C++ · MIT
- [DynamicDevices/game-playtesting-skill](https://github.com/DynamicDevices/game-playtesting-skill) — Portable game and app playtesting skill for Claude and other agents: reproducible tests, developer feedback, creative ideas and experiment planning. · Python · MIT
- [Fahmida04/Ravens-Claw](https://github.com/Fahmida04/Ravens-Claw) — Raven's Claw: game testing & QA team, Bangladesh · license not detected
- [game-ci/unity-test-runner](https://github.com/game-ci/unity-test-runner) — Run tests for any Unity project · TypeScript · MIT
- [GhazaGG/Unity-Playtest-for-Claude](https://github.com/GhazaGG/Unity-Playtest-for-Claude) — Claude playtests your Unity game: Editor probes, scripted Play Mode, host + client with latency, honest pass/fail report. A Claude Code skill built on… · Python · MIT
- [godot-gdunit-labs/gdUnit4](https://github.com/godot-gdunit-labs/gdUnit4) — Embedded unit testing framework for Godot 4 supporting GDScript and C#. Features test-driven development, embedded test inspector, extensive… · GDScript · MIT
- [grloper/playgoblin](https://github.com/grloper/playgoblin) — A goblin plays your game overnight and files the bugs it breaks. Open-source QA bot for Unity, Unreal and any engine, with an MCP server for AI agents. · C# · Apache-2.0
- [jinsajoy13/Game-Testing-Portfolio](https://github.com/jinsajoy13/Game-Testing-Portfolio) — This repository contains a collection of my manual game testing projects created as part of my QA practice and portfolio. Each project focuses on a… · license not detected
- [kelinacowellqa/Manual-QA-Portfolio-Kelina-Cowell](https://github.com/kelinacowellqa/Manual-QA-Portfolio-Kelina-Cowell) — Complete QA portfolio featuring six cross-platform testing projects and documentation examples. · HTML · license not detected
- [liortal53/UnityTestingExtensions](https://github.com/liortal53/UnityTestingExtensions) — Unity Test Framework Extension Library · C# · MIT
- [masteryee-labs/Open-Godot-MCP](https://github.com/masteryee-labs/Open-Godot-MCP) — Open-source MCP server for AI-autonomous Godot game development. Deterministic playtesting, multiplayer testing, DAP debugging, LSP, token-efficient… · GDScript · MIT
- [needle-mirror/com.unity.test-framework.performance](https://github.com/needle-mirror/com.unity.test-framework.performance) — Package that extends Unity Test Framework package. Adds performance testing capabilities and collects configuration metadata. 📦 [Mirrored from UPM, not… · C# · NOASSERTION
- [needle-mirror/com.unity.test-framework](https://github.com/needle-mirror/com.unity.test-framework) — Test framework for running Edit mode and Play mode tests in Unity. 📦 [Mirrored from UPM, not affiliated with Unity Technologies.] · C# · NOASSERTION
- [Regression-Games/RegressionGames.Unity.Testing](https://github.com/Regression-Games/RegressionGames.Unity.Testing) — Regression Games Unity Testing SDK · C# · NOASSERTION
- [Roboter-Schlafen-Nicht/rsn-game-qa](https://github.com/Roboter-Schlafen-Nicht/rsn-game-qa) — Autonomous game testing — RL-trained agents find bugs through pixel-based playtesting. 19K LoC, 1,137 tests, 95% coverage. · Python · MIT
- [rohanvijaykumar/enhance-qa](https://github.com/rohanvijaykumar/enhance-qa) — A QA team for any app, inside your coding agent. Works with Claude Code, Codex, Cursor and more. · JavaScript · MIT
- [stixez/ac-playtest](https://github.com/stixez/ac-playtest) — Unofficial offline playtest harness for AirConsole games: simulate a TV screen and any number of phones locally, and script full multiplayer sessions… · JavaScript · MIT
- [tanggengbo4532/task-tree-acceptance-replication](https://github.com/tanggengbo4532/task-tree-acceptance-replication) — A DSH plugin implementing a multi-agent loop acceptance framework: four-role task-tree acceptance testing with human-in-the-loop, no-cheat… · GDScript · MIT
- [tobyselway/bevy-autoplay](https://github.com/tobyselway/bevy-autoplay) — Automated integration testing based on recorded play-testing sessions · Rust · Apache-2.0
- [youichi-uda/godot-qa](https://github.com/youichi-uda/godot-qa) — Automated playtest runner for Godot 4 - headless CI testing with input replay, node/text asserts, screenshot diff. Scenario format compatible with… · GDScript · MIT

## Debugging, profiling, and observability

- [baldurk/renderdoc](https://github.com/baldurk/renderdoc) — RenderDoc is a stand-alone graphics debugging tool. · C++ · MIT
- [bbbscarter/GodotRuntimeDebugTools](https://github.com/bbbscarter/GodotRuntimeDebugTools) — A proof-of-concept Godot addon to improve the runtime debugging experience · GDScript · MIT
- [bombomby/optick](https://github.com/bombomby/optick) — C++ Profiler For Games · C# · MIT
- [dev-pikapik/unity-mcp-driver](https://github.com/dev-pikapik/unity-mcp-driver) — Let an AI agent see, play and debug your Unity game through the Model Context Protocol: UI Toolkit & uGUI automation, screenshots, logs, live state… · C# · NOASSERTION
- [GameTechDev/PresentMon](https://github.com/GameTechDev/PresentMon) — Capture and analyze the high-level performance characteristics of graphics applications on Windows. · C++ · MIT
- [godot-extended-libraries/godot-debug-menu](https://github.com/godot-extended-libraries/godot-debug-menu) — Display in-game FPS/performance/hardware metrics in a Godot 4.x project · GDScript · MIT
- [GPUOpen-Tools/radeon_gpu_profiler](https://github.com/GPUOpen-Tools/radeon_gpu_profiler) — Radeon GPU Profiler (RGP) is a tool from AMD that allows for deep inspection of GPU workloads. · license not detected
- [needle-mirror/com.unity.memoryprofiler](https://github.com/needle-mirror/com.unity.memoryprofiler) — The Memory Profiler offers a unified solution allowing you to profile both small projects on mobile devices and big AAA projects on high end machines… · C# · NOASSERTION
- [needle-mirror/com.unity.performance.profile-analyzer](https://github.com/needle-mirror/com.unity.performance.profile-analyzer) — The Profile Analyzer tool supports the standard Unity Profiler. You can use it to analyze multiple frames and multiple data sets of the CPU data in the… · C# · NOASSERTION
- [NVIDIA/nsight-aftermath-samples](https://github.com/NVIDIA/nsight-aftermath-samples) — Samples for the Nsight Aftermath SDK. · C · license not detected
- [Pineapple/GodotTracy](https://github.com/Pineapple/GodotTracy) — Tracy Profiler module for the Godot Engine · Python · MIT
- [sinai-dev/UnityExplorer](https://github.com/sinai-dev/UnityExplorer) — [Archived] An in-game UI for exploring, debugging and modifying IL2CPP and Mono Unity games. · C# · GPL-3.0
- [Singe-dore/Debugging-Kit-Godot](https://github.com/Singe-dore/Debugging-Kit-Godot) — Automated live testing CLI for Godot projects. Systematically execute every input path and monitor all numeric properties in real-time. Identify… · Shell · NOASSERTION
- [Tencent/BqLog](https://github.com/Tencent/BqLog) — A lightweight, high-performance, industrial-grade cross-language logging library (C++/Java/C#/Kotlin/TS/Python/Go), battle-tested in Honor of Kings. · C++ · NOASSERTION
- [wolfpld/tracy](https://github.com/wolfpld/tracy) — Frame profiler · C++ · NOASSERTION
- [yasirkula/UnityIngameDebugConsole](https://github.com/yasirkula/UnityIngameDebugConsole) — A uGUI based console to see debug messages and execute commands during gameplay in Unity · C# · MIT
- [yasirkula/UnityRuntimeInspector](https://github.com/yasirkula/UnityRuntimeInspector) — Runtime Inspector and Hierarchy solution for Unity for debugging and runtime editing purposes · C# · MIT
- [Zylann/zprofiler](https://github.com/Zylann/zprofiler) — A CPU time profiler for Godot Engine · C++ · NOASSERTION

## Build, CI, packaging, and release

- [abarichello/godot-ci](https://github.com/abarichello/godot-ci) — Docker image to export Godot Engine games. Templates for Gitlab CI and GitHub Actions to deploy to GitLab Pages/GitHub Pages/Itch.io. · Dockerfile · MIT
- [Avalin/Unity-CI-CD](https://github.com/Avalin/Unity-CI-CD) — Unity CI/CD pipeline with multi-platform builds, releases, and deploys · ShaderLab · MIT
- [buildalon/activate-unity-license](https://github.com/buildalon/activate-unity-license) — A GitHub Action to activate a Unity Game Engine license for CI/CD workflows · TypeScript · MIT
- [buildalon/unity-setup](https://github.com/buildalon/unity-setup) — A GitHub Action for setting up the Unity Game Engine for CI/CD workflows · TypeScript · MIT
- [firebelley/godot-export](https://github.com/firebelley/godot-export) — Automatically exports your Godot games. · TypeScript · MIT
- [game-ci/docker](https://github.com/game-ci/docker) — Series of CI-specialised docker images for Unity. · Dockerfile · MIT
- [game-ci/unity-actions](https://github.com/game-ci/unity-actions) — Github actions for testing and building Unity projects · Mathematica · MIT
- [game-ci/unity-builder](https://github.com/game-ci/unity-builder) — Build Unity projects for different platforms · TypeScript · MIT
- [game-ci/unity-license-activate](https://github.com/game-ci/unity-license-activate) — Activate Unity license through CLI · JavaScript · NOASSERTION
- [game-ci/unity-orb](https://github.com/game-ci/unity-orb) — Build and test Unity projects for several platforms using CircleCI. · Shell · MIT
- [godot-gdunit-labs/gdUnit4-action](https://github.com/godot-gdunit-labs/gdUnit4-action) — 🎮 Official GdUnit4 GitHub Action for automated testing in Godot 4.x projects. Supports GDScript & C#, test reporting, and CI/CD pipeline integration… · JavaScript · MIT
- [hubacekjakub/Godot-QuickStart](https://github.com/hubacekjakub/Godot-QuickStart) — Simple CI/CD template for Godot projects · MIT
- [polzon/godot-gha-ci-cd](https://github.com/polzon/godot-gha-ci-cd) — Github Action ci/cd scripts for Godot Engine. · Shell · MIT
- [RageAgainstThePixel/unity-setup](https://github.com/RageAgainstThePixel/unity-setup) — A GitHub action for setting up the Unity Game Engine for CI/CD workflows. · TypeScript · MIT
- [RedpointGames/uet](https://github.com/RedpointGames/uet) — UET (Unreal Engine Tool) makes building and testing Unreal Engine projects and plugins easy. It can distribute builds with BuildGraph, remotely execute… · C# · MIT
- [Sector9Ltd/UE5-Build-Project](https://github.com/Sector9Ltd/UE5-Build-Project) — Build, cook, stage, package and archive an Unreal project with RunUAT. · NOASSERTION
- [studentutu/UnityTemplateArchitecture](https://github.com/studentutu/UnityTemplateArchitecture) — Base Template for Unity Projects, IOC, MVC, Message Broker,Unitask, ECS-Entitas, Addressables, Tests, profiling, CI/CD/staging · C# · license not detected
- [undying-cipher/godot-ci-cd](https://github.com/undying-cipher/godot-ci-cd) — Godot game build, test, release GitHub actions (itch.io, web, etc.) · GDScript · GPL-3.0
- [vini-guerrero/godot-exporter](https://github.com/vini-guerrero/godot-exporter) — Godot Engine Automation Pipeline Android – iOS – Linux – MacOS – Windows – HTML5 – Itch.io. · Shell · MIT
- [YenidoganKursat/Kaynexis-Agentic-Game-Studio](https://github.com/YenidoganKursat/Kaynexis-Agentic-Game-Studio) — Codex-first multi-engine game studio system with starter kits, research, checklists, and CI/CD for Godot, Unity, and Unreal. · Python · MIT

## Publishing, distribution, and monetization

- [adaptyteam/AdaptySDK-Unity](https://github.com/adaptyteam/AdaptySDK-Unity) — SDK for growing mobile in-app purchases · C# · MIT
- [ArtyProf/steamworks-ffi-node](https://github.com/ArtyProf/steamworks-ffi-node) — A TypeScript/JavaScript wrapper for the Steamworks SDK using Koffi FFI, designed for Node.js and Electron applications with Steamworks SDK integration. · TypeScript · MIT
- [CM2Walki/steampipe](https://github.com/CM2Walki/steampipe) — Dockerfile for automated build of a SteamCMD + Steamworks SDK Tools installation: https://hub.docker.com/r/cm2network/steampipe/ · Dockerfile · MIT
- [Facepunch/Facepunch.Steamworks](https://github.com/Facepunch/Facepunch.Steamworks) — Another fucking c# Steamworks implementation · C# · MIT
- [GodotSteam/GodotSteam](https://github.com/GodotSteam/GodotSteam) — [Archived] An ecosystem of tools for Godot Engine and Valve's Steam. For Linux, Mac, and Windows. · license not detected
- [indiesoftby/defold-yagames](https://github.com/indiesoftby/defold-yagames) — YaGames is the Yandex.Games SDK implementation for the Defold game engine. · Lua · MIT
- [jasielmacedo/steam-microtransaction-api](https://github.com/jasielmacedo/steam-microtransaction-api) — An intermediate api to handle steam microtransactions using steam web services. Ready to use with Unity, Unreal, Godot and so on · TypeScript · MIT
- [JDeffner/steamwand.js](https://github.com/JDeffner/steamwand.js) — TypeScript bindings for the Steamworks SDK, generated from Valve's steam_api.json and called through koffi FFI. No native build step. · TypeScript · NOASSERTION
- [LANCommander/LANCommander](https://github.com/LANCommander/LANCommander) — Self-hosted game library and distribution platform with desktop launcher and package management. · C# · MIT
- [Playgama/bridge-godot-4](https://github.com/Playgama/bridge-godot-4) — One SDK for cross-platform publishing HTML5 games · GDScript · MIT
- [Playgama/bridge-unity](https://github.com/Playgama/bridge-unity) — One SDK for cross-platform publishing HTML5 games · C# · MIT
- [Playgama/bridge](https://github.com/Playgama/bridge) — One SDK for cross-platform publishing HTML5 games · TypeScript · LGPL-3.0
- [Prime-SDK/PrimeSDK](https://github.com/Prime-SDK/PrimeSDK) — Unity abstraction SDK for game ads, payments, analytics, data, and web game platform providers. · C# · license not detected
- [qonversion/unity-sdk](https://github.com/qonversion/unity-sdk) — Qonversion Unity SDK: iOS and Android purchases confirmed with the stores, entitlements, and the revenue data behind Apple Ads, A/B tests and analytics. · C# · MIT
- [rlabrecque/Steamworks.NET](https://github.com/rlabrecque/Steamworks.NET) — Steamworks wrapper for Unity / C# · C# · MIT
- [SandwichCakeStudios/SandwichSteam](https://github.com/SandwichCakeStudios/SandwichSteam) — Steamworks SDK integration for Unreal Engine 5 on Windows, macOS and Linux. Features Blueprint and C++ APIs for multiplayer, lobbies, voice chat, Steam… · C++ · MIT
- [tomicz/steam-pipe-gui-macos-unity](https://github.com/tomicz/steam-pipe-gui-macos-unity) — SteamPipeGUI for macOS: build and upload Unity games to Steam from the Unity Editor on Mac, with no steamcmd commands or VDF scripts to write. The… · C# · MIT
- [yevhenii-sir/purser](https://github.com/yevhenii-sir/purser) — In-app purchases for games on SpacetimeDB: live on maincloud in seconds, or self-hosted · Rust · MIT

## Learning and reference implementations

- [bastientanesie/godot-43-2d-game-tutorial](https://github.com/bastientanesie/godot-43-2d-game-tutorial) — Complete sources for the official Godot 4.3 tutorial "Your first 2D game" · GDScript · license not detected
- [ConstructCommunity/awesome-construct](https://github.com/ConstructCommunity/awesome-construct) — A curated list of tools, tutorials, examples, and much more, for the awesome game development engines Construct 2 and Construct 3 · CC0-1.0
- [game-ci/documentation](https://github.com/game-ci/documentation) — 📚 Documentation for GameCI open source projects · MDX · MIT
- [GamineAI/GamineAI-README.md-resources-tutorials-prompts-assets-tools-docs-](https://github.com/GamineAI/GamineAI-README.md-resources-tutorials-prompts-assets-tools-docs-) — AI-powered game development platform with free tools, tutorials, resources, and workflows for indie developers 🎮🤖 · license not detected
- [kidscancode/circle_jump](https://github.com/kidscancode/circle_jump) — An open source mobile game made with Godot. · GDScript · NOASSERTION
- [krs9851/video-game-accessibility](https://github.com/krs9851/video-game-accessibility) — Learn how to add accessibility features to your unity game · C# · MIT
- [mackysoft/Unity-GitHubActions-Tutorials](https://github.com/mackysoft/Unity-GitHubActions-Tutorials) — A tutorials on CI using Unity and GitHub Actions. All tutorials include a example project. · MIT
- [MostlyAdequate/mostly-adequate-guide](https://github.com/MostlyAdequate/mostly-adequate-guide) — Mostly adequate guide to FP (in javascript) · JavaScript · NOASSERTION
- [MrRobinOfficial/Guide-UnrealEngine](https://github.com/MrRobinOfficial/Guide-UnrealEngine) — This repository is designed to help developers learn how to get started with Unreal Engine and C++. · Markdown · license not detected
- [nanshaws/LibgdxTutorial](https://github.com/nanshaws/LibgdxTutorial) — libgdx 教程项目 本项目旨在提供完整的libgdx桌面教程，帮助开发者快速掌握libgdx游戏开发框架的使用。成功的将gdx-ai和ashley的tests从官网剥离出来,并成功运行。libgdx tutorial project This project aims to provide a… · Java · license not detected
- [Overv/VulkanTutorial](https://github.com/Overv/VulkanTutorial) — Tutorial for the Vulkan graphics and compute API · C++ · CC-BY-SA-4.0
- [RNIB-MediaAndCulture/Gaming_Devkit](https://github.com/RNIB-MediaAndCulture/Gaming_Devkit) — Repository for RNIB's gaming accessibility Devkit · HTML · license not detected
- [ronja-tutorials/ShaderTutorials](https://github.com/ronja-tutorials/ShaderTutorials) — unity shader tutorials · ShaderLab · license not detected
- [steincodes/godot-shader-tutorials](https://github.com/steincodes/godot-shader-tutorials) — Basic godot shader tutorial projects from my youtube tutorials. · GLSL · MIT
- [XRAccessibility/xraccessibility.github.io](https://github.com/XRAccessibility/xraccessibility.github.io) — Curated repository of code and resources for accessibility in XR, including game-focused plugins and toolkits. · license not detected
- [ZachGoldberg/Startup-CTO-Handbook](https://github.com/ZachGoldberg/Startup-CTO-Handbook) — The Startup CTO's Handbook, a book covering leadership, management and technical topics for leaders of software engineering teams · NOASSERTION

## How to assemble a reusable stack

A repository being useful to game development does not mean it works with every engine or with every other entry here. Treat each choice as a component with explicit constraints:

- **Foundation:** select one engine, framework, or runtime first.
- **Working baseline:** fork or clone a starter that already builds and runs.
- **Compatibility:** prefer components with examples for that foundation; check language, engine version, license, platform, and dependency constraints.
- **Small integrations:** add one system at a time and keep a known-good build.
- **Verification:** test the full player path—from launch through a core interaction to save, network, or exit—on intended platforms.
- **Upkeep:** track upstream releases and security notices; replace abandoned dependencies deliberately, not during a late release crunch.

## Sources and scope

Entries were discovered and checked against public GitHub repository metadata and established community indexes, including [awesome-game-engine-dev](https://github.com/stevinz/awesome-game-engine-dev), [awesome-gamedev](https://github.com/Calinou/awesome-gamedev), [Magic Tools](https://github.com/ellisonleao/magictools), and [Awesome-Gamedev](https://github.com/FronkonGames/Awesome-Gamedev). Descriptions are concise editorial summaries; use each project's own documentation and repository history as the source of truth. This list does not imply endorsement or guarantee that a project is maintained, secure, compatible, or production-ready.

## License

This curated list is available under [CC BY-SA 4.0](LICENSE). Each linked project keeps its own license and terms.
