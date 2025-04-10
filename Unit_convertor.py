import streamlit as st
st.markdown("<h1> Unit Convertor Using by Python and Streamlit </h1>", unsafe_allow_html=True)
st.write("Easily convert between different units of length, weight, and temprature.")

#sidebar menu
conversion_type = st.sidebar.selectbox("Choose Conversion Type",["Length", "Weight","Temprature"])
value =st.number_input("Enter Value, value=0.0,step=0.1")
col1, col2 = st.columns(2)

if conversion_type == "Length":
    with col1:
        from_unit = st.selectbox("From", ["Meters", "Centimeters", "Millimeters", "Miles", "Yards", "Inches", "Feet"])
    with col2:
        to_unit = st.selectbox("To", ["Meters", "Centimeters", "Millimeters", "Miles", "Yards", "Inches", "Feet"])
elif conversion_type == "Weight":
    with col1:
        from_unit = st.selectbox("From", ["Kilogram", "Grams", "Miligrams", "Pounds", "ounces"])
    with col2:
        to_unit = st.selectbox("To", ["Kilogram", "Grams", "Miligrams", "Pounds", "ounces"])
elif conversion_type == "Temprature":
    with col1:
        from_unit = st.selectbox("From", ["Celsis", "Fahrenheit", "kelvin"])
    with col2:
        to_unit = st.selectbox("To", ["Celsis", "Fahrenheit", "kelvin"])

#converted function
def length_convertor(value, from_unit, to_unit):
    length_units = {
        'Meters':1, 'Kilometers': 0.001, 'Centimeters': 100, 'Millimeters': 1000,
          'Miles': 0.000621371,'Yards': 1.09361, 'Feet': 3.28, 'Inches': 39.37}
    return (value / length_units[from_unit]) * length_units[to_unit]

def weight_convertor(value, from_unit, to_unit):
    weight_units = {
        'Kilogram': 1, 'Grams': 1000, 'Miligrams' : 1000000, 'Pounds': 2.2046, 'Ounces': 35.27}
    return(value / weight_units[from_unit]) * weight_units[to_unit]

def temp_convertor(value, from_unit, to_unit):
    if from_unit == "Celsius":
        return (value * 9/5 *32) if to_unit == "Fahrenheit" else value + 273.15 if to_unit == "Kelvis" else value
    elif from_unit == "Fahrenheit":
        return (value - 32) * 5/9 if to_unit == "Celsius" else (value -32) * 5/9 + 273.15 if to_unit == "Kelvis" else value
    elif from_unit == "kelvis":
        return value -273.15 if to_unit == "Celsius" else (value -273.15) * 9/5+32 if to_unit == "Fahrenheit" else value
    return value

#button for conversion
if st.button("Convert"):
    if conversion_type == "Length":
        result = length_convertor(value, from_unit, to_unit)
    elif conversion_type == "Weight":
        result = weight_convertor(value, from_unit, to_unit)
    elif conversion_type == "Temprature":
        result = temp_convertor (value, from_unit, to_unit)
    st.markdown(f"<div class='result-box'>{value} {from_unit} = {result:.4f} {to_unit}</div>", unsafe_allow_html=True)
st.markdown("<div class='footer'>Created by Mr. Salman Ali", unsafe_allow_html=True)
