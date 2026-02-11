# Quiet Hours – Home Assistant Integration

Quiet Hours provides a single switch that temporarily silences your home.
It is designed for nighttime, meetings, naps, or any moment when your
smart home should calm down.

## What It Does
When enabled, Quiet Hours will:
- Mute selected media players
- Remember their previous mute state
- Restore everything when disabled

No complex automations. One switch. Total peace.

## Features
- UI-based configuration (no YAML)
- Restore-safe across restarts
- HACS compatible
- Lightweight and fast
- Designed for automation and dashboards

## Installation

### HACS (Recommended)
1. Open HACS
2. Add this repository as a custom integration
3. Install **Quiet Hours**
4. Restart Home Assistant

### Manual
Copy `custom_components/quiet_hours` into your Home Assistant
configuration directory and restart.

## Usage
Toggle the `Quiet Hours` switch manually or use it in automations:

- Night mode
- Movie time
- Meetings
- Baby nap schedules

## Example Automation
Enable Quiet Hours every night at 10 PM and disable it at 7 AM.

## Roadmap
- Light dimming support
- Notification muting
- Time-based schedules
- Calendar integration
- Per-room profiles

## Support
Issues and feature requests can be reported on GitHub.
