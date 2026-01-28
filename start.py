#!/usr/bin/env python3
"""
Telegram Mention Bot Startup Script
"""
import subprocess
import sys
import os

def main():
    """Start the bot with auto-restart wrapper"""
    print("🚀 Starting Telegram Mention Bot...")
    
    # Check if .env exists
    if not os.path.exists('.env'):
        print("❌ .env file not found!")
        print("📋 Please copy sample.env to .env and configure it")
        return
    
    # Check if requirements are installed
    print("📦 Checking dependencies...")
    try:
        import pyrogram
        import aiosqlite
        print("✅ Dependencies are installed")
    except ImportError as e:
        print("❌ Missing dependencies. Installing...")
        try:
            subprocess.run([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'], check=True)
            print("✅ Dependencies installed successfully")
        except subprocess.CalledProcessError:
            print("❌ Failed to install dependencies. Please install manually:")
            print("pip install -r requirements.txt")
            return
    
    try:
        # Run bot_runner.py for auto-restart capability
        print("🔄 Starting with auto-restart wrapper...")
        subprocess.run([sys.executable, 'bot_runner.py'], check=True)
    except KeyboardInterrupt:
        print("\n🛑 Bot stopped by user")
    except Exception as e:
        print(f"❌ Error: {e}")
        print("💡 Try running directly: python bot_runner.py")

if __name__ == "__main__":
    main()
