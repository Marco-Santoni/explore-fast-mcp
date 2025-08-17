import asyncio

from fastmcp import Client

client = Client(transport="http://localhost:8000/mcp")

async def call_tool(name: str):
    async with client:
        tools = await client.list_tools()
        print("\nAvailable tools:", tools)
        resources = await client.list_resources()
        print("\nAvailable resources:", resources)
        prompts = await client.list_prompts()
        print("\nAvailable prompts:", prompts)

        result = await client.call_tool("greet", {"name": name})
        print("\nTool call result:", result.content[0].text)

        content = await client.read_resource("resource://greeting")
        print("\nGreeting resource content:", content[0].text)

        prompt = await client.get_prompt("ask_about_topic", {"topic": "quantum computing"})
        print("\nPrompt content:", prompt.messages[0].content.text)

asyncio.run(call_tool("Ford"))