# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is the "amadeus" project - a Python/FastAPI application following Clean Architecture principles.

## Development Environment

This project uses a devcontainer configuration with:
- Python 3.11+ runtime
- FastAPI web framework
- Development tools: git, zsh, fzf, gh (GitHub CLI), jq
- Network utilities: iptables, ipset, iproute2, dnsutils
- VS Code extensions: Python, Pylint, Black formatter with format-on-save enabled
- Claude Code CLI pre-installed globally

## Repository Structure

- FastAPI application with Clean Architecture
- Development container configured for Python development
- Git repository initialized with main branch

## Architecture Rules

This project follows Clean Architecture principles with the following layers:

### Layer Structure
1. **Entity** - Core business entities and domain models
2. **UseCase** - Application business logic
3. **Gateway** - Interfaces for external systems
4. **Repository** - Data persistence interfaces
5. **Router** - FastAPI routing and request handling

### Architecture Guidelines
- **Dependency Rule**: Dependencies must point inward. Outer layers can depend on inner layers, but not vice versa
- **Entity Layer**: Contains pure business logic with no external dependencies
- **UseCase Layer**: Orchestrates business operations using entities and repository/gateway interfaces
- **Repository/Gateway**: Define interfaces (protocols) in the use case layer, implement in the infrastructure layer
- **Router Layer**: Handles HTTP concerns using FastAPI and delegates to use cases

### Directory Structure
```
src/
├── domain/
│   ├── entities/      # Business entities (Pydantic models for domain)
│   └── repositories/  # Repository interfaces (Protocol classes)
├── usecases/         # Application business logic
├── infrastructure/
│   ├── repositories/  # Repository implementations
│   ├── gateways/     # External service implementations
│   └── database/     # Database connection and models
├── presentation/
│   ├── routers/      # FastAPI routers
│   └── schemas/      # Request/Response Pydantic models
└── main.py           # FastAPI application entry point
```

### Development Principles
- Use Pydantic for data validation and serialization
- Define repository interfaces using Python Protocol classes
- Keep FastAPI dependencies only in the presentation layer
- Use dependency injection with FastAPI's Depends()
- Test each layer independently with pytest
- Avoid framework dependencies in domain and usecase layers
- Use type hints throughout the codebase

### FastAPI Specific Guidelines
- Routers should be thin and delegate to use cases
- Use Pydantic models for request/response schemas (separate from domain entities)
- Leverage FastAPI's dependency injection for repository implementations
- Handle errors with appropriate HTTP status codes
- Use async/await for I/O operations

## Development Notes

- The devcontainer provides a complete development environment with Claude Code pre-installed
- VS Code is configured for Python development with Pylint and Black formatter
- Network capabilities are enabled for potential networking-related development
- Follow Clean Architecture principles for all new code additions
- Use FastAPI's built-in features while maintaining architectural boundaries