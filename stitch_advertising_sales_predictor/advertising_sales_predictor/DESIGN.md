---
name: Advertising Sales Predictor
colors:
  surface: '#0b1326'
  surface-dim: '#0b1326'
  surface-bright: '#31394d'
  surface-container-lowest: '#060e20'
  surface-container-low: '#131b2e'
  surface-container: '#171f33'
  surface-container-high: '#222a3d'
  surface-container-highest: '#2d3449'
  on-surface: '#dae2fd'
  on-surface-variant: '#bdc8d1'
  inverse-surface: '#dae2fd'
  inverse-on-surface: '#283044'
  outline: '#87929a'
  outline-variant: '#3e484f'
  surface-tint: '#7bd0ff'
  primary: '#8ed5ff'
  on-primary: '#00354a'
  primary-container: '#38bdf8'
  on-primary-container: '#004965'
  inverse-primary: '#00668a'
  secondary: '#c0c1ff'
  on-secondary: '#1000a9'
  secondary-container: '#3131c0'
  on-secondary-container: '#b0b2ff'
  tertiary: '#ffc176'
  on-tertiary: '#472a00'
  tertiary-container: '#f1a02b'
  on-tertiary-container: '#613b00'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#c4e7ff'
  primary-fixed-dim: '#7bd0ff'
  on-primary-fixed: '#001e2c'
  on-primary-fixed-variant: '#004c69'
  secondary-fixed: '#e1e0ff'
  secondary-fixed-dim: '#c0c1ff'
  on-secondary-fixed: '#07006c'
  on-secondary-fixed-variant: '#2f2ebe'
  tertiary-fixed: '#ffddb8'
  tertiary-fixed-dim: '#ffb960'
  on-tertiary-fixed: '#2a1700'
  on-tertiary-fixed-variant: '#653e00'
  background: '#0b1326'
  on-background: '#dae2fd'
  surface-variant: '#2d3449'
typography:
  display:
    fontFamily: Inter
    fontSize: 2.25rem
    fontWeight: '700'
    lineHeight: 2.75rem
    letterSpacing: -0.025em
  headline-lg:
    fontFamily: Inter
    fontSize: 1.875rem
    fontWeight: '600'
    lineHeight: 2.25rem
    letterSpacing: -0.02em
  headline-lg-mobile:
    fontFamily: Inter
    fontSize: 1.5rem
    fontWeight: '600'
    lineHeight: 2rem
    letterSpacing: -0.015em
  headline-md:
    fontFamily: Inter
    fontSize: 1.5rem
    fontWeight: '600'
    lineHeight: 2rem
    letterSpacing: -0.015em
  headline-sm:
    fontFamily: Inter
    fontSize: 1.25rem
    fontWeight: '600'
    lineHeight: 1.75rem
    letterSpacing: -0.01em
  title-md:
    fontFamily: Inter
    fontSize: 1rem
    fontWeight: '600'
    lineHeight: 1.5rem
    letterSpacing: -0.005em
  body-lg:
    fontFamily: Inter
    fontSize: 1.125rem
    fontWeight: '400'
    lineHeight: 1.75rem
  body-md:
    fontFamily: Inter
    fontSize: 0.875rem
    fontWeight: '400'
    lineHeight: 1.375rem
  body-sm:
    fontFamily: Inter
    fontSize: 0.75rem
    fontWeight: '400'
    lineHeight: 1.125rem
  label-md:
    fontFamily: Inter
    fontSize: 0.75rem
    fontWeight: '500'
    lineHeight: 1rem
    letterSpacing: 0.025em
  data-metric-lg:
    fontFamily: Inter
    fontSize: 2rem
    fontWeight: '700'
    lineHeight: 2.25rem
    letterSpacing: -0.03em
  data-metric-sm:
    fontFamily: Inter
    fontSize: 1.125rem
    fontWeight: '600'
    lineHeight: 1.5rem
    letterSpacing: -0.02em
  code-sm:
    fontFamily: Inter
    fontSize: 0.8125rem
    fontWeight: '500'
    lineHeight: 1.25rem
    letterSpacing: '0'
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  space-2xs: 0.125rem
  space-xs: 0.25rem
  space-sm: 0.5rem
  space-md: 0.75rem
  space-base: 1rem
  space-lg: 1.25rem
  space-xl: 1.5rem
  space-2xl: 2rem
  space-3xl: 3rem
  space-4xl: 4rem
  gutter-mobile: 1rem
  gutter-tablet: 1.5rem
  gutter-desktop: 2rem
  sidebar-width: 17.5rem
  max-content-width: 90rem
---

## Brand & Style

