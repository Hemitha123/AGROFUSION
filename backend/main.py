from fastapi import FastAPI
from schemas import FarmInput
from crop_engine import recommend_crop
from risk_engine import get_weather_forecast, calculate_risk
from prevention_engine import generate_prevention_alert

app = FastAPI(title="AgroFusion AI")


@app.post("/plan")
def generate_plan(data: FarmInput):

    # ✅ Step 1: Crop recommendation
    result = recommend_crop(data.soil_type, data.water_availability)

    # ✅ Step 2: Weather forecast
    forecast = get_weather_forecast(data.location)

    # ✅ Step 3: Risk calculation
    risk = calculate_risk(
        temperature=data.temperature,
        rainfall=data.rainfall,
        humidity=data.humidity
    )

    # ✅ Step 3.1: Prepare weather summary
    avg_temp = data.temperature
    total_rain = data.rainfall

    # ✅ Step 4: Yield based on land size
    total_yield = result["yield"] * data.land_size

    # ✅ Step 5: Farmer-friendly advice
    advice_msg = (
        f"Based on your soil and water conditions, "
        f"{result['crop']} is recommended for your farm."
    )

    # 🔹 Step 6: Prevention alerts
    alerts = generate_prevention_alert(
        result["crop"],
        avg_temp,
        total_rain
    )

    # ✅ Final response
    return {
        "recommended_crop": result["crop"],
        "expected_yield": f"{total_yield} quintal",
        "estimated_price_per_quintal": f"₹{result['price']}",
        "confidence_score": result["score"],
        "weather_risk": risk,
        "weather_summary": {
            "avg_temp": avg_temp,
            "total_rain": total_rain
        },
        "prevention_alerts": alerts,
        "advice": advice_msg
    }
