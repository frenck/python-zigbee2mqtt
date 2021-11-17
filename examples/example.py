"""Python client for Zigbee2MQTT."""
import asyncio

from zigbee2mqtt import Zigbee2MQTT


async def main():
    """Show example on using the Zigbee2MQTT client."""
    z2m = Zigbee2MQTT(
        base_topic="/zigbee2mqtt",
    )
    print(z2m.base_topic)


if __name__ == "__main__":
    asyncio.run(main())
