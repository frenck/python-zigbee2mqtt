"""Python client for Zigbee2MQTT."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Zigbee2MQTT:
    """Main class for the Python Zigbee2MQTT client."""

    base_topic: str
