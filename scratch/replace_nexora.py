import os
import re

root_dir = r"c:\Desktop\nexora-website"

skip_dirs = {".git", "node_modules", ".next"}

def replace_in_file(filepath):
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
    except Exception:
        return

    original = content

    # 1. NEXORA -> HOMECRAFT
    content = content.replace("NEXORA", "HOMECRAFT")

    # 2. Nexora -> HomeCraft Services (for branding text, titles, text content)
    # But wait, avoid changing email domains if needed, or update support@nexora.in to support@homecraftservices.in / support@homecraft.com
    # Let's replace email domains: support@nexora.in -> support@homecraft.in, privacy@nexora.in -> privacy@homecraft.in
    content = content.replace("support@nexora.in", "support@homecraft.in")
    content = content.replace("privacy@nexora.in", "privacy@homecraft.in")

    # Replace 'Nexora' with 'HomeCraft Services' or 'HomeCraft' where appropriate
    # E.g. 'Nexora Assurance' -> 'HomeCraft Assurance'
    # 'Nexora Gold Standard' -> 'HomeCraft Gold Standard'
    # '© Nexora' -> '© HomeCraft Services'
    # 'Nexora' -> 'HomeCraft Services'
    content = content.replace("Nexora", "HomeCraft Services")

    # 3. nexora_ -> homecraft_ (for localStorage keys like nexora_token -> homecraft_token)
    content = content.replace("nexora_", "homecraft_")

    # 4. nexora- -> homecraft- (for preset names, folder names in cloudinary, etc.)
    content = content.replace("nexora-", "homecraft-")

    # 5. /nexora -> /homecraft
    content = content.replace("/nexora", "/homecraft")

    # 6. standalone 'nexora' -> 'homecraft'
    content = re.sub(r'\bnexora\b', 'homecraft', content)

    if content != original:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated: {filepath}")

for root, dirs, files in os.walk(root_dir):
    dirs[:] = [d for d in dirs if d not in skip_dirs]
    for file in files:
        if file.endswith((".js", ".jsx", ".ts", ".tsx", ".json", ".md", ".env", ".env.local", ".html", ".css", ".mjs")):
            replace_in_file(os.path.join(root, file))

print("Replacement complete.")
