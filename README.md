# Aerial Quadripod Structure

A modular steel structure designed for aerial acrobatics practice (e.g. aerial silks, hoop, trapeze). This repository contains all CAD files, welded assemblies, and the documentation needed for fabrication and assembly.

## Features

- FreeCAD models for all components and subassemblies
- Welded assemblies grouped as manufacturable parts
- CI/CD pipeline to auto-generate:
  - Fabrication plans (PDF/DXF)
  - Assembly instructions
  - Bill of materials (BOM)
- Designed for robustness, portability, and outdoor/indoor use

> [!NOTE]
> Currently, the generation of TechDraw sheets (PDF/DXF) must be done manually.
> Due to implementation challenges, full automation of this step in the CI/CD pipeline is not yet available.
> Work is ongoing to find a stable and reliable solution to automate this process in the future.

## Tech Stack

- 🧱 **FreeCAD** for 3D modeling and assemblies
- 🐍 **Python** scripts for automation
- ⚙️ **CI/CD** (Jenkins) for doc generation

## License

Open-source under the MIT License. Contributions welcome!
