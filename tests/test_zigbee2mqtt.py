"""Python client for Zigbee2MQTT."""
import pytest

from zigbee2mqtt import Zigbee2MQTT


@pytest.mark.asyncio
async def test_something() -> None:
    """Test Something."""
    z2m = Zigbee2MQTT(base_topic="/zigbee2mqtt")
    assert z2m.base_topic == "/zigbee2mqtt"
