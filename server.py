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


@mcp.resource(
        uri="resource://greeting",
        description="A resource that provides a greeting message text."
)
def get_greeting() -> str:
    """Provides a simple greeting message."""
    return "Hello from FastMCP Resources!"

@mcp.resource(
        uri="data://config",
        description="A resource that provides application configuration.",
        annotations={
            "readOnlyHint": True,
            "idempotentHint": True
        }
)
def get_config() -> dict:
    """Provides application configuration as JSON."""
    return {
        "theme": "dark",
        "version": "1.2.0",
        "features": ["tools", "resources"],
    }

@mcp.resource("weather://{city}/current")
def get_weather(city: str) -> dict:
    """Provides weather information for a specific city."""
    # In a real implementation, this would call a weather API
    # Here we're using simplified logic for example purposes
    return {
        "city": city.capitalize(),
        "temperature": 22,
        "condition": "Sunny",
        "unit": "celsius"
    }

@mcp.prompt
def ask_about_topic(topic: str) -> str:
    """Generates a user message asking for an explanation of a topic."""
    return f"Can you please explain the concept of '{topic}'?"

if __name__ == "__main__":
    print("Starting MCP server...")
    mcp.run(transport="streamable-http")
    