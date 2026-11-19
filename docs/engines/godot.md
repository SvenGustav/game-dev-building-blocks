# Godot Game Development Stack

This is a full stack view: engine-specific repositories plus shared tools that can provide reusable assets, systems, or formats. Shared does not mean drop-in compatible; check integration and versions. The catalog includes repositories with at least 10 GitHub stars.

**Browse:** [all engines](README.md) · [game types](../game-types.md) · [shared building blocks](../shared-building-blocks.md)

Use the sections below to assemble a stack by function. Star counts are snapshots, not quality or maintenance guarantees. Check upstream engine versions, licenses, and project status before adopting anything.

**Godot-tagged repositories:** 40

### Engines & frameworks

- [godotengine/godot](https://github.com/godotengine/godot) — Godot Engine – Multi-platform 2D and 3D game engine · engine: Godot · type: 2D, 3D · C++ · license: MIT · ⭐ 120397

### Project foundations & templates

- [chickensoft-games/GodotGame](https://github.com/chickensoft-games/GodotGame) — C# game template for Godot 4 with debug launch configurations, testing (locally and on CI/CD), code coverage, dependency update checks, and spell check working out-of-the-box! · engine: Godot · C# · license: MIT · ⭐ 431
- [MechanicalFlower/godot-template](https://github.com/MechanicalFlower/godot-template) — Godot project template with code formatting, license tracking, and CI/CD. · engine: Godot · GDScript · license: MIT · ⭐ 69

### Game design & planning

- [dialogic-godot/dialogic](https://github.com/dialogic-godot/dialogic) — 💬 Create Dialogs, Visual Novels, RPGs, and manage Characters with Godot to create your Game! · engine: Godot · type: Narrative & visual novel · GDScript · license: MIT · ⭐ 6181
- [inkle/ink](https://github.com/inkle/ink) — inkle's open source scripting language for writing interactive narrative. · cross-engine · type: Narrative & visual novel · C# · license: MIT · ⭐ 5025
- [nathanhoad/godot_dialogue_manager](https://github.com/nathanhoad/godot_dialogue_manager) — A powerful nonlinear dialogue system for Godot · engine: Godot · type: Narrative & visual novel · GDScript · license: MIT · ⭐ 3991
- [inkle/inky](https://github.com/inkle/inky) — An editor for ink: inkle's narrative scripting language · cross-engine · type: Narrative & visual novel · JavaScript · license: not detected · ⭐ 2760
- [galaxykate/tracery](https://github.com/galaxykate/tracery) — Tracery: a story-grammar generation library for javascript · cross-engine · JavaScript · license: Apache-2.0 · ⭐ 2222
- [patterkit/patter](https://github.com/patterkit/patter) — Editor, compiler, and runtimes for writing and running dialogue flows for videogames. · engine: Godot, Unity, Unreal Engine · type: Narrative & visual novel · TypeScript · license: MIT · ⭐ 23

### Architecture, ECS & scripting

- [skypjack/entt](https://github.com/skypjack/entt) — Gaming meets modern C++ - a fast and reliable entity component system (ECS) and much more · cross-engine · C++ · license: MIT · ⭐ 13279
- [SanderMertens/flecs](https://github.com/SanderMertens/flecs) — A fast entity component system (ECS) for C & C++ · cross-engine · C · license: NOASSERTION · ⭐ 8854
- [genaray/Arch](https://github.com/genaray/Arch) — A high-performance C# based Archetype & Chunks Entity Component System (ECS) with optional multithreading. · engine: Godot, Unity, MonoGame, Stride · C# · license: Apache-2.0 · ⭐ 1883
- [jmorton06/Lumos](https://github.com/jmorton06/Lumos) — Cross-Platform C++ 2D/3D game engine · cross-engine · type: 2D, 3D · C++ · license: MIT · ⭐ 1605
- [NateTheGreatt/bitECS](https://github.com/NateTheGreatt/bitECS) — Flexible, minimal, data-oriented ECS library for Typescript · cross-engine · TypeScript · license: MPL-2.0 · ⭐ 1541
- [fubark/cyber](https://github.com/fubark/cyber) — Fast and concurrent scripting. · cross-engine · Zig · license: MIT · ⭐ 1520
- [increpare/PuzzleScript](https://github.com/increpare/PuzzleScript) — Open Source HTML5 Puzzle Game Engine · cross-engine · type: Puzzle & board games · JavaScript · license: MIT · ⭐ 1115
- [hmans/miniplex](https://github.com/hmans/miniplex) — A 👩‍💻 developer-friendly entity management system for 🕹 games and similarly demanding applications, based on 🛠 ECS architecture. · cross-engine · TypeScript · license: MIT · ⭐ 1067
- [friflo/Friflo.Engine.ECS](https://github.com/friflo/Friflo.Engine.ECS) — High-performance C# ECS · engine: Godot, Unity, MonoGame, Raylib · C# · license: MIT · ⭐ 818
- [Doraku/DefaultEcs](https://github.com/Doraku/DefaultEcs) — Entity Component System framework aiming for syntax and usage simplicity with maximum performance for game development. · cross-engine · C# · license: MIT-0 · ⭐ 765
- [phisko/kengine](https://github.com/phisko/kengine) — Game engine with an Entity-Component-System (ECS) architecture. Focus on ease-of-use, runtime extensibility and compile-time type safety. · cross-engine · C++ · license: MIT · ⭐ 619
- [i42output/neoGFX](https://github.com/i42output/neoGFX) — Cross-platform GPU-oriented C++ application/game framework · cross-engine · C++ · license: GPL-3.0 · ⭐ 577
- [r-lyeh-archived/scriptorium](https://github.com/r-lyeh-archived/scriptorium) — :scroll: Game Scripting Languages benchmarked · cross-engine · C · license: Unlicense · ⭐ 525
- [InvadingOctopus/octopuskit](https://github.com/InvadingOctopus/octopuskit) — 2D ECS game engine in 100% Swift + SwiftUI for iOS, macOS, tvOS · cross-engine · type: 2D · Swift · license: Apache-2.0 · ⭐ 487
- [LastOliveGames/becsy](https://github.com/LastOliveGames/becsy) — A multithreaded Entity Component System (ECS) for TypeScript and JavaScript, inspired by ECSY and bitecs. · cross-engine · TypeScript · license: MIT · ⭐ 299
- [kovacsv/VisualScriptEngine](https://github.com/kovacsv/VisualScriptEngine) — A C++ visual scripting engine designed for embedding. · cross-engine · C++ · license: MIT · ⭐ 222
- [Glade-tool/glade-mcp](https://github.com/Glade-tool/glade-mcp) — Connect AI coding clients to Godot and Unity editors with editor-aware tools and project context. · engine: Godot, Unity · C# · license: MIT · ⭐ 205

### Gameplay systems, physics & AI

- [liabru/matter-js](https://github.com/liabru/matter-js) — a 2D rigid body physics engine for the web ▲● ■ · cross-engine · type: 2D · JavaScript · license: MIT · ⭐ 18659
- [bulletphysics/bullet3](https://github.com/bulletphysics/bullet3) — Bullet Physics SDK: real-time collision detection and multi-physics simulation for VR, games, visual effects, robotics, machine learning etc. · cross-engine · type: VR & XR · C++ · license: NOASSERTION · ⭐ 14876
- [jrouwe/JoltPhysics](https://github.com/jrouwe/JoltPhysics) — A multi core friendly rigid body physics and collision detection library. Written in C++. Suitable for games and VR applications. Used by Horizon Forbidden West and Death Stranding 2. · cross-engine · type: VR & XR · C++ · license: MIT · ⭐ 12349
- [recastnavigation/recastnavigation](https://github.com/recastnavigation/recastnavigation) — Industry-standard navigation-mesh toolset for games · cross-engine · type: 3D, Strategy & simulation · C++ · license: Zlib · ⭐ 8201
- [galacean/engine](https://github.com/galacean/engine) — A typescript interactive engine, support 2D, 3D, animation, physics, built on WebGL and glTF. · cross-engine · type: 2D, 3D · TypeScript · license: MIT · ⭐ 5921
- [piqnt/planck.js](https://github.com/piqnt/planck.js) — 2D JavaScript Physics Engine · cross-engine · type: 2D · TypeScript · license: MIT · ⭐ 5322
- [RandyGaul/cute_headers](https://github.com/RandyGaul/cute_headers) — Collection of cross-platform one-file C/C++ libraries with no dependencies, primarily used for games · cross-engine · C · license: NOASSERTION · ⭐ 5102
- [schteppe/p2.js](https://github.com/schteppe/p2.js) — JavaScript 2D physics library · cross-engine · type: 2D · JavaScript · license: NOASSERTION · ⭐ 2694
- [DanielChappuis/reactphysics3d](https://github.com/DanielChappuis/reactphysics3d) — Open source C++ physics engine library in 3D · cross-engine · type: 3D · C++ · license: Zlib · ⭐ 1776
- [gurkenlabs/litiengine](https://github.com/gurkenlabs/litiengine) — LITIENGINE 🕹 The Java 2D game engine. · cross-engine · type: 2D · Java · license: MIT · ⭐ 843
- [xissburg/edyn](https://github.com/xissburg/edyn) — Edyn is a real-time physics engine organized as an ECS. · cross-engine · C++ · license: MIT · ⭐ 795
- [Genbox/VelcroPhysics](https://github.com/Genbox/VelcroPhysics) — High performance 2D collision detection system with realistic physics responses. · cross-engine · type: 2D · C# · license: MIT · ⭐ 749
- [anuraghazra/Verly.js](https://github.com/anuraghazra/Verly.js) — :red_circle::wavy_dash::large_blue_circle::wavy_dash::black_circle: Easy to integrate Verlet physics engine. :link: · cross-engine · type: 2D · JavaScript · license: MIT · ⭐ 711
- [jrouwe/JoltPhysics.js](https://github.com/jrouwe/JoltPhysics.js) — Port of JoltPhysics to JavaScript using emscripten · cross-engine · type: VR & XR · C++ · license: MIT · ⭐ 590
- [notgiven688/jitterphysics2](https://github.com/notgiven688/jitterphysics2) — Fast, simple to use, and dependency-free physics engine written in C# with a clear and user-friendly API. · cross-engine · C# · license: MIT · ⭐ 457
- [milcktoast/particulate-js](https://github.com/milcktoast/particulate-js) — Particle physics micro library. · cross-engine · JavaScript · license: MIT · ⭐ 353
- [ikpil/Box2D.NET](https://github.com/ikpil/Box2D.NET) — Box2D.NET - a C# port of Box2D, is a 2D physics engine for games, .NET, Unity3D, servers · cross-engine · type: 2D · C# · license: MIT · ⭐ 228
- [mgerhardy/simpleai](https://github.com/mgerhardy/simpleai) — C++ behavior-tree AI library with a remote debugger and optional Lua bindings. · cross-engine · C++ · license: NOASSERTION · ⭐ 177
- [BeRo1985/kraft](https://github.com/BeRo1985/kraft) — Kraft Physics Engine is an open source Object Pascal physics engine library that can be used in 3D games. · cross-engine · type: 3D · Pascal · license: not detected · ⭐ 132
- [noonat/intersect](https://github.com/noonat/intersect) — An explanation of 2D collision tests in JavaScript · cross-engine · type: 2D · TypeScript · license: Zlib · ⭐ 93

### Rendering, shaders & visual effects

- [google/filament](https://github.com/google/filament) — Filament is a real-time physically based rendering engine for Android, iOS, Windows, Linux, macOS, WebGPU, and WebGL2 · cross-engine · type: 3D · C++ · license: Apache-2.0 · ⭐ 20771
- [gfx-rs/wgpu](https://github.com/gfx-rs/wgpu) — A cross-platform, safe, pure-Rust graphics API. · cross-engine · Rust · license: Apache-2.0 · ⭐ 18580
- [playcanvas/engine](https://github.com/playcanvas/engine) — Open-source web graphics engine built on WebGPU and WebGL2 · cross-engine · type: 3D · JavaScript · license: MIT · ⭐ 17330
- [jonobr1/two.js](https://github.com/jonobr1/two.js) — A renderer agnostic two-dimensional drawing api for the web · cross-engine · type: 2D · JavaScript · license: MIT · ⭐ 8752
- [gpuweb/gpuweb](https://github.com/gpuweb/gpuweb) — Where the GPU for the Web work happens! · cross-engine · Bikeshed · license: NOASSERTION · ⭐ 5536
- [LWJGL/lwjgl3](https://github.com/LWJGL/lwjgl3) — LWJGL is a Java library that enables cross-platform access to popular native APIs useful in the development of graphics (OpenGL, Vulkan, bgfx), audio (OpenAL, Opus), parallel computing (OpenCL, CUDA) and XR (OpenVR… · cross-engine · type: VR & XR · Java · license: BSD-3-Clause · ⭐ 5492
- [vulkano-rs/vulkano](https://github.com/vulkano-rs/vulkano) — Safe and rich Rust wrapper around the Vulkan API · cross-engine · Rust · license: Apache-2.0 · ⭐ 5193
- [dfranx/SHADERed](https://github.com/dfranx/SHADERed) — Lightweight, cross-platform & full-featured shader IDE · cross-engine · C++ · license: MIT · ⭐ 4814
- [OGRECave/ogre](https://github.com/OGRECave/ogre) — high-performance rendering backend (C++, Python, C#, Java) · cross-engine · type: 3D · C++ · license: MIT · ⭐ 4708
- [DiligentGraphics/DiligentEngine](https://github.com/DiligentGraphics/DiligentEngine) — A modern cross-platform low-level graphics library and rendering framework · cross-engine · type: 3D · Batchfile · license: Apache-2.0 · ⭐ 4519
- [opentk/opentk](https://github.com/opentk/opentk) — The Open Toolkit library is a fast, low-level C# wrapper for OpenGL, OpenAL & OpenCL. · cross-engine · C# · license: NOASSERTION · ⭐ 3548
- [microsoft/DirectXTK](https://github.com/microsoft/DirectXTK) — The DirectX Tool Kit (aka DirectXTK) is a collection of helper classes for writing DirectX 11.x code in C++ · cross-engine · C++ · license: MIT · ⭐ 2875
- [LukasBanana/LLGL](https://github.com/LukasBanana/LLGL) — Low Level Graphics Library (LLGL) is a thin abstraction layer for the modern graphics APIs OpenGL, Direct3D, Vulkan, and Metal · cross-engine · C++ · license: BSD-3-Clause · ⭐ 2650
- [shader-park/shader-park-core](https://github.com/shader-park/shader-park-core) — A JavaScript library for creating real-time 2D and 3D shaders. JS -> Shader. https://shaderpark.com/ https://twitter.com/shaderpark · cross-engine · type: 2D, 3D · JavaScript · license: MIT · ⭐ 834
- [KTStephano/StratusGFX](https://github.com/KTStephano/StratusGFX) — Realtime 3D rendering engine · cross-engine · type: 3D · C++ · license: MPL-2.0 · ⭐ 823
- [kool-engine/kool](https://github.com/kool-engine/kool) — A Vulkan / WebGPU / OpenGL engine for Desktop JVM, Android and Javascript written in Kotlin · cross-engine · type: 3D · Kotlin · license: Apache-2.0 · ⭐ 598
- [alaingalvan/CrossShader](https://github.com/alaingalvan/CrossShader) — ⚔️ A tool for cross compiling shaders. Convert between GLSL, HLSL, Metal Shader Language, or older versions of GLSL. · cross-engine · C++ · license: MIT · ⭐ 309

### Art, sprites, animation & 3D

- [animate-css/animate.css](https://github.com/animate-css/animate.css) — 🍿 A cross-browser library of CSS animations. As easy to use as an easy thing. · cross-engine · CSS · license: NOASSERTION · ⭐ 83028
- [greensock/GSAP](https://github.com/greensock/GSAP) — GSAP (GreenSock Animation Platform), a JavaScript animation library for the modern web · cross-engine · JavaScript · license: not detected · ⭐ 30918
- [blender/blender](https://github.com/blender/blender) — Official mirror of Blender · cross-engine · type: 3D · C++ · license: NOASSERTION · ⭐ 22209
- [konvajs/konva](https://github.com/konvajs/konva) — Konva.js is an HTML5 Canvas JavaScript framework for interactive graphics, design editors, whiteboards, and diagrams. Scene graph with events, drag and drop, transforms, animations, and export. · cross-engine · TypeScript · license: NOASSERTION · ⭐ 15003
- [piskelapp/piskel](https://github.com/piskelapp/piskel) — Web-based sprite and pixel-art editor. · cross-engine · type: 2D · JavaScript · license: Apache-2.0 · ⭐ 13000
- [Orama-Interactive/Pixelorama](https://github.com/Orama-Interactive/Pixelorama) — Unleash your creativity with Pixelorama, a powerful and accessible open-source pixel art multitool. · engine: Godot · type: 2D · GDScript · license: MIT · ⭐ 11147
- [tweenjs/tween.js](https://github.com/tweenjs/tween.js) — JavaScript/TypeScript animation engine · cross-engine · TypeScript · license: NOASSERTION · ⭐ 10159
- [a1studmuffin/SpaceshipGenerator](https://github.com/a1studmuffin/SpaceshipGenerator) — A Blender script to procedurally generate 3D spaceships · cross-engine · type: 3D · Python · license: NOASSERTION · ⭐ 7869
- [RodZill4/material-maker](https://github.com/RodZill4/material-maker) — A procedural textures authoring and 3D model painting tool based on the Godot game engine · engine: Godot · type: 3D · GDScript · license: MIT · ⭐ 6272
- [armory3d/armorpaint](https://github.com/armory3d/armorpaint) — Graphics Creation Tools · cross-engine · type: 3D · C · license: NOASSERTION · ⭐ 5507
- [armory3d/armory](https://github.com/armory3d/armory) — 3D Engine with Blender Integration · cross-engine · type: 3D · C++ · license: Zlib · ⭐ 3373
- [guillaumechereau/goxel](https://github.com/guillaumechereau/goxel) — Goxel: Free and Open Source 3D Voxel Editor · cross-engine · type: 3D · C++ · license: GPL-3.0 · ⭐ 3242
- [guillaumeblanc/ozz-animation](https://github.com/guillaumeblanc/ozz-animation) — Open source c++ skeletal animation library and toolset · cross-engine · C++ · license: NOASSERTION · ⭐ 3149
- [daybrush/scenejs](https://github.com/daybrush/scenejs) — 🎬 Scene.js is JavaScript & CSS timeline-based animation library · cross-engine · TypeScript · license: MIT · ⭐ 2788
- [Bingeljell/image-to-3dlab](https://github.com/Bingeljell/image-to-3dlab) — AssetFurnace: the most complete open-source image-to-3D pipeline (Oct 2026). Prompt or picture → textured, rigged, animated game character, locally on Apple Silicon or NVIDIA. · engine: Godot, Unity · type: 3D · Python · license: Apache-2.0 · ⭐ 1215
- [sketchpunklabs/ossos](https://github.com/sketchpunklabs/ossos) — Webbased Character Animation System · cross-engine · TypeScript · license: MIT · ⭐ 508
- [papercraftgames/folded-paper-engine](https://github.com/papercraftgames/folded-paper-engine) — A custom Blender-to-Godot addon that makes level and gameplay creation as easy as a few clicks! · engine: Godot · GDScript · license: MIT · ⭐ 175
- [openfl/actuate](https://github.com/openfl/actuate) — Actuate is a flexible, fast "tween" library for animations in Haxe · cross-engine · Haxe · license: MIT · ⭐ 161
- [pawsgineer/b3d_paws_bakery](https://github.com/pawsgineer/b3d_paws_bakery) — PAWS Bakery is a Blender add-on that speeds up the Texture Baking pipeline for Game-Ready assets · cross-engine · Python · license: GPL-3.0 · ⭐ 30

### Levels & world building

- [mapeditor/tiled](https://github.com/mapeditor/tiled) — Flexible level editor · cross-engine · C++ · license: NOASSERTION · ⭐ 13080
- [Azgaar/Fantasy-Map-Generator](https://github.com/Azgaar/Fantasy-Map-Generator) — Web application generating interactive and highly customizable maps · cross-engine · TypeScript · license: NOASSERTION · ⭐ 6225
- [deepnight/ldtk](https://github.com/deepnight/ldtk) — Modern, lightweight and efficient 2D level editor · cross-engine · type: 2D · Haxe · license: MIT · ⭐ 4992
- [TrenchBroom/TrenchBroom](https://github.com/TrenchBroom/TrenchBroom) — Cross-Platform Level Editor · cross-engine · C++ · license: GPL-3.0 · ⭐ 2916
- [Jaysmito101/TerraForge3D](https://github.com/Jaysmito101/TerraForge3D) — Cross-platform procedural terrain-generation and texturing tool. · cross-engine · type: 3D, Sandbox & procedural worlds · C++ · license: MIT · ⭐ 1268
- [sirjuddington/SLADE](https://github.com/sirjuddington/SLADE) — It's a Doom editor · cross-engine · C++ · license: GPL-2.0 · ⭐ 884
- [H2xDev/GodotVMF](https://github.com/H2xDev/GodotVMF) — Run Valve Hammer (VMF) maps in Godot Engine · engine: Godot · GDScript · license: MIT · ⭐ 421
- [adrien-bon/bevy_ecs_tiled](https://github.com/adrien-bon/bevy_ecs_tiled) — Helpers for working with 2D tilemaps created with the Tiled map editor · cross-engine · type: 2D · Rust · license: MIT · ⭐ 181

### Asset pipelines & formats

- [aseprite/aseprite](https://github.com/aseprite/aseprite) — Animated sprite editor & pixel art tool (Windows, macOS, Linux) · cross-engine · type: 2D · C++ · license: not detected · ⭐ 41023
- [LibreSprite/LibreSprite](https://github.com/LibreSprite/LibreSprite) — Animated sprite editor & pixel art tool -- Fork of the last GPLv2 commit of Aseprite · cross-engine · type: 2D · C++ · license: GPL-2.0 · ⭐ 8819
- [jkuhlmann/cgltf](https://github.com/jkuhlmann/cgltf) — :diamond_shape_with_a_dot_inside: Single-file glTF 2.0 loader and writer written in C99 · cross-engine · type: 3D · C · license: MIT · ⭐ 2034
- [KhronosGroup/glTF-Blender-IO](https://github.com/KhronosGroup/glTF-Blender-IO) — Blender glTF 2.0 importer and exporter · cross-engine · Python · license: Apache-2.0 · ⭐ 1683
- [KhronosGroup/KTX-Software](https://github.com/KhronosGroup/KTX-Software) — KTX (Khronos Texture) Library and Tools · cross-engine · C++ · license: NOASSERTION · ⭐ 1405
- [Hugo-Dz/spritefusion-sprite-normals](https://github.com/Hugo-Dz/spritefusion-sprite-normals) — Generate normal maps from sprites and animated sprite sheets. · cross-engine · type: 2D · Rust · license: MIT · ⭐ 840
- [LayrKits/Sprite-Pipeline](https://github.com/LayrKits/Sprite-Pipeline) — 2D Sprite Sheet Creation Pipeline · cross-engine · type: 2D · Python · license: not detected · ⭐ 600
- [mrven/Blender-Asset-Creation-Toolset](https://github.com/mrven/Blender-Asset-Creation-Toolset) — Many Tools for Game Asset Creation (Import/Export FBXs, Origin Aligment Tool, Renaming, Low-Poly Art workflow tools, etc.) · cross-engine · Python · license: GPL-3.0 · ⭐ 374
- [openaigames/OpenAIGamesDesigner](https://github.com/openaigames/OpenAIGamesDesigner) — Skills, asset pipelines, and runtime tools for AI-assisted game development with Godot, Unity, Unreal Engine, Three.js, and Phaser. · engine: Godot, Unity, Unreal Engine, Phaser, Three.js · Python · license: MIT · ⭐ 27
- [quinteroac/ComfyUI-GameAssetsMaker](https://github.com/quinteroac/ComfyUI-GameAssetsMaker) — Custom ComfyUI nodes for game asset preparation workflows. · cross-engine · Python · license: not detected · ⭐ 27

### Audio & music

- [goldfire/howler.js](https://github.com/goldfire/howler.js) — Javascript audio library for the modern web. · cross-engine · JavaScript · license: MIT · ⭐ 25451
- [Tonejs/Tone.js](https://github.com/Tonejs/Tone.js) — A Web Audio framework for making interactive music in the browser. · cross-engine · TypeScript · license: MIT · ⭐ 14933
- [CreateJS/SoundJS](https://github.com/CreateJS/SoundJS) — A Javascript library for working with Audio. It provides a consistent API for loading and playing audio on different browsers and devices. · cross-engine · JavaScript · license: MIT · ⭐ 4598
- [ValveSoftware/steam-audio](https://github.com/ValveSoftware/steam-audio) — Steam Audio · cross-engine · type: VR & XR · C++ · license: Apache-2.0 · ⭐ 3007
- [faiface/beep](https://github.com/faiface/beep) — A little package that brings sound to any Go application. Suitable for playback and audio-processing. · cross-engine · Go · license: MIT · ⭐ 2224
- [milkytracker/MilkyTracker](https://github.com/milkytracker/MilkyTracker) — A Fasttracker II compatible music editor · cross-engine · C++ · license: NOASSERTION · ⭐ 2136
- [Theodeus/tuna](https://github.com/Theodeus/tuna) — An audio effects library for the Web Audio API. · cross-engine · JavaScript · license: not detected · ⭐ 1835
- [naomiaro/waveform-playlist](https://github.com/naomiaro/waveform-playlist) — Multitrack Web Audio editor and player with canvas waveform preview. Set cues, fades and shift multiple tracks in time. Record audio tracks or provide audio annotations. · cross-engine · TypeScript · license: MIT · ⭐ 1695
- [increpare/bfxr](https://github.com/increpare/bfxr) — Flash + AIR sound effects generator. Based on Sfxr. · cross-engine · ActionScript · license: not detected · ⭐ 1028
- [KilledByAPixel/ZzFX](https://github.com/KilledByAPixel/ZzFX) — A Tiny JavaScript Sound FX System · cross-engine · JavaScript · license: MIT · ⭐ 816
- [Dn-Programming-Core-Management/Dn-FamiTracker](https://github.com/Dn-Programming-Core-Management/Dn-FamiTracker) — modifications and improvements for 0CC-FamiTracker (based on j0CC-FamiTracker 0.6.3) · cross-engine · C · license: NOASSERTION · ⭐ 540
- [chr15m/jsfxr](https://github.com/chr15m/jsfxr) — JavaScript sound effects generator. · cross-engine · JavaScript · license: Unlicense · ⭐ 467
- [increpare/bfxr2](https://github.com/increpare/bfxr2) — bfxr.net in javascript, with more things! · cross-engine · HTML · license: MIT · ⭐ 355
- [nicolas-van/sonant-x](https://github.com/nicolas-van/sonant-x) — Small JavaScript synthesizer library · cross-engine · JavaScript · license: Zlib · ⭐ 250
- [meshula/LabMidi](https://github.com/meshula/LabMidi) — Midi IN and OUT. Standard midi file parser and player. Midi Softsynth implementation. · cross-engine · type: 3D · C++ · license: NOASSERTION · ⭐ 92
- [AmplitudeAudio/sdk](https://github.com/AmplitudeAudio/sdk) — A powerful cross-platform audio engine, optimized for games. · cross-engine · C++ · license: Apache-2.0 · ⭐ 83
- [inexorgame/audioaugust](https://github.com/inexorgame/audioaugust) — A self made set of sounds. · cross-engine · license: CC-BY-4.0 · ⭐ 27

### UI, input, accessibility & localization

- [ocornut/imgui](https://github.com/ocornut/imgui) — Immediate-mode graphical UI library for C++ tools and runtime interfaces. · cross-engine · C++ · license: MIT · ⭐ 77171
- [cegui/cegui](https://github.com/cegui/cegui) — Crazy Eddie's GUI library is a versatile, fast, adjustable, multi-platform, C++ library for creating graphical user interfaces for games and rendering applications · cross-engine · C++ · license: MIT · ⭐ 584
- [rouges78/GameStringer](https://github.com/rouges78/GameStringer) — Desktop app that auto-detects a game's engine, extracts the text, translates it with local or cloud AI, and re-applies the patch. 20+ engines, 20+ AI providers, 11 UI languages. · engine: Godot, Unity, Unreal Engine, Ren’Py · type: RPG & roguelike · TypeScript · license: NOASSERTION · ⭐ 143
- [mikrima/UnityAccessibilityPlugin](https://github.com/mikrima/UnityAccessibilityPlugin) — The UI Accessibility Plugin (UAP) allows you to make your UI accessible to blind and visually impaired players on Windows, Android, iOS, Mac and WebGL. · cross-engine · C# · license: Apache-2.0 · ⭐ 85
- [mtwilliams/libgamepad](https://github.com/mtwilliams/libgamepad) — :video_game: Cross-platform library for gamepad input. MIT licensed. · cross-engine · C · license: MIT · ⭐ 25
- [OwlcatGames/LocalizationTool](https://github.com/OwlcatGames/LocalizationTool) — A tool for creating and maintaining game's localization resources · cross-engine · C# · license: MIT · ⭐ 18
- [GasimoCodes/Subtitler](https://github.com/GasimoCodes/Subtitler) — A simple subtitle tool for Unity3D inspired by Source Engine Closed Captions · cross-engine · HTML · license: MIT · ⭐ 11

### Networking & multiplayer

- [heroiclabs/nakama](https://github.com/heroiclabs/nakama) — Scalable open-source game backend server: multiplayer, matchmaking, leaderboards, chat, and social features for games. · engine: Godot, Unity, Unreal Engine · type: Multiplayer & online · Go · license: Apache-2.0 · ⭐ 13750
- [ValveSoftware/GameNetworkingSockets](https://github.com/ValveSoftware/GameNetworkingSockets) — Reliable & unreliable messages over UDP. Robust message fragmentation & reassembly. P2P networking / NAT traversal. Encryption. · cross-engine · type: Multiplayer & online · C++ · license: BSD-3-Clause · ⭐ 10087
- [colyseus/colyseus](https://github.com/colyseus/colyseus) — ⚔ Multiplayer Framework for Node.js · cross-engine · type: Multiplayer & online · TypeScript · license: MIT · ⭐ 7561
- [pond3r/ggpo](https://github.com/pond3r/ggpo) — Good Game, Peace Out Rollback Network SDK · cross-engine · type: Multiplayer & online · C++ · license: MIT · ⭐ 3627
- [facebookarchive/RakNet](https://github.com/facebookarchive/RakNet) — RakNet is a cross platform, open source, C++ networking engine for game programmers. · cross-engine · type: Multiplayer & online · HTML · license: NOASSERTION · ⭐ 3424 · ARCHIVED
- [lsalzman/enet](https://github.com/lsalzman/enet) — ENet reliable UDP networking library · cross-engine · type: Multiplayer & online · C · license: MIT · ⭐ 3305
- [mas-bandwidth/yojimbo](https://github.com/mas-bandwidth/yojimbo) — A network library for client/server games written in C++ · cross-engine · type: Multiplayer & online · C++ · license: BSD-3-Clause · ⭐ 2759
- [mas-bandwidth/netcode](https://github.com/mas-bandwidth/netcode) — Secure client/server protocol for multiplayer games built on top of UDP · cross-engine · type: Multiplayer & online · C · license: BSD-3-Clause · ⭐ 2607
- [zpl-c/librg](https://github.com/zpl-c/librg) — 🚀 Making multi-player gamedev simpler since 2017 · cross-engine · type: Multiplayer & online · C · license: BSD-3-Clause · ⭐ 1520
- [SirFroweey/PyDark](https://github.com/SirFroweey/PyDark) — PyDark is a 2D and Online Multiplayer video game framework written on-top of Python and PyGame. · cross-engine · type: 2D, Multiplayer & online · Python · license: not detected · ⭐ 220
- [GodotSteam/MultiplayerPeer](https://github.com/GodotSteam/MultiplayerPeer) — An ecosystem of tools for Godot Engine and Valve's Steam. For the Windows, Linux, and Mac platforms. · engine: Godot · type: Multiplayer & online · license: not detected · ⭐ 131 · ARCHIVED
- [albertok/godot-rocket-league](https://github.com/albertok/godot-rocket-league) — Network physics with rollback test using Godot and netfox · engine: Godot · type: Multiplayer & online · GDScript · license: MIT · ⭐ 126
- [donislawdev/BeanNetworkTester](https://github.com/donislawdev/BeanNetworkTester) — Simulate bad network conditions on Windows/Linux - latency, burst packet loss, jitter, bandwidth limits, drops - to test how your app behaves on a poor connection. GUI + CLI, comes with network tools · cross-engine · Python · license: GPL-3.0 · ⭐ 77
- [Kaigen-Technologies/net-crowd-stress-test](https://github.com/Kaigen-Technologies/net-crowd-stress-test) — A plaza of networked players on one server: a netcode stress test for the Kaigen Engine · cross-engine · type: 3D, Multiplayer & online · C · license: MIT · ⭐ 23

### Backend, persistence & live operations

- [agones-dev/agones](https://github.com/agones-dev/agones) — Dedicated Game Server Hosting and Scaling for Multiplayer Games on Kubernetes · cross-engine · type: Multiplayer & online · Go · license: Apache-2.0 · ⭐ 7107
- [googleforgames/open-match](https://github.com/googleforgames/open-match) — Flexible, extensible, and scalable video game matchmaking. · cross-engine · type: Multiplayer & online · Go · license: Apache-2.0 · ⭐ 3428
- [heroiclabs/nakama-godot](https://github.com/heroiclabs/nakama-godot) — Nakama Godot Client SDK · engine: Godot · type: Multiplayer & online · GDScript · license: Apache-2.0 · ⭐ 786
- [TaloDev/godot](https://github.com/TaloDev/godot) — Talo's Godot plugin for open source leaderboards, stats, auth, game saves and more · engine: Godot · GDScript · license: MIT · ⭐ 251
- [googleforgames/open-saves](https://github.com/googleforgames/open-saves) — Open Saves is a cloud native data store for game development. · cross-engine · Go · license: Apache-2.0 · ⭐ 243
- [heroiclabs/nakama-js](https://github.com/heroiclabs/nakama-js) — Nakama JavaScript Client SDK · cross-engine · type: Multiplayer & online · TypeScript · license: Apache-2.0 · ⭐ 221
- [GameAnalytics/GA-SDK-GODOT](https://github.com/GameAnalytics/GA-SDK-GODOT) — Official GameAnalytics Godot SDK repository · engine: Godot · Objective-C · license: MIT · ⭐ 65
- [googleforgames/open-match2](https://github.com/googleforgames/open-match2) — Open Match 2 core application and API/protobuf implementation for building matchmaking services. · cross-engine · type: Multiplayer & online · Go · license: Apache-2.0 · ⭐ 63
- [heroiclabs/hiro](https://github.com/heroiclabs/hiro) — The server interface for the Hiro game framework. · cross-engine · Go · license: Apache-2.0 · ⭐ 61
- [GameAnalytics/GA-SDK-JAVASCRIPT](https://github.com/GameAnalytics/GA-SDK-JAVASCRIPT) — Official repository for GameAnalytics JavaScript SDK · cross-engine · TypeScript · license: MIT · ⭐ 24

### Testing & QA

- [bitwes/Gut](https://github.com/bitwes/Gut) — Godot Unit Test. Unit testing tool for Godot Game Engine. · engine: Godot · GDScript · license: not detected · ⭐ 2786
- [godot-gdunit-labs/gdUnit4](https://github.com/godot-gdunit-labs/gdUnit4) — Embedded unit testing framework for Godot 4 supporting GDScript and C#. Features test-driven development, embedded test inspector, extensive assertions, mocking, scene testing. · engine: Godot · GDScript · license: MIT · ⭐ 1308
- [MikeSchulze/gdUnit3](https://github.com/MikeSchulze/gdUnit3) — Godot 3 unit-testing framework for GDScript and C#. · engine: Godot · GDScript · license: MIT · ⭐ 320
- [waiterve/wai-play](https://github.com/waiterve/wai-play) — AI-based web-game testing and quality-evaluation platform. · cross-engine · Python · license: not detected · ⭐ 256
- [chickensoft-games/GoDotTest](https://github.com/chickensoft-games/GoDotTest) — C# test runner for Godot. Run tests from the command line, collect code coverage, and debug tests. · engine: Godot · C# · license: MIT · ⭐ 158
- [chickensoft-games/GodotTestDriver](https://github.com/chickensoft-games/GodotTestDriver) — Easy integration testing for Godot with simulated input, node drivers, and fixtures. · engine: Godot · C# · license: MIT · ⭐ 63
- [masteryee-labs/Open-Godot-MCP](https://github.com/masteryee-labs/Open-Godot-MCP) — Open-source MCP server for AI-autonomous Godot game development. Deterministic playtesting, multiplayer testing, DAP debugging, LSP, token-efficient. 100% MIT. · engine: Godot · type: Multiplayer & online · GDScript · license: MIT · ⭐ 15

### Debugging & profiling

- [wolfpld/tracy](https://github.com/wolfpld/tracy) — Frame profiler · cross-engine · C++ · license: NOASSERTION · ⭐ 17143
- [baldurk/renderdoc](https://github.com/baldurk/renderdoc) — RenderDoc is a stand-alone graphics debugging tool. · cross-engine · C++ · license: MIT · ⭐ 11335
- [bombomby/optick](https://github.com/bombomby/optick) — C++ Profiler For Games · cross-engine · C# · license: MIT · ⭐ 3163
- [GameTechDev/PresentMon](https://github.com/GameTechDev/PresentMon) — Capture and analyze the high-level performance characteristics of graphics applications on Windows. · cross-engine · C++ · license: MIT · ⭐ 2682
- [godot-extended-libraries/godot-debug-menu](https://github.com/godot-extended-libraries/godot-debug-menu) — Display in-game FPS/performance/hardware metrics in a Godot 4.x project · engine: Godot · GDScript · license: MIT · ⭐ 673
- [GPUOpen-Tools/radeon_gpu_profiler](https://github.com/GPUOpen-Tools/radeon_gpu_profiler) — Radeon GPU Profiler (RGP) is a tool from AMD that allows for deep inspection of GPU workloads. · cross-engine · license: not detected · ⭐ 455
- [bbbscarter/GodotRuntimeDebugTools](https://github.com/bbbscarter/GodotRuntimeDebugTools) — A proof-of-concept Godot addon to improve the runtime debugging experience · engine: Godot · GDScript · license: MIT · ⭐ 251
- [Pineapple/GodotTracy](https://github.com/Pineapple/GodotTracy) — Tracy Profiler module for the Godot Engine · engine: Godot · Python · license: MIT · ⭐ 132
- [Zylann/zprofiler](https://github.com/Zylann/zprofiler) — A CPU time profiler for Godot Engine · engine: Godot · C++ · license: NOASSERTION · ⭐ 17

### Build, CI & release

- [abarichello/godot-ci](https://github.com/abarichello/godot-ci) — Docker image to export Godot Engine games. Templates for Gitlab CI and GitHub Actions to deploy to GitLab Pages/GitHub Pages/Itch.io. · engine: Godot · Dockerfile · license: MIT · ⭐ 1159
- [firebelley/godot-export](https://github.com/firebelley/godot-export) — Automatically exports your Godot games. · engine: Godot · TypeScript · license: MIT · ⭐ 655
- [vini-guerrero/godot-exporter](https://github.com/vini-guerrero/godot-exporter) — Godot Engine Automation Pipeline Android – iOS – Linux – MacOS – Windows – HTML5 – Itch.io. · engine: Godot · Shell · license: MIT · ⭐ 74
- [godot-gdunit-labs/gdUnit4-action](https://github.com/godot-gdunit-labs/gdUnit4-action) — 🎮 Official GdUnit4 GitHub Action for automated testing in Godot 4.x projects. Supports GDScript & C#, test reporting, and CI/CD pipeline integration. Built for game developers to streamline their testing workflow. · engine: Godot · JavaScript · license: MIT · ⭐ 63
- [bend-n/godot-actions](https://github.com/bend-n/godot-actions) — GitHub Actions for exporting Godot projects. · engine: Godot · license: MIT · ⭐ 38

### Publishing & monetization

- [GodotSteam/GodotSteam](https://github.com/GodotSteam/GodotSteam) — An ecosystem of tools for Godot Engine and Valve's Steam. For Linux, Mac, and Windows. · engine: Godot · license: not detected · ⭐ 3772 · ARCHIVED
- [Noxime/steamworks-rs](https://github.com/Noxime/steamworks-rs) — Rust bindings for the Steamworks SDK. · cross-engine · type: Multiplayer & online · Rust · license: Apache-2.0 · ⭐ 498
- [LANCommander/LANCommander](https://github.com/LANCommander/LANCommander) — Self-hosted game library and distribution platform with desktop launcher and package management. · cross-engine · C# · license: MIT · ⭐ 482
- [game-ci/steam-deploy](https://github.com/game-ci/steam-deploy) — GitHub Action for deploying a game to Steam. · cross-engine · TypeScript · license: MIT · ⭐ 349
- [Playgama/bridge](https://github.com/Playgama/bridge) — One SDK for cross-platform publishing HTML5 games · cross-engine · TypeScript · license: LGPL-3.0 · ⭐ 100
- [ArtyProf/steamworks-ffi-node](https://github.com/ArtyProf/steamworks-ffi-node) — A TypeScript/JavaScript wrapper for the Steamworks SDK using Koffi FFI, designed for Node.js and Electron applications with Steamworks SDK integration. · cross-engine · TypeScript · license: MIT · ⭐ 93
- [jasielmacedo/steam-microtransaction-api](https://github.com/jasielmacedo/steam-microtransaction-api) — An intermediate api to handle steam microtransactions using steam web services. Ready to use with Unity, Unreal, Godot and so on · engine: Godot, Unity, Unreal Engine · TypeScript · license: MIT · ⭐ 57
- [Playgama/bridge-godot-4](https://github.com/Playgama/bridge-godot-4) — One SDK for cross-platform publishing HTML5 games · engine: Godot · GDScript · license: MIT · ⭐ 47
- [CM2Walki/steampipe](https://github.com/CM2Walki/steampipe) — Dockerfile for automated build of a SteamCMD + Steamworks SDK Tools installation: https://hub.docker.com/r/cm2network/steampipe/ · cross-engine · Dockerfile · license: MIT · ⭐ 20
