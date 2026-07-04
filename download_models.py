"""Download all required models"""
from huggingface_hub import snapshot_download
import sys

models = [
    "vidore/colpaligemma-3b-pt-448-base",
    "vidore/colpali-v1.2",
    "Qwen/Qwen2-VL-2B-Instruct",
]

print("=" * 60)
print("Model Download Script")
print("=" * 60)

for i, model_name in enumerate(models, 1):
    print(f"\n[{i}/3] Downloading {model_name}...")
    try:
        path = snapshot_download(
            repo_id=model_name,
            local_files_only=False,
        )
        print(f"  [OK] Saved to: {path}")
    except Exception as e:
        print(f"  [FAIL] Error: {e}")
        print("  Check your internet connection and try again.")

print("\n" + "=" * 60)
print("Download process finished")
print("=" * 60)
