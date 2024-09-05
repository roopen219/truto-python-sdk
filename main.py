# main.py

import asyncio
from truto_python_sdk import TrutoApi

# Initialize the SDK with your token
truto_api = TrutoApi(token="9489d3df-69cb-4242-9e4e-29f41ceaad6a", base_url="https://truto-dev.truto.dev")

async def main():
    async for ticket in truto_api.unified_api.list("ticketing", "tickets", {
        "integrated_account_id": "c54bc595-486e-4bbb-8c17-20810fa4a86c"
    }):
        print(await truto_api.proxy_api.get("ticketing-tickets", ticket["id"], {
            "integrated_account_id": "c54bc595-486e-4bbb-8c17-20810fa4a86c"
        }))

# Run the async function
asyncio.run(main())