#!/usr/bin/env python3
"""
Test script to validate fresh ProtagoDoc setup.
This simulates what a new user would experience.
"""

import os
import subprocess
import sys
from pathlib import Path


def run_command(cmd, description="", check=True):
    """Run a shell command and return the result."""
    print(f"\n🔄 {description}")
    print(f"Running: {cmd}")
    
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    
    if result.stdout:
        print(f"✅ Output: {result.stdout.strip()}")
    if result.stderr and result.returncode != 0:
        print(f"❌ Error: {result.stderr.strip()}")
    
    if check and result.returncode != 0:
        print(f"❌ Command failed with return code {result.returncode}")
        return False
    
    return True


def check_file_exists(file_path, description=""):
    """Check if a file exists."""
    if Path(file_path).exists():
        print(f"✅ {description}: {file_path}")
        return True
    else:
        print(f"❌ {description} missing: {file_path}")
        return False


def check_directory_structure():
    """Verify the expected directory structure exists."""
    print("\n📁 Checking directory structure...")
    
    required_paths = [
        ("scripts/download_models_hf.py", "Model download script"),
        ("configs/magic-pdf-gpu.template.json", "GPU config template"),
        ("tools/mineru", "MinerU submodule"),
        (".gitignore", "Git ignore file"),
    ]
    
    all_good = True
    for path, desc in required_paths:
        if not check_file_exists(path, desc):
            all_good = False
    
    return all_good


def test_python_imports():
    """Test if required Python packages are available."""
    print("\n🐍 Testing Python imports...")
    
    imports_to_test = [
        ("torch", "PyTorch"),
        ("huggingface_hub", "Hugging Face Hub"),
    ]
    
    all_good = True
    for module, desc in imports_to_test:
        try:
            __import__(module)
            print(f"✅ {desc} available")
        except ImportError:
            print(f"❌ {desc} not available - install with: pip install {module}")
            all_good = False
    
    return all_good


def test_gpu_availability():
    """Test GPU availability."""
    print("\n🖥️  Testing GPU availability...")
    
    try:
        import torch
        if torch.cuda.is_available():
            gpu_count = torch.cuda.device_count()
            print(f"✅ CUDA available with {gpu_count} GPU(s)")
            for i in range(gpu_count):
                gpu_name = torch.cuda.get_device_name(i)
                print(f"   GPU {i}: {gpu_name}")
            return True
        else:
            print("⚠️  CUDA not available - will use CPU mode")
            return False
    except ImportError:
        print("❌ PyTorch not available")
        return False


def validate_setup():
    """Run the complete validation."""
    print("🔍 ProtagoDoc Fresh Setup Validation")
    print("=" * 50)
    
    # Check if we're in the right directory
    if not Path("scripts/download_models_hf.py").exists():
        print("❌ Must run from ProtagoDoc project root directory")
        return False
    
    all_checks = []
    
    # Basic structure check
    all_checks.append(check_directory_structure())
    
    # Python dependencies check
    all_checks.append(test_python_imports())
    
    # GPU check (warning only)
    gpu_available = test_gpu_availability()
    
    # Check if MinerU is installed
    print("\n📦 Checking MinerU installation...")
    try:
        import magic_pdf
        print("✅ MinerU (magic_pdf) is installed")
        all_checks.append(True)
    except ImportError:
        print("⚠️  MinerU not installed yet - run setup first")
        all_checks.append(False)
    
    # Check if models are downloaded
    print("\n🤖 Checking model availability...")
    models_dir = Path("tools/mineru/local_models/models")
    if models_dir.exists() and any(models_dir.iterdir()):
        print("✅ Models directory exists and has content")
        all_checks.append(True)
    else:
        print("⚠️  Models not downloaded yet - run model download script")
        all_checks.append(False)
    
    # Check config file
    print("\n⚙️  Checking configuration...")
    config_file = Path.home() / "magic-pdf.json"
    if config_file.exists():
        print("✅ Configuration file exists")
        try:
            import json
            with open(config_file) as f:
                config = json.load(f)
            device_mode = config.get('device-mode', 'not set')
            models_dir_config = config.get('models-dir', 'not set')
            print(f"   Device mode: {device_mode}")
            print(f"   Models directory: {models_dir_config}")
            all_checks.append(True)
        except Exception as e:
            print(f"❌ Error reading config: {e}")
            all_checks.append(False)
    else:
        print("⚠️  Configuration file missing - run model download script")
        all_checks.append(False)
    
    # Summary
    print("\n📊 VALIDATION SUMMARY")
    print("=" * 30)
    
    if all(all_checks):
        print("🎉 ALL CHECKS PASSED! Setup appears complete.")
        print("\n📝 Next steps:")
        print("   magic-pdf -p demo/pdfs/small_ocr.pdf -o output/")
        return True
    else:
        print("⚠️  Some checks failed. Follow the setup instructions:")
        print("\n📝 Setup steps:")
        print("1. Ensure conda environment is activated")
        print("2. cd tools/mineru && pip install -e .[full]")
        print("3. cd ../.. && python scripts/download_models_hf.py")
        print("4. Test: magic-pdf --help")
        return False


if __name__ == "__main__":
    success = validate_setup()
    sys.exit(0 if success else 1) 