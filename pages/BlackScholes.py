import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Function to calculate d1 and d2
def d1_d2(S, E, T, rf, sigma):
    d1 = (np.log(S / E) + (rf + sigma ** 2 / 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    return d1, d2

# Function to calculate call option price
def call_option_price(S, E, T, rf, sigma):
    d1, d2 = d1_d2(S, E, T, rf, sigma)
    return S * stats.norm.cdf(d1) - E * np.exp(-rf * T) * stats.norm.cdf(d2)

# Function to calculate put option price
def put_option_price(S, E, T, rf, sigma):
    d1, d2 = d1_d2(S, E, T, rf, sigma)
    return E * np.exp(-rf * T) * stats.norm.cdf(-d2) - S * stats.norm.cdf(-d1)

st.title("Black-Scholes Option Pricing Model")

# Inputs
st.sidebar.header("Option Pricing Parameters")
S = st.sidebar.number_input("Current Asset Price", value=100.0)
E = st.sidebar.number_input("Strike Price", value=100.0)
T = st.sidebar.number_input("Time to Maturity (Years)", value=1.0)
sigma = st.sidebar.number_input("Volatility (σ)", value=0.2)
rf = st.sidebar.number_input("Risk-Free Interest Rate", value=0.05)

# Calculate prices
call_price = call_option_price(S, E, T, rf, sigma)
put_price = put_option_price(S, E, T, rf, sigma)

# Display prices
st.markdown("### Option Prices")
col1, col2 = st.columns(2)
with col1:
    st.markdown("#### Call Option Price")
    st.success(f"${call_price:.2f}")
with col2:
    st.markdown("#### Put Option Price")
    st.error(f"${put_price:.2f}")

# Heatmap
st.sidebar.header("Heatmap Parameters")
min_spot = st.sidebar.number_input("Min Spot Price", value=50.0)
max_spot = st.sidebar.number_input("Max Spot Price", value=70.0)
min_vol = st.sidebar.slider("Min Volatility", min_value=0.01, max_value=1.0, value=0.1)
max_vol = st.sidebar.slider("Max Volatility", min_value=0.01, max_value=1.0, value=0.3)

spot_prices = np.arange(min_spot, max_spot + 5, 5)
volatilities = np.arange(min_vol, max_vol + 0.02, 0.02)

call_prices = np.array([[call_option_price(s, E, T, rf, v) for s in spot_prices] for v in volatilities])
put_prices = np.array([[put_option_price(s, E, T, rf, v) for s in spot_prices] for v in volatilities])

st.markdown("### Heatmap of Option Prices")
fig, ax = plt.subplots(1, 2, figsize=(16, 8))
sns.heatmap(call_prices, xticklabels=np.round(spot_prices, 2), yticklabels=np.round(volatilities, 2), ax=ax[0], cmap="coolwarm", annot=True)
ax[0].set_title("Call Option Prices")
ax[0].set_xlabel("Spot Price")
ax[0].set_ylabel("Volatility")
sns.heatmap(put_prices, xticklabels=np.round(spot_prices, 2), yticklabels=np.round(volatilities, 2), ax=ax[1], cmap="viridis", annot=True)
ax[1].set_title("Put Option Prices")
ax[1].set_xlabel("Spot Price")
ax[1].set_ylabel("Volatility")
st.pyplot(fig)
