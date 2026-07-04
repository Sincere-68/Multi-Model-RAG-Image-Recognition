"""Check if required dependencies are installed"""
import sys

print(f"Python: {sys.version}\n")

packages = {
    'torch': 'PyTorch',
    'torchvision': 'TorchVision',
    'transformers': 'Transformers',
    'colpali_engine': 'ColPali Engine',
    'qwen_vl_utils': 'Qwen VL Utils',
    'pdf2image': 'pdf2image',
    'PIL': 'Pillow',
    'matplotlib': 'Matplotlib',
    'einops': 'Einops',
    'seaborn': 'Seaborn',
    'ipywidgets': 'ipywidgets',
    'jinja2': 'Jinja2',
    'tqdm': 'tqdm',
    'requests': 'Requests',
    'safetensors': 'Safetensors',
    'sentencepiece': 'SentencePiece',
    'tokenizers': 'Tokenizers',
}

print("Dependency Check:")
print("-" * 50)
all_ok = True
for pkg, name in packages.items():
    try:
        module = __import__(pkg)
        version = getattr(module, '__version__', 'Installed')
        print(f"  [OK] {name:20} {version}")
    except ImportError:
        print(f"  [MISSING] {name:20}")
        all_ok = False

print("-" * 50)
if all_ok:
    print("All dependencies are installed!")
else:
    print("Some packages are missing. Run:")
    print("  pip install colpali-engine pdf2image qwen-vl-utils")
