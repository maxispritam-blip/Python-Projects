# Python-Projects
# 🐍 Python Data Science & Statistical Analytics Portfolio

Welcome to my Data Science and Business Intelligence repository! This workspace contains **4 modular, end-to-end data analytics pipelines** written in Python. The projects demonstrate core technical skills in exploratory data analysis (EDA), data cleaning, statistical modeling, data scaling, and advanced data visualization using industrial-grade scientific libraries.

---

## 🛠️ Global Technical Core
* **Language Core:** Python 3.x
* **Data Wrangling:** `Pandas` (Aggregation, Datetime Schema Parsing, GroupBy Data Structures)
* **Scientific Computing:** `NumPy` (Vectorized Matrix Math, Min-Max Normalization Filters)
* **Visual Graphics Engine:** `Matplotlib` (Multi-Axis Lines, Aggregated Bars, Stacked Areas), `Seaborn` (Boxplots, Scatter Matrices, Correlation Heatmaps)

---

## 📂 Executive Portfolio Directory

| Analysis Module | Primary Domain | Analytical Objective | Tech Stack Highlights |
| :--- | :--- | :--- | :--- |
| [1. Retail Operations Analytics](#1-corporate-retail--sales-operations-analytics) | E-Commerce / Retail | Multi-Region Profit Extraction & Order Ingestion | `Pandas` |
| [2. Climatological Normalization](#2-climatological-matrix-normalization--statistical-metrics) | Environmental Science | Vector Matrix Scaling & Threshold Violations | `NumPy`, `Pandas` |
| [3. Time-Series Revenue Profiles](#3-time-series-revenue-distribution--forecasting) | Corporate Finance | Multi-Product Portfolio Growth Over Time | `Matplotlib`, `Pandas` |
| [4. HR Matrix Talent Operations](#4-human-resource-talent-matrix--performance-analytics) | Workforce Analytics | Performance-to-Salary Linear Relationships | `Seaborn`, `Matplotlib` |

---

## 🗒️ Detailed Project Breakdowns

### 1. Corporate Retail & Sales Operations Analytics
* **Business Objective:** Built to automate sales performance reporting, map regional profitability variances, and target high-velocity consumer spending categories.
* **Core Dataset Grounding:** Ingested granular corporate order records (`sales_data.csv`) tracking invoice variables, regions, and net metrics.
* **Analytical Discoveries & KPIs Implemented:**
  * **Regional Outperformance Matrix:** Isolated the **North Region** as the primary sales leader, capturing `$72,000` in total sales and `$16,000` in profit.
  * **Categorical Spending Averages:** Identified **Electronics** as the highest transaction size driver, yielding a mean order value of `$26,500.00`.
  * **Top Order Ingestion:** Programmatically isolated `Order_ID 1009` as the largest single order invoice at `$32,000`.
* **Technical Engineering Highlight:** Established strict data validation checks utilizing `df.isna().sum()` to handle missing values and implemented `pd.to_datetime()` formatting to eliminate time-intelligence parsing errors.
* **Code Output Showcase:** Automated regional metrics export to an external, clean `region_summary_report.csv` file for cross-functional stakeholders.

---

### 2. Climatological Matrix Normalization & Statistical Metrics
* **Business Objective:** Developed a scientific computing model designed to ingest extensive temperature arrays, apply min-max mathematical scaling formulas, and isolate environmental threat zones.
* **Core Dataset Grounding:** Processed multi-dimensional temperature arrays (`temperature_data.csv`) mapping reading timelines across five distinct cities.
* **Analytical Discoveries & KPIs Implemented:**
  * **Dataset Central Tendency:** Evaluated deep matrix stats, tracking a dataset Mean and Median score resting exactly at `36.5`.
  * **Absolute Peak Identification:** Programmatically located the absolute maximum temperature across the grid, tracking a record apex of `58.0°C` in `City3`.
  * **Boolean Threshold Filter:** Isolated extreme weather anomalies where local conditions crossed a designated baseline constraint of `>30.0°C`.
* **Technical Engineering Highlight:** Engineered a vector scaling equation `(df - min) / (max - min)` via NumPy functions to map unpredictable readings into a standardized bounding frame from `0.0` to `1.0`.

---

### 3. Time-Series Revenue Distribution & Forecasting
* **Business Objective:** Built a dynamic asset visualization dashboard for multi-product lines to assess seasonal transaction behavior, annual run rates, and cumulative portfolio metrics.
* **Core Dataset Grounding:** Continuous chronological records tracking separate operational lines (`Product A`, `Product B`, and `Product C`) across a full calendar fiscal year.
* **Analytical Discoveries & KPIs Implemented:**
  * **Peak Performance Capture:** Tracked strong year-end growth patterns, peaking in December with `Product A` at `$80,000`, `Product B` at `$72,000`, and `Product C` at `$65,000`.
  * **Market Share Visibility:** Visualized clear long-term trends showing `Product A` maintaining definitive revenue dominance over the remaining products throughout all four quarters.
* **Technical Engineering Highlight:** Implemented three distinct visualization viewpoints using Matplotlib: multi-line plots for trend vectors, grouped category charts for annual revenue totals, and alpha-blended `stackplot()` area models to map changes in portfolio composition over time.

---

### 4. Human Resource Talent Matrix & Performance Analytics
* **Business Objective:** Constructed a predictive people-analytics system designed to uncover hidden trends between years of experience, workforce performance ratings, and organizational salary structures.
* **Core Dataset Grounding:** Processed granular corporate talent records (`employee_performance.csv`) detailing experience metrics and performance scores.
* **Analytical Discoveries & KPIs Implemented:**
  * **Compensation Floor Dispersion:** Exposed substantial compensation variances using interactive metrics, finding the **Finance** division driving the highest median salaries.
  * **Tenure to Value Mapping:** Charted clear positive correlations linking career duration to higher value output (e.g., employee `E107` reaching a peak performance evaluation tier of `4.8`).
  * **Linear Strength Verification:** Verified a strong positive statistical association, documenting a massive `0.99 Pearson R` correlation score matching experience vectors to salary tiers.
* **Technical Engineering Highlight:** Created an exploratory multi-plot visualization pipeline, combining continuous distribution curves (`kde=True`), multi-colored boxplots, and an annotated `coolwarm` Seaborn heatmap to evaluate corporate workforce costs.

---
