import streamlit as st

st.set_page_config(page_title="Option Pricing Model", page_icon="📈")

st.title("Option Pricing Model App")
st.write("""
Welcome to the Option Pricing Model App. Navigate through the pages using the sidebar to calculate option prices using the Black-Scholes model or to determine implied volatility.
""")

# Personal Information
st.markdown("---")
st.markdown("### Built by")
linkedin_url = "https://www.linkedin.com/in/subham-thirani-0aba8b157/"
st.markdown(f"[![LinkedIn](https://img.shields.io/badge/LinkedIn-Subham%20Thirani-blue)]({linkedin_url})")
st.markdown("""
Passionate software engineer with a focus on quantitative finance & trading, leveraging cutting-edge technologies & self-learned quant skills to solve complex problems. Enthusiastic about innovation, continuous learning, and practical applications in the finance industry.
""")

st.markdown("---")
st.markdown("### Contact Me")
st.write("""
Feel free to reach out to me for any queries or potential collaboration opportunities:
- **Email:** subham.thirani@gmail.com
- **LinkedIn:** [Subham Thirani](https://www.linkedin.com/in/subham-thirani-0aba8b157/)
""")
