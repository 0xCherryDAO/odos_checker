import pyuseragents

from config import RETRIES, PAUSE_BETWEEN_RETRIES
from src.utils.common.wrappers.decorators import retry
from src.utils.proxy_manager import Proxy
from src.utils.request_client.client import RequestClient


class Checker(RequestClient):
    def __init__(
            self,
            address: str,
            proxy: Proxy | None
    ):
        self.wallet_address = address
        RequestClient.__init__(self, proxy=proxy)

    @retry(retries=RETRIES, delay=PAUSE_BETWEEN_RETRIES, backoff=1.5)
    async def check_for_tokens(self) -> float:
        response_json, status = await self.make_request(
            url=f'https://api.odos.xyz/loyalty/users/{self.wallet_address}/balances',
            headers={
                'accept': '*/*',
                'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
                'user-agent': pyuseragents.random(),
            }
        )
        tokens = float(response_json['data']['pendingTokenBalance']) / 10 ** 18
        return tokens
