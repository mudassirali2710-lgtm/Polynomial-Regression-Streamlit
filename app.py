import os
import json
import joblib
import pandas as pd
import numpy as np
import streamlit as st
import streamlit.components.v1 as components
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

# ============================================================
# 1. POLYNOMIAL REGRESSION BACKEND LOGIC
# ============================================================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(BASE_DIR, "advertising.csv")
MODEL_PATH = os.path.join(BASE_DIR, "polynomial_regression_model.pkl")

# Load and clean dataset matching Polynomial_Regression_.ipynb
df = pd.read_csv(CSV_PATH)
required_columns = ["TV", "Radio", "Newspaper", "Sales"]
df = df[required_columns].dropna().drop_duplicates()

X = df[["TV", "Radio", "Newspaper"]]
y = df["Sales"]

# Train/Test split: 80% train, 20% test, random_state=42
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42
)

# Polynomial regression degree 2 pipeline
degree = 2
if os.path.exists(MODEL_PATH):
    try:
        model = joblib.load(MODEL_PATH)
    except Exception:
        model = Pipeline([
            ("polynomial_features", PolynomialFeatures(degree=degree, include_bias=False)),
            ("linear_regression", LinearRegression())
        ])
        model.fit(X_train, y_train)
        joblib.dump(model, MODEL_PATH)
else:
    model = Pipeline([
        ("polynomial_features", PolynomialFeatures(degree=degree, include_bias=False)),
        ("linear_regression", LinearRegression())
    ])
    model.fit(X_train, y_train)
    joblib.dump(model, MODEL_PATH)

# Model performance metrics
y_pred = model.predict(X_test)
r2 = r2_score(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))

# Coefficients extraction
poly_features = model.named_steps["polynomial_features"].get_feature_names_out(["TV", "Radio", "Newspaper"])
linear_reg = model.named_steps["linear_regression"]
intercept = float(linear_reg.intercept_)
coef_dict = {name: float(coef) for name, coef in zip(poly_features, linear_reg.coef_)}

# Generate 200 real dataset observations for the SVG chart
svg_circles = []
for _, row in df.iterrows():
    total_spend = row["TV"] + row["Radio"] + row["Newspaper"]
    clamped_spend = min(350.0, max(0.0, total_spend))
    cx = round(60.0 + clamped_spend * 2.0, 1)
    cy = round(340.0 - min(30.0, max(0.0, row["Sales"])) * 10.0, 1)
    svg_circles.append(f'<circle cx="{cx}" cy="{cy}" r="3.5"></circle>')

svg_circles_markup = "\n".join(svg_circles)

