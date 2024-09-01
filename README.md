# post-tracking-automation

## Overview

**post-tracking-automation** is a Python-based automation tool for tracking packages through the Iran Post service. The tool reads barcodes from an Excel file, submits them to the Iran Post tracking website, and retrieves the tracking results. The results are then saved back into an Excel file for easy access and review.

## Features

- Automatically track multiple packages by submitting barcodes to the Iran Post tracking website.
- Extract tracking information and store the results in a structured Excel file.
- Includes both standard and headless browser operation modes for flexibility and performance.

## Prerequisites

Before running the script, make sure you have the following installed:

- Python 3.x
- Google Chrome browser

The script relies on the following Python packages:

- `selenium`
- `webdriver_manager`
- `pandas`
- `openpyxl`

These can be installed via pip:

```bash
pip install selenium webdriver_manager pandas openpyxl
```

## Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/post-tracking-automation.git
   ```

2. Navigate to the project directory:

   ```bash
   cd post-tracking-automation
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Prepare your barcodes in an Excel file named `barcode.xlsx`, with a column named `barcode` containing the barcode numbers.

2. Run the script:

   ```bash
   python main.py
   ```

   **Important:** You must use an Iranian IP address to access the Iran Post tracking website. Ensure you are either located in Iran or using a VPN/proxy with an Iranian IP.

3. The script will process each barcode, retrieve the tracking information, and save the results in a file named `output.xlsx`.

### Running in Headless Mode

For better performance or when running on a server without a GUI, the script can operate in headless mode (i.e., without opening a browser window). This mode is enabled by default in the final part of the script.

## Output

The script will generate an `output.xlsx` file containing the original barcodes and their corresponding tracking results. This file can be opened with any Excel-compatible software.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request or open an Issue for any bugs or feature requests.

## Contact

For any questions or support, please open an issue or contact me at [mahmodihamed98@gmail.com].
