import yaml
import os
import subprocess
import pathlib

def run_command(command, description):
    print(f"[RUNNING] {description}...")
    try:
        subprocess.run(command, shell=True, check=True, capture_output=True)
        print(f"[SUCCESS] {description}")
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] {description}: {e.stderr.decode()}")

def bootstrap():
    # 1. Load Manifest
    with open("boby_system_manifest.yaml", "r") as f:
        manifest = yaml.safe_load(f)

    meta = manifest['metadata']
    env_setup = manifest['environment_setup']
    sec_policy = manifest['security_policy']

    print(f"--- INITIALIZING BOOTSTRAP: {meta['entity']} ({meta['protocol']}) ---")

    # 2. Set Global Git Configuration
    git_conf = env_setup['git_configuration']
    run_command(f"git config --global user.name '{git_conf['user_name']}'", "Setting Global Git User")
    
    # 3. Create Global .gitignore
    home = str(pathlib.Path.home())
    gitignore_path = os.path.join(home, ".gitignore_global")
    with open(gitignore_path, "w") as f:
        f.write("\n".join(git_conf['global_ignore']))
    run_command(f"git config --global core.excludesfile {gitignore_path}", "Configuring Global Gitignore")

    # 4. Enforce Local Identity Hooks (Pre-commit)
    hook_content = f"""#!/bin/bash
FORBIDDEN="{sec_policy['legacy_block']['pattern']}"
MATCHES=$(git diff --cached --name-only | xargs grep -i "$FORBIDDEN" 2>/dev/null)
if [ -n "$MATCHES" ]; then
    echo "CRITICAL: Legacy identity '$FORBIDDEN' detected in staged files."
    exit 1
fi
exit 0
"""
    # Pasang pada repo semasa jika ada .git
    if os.path.exists(".git"):
        hook_path = ".git/hooks/pre-commit"
        with open(hook_path, "w") as f:
            f.write(hook_content)
        run_command(f"chmod +x {hook_path}", "Enabling Identity Guard Hook")

    # 5. Export Environment Variables to .env
    env_vars = env_setup['global_variables']
    with open(".env", "a+") as f:
        f.seek(0)
        content = f.read()
        for key, value in env_vars.items():
            line = f'{key}="{value}"'
            if line not in content:
                f.write(f"\n{line}")
    print("[SUCCESS] Environment variables updated in .env")

    print(f"\n--- [BOOTSTRAP COMPLETE] ---")
    print(f"Entity: {meta['entity']}")
    print(f"Status: Identity Hardened & Locked.")

if __name__ == "__main__":
    bootstrap()
  
