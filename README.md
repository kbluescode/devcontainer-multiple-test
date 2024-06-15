# devcontainer-multiple-test

This repo represents a frontend app (SvelteKit), backend app (Python Flask) that work together with a reverse proxy (Caddy) and database (RedisStack). 

Idea from https://code.visualstudio.com/remote/advancedcontainers/connect-multiple-containers

## Goal
- Test a devcontainer-based workflow that involves multiple services
- Share configs, secrets and environments
- Uses docker compose as the orchestration layer