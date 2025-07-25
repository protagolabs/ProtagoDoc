import json
import os
import shutil
from pathlib import Path

import requests
from huggingface_hub import snapshot_download


def download_json(url):
    # Download JSON file
    response = requests.get(url)
    response.raise_for_status()  # Check if request was successful
    return response.json()


def download_and_modify_json(url, local_filename, modifications):
    if os.path.exists(local_filename):
        data = json.load(open(local_filename))
        config_version = data.get('config_version', '0.0.0')
        if config_version < '1.2.0':
            data = download_json(url)
    else:
        data = download_json(url)

    # Apply modifications
    for key, value in modifications.items():
        data[key] = value

    # Save modified content
    with open(local_filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    # Get the project root directory (assuming script is run from tools/mineru)
    script_dir = Path(__file__).parent.absolute()
    project_root = script_dir.parent
    
    # Set up local model directories within the project
    local_models_dir = project_root / 'tools' / 'mineru' / 'local_models'
    models_dir = local_models_dir / 'models'
    layoutreader_dir = local_models_dir / 'layoutreader'
    
    # Create directories if they don't exist
    models_dir.mkdir(parents=True, exist_ok=True)
    layoutreader_dir.mkdir(parents=True, exist_ok=True)

    print(f"Downloading models to: {models_dir}")
    print(f"Downloading layoutreader to: {layoutreader_dir}")

    # Download patterns for MinerU models
    mineru_patterns = [
        "models/Layout/YOLO/*",
        "models/MFD/YOLO/*", 
        "models/MFR/unimernet_hf_small_2503/*",
        "models/OCR/paddleocr_torch/*",
    ]
    
    # Download models to local directory
    downloaded_model_dir = snapshot_download(
        'opendatalab/PDF-Extract-Kit-1.0', 
        allow_patterns=mineru_patterns,
        local_dir=str(models_dir.parent),
        local_dir_use_symlinks=False
    )

    # Download layoutreader model to local directory
    layoutreader_pattern = [
        "*.json",
        "*.safetensors",
    ]
    downloaded_layoutreader_dir = snapshot_download(
        'hantian/layoutreader', 
        allow_patterns=layoutreader_pattern,
        local_dir=str(layoutreader_dir),
        local_dir_use_symlinks=False
    )

    # Use the downloaded model paths
    final_models_dir = str(models_dir / 'models') if (models_dir / 'models').exists() else str(models_dir)
    final_layoutreader_dir = str(layoutreader_dir)

    print(f'Models directory: {final_models_dir}')
    print(f'Layoutreader directory: {final_layoutreader_dir}')

    # Configure the magic-pdf.json file
    json_url = 'https://github.com/opendatalab/MinerU/raw/master/magic-pdf.template.json'
    config_file_name = 'magic-pdf.json'
    home_dir = os.path.expanduser('~')
    config_file = os.path.join(home_dir, config_file_name)

    json_mods = {
        'models-dir': final_models_dir,
        'layoutreader-model-dir': final_layoutreader_dir,
        'device-mode': 'cuda',  # Default to CUDA for GPU acceleration
    }

    download_and_modify_json(json_url, config_file, json_mods)
    print(f'Configuration file created at: {config_file}')
    print(f'GPU acceleration enabled by default (device-mode: cuda)')
    print(f'To verify configuration: python -c "from magic_pdf.libs.config_reader import get_device; print(\'Device:\', get_device())"') 