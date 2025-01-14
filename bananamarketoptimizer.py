import streamlit as st
import numpy as np
from itertools import product
import base64

st.set_page_config(page_title="Cavendish Banana Market Optimizer", layout="wide")

with open('style_bananamarketoptimizer.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

@st.cache_data
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

img = get_img_as_base64("bananatree1.jpg")

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
    background-image: url("data:image/png;base64,{img}");
    background-size: cover;
    background-position: center center;
    background-repeat: no-repeat;
    height: 100vh;
}}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center'>Cavendish Banana Market Optimizer</h1>", unsafe_allow_html=True)
st.write("---")

total_percentbanana = 0
total_percentflour = 0
conversion_factor = 0.50
total_cost = 0

with st.expander("Cavendish Banana Farm General Information"):
    col1, col2, col3 = st.columns(3)
    with col1:
        total_banana = st.number_input("Total amount of banana harvested in kilograms:", min_value=0.00, step=1.0)
        bunch = st.number_input("Number of banana bunch harvested:", min_value=0.00, step=1.0)
    with col2:
        type_of_banana_sell = st.radio("Please select the type of banana you would sell:", ("Banana", "Banana and Banana Flour"))
    with col3:
        dataset = st.radio("Please select the dataset to use for the computation:", ("Sto. Tomas, Davao del Norte - CHED 2017", "Sto. Tomas, Davao del Norte - World Bank 2012"))

maincol1, maincol2 = st.columns(2)
with maincol1:            
    if type_of_banana_sell == "Banana":
        regular_laborers = 0
        regular_days = 0
        regular_laborers_day = 0
        nonregular_laborers_wash = 0
        nonregular_laborers_peel = 0
        nonregular_kilos_wash = 0
        nonregular_kilos_peel = 0
        number_mills = 0
        cost_per_mill = 0
        setup_cost = 0
        other_operational_costs = 0
        st.header("Market Allocations")
        tab1, tab2 = st.tabs(["Contractual Market", "Spot Market"])
        percent_bananaflourmarket = 0
    
        with tab1:
            st.subheader("Contractual Market")
            contractualmarket_yesno = st.radio("Will you allocate bananas to Contractual Market:", ("Yes", "No"))
            if contractualmarket_yesno == "Yes":
                percent_contractualmarket = st.number_input("How many percentage of Cavendish banana will you allocate to Contractual Market?", min_value=0.00, step=1.0)
                price_contractualmarket = st.number_input("How much is the price of Cavendish banana when sold to Contractual Market per kilo?", min_value=0.00, step=1.0)
    
        with tab2:
            st.subheader("Spot Market")
            spotmarket_yesno = st.radio("Will you allocate bananas to Spot Market:", ("Yes", "No"))
            if spotmarket_yesno == "Yes":
                percent_spotmarket = st.number_input("How many percentage of Cavendish banana will you allocate to the Spot Market?", min_value=0.00, step=1.0)
                price_spotmarket = st.number_input("How much is the price of Cavendish banana when sold to the Spot Market per kilo?", min_value=0.00, step=1.0)
                
    elif type_of_banana_sell == "Banana and Banana Flour":
        st.header("Market Allocations")
        tab1, tab2, tab3 = st.tabs(["Contractual Market", "Spot Market", "Banana Flour Market"])
    
        with tab1:
            st.subheader("Contractual Market")
            contractualmarket_yesno = st.radio("Will you allocate bananas to Contractual Market:", ("Yes", "No"))
            if contractualmarket_yesno == "Yes":
                percent_contractualmarket = st.number_input("How many percentage of Cavendish banana will you allocate to Contractual Market?", min_value=0.00, step=1.0)
                price_contractualmarket = st.number_input("How much is the price of Cavendish banana when sold to Contractual Market per kilo?", min_value=0.00, step=1.0)
    
        with tab2:
            st.subheader("Spot Market")
            spotmarket_yesno = st.radio("Will you allocate bananas to Spot Market:", ("Yes", "No"))
            if spotmarket_yesno == "Yes":
                percent_spotmarket = st.number_input("How many percentage of Cavendish banana will you allocate to the Spot Market?", min_value=0.00, step=1.0)
                price_spotmarket = st.number_input("How much is the price of Cavendish banana when sold to the Spot Market per kilo?", min_value=0.00, step=1.0)
    
        with tab3:
            st.subheader("Banana Flour Market")
            bananaflourmarket_yesno = st.radio("Will you allocate bananas for the Banana Flour Market:", ("Yes", "No"))
            if bananaflourmarket_yesno == "Yes":
                percent_bananaflourmarket = st.number_input("How many percentage of Cavendish banana will you allocate to the Banana Flour Market?", min_value=0.00, step=1.0)
                price_bananaflourmarket = st.number_input("How much is the price of banana flour when sold to the Banana Flour Market per kilo?", min_value=0.00, step=1.0)