This design system delivers a disciplined, modern analytical environment tailored for machine learning, statistical modeling, and data science research. Crafted for students, researchers, and data professionals, the interface favors cognitive clarity, reproducibility, and high-density information architecture over decorative trends. 

The aesthetic adheres to **Corporate Modern / Analytical Minimalism**:
- **Palette Logic:** A dark, light-absorbent slate substrate that mitigates visual fatigue during long analytical sessions, contrasted by sharp, functional electric cyan accents that direct user attention strictly to active models, inputs, and regression curves.
- **Academic Precision:** Rejects noisy multi-colored gradients, extraneous skeuomorphism, and heavy frosted glassmorphism in favor of structured data layouts, crisp 1px borders, and deliberate typographic rhythm.
- **Data Centricity:** Prioritizes chart legibility, monospaced tabular data integrity, and direct metric scanning to instill immediate trust in predicted regression outputs.

## Colors

The color palette establishes a deep contrast hierarchy built around a calibrated slate matrix and functional semantic accents.

### Core Architecture
- **Primary (`#38BDF8` - Electric Cyan):** The primary focus accent. Used for high-impact interactive controls, optimal regression fit lines, active states, and key trendline data points.
- **Secondary (`#6366F1` - Indigo):** Secondary predictor variables, multi-variable polynomial comparison paths, and secondary feature weight indicators.
- **Tertiary (`#A855F7` - Violet):** Baseline reference markers, confidence intervals, and secondary statistical metrics.
- **Neutral Surface Matrix:**
  - `Surface Base`: `#0F172A` (Deep Slate Canvas)
  - `Surface Layer 1`: `#1E293B` (Cards, sidebars, panel containers)
  - `Surface Layer 2`: `#334155` (Hover states, input backgrounds, active borders)
  - `Border Subtle`: `#1E293B`
  - `Border Muted`: `#334155`
  - `Border Focus`: `#38BDF8`

### Typography & Hierarchy
- **Text High-Contrast:** `#F8FAFC` (98% contrast for core metrics, regression formulas, and key headlines)
- **Text Secondary:** `#94A3B8` (Labels, metadata, axis ticks, table column headers)
- **Text Tertiary:** `#64748B` (Inactive states, helper text, chart grid notations)

### Semantic & Data Visualization Tokens
- **Positive / Fit Increase:** `#34D399` (Emerald 400)
- **Warning / Outlier Alert:** `#FBBF24` (Amber 400)
- **Negative / Error Loss:** `#F87171` (Rose 400)
- **Scatter Plot Residual Points:** `#38BDF8` with 20% opacity fills and 100% opacity 1.5px borders.

## Typography

The typography system is built entirely on `Inter`, leveraging its OpenType tabular figure features (`tnum`, `cv05`, `cv08`) to ensure all scalar coordinates, loss values, coefficient matrices, and regression metrics maintain strict vertical alignment across rows and tables.

- **Numerics & Monospace Behavior:** All values displayed in predictive tables, summary metric cards, axis scales, and coefficients must activate OpenType tabular numbers: `font-feature-settings: "tnum" 1, "cv05" 1`.
- **Vertical Rhythm:** Strict, compact line heights prevent excessive scrolling in multidimensional data views while maintaining optical breathing room.
- **Hierarchy Enforcement:** Display and headline levels are reserved strictly for dataset metadata, primary dashboard headings, and top-level scenario summaries. Metric sizes (`data-metric-lg` and `data-metric-sm`) bypass typical body hierarchies to surface raw predictive outputs instantly.

## Layout & Spacing

The layout architecture relies on a responsive 12-column analytical grid with fixed lateral controls and fluid visualization stages:

### Grid Architecture
- **Desktop (1200px+):** 12-column grid, 24px gutters, fixed `17.5rem` parameter control sidebar on the left, main visualization and performance summary canvas spanning the remaining fluid container up to a max width of `90rem`.
- **Tablet (768px - 1199px):** 8-column layout, 20px gutters. Parameter inputs collapse into an expandable top tray; regression charts maintain full horizontal span.
- **Mobile (< 768px):** 4-column layout, 16px gutters. Scatter plots stack vertically above evaluation metrics. Sliders and numeric model inputs format into stacked touch controls.

### Density and Cadence
- **Dense Data Zones:** Chart control toolbars, data matrices, and model parameter inputs use tight 4px and 8px gaps (`space-xs` and `space-sm`) to support fast comparative adjustments.
- **Structural Separation:** Canvas panels and metric card clusters use 16px to 24px intervals (`space-base` to `space-xl`) to clearly delineate experimental runs without visual clutter.

## Elevation & Depth

The design system intentionally rejects heavy, blurred drop shadows and glossy overlays. Depth is communicated strictly via **tonal layering**, **1px crisp border framing**, and **surface luminary hierarchy**:

