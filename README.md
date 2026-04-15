# machine-template

Template monorepo for a PUDA machine edge service. Use this to scaffold a new machine integration.

## Repo Structure

```
machine-template/
├── pyproject.toml          # uv workspace root (members: edge, driver)
├── edge/
│   ├── pyproject.toml      # Edge service package
│   ├── main.py             # Main event loop — NATS + driver glue
│   ├── Dockerfile          # Container build
│   ├── compose.yml         # Docker Compose
│   └── .env.example        # Environment variable template
└── driver/
    ├── pyproject.toml      # Driver package (driver)
    ├── README.md
    └── src/
        └── driver/         # Source code
```

## AI Agent Instructions

Follow these steps in order to adapt this template for a new machine.

### 1. Choose a Machine ID

Pick a short, lowercase, hyphen-separated identifier for the machine (e.g. `centrifuge`, `bioshake`, `thermocycler`). This becomes `MACHINE_ID` everywhere. 

### 2. Complete all TODOs

Search the repo for every `TODO` marker and resolve each one — typically renaming placeholder strings, filling in package metadata, and updating import paths to match the chosen `MACHINE_ID`.

### 3. Implement the Driver

Add the machine driver source under `driver/src/driver/`. The driver must expose a class that `puda_comms.EdgeRunner` can wrap. Update `driver/pyproject.toml`:

- Add required dependencies

### 4. Wire the Driver into main.py

In `edge/main.py`:

1. Uncomment and update the driver import line.
2. Add any driver-specific fields to `Config` (e.g. device port, IP address).
3. Instantiate the driver using those config fields.
4. Remove the `driver = None` placeholder line.

### 5. Add Driver-Specific Environment Variables

In `edge/.env.example`, add any new config fields below `MACHINE_ID` (e.g. `${MACHINE_ID}_PORT`, `${MACHINE_ID}_HOST`). Keep `NATS_SERVERS` and `MACHINE_ID` as-is.

### 6. Update the Dockerfile

In `edge/Dockerfile`, uncomment the `COPY driver/` line and add any system-level dependencies your driver needs (e.g. `libusb-dev` for USB devices).



Replace this file with a machine-specific README describing what the machine does, how to connect to it, and any hardware prerequisites.

---

## Environment Setup

From repo root:

```bash
cp edge/.env.example edge/.env
```

Edit `edge/.env` and fill in:

- `MACHINE_ID` — machine identifier
- `NATS_SERVERS` — comma-separated NATS server URLs
- Any additional driver-specific variables

## Run With Docker (Recommended)

All commands below run from repo root.

Build and start:

```bash
docker compose -f edge/compose.yml up -d --build
```

View logs:

```bash
docker compose -f edge/compose.yml logs -f
```

Stop:

```bash
docker compose -f edge/compose.yml down
```

## Run Baremetal (uv)

```bash
uv sync --all-packages
uv run --package edge python edge/main.py
```

## Build and Push Image (GHCR)

Login:

```bash
echo $GITHUB_TOKEN | docker login ghcr.io -u USERNAME --password-stdin
```

Build and push:

```bash
docker compose -f edge/compose.yml build
docker compose -f edge/compose.yml push
```

## Notes

- Docker build context is workspace root (`..` in `edge/compose.yml`).
- Dockerfile path is `edge/Dockerfile`.
- `MACHINE_ID` in `.env` is used for NATS subject routing and Docker image/container naming.
