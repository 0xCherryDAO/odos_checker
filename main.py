from asyncio import run, set_event_loop_policy
import asyncio
import logging
import sys
import random

from config import SHUFFLE_WALLETS
from src.utils.data.helper import addresses

from src.utils.runner import process_checker

logging.getLogger("asyncio").setLevel(logging.CRITICAL)

logging.basicConfig(level=logging.CRITICAL)

if sys.platform == 'win32':
    set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


async def main() -> None:
    if SHUFFLE_WALLETS:
        random.shuffle(addresses)
    await process_checker(addresses)


if __name__ == '__main__':
    run(main())