1. **Base Layer (`#0F172A`):** The master canvas level. Charts, coordinate grids, and table backdrops rest here.
2. **Elevated Surface Layer (`#1E293B`):** Metric panels, control trays, and floating summary sidebars. Outlined with a subtle, non-distracting stroke of `1px solid #334155`.
3. **Interactive Surface Layer (`#334155`):** Inputs, dropdown toggles, active tab selectors, and hovered data rows.
4. **Overlay / Popover Layer (`#1E293B`):** Hover inspection tooltips for chart data nodes and dropdown menus. Uses a precise, low-spread ambient occlusion shadow: `0 4px 20px -2px rgba(0, 0, 0, 0.45)`, enclosed within a `1px solid #38BDF8` border (20% opacity).

## Shapes

The design system implements a controlled, soft corner philosophy (`roundedness: 1`). Radii are kept small and architectural to preserve an engineering-grade, scientific feel:

- **Interactive Elements (Buttons, Inputs, Selectors):** `0.25rem` (`rounded`, 4px). Delivers a crisp, precise mechanical boundary.
- **Panels & Containers:** `0.5rem` (`rounded-lg`, 8px). Creates visual cohesion across model containers, scatter plot panels, and data tables.
- **Badges, Status Tags & Data Tooltips:** `0.25rem` (4px). Avoids stadium/pill shapes to maintain an analytical tone.
- **Scatter Plot Nodes:** Pure geometric circles (diameter 6px default, 10px active/inspected).

## Components

### Buttons
- **Primary (Model Run / Fit):** Solid `#38BDF8` fill with `#0F172A` bold Inter text. On hover, background shifts to `#7DD3FC`. Active state scales subtly (`scale-98`). Focus outline: 2px offset cyan border.
- **Secondary (Parameter Reset / Export):** `#1E293B` surface, `1px solid #334155` border, `#F8FAFC` text. Hover changes border to `#64748B` and surface to `#334155`.
- **Tertiary / Ghost (Table Action / Formula View):** Transparent background, `#94A3B8` text. Hover applies `#1E293B` background and `#38BDF8` text.

### Input Fields & Steppers
- **Numeric & Advertising Budget Inputs (TV, Radio, Social):** Background `#0F172A`, border `1px solid #334155`, text `#F8FAFC` in tabular format. Left-aligned currency/unit indicator in `#64748B`. Focus transitions border to `#38BDF8` without glowing halos.
- **Hyperparameter Sliders:** Base track `4px` height in `#1E293B`. Active filled track in `#38BDF8`. Thumb is a sharp `16px` circle in `#38BDF8` with a `2px solid #0F172A` ring.

### Cards & Analytical Panels
- Background `#1E293B`, rounded `0.5rem`, border `1px solid #334155`.
- **Metric Card Sub-elements:** Upper-case label in `#94A3B8` (`label-md`), primary statistical value in `#F8FAFC` (`data-metric-lg`), sub-metric indicator displaying variance or delta in either `#34D399` (positive) or `#F87171` (negative).

### Data Tables
- Header row with `#0F172A` sticky surface, `#94A3B8` uppercase labels (`0.75rem`), bottom border `1px solid #334155`.
- Table body cells: `#F8FAFC` tabular text, alternating row striping with `#0F172A` and `#1E293B` at 40% opacity. Hover row highlights with a `1px solid #38BDF8` inset stroke.

### Checkboxes, Radio Buttons & Model Selectors
- **Checkbox/Radio:** Base `16px` square or circle, background `#0F172A`, border `1px solid #475569`. Selected state displays `#38BDF8` fill with `#0F172A` icon checkmark.
- **Polynomial Degree Segmented Control:** Segment group in `#0F172A` with `1px solid #334155` enclosure. Selected segment transitions to `#334155` with `#38BDF8` text and a discrete bottom indicator line.

### Data Visualization Components (Scatter Plots & Curves)
- **Grid Lines:** `1px dashed #334155` at 50% opacity over `#0F172A` chart backdrop.
- **Data Points (Scatter):** `6px` circles, fill `#38BDF8` at 25% opacity, stroke `1.5px solid #38BDF8`. Hover state scales node to `8px`, opacity to 100%, and displays tooltip with tabular coordinates $(X_i, Y_i)$.
- **Polynomial / Linear Fit Curve:** Smooth SVG vector path, `2.5px` stroke weight in `#38BDF8` (primary model) or `#6366F1` (baseline/comparison model). No glow; crisp antialiased rendering.
- **Confidence Interval Band:** Polygon fill with `#38BDF8` at 10% opacity, bounded by `1px dashed #38BDF8` (30% opacity).