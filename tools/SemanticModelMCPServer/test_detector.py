
import sys
import os
import json

# Add current directory to path so we can import tools
sys.path.append(os.getcwd())

try:
    from tools.ultra_fast_powerbi_detector import detect_powerbi_desktop_instances_ultra_fast
    print("Import successful")
    
    print("Running detection...")
    result = detect_powerbi_desktop_instances_ultra_fast()
    print("Detection complete")
    print(json.dumps(result, indent=2))
    
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
