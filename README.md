Here’s my 6-week plan to build a polished algorithmic trading project for my CV, based on *Learn Algorithmic Trading* by Donadio & Ghosh. Everything will run locally—no live trading or deployment needed.

---

### **The Goal**
One clean GitHub repo: a modular backtesting framework with multiple strategies, risk management, and full performance analytics.  
CV-ready line: *“Built a Python algorithmic trading framework implementing momentum, mean-reversion, and statistical arbitrage strategies, with custom risk modules and walk-forward validation.”*

---

### **My 6-Week Roadmap**

**Week 1 – Data & Indicators**  
*Focus:* Get a reliable data pipeline up.  
- Chapters 1 & 2 for foundation.  
- Use `yfinance` or a free API (Alpha Vantage, Polygon) to pull 5+ years of daily OHLCV for a few tickers (e.g., SPY, EUR/USD, BTC).  
- Build functions to compute SMA, RSI, Bollinger Bands.  
*Deliverable:* Scripts in `/data` that can fetch and calculate. A Jupyter notebook exploring the data and indicators.

**Week 2 – First Strategy & Simple Backtester**  
*Focus:* Turn signals into P&L.  
- Chapters 3 & 4.  
- Code a basic backtester: given a DataFrame with signals, simulate positions and equity curve.  
- Implement a simple momentum strategy (e.g., SMA crossover).  
- Add basic metrics: Sharpe ratio, max drawdown.  
*Deliverable:* Backtesting engine in `/backtest`. Notebook showing the momentum strategy’s performance.

**Week 3 – Another Strategy & Risk Basics**  
*Focus:* Expand strategy diversity and add simple risk controls.  
- Chapters 5 & 6.  
- Code a mean-reversion strategy (e.g., RSI-based).  
- Implement position sizing (fixed fractional) and a trailing stop-loss.  
*Deliverable:* Updated backtester with risk module. Notebook comparing momentum vs. mean-reversion.

**Week 4 – System Design & Clean Architecture**  
*Focus:* Refactor into a modular, reusable system.  
- Chapters 7 & 8.  
- Organize code into clear modules:  
  `data/` – data fetching and preprocessing  
  `strategies/` – strategy classes  
  `risk/` – position sizing and stops  
  `backtest/` – simulation engine  
  `metrics/` – performance analytics  
- Test on out-of-sample data.  
*Deliverable:* Clean repo structure with a main script `run_backtest.py`.

**Week 5 – Adding Depth (Chan-Style Strategy)**  
*Focus:* Introduce a more sophisticated approach for credibility.  
- Read Chan’s *Algorithmic Trading* Ch 3-5 for intuition on pairs trading and cointegration.  
- Implement a basic pairs trading strategy (cointegration-based) or a Kalman filter mean-reversion.  
- Compare its performance to the simpler strategies.  
*Deliverable:* New strategy in `/strategies`. Notebook: “Pairs Trading vs. Classic Strategies.”

**Week 6 – Polish & Package**  
*Focus:* Make it recruiter-ready.  
- Add realistic transaction costs (slippage, commissions).  
- Run a basic walk-forward analysis to check robustness.  
- Write a thorough README: architecture diagram, setup instructions, summary of results.  
- Create a final performance table (Sharpe, max DD, win rate) across all strategies.  
*Deliverable:* Final GitHub repo with documentation and clear, reproducible results.

---

### **Why This Sequence Works for Me**
- **Weeks 1-2:** Quick tangible progress—seeing a strategy work keeps motivation high.
- **Weeks 3-4:** Forces me to build clean, reusable code (good engineering practice).
- **Week 5:** Goes beyond the book, showing I can integrate additional research (Chan).
- **Week 6:** Ensures the project is presentable and tells a clear story on my CV.

**Time:** ~8-12 hours/week, all in Python/Jupyter.  
**Start:** This weekend with data fetching and playing with indicators.

---

### **Final CV Bullets**
```
- Built a local Python backtesting framework from scratch, processing multi-year OHLCV data; implemented and tested momentum, mean-reversion, and cointegration-based statistical arbitrage strategies.
- Incorporated risk management modules (position sizing, stop-loss) and transaction costs, achieving Sharpe ratios between 0.8-1.4 in walk-forward analysis on equities and FX.
- Designed a modular architecture (data, strategy, risk, analytics) for easy extension; extended framework with Chan-inspired pairs trading using Kalman filters.
```

I’ll start with Week 1 and adjust if I hit snags or want to focus on a specific asset class.