from flask import Flask, request, render_template_string

app = Flask(__name__)

# Full HTML content as a string
html_code = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>FinanceWise Tips - Professional Personal Finance Blog</title>
    <style>
        body { font-family: 'Arial', sans-serif; margin: 0; padding: 0; background: #f4f6f9; color: #333; line-height: 1.6; animation: fadeInBody 1s ease-in-out; }
        @keyframes fadeInBody { from { opacity: 0; } to { opacity: 1; } }
        header { background: linear-gradient(135deg, #004085, #0056b3); color: #fff; padding: 15px 20px; position: sticky; top: 0; z-index: 100; display: flex; align-items: center; animation: slideDown 0.5s ease; }
        @keyframes slideDown { from { transform: translateY(-100%); } to { transform: translateY(0); } }
        .logo { font-size: 24px; font-weight: bold; margin-right: 20px; color: #fff; animation: pulseLogo 1.5s infinite; }
        @keyframes pulseLogo { 0% { transform: scale(1); } 50% { transform: scale(1.05); } 100% { transform: scale(1); } }
        .search-bar { flex: 1; display: flex; max-width: 600px; }
        .search-input { width: 100%; padding: 10px; border: none; border-radius: 4px 0 0 4px; animation: glowSearch 1.5s infinite; }
        @keyframes glowSearch { 0% { box-shadow: 0 0 0 0 rgba(0, 64, 133, 0.7); } 70% { box-shadow: 0 0 0 10px rgba(0, 64, 133, 0); } 100% { box-shadow: 0 0 0 0 rgba(0, 64, 133, 0); } }
        .search-btn { padding: 10px 20px; background: #28a745; border: none; border-radius: 0 4px 4px 0; cursor: pointer; color: #fff; font-weight: bold; }
        .search-btn:hover { background: #218838; transition: background 0.3s; }
        nav { background: #003366; padding: 10px 0; animation: fadeInNav 1s ease; }
        @keyframes fadeInNav { from { opacity: 0; } to { opacity: 1; } }
        nav ul { list-style: none; padding: 0; margin: 0; display: flex; justify-content: center; }
        nav ul li { margin: 0 15px; }
        nav ul li a { color: #ddd; text-decoration: none; font-weight: bold; transition: color 0.3s; }
        nav ul li a:hover { color: #fff; }
        .hero { background: linear-gradient(135deg, #0056b3, #007bff); color: #fff; text-align: center; padding: 100px 20px; animation: slideInHero 1s ease; }
        @keyframes slideInHero { from { transform: translateX(-100%); } to { transform: translateX(0); } }
        .hero h2 { font-size: 48px; margin: 0; animation: bounceText 2s infinite; }
        @keyframes bounceText { 0% { transform: translateY(0); } 50% { transform: translateY(-10px); } 100% { transform: translateY(0); } }
        .hero p { font-size: 24px; margin: 10px 0; }
        .hero .btn { background: #28a745; color: #fff; padding: 15px 30px; text-decoration: none; border-radius: 5px; transition: background 0.3s; animation: pulseBtn 1.5s infinite; }
        @keyframes pulseBtn { 0% { transform: scale(1); } 50% { transform: scale(1.05); } 100% { transform: scale(1); } }
        .hero .btn:hover { background: #218838; }
        .main-content { max-width: 1200px; margin: 0 auto; padding: 20px; }
        .category-section { margin-bottom: 40px; animation: fadeInSection 1s ease; }
        @keyframes fadeInSection { from { opacity: 0; transform: translateY(20px); } to { opacity: 1; transform: translateY(0); } }
        .category-section h2 { font-size: 32px; color: #0056b3; }
        .post-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 20px; }
        .post-card { background: #fff; border: 1px solid #ddd; padding: 15px; border-radius: 5px; transition: box-shadow 0.3s, transform 0.3s; }
        .post-card:hover { box-shadow: 0 4px 8px rgba(0,64,133,0.2); transform: translateY(-5px); }
        .post-card h3 { font-size: 20px; margin: 10px 0; color: #28a745; }
        .post-card p { margin: 10px 0; }
        .post-card .btn { background: #007bff; color: #fff; padding: 10px; text-decoration: none; border-radius: 4px; transition: background 0.3s; }
        .post-card .btn:hover { background: #0056b3; }
        .full-post { display: none; margin-top: 20px; padding: 20px; background: #e9ecef; border-radius: 5px; animation: fadeInFull 0.5s ease; }
        @keyframes fadeInFull { from { opacity: 0; } to { opacity: 1; } }
        .newsletter { background: #e3f2fd; padding: 20px; border-radius: 5px; text-align: center; animation: fadeInSection 1s ease; }
        .newsletter input { padding: 10px; width: 300px; border: none; border-radius: 4px 0 0 4px; }
        .newsletter button { padding: 10px 20px; background: #28a745; border: none; border-radius: 0 4px 4px 0; cursor: pointer; color: #fff; }
        .contact-section { margin: 40px 0; animation: fadeInSection 1s ease; }
        .contact-section form { max-width: 600px; margin: 0 auto; }
        .contact-section label { display: block; margin: 10px 0 5px; }
        .contact-section input, .contact-section textarea { width: 100%; padding: 10px; border: 1px solid #ddd; border-radius: 4px; }
        .contact-section button { background: #007bff; color: #fff; padding: 10px; border: none; border-radius: 4px; cursor: pointer; }
        .contact-section .extra { margin-top: 20px; }
        footer { background: #003366; color: #ddd; padding: 20px; text-align: center; }
        footer a { color: #28a745; margin: 0 10px; text-decoration: none; }
        footer a:hover { color: #fff; }
    </style>
</head>
<body>
    <header>
        <div class="logo">FinanceWise Tips</div>
        <div class="search-bar">
            <input type="text" class="search-input" id="searchInput" placeholder="Search finance tips...">
            <button class="search-btn" onclick="searchPosts()">Search</button>
        </div>
    </header>
    <nav>
        <ul>
            <li><a href="#home">Home</a></li>
            <li><a href="#budgeting">Budgeting</a></li>
            <li><a href="#investing">Investing</a></li>
            <li><a href="#saving">Saving</a></li>
            <li><a href="#credit">Credit</a></li>
            <li><a href="#debt">Debt Management</a></li>
            <li><a href="#passive">Passive Income</a></li>
            <li><a href="#contact">Contact</a></li>
        </ul>
    </nav>
    <section class="hero">
        <h2>Master Your Finances in 2025</h2>
        <p>Expert tips on budgeting, investing, saving, credit, debt, and passive income to build wealth.</p>
        <a href="#posts" class="btn">Start Learning</a>
    </section>
    <div class="main-content">
        <section id="posts" class="category-section">
            <h2>Latest Posts</h2>
            <div class="post-grid" id="postGrid">
                <div class="post-card">
                    <h3>Top 5 Budgeting Apps for 2025</h3>
                    <p>Short intro: Discover the best apps to track your spending and save more. Budgeting is essential for financial stability...</p>
                    <a href="#" class="btn" onclick="toggleFullPost(1); return false;">Read More</a>
                    <div id="full1" class="full-post">
                        <h4>Top 5 Budgeting Apps for 2025</h4>
                        <p>In 2025, budgeting apps have evolved to include AI-driven insights and seamless integration with bank accounts. This makes managing finances easier than ever. Let's explore the top five apps that can help you take control of your money.</p>
                        <p><strong>1. Mint</strong>: Mint is a free app from Intuit that automatically tracks and categorizes your expenses. It provides real-time alerts for bills and unusual spending, helps you create budgets, and even monitors your credit score. Pros: Free, user-friendly interface. Cons: Ads in the free version. Ideal for beginners who want a hands-off approach.</p>
                        <p><strong>2. YNAB (You Need A Budget)</strong>: YNAB focuses on giving every dollar a job, teaching you to budget proactively. It offers educational resources and syncs across devices. Price: $14.99/month or $99/year. Pros: Builds good habits, detailed reporting. Cons: Learning curve. Best for those serious about changing their financial behavior.</p>
                        <p><strong>3. PocketGuard</strong>: This app shows how much "pocket money" you have after bills and savings, preventing overspending. It also finds subscription savings and negotiates bills. Price: Free with premium features at $7.99/month. Pros: Bill negotiation tool. Cons: Limited free version. Great for people with many recurring expenses.</p>
                        <p><strong>4. Goodbudget</strong>: Based on the envelope budgeting system, it lets you allocate money to virtual envelopes for different categories. Syncs with partners for shared budgeting. Price: Free with premium at $6/month. Pros: No bank sync needed. Cons: Manual entry for transactions. Perfect for cash-based budgeters.</p>
                        <p><strong>5. Honeydue</strong>: Designed for couples, it tracks shared expenses, sets joint budgets, and allows comments on transactions. Price: Free. Pros: Relationship-focused features. Cons: Limited for singles. Excellent for households managing money together.</p>
                        <p><strong>Getting Started</strong>: Choose an app based on your needs—start with free versions to test. Link your bank accounts for auto-tracking, set realistic budgets using the 50/30/20 rule (50% needs, 30% wants, 20% savings), and review weekly. Many users save hundreds monthly by identifying leaks like unused subscriptions. For advanced users, integrate with tools like Excel for custom reports. Remember, the best app is the one you use consistently.</p>
                    </div>
                </div>
                <div class="post-card">
                    <h3>How to Start Investing with $100</h3>
                    <p>Short intro: Beginner guide to stocks, crypto, and ETFs. Investing doesn't require thousands to start...</p>
                    <a href="#" class="btn" onclick="toggleFullPost(2); return false;">Read More</a>
                    <div id="full2" class="full-post">
                        <h4>How to Start Investing with $100</h4>
                        <p>Starting with $100 is achievable in 2025 thanks to fractional shares and accessible platforms. Here’s how:</p>
                        <ol>
                            <li><strong>Open a Brokerage Account</strong>: Use Robinhood, E*Trade, or Fidelity for low or no fees.</li>
                            <li><strong>Buy ETFs</strong>: Invest in VTI or SPY for broad market exposure with as little as $10.</li>
                            <li><strong>Stocks</strong>: Purchase fractional shares of blue-chip companies like Apple or Microsoft.</li>
                            <li><strong>Crypto</strong>: Start with Bitcoin or Ethereum on Binance using stablecoins to minimize risk.</li>
                            <li><strong>Robo-Advisors</strong>: Try Betterment or Wealthfront for automated portfolios starting at $15.</li>
                        </ol>
                        <p><strong>Risks</strong>: Market volatility can lead to losses, so diversify. <strong>Tip</strong>: Use compound interest calculators to project growth—$100 at 7% annually could be $200 in 10 years. <strong>More Tips</strong>: Set up automatic deposits, explore Roth IRA for tax benefits, and read "The Intelligent Investor" by Benjamin Graham. <strong>Success Story</strong>: A beginner turned $100 into $500 in a year with consistent small investments. <strong>Pro Tip</strong>: Avoid day trading; focus on long-term growth. <strong>Resources</strong>: Visit Investopedia for education. <strong>Conclusion</strong>: Start small, learn continuously, and let your money work for you.</p>
                    </div>
                </div>
                <div class="post-card">
                    <h3>Save $10,000 in a Year: Step-by-Step Plan</h3>
                    <p>Short intro: Practical tips for building an emergency fund. Saving is the foundation of financial freedom...</p>
                    <a href="#" class="btn" onclick="toggleFullPost(3); return false;">Read More</a>
                    <div id="full3" class="full-post">
                        <h4>Save $10,000 in a Year: Step-by-Step Plan</h4>
                        <p>Goal: $833/month. Follow these steps to build your emergency fund:</p>
                        <ol>
                            <li><strong>Track Expenses</strong>: Monitor spending for one week using a notebook or app.</li>
                            <li><strong>Cut Non-Essentials</strong>: Reduce eating out or subscriptions to save $200/month.</li>
                            <li><strong>Automate Savings</strong>: Set up a high-yield savings account (4.5% APY) with automatic transfers.</li>
                            <li><strong>Side Hustle</strong>: Earn extra with freelancing on Upwork or selling crafts on Etsy.</li>
                            <li><strong>Sell Unused Items</strong>: Clear clutter with eBay or Facebook Marketplace sales.</li>
                        </ol>
                        <p><strong>Tip</strong>: Use the 24-hour rule for impulse purchases to avoid regret. <strong>More Tips</strong>: Negotiate bills (e.g., cable, phone), use cash for groceries to limit spending, and reward yourself at milestones (e.g., $2,000 saved). <strong>Success Story</strong>: A family saved $12,000 by meal prepping and cutting dining out. <strong>Pro Tip</strong>: Aim for a 3-6 month emergency fund before other goals. <strong>Resources</strong>: Use Bankrate.com for savings calculators. <strong>Conclusion</strong>: Consistency and small changes lead to big results—review progress monthly.</p>
                    </div>
                </div>
                <div class="post-card">
                    <h3>Credit Card Rewards: Maximize Your Benefits</h3>
                    <p>Short intro: Best cards for cashback and travel points. Credit cards can be a tool, not a trap...</p>
                    <a href="#" class="btn" onclick="toggleFullPost(4); return false;">Read More</a>
                    <div id="full4" class="full-post">
                        <h4>Credit Card Rewards: Maximize Your Benefits</h4>
                        <p>Top credit cards for 2025 rewards:</p>
                        <ul>
                            <li><strong>Chase Sapphire Preferred</strong>: Earn 2x points on travel, plus a 60,000-point sign-up bonus.</li>
                            <li><strong>Capital One Venture</strong>: Get 1.5x miles on all purchases, transferable to travel partners.</li>
                            <li><strong>Citi Double Cash</strong>: Offers 2% cashback (1% on purchase, 1% on payment).</li>
                        </ul>
                        <p><strong>Tip</strong>: Pay your balance in full each month to avoid interest (average 18-22%). <strong>More Tips</strong>: Use category bonuses (5x on groceries with certain cards), claim sign-up bonuses after spending $500 in 3 months, and track points with AwardWallet. <strong>Success Story</strong>: A traveler redeemed points for $1,000 in free flights. <strong>Pro Tip</strong>: Pair with airline/hotel loyalty programs for bigger rewards. <strong>Resources</strong>: Check ThePointsGuy.com for reviews. <strong>Conclusion</strong>: Select a card matching your spending habits to maximize returns.</p>
                    </div>
                </div>
                <div class="post-card">
                    <h3>Debt Free in 2025: Proven Strategies</h3>
                    <p>Short intro: Get out of debt with snowball and avalanche methods. Debt is a burden—let's lift it...</p>
                    <a href="#" class="btn" onclick="toggleFullPost(5); return false;">Read More</a>
                    <div id="full5" class="full-post">
                        <h4>Debt Free in 2025: Proven Strategies</h4>
                        <p>Two popular methods to eliminate debt:</p>
                        <ul>
                            <li><strong>Snowball Method</strong>: Pay off smallest debts first for quick wins, boosting motivation.</li>
                            <li><strong>Avalanche Method</strong>: Tackle highest interest rates first to save on interest costs.</li>
                        </ul>
                        <p><strong>Steps</strong>: 1. List all debts with amounts and rates. 2. Create a budget to free $200/month. 3. Negotiate lower rates with lenders. 4. Consolidate with a low-interest loan if possible. <strong>Tip</strong>: Stop using credit cards during repayment. <strong>More Tips</strong>: Use Undebt.it for repayment plans, earn extra with a side hustle, and celebrate each paid-off debt. <strong>Success Story</strong>: A user cleared $20,000 in 18 months. <strong>Pro Tip</strong>: Build a $1,000 emergency fund to prevent new debt. <strong>Resources</strong>: Visit Debt.org for tools. <strong>Conclusion</strong>: Commitment and strategy will lead to freedom.</p>
                    </div>
                </div>
                <div class="post-card">
                    <h3>Passive Income Ideas for Beginners</h3>
                    <p>Short intro: Earn money while you sleep with these tips. Passive income is the key to wealth...</p>
                    <a href="#" class="btn" onclick="toggleFullPost(6); return false;">Read More</a>
                    <div id="full6" class="full-post">
                        <h4>Passive Income Ideas for Beginners</h4>
                        <p>Five ways to start passive income with minimal effort:</p>
                        <ol>
                            <li><strong>Dividend Stocks</strong>: Invest in companies like Coca-Cola for quarterly payouts.</li>
                            <li><strong>REITs</strong>: Real estate investment trusts for rental income without property management.</li>
                            <li><strong>Peer-to-Peer Lending</strong>: Lend via LendingClub for interest returns.</li>
                            <li><strong>Digital Products</strong>: Sell eBooks or printables on Etsy.</li>
                            <li><strong>Affiliate Marketing</strong>: Promote products on Amazon Associates.</li>
                        </ol>
                        <p><strong>Tip</strong>: Start with $500 and reinvest earnings. <strong>More Tips</strong>: Diversify sources, track with Google Sheets, and use tax-advantaged accounts like IRA. <strong>Success Story</strong>: A blogger earns $3,000/month from affiliates. <strong>Pro Tip</strong>: Focus on scalable streams. <strong>Resources</strong>: PassiveIncome.com for ideas. <strong>Conclusion</strong>: Build multiple streams for financial security.</p>
                    </div>
                </div>
                <div class="post-card">
                    <h3>Retirement Planning in Your 20s</h3>
                    <p>Short intro: Start early to retire rich. Time is your biggest asset...</p>
                    <a href="#" class="btn" onclick="toggleFullPost(7); return false;">Read More</a>
                    <div id="full7" class="full-post">
                        <h4>Retirement Planning in Your 20s</h4>
                        <p>Steps to secure your future:</p>
                        <ol>
                            <li><strong>Open a 401(k) or IRA</strong>: Start with your employer’s plan or a Roth IRA.</li>
                            <li><strong>Contribute 15% of Income</strong>: Aim for this percentage to maximize growth.</li>
                            <li><strong>Invest in Index Funds</strong>: Choose low-cost options like S&P 500 funds.</li>
                            <li><strong>Maximize Employer Match</strong>: Don’t leave free money on the table.</li>
                        </ol>
                        <p><strong>Tip</strong>: Use retirement calculators to see growth potential. <strong>More Tips</strong>: Avoid lifestyle inflation, learn Roth vs. Traditional IRA, and review annually. <strong>Success Story</strong>: A 25-year-old is on track for $1M by 60. <strong>Pro Tip</strong>: Leverage compound interest—$5,000 at 20 grows to $70,000 by 60 at 7%. <strong>Resources</strong>: Vanguard.com for tools. <strong>Conclusion</strong>: Early action ensures a comfortable retirement.</p>
                    </div>
                </div>
                <div class="post-card">
                    <h3>Crypto Investing Basics for 2025</h3>
                    <p>Short intro: Navigate the crypto market safely. Bitcoin, Ethereum, and beyond...</p>
                    <a href="#" class="btn" onclick="toggleFullPost(8); return false;">Read More</a>
                    <div id="full8" class="full-post">
                        <h4>Crypto Investing Basics for 2025</h4>
                        <p>Guide to entering the crypto world:</p>
                        <ol>
                            <li><strong>Understand Blockchain</strong>: Learn how transactions are secured.</li>
                            <li><strong>Start with Bitcoin/Ethereum</strong>: The most stable options.</li>
                            <li><strong>Use Exchanges</strong>: Sign up on Coinbase or Kraken.</li>
                            <li><strong>Secure with Wallets</strong>: Use Ledger or Trezor for safety.</li>
                            <li><strong>Diversify with Altcoins</strong>: Explore Cardano or Solana.</li>
                        </ol>
                        <p><strong>Tip</strong>: Invest only what you can afford to lose. <strong>More Tips</strong>: Follow regulations, use dollar-cost averaging, and study technical analysis. <strong>Success Story</strong>: An investor turned $1K to $10K in a bull run. <strong>Pro Tip</strong>: Avoid FOMO—stick to a plan. <strong>Resources</strong>: CoinMarketCap for prices. <strong>Conclusion</strong>: High risk, high reward—proceed with caution.</p>
                    </div>
                </div>
                <div class="post-card">
                    <h3>Home Buying Tips for First-Timers</h3>
                    <p>Short intro: Navigate the market in 2025. From mortgage to closing...</p>
                    <a href="#" class="btn" onclick="toggleFullPost(9); return false;">Read More</a>
                    <div id="full9" class="full-post">
                        <h4>Home Buying Tips for First-Timers</h4>
                        <p>Steps to buy your first home:</p>
                        <ol>
                            <li><strong>Check Credit Score</strong>: Aim for 700+ for better rates.</li>
                            <li><strong>Save for Down Payment</strong>: Target 20% to avoid PMI.</li>
                            <li><strong>Get Pre-Approved</strong>: Secure a mortgage commitment.</li>
                            <li><strong>Find a Realtor</strong>: Choose an experienced local agent.</li>
                            <li><strong>Inspect Thoroughly</strong>: Hire a professional inspector.</li>
                        </ol>
                        <p><strong>Tip</strong>: Budget for closing costs (2-5% of home price). <strong>More Tips</strong>: Opt for a fixed-rate mortgage, plan for maintenance (1-2% of home value/year), and pick a location with growth potential. <strong>Success Story</strong>: A couple bought under budget with negotiation. <strong>Pro Tip</strong>: Don’t max your pre-approval—leave room for emergencies. <strong>Resources</strong>: Zillow.com for listings. <strong>Conclusion</strong>: Patience and research ensure a smart purchase.</p>
                    </div>
                </div>
                <div class="post-card">
                    <h3>Side Hustle Ideas to Boost Income</h3>
                    <p>Short intro: Earn extra money in 2025. From freelancing to gig economy...</p>
                    <a href="#" class="btn" onclick="toggleFullPost(10); return false;">Read More</a>
                    <div id="full10" class="full-post">
                        <h4>Side Hustle Ideas to Boost Income</h4>
                        <p>Top side hustles to try:</p>
                        <ol>
                            <li><strong>Freelance Writing</strong>: Write for Upwork or Fiverr ($20-$50/hour).</li>
                            <li><strong>Drive for Uber</strong>: Earn $15-$25/hour in busy areas.</li>
                            <li><strong>Sell Handmade Goods</strong>: Create on Etsy for passive sales.</li>
                            <li><strong>Tutor Online</strong>: Teach on VIPKid ($14-$22/hour).</li>
                            <li><strong>Stock Photography</strong>: Upload to Shutterstock for royalties.</li>
                        </ol>
                        <p><strong>Tip</strong>: Dedicate 10 hours/week to start. <strong>More Tips</strong>: Track income for taxes, scale successful hustles, and network on LinkedIn. <strong>Success Story</strong>: A teacher earns $2,000/month tutoring. <strong>Pro Tip</strong>: Begin with one skill, build expertise. <strong>Resources</strong>: SideHustleNation.com. <strong>Conclusion</strong>: Diversify income for financial stability.</p>
                    </div>
                </div>
                <div class="post-card">
                    <h3>Tax Saving Strategies for 2025</h3>
                    <p>Short intro: Reduce your tax bill legally. Deductions, credits, and more...</p>
                    <a href="#" class="btn" onclick="toggleFullPost(11); return false;">Read More</a>
                    <div id="full11" class="full-post">
                        <h4>Tax Saving Strategies for 2025</h4>
                        <p>Ways to lower your tax liability:</p>
                        <ul>
                            <li><strong>Max Retirement Contributions</strong>: Add to 401(k) or IRA (up to $7,000 in 2025).</li>
                            <li><strong>Use HSA</strong>: Save on medical expenses tax-free.</li>
                            <li><strong>Charitable Donations</strong>: Deduct up to 60% of AGI.</li>
                            <li><strong>Home Office Deduction</strong>: Claim if you work from home.</li>
                            <li><strong>Education Credits</strong>: Use American Opportunity Credit.</li>
                        </ul>
                        <p><strong>Tip</strong>: Keep detailed records for audits. <strong>More Tips</strong>: File early to avoid errors, use TurboTax for accuracy, and consult a CPA for complex cases. <strong>Success Story</strong>: Saved $3,000 with deductions. <strong>Pro Tip</strong>: Understand tax brackets to optimize. <strong>Resources</strong>: IRS.gov. <strong>Conclusion</strong>: Proactive planning saves thousands.</p>
                    </div>
                </div>
                <div class="post-card">
                    <h3>Financial Goal Setting Guide</h3>
                    <p>Short intro: Set SMART goals for wealth building. From short-term to long-term...</p>
                    <a href="#" class="btn" onclick="toggleFullPost(12); return false;">Read More</a>
                    <div id="full12" class="full-post">
                        <h4>Financial Goal Setting Guide</h4>
                        <p>Use the SMART framework: Specific, Measurable, Achievable, Relevant, Time-bound. Example: Save $5,000 for a vacation in 6 months.</p>
                        <ol>
                            <li><strong>List Goals</strong>: Write down short-term (1 year) and long-term (10+ years).</li>
                            <li><strong>Prioritize</strong>: Focus on emergency fund or debt first.</li>
                            <li><strong>Break Down</strong>: Divide into monthly targets (e.g., $833/month).</li>
                        </ol>
                        <p><strong>Tip</strong>: Track progress weekly with a journal or app. <strong>More Tips</strong>: Use GoalsOnTrack, celebrate milestones (e.g., $1,000 saved), and adjust as life changes. <strong>Success Story</strong>: Achieved a home down payment in 2 years. <strong>Pro Tip</strong>: Align goals with personal values (e.g., travel, security). <strong>Resources</strong>: MindTools.com. <strong>Conclusion</strong>: Clear goals turn dreams into achievements.</p>
                    </div>
                </div>
            </div>
        </section>
        <section class="newsletter">
            <h2>Subscribe for Weekly Tips</h2>
            <input type="email" placeholder="Enter your email">
            <button>Subscribe</button>
        </section>
        <section id="contact" class="contact-section">
            <h2>Contact Us</h2>
            <p>Email: averyval42@yahoo.com</p>
            <p>Phone: +1-555-1234-567</p>
            <p>Address: 123 Finance St, Money City, USA</p>
            <p>Social: Follow us on X, Facebook, LinkedIn for daily tips.</p>
            <p>Support: For inquiries, fill the form below or email us directly.</p>
            <p>Hours: Monday-Friday, 9 AM - 5 PM WAT</p>
            <form method="POST" action="/">
                <label for="name">Full Name:</label>
                <input type="text" id="name" name="name" required>
                <label for="email">Email Address:</label>
                <input type="email" id="email" name="email" required>
                <label for="phone">Phone Number (Optional):</label>
                <input type="tel" id="phone" name="phone">
                <label for="subject">Subject:</label>
                <input type="text" id="subject" name="subject" required>
                <label for="message">Message:</label>
                <textarea id="message" name="message" required></textarea>
                <button type="submit">Send Message</button>
            </form>
            {% if message_sent %}
                <p style="color: green;">Message sent successfully! We will respond soon.</p>
            {% endif %}
        </section>
    </div>
    <footer>
        <p>&copy; 2025 FinanceWise Tips. All rights reserved.</p>
        <a href="#">Privacy Policy</a>
        <a href="#">Terms of Service</a>
        <a href="#">About Us</a>
        <a href="#">Contact</a>
    </footer>
    <script>
        function toggleFullPost(id) {
            const full = document.getElementById('full' + id);
            full.style.display = full.style.display === 'block' ? 'none' : 'block';
        }
        function searchPosts() {
            const query = document.getElementById('searchInput').value.toLowerCase();
            const cards = document.querySelectorAll('.post-card');
            cards.forEach(card => {
                const title = card.querySelector('h3').textContent.toLowerCase();
                card.style.display = title.includes(query) ? 'block' : 'none';
            });
        }
        document.querySelector('.newsletter button').addEventListener('click', function() {
            alert('Subscribed! Thank you for joining FinanceWise Tips.');
        });
    </script>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def home():
    message_sent = False
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        subject = request.form.get('subject')
        message = request.form.get('message')
        # For now, print to Termux console; later, add email with smtplib
        print(f"Message from {name} ({email}, {phone}): Subject - {subject}, Message - {message}")
        message_sent = True
    return render_template_string(html_code, message_sent=message_sent)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
