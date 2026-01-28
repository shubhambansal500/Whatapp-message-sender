#!/usr/bin/env python3
"""
Generate 7-inch tablet screenshot for Play Store listing.
This script uses Playwright to capture the HTML mockup as a PNG image.
"""

import os
import sys
from pathlib import Path

def generate_screenshot():
    """Generate screenshot using Playwright."""
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("Error: Playwright is not installed.")
        print("Install it with: pip install playwright")
        print("Then run: playwright install chromium")
        return False

    html_file = Path(__file__).parent / "tablet_screenshot_7inch.html"
    output_file = Path(__file__).parent / "tablet_screenshot_7inch.png"

    if not html_file.exists():
        print(f"Error: {html_file} not found!")
        return False

    print("Generating 7-inch tablet screenshot...")
    
    with sync_playwright() as p:
        # Launch browser
        browser = p.chromium.launch(headless=True)
        
        # Create a new page with tablet viewport
        # 7-inch tablet resolution: 600x960 (portrait) or 960x600 (landscape)
        page = browser.new_page(
            viewport={'width': 600, 'height': 960},
            device_scale_factor=2  # For high DPI
        )
        
        # Load the HTML file
        html_path = html_file.absolute().as_uri()
        page.goto(html_path)
        
        # Wait for content to load
        page.wait_for_timeout(500)
        
        # Take screenshot
        page.screenshot(
            path=str(output_file),
            full_page=True,
            type='png'
        )
        
        browser.close()
        
        print(f"✓ Screenshot saved to: {output_file}")
        print(f"  Resolution: 1200x1920 pixels (2x scale)")
        print(f"  Format: PNG")
        return True

def generate_with_selenium():
    """Alternative method using Selenium."""
    try:
        from selenium import webdriver
        from selenium.webdriver.chrome.options import Options
        from selenium.webdriver.chrome.service import Service
    except ImportError:
        print("Error: Selenium is not installed.")
        print("Install it with: pip install selenium")
        return False

    html_file = Path(__file__).parent / "tablet_screenshot_7inch.html"
    output_file = Path(__file__).parent / "tablet_screenshot_7inch.png"

    if not html_file.exists():
        print(f"Error: {html_file} not found!")
        return False

    print("Generating 7-inch tablet screenshot with Selenium...")
    
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--window-size=600,960')
    
    try:
        driver = webdriver.Chrome(options=chrome_options)
        html_path = html_file.absolute().as_uri()
        driver.get(html_path)
        driver.save_screenshot(str(output_file))
        driver.quit()
        
        print(f"✓ Screenshot saved to: {output_file}")
        return True
    except Exception as e:
        print(f"Error: {e}")
        print("Make sure ChromeDriver is installed and in PATH")
        return False

if __name__ == "__main__":
    print("=" * 60)
    print("7-inch Tablet Screenshot Generator")
    print("=" * 60)
    print()
    
    # Try Playwright first
    if generate_screenshot():
        sys.exit(0)
    
    # Fallback to Selenium
    print("\nTrying Selenium as fallback...")
    if generate_with_selenium():
        sys.exit(0)
    
    print("\n" + "=" * 60)
    print("MANUAL INSTRUCTIONS:")
    print("=" * 60)
    print("1. Open 'tablet_screenshot_7inch.html' in a web browser")
    print("2. Press F12 to open Developer Tools")
    print("3. Press Ctrl+Shift+P (Cmd+Shift+P on Mac)")
    print("4. Type 'screenshot' and select 'Capture full size screenshot'")
    print("5. Save the screenshot as 'tablet_screenshot_7inch.png'")
    print()
    print("OR use a browser extension like 'Full Page Screen Capture'")
    print("=" * 60)
    
    sys.exit(1)
