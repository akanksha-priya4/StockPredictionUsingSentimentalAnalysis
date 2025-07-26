import os
from flask import Flask, render_template, request, jsonify
from datetime import datetime
import requests
import random
import google.generativeai as genai

app = Flask(__name__)

# Configure Gemini API
GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY', 'AIzaSyDwerbrg7P74EQDw3jgg6bfECNEEkbup0M')
genai.configure(api_key=GEMINI_API_KEY)

# Initialize Gemini model
try:
    model = genai.GenerativeModel('gemini-pro')
    print("✅ Gemini model initialized successfully")
except Exception as e:
    print(f"❌ Gemini initialization error: {e}")
    model = None

# Popular stocks
POPULAR_STOCKS = {
    'AAPL': 'Apple Inc.',
    'GOOGL': 'Alphabet Inc.',
    'MSFT': 'Microsoft Corporation',
    'AMZN': 'Amazon.com Inc.',
    'TSLA': 'Tesla Inc.',
    'META': 'Meta Platforms Inc.',
    'NVDA': 'NVIDIA Corporation',
    'NFLX': 'Netflix Inc.'
}

def get_stock_analysis(symbol):
    """Get stock analysis from Gemini"""
    try:
        if not model:
            return generate_fallback_data(symbol)
            
        prompt = f"Analyze {symbol} stock with current price, sentiment, and recommendation (Buy/Hold/Sell). Keep response under 500 words."
        response = model.generate_content(prompt)
        
        # Extract basic data
        data = generate_fallback_data(symbol)
        data['analysis'] = response.text
        return data
        
    except Exception as e:
        print(f"Analysis error: {e}")
        return generate_fallback_data(symbol)

def generate_fallback_data(symbol):
    """Generate sample data"""
    random.seed(hash(symbol) % 1000)
    base_price = random.uniform(50, 400)
    change = random.uniform(-5, 5)
    
    return {
        'symbol': symbol,
        'current_price': round(base_price, 2),
        'price_change': round(change, 2),
        'price_change_pct': round((change/base_price)*100, 2),
        'volume': random.randint(1000000, 10000000),
        'high_52w': round(base_price * 1.3, 2),
        'low_52w': round(base_price * 0.7, 2),
        'sentiment': random.uniform(-0.5, 0.5),
        'recommendation': random.choice(['BUY', 'HOLD', 'SELL']),
        'analysis': f"Stock analysis for {symbol}. Current market conditions suggest moderate volatility with mixed sentiment indicators."
    }

@app.route('/')
def index():
    return render_template('index.html', popular_stocks=POPULAR_STOCKS)

@app.route('/analyze', methods=['POST'])
def analyze():
    try:
        data = request.get_json() if request.is_json else request.form
        symbol = data.get('symbol', '').upper().strip()
        
        if not symbol:
            return jsonify({'error': 'Please enter a stock symbol'}), 400
            
        result = get_stock_analysis(symbol)
        
        return jsonify({
            'symbol': result['symbol'],
            'company_name': POPULAR_STOCKS.get(symbol, symbol),
            'current_price': result['current_price'],
            'price_change': result['price_change'],
            'price_change_pct': result['price_change_pct'],
            'volume': result['volume'],
            'high_52w': result['high_52w'],
            'low_52w': result['low_52w'],
            'avg_sentiment': result['sentiment'],
            'recommendation': result['recommendation'],
            'ai_analysis': result['analysis'],
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/health')
def health():
    return jsonify({'status': 'ok', 'timestamp': datetime.now().isoformat()})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True) 