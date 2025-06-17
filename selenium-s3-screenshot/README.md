# Selenium S3 Screenshot Upload

This project demonstrates how to integrate Selenium with AWS S3 to capture and upload website screenshots to an S3 bucket. It is designed to run on Ubuntu and includes a setup script for easy environment configuration.

## Prerequisites
- Ubuntu (tested on 20.04/22.04)
- AWS account with administrative access
- Python 3.8+
- Google Chrome installed
- AWS S3 bucket created
- AWS IAM access keys

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/selenium-s3-lab.git
   cd selenium-s3-lab
   ```
   
2. Run the setup script to configure the environment:
   ```bash
   chmod +x setup.sh
   ./setup.sh
   ```

3. Create a .env file with your AWS credentials:
   ```env
   AWS_ACCESS_KEY_ID=your_access_key_id
   AWS_SECRET_ACCESS_KEY=your_secret_access_key
   AWS_REGION=your_region
   S3_BUCKET_NAME=your_bucket_name
   ```
4. Run the script:
   ```bash
    source venv/bin/activate
    python scripts/upload_screenshot.py
   ```

## Project Structure
```text
/selenium-s3-lab
├── scripts/
│   └── upload_screenshot.py  # Main script for Selenium and S3
├── .gitignore               # Git ignore file
├── README.md                # Project documentation
├── requirements.txt         # Python dependencies
├── .env                    # Environment variables (not tracked)
└── setup.sh                # Setup script for Ubuntu
```
## Notes
 - Ensure your S3 bucket exists before running the script.
 - The script uses webdriver-manager to automatically handle ChromeDriver. 
 - The .env file contains sensitive information and should not be committed to Git.

## License

MIT License
