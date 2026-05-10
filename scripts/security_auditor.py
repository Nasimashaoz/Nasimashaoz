import json
import os
import re
import sys

# High-risk or deprecated URL shorteners
DEPRECATED_DOMAINS = [
    "git.io", "goo.gl", "t.ly", "tinyurl.com",
    "rebrand.ly", "is.gd", "goo.su", "qrco.de"
]

def check_file_for_risks(filepath):
    """Scans a file for high-risk domains and insecure URLs."""
    errors = []
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Find all URLs
        urls = re.findall(r'https?://[^\s\)\"\'\>]+', content)

        for url in urls:
            # Check for HTTP (insecure)
            if url.startswith('http://'):
                errors.append(f"Insecure URL found: {url}")

            # Check for deprecated domains
            domain = url.split('/')[2]
            if any(d in domain for d in DEPRECATED_DOMAINS):
                errors.append(f"Deprecated/High-risk domain found: {url}")

    except Exception as e:
        errors.append(f"Could not read file {filepath}: {str(e)}")

    return errors

def main():
    manifest_path = "security-map.json"
    if not os.path.exists(manifest_path):
        print(f"❌ Manifest {manifest_path} not found.")
        sys.exit(1)

    with open(manifest_path, 'r') as f:
        manifest = json.load(f)

    all_errors = []
    artifacts_scanned = set()

    print(f"🛡️ Starting Security Audit for {manifest['project']} v{manifest['version']}")

    # Parse frameworks
    frameworks = manifest.get("security_frameworks", {})
    for fw_name, controls in frameworks.items():
        print(f"\n🔍 Auditing {fw_name}:")
        for control_id, data in controls.items():
            status = data.get("status", "Unknown")
            artifacts = data.get("artifacts", [])

            if status == "Pass":
                print(f"  ✅ {control_id}: Passing")
                for art in artifacts:
                    if not os.path.exists(art):
                        all_errors.append(f"Missing artifact for {control_id}: {art}")
                    else:
                        artifacts_scanned.add(art)
            else:
                print(f"  ⚠️ {control_id}: {status}")

    # Deep scan identified artifacts
    print("\n🔬 Deep scanning artifacts for high-risk patterns:")
    for art in artifacts_scanned:
        print(f"  Scanning {art}...")
        file_errors = check_file_for_risks(art)
        for err in file_errors:
            all_errors.append(f"[{art}] {err}")

    if all_errors:
        print("\n❌ Audit Failed with the following errors:")
        for err in all_errors:
            print(f"  - {err}")
        sys.exit(1)

    print("\n🎉 All security checks passed!")
    sys.exit(0)

if __name__ == "__main__":
    main()
