"""Legacy report generator with an outdated pinned dependency (fictional demo app)."""

import sys

import yaml


def load_config(path: str) -> dict:
    with open(path) as f:
        # Unsafe on purpose: this app is the "has a problem" demo.
        return yaml.load(f, Loader=yaml.Loader)


if __name__ == "__main__":
    cfg = load_config(sys.argv[1] if len(sys.argv) > 1 else "report.yaml")
    print(f"Generating {cfg.get('name', 'report')}")
