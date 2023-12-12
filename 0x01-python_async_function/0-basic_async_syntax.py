#!/usr/bin/env python3
"""Task O"""
import asyncio
import random


async def wait_random(max_delay:int=10) -> float:
    """Returning a random value after a certain duration of time 1-10"""
    delay = random.random() * max_delay
    await asyncio.sleep(delay)
    return delay

