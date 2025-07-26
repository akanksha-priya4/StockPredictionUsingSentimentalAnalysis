# 🚀 Quick Setup Guide

## Step 1: Install Python (if not already installed)

### Windows:
1. Go to [python.org](https://python.org/downloads/)
2. Download Python 3.8 or higher
3. **Important**: Check "Add Python to PATH" during installation
4. Restart your computer after installation

### Mac:
```bash
# Using Homebrew (recommended)
brew install python3

# Or download from python.org
```

### Linux:
```bash
# Ubuntu/Debian
sudo apt update
sudo apt install python3 python3-pip

# CentOS/RHEL
sudo yum install python3 python3-pip
```

## Step 2: Verify Installation

Open Command Prompt/Terminal and run:
```bash
python --version
```
or
```bash
python3 --version
```

You should see something like "Python 3.x.x"

## Step 3: Install Required Packages

In the project directory, run **ONE** of these commands:

### Option A: Using pip
```bash
pip install -r requirements.txt
```

### Option B: Using python -m pip
```bash
python -m pip install -r requirements.txt
```

### Option C: Using python3
```bash
python3 -m pip install -r requirements.txt
```

### Option D: Manual installation (if requirements.txt fails)
```bash
pip install Flask yfinance pandas numpy plotly requests beautifulsoup4 textblob matplotlib seaborn scikit-learn
```

## Step 4: Run the Application

### Option A: Simple run
```bash
python app.py
```

### Option B: Using the startup script
```bash
python run.py
```

### Option C: Windows users (double-click)
```
start.bat
```

## Step 5: Open Your Browser

Once the server starts, you'll see:
```
* Running on all addresses (0.0.0.0)
* Running on http://127.0.0.1:5000
* Running on http://[your-ip]:5000
```

Open your browser and go to: **http://localhost:5000**

## 🎉 You're Done!

The application will automatically load with Apple (AAPL) stock analysis as a demo.

## 🛠️ Features You Can Use:

1. **Search Stocks**: Enter any stock symbol (AAPL, GOOGL, TSLA, etc.)
2. **Select Time Period**: Choose from 1 month to 5 years
3. **View Interactive Charts**: Candlestick charts with technical indicators
4. **See Predictions**: AI-powered next-day price predictions
5. **Sentiment Analysis**: View market sentiment scores

## 🐛 Troubleshooting

### "Python not found"
- Reinstall Python and check "Add to PATH"
- Restart your computer
- Try `python3` instead of `python`

### "Module not found" errors
- Run: `pip install [module-name]`
- Or: `python -m pip install [module-name]`

### "Port already in use"
- Close other programs using port 5000
- Or change the port in `app.py` (line 299): `port=8000`

### Charts not loading
- Check your internet connection
- Enable JavaScript in your browser
- Try refreshing the page

## 📱 Usage Tips

- **Popular Stocks**: Use the dropdown for quick stock selection
- **Mobile Friendly**: Works great on phones and tablets
- **Real-time Data**: All data is fetched live from Yahoo Finance
- **Technical Analysis**: View RSI, Moving Averages, and more
- **Save Results**: Use browser bookmarks for specific analyses

## 🆘 Need Help?

1. Check the console/terminal for error messages
2. Make sure all packages are installed correctly
3. Verify your internet connection
4. Try a different stock symbol

## 🎯 Popular Stocks to Try:

- **Tech**: AAPL, GOOGL, MSFT, NVDA, META
- **Tesla**: TSLA
- **ETFs**: SPY, QQQ, VTI
- **Finance**: JPM, BAC, WFC
- **Retail**: AMZN, WMT, TGT

Happy trading! 📈✨ 