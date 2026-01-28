#!/bin/bash
# Telegram Mention Bot Startup Script (Linux/Mac)

echo "🚀 Starting Telegram Mention Bot..."

# Check if .env exists
if [ ! -f ".env" ]; then
    echo "❌ .env file not found!"
    echo "📋 Please copy sample.env to .env and configure it"
    exit 1
fi

# Check if Python 3 is available
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed"
    exit 1
fi

# Check if dependencies are installed
echo "📦 Checking dependencies..."
python3 -c "import pyrogram, aiosqlite" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "❌ Missing dependencies. Installing..."
    python3 -m pip install -r requirements.txt
    if [ $? -ne 0 ]; then
        echo "❌ Failed to install dependencies. Please install manually:"
        echo "pip3 install -r requirements.txt"
        exit 1
    fi
    echo "✅ Dependencies installed successfully"
else
    echo "✅ Dependencies are installed"
fi

# Start the bot with auto-restart wrapper
echo "🔄 Starting with auto-restart wrapper..."
python3 bot_runner.py
