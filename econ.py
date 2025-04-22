import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import graphviz

st.set_page_config(page_title="Economics Study Notes", layout="wide")

# 🌞 Force light mode styles because streamlit emotions specificity is stupid
st.markdown("""
<style>
/* Force light theme for everything */
html, body, .stApp, .main, .block-container, [data-testid="stMarkdownContainer"] {
    background-color: #ffffff !important;
    color: #000000 !important;
}

/* Fix links */
a, a:visited {
    color: #1f618d !important;
}

/* Force TOC & content box style */
.toc, .content-box, div[style*="background-color"] {
    background-color: #ffffff !important;
    color: #000000 !important;
    border: none !important;
}

/* Reset headings */
h1, h2, h3, h4, h5, h6, strong {
    color: #111111 !important;
}

/* Reset all elements */
*, *::before, *::after {
    box-shadow: none !important;
    border-color: #ccc !important;
    background-image: none !important;
}
</style>
""", unsafe_allow_html=True)

# === HTML LECTURE NOTES ===
with open("Econ_Lecture_Notes_Final.html", "r", encoding="utf-8") as f:
    html_content = f.read()

st.markdown("## 📘 Lecture Notes", unsafe_allow_html=True)
st.markdown(html_content, unsafe_allow_html=True)

# === GENERATED VISUALS ===
st.markdown("---")
st.markdown("## 📊 Graphs and Charts")

# --- 1. Economic Concepts (Descriptive Chart) ---
st.markdown("### Economic Concepts: Scarcity, Choice, and Marginal Analysis")
st.markdown("These concepts form the foundation of economic decision-making. They explain why choices must be made and how individuals and firms weigh costs and benefits.")
fig1, ax1 = plt.subplots(figsize=(6, 3.5))
ax1.axis("off")
concepts = [
    ("Scarcity", "Resources are limited"),
    ("Choice", "Because of scarcity, choices must be made"),
    ("Opportunity Cost", "Choosing one thing means giving up another"),
    ("Purposeful Behavior", "Individuals & firms act to maximize utility or profit"),
    ("Marginal Analysis", "Decisions are made by comparing extra benefit vs extra cost")
]
y = 1.0
for title, description in concepts:
    ax1.text(0.05, y, f"• {title}: {description}", fontsize=10.5, va="top", ha="left", transform=ax1.transAxes)
    y -= 0.15
plt.title("Economic Concepts: Scarcity, Choice, and Marginal Analysis", fontsize=12, weight="bold")
st.markdown("<div style='max-width: 600px;'>", unsafe_allow_html=True)
st.pyplot(fig1)
st.markdown("</div>", unsafe_allow_html=True)

# --- 2. The Consumer's Budget Line ---
# this is the table
st.markdown("### Budget Line Table")
st.markdown("This table shows all combinations of movies and books that can be purchased with $120.")
budget_data = {
    "Units of Movies ($20 each)": [6, 5, 4, 3, 2, 1, 0],
    "Units of Books ($10 each)": [0, 2, 4, 6, 8, 10, 12],
    "Total Expenditure": ["$120"] * 7
}
budget_df = pd.DataFrame(budget_data)
st.dataframe(budget_df, use_container_width=True)

# this is the graph
st.markdown("### The Consumer’s Budget Line")
st.markdown("This graph shows all combinations of books and movies a consumer can afford with a fixed budget, illustrating trade-offs between two goods.")
books = [0, 2, 4, 6, 8, 10, 12]
movies = [6, 5, 4, 3, 2, 1, 0]
fig2 = plt.figure(figsize=(5.5, 3.5))
plt.plot(books, movies, marker='o', linestyle='-', color='teal')
plt.title("The Consumer’s Budget Line")
plt.xlabel("Books")
plt.ylabel("Movies")
plt.grid(True)
st.markdown("<div style='max-width: 600px;'>", unsafe_allow_html=True)
st.pyplot(fig2)
st.markdown("</div>", unsafe_allow_html=True)

