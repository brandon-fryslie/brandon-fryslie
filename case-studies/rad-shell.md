# rad-shell: From Personal Tool to Open Source Project

## Overview

[rad-shell](https://github.com/brandon-fryslie/rad-shell) started as personal shell configuration in 2011 and evolved into a maintained open-source project with 41 stars, 7 forks, and 8 years of active development. It's a preconfigured Zsh environment using Prezto and Zgen, with a plugin composition model that became its signature feature.

## The Problem

Shell configuration typically exists as a tangled mess of dot files scattered across machines. Updates require manual synchronization. Adding new tools means editing multiple files. Version control is awkward—your local `.zshrc` isn't the same as your coworker's, so sharing improvements is manual.

## The Solution

The `.rad-plugins` composition model makes user configuration the single source of truth. Plugins load from any GitHub repository, enabling a modular, version-controlled approach. The system uses lazy-loading for NVM to keep startup times fast even with dozens of plugins installed.

## Technical Highlights

- **Plugin Architecture**: Declarative plugin composition via `.rad-plugins` manifest
- **Cross-platform**: Works on macOS and Linux without modification
- **Companion Project**: [rad-plugins](https://github.com/brandon-fryslie/rad-plugins) repository (3 stars, 1 fork) demonstrates the plugin pattern in practice
- **rad-spinner**: Includes procedural braille-grid animations (12×4 grid) for terminal spinners using geometric rules

## Maintenance Record

- Created: 2017 (building on shell tooling back to 2011)
- Latest commit: November 2025
- 25+ merged pull requests
- Active issue tracking and user support
- Regular dependency updates (Prezto, Zgen)

## What Changed

Most personal tools die after their creator moves on. rad-shell stayed maintained because the plugin architecture created value for others. When users file issues, they're reporting real problems in their daily workflow. When contributors submit PRs, they're improving their own tools. The composition model aligned incentives—everyone who uses it has a reason to keep it working.

## Links

- [rad-shell](https://github.com/brandon-fryslie/rad-shell) — Main repository
- [rad-plugins](https://github.com/brandon-fryslie/rad-plugins) — Example plugin collection
