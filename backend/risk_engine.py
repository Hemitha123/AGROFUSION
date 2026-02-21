# risk_engine.py

def get_weather_forecast(location: str):
    """
    Dummy weather forecast (hackathon friendly).
    Later you can connect real weather API.
    """

    # simple static forecast
    return {
        "temperature": 30,
        "rainfall": 100,
        "humidity": 70
    }


def calculate_risk(temperature: float, rainfall: float, humidity: float):
    """
    Simple weather risk logic.
    """

    risk_score = 0

    # 🌧 Rainfall risk
    if rainfall < 50:
        risk_score += 2
    elif rainfall < 100:
        risk_score += 1

    # 🌡 Temperature risk
    if temperature > 40 or temperature < 15:
        risk_score += 2
    elif temperature > 35:
        risk_score += 1

    # 💧 Humidity risk
    if humidity > 85:
        risk_score += 1

    # ✅ Final label
    if risk_score >= 4:
        return "High Risk"
    elif risk_score >= 2:
        return "Medium Risk"
    else:
        return "Low Risk"
