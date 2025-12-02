4.1 Insights per Bank

Using our computed sentiment proportions, average sentiment scores, top positive/negative keywords, and complaint themes, the following insights emerge:

➡️ Bank: BOA (Bank of Abyssinia)
Top Drivers (Positive Factors)

Speed & performance when it works

Users mention: “fast”, “working”, “good”, “easy”.

Good ease of use for basic features

Positive keywords like “nice”, “great”, “excellent” show appreciation for UI simplicity.

Top Pain Points

Performance issues

Keywords: “slow”, “bug”, “poor”, “worst”.

Complaint themes: Performance Issues, Transaction/Feature Issues.

Login & access problems

Frequent user issues: account lockouts, failed login attempts, unstable sessions.

Recommendations

Improve app stability and loading time

Prioritize backend optimizations and caching strategies to reduce slowdowns.

Redesign login flow

Add biometric fallback, improve OTP reliability, and reduce session timeout failures.

➡️ Bank: CBE (Commercial Bank of Ethiopia)
Top Drivers

Useful and friendly customer experience

Positive words: “useful”, “friendly”, “smart”, “love”.

General reliability

High positive score (58.75%), low negative score (7.75%).

Top Pain Points

Transaction/Feature Issues

Fails during transfers or payments; common complaint theme.

Update-related issues

Negative keywords: “update”, “doesn”, “bad”.

Recommendations

Increase transaction success rate

Improve error handling during network latency; provide clearer user guidance on failed transactions.

Test app updates more rigorously

Reduce breaking changes after updates and strengthen QA cycles.

➡️ Bank: Dashen Bank
Top Drivers

Very positive usability experience

Strong positive words: “super”, “amazing”, “fast”, “excellent”.

Complaint theme even includes “Positive Ease of Use”.

High functional reliability

Highest average sentiment score (0.3112).

Top Pain Points

Slow performance (occasional)

Negative words: “slow”, “update”, “issue”.

Update-related issues

Users report performance drops after updates.

Recommendations

Optimize performance during peak traffic

Improve API response times and server load-balancing.

Reduce issues introduced by updates

Implement staged rollouts and crash analytics monitoring.

4.2 Bank Comparison (CBE vs BOA vs Dashen)
Overall Sentiment

Dashen → Most positive (0.311 avg score; 64.5% positive reviews).

CBE → Relatively stable with fewer negative reviews (7.75%).

BOA → Weakest sentiment (19% negative; lowest avg score 0.153).

User Perception Summary

Dashen is viewed as fast and easy to use, with minimal issues.

CBE is seen as useful and reliable, but suffers from some failed transactions.

BOA faces recurring stability problems and more severe complaints.

4.3 Visualizations (Required 3–5 Plots)
You can generate the following:
1️⃣ Sentiment Distribution per Bank (Bar Plot)

X-axis: Bank

Y-axis: Positive / Neutral / Negative proportions

2️⃣ Average Sentiment Score per Bank (Bar Plot)

Shows overall ranking of banks.

3️⃣ Word Clouds

Positive words per bank

Negative words per bank

4️⃣ Rating Distribution (Histogram or KDE)

Shows how users rate each app (1–5 stars).

5️⃣ Sentiment Trend Over Time (Line Plot)

Sentiment score per month/year

Helps identify performance dips.

If you want, I can generate all these plots using Matplotlib and send the images.

4.4 Ethics: Bias & Limitations

When analyzing user reviews, several biases may distort conclusions:

⚠️ Bias Factors

Negative Skew Bias

Users are more likely to leave reviews when upset than when satisfied.

Fake or incentivized reviews

Some extremely positive reviews may not reflect real experience.

Sampling Bias

Reviews from Play Store may not represent all customers (e.g., older users rarely review).

Language Bias

Users may express different levels of intensity depending on their English proficiency.

⚠️ Ethical Considerations

Insights should not be used to shame or unfairly compare institutions.

Analysis should guide improvement, not reputational damage.