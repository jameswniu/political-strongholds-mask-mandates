# Political strongholds in the US and their effects on the socio-economic man through the mask mandate

Showcase URL: https://wendiniu.wixsite.com/bcsproject1

GitLab Repo: https://github.com/jameswniu/project.git


A Data-Driven Analysis on Efficacy of Mask Mandates in the United States

1.	Introduction:
Because Covid-19 is all inclusive in affecting the way we live and how we live after, we aim to explore public data to solidify or critically analyze claims that our surroundings feed to us. Based on official data collected by the Centers for Disease Control and Prevention (“CDC”), we would utilize mask mandate as a factor to capture its effect on individual or public health, and to quantify economic, social, and political impacts descriptively and comparatively.

2.	Dataset:
The dataset by the CDC spans 17 months from April 10, 2020 through January 10, 2021 by country by day. Each row represents an individual country for a State on that particular day with Boolean on whether face masks are required in public places. Requirements for face masks have all-encompassing sources and can include executive orders, administrative orders, resolutions, and proclamations.

3.	Data Preparation: https://catalog.data.gov/dataset/u-s-state-and-territorial-public-mask-mandates-from-april-10-2020-through-january-10-2021--e0ce3
This dataset has 1,594,118 records that is large enough to exceed Excel’s limit (one million records), so we use a simple editor such as Notepad++ to open it.
We first pick out relevant variables only that we can use to describe and analyze such as the State, country, date, and Boolean on whether mask mandate was in effect on that day. We left out other variables such as State and County FIPS codes and URLs to executive orders.
The dataset is grouped by State by County by Month that leaves us with approximately 54,000 records. This data is usable to take into account the timeframe and time lags when considering its healthcare, economic, social, political impacts.
The second usable dataset is grouped by State by County summing days with mask mandate for entire period. This leaves us with approximately 3,200 records. This data is useful for descriptive purposes to summarize and compare if States with more mask mandate days end up better after all.

4.	Research Questions:
James will prepare the data into the two meaningful sets. The group will split up to do the analysis into diverse but overlapping topics. Based on the data each member is going to find for the right-hand side, he or she will merge records and construct descriptive visuals or correlation analysis. This allows each member to delve deeper into his/her topic of interest, facilitates allocation of individual focus in line with GitLab branches and subsequent time management for collaboration.

Plausible Topics of Interest:

James: Impact of mask mandates on unemployment - does it facilitate or push people away from work?
Impact of mask mandates on federal payouts - does it incentives more payout from the government?
Lag of mask mandates vs changes in political inclination

Elsa: Car accidents by county and relationship with mask mandates.
If data permits also explore how mask mandates affect school closures, maybe by county.
This represents the relationship between total school closures and mask mandates.

Ethan: Impact of mask mandates on Covid hotspots and outbreaks.
Comparison of timing of mask mandates whether policy was proactive or reactive, with regards to outbreaks and hotspots.
Correlation of mask mandates and vaccination rates for a given area - are mask mandates predictive of vaccination status?

Steven: Utilization of public places and capacity in regards to mask mandates, especially with regards to restaurants - does it give more people a peace
of mind or discourages them to physically go there?  Google maps API etc may have some data on usage capacity of places.

Babatunde: CDC says 27x more likely to die from COVID-19 without vaccine. 
However is it possible those who are eager to take vaccine prioritize their health so have better health metrics to begin with.
With this in mind, to compare COVID-19 survival rates for vaccinated across combinations of high/low income/education counties for conclusion.