# ============================================================
# 2. STREAMLIT CONFIGURATION (PRESERVES EXACT STITCH UI)
# ============================================================
st.set_page_config(
    page_title="Advertising Sales Predictor",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Hide Streamlit header, footer, and default padding to maintain approved Stitch design
st.markdown("""
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .block-container {
        padding: 0 !important;
        max-width: 100% !important;
    }
    iframe {
        border: none !important;
        width: 100% !important;
    }
</style>
""", unsafe_allow_html=True)

# Build the complete single-page application integrating both approved Stitch views
html_content = f"""<!DOCTYPE html>
<html class="dark" lang="en">
<head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<link href="https://fonts.googleapis.com" rel="preconnect"/>
<link crossorigin="" href="https://fonts.gstatic.com" rel="preconnect"/>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&amp;display=swap" rel="stylesheet"/>
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@24,400,0,0" rel="stylesheet"/>
<style>
@layer base {{
  html, body {{ margin: 0; padding: 0; }}
  body {{ overscroll-behavior: none; }}
  main > :first-child {{ margin-top: 0 !important; }}
  main > :last-child {{ margin-bottom: 0 !important; }}
}}
::-webkit-scrollbar {{ display: none; }}
.view-hidden {{ display: none !important; }}
</style>
<script src="https://cdn.tailwindcss.com"></script>
<script id="tailwind-config">
tailwind.config = {{
  darkMode: "class",
  theme: {{
    extend: {{
      "colors": {{
        "on-surface": "#dae2fd",
        "error": "#ffb4ab",
        "on-tertiary-fixed-variant": "#653e00",
        "surface-container-lowest": "#060e20",
        "primary-container": "#38bdf8",
        "tertiary-container": "#f1a02b",
        "outline-variant": "#3e484f",
        "on-primary-container": "#004965",
        "inverse-on-surface": "#283044",
        "secondary": "#c0c1ff",
        "on-secondary-fixed-variant": "#2f2ebe",
        "primary": "#8ed5ff",
        "surface-dim": "#0b1326",
        "on-tertiary-container": "#613b00",
        "surface-container-high": "#222a3d",
        "surface-container-low": "#131b2e",
        "secondary-container": "#3131c0",
        "inverse-surface": "#dae2fd",
        "surface": "#0b1326",
        "on-error-container": "#ffdad6",
        "outline": "#87929a",
        "on-primary-fixed": "#001e2c",
        "on-primary-fixed-variant": "#004c69",
        "primary-fixed-dim": "#7bd0ff",
        "surface-container": "#171f33",
        "surface-container-highest": "#2d3449",
        "surface-bright": "#31394d",
        "on-secondary-fixed": "#07006c",
        "on-primary": "#00354a",
        "secondary-fixed-dim": "#c0c1ff",
        "on-secondary-container": "#b0b2ff",
        "on-secondary": "#1000a9",
        "on-background": "#dae2fd",
        "on-tertiary-fixed": "#2a1700",
        "on-surface-variant": "#bdc8d1",
        "tertiary": "#ffc176",
        "tertiary-fixed": "#ffddb8",
        "surface-variant": "#2d3449",
        "tertiary-fixed-dim": "#ffb960",
        "background": "#0b1326",
        "inverse-primary": "#00668a",
        "on-error": "#690005",
        "on-tertiary": "#472a00",
        "error-container": "#93000a",
        "surface-tint": "#7bd0ff",
        "secondary-fixed": "#e1e0ff",
        "primary-fixed": "#c4e7ff"
      }},
      "borderRadius": {{ "DEFAULT": "0.125rem", "lg": "0.25rem", "xl": "0.5rem", "full": "0.75rem" }},
      "spacing": {{
        "space-sm": "0.5rem", "space-lg": "1.25rem", "gutter-tablet": "1.5rem", "space-xl": "1.5rem",
        "space-xs": "0.25rem", "sidebar-width": "17.5rem", "space-2xl": "2rem", "space-base": "1rem",
        "gutter-mobile": "1rem", "gutter-desktop": "2rem", "space-2xs": "0.125rem", "max-content-width": "90rem",
        "space-md": "0.75rem", "space-4xl": "4rem", "space-3xl": "3rem"
      }},
      "fontFamily": {{
        "headline-lg": ["Inter"], "display": ["Inter"], "headline-lg-mobile": ["Inter"], "code-sm": ["Inter"],
        "data-metric-lg": ["Inter"], "data-metric-sm": ["Inter"], "title-md": ["Inter"], "body-lg": ["Inter"],
        "label-md": ["Inter"], "headline-md": ["Inter"], "body-md": ["Inter"], "body-sm": ["Inter"], "headline-sm": ["Inter"]
      }},
      "fontSize": {{
        "headline-lg": ["1.875rem", {{ "lineHeight": "2.25rem", "letterSpacing": "-0.02em", "fontWeight": "600" }}],
        "display": ["2.25rem", {{ "lineHeight": "2.75rem", "letterSpacing": "-0.025em", "fontWeight": "700" }}],
        "headline-lg-mobile": ["1.5rem", {{ "lineHeight": "2rem", "letterSpacing": "-0.015em", "fontWeight": "600" }}],
        "code-sm": ["0.8125rem", {{ "lineHeight": "1.25rem", "letterSpacing": "0", "fontWeight": "500" }}],
        "data-metric-lg": ["2rem", {{ "lineHeight": "2.25rem", "letterSpacing": "-0.03em", "fontWeight": "700" }}],
        "data-metric-sm": ["1.125rem", {{ "lineHeight": "1.5rem", "letterSpacing": "-0.02em", "fontWeight": "600" }}],
        "title-md": ["1rem", {{ "lineHeight": "1.5rem", "letterSpacing": "-0.005em", "fontWeight": "600" }}],
        "body-lg": ["1.125rem", {{ "lineHeight": "1.75rem", "fontWeight": "400" }}],
        "label-md": ["0.75rem", {{ "lineHeight": "1rem", "letterSpacing": "0.025em", "fontWeight": "500" }}],
        "headline-md": ["1.5rem", {{ "lineHeight": "2rem", "letterSpacing": "-0.015em", "fontWeight": "600" }}],
        "body-md": ["0.875rem", {{ "lineHeight": "1.375rem", "fontWeight": "400" }}],
        "body-sm": ["0.75rem", {{ "lineHeight": "1.125rem", "fontWeight": "400" }}],
        "headline-sm": ["1.25rem", {{ "lineHeight": "1.75rem", "letterSpacing": "-0.01em", "fontWeight": "600" }}]
      }}
    }}
  }}
}};
</script>
</head>
<body class="bg-surface font-body-md text-body-md text-on-surface min-h-screen flex flex-col">

<!-- Top Navigation Bar -->
<header class="fixed top-0 left-0 right-0 z-50 bg-surface/90 backdrop-blur-md border-b border-outline-variant/30 shadow-[0_1px_8px_rgba(0,0,0,0.4)]">
  <div class="h-16 max-w-6xl mx-auto px-gutter-tablet flex items-center justify-between gap-space-base">
    <div class="flex items-center gap-space-md min-w-0">
      <svg class="h-8 w-8 object-contain flex-shrink-0" fill="none" viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg">
        <rect fill="#0F172A" height="32" rx="8" width="32"></rect>
        <circle cx="8" cy="22" fill="#38BDF8" opacity="0.8" r="2.5"></circle>
        <circle cx="14" cy="18" fill="#38BDF8" opacity="0.6" r="2"></circle>
        <circle cx="20" cy="11" fill="#38BDF8" opacity="0.6" r="2"></circle>
        <circle cx="26" cy="7" fill="#38BDF8" opacity="0.9" r="2.5"></circle>
        <path d="M6 24 C 12 22, 18 14, 26 6" stroke="#6366F1" stroke-linecap="round" stroke-width="2.5"></path>
      </svg>
      <div class="flex items-center gap-space-sm truncate">
        <span class="font-title-md text-title-md text-on-surface font-semibold tracking-tight truncate">Advertising Sales Predictor</span>
        <span class="hidden sm:inline-flex items-center px-space-sm py-space-2xs rounded bg-surface-container-high border border-outline-variant/50 font-label-md text-label-md text-primary font-medium tracking-wide whitespace-nowrap">v1.0 • Polynomial Regression</span>
      </div>
    </div>
    <div class="flex items-center gap-space-lg flex-shrink-0">
      <nav class="flex items-center gap-space-xs" id="nav-container">
        <a id="nav-btn-predict" aria-current="page" class="px-space-base py-space-sm transition-colors bg-surface-container-high text-primary font-medium rounded-lg cursor-pointer" data-path="predict-sales">Predict Sales</a>
        <a id="nav-btn-how" class="px-space-base py-space-sm text-on-surface-variant hover:text-on-surface hover:bg-surface-container-low rounded-lg transition-colors font-body-md text-body-md cursor-pointer" data-path="how-it-works">How It Works</a>
      </nav>
    </div>
  </div>
</header>

<!-- PAGE 1: PREDICT SALES -->
<main id="view-predict-sales" class="w-full flex-1 pt-16 bg-surface">
  <div class="max-w-6xl mx-auto px-gutter-tablet py-space-2xl">
    <div class="flex flex-col w-full">
      <div class="flex flex-col gap-space-2xl w-full">
        <section class="flex flex-col gap-space-xs pb-space-sm">
          <div class="flex items-center gap-space-sm text-primary font-label-md text-label-md tracking-wider uppercase">
            <span class="w-2 h-2 rounded-full bg-primary animate-pulse"></span>
            Interactive Machine Learning
          </div>
          <h1 class="font-display text-display text-on-surface font-bold tracking-tight">
            Advertising Sales Predictor
          </h1>
          <p class="font-body-lg text-body-lg text-on-surface-variant max-w-3xl">
            Estimate sales from your advertising budget using Polynomial Regression.
          </p>
        </section>

        <section class="grid grid-cols-1 lg:grid-cols-12 gap-space-xl items-stretch">
          <!-- Left: Budget Input Controls -->
          <div class="lg:col-span-6 bg-surface-container rounded-xl p-space-xl shadow-lg flex flex-col justify-between">
            <div class="flex flex-col gap-space-lg">
              <div class="flex flex-col gap-space-2xs">
                <h2 class="font-headline-sm text-headline-sm text-on-surface font-semibold">
                  Set Advertising Budget
                </h2>
                <p class="font-body-sm text-body-sm text-on-surface-variant">
                  Enter spending across media channels ($k).
                </p>
              </div>
              <div class="flex flex-col gap-space-md">
                <!-- TV Slider -->
                <div class="flex flex-col gap-space-xs bg-surface-container-low p-space-md rounded-lg">
                  <div class="flex items-center justify-between">
                    <label class="font-title-md text-title-md text-on-surface font-medium" for="tv-input">
                      TV Advertising
                    </label>
                    <div class="flex items-center gap-1 text-primary font-title-md text-title-md font-semibold">
                      <span>$</span>
                      <span id="tv-val-display">150</span>
                      <span class="font-label-md text-label-md text-on-surface-variant font-normal">k</span>
                    </div>
                  </div>
                  <input class="w-full accent-primary-container h-1.5 bg-surface-container-highest rounded-lg cursor-pointer transition-all" id="tv-input" max="300" min="0" step="1" type="range" value="150"/>
                  <div class="flex justify-between font-label-md text-label-md text-on-surface-variant">
                    <span>$0k</span>
                    <span>$150k</span>
                    <span>$300k</span>
                  </div>
                </div>

                <!-- Radio Slider -->
                <div class="flex flex-col gap-space-xs bg-surface-container-low p-space-md rounded-lg">
                  <div class="flex items-center justify-between">
                    <label class="font-title-md text-title-md text-on-surface font-medium" for="radio-input">
                      Radio Advertising
                    </label>
                    <div class="flex items-center gap-1 text-primary font-title-md text-title-md font-semibold">
                      <span>$</span>
                      <span id="radio-val-display">25</span>
                      <span class="font-label-md text-label-md text-on-surface-variant font-normal">k</span>
                    </div>
                  </div>
                  <input class="w-full accent-primary-container h-1.5 bg-surface-container-highest rounded-lg cursor-pointer transition-all" id="radio-input" max="50" min="0" step="1" type="range" value="25"/>
                  <div class="flex justify-between font-label-md text-label-md text-on-surface-variant">
                    <span>$0k</span>
                    <span>$25k</span>
                    <span>$50k</span>
                  </div>
                </div>

                <!-- Newspaper Slider -->
                <div class="flex flex-col gap-space-xs bg-surface-container-low p-space-md rounded-lg">
                  <div class="flex items-center justify-between">
                    <label class="font-title-md text-title-md text-on-surface font-medium" for="newspaper-input">
                      Newspaper Advertising
                    </label>
                    <div class="flex items-center gap-1 text-primary font-title-md text-title-md font-semibold">
                      <span>$</span>
                      <span id="newspaper-val-display">20</span>
                      <span class="font-label-md text-label-md text-on-surface-variant font-normal">k</span>
                    </div>
                  </div>
                  <input class="w-full accent-primary-container h-1.5 bg-surface-container-highest rounded-lg cursor-pointer transition-all" id="newspaper-input" max="100" min="0" step="1" type="range" value="20"/>
                  <div class="flex justify-between font-label-md text-label-md text-on-surface-variant">
                    <span>$0k</span>
                    <span>$50k</span>
                    <span>$100k</span>
                  </div>
                </div>
              </div>
            </div>

            <div class="pt-space-lg flex flex-col gap-space-md">
              <p class="font-body-sm text-body-sm text-on-surface-variant flex items-center gap-space-xs">
                <span class="material-symbols-outlined text-primary text-[18px]">info</span>
                Try different advertising budgets to see how the prediction changes.
              </p>
              <button class="w-full py-space-md px-space-xl bg-primary-container hover:bg-primary text-on-primary-container font-headline-sm text-headline-sm font-semibold rounded-lg shadow transition-all duration-200 flex items-center justify-center gap-space-sm active:scale-[0.99] cursor-pointer" id="predict-btn">
                <span class="material-symbols-outlined text-[20px]">bolt</span>
                Predict Sales
              </button>
            </div>
          </div>

          <!-- Right: Prediction Result Display Card -->
          <div class="lg:col-span-6 bg-surface-container rounded-xl p-space-xl shadow-lg flex flex-col justify-between relative overflow-hidden">
            <div class="absolute -right-16 -top-16 w-48 h-48 bg-primary/10 rounded-full blur-2xl pointer-events-none"></div>
            <div class="flex items-center justify-between">
              <span class="inline-flex items-center gap-space-xs px-space-sm py-space-2xs rounded-full bg-surface-container-highest text-primary font-label-md text-label-md font-medium">
                <span class="material-symbols-outlined text-[14px]">model_training</span>
                Model: Polynomial Degree 2 (Trained)
              </span>
              <span class="font-code-sm text-code-sm text-on-surface-variant bg-surface-container-lowest px-space-sm py-space-2xs rounded">
                R² = {r2:.3f}
              </span>
            </div>
            <div class="my-space-xl flex flex-col items-center justify-center text-center">
              <span class="font-label-md text-label-md uppercase tracking-wider text-on-surface-variant mb-space-xs font-semibold">
                Predicted Sales
              </span>
              <div class="flex items-baseline justify-center gap-space-xs">
                <span class="font-display text-[4.5rem] leading-none text-primary font-bold tracking-tight" id="predicted-sales-number">
                  15.9
                </span>
                <span class="font-title-md text-title-md text-on-surface-variant font-medium">
                  k units
                </span>
              </div>
              <p class="mt-space-sm font-body-md text-body-md text-on-surface-variant max-w-sm">
                Estimated sales based on your advertising budget.
              </p>
            </div>
            <div class="p-space-md rounded-lg bg-surface-container-lowest flex items-center justify-between">
              <div class="flex items-center gap-space-sm">
                <span class="material-symbols-outlined text-on-surface-variant text-[20px]">payments</span>
                <span class="font-body-md text-body-md text-on-surface-variant">Total Ad Spend:</span>
              </div>
              <div class="font-title-md text-title-md text-on-surface font-semibold">
                $<span id="total-spend-display">195</span>k
              </div>
            </div>
          </div>
        </section>

        <!-- Chart Section -->
        <section class="bg-surface-container rounded-xl p-space-xl shadow-lg flex flex-col gap-space-lg">
          <div class="flex flex-col md:flex-row md:items-center justify-between gap-space-sm">
            <div>
              <h2 class="font-headline-sm text-headline-sm text-on-surface font-semibold">
                Sales vs. Advertising Spending
              </h2>
              <p class="font-body-sm text-body-sm text-on-surface-variant">
                Polynomial regression curve (Degree 2) fitted across combined spend vs. observed sales.
              </p>
            </div>
            <div class="flex flex-wrap items-center gap-space-md font-label-md text-label-md">
              <div class="flex items-center gap-space-xs text-on-surface-variant">
                <span class="w-2.5 h-2.5 rounded-full bg-outline-variant inline-block"></span>
                Dataset Observations
              </div>
              <div class="flex items-center gap-space-xs text-on-surface">
                <span class="w-4 h-0.5 bg-primary-container inline-block"></span>
                Polynomial Fit (Degree 2)
              </div>
              <div class="flex items-center gap-space-xs text-primary font-semibold">
                <span class="w-3 h-3 rounded-full bg-primary inline-block shadow-[0_0_8px_rgba(142,213,255,0.8)]"></span>
                Current Prediction
              </div>
            </div>
          </div>

          <div class="w-full bg-surface-container-lowest rounded-lg p-space-md overflow-hidden relative">
            <svg class="w-full h-auto select-none overflow-visible" id="regression-chart" viewBox="0 0 800 380">
              <defs>
                <linearGradient id="curveGradient" x1="0%" x2="100%" y1="0%" y2="0%">
                  <stop offset="0%" stop-color="#38bdf8"></stop>
                  <stop offset="100%" stop-color="#8ed5ff"></stop>
                </linearGradient>
                <filter height="200%" id="glow" width="200%" x="-50%" y="-50%">
                  <feDropShadow dx="0" dy="0" flood-color="#8ed5ff" flood-opacity="0.8" stdDeviation="4"></feDropShadow>
                </filter>
              </defs>
              <!-- Axes grid lines -->
              <g class="opacity-15 stroke-on-surface" stroke-dasharray="3 3">
                <line x1="60" x2="760" y1="40" y2="40"></line>
                <line x1="60" x2="760" y1="100" y2="100"></line>
                <line x1="60" x2="760" y1="160" y2="160"></line>
                <line x1="60" x2="760" y1="220" y2="220"></line>
                <line x1="60" x2="760" y1="280" y2="280"></line>
                <line x1="60" x2="760" y1="340" y2="340"></line>
                <line x1="60" x2="60" y1="40" y2="340"></line>
                <line x1="160" x2="160" y1="40" y2="340"></line>
                <line x1="260" x2="260" y1="40" y2="340"></line>
                <line x1="360" x2="360" y1="40" y2="340"></line>
                <line x1="460" x2="460" y1="40" y2="340"></line>
                <line x1="560" x2="560" y1="40" y2="340"></line>
                <line x1="660" x2="660" y1="40" y2="340"></line>
                <line x1="760" x2="760" y1="40" y2="340"></line>
              </g>
              <!-- Y Axis Labels -->
              <g class="fill-on-surface-variant text-[11px] font-medium" text-anchor="end">
                <text x="50" y="344">0</text>
                <text x="50" y="284">6</text>
                <text x="50" y="224">12</text>
                <text x="50" y="164">18</text>
                <text x="50" y="104">24</text>
                <text x="50" y="44">30</text>
              </g>
              <!-- X Axis Labels -->
              <g class="fill-on-surface-variant text-[11px] font-medium" text-anchor="middle">
                <text x="60" y="362">0</text>
                <text x="160" y="362">50</text>
                <text x="260" y="362">100</text>
                <text x="360" y="362">150</text>
                <text x="460" y="362">200</text>
                <text x="560" y="362">250</text>
                <text x="660" y="362">300</text>
                <text x="760" y="362">350</text>
              </g>
              <!-- Axis Titles -->
              <text class="fill-on-surface font-semibold text-[11px] tracking-wide" text-anchor="middle" x="410" y="378">
                Advertising Spending ($k)
              </text>
              <text class="fill-on-surface font-semibold text-[11px] tracking-wide" text-anchor="middle" transform="rotate(-90)" x="-190" y="20">
                Sales (Units)
              </text>
              <!-- Historical Observation Points from advertising.csv -->
              <g class="fill-outline opacity-40" id="historical-points">
{svg_circles_markup}
              </g>
              <!-- Polynomial Degree 2 Reference Curve -->
              <path d="M 60 302 Q 380 152 760 70" fill="none" stroke="url(#curveGradient)" stroke-linecap="round" stroke-width="3"></path>
              <!-- User's Prediction Highlight Target Lines -->
              <g class="stroke-primary/40" id="target-guidelines" stroke-dasharray="4 4" stroke-width="1.5">
                <line id="guide-x" x1="450" x2="450" y1="340" y2="181"></line>
                <line id="guide-y" x1="60" x2="450" y1="181" y2="181"></line>
              </g>
              <!-- User Prediction Indicator Dot & Callout -->
              <g id="prediction-marker" transform="translate(450, 181)">
                <circle class="fill-primary" filter="url(#glow)" r="8"></circle>
                <circle class="fill-surface-container-lowest" r="3.5"></circle>
                <!-- Floating Callout Label -->
                <g id="marker-callout" transform="translate(0, -32)">
                  <rect class="fill-surface-bright stroke-primary stroke-[1]" filter="drop-shadow(0 2px 4px rgba(0,0,0,0.5))" height="24" rx="4" width="210" x="-105" y="-12"></rect>
                  <text class="fill-on-surface font-code-sm text-[11px] font-semibold" id="marker-text" text-anchor="middle" x="0" y="4">
                    Your Budget: $195k → Predicted: 15.9
                  </text>
                </g>
              </g>
            </svg>
          </div>
          <div class="bg-surface-container-low rounded-lg p-space-lg flex flex-col md:flex-row gap-space-md items-start">
            <div class="w-8 h-8 rounded bg-surface-container-high flex items-center justify-center flex-shrink-0 text-primary">
              <span class="material-symbols-outlined text-[20px]">lightbulb</span>
            </div>
            <div class="flex flex-col gap-space-2xs">
              <h3 class="font-title-md text-title-md text-on-surface font-semibold">
                How to read this graph
              </h3>
              <p class="font-body-md text-body-md text-on-surface-variant leading-relaxed">
                The dots represent actual observations from the dataset. The curve represents the relationship learned by the Polynomial Regression model. Changing the advertising budget changes the predicted sales.
              </p>
            </div>
          </div>
        </section>

        <!-- Model Logic Section -->
        <section class="bg-surface-container rounded-xl p-space-xl shadow-lg flex flex-col gap-space-xl">
          <div class="flex flex-col gap-space-2xs">
            <span class="font-label-md text-label-md uppercase tracking-wider text-primary font-semibold">
              Model Logic
            </span>
            <h2 class="font-headline-sm text-headline-sm text-on-surface font-semibold">
              How was this calculated?
            </h2>
          </div>
          <div class="grid grid-cols-1 md:grid-cols-5 items-center gap-space-sm bg-surface-container-lowest p-space-lg rounded-xl">
            <div class="md:col-span-2 bg-surface-container p-space-md rounded-lg flex flex-col gap-space-2xs text-center md:text-left">
              <span class="font-label-md text-label-md uppercase text-on-surface-variant">Step 1: Budget Inputs</span>
              <div class="font-code-sm text-code-sm text-on-surface font-medium">
                TV (<span class="text-primary" id="calc-tv">$150k</span>) + 
                Radio (<span class="text-primary" id="calc-radio">$25k</span>) + 
                News (<span class="text-primary" id="calc-news">$20k</span>)
              </div>
              <span class="font-body-sm text-body-sm text-on-surface-variant">Total Spend = $<span id="calc-total">195</span>k</span>
            </div>
            <div class="flex items-center justify-center text-primary-container">
              <span class="material-symbols-outlined text-[28px] transform rotate-90 md:rotate-0">trending_flat</span>
            </div>
            <div class="md:col-span-1 bg-surface-container p-space-md rounded-lg flex flex-col gap-space-2xs text-center">
              <span class="font-label-md text-label-md uppercase text-on-surface-variant">Step 2: Regression</span>
              <span class="font-title-md text-title-md text-primary font-semibold">Polynomial Degree 2</span>
              <span class="font-code-sm text-code-sm text-on-surface-variant">f(x) = β₀ + β₁x + β₂x²</span>
            </div>
            <div class="flex items-center justify-center text-primary-container">
              <span class="material-symbols-outlined text-[28px] transform rotate-90 md:rotate-0">trending_flat</span>
            </div>
            <div class="md:col-span-1 bg-surface-container-high p-space-md rounded-lg flex flex-col gap-space-2xs text-center">
              <span class="font-label-md text-label-md uppercase text-primary font-semibold">Step 3: Outcome</span>
              <span class="font-headline-sm text-headline-sm text-on-surface font-bold">
                <span class="text-primary" id="calc-result">15.9</span>k
              </span>
              <span class="font-body-sm text-body-sm text-on-surface-variant">Predicted Sales</span>
            </div>
          </div>
          <div class="flex flex-col md:flex-row items-start md:items-center justify-between gap-space-md pt-space-xs">
            <p class="font-body-md text-body-md text-on-surface-variant max-w-2xl leading-relaxed">
              The model learned patterns from historical advertising and sales data. Polynomial Regression can capture curved relationships instead of assuming that every relationship is a straight line.
            </p>
            <a class="inline-flex items-center gap-space-xs px-space-base py-space-sm bg-surface-container-high hover:bg-surface-bright text-primary font-title-md text-title-md rounded-lg transition-colors flex-shrink-0 cursor-pointer" data-path="how-it-works">
              Learn more in How It Works
              <span class="material-symbols-outlined text-[18px]">arrow_forward</span>
            </a>
          </div>
        </section>
      </div>
    </div>
  </div>
</main>

<!-- PAGE 2: HOW IT WORKS -->
<main id="view-how-it-works" class="w-full flex-1 pt-16 bg-surface view-hidden">
  <div class="max-w-6xl mx-auto px-gutter-tablet py-space-2xl">
    <div class="flex flex-col w-full">
      <div class="flex flex-col gap-space-2xl w-full">
        <!-- Page Header Area -->
        <div class="flex flex-col md:flex-row md:items-end justify-between gap-space-base pb-space-lg">
          <div class="flex flex-col gap-space-xs">
            <div class="inline-flex items-center gap-space-xs font-label-md text-label-md text-primary font-medium tracking-wider uppercase">
              <span class="w-1.5 h-1.5 rounded-full bg-primary animate-pulse"></span>
              Interactive Architecture &amp; Theory
            </div>
            <h1 class="font-display text-display text-on-surface tracking-tight">How It Works</h1>
            <p class="font-body-lg text-body-lg text-on-surface-variant max-w-2xl">
              Understand how advertising data transforms into an accurate sales prediction through Degree-2 polynomial regression.
            </p>
          </div>
          <a class="inline-flex items-center gap-space-xs px-space-base py-space-sm rounded-lg bg-surface-container-high hover:bg-surface-bright text-primary font-title-md text-title-md transition-colors self-start md:self-auto cursor-pointer" data-path="predict-sales">
            <span class="material-symbols-outlined text-[18px]">query_stats</span>
            Open Live Predictor
          </a>
        </div>

        <!-- Section 1: The Advertising Data -->
        <section class="rounded-xl bg-surface-container p-space-xl flex flex-col gap-space-xl">
          <div class="flex items-center justify-between">
            <div class="flex items-center gap-space-sm">
              <span class="px-space-sm py-space-2xs rounded bg-primary text-on-primary font-label-md text-label-md font-bold">01</span>
              <h2 class="font-headline-md text-headline-md text-on-surface">The Advertising Data</h2>
            </div>
            <span class="font-label-md text-label-md text-on-surface-variant uppercase tracking-wider hidden sm:inline">Feature Mapping</span>
          </div>
          <p class="font-body-md text-body-md text-on-surface-variant">
            TV, Radio, and Newspaper are the numeric inputs fed into the regression algorithm. Sales represents the continuous target response variable the model learns to forecast.
          </p>
          <!-- 4 Data Cards Grid -->
          <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-space-md">
            <div class="rounded-lg bg-surface-container-low p-space-base flex flex-col gap-space-xs hover:bg-surface-container-high transition-colors">
              <div class="flex items-center justify-between text-on-surface-variant">
                <span class="material-symbols-outlined text-[20px] text-primary">tv</span>
                <span class="font-label-md text-label-md uppercase tracking-wider text-primary">Input Feature</span>
              </div>
              <span class="font-title-md text-title-md text-on-surface">TV Advertising</span>
              <span class="font-body-sm text-body-sm text-on-surface-variant">Broadcast media expenditure in thousands ($k). Primary baseline driver.</span>
            </div>
            <div class="rounded-lg bg-surface-container-low p-space-base flex flex-col gap-space-xs hover:bg-surface-container-high transition-colors">
              <div class="flex items-center justify-between text-on-surface-variant">
                <span class="material-symbols-outlined text-[20px] text-primary">radio</span>
                <span class="font-label-md text-label-md uppercase tracking-wider text-primary">Input Feature</span>
              </div>
              <span class="font-title-md text-title-md text-on-surface">Radio Advertising</span>
              <span class="font-body-sm text-body-sm text-on-surface-variant">Audio frequency investment ($k). High cross-channel multiplier impact.</span>
            </div>
            <div class="rounded-lg bg-surface-container-low p-space-base flex flex-col gap-space-xs hover:bg-surface-container-high transition-colors">
              <div class="flex items-center justify-between text-on-surface-variant">
                <span class="material-symbols-outlined text-[20px] text-primary">newspaper</span>
                <span class="font-label-md text-label-md uppercase tracking-wider text-primary">Input Feature</span>
              </div>
              <span class="font-title-md text-title-md text-on-surface">Newspaper Advertising</span>
              <span class="font-body-sm text-body-sm text-on-surface-variant">Print publications and localized placements ($k). Secondary channel.</span>
            </div>
            <div class="rounded-lg bg-surface-container-high p-space-base flex flex-col gap-space-xs">
              <div class="flex items-center justify-between text-on-surface">
                <span class="material-symbols-outlined text-[20px] text-tertiary">trending_up</span>
                <span class="font-label-md text-label-md uppercase tracking-wider text-tertiary">Target Output</span>
              </div>
              <span class="font-title-md text-title-md text-on-surface">Sales Volume</span>
              <span class="font-body-sm text-body-sm text-on-surface-variant">Product units sold in thousands (k). The target parameter to optimize.</span>
            </div>
          </div>
          <!-- Flow Architecture -->
          <div class="rounded-lg bg-surface-container-lowest p-space-lg flex flex-col items-center justify-center">
            <div class="w-full flex flex-col lg:flex-row items-center justify-between gap-space-md font-code-sm text-code-sm">
              <div class="flex-1 w-full flex items-center justify-center gap-space-sm p-space-md rounded bg-surface-container-low text-on-surface">
                <span class="material-symbols-outlined text-primary text-[18px]">tune</span>
                <span class="font-semibold">[ TV + Radio + Newspaper ]</span>
              </div>
              <div class="flex items-center gap-space-xs text-on-surface-variant py-space-xs px-space-sm">
                <span class="hidden lg:inline text-primary">────────</span>
                <span class="font-label-md text-label-md text-primary font-medium tracking-wide">(Inputs Matrix)</span>
                <span class="material-symbols-outlined text-primary text-[18px]">arrow_forward</span>
              </div>
              <div class="flex-1 w-full flex flex-col items-center justify-center p-space-md rounded bg-surface-container-high text-on-surface">
                <div class="flex items-center gap-space-xs text-primary font-semibold">
                  <span class="material-symbols-outlined text-[18px]">functions</span>
                  <span>Degree-2 Model</span>
                </div>
                <span class="font-label-md text-label-md text-on-surface-variant">f(x, x², x_i x_j)</span>
              </div>
              <div class="flex items-center gap-space-xs text-on-surface-variant py-space-xs px-space-sm">
                <span class="hidden lg:inline text-tertiary">────────</span>
                <span class="font-label-md text-label-md text-tertiary font-medium tracking-wide">(Target Prediction)</span>
                <span class="material-symbols-outlined text-tertiary text-[18px]">arrow_forward</span>
              </div>
              <div class="flex-1 w-full flex items-center justify-center gap-space-sm p-space-md rounded bg-surface-container-low text-tertiary font-semibold">
                <span class="material-symbols-outlined text-[18px]">insights</span>
                <span>[ Predicted Sales ŷ ]</span>
              </div>
            </div>
          </div>
        </section>

        <!-- Section 2: How Polynomial Regression Works -->
        <section class="rounded-xl bg-surface-container p-space-xl flex flex-col gap-space-xl">
          <div class="flex items-center justify-between">
            <div class="flex items-center gap-space-sm">
              <span class="px-space-sm py-space-2xs rounded bg-primary text-on-primary font-label-md text-label-md font-bold">02</span>
              <h2 class="font-headline-md text-headline-md text-on-surface">How Polynomial Regression Learns</h2>
            </div>
            <span class="font-label-md text-label-md text-primary bg-surface-container-high px-space-sm py-space-2xs rounded">Degree 2 Pipeline</span>
          </div>
          <!-- Step Horizontal Process -->
          <div class="grid grid-cols-1 md:grid-cols-5 gap-space-sm">
            <div class="flex flex-col gap-space-sm p-space-base rounded-lg bg-surface-container-low relative">
              <div class="flex items-center justify-between text-on-surface-variant">
                <span class="font-label-md text-label-md text-primary font-bold">STEP 01</span>
                <span class="material-symbols-outlined text-[18px] text-primary">dataset</span>
              </div>
              <span class="font-title-md text-title-md text-on-surface">Historical Data</span>
              <p class="font-body-sm text-body-sm text-on-surface-variant">
                Raw observational records matching past channel ad spend against actual resulting unit sales.
              </p>
            </div>
            <div class="flex flex-col gap-space-sm p-space-base rounded-lg bg-surface-container-low relative">
              <div class="flex items-center justify-between text-on-surface-variant">
                <span class="font-label-md text-label-md text-primary font-bold">STEP 02</span>
                <span class="material-symbols-outlined text-[18px] text-primary">hub</span>
              </div>
              <span class="font-title-md text-title-md text-on-surface">Learns Patterns</span>
              <p class="font-body-sm text-body-sm text-on-surface-variant">
                The algorithm scans correlations and channel dynamics across simultaneous media allocations.
              </p>
            </div>
            <div class="flex flex-col gap-space-sm p-space-base rounded-lg bg-surface-container-high relative">
              <div class="flex items-center justify-between text-on-surface">
                <span class="font-label-md text-label-md text-primary font-bold">STEP 03</span>
                <span class="material-symbols-outlined text-[18px] text-primary">superscript</span>
              </div>
              <span class="font-title-md text-title-md text-on-surface">Polynomial Shift</span>
              <p class="font-body-sm text-body-sm text-on-surface-variant">
                Expands base features into squared ($x^2$) and cross-interaction terms ($x_i \\cdot x_j$) to capture nonlinear curves.
              </p>
            </div>
            <div class="flex flex-col gap-space-sm p-space-base rounded-lg bg-surface-container-low relative">
              <div class="flex items-center justify-between text-on-surface-variant">
                <span class="font-label-md text-label-md text-primary font-bold">STEP 04</span>
                <span class="material-symbols-outlined text-[18px] text-primary">query_builder</span>
              </div>
              <span class="font-title-md text-title-md text-on-surface">Optimal Fit</span>
              <p class="font-body-sm text-body-sm text-on-surface-variant">
                Calculates regression coefficients by minimizing the Mean Squared Error (residuals) to the training points.
              </p>
            </div>
            <div class="flex flex-col gap-space-sm p-space-base rounded-lg bg-surface-container-low relative">
              <div class="flex items-center justify-between text-on-surface-variant">
                <span class="font-label-md text-label-md text-tertiary font-bold">STEP 05</span>
                <span class="material-symbols-outlined text-[18px] text-tertiary">check_circle</span>
              </div>
              <span class="font-title-md text-title-md text-on-surface">Predicted Sales</span>
              <p class="font-body-sm text-body-sm text-on-surface-variant">
                Executes fast evaluation for any novel multi-budget distribution to produce an accurate target projection.
              </p>
            </div>
          </div>
          <div class="rounded-lg bg-surface-container-lowest p-space-base flex items-start gap-space-md">
            <span class="material-symbols-outlined text-primary text-[22px] flex-shrink-0 mt-0.5">lightbulb</span>
            <div class="flex flex-col gap-space-2xs">
              <span class="font-title-md text-title-md text-on-surface">Why Polynomial over Simple Linear?</span>
              <p class="font-body-sm text-body-sm text-on-surface-variant">
                Polynomial Regression allows the model to learn curved relationships and more complex patterns in the data rather than forcing a straight line. This Version 1 model uses Polynomial Degree 2, capturing non-linear response rates and cross-channel synergy.
              </p>
            </div>
          </div>
        </section>

        <!-- Section 3: What Does the Curve Mean? -->
        <section class="rounded-xl bg-surface-container p-space-xl flex flex-col gap-space-xl">
          <div class="flex items-center justify-between">
            <div class="flex items-center gap-space-sm">
              <span class="px-space-sm py-space-2xs rounded bg-primary text-on-primary font-label-md text-label-md font-bold">03</span>
              <h2 class="font-headline-md text-headline-md text-on-surface">What Does the Curve Mean?</h2>
            </div>
            <span class="font-label-md text-label-md text-on-surface-variant uppercase tracking-wider">Geometric Intuition</span>
          </div>
          <div class="grid grid-cols-1 lg:grid-cols-12 gap-space-xl items-center">
            <div class="lg:col-span-7 flex flex-col gap-space-sm">
              <div class="w-full bg-surface-container-lowest p-space-base rounded-lg flex flex-col gap-space-xs">
                <div class="flex items-center justify-between text-on-surface-variant font-code-sm text-code-sm">
                  <span class="flex items-center gap-space-xs">
                    <span class="w-2.5 h-2.5 rounded-full bg-primary inline-block"></span>
                    Polynomial Regression Curve (Degree 2)
                  </span>
                  <span class="flex items-center gap-space-xs text-on-surface-variant">
                    <span class="w-2.5 h-0.5 bg-outline inline-block"></span>
                    Linear Assumption (Reference)
                  </span>
                </div>
                <div class="relative w-full aspect-[16/9] min-h-[220px]">
                  <svg class="w-full h-full select-none" preserveaspectratio="xMidYMid meet" viewBox="0 0 500 280">
                    <defs>
                      <linearGradient id="areaGlow" x1="0%" x2="0%" y1="0%" y2="100%">
                        <stop offset="0%" stop-color="#38bdf8" stop-opacity="0.18"></stop>
                        <stop offset="100%" stop-color="#38bdf8" stop-opacity="0.0"></stop>
                      </linearGradient>
                    </defs>
                    <g opacity="0.4" stroke="#3e484f" stroke-dasharray="3,3" stroke-width="0.75">
                      <line x1="60" x2="470" y1="40" y2="40"></line>
                      <line x1="60" x2="470" y1="90" y2="90"></line>
                      <line x1="60" x2="470" y1="140" y2="140"></line>
                      <line x1="60" x2="470" y1="190" y2="190"></line>
                      <line x1="60" x2="470" y1="240" y2="240"></line>
                      <line x1="60" x2="60" y1="40" y2="240"></line>
                      <line x1="160" x2="160" y1="40" y2="240"></line>
                      <line x1="260" x2="260" y1="40" y2="240"></line>
                      <line x1="360" x2="360" y1="40" y2="240"></line>
                      <line x1="470" x2="470" y1="40" y2="240"></line>
                    </g>
                    <line stroke="#87929a" stroke-width="1.5" x1="60" x2="470" y1="240" y2="240"></line>
                    <line stroke="#87929a" stroke-width="1.5" x1="60" x2="60" y1="40" y2="240"></line>
                    <text fill="#bdc8d1" font-family="Inter" font-size="11" font-weight="500" text-anchor="middle" x="260" y="270">Advertising Spending ($k) ──►</text>
                    <text fill="#bdc8d1" font-family="Inter" font-size="11" font-weight="500" text-anchor="middle" transform="rotate(-90 25 140)" x="25" y="140">Predicted Sales (Units) ──►</text>
                    <line opacity="0.6" stroke="#87929a" stroke-dasharray="4,4" stroke-width="1.5" x1="60" x2="450" y1="220" y2="80"></line>
                    <path d="M 60 220 Q 180 130, 300 80 T 450 62 L 450 240 L 60 240 Z" fill="url(#areaGlow)"></path>
                    <path d="M 60 220 Q 180 130, 300 80 T 450 62" fill="none" stroke="#38bdf8" stroke-linecap="round" stroke-width="3"></path>
                    <g fill="#38bdf8" fill-opacity="0.3" stroke="#38bdf8" stroke-width="1">
                      <circle cx="85" cy="205" r="3.5"></circle>
                      <circle cx="110" cy="180" r="3.5"></circle>
                      <circle cx="140" cy="165" r="3.5"></circle>
                      <circle cx="170" cy="130" r="3.5"></circle>
                      <circle cx="210" cy="115" r="3.5"></circle>
                      <circle cx="245" cy="100" r="3.5"></circle>
                      <circle cx="290" cy="85" r="3.5"></circle>
                      <circle cx="330" cy="78" r="3.5"></circle>
                      <circle cx="380" cy="70" r="3.5"></circle>
                      <circle cx="430" cy="65" r="3.5"></circle>
                    </g>
                    <circle cx="150" cy="148" fill="#38bdf8" r="4.5"></circle>
                    <rect fill="#171f33" height="22" rx="4" width="95" x="110" y="102"></rect>
                    <text fill="#8ed5ff" font-family="Inter" font-size="9" font-weight="600" text-anchor="middle" x="157" y="117">Steep Early Gains</text>
                    <circle cx="390" cy="68" fill="#ffc176" r="4.5"></circle>
                    <rect fill="#171f33" height="22" rx="4" width="120" x="330" y="32"></rect>
                    <text fill="#ffc176" font-family="Inter" font-size="9" font-weight="600" text-anchor="middle" x="390" y="47">Diminishing Returns (Tapers)</text>
                  </svg>
                </div>
              </div>
            </div>
            <div class="lg:col-span-5 flex flex-col gap-space-md">
              <div class="flex flex-col gap-space-xs">
                <span class="font-title-md text-title-md text-on-surface">Nonlinear Dynamics</span>
                <p class="font-body-md text-body-md text-on-surface-variant leading-relaxed">
                  The curve shows how the model estimates the relationship between advertising spending and sales. A curve can represent situations where the effect of additional advertising is not exactly the same at every spending level.
                </p>
              </div>
              <div class="rounded-lg bg-surface-container-low p-space-base flex flex-col gap-space-xs">
                <div class="flex items-center gap-space-xs text-tertiary">
                  <span class="material-symbols-outlined text-[18px]">show_chart</span>
                  <span class="font-title-md text-title-md font-semibold">The Law of Diminishing Returns</span>
                </div>
                <p class="font-body-sm text-body-sm text-on-surface-variant">
                  At higher spending levels, the increase in predicted sales may become smaller. In business strategy, saturation occurs when your target audience has already seen the campaign multiple times.
                </p>
              </div>
              <div class="grid grid-cols-2 gap-space-sm pt-space-xs font-code-sm text-code-sm">
                <div class="rounded bg-surface-container-lowest p-space-sm flex flex-col">
                  <span class="text-on-surface-variant text-label-md">Phase 1 ($0k - $100k)</span>
                  <span class="text-primary font-bold">High Elasticity</span>
                </div>
                <div class="rounded bg-surface-container-lowest p-space-sm flex flex-col">
                  <span class="text-on-surface-variant text-label-md">Phase 2 ($250k+)</span>
                  <span class="text-tertiary font-bold">Channel Saturation</span>
                </div>
              </div>
            </div>
          </div>
        </section>

        <!-- Section 4: Try Different Values (Scenarios) -->
        <section class="rounded-xl bg-surface-container p-space-xl flex flex-col gap-space-xl">
          <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-space-xs">
            <div class="flex items-center gap-space-sm">
              <span class="px-space-sm py-space-2xs rounded bg-primary text-on-primary font-label-md text-label-md font-bold">04</span>
              <h2 class="font-headline-md text-headline-md text-on-surface">Demonstrating Changing Inputs</h2>
            </div>
            <span class="font-label-md text-label-md text-on-surface-variant">Sensitivity Demonstration</span>
          </div>
          <p class="font-body-md text-body-md text-on-surface-variant">
            Observe how re-allocating or scaling channel investments immediately recalculates model confidence and output volumes:
          </p>
          <div class="grid grid-cols-1 md:grid-cols-2 gap-space-lg">
            <!-- Scenario 1 -->
            <div class="rounded-lg bg-surface-container-low p-space-lg flex flex-col justify-between gap-space-md hover:bg-surface-container-high transition-colors">
              <div class="flex flex-col gap-space-sm">
                <div class="flex items-center justify-between">
                  <span class="px-space-sm py-space-2xs rounded bg-surface-container-highest font-label-md text-label-md text-on-surface font-semibold tracking-wide">
                    SCENARIO 01: MODERATE BUDGET
                  </span>
                  <span class="font-code-sm text-code-sm text-primary">Baseline Test</span>
                </div>
                <div class="grid grid-cols-3 gap-space-xs pt-space-xs">
                  <div class="bg-surface-container-lowest p-space-sm rounded flex flex-col">
                    <span class="text-label-md text-on-surface-variant uppercase">TV</span>
                    <span class="font-data-metric-sm text-data-metric-sm text-on-surface">$100k</span>
                  </div>
                  <div class="bg-surface-container-lowest p-space-sm rounded flex flex-col">
                    <span class="text-label-md text-on-surface-variant uppercase">Radio</span>
                    <span class="font-data-metric-sm text-data-metric-sm text-on-surface">$20k</span>
                  </div>
                  <div class="bg-surface-container-lowest p-space-sm rounded flex flex-col">
                    <span class="text-label-md text-on-surface-variant uppercase">News</span>
                    <span class="font-data-metric-sm text-data-metric-sm text-on-surface">$10k</span>
                  </div>
                </div>
                <div class="flex items-center justify-between font-body-sm text-body-sm text-on-surface-variant pt-space-xs">
                  <span>Total Capital Committed:</span>
                  <span class="font-bold text-on-surface">$130,000</span>
                </div>
              </div>
              <div class="rounded bg-surface-container-lowest p-space-md flex items-center justify-between">
                <div class="flex flex-col">
                  <span class="font-label-md text-label-md text-on-surface-variant uppercase">Estimated Prediction</span>
                  <span class="font-data-metric-lg text-data-metric-lg text-primary">~12.5k</span>
                </div>
                <div class="text-right">
                  <span class="font-code-sm text-code-sm text-on-surface-variant">Units Sold</span>
                  <div class="font-label-md text-label-md text-primary font-medium">Model Output</div>
                </div>
              </div>
            </div>

            <!-- Scenario 2 -->
            <div class="rounded-lg bg-surface-container-low p-space-lg flex flex-col justify-between gap-space-md hover:bg-surface-container-high transition-colors">
              <div class="flex flex-col gap-space-sm">
                <div class="flex items-center justify-between">
                  <span class="px-space-sm py-space-2xs rounded bg-primary-container/20 font-label-md text-label-md text-primary font-semibold tracking-wide">
                    SCENARIO 02: SCALED TV CAMPAIGN
                  </span>
                  <span class="font-code-sm text-code-sm text-tertiary">+100k TV Push</span>
                </div>
                <div class="grid grid-cols-3 gap-space-xs pt-space-xs">
                  <div class="bg-surface-container-lowest p-space-sm rounded flex flex-col">
                    <span class="text-label-md text-on-surface-variant uppercase">TV</span>
                    <span class="font-data-metric-sm text-data-metric-sm text-primary">$200k</span>
                  </div>
                  <div class="bg-surface-container-lowest p-space-sm rounded flex flex-col">
                    <span class="text-label-md text-on-surface-variant uppercase">Radio</span>
                    <span class="font-data-metric-sm text-data-metric-sm text-on-surface">$20k</span>
                  </div>
                  <div class="bg-surface-container-lowest p-space-sm rounded flex flex-col">
                    <span class="text-label-md text-on-surface-variant uppercase">News</span>
                    <span class="font-data-metric-sm text-data-metric-sm text-on-surface">$10k</span>
                  </div>
                </div>
                <div class="flex items-center justify-between font-body-sm text-body-sm text-on-surface-variant pt-space-xs">
                  <span>Total Capital Committed:</span>
                  <span class="font-bold text-on-surface">$230,000</span>
                </div>
              </div>
              <div class="rounded bg-surface-container-lowest p-space-md flex items-center justify-between">
                <div class="flex flex-col">
                  <span class="font-label-md text-label-md text-on-surface-variant uppercase">Estimated Prediction</span>
                  <span class="font-data-metric-lg text-data-metric-lg text-tertiary">~17.7k</span>
                </div>
                <div class="text-right">
                  <span class="font-code-sm text-code-sm text-tertiary font-bold">+42.1% Lift</span>
                  <div class="font-label-md text-label-md text-on-surface-variant">Non-linear Yield</div>
                </div>
              </div>
            </div>
          </div>
          <div class="flex items-center justify-between flex-wrap gap-space-sm pt-space-xs">
            <p class="font-body-sm text-body-sm text-on-surface-variant italic">
              Example comparisons from trained Polynomial Regression model to illustrate sensitivity to input changes.
            </p>
            <span class="font-code-sm text-code-sm text-on-surface-variant">Model Version: v1.0-Poly2</span>
          </div>
          <div class="pt-space-md flex justify-center">
            <a class="inline-flex items-center gap-space-sm px-space-2xl py-space-md rounded-lg bg-primary text-on-primary font-headline-sm text-headline-sm hover:bg-primary-fixed-dim transition-all shadow-md cursor-pointer" data-path="predict-sales">
              <span class="material-symbols-outlined text-[22px]">calculate</span>
              Return to Predict Sales
            </a>
          </div>
        </section>
      </div>
    </div>
  </div>
</main>

<!-- Footer -->
<footer class="w-full bg-surface-container-lowest border-t border-outline-variant/20 py-space-lg">
  <div class="max-w-6xl mx-auto px-gutter-tablet text-center">
    <p class="font-body-sm text-body-sm text-on-surface-variant/80 tracking-wide">
      Advertising Sales Predictor — Interactive Machine Learning Project (Degree 2 Polynomial Model)
    </p>
  </div>
</footer>

<!-- Interactive Logic and Polynomial Model Calculation -->
<script>
  (function() {{
    // Navigation handlers
    const navBtnPredict = document.getElementById('nav-btn-predict');
    const navBtnHow = document.getElementById('nav-btn-how');
    const viewPredict = document.getElementById('view-predict-sales');
    const viewHow = document.getElementById('view-how-it-works');

    function showPage(pageId) {{
      if (pageId === 'predict-sales') {{
        viewPredict.classList.remove('view-hidden');
        viewHow.classList.add('view-hidden');
        navBtnPredict.className = "px-space-base py-space-sm transition-colors bg-surface-container-high text-primary font-medium rounded-lg cursor-pointer";
        navBtnPredict.setAttribute('aria-current', 'page');
        navBtnHow.className = "px-space-base py-space-sm text-on-surface-variant hover:text-on-surface hover:bg-surface-container-low rounded-lg transition-colors font-body-md text-body-md cursor-pointer";
        navBtnHow.removeAttribute('aria-current');
      }} else {{
        viewHow.classList.remove('view-hidden');
        viewPredict.classList.add('view-hidden');
        navBtnHow.className = "px-space-base py-space-sm transition-colors bg-surface-container-high text-primary font-medium rounded-lg cursor-pointer";
        navBtnHow.setAttribute('aria-current', 'page');
        navBtnPredict.className = "px-space-base py-space-sm text-on-surface-variant hover:text-on-surface hover:bg-surface-container-low rounded-lg transition-colors font-body-md text-body-md cursor-pointer";
        navBtnPredict.removeAttribute('aria-current');
      }}
      window.scrollTo({{ top: 0, behavior: 'smooth' }});
    }}

    document.querySelectorAll('[data-path]').forEach(function(el) {{
      el.addEventListener('click', function(e) {{
        e.preventDefault();
        const targetPath = el.getAttribute('data-path');
        showPage(targetPath);
      }});
    }});

    // Regression Model Elements
    const tvInput = document.getElementById('tv-input');
    const radioInput = document.getElementById('radio-input');
    const newspaperInput = document.getElementById('newspaper-input');
    const predictBtn = document.getElementById('predict-btn');

    const tvValDisplay = document.getElementById('tv-val-display');
    const radioValDisplay = document.getElementById('radio-val-display');
    const newspaperValDisplay = document.getElementById('newspaper-val-display');

    const predictedSalesNumber = document.getElementById('predicted-sales-number');
    const totalSpendDisplay = document.getElementById('total-spend-display');

    const calcTv = document.getElementById('calc-tv');
    const calcRadio = document.getElementById('calc-radio');
    const calcNews = document.getElementById('calc-news');
    const calcTotal = document.getElementById('calc-total');
    const calcResult = document.getElementById('calc-result');

    const marker = document.getElementById('prediction-marker');
    const guideX = document.getElementById('guide-x');
    const guideY = document.getElementById('guide-y');
    const markerText = document.getElementById('marker-text');

    // Degree 2 Polynomial Regression Weights from trained model
    const beta0 = {intercept};
    const beta_tv = {coef_dict.get('TV', 0.0)};
    const beta_radio = {coef_dict.get('Radio', 0.0)};
    const beta_news = {coef_dict.get('Newspaper', 0.0)};
    const beta_tv2 = {coef_dict.get('TV^2', 0.0)};
    const beta_tv_radio = {coef_dict.get('TV Radio', 0.0)};
    const beta_tv_news = {coef_dict.get('TV Newspaper', 0.0)};
    const beta_radio2 = {coef_dict.get('Radio^2', 0.0)};
    const beta_radio_news = {coef_dict.get('Radio Newspaper', 0.0)};
    const beta_news2 = {coef_dict.get('Newspaper^2', 0.0)};

    function calculatePrediction() {{
      const tv = parseFloat(tvInput.value) || 0;
      const radio = parseFloat(radioInput.value) || 0;
      const news = parseFloat(newspaperInput.value) || 0;
      const total = tv + radio + news;

      // Polynomial degree 2 calculation
      let sales = beta0 
        + (beta_tv * tv) 
        + (beta_radio * radio) 
        + (beta_news * news) 
        + (beta_tv2 * tv * tv) 
        + (beta_tv_radio * tv * radio) 
        + (beta_tv_news * tv * news) 
        + (beta_radio2 * radio * radio) 
        + (beta_radio_news * radio * news) 
        + (beta_news2 * news * news);

      sales = Math.max(0.0, sales);
      const salesFormatted = sales.toFixed(1);

      // Update text displays
      tvValDisplay.textContent = tv;
      radioValDisplay.textContent = radio;
      newspaperValDisplay.textContent = news;
      totalSpendDisplay.textContent = total;
      predictedSalesNumber.textContent = salesFormatted;

      calcTv.textContent = '$' + tv + 'k';
      calcRadio.textContent = '$' + radio + 'k';
      calcNews.textContent = '$' + news + 'k';
      calcTotal.textContent = total;
      calcResult.textContent = salesFormatted;

      // Visual chart coordinates (X: 0 spend -> 60px, 350 spend -> 760px; Y: 0 units -> 340px, 30 units -> 40px)
      const clampedSpend = Math.min(350, Math.max(0, total));
      const targetX = 60 + (clampedSpend * 2);
      const clampedSales = Math.min(30, Math.max(0, sales));
      const targetY = 340 - (clampedSales * 10);

      if (marker) marker.setAttribute('transform', `translate(${{targetX}}, ${{targetY}})`);
      if (guideX) {{
        guideX.setAttribute('x1', targetX);
        guideX.setAttribute('x2', targetX);
        guideX.setAttribute('y2', targetY);
      }}
      if (guideY) {{
        guideY.setAttribute('y1', targetY);
        guideY.setAttribute('y2', targetY);
        guideY.setAttribute('x2', targetX);
      }}
      if (markerText) {{
        markerText.textContent = `Your Budget: $${{total}}k → Predicted: ${{salesFormatted}}`;
      }}
    }}

    tvInput.addEventListener('input', calculatePrediction);
    radioInput.addEventListener('input', calculatePrediction);
    newspaperInput.addEventListener('input', calculatePrediction);

    predictBtn.addEventListener('click', function() {{
      calculatePrediction();
      predictBtn.classList.add('scale-95');
      setTimeout(() => predictBtn.classList.remove('scale-95'), 150);
    }});

    // Initialize default prediction
    calculatePrediction();
  }})();
</script>
</body>
</html>
"""

components.html(html_content, height=1400, scrolling=True)
