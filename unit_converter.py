import streamlit as st

conversion_factors = {
        'meters': 1,
        'kilometers': 1000,
        'centimeters': 0.01,
        'millimeters': 0.001,
        'inches': 0.0254,
        'feet': 0.3048,
        'yards': 0.9144,
        'miles': 1609.34,
        "grams": 0.001,
        "kilograms": 1,
        "milligrams": 0.000001,
    }

def converter(value, from_unit, to_unit):
    """Convert between different units of measurement."""
    
    try:
        converted_value = value * (conversion_factors[from_unit] / conversion_factors[to_unit])
        return converted_value
    except KeyError:
        st.error("Invalid unit selected.")
        return None
    
st.title("Unit Converter")
value = st.number_input("Enter the value to convert:", step= 1.0, min_value=0.0)
from_unit = st.selectbox("Select the unit to convert from:", list(conversion_factors.keys()))
to_unit = st.selectbox("Select the unit to convert to:", list(conversion_factors.keys()))


if st.button("Convert"):
    if value is not None:
        result = converter(value, from_unit, to_unit)
        if result is not None:
            st.success(f"{value} {from_unit} is equal to {result: .2f} {to_unit}")
