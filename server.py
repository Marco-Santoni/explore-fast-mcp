from fastmcp import FastMCP
from typing import Annotated

mcp = FastMCP(
    name="My MCP Server",
    instructions="An example MCP server that greets users.",
)

@mcp.tool(
        annotations={
            "title": "Greet User",
            "readOnlyHint": True,
            "idempotentHint": True,
        }
)
def greet(
    name: Annotated[str, "The name of the user to greet"]
) -> str:
    """A simple tool that greets the user."""
    return f"Hello {name} from my_tool!"


@mcp.resource("resource://greeting")
def get_greeting() -> str:
    """Provides a simple greeting message."""
    return "Hello from FastMCP Resources!"

@mcp.resource("data://config")
def get_config() -> dict:
    """Provides application configuration as JSON."""
    return {
        "theme": "dark",
        "version": "1.2.0",
        "features": ["tools", "resources"],
    }

if __name__ == "__main__":
    print("Starting MCP server...")
    mcp.run(transport="streamable-http")
    