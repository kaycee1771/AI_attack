import json

# Load attack logs
with open("caldera/logs/attack_log.json", "r") as f:
    logs = json.load(f)

# Extract executed techniques
executed_ttps = [entry["technique_id"] for entry in logs if entry["status"] == "executed"]

# Generate MITRE ATT&CK Heatmap
heatmap = {ttp: executed_ttps.count(ttp) for ttp in set(executed_ttps)}

# Save heatmap
with open("caldera/logs/heatmap.json", "w") as f:
    json.dump(heatmap, f, indent=4)

print("[+] MITRE ATT&CK Heatmap Generated!")