# --- 3. Production Possibilities Curve ---
st.markdown("### Production Possibilities Curve (PPC)")
st.markdown("The PPC illustrates the maximum potential output combinations of two goods that an economy can produce using all resources efficiently.")
consumer_goods = [0, 4, 7, 9, 10]
capital_goods = [10, 9, 7, 4, 0]
fig3 = plt.figure(figsize=(5.5, 3.5))
plt.plot(consumer_goods, capital_goods, marker='o', linestyle='-', color='purple')
plt.title("Production Possibilities Curve (PPC)")
plt.xlabel("Consumer Goods")
plt.ylabel("Capital Goods")
plt.grid(True)
st.markdown("<div style='max-width: 600px;'>", unsafe_allow_html=True)
st.pyplot(fig3)
st.markdown("</div>", unsafe_allow_html=True)

# --- 4. Trade-Off Table ---
st.markdown("### Trade-Off Combinations Table")
st.markdown("This table displays production possibilities showing how producing more of one good requires sacrificing the other.")
data = {
    "Combination": ["A", "B", "C", "D", "E", "F"],
    "Consumer Goods": [15, 14, 12, 9, 5, 0],
    "Capital Goods": [0, 1, 2, 3, 4, 5]
}
df = pd.DataFrame(data)
st.dataframe(df)

# --- 5. Shifts in the PPC ---
st.markdown("### Shifts in the Production Possibilities Curve")
st.markdown("This graph shows how the PPC can shift outward due to growth or inward due to decline in resources, technology, or labor force.")
consumer_goods_growth = [0, 5, 9, 12, 14]
capital_goods_growth = [12, 11, 9, 6, 0]
consumer_goods_decline = [0, 3, 5, 6, 7]
capital_goods_decline = [8, 7, 5, 3, 0]
fig5 = plt.figure(figsize=(5.5, 3.5))
plt.plot(consumer_goods, capital_goods, label="Original PPC", linestyle='--', marker='o')
plt.plot(consumer_goods_growth, capital_goods_growth, label="Outward Shift (Growth)", linestyle='-', marker='o')
plt.plot(consumer_goods_decline, capital_goods_decline, label="Inward Shift (Decline)", linestyle='-', marker='x')
plt.title("Shifts in the Production Possibilities Curve")
plt.xlabel("Consumer Goods")
plt.ylabel("Capital Goods")
plt.legend()
plt.grid(True)
st.markdown("<div style='max-width: 600px;'>", unsafe_allow_html=True)
st.pyplot(fig5)
st.markdown("</div>", unsafe_allow_html=True)

# --- 6. Global Perspective Chart ---
st.markdown("### Global Perspective: Average Income by Country")
st.markdown("This chart compares average income across several countries to highlight global budget constraints.")
income_data = {
    "Country": [
        "Norway", "Sweden", "United States", "Singapore", "France", "South Korea",
        "Mexico", "China", "Iraq", "India", "Madagascar", "Malawi"
    ],
    "Income (USD, 2014)": [
        103630, 61610, 55200, 55150, 42960, 27090,
        9870, 7400, 6500, 1570, 440, 250
    ]
}
income_df = pd.DataFrame(income_data)
fig6 = plt.figure(figsize=(6, 4))
bars = plt.barh(income_df["Country"], income_df["Income (USD, 2014)"], color='skyblue')
plt.xlabel("Per Capita Income (USD)")
plt.title("Average Income, Selected Nations (2014)")
plt.gca().invert_yaxis()
plt.tight_layout()
for bar in bars:
    width = bar.get_width()
    plt.text(width + 1000, bar.get_y() + bar.get_height() / 2, f"${width:,.0f}", va='center')
st.markdown("<div style='max-width: 600px;'>", unsafe_allow_html=True)
st.pyplot(fig6)
st.markdown("</div>", unsafe_allow_html=True)

# circular flow
st.markdown("### The Circular Flow Diagram")

diagram = graphviz.Digraph(engine="neato")

# Node positions to form a diamond shape
diagram.node("Households", pos="0,1!", shape="box", style="filled", fillcolor="#1f77b4", fontcolor="white")
diagram.node("Resource Market", pos="1,2!", shape="box", style="filled", fillcolor="#d62728", fontcolor="white")
diagram.node("Businesses", pos="2,1!", shape="box", style="filled", fillcolor="#1f77b4", fontcolor="white")
diagram.node("Product Market", pos="1,0!", shape="box", style="filled", fillcolor="#d62728", fontcolor="white")

# Arrows for real and money flows (counterclockwise and clockwise)
diagram.edge("Households", "Resource Market", label="Sell Resources")
diagram.edge("Resource Market", "Businesses", label="Buy Resources")
diagram.edge("Businesses", "Product Market", label="Sell Goods")
diagram.edge("Product Market", "Households", label="Buy Goods")

# Opposite money flows (clockwise)
diagram.edge("Businesses", "Resource Market", label="Costs (Wages, Rent, Interest)", style="dashed")
diagram.edge("Resource Market", "Households", label="Income", style="dashed")
diagram.edge("Households", "Product Market", label="Consumption Expenditures", style="dashed")
diagram.edge("Product Market", "Businesses", label="Revenue", style="dashed")

st.graphviz_chart(diagram)

# --- 7. The Demand Curve ---
st.markdown("### The Demand Curve")
st.markdown("This chart shows the inverse relationship between the price of corn and the quantity demanded.")

# Create two columns
col1, col2 = st.columns(2)

# Column 1: Demand Table
with col1:
    st.markdown("#### 📋 Demand Table")
    demand_data = {
        "Price per Bushel ($)": [5, 4, 3, 2, 1],
        "Quantity Demanded per Week": [10, 20, 35, 55, 80]
    }
    demand_df = pd.DataFrame(demand_data)
    st.dataframe(demand_df, use_container_width=True)

# Column 2: Demand Curve Graph
with col2:
    st.markdown("#### 📈 Demand Curve")
    price = [5, 4, 3, 2, 1]
    quantity = [10, 20, 35, 55, 80]

    fig7 = plt.figure(figsize=(5, 3.5))
    plt.plot(quantity, price, marker='o', color='green')
    plt.title("Demand Curve for Corn")
    plt.xlabel("Quantity Demanded (bushels/week)")
    plt.ylabel("Price per Bushel ($)")
    plt.grid(True)
    plt.xlim(0, 90)
    plt.ylim(0, 6)
    st.pyplot(fig7)

# --- 8. Market Demand Table ---
st.markdown("### Market Demand for Corn (Three Buyers)")
st.markdown("This table aggregates the quantity of corn demanded by Joe, Jen, and Jay at various price levels.")

market_demand_data = {
    "Price per Bushel ($)": [5, 4, 3, 2, 1],
    "Joe": [10, 20, 35, 55, 80],
    "Jen": [12, 23, 39, 60, 87],
    "Jay": [8, 17, 26, 39, 54],
    "Total Quantity Demanded": [30, 60, 100, 154, 221]
}
market_demand_df = pd.DataFrame(market_demand_data)
st.dataframe(market_demand_df, use_container_width=True)

# --- 9. Changes in Demand ---
st.markdown("### Changes in Demand")
st.markdown("The following table and chart show how the demand curve shifts due to factors other than price, such as preferences, population, or income.")

col1, col2 = st.columns([1, 2])

# Table
with col1:
    st.markdown("#### Market Demand for Corn (200 Buyers, D₁)")
    changes_demand_data = {
        "Price per Bushel ($)": [5, 4, 3, 2, 1],
        "Quantity Demanded (per week)": [2000, 4000, 7000, 11000, 16000]
    }
    changes_df = pd.DataFrame(changes_demand_data)
    st.dataframe(changes_df, use_container_width=True)

# Chart
with col2:
    demand_d1 = [2000, 4000, 7000, 11000, 16000]
    prices = [5, 4, 3, 2, 1]
    demand_d2 = [q + 3000 for q in demand_d1]
    demand_d3 = [q - 2000 for q in demand_d1]

    fig9 = plt.figure(figsize=(6, 4))
    plt.plot([q/1000 for q in demand_d1], prices, label="D₁", marker='o', color="green")
    plt.plot([q/1000 for q in demand_d2], prices, label="D₂ (↑ Demand)", linestyle='--', marker='o')
    plt.plot([q/1000 for q in demand_d3], prices, label="D₃ (↓ Demand)", linestyle='--', marker='x')
    plt.xlabel("Quantity Demanded (Thousands of Bushels)")
    plt.ylabel("Price per Bushel ($)")
    plt.title("Shifts in the Demand Curve")
    plt.grid(True)
    plt.legend()
    st.pyplot(fig9)

# --- 10. Determinants of Demand (HTML for better formatting) ---
st.markdown("### Determinants of Demand")
st.markdown("These factors shift the entire demand curve, affecting consumer purchasing behavior regardless of price.")

st.markdown("""
<style>
    .demand-table {
        border-collapse: collapse;
        width: 100%;
    }
    .demand-table th, .demand-table td {
        border: 1px solid #ddd;
        padding: 12px;
        text-align: left;
        vertical-align: top;
    }
    .demand-table th {
        background-color: #f2f2f2;
        font-weight: bold;
    }
    .demand-table td {
        background-color: #ffffff;
        word-wrap: break-word;
        max-width: 600px;
    }
</style>

<table class="demand-table">
    <tr>
        <th>Determinant</th>
        <th>Examples</th>
    </tr>
    <tr>
        <td>Change in buyers’ tastes</td>
        <td>Physical fitness rises in popularity, increasing the demand for jogging shoes and bicycles; cell phone popularity rises, reducing the demand for landline phones.</td>
    </tr>
    <tr>
        <td>Change in the number of buyers</td>
        <td>A decline in the birthrate reduces the demand for children’s toys.</td>
    </tr>
    <tr>
        <td>Change in income</td>
        <td>A rise in incomes increases the demand for normal goods (e.g., restaurant meals) while reducing demand for inferior goods (e.g., cabbage, turnips).</td>
    </tr>
    <tr>
        <td>Change in the prices of related goods</td>
        <td>A reduction in airfares reduces the demand for bus transportation (substitute goods); a drop in DVD player prices increases demand for DVD movies (complementary goods).</td>
    </tr>
    <tr>
        <td>Change in consumer expectations</td>
        <td>Bad weather in South America leads to expectations of higher future coffee prices, increasing demand today.</td>
    </tr>
</table>
""", unsafe_allow_html=True)

import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

# --- supply curve ---
supply_data = {
    "Price per Bushel": ["$5", "4", "3", "2", "1"],
    "Quantity Supplied per Week": [60, 50, 35, 20, 5]
}
supply_df = pd.DataFrame(supply_data)

# --- Layout ---
col1, col2 = st.columns([1, 2])

with col1:
    st.markdown("### Supply of Corn")
    st.dataframe(supply_df, use_container_width=True)

with col2:
    st.markdown("### The Supply Curve")
    price = [5, 4, 3, 2, 1]
    quantity = [60, 50, 35, 20, 5]
    fig, ax = plt.subplots(figsize=(5.5, 3.5))
    ax.plot(quantity, price, marker='o', color='crimson', linewidth=2)
    ax.set_title("Supply Curve of Corn")
    ax.set_xlabel("Quantity Supplied (bushels per week)")
    ax.set_ylabel("Price (per bushel)")
    ax.grid(True)
    st.pyplot(fig)

st.markdown("### Determinants of Supply: Factors That Shift the Supply Curve", unsafe_allow_html=True)

supply_table_html = """
<table style="width:100%; border-collapse: collapse; font-family: Arial, sans-serif; font-size: 15px;">
  <thead style="background-color: #d9ead3;">
    <tr>
      <th style="border: 1px solid #999; padding: 10px; text-align: left;">Determinant</th>
      <th style="border: 1px solid #999; padding: 10px; text-align: left;">Examples</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border: 1px solid #ccc; padding: 10px;">Change in resource prices</td>
      <td style="border: 1px solid #ccc; padding: 10px;">A decrease in the price of microchips increases the supply of computers; an increase in the price of crude oil reduces the supply of gasoline.</td>
    </tr>
    <tr>
      <td style="border: 1px solid #ccc; padding: 10px;">Change in technology</td>
      <td style="border: 1px solid #ccc; padding: 10px;">The development of more effective wireless technology increases the supply of cell phones.</td>
    </tr>
    <tr>
      <td style="border: 1px solid #ccc; padding: 10px;">Change in taxes and subsidies</td>
      <td style="border: 1px solid #ccc; padding: 10px;">An increase in the excise tax on cigarettes reduces the supply of cigarettes; a decline in subsidies to state universities reduces the supply of higher education.</td>
    </tr>
    <tr>
      <td style="border: 1px solid #ccc; padding: 10px;">Change in prices of other goods</td>
      <td style="border: 1px solid #ccc; padding: 10px;">An increase in the price of cucumbers decreases the supply of watermelons.</td>
    </tr>
    <tr>
      <td style="border: 1px solid #ccc; padding: 10px;">Change in producer expectations</td>
      <td style="border: 1px solid #ccc; padding: 10px;">An expectation of a substantial rise in future log prices decreases the supply of logs today.</td>
    </tr>
    <tr>
      <td style="border: 1px solid #ccc; padding: 10px;">Change in the number of suppliers</td>
      <td style="border: 1px solid #ccc; padding: 10px;">An increase in the number of tattoo parlors increases the supply of tattoos; the formation of women’s professional basketball leagues increases the supply of women’s professional basketball games.</td>
    </tr>
  </tbody>
</table>
"""

st.markdown(supply_table_html, unsafe_allow_html=True)

import streamlit as st
import matplotlib.pyplot as plt

# --- 7. Changes in Demand and Equilibrium ---
# External image URL for "Changes in Demand and Equilibrium"

st.markdown("### Changes in Demand and Equilibrium")

# Two-column label section
col1, col2 = st.columns(2)
with col1:
    st.markdown(
        """
        <div style="border: 1px solid #2c3e50; padding: 8px; display: inline-block;">
            <strong>D increase:</strong><br>P↑, Q↑
        </div>
        """,
        unsafe_allow_html=True
    )
with col2:
    st.markdown(
        """
        <div style="border: 1px solid #2c3e50; padding: 8px; display: inline-block;">
            <strong>D decrease:</strong><br>P↓, Q↓
        </div>
        """,
        unsafe_allow_html=True
    )

image_url = "http://www.econport.org/content/handbook/Equilibrium/shifts-graph/mainColumnParagraphs/0/content_files/file0/market_equilibrium_g34.gif"


st.image(image_url, caption="Source: EconPort", use_column_width=True)

# --- changes in supply
st.markdown("### Changes in Supply and Equilibrium")

# Two-column label section
col1, col2 = st.columns(2)
with col1:
    st.markdown(
        """
        <div style="border: 1px solid #2c3e50; padding: 8px; display: inline-block;">
            <strong>S increase:</strong><br>P↓, Q↑
        </div>
        """,
        unsafe_allow_html=True
    )
with col2:
    st.markdown(
        """
        <div style="border: 1px solid #2c3e50; padding: 8px; display: inline-block;">
            <strong>S decrease:</strong><br>P↑, Q↓
        </div>
        """,
        unsafe_allow_html=True
    )

# Image from online source
supply_image_url = "http://www.econport.org/content/handbook/Equilibrium/shifts-graph/mainColumnParagraphs/0/content_files/file2/market_equilibrium_g12.gif"
st.image(supply_image_url, caption="Source: EconPort", use_column_width=True)

st.markdown("### Complex Cases: Combined Supply and Demand Changes")
st.markdown("This table summarizes how simultaneous changes in supply and demand affect equilibrium price and quantity.")

#--- complex cases

complex_cases_data = {
    "Change in Supply": ["Increase", "Decrease", "Increase", "Decrease"],
    "Change in Demand": ["Decrease", "Increase", "Increase", "Decrease"],
    "Effect on Equilibrium Price": ["Decrease", "Increase", "Indeterminate", "Indeterminate"],
    "Effect on Equilibrium Quantity": ["Indeterminate", "Indeterminate", "Increase", "Decrease"]
}

complex_cases_df = pd.DataFrame(complex_cases_data, index=[1, 2, 3, 4])
st.dataframe(complex_cases_df, use_container_width=True)

#--- ceiling
st.markdown("### Price Ceiling")
st.image("https://cdn.kastatic.org/ka-perseus-images/01cfdf0fcf4813d17847438b6f38277734cc7534.jpg", caption="Price Ceiling")

# price floor
st.markdown("### Price Floor")
st.image("https://cdn.kastatic.org/ka-perseus-images/5f8d450d1e4ef5a26b1e9c61bacc09ce47581d12.jpg", caption="Price Floor")




