# MinerU Configuration Templates

This directory contains configuration templates for MinerU setup.

## Configuration Files

### `magic-pdf-gpu.template.json`
Template configuration for GPU-accelerated MinerU processing.

## Configuration Options

### Device Mode
- **`"cpu"`**: Use CPU processing (slower, ~16-17 it/s)
- **`"cuda"`**: Use GPU acceleration (faster, ~130+ it/s)
- **`"mps"`**: Use Apple Silicon MPS acceleration (macOS only)

### Model Directories
- **`models-dir`**: Path to downloaded model weights
- **`layoutreader-model-dir`**: Path to layout reader models

### Feature Toggles
- **`formula-config.enable`**: Enable/disable formula recognition
- **`table-config.enable`**: Enable/disable table recognition
- **`llm-aided-config.*.enable`**: Enable/disable LLM-assisted processing

## Setup Instructions

1. **Copy template to home directory:**
   ```bash
   cp configs/magic-pdf-gpu.template.json ~/magic-pdf.json
   ```

2. **Update paths in the configuration:**
   - Set `models-dir` to your actual model directory path
   - Set `layoutreader-model-dir` to your layoutreader path

3. **Verify configuration:**
   ```bash
   python -c "from magic_pdf.libs.config_reader import get_device; print('Device:', get_device())"
   ```

## Performance Expectations

| Mode | Processing Speed | Memory Usage | Use Case |
|------|------------------|--------------|----------|
| CPU  | ~16-17 it/s     | Low          | Limited resources |
| CUDA | ~130+ it/s      | GPU VRAM     | Production use |
| MPS  | ~50-80 it/s     | Unified      | Apple Silicon |

## Troubleshooting

If configuration changes aren't taking effect:
1. Ensure the config file is in your home directory (`~/magic-pdf.json`)
2. Restart any running MinerU processes
3. Check file permissions: `ls -la ~/magic-pdf.json` 