with maincol2:
    if type_of_banana_sell == "Banana":
        st.header("Costs")
        tab1, tab2, tab3, tab4 = st.tabs(["Input Costs", "Materials Costs", "Labor Costs", "Other Cost"])
        with tab1:
            if dataset == "Sto. Tomas, Davao del Norte - CHED 2017":
                st.subheader("Fertilizer")
                fert_cost_per_sackbag = st.number_input("How much does a sack/bag of Fertilizer cost?", min_value=0.00, step=1.0)
                fert_number_sackbag = st.number_input("How many sacks/bags of Fertilizer did you use per hectare?", min_value=0.00, step=1.0)
                fert_days = st.number_input("How many days in a week did you apply the Fertilizer?", min_value=0.00, max_value=7.00, step=1.0)
                fert_weeks = st.number_input("How many weeks in a month did you apply the Fertilizer?", min_value=0.00, max_value=4.00, step=1.0)
                fert_months = st.number_input("How many months in a year did you apply the Fertilizer?", min_value=0.00, max_value=12.00, step=1.0)
                st.subheader("Sigatoka Control Chemical")
                siga_cost_per_sackbag = st.number_input("How much does a liter of Sigatoka Control Chemical cost?", min_value=0.00, step=1.0)
                siga_number_sackbag = st.number_input("How many liters of Sigatoka Control Chemical did you use per hectare?", min_value=0.00, step=1.0)
                siga_days = st.number_input("How many days in a week did you apply the Sigatoka Control Chemical?", min_value=0.00, max_value=7.00, step=1.0)
                siga_weeks = st.number_input("How many weeks in a month did you apply the Sigatoka Control Chemical?", min_value=0.00, max_value=4.00, step=1.0)
                siga_months = st.number_input("How many months in a year did you apply the Sigatoka Control Chemical?", min_value=0.00, max_value=12.00, step=1.0)
            elif dataset == "Sto. Tomas, Davao del Norte - World Bank 2012":
                st.subheader("Fertilizer")
                fert_cost_per_sackbag = st.number_input("How much does a sack/bag of Fertilizer cost?", min_value=0.00, step=1.0)
                fert_number_sackbag = st.number_input("How many sacks/bags of Fertilizer did you use per hectare?", min_value=0.00, step=1.0)
                fert_days = st.number_input("How many days in a week did you apply the Fertilizer?", min_value=0.00, max_value=7.00, step=1.0)
                fert_weeks = st.number_input("How many weeks in a month did you apply the Fertilizer?", min_value=0.00, max_value=4.00, step=1.0)
                fert_months = st.number_input("How many months in a year did you apply the Fertilizer?", min_value=0.00, max_value=12.00, step=1.0)
                st.subheader("Herbicide")
                h_cost_per_liter = st.number_input("How much does a liter of Herbicide cost?", min_value=0.00, step=1.0)
                h_number_liter = st.number_input("How many liters of Herbicide did you use per hectare?", min_value=0.00, step=1.0)
                h_days = st.number_input("How many days in a week did you apply the Herbicide?", min_value=0.00, max_value=7.00, step=1.0)
                h_weeks = st.number_input("How many weeks in a month did you apply the Herbicide?", min_value=0.00, max_value=4.00, step=1.0)
                h_months = st.number_input("How many months in a year did you apply the Herbicide?", min_value=0.00, max_value=12.00, step=1.0)
                st.subheader("Sigatoka Control Chemical")
                siga_cost_per_sackbag = st.number_input("How much does a liter of Sigatoka Control Chemical cost?", min_value=0.00, step=1.0)
                siga_number_sackbag = st.number_input("How many liters of Sigatoka Control Chemical did you use per hectare?", min_value=0.00, step=1.0)
                siga_days = st.number_input("How many days in a week did you apply the Sigatoka Control Chemical?", min_value=0.00, max_value=7.00, step=1.0)
                siga_weeks = st.number_input("How many weeks in a month did you apply the Sigatoka Control Chemical?", min_value=0.00, max_value=4.00, step=1.0)
                siga_months = st.number_input("How many months in a year did you apply the Sigatoka Control Chemical?", min_value=0.00, max_value=12.00, step=1.0)
                st.subheader("Bud Injection")
                bi_cost_per_liter = st.number_input("How much does a liter of Bud Injection cost?", min_value=0.00, step=1.0)
                bi_number_liter = st.number_input("How many liters of Bud Injection did you use per hectare?", min_value=0.00, step=1.0)
                bi_days = st.number_input("How many days in a week did you apply the Bud Injection?", min_value=0.00, max_value=7.00, step=1.0)
                bi_weeks = st.number_input("How many weeks in a month did you apply the Bud Injection?", min_value=0.00, max_value=4.00, step=1.0)
                bi_months = st.number_input("How many months in a year did you apply the Bud Injection?", min_value=0.00, max_value=12.00, step=1.0)
                st.subheader("Bunch Spray")
                bs_cost_per_liter = st.number_input("How much does a liter of Bunch Spray cost?", min_value=0.00, step=1.0)
                bs_number_liter = st.number_input("How many liters of Bunch Spray did you use per hectare?", min_value=0.00, step=1.0)
                bs_days = st.number_input("How many days in a week did you apply the Bunch Spray?", min_value=0.00, max_value=7.00, step=1.0)
                bs_weeks = st.number_input("How many weeks in a month did you apply the Bunch Spray?", min_value=0.00, max_value=4.00, step=1.0)
                bs_months = st.number_input("How many months in a year did you apply the Bunch Spray?", min_value=0.00, max_value=12.00, step=1.0)

        with tab2:
            st.subheader("Polybags")
            polybags_yesno = st.radio("Did you use polybags?", ("Yes", "No"))
            if polybags_yesno == "Yes":
                polybags_cost_per_kilo = st.number_input("How much does a kilogram of polybags cost?", min_value=0.00, step=1.0)
                polybags_number_kilo = st.number_input("How many kilograms of polybags did you use per hectare?", min_value=0.00, step=1.0)
            st.subheader("Ribbons")
            ribbons_yesno = st.radio("Did you use ribbons?", ("Yes", "No"))
            if ribbons_yesno == "Yes":
                ribbons_cost_per_kilo = st.number_input("How much does a kilogram of ribbons cost?", min_value=0.00, step=1.0)
                ribbons_number_kilo = st.number_input("How many kilograms of ribbons did you use per hectare?", min_value=0.00, step=1.0)
            st.subheader("Twine")
            twine_yesno = st.radio("Did you use twine?", ("Yes", "No"))
            if twine_yesno == "Yes":
                twine_cost_per_kilo = st.number_input("How much does a kilogram of twine cost?", min_value=0.00, step=1.0)
                twine_number_kilo = st.number_input("How many kilograms of twine did you use per hectare?", min_value=0.00, step=1.0)
            st.subheader("Bamboo")
            bamboo_yesno = st.radio("Did you use bamboo?", ("Yes", "No"))
            if bamboo_yesno == "Yes":
                bamboo_cost_per_piece = st.number_input("How much does a piece of bamboo cost?", min_value=0.00, step=1.0)
                bamboo_number_piece = st.number_input("How many pieces of bamboo did you use per hectare?", min_value=0.00, step=1.0)
            st.subheader("Fuel/Oil/Lubricants")
            fol_yesno = st.radio("Did you use Fuel/Oil/Lubricants?", ("Yes", "No"))
            if fol_yesno == "Yes":
                fol_cost_per_piece = st.number_input("How much does a liter of Fuel/Oil/Lubricants cost?", min_value=0.00, step=1.0)
                fol_number_piece = st.number_input("How many liters of Fuel/Oil/Lubricants did you use per hectare?", min_value=0.00, step=1.0)

        with tab3:
            if dataset == "Sto. Tomas, Davao del Norte - CHED 2017":
                st.subheader("Spraying")
                spraying_yesno = st.radio("Did you incur any costs for Spraying?:", ("Yes", "No"))
                if spraying_yesno == "Yes":
                    spraying_laborers = st.number_input("How many laborers did you hire for spraying?", min_value=0.00, step=1.0)
                    spraying_days = st.number_input("How many days in a week do you spray?", min_value=0.00, max_value=7.00, step=1.0)
                    spraying_weeks = st.number_input("How many weeks in a month did you spray?", min_value=0.00, max_value=4.00, step=1.0)
                    spraying_months = st.number_input("How many months in a year did you spray?", min_value=0.00, max_value=12.00, step=1.0)
                st.subheader("Fertilizing")
                fertilizing_yesno = st.radio("Did you incur any costs for Fertilizing?:", ("Yes", "No"))
                if fertilizing_yesno == "Yes":
                    fertilizing_laborers = st.number_input("How many laborers did you hire for fertilizing?", min_value=0.00, step=1.0)
                    fertilizing_days = st.number_input("How many days in a week do you fertilize?", min_value=0.00, max_value=7.00, step=1.0)
                    fertilizing_weeks = st.number_input("How many weeks in a month did you fertilize?", min_value=0.00, max_value=4.00, step=1.0)
                    fertilizing_months = st.number_input("How many months in a year did you fertilize?", min_value=0.00, max_value=12.00, step=1.0)
                st.subheader("Weeding")
                weeding_yesno = st.radio("Did you incur any costs for Weeding?:", ("Yes", "No"))
                if weeding_yesno == "Yes":
                    weeding_laborers = st.number_input("How many laborers did you hire for Weeding?", min_value=0.00, step=1.0)
                    weeding_days = st.number_input("How many days in a week do you perform weeding?", min_value=0.00, max_value=7.00, step=1.0)
                    weeding_weeks = st.number_input("How many weeks in a month did you perform weeding?", min_value=0.00, max_value=4.00, step=1.0)
                    weeding_months = st.number_input("How many months in a year did you perform weeding?", min_value=0.00, max_value=12.00, step=1.0)
                st.subheader("Bagging")
                bagging_yesno = st.radio("Did you incur any costs for bagging?:", ("Yes", "No"))
                if bagging_yesno == "Yes":
                    bagging_laborers = st.number_input("How many laborers did you hire for bagging?", min_value=0.00, step=1.0)
                    bagging_days = st.number_input("How many days in a week do you perform bagging?", min_value=0.00, max_value=7.00, step=1.0)
                    bagging_weeks = st.number_input("How many weeks in a month did you perform bagging?", min_value=0.00, max_value=4.00, step=1.0)
                    bagging_months = st.number_input("How many months in a year did you perform bagging?", min_value=0.00, max_value=12.00, step=1.0)
                st.subheader("Harvesting")
                harvesting_yesno = st.radio("Did you incur any costs for harvesting?:", ("Yes", "No"))
                if harvesting_yesno == "Yes":
                    harvesting_cost_per_bunch = st.number_input("How much does each laborer get paid for harvesting one bunch?", min_value=0.00, step=1.0)
            elif dataset == "Sto. Tomas, Davao del Norte - World Bank 2012":
                st.subheader("Deleafing")
                deleafing_yesno = st.radio("Did you incur any costs for deleafing?:", ("Yes", "No"))
                if deleafing_yesno == "Yes":
                    deleafing_laborers = st.number_input("How many laborers did you hire for deleafing?", min_value=0.00, step=1.0)
                    deleafing_days = st.number_input("How many days in a week do you perform deleafing?", min_value=0.00, max_value=7.00, step=1.0)
                    deleafing_weeks = st.number_input("How many weeks in a month did you perform deleafing?", min_value=0.00, max_value=4.00, step=1.0)
                    deleafing_months = st.number_input("How many months in a year did you perform deleafing?", min_value=0.00, max_value=12.00, step=1.0)
                st.subheader("Spraying")
                spraying_yesno = st.radio("Did you incur any costs for Spraying?:", ("Yes", "No"))
                if spraying_yesno == "Yes":
                    spraying_laborers = st.number_input("How many laborers did you hire for spraying?", min_value=0.00, step=1.0)
                    spraying_days = st.number_input("How many days in a week do you spray?", min_value=0.00, max_value=7.00, step=1.0)
                    spraying_weeks = st.number_input("How many weeks in a month did you spray?", min_value=0.00, max_value=4.00, step=1.0)
                    spraying_months = st.number_input("How many months in a year did you spray?", min_value=0.00, max_value=12.00, step=1.0)
                st.subheader("Fertilizing")
                fertilizing_yesno = st.radio("Did you incur any costs for Fertilizing?:", ("Yes", "No"))
                if fertilizing_yesno == "Yes":
                    fertilizing_laborers = st.number_input("How many laborers did you hire for fertilizing?", min_value=0.00, step=1.0)
                    fertilizing_days = st.number_input("How many days in a week do you fertilize?", min_value=0.00, max_value=7.00, step=1.0)
                    fertilizing_weeks = st.number_input("How many weeks in a month did you fertilize?", min_value=0.00, max_value=4.00, step=1.0)
                    fertilizing_months = st.number_input("How many months in a year did you fertilize?", min_value=0.00, max_value=12.00, step=1.0)
                st.subheader("Weeding")
                weeding_yesno = st.radio("Did you incur any costs for Weeding?:", ("Yes", "No"))
                if weeding_yesno == "Yes":
                    weeding_laborers = st.number_input("How many laborers did you hire for Weeding?", min_value=0.00, step=1.0)
                    weeding_days = st.number_input("How many days in a week do you perform weeding?", min_value=0.00, max_value=7.00, step=1.0)
                    weeding_weeks = st.number_input("How many weeks in a month did you perform weeding?", min_value=0.00, max_value=4.00, step=1.0)
                    weeding_months = st.number_input("How many months in a year did you perform weeding?", min_value=0.00, max_value=12.00, step=1.0)
                st.subheader("Bagging")
                bagging_yesno = st.radio("Did you incur any costs for bagging?:", ("Yes", "No"))
                if bagging_yesno == "Yes":
                    bagging_laborers = st.number_input("How many laborers did you hire for bagging?", min_value=0.00, step=1.0)
                    bagging_days = st.number_input("How many days in a week do you perform bagging?", min_value=0.00, max_value=7.00, step=1.0)
                    bagging_weeks = st.number_input("How many weeks in a month did you perform bagging?", min_value=0.00, max_value=4.00, step=1.0)
                    bagging_months = st.number_input("How many months in a year did you perform bagging?", min_value=0.00, max_value=12.00, step=1.0)
                st.subheader("Harvesting")
                harvesting_yesno = st.radio("Did you incur any costs for harvesting?:", ("Yes", "No"))
                if harvesting_yesno == "Yes":
                    harvesting_cost_per_bunch = st.number_input("How much does each laborer get paid for harvesting one bunch?", min_value=0.00, step=1.0)

        with tab4:
            st.subheader("Transportation")
            transpo_yesno = st.radio("Did you incur any costs for transportation?:", ("Yes", "No"))
            if transpo_yesno == "Yes":
                transpo_cost = st.number_input("How much did you spent on transportation?", min_value=0.00, step=1.0)
            st.subheader("Others")
            other_yesno = st.radio("Did you incur any other costs?:", ("Yes", "No"))
            if other_yesno == "Yes":
                other_cost = st.number_input("How much did you spend on the other cost?", min_value=0.00, step=1.0)

    elif type_of_banana_sell == "Banana and Banana Flour":
        st.header("Costs")
        tab1, tab2, tab3, tab4, tab5 = st.tabs(["Input Costs", "Materials Costs", "Labor Costs", "Other Cost", "Banana Flour Processing Costs"])
        with tab1:
            if dataset == "Sto. Tomas, Davao del Norte - CHED 2017":
                st.subheader("Fertilizer")
                fert_cost_per_sackbag = st.number_input("How much does a sack/bag of Fertilizer cost?", min_value=0.00, step=1.0)
                fert_number_sackbag = st.number_input("How many sacks/bags of Fertilizer did you use per hectare?", min_value=0.00, step=1.0)
                fert_days = st.number_input("How many days in a week did you apply the Fertilizer?", min_value=0.00, max_value=7.00, step=1.0)
                fert_weeks = st.number_input("How many weeks in a month did you apply the Fertilizer?", min_value=0.00, max_value=4.00, step=1.0)
                fert_months = st.number_input("How many months in a year did you apply the Fertilizer?", min_value=0.00, max_value=12.00, step=1.0)
                st.subheader("Sigatoka Control Chemical")
                siga_cost_per_sackbag = st.number_input("How much does a liter of Sigatoka Control Chemical cost?", min_value=0.00, step=1.0)
                siga_number_sackbag = st.number_input("How many liters of Sigatoka Control Chemical did you use per hectare?", min_value=0.00, step=1.0)
                siga_days = st.number_input("How many days in a week did you apply the Sigatoka Control Chemical?", min_value=0.00, max_value=7.00, step=1.0)
                siga_weeks = st.number_input("How many weeks in a month did you apply the Sigatoka Control Chemical?", min_value=0.00, max_value=4.00, step=1.0)
                siga_months = st.number_input("How many months in a year did you apply the Sigatoka Control Chemical?", min_value=0.00, max_value=12.00, step=1.0)
            elif dataset == "Sto. Tomas, Davao del Norte - World Bank 2012":
                st.subheader("Fertilizer")
                fert_cost_per_sackbag = st.number_input("How much does a sack/bag of Fertilizer cost?", min_value=0.00, step=1.0)
                fert_number_sackbag = st.number_input("How many sacks/bags of Fertilizer did you use per hectare?", min_value=0.00, step=1.0)
                fert_days = st.number_input("How many days in a week did you apply the Fertilizer?", min_value=0.00, max_value=7.00, step=1.0)
                fert_weeks = st.number_input("How many weeks in a month did you apply the Fertilizer?", min_value=0.00, max_value=4.00, step=1.0)
                fert_months = st.number_input("How many months in a year did you apply the Fertilizer?", min_value=0.00, max_value=12.00, step=1.0)
                st.subheader("Herbicide")
                h_cost_per_liter = st.number_input("How much does a liter of Herbicide cost?", min_value=0.00, step=1.0)
                h_number_liter = st.number_input("How many liters of Herbicide did you use per hectare?", min_value=0.00, step=1.0)
                h_days = st.number_input("How many days in a week did you apply the Herbicide?", min_value=0.00, max_value=7.00, step=1.0)
                h_weeks = st.number_input("How many weeks in a month did you apply the Herbicide?", min_value=0.00, max_value=4.00, step=1.0)
                h_months = st.number_input("How many months in a year did you apply the Herbicide?", min_value=0.00, max_value=12.00, step=1.0)
                st.subheader("Sigatoka Control Chemical")
                siga_cost_per_sackbag = st.number_input("How much does a liter of Sigatoka Control Chemical cost?", min_value=0.00, step=1.0)
                siga_number_sackbag = st.number_input("How many liters of Sigatoka Control Chemical did you use per hectare?", min_value=0.00, step=1.0)
                siga_days = st.number_input("How many days in a week did you apply the Sigatoka Control Chemical?", min_value=0.00, max_value=7.00, step=1.0)
                siga_weeks = st.number_input("How many weeks in a month did you apply the Sigatoka Control Chemical?", min_value=0.00, max_value=4.00, step=1.0)
                siga_months = st.number_input("How many months in a year did you apply the Sigatoka Control Chemical?", min_value=0.00, max_value=12.00, step=1.0)
                st.subheader("Bud Injection")
                bi_cost_per_liter = st.number_input("How much does a liter of Bud Injection cost?", min_value=0.00, step=1.0)
                bi_number_liter = st.number_input("How many liters of Bud Injection did you use per hectare?", min_value=0.00, step=1.0)
                bi_days = st.number_input("How many days in a week did you apply the Bud Injection?", min_value=0.00, max_value=7.00, step=1.0)
                bi_weeks = st.number_input("How many weeks in a month did you apply the Bud Injection?", min_value=0.00, max_value=4.00, step=1.0)
                bi_months = st.number_input("How many months in a year did you apply the Bud Injection?", min_value=0.00, max_value=12.00, step=1.0)
                st.subheader("Bunch Spray")
                bs_cost_per_liter = st.number_input("How much does a liter of Bunch Spray cost?", min_value=0.00, step=1.0)
                bs_number_liter = st.number_input("How many liters of Bunch Spray did you use per hectare?", min_value=0.00, step=1.0)
                bs_days = st.number_input("How many days in a week did you apply the Bunch Spray?", min_value=0.00, max_value=7.00, step=1.0)
                bs_weeks = st.number_input("How many weeks in a month did you apply the Bunch Spray?", min_value=0.00, max_value=4.00, step=1.0)
                bs_months = st.number_input("How many months in a year did you apply the Bunch Spray?", min_value=0.00, max_value=12.00, step=1.0)

        with tab2:
            st.subheader("Polybags")
            polybags_yesno = st.radio("Did you use polybags?", ("Yes", "No"))
            if polybags_yesno == "Yes":
                polybags_cost_per_kilo = st.number_input("How much does a kilogram of polybags cost?", min_value=0.00, step=1.0)
                polybags_number_kilo = st.number_input("How many kilograms of polybags did you use per hectare?", min_value=0.00, step=1.0)
            st.subheader("Ribbons")
            ribbons_yesno = st.radio("Did you use ribbons?", ("Yes", "No"))
            if ribbons_yesno == "Yes":
                ribbons_cost_per_kilo = st.number_input("How much does a kilogram of ribbons cost?", min_value=0.00, step=1.0)
                ribbons_number_kilo = st.number_input("How many kilograms of ribbons did you use per hectare?", min_value=0.00, step=1.0)
            st.subheader("Twine")
            twine_yesno = st.radio("Did you use twine?", ("Yes", "No"))
            if twine_yesno == "Yes":
                twine_cost_per_kilo = st.number_input("How much does a kilogram of twine cost?", min_value=0.00, step=1.0)
                twine_number_kilo = st.number_input("How many kilograms of twine did you use per hectare?", min_value=0.00, step=1.0)
            st.subheader("Bamboo")
            bamboo_yesno = st.radio("Did you use bamboo?", ("Yes", "No"))
            if bamboo_yesno == "Yes":
                bamboo_cost_per_piece = st.number_input("How much does a piece of bamboo cost?", min_value=0.00, step=1.0)
                bamboo_number_piece = st.number_input("How many pieces of bamboo did you use per hectare?", min_value=0.00, step=1.0)
            st.subheader("Fuel/Oil/Lubricants")
            fol_yesno = st.radio("Did you use Fuel/Oil/Lubricants?", ("Yes", "No"))
            if fol_yesno == "Yes":
                fol_cost_per_piece = st.number_input("How much does a liter of Fuel/Oil/Lubricants cost?", min_value=0.00, step=1.0)
                fol_number_piece = st.number_input("How many liters of Fuel/Oil/Lubricants did you use per hectare?", min_value=0.00, step=1.0)

        with tab3:
            if dataset == "Sto. Tomas, Davao del Norte - CHED 2017":
                st.subheader("Spraying")
                spraying_yesno = st.radio("Did you incur any costs for Spraying?:", ("Yes", "No"))
                if spraying_yesno == "Yes":
                    spraying_laborers = st.number_input("How many laborers did you hire for spraying?", min_value=0.00, step=1.0)
                    spraying_days = st.number_input("How many days in a week do you spray?", min_value=0.00, max_value=7.00, step=1.0)
                    spraying_weeks = st.number_input("How many weeks in a month did you spray?", min_value=0.00, max_value=4.00, step=1.0)
                    spraying_months = st.number_input("How many months in a year did you spray?", min_value=0.00, max_value=12.00, step=1.0)
                st.subheader("Fertilizing")
                fertilizing_yesno = st.radio("Did you incur any costs for Fertilizing?:", ("Yes", "No"))
                if fertilizing_yesno == "Yes":
                    fertilizing_laborers = st.number_input("How many laborers did you hire for fertilizing?", min_value=0.00, step=1.0)
                    fertilizing_days = st.number_input("How many days in a week do you fertilize?", min_value=0.00, max_value=7.00, step=1.0)
                    fertilizing_weeks = st.number_input("How many weeks in a month did you fertilize?", min_value=0.00, max_value=4.00, step=1.0)
                    fertilizing_months = st.number_input("How many months in a year did you fertilize?", min_value=0.00, max_value=12.00, step=1.0)
                st.subheader("Weeding")
                weeding_yesno = st.radio("Did you incur any costs for Weeding?:", ("Yes", "No"))
                if weeding_yesno == "Yes":
                    weeding_laborers = st.number_input("How many laborers did you hire for Weeding?", min_value=0.00, step=1.0)
                    weeding_days = st.number_input("How many days in a week do you perform weeding?", min_value=0.00, max_value=7.00, step=1.0)
                    weeding_weeks = st.number_input("How many weeks in a month did you perform weeding?", min_value=0.00, max_value=4.00, step=1.0)
                    weeding_months = st.number_input("How many months in a year did you perform weeding?", min_value=0.00, max_value=12.00, step=1.0)
                st.subheader("Bagging")
                bagging_yesno = st.radio("Did you incur any costs for bagging?:", ("Yes", "No"))
                if bagging_yesno == "Yes":
                    bagging_laborers = st.number_input("How many laborers did you hire for bagging?", min_value=0.00, step=1.0)
                    bagging_days = st.number_input("How many days in a week do you perform bagging?", min_value=0.00, max_value=7.00, step=1.0)
                    bagging_weeks = st.number_input("How many weeks in a month did you perform bagging?", min_value=0.00, max_value=4.00, step=1.0)
                    bagging_months = st.number_input("How many months in a year did you perform bagging?", min_value=0.00, max_value=12.00, step=1.0)
                st.subheader("Harvesting")
                harvesting_yesno = st.radio("Did you incur any costs for harvesting?:", ("Yes", "No"))
                if harvesting_yesno == "Yes":
                    harvesting_cost_per_bunch = st.number_input("How much does each laborer get paid for harvesting one bunch?", min_value=0.00, step=1.0)
            elif dataset == "Sto. Tomas, Davao del Norte - World Bank 2012":
                st.subheader("Deleafing")
                deleafing_yesno = st.radio("Did you incur any costs for deleafing?:", ("Yes", "No"))
                if deleafing_yesno == "Yes":
                    deleafing_laborers = st.number_input("How many laborers did you hire for deleafing?", min_value=0.00, step=1.0)
                    deleafing_days = st.number_input("How many days in a week do you perform deleafing?", min_value=0.00, max_value=7.00, step=1.0)
                    deleafing_weeks = st.number_input("How many weeks in a month did you perform deleafing?", min_value=0.00, max_value=4.00, step=1.0)
                    deleafing_months = st.number_input("How many months in a year did you perform deleafing?", min_value=0.00, max_value=12.00, step=1.0)
                st.subheader("Spraying")
                spraying_yesno = st.radio("Did you incur any costs for Spraying?:", ("Yes", "No"))
                if spraying_yesno == "Yes":
                    spraying_laborers = st.number_input("How many laborers did you hire for spraying?", min_value=0.00, step=1.0)
                    spraying_days = st.number_input("How many days in a week do you spray?", min_value=0.00, max_value=7.00, step=1.0)
                    spraying_weeks = st.number_input("How many weeks in a month did you spray?", min_value=0.00, max_value=4.00, step=1.0)
                    spraying_months = st.number_input("How many months in a year did you spray?", min_value=0.00, max_value=12.00, step=1.0)
                st.subheader("Fertilizing")
                fertilizing_yesno = st.radio("Did you incur any costs for Fertilizing?:", ("Yes", "No"))
                if fertilizing_yesno == "Yes":
                    fertilizing_laborers = st.number_input("How many laborers did you hire for fertilizing?", min_value=0.00, step=1.0)
                    fertilizing_days = st.number_input("How many days in a week do you fertilize?", min_value=0.00, max_value=7.00, step=1.0)
                    fertilizing_weeks = st.number_input("How many weeks in a month did you fertilize?", min_value=0.00, max_value=4.00, step=1.0)
                    fertilizing_months = st.number_input("How many months in a year did you fertilize?", min_value=0.00, max_value=12.00, step=1.0)
                st.subheader("Weeding")
                weeding_yesno = st.radio("Did you incur any costs for Weeding?:", ("Yes", "No"))
                if weeding_yesno == "Yes":
                    weeding_laborers = st.number_input("How many laborers did you hire for Weeding?", min_value=0.00, step=1.0)
                    weeding_days = st.number_input("How many days in a week do you perform weeding?", min_value=0.00, max_value=7.00, step=1.0)
                    weeding_weeks = st.number_input("How many weeks in a month did you perform weeding?", min_value=0.00, max_value=4.00, step=1.0)
                    weeding_months = st.number_input("How many months in a year did you perform weeding?", min_value=0.00, max_value=12.00, step=1.0)
                st.subheader("Bagging")
                bagging_yesno = st.radio("Did you incur any costs for bagging?:", ("Yes", "No"))
                if bagging_yesno == "Yes":
                    bagging_laborers = st.number_input("How many laborers did you hire for bagging?", min_value=0.00, step=1.0)
                    bagging_days = st.number_input("How many days in a week do you perform bagging?", min_value=0.00, max_value=7.00, step=1.0)
                    bagging_weeks = st.number_input("How many weeks in a month did you perform bagging?", min_value=0.00, max_value=4.00, step=1.0)
                    bagging_months = st.number_input("How many months in a year did you perform bagging?", min_value=0.00, max_value=12.00, step=1.0)
                st.subheader("Harvesting")
                harvesting_yesno = st.radio("Did you incur any costs for harvesting?:", ("Yes", "No"))
                if harvesting_yesno == "Yes":
                    harvesting_cost_per_bunch = st.number_input("How much does each laborer get paid for harvesting one bunch?", min_value=0.00, step=1.0)

        with tab4:
            st.subheader("Transportation")
            transpo_yesno = st.radio("Did you incur any costs for transportation?:", ("Yes", "No"))
            if transpo_yesno == "Yes":
                transpo_cost = st.number_input("How much did you spent on transportation?", min_value=0.00, step=1.0)
            st.subheader("Others")
            other_yesno = st.radio("Did you incur any other costs?:", ("Yes", "No"))
            if other_yesno == "Yes":
                other_cost = st.number_input("How much did you spend on the other cost?", min_value=0.00, step=1.0)

        with tab5:
            st.subheader("Labor Costs")
            regular_laborers = st.number_input("How many regular laborers were hired?", min_value=0.00, step=1.0)
            regular_days = st.number_input("How many days were the regular laborers hired for slicing and drying?", min_value=0.00, step=1.0)
            regular_laborers_day = st.number_input("How much is a regular laborer paid per day?", min_value=0.00, step=1.0)
            nonregular_laborers_wash = st.number_input("How many non regular laborers were hired for washing?", min_value=0.00, step=1.0)
            nonregular_laborers_peel = st.number_input("How many non regular laborers were hired for peeling?", min_value=0.00, step=1.0)
            nonregular_kilos_wash = st.number_input("How many kilos of banana were assigned to each non regular laborer for washing?", min_value=0.00, step=1.0)
            nonregular_kilos_peel = st.number_input("How many kilos of banana were assigned to each non regular laborer for peeling?", min_value=0.00, step=1.0)
            st.subheader("Milling Costs")
            number_mills = st.number_input("How many mills were operated?", min_value=0.00, step=1.0)
            cost_per_mill = st.number_input("What is the operational cost per mill?", min_value=0.00, step=1.0)
            st.subheader("Setup Costs")
            setup_cost = st.number_input("How many kilos of off grade bananas were delivered?", min_value=0.00, step=1.0)
            st.subheader("Other Operational Costs")
            other_operational_costs = st.number_input("Input Other Operational Costs that you incurred", min_value=0.00, step=1.0)

if dataset == "Sto. Tomas, Davao del Norte - World Bank 2012":
    m_deleafing_cost_per_laborer = 180
    m_spraying_cost_per_laborer = 180
    m_fertilizing_cost_per_laborer = 200
    m_weeding_cost_per_laborer = 180
    m_bagging_cost_per_laborer = 180

    nonregular_laborers_cost_peel = 0.4545
    nonregular_laborers_cost_wash = 0.5303
		
    bi_cost = (bi_cost_per_liter * bi_number_liter * bi_days * bi_weeks * bi_months)
    bs_cost = (bs_cost_per_liter * bs_number_liter * bs_days * bs_weeks * bs_months)
    fert_cost = (fert_cost_per_sackbag * fert_number_sackbag * fert_days * fert_weeks * fert_months)
    h_cost = (h_cost_per_liter * h_number_liter * h_days * h_weeks * h_months)
    siga_cost = (siga_cost_per_sackbag * siga_number_sackbag * siga_days * siga_weeks * siga_months)
    input_cost = (bi_cost + bs_cost + fert_cost + siga_cost + h_cost)
	
    polybag_cost = (polybags_cost_per_kilo * polybags_number_kilo)
    ribbons_cost = (ribbons_cost_per_kilo * ribbons_number_kilo)
    twine_cost = (twine_cost_per_kilo * twine_number_kilo)
    bamboo_cost = (bamboo_cost_per_piece * bamboo_number_piece)
    materials_cost = (polybag_cost + ribbons_cost + twine_cost + bamboo_cost)
    
    m_spraying_cost = (spraying_laborers * m_spraying_cost_per_laborer * spraying_days * spraying_weeks * spraying_months)
    m_fertilizing_cost = (fertilizing_laborers * m_fertilizing_cost_per_laborer * fertilizing_days * fertilizing_weeks * fertilizing_months)
    m_weeding_cost = (weeding_laborers * m_weeding_cost_per_laborer * weeding_days * weeding_weeks * weeding_months)
    m_deleafing_cost = (deleafing_laborers * m_deleafing_cost_per_laborer * deleafing_days * deleafing_weeks * deleafing_months)
    m_bagging_cost = (bagging_laborers * m_bagging_cost_per_laborer * bagging_days * bagging_weeks * bagging_months)
    
    harvesting_cost = (harvesting_cost_per_bunch * bunch)
    m_labor_cost = (m_spraying_cost + m_fertilizing_cost + m_weeding_cost + m_deleafing_cost + m_bagging_cost + harvesting_cost)

    regular_laborers_cost = regular_laborers * regular_days * regular_laborers_day
    nonregular_laborers_cost_wash = nonregular_laborers_wash * nonregular_kilos_wash * nonregular_laborers_cost_wash
    nonregular_laborers_cost_peel = nonregular_laborers_peel * nonregular_kilos_peel * nonregular_laborers_cost_peel
    mill_cost = number_mills * cost_per_mill
    setupcost = setup_cost * 0.25
    
    banana_flour_production_cost = regular_laborers_cost + nonregular_laborers_cost_wash+ nonregular_laborers_cost_peel + mill_cost + setupcost + other_operational_costs

    total_cost = input_cost + materials_cost + m_labor_cost + transpo_cost +  banana_flour_production_cost

elif dataset == "Sto. Tomas, Davao del Norte - CHED 2017":
    input_cost = 0
    materials_cost = 0
    total_cost = 0
		
    bi_cost = 0
    bs_cost = 0
    fert_cost = (fert_cost_per_sackbag * fert_number_sackbag * fert_days * fert_weeks * fert_months)
    siga_cost = (siga_cost_per_sackbag * siga_number_sackbag * siga_days * siga_weeks * siga_months)
    h_cost = 0
    input_cost = (fert_cost + siga_cost)

    nonregular_laborers_cost_peel = 0.4545
    nonregular_laborers_cost_wash = 0.5303
	
    polybag_cost = (polybags_cost_per_kilo * polybags_number_kilo)
    ribbons_cost = (ribbons_cost_per_kilo * ribbons_number_kilo)
    twine_cost = (twine_cost_per_kilo * twine_number_kilo)
    bamboo_cost = (bamboo_cost_per_piece * bamboo_number_piece)
    materials_cost = (polybag_cost + ribbons_cost + twine_cost + bamboo_cost)
	
    spraying_cost = (spraying_laborers * 340 * spraying_days * spraying_weeks * spraying_months)
    fertilizing_cost = (fertilizing_laborers * 340 * fertilizing_days * fertilizing_weeks * fertilizing_months)
    weeding_cost = (weeding_laborers * 340 * weeding_days * weeding_weeks * weeding_months)
    deleafing_cost = 0
    bagging_cost = (bagging_laborers * 340 * bagging_days * bagging_weeks * bagging_months)
    harvesting_cost = (harvesting_cost_per_bunch * bunch)
    labor_cost = (spraying_cost + fertilizing_cost + weeding_cost + bagging_cost + harvesting_cost)
	
    regular_laborers_cost = regular_laborers * regular_days * regular_laborers_day
    nonregular_laborers_cost_wash = nonregular_laborers_wash * nonregular_kilos_wash * nonregular_laborers_cost_wash
    nonregular_laborers_cost_peel = nonregular_laborers_peel * nonregular_kilos_peel * nonregular_laborers_cost_peel
    mill_cost = number_mills * cost_per_mill
    setupcost = setup_cost * 0.25
    
    banana_flour_production_cost = regular_laborers_cost + nonregular_laborers_cost_wash+ nonregular_laborers_cost_peel + mill_cost + setupcost + other_operational_costs

    total_cost = input_cost + materials_cost + labor_cost + transpo_cost +  banana_flour_production_cost

def calculate_profit_banana_flour(percent_contractualmarket, percent_spotmarket, percent_bananaflourmarket):
    total_percentbanana = percent_contractualmarket + percent_spotmarket + percent_bananaflourmarket
    total_percentflour = percent_bananaflourmarket

    total_flour = (percent_bananaflourmarket * total_banana) * conversion_factor

    if total_percentbanana > 0:
        contractualmarket_profit = (
            ((percent_contractualmarket/total_percentbanana) * total_banana) * price_contractualmarket
        )
        spotmarket_profit = (
            ((percent_spotmarket/total_percentbanana) * total_banana) * price_spotmarket
        )
    if total_percentbanana == 0:
        contractualmarket_profit = 0
        spotmarket_profit = 0
        bananaflourmarket_profit = 0
    if total_percentflour > 0:
        bananaflourmarket_profit = (
            ((percent_bananaflourmarket/total_percentbanana) * total_flour) * price_bananaflourmarket
        )
    if total_percentflour == 0:
        bananaflourmarket_profit = 0
    total_profit = (
        (contractualmarket_profit + spotmarket_profit + bananaflourmarket_profit) - (total_cost)
    )
    return total_profit

def calculate_profit_banana(percent_contractualmarket, percent_spotmarket):
    total_percentbanana = percent_contractualmarket + percent_spotmarket
    total_percentflour = 0

    total_flour = (percent_bananaflourmarket * total_banana) * conversion_factor

    if total_percentbanana > 0:
        contractualmarket_profit = (
            ((percent_contractualmarket/total_percentbanana) * total_banana) * price_contractualmarket
        )
        spotmarket_profit = (
            ((percent_spotmarket/total_percentbanana) * total_banana) * price_spotmarket
        )
    if total_percentbanana == 0:
        contractualmarket_profit = 0
        spotmarket_profit = 0
    if total_percentflour > 0:
        bananaflourmarket_profit = (
            ((percent_bananaflourmarket/total_percentbanana) * total_flour) * price_bananaflourmarket
        )
    if total_percentflour == 0:
        bananaflourmarket_profit = 0
    total_profit = (
        (contractualmarket_profit + spotmarket_profit + bananaflourmarket_profit) - (total_cost)
    )
    return total_profit

def optimize_market_allocations():
    variables = []
    if type_of_banana_sell == "Banana":
        variables = ['percent_contractualmarket', 'percent_spotmarket']
    elif type_of_banana_sell == "Banana and Banana Flour":
        variables = ['percent_contractualmarket', 'percent_spotmarket', 'percent_bananaflourmarket']

    values = np.linspace(0, 1, num=11)

    def market_allocation_generator(variables):
        for combo in product(values, repeat=len(variables)):
            allocation = dict(zip(variables, combo))
            if all(value >= 0 for value in allocation.values()):
                if np.isclose(sum(allocation.values()), 1):
                    yield allocation

    market_allocations = list(market_allocation_generator(variables))
    num_allocations = len(market_allocations)

    if num_allocations == 0:
        st.warning("No valid market allocations found.")
        return

    profits = np.zeros(num_allocations)

    # Calculate profits for each market allocation
    for i, case in enumerate(market_allocations):
        if type_of_banana_sell == "Banana":
            profits[i] = calculate_profit_banana(**case)
        elif type_of_banana_sell == "Banana and Banana Flour":
            profits[i] = calculate_profit_banana_flour(**case)

    # Find the index of the maximum profit
    max_profit_index = np.argmax(profits)
    max_profit_value = profits[max_profit_index]
    max_profit_case = market_allocations[max_profit_index]

    # Print overall maximum profit
    if type_of_banana_sell == "Banana":
        st.markdown(f"<h3>OPTIMIZED MARKET ALLOCATION:</h3>", unsafe_allow_html=True)
        st.write(f"\n")
        st.markdown(f"<h4>Contractual Market: {round((max_profit_case['percent_contractualmarket'] * 100), 2)}%</h4>", unsafe_allow_html=True)
        st.write(f"\n")
        st.markdown(f"<h4>Spot Market: {round((max_profit_case['percent_spotmarket'] * 100), 2)}%</h4>", unsafe_allow_html=True)
        st.write(f"\n")
        st.markdown(f"<h4>Maximum Profit: ₱{max_profit_value:.2f}</h4>", unsafe_allow_html=True)
        st.write(f"\n")
    elif type_of_banana_sell == "Banana and Banana Flour":
        st.markdown(f"<h3>OPTIMIZED MARKET ALLOCATION:</h3>", unsafe_allow_html=True)
        st.write(f"\n")
        st.markdown(f"<h4>Contractual Market: {round((max_profit_case['percent_contractualmarket'] * 100), 2)}%</h4>", unsafe_allow_html=True)
        st.write(f"\n")
        st.markdown(f"<h4>Spot Market: {round((max_profit_case['percent_spotmarket'] * 100), 2)}%</h4>", unsafe_allow_html=True)
        st.write(f"\n")
        st.markdown(f"<h4>Banana Flour Market: {round((max_profit_case['percent_bananaflourmarket'] * 100), 2)}%</h4>", unsafe_allow_html=True)
        st.write(f"\n")
        st.markdown(f"<h4>Maximum Profit: ₱{max_profit_value:.2f}</h4>", unsafe_allow_html=True)
        st.write(f"\n")
    
st.header("Calculation:")
if st.button("Optimize"):
    if type_of_banana_sell == "Banana":
        st.markdown(f"<h3>DESIRED ALLOCATION:</h3>", unsafe_allow_html=True)
        st.write(f"\n")
        st.markdown(f"<h4>Contractual Market: {percent_contractualmarket}%</h4>", unsafe_allow_html=True)
        st.write(f"\n")
        st.markdown(f"<h4>Spot Market: {percent_spotmarket}%</h4>", unsafe_allow_html=True)
        st.write(f"\n")

        # Normalize the percentages to ensure they add up to 100%
        total_desired_allocation = percent_contractualmarket + percent_spotmarket
        normalized_percent_contractual = percent_contractualmarket / total_desired_allocation
        normalized_percent_spot = percent_spotmarket / total_desired_allocation

        # Use the calculate_profit function for the normalized desired allocation
        desired_allocation_profit = calculate_profit_banana(
            normalized_percent_contractual, normalized_percent_spot
        )

        st.markdown(f"<h4>Total Profit: ₱{desired_allocation_profit:.2f}</h4>", unsafe_allow_html=True)
        st.write(f"\n")
    elif type_of_banana_sell == "Banana and Banana Flour":
        st.markdown(f"<h3>DESIRED ALLOCATION:</h3>", unsafe_allow_html=True)
        st.write(f"\n")
        st.markdown(f"<h4>Contractual Market: {percent_contractualmarket}%</h4>", unsafe_allow_html=True)
        st.write(f"\n")
        st.markdown(f"<h4>Spot Market: {percent_spotmarket}%</h4>", unsafe_allow_html=True)
        st.write(f"\n")
        st.markdown(f"<h4>Banana Flour Market: {percent_bananaflourmarket}%</h4>", unsafe_allow_html=True)
        st.write(f"\n")

        # Normalize the percentages to ensure they add up to 100%
        total_desired_allocation = percent_contractualmarket + percent_spotmarket + percent_bananaflourmarket
        normalized_percent_contractual = percent_contractualmarket / total_desired_allocation
        normalized_percent_spot = percent_spotmarket / total_desired_allocation
        normalized_percent_bananaflour = percent_bananaflourmarket / total_desired_allocation

        # Use the calculate_profit function for the normalized desired allocation
        desired_allocation_profit = calculate_profit_banana_flour(
            normalized_percent_contractual, normalized_percent_spot, normalized_percent_bananaflour
        )

        st.markdown(f"<h4>Total Profit: ₱{desired_allocation_profit:.2f}</h4>", unsafe_allow_html=True)
        st.write(f"\n")

    optimize_market_allocations()
