# FastMCP Exploration

A simple exploration project demonstrating the Model Context Protocol (MCP) using the FastMCP library. This project showcases how to create an MCP server with tools, resources, and prompts, along with a client to interact with the server.

## Overview

This project contains:
- **MCP Server** (`server.py`): A FastMCP server that provides tools, resources, and prompts
- **MCP Client** (`client.py`): A simple client that connects to the server and calls tools

## Prerequisites

- Developed with Python 3.13
- FastMCP library 2.11

## Usage

### Running the Server

Start the MCP server with HTTP transport:

```bash
python server.py
```

The server will start on `http://localhost:8000/mcp` by default.

### Running the Client

In a separate terminal, run the client:

```bash
python client.py
```

The client will connect to the server and call the `greet` tool with the name "Ford".