def fungal_risk_rule(avg_temp, humidity_estimate):
    """
    Simple scientific rule:
    Fungus thrives in:
    - high humidity
    - moderate temperature
    """

    if humidity_estimate > 80 and 20 <= avg_temp <= 30:
        return True
    return False


def pest_risk_rule(avg_temp):
    """
    Many pests increase in warm weather.
    """

    if avg_temp > 32:
        return True
    return False
def generate_prevention_alert(crop, avg_temp, total_rain):
    alerts = []

    # 🔹 crude humidity estimate from rain
    humidity_estimate = min(100, total_rain * 2)

    # 🌿 fungal check
    if fungal_risk_rule(avg_temp, humidity_estimate):
        alerts.append({
            "type": "Fungal Risk",
            "message": f"High chance of fungal infection in {crop}",
            "action": "Spray neem oil or recommended fungicide"
        })

    # 🐛 pest check
    if pest_risk_rule(avg_temp):
        alerts.append({
            "type": "Pest Risk",
            "message": f"Pest activity may increase in {crop}",
            "action": "Use pheromone traps and monitor leaves"
        })

    # ✅ fallback
    if not alerts:
        alerts.append({
            "type": "Safe",
            "message": "No major disease risk predicted",
            "action": "Continue regular monitoring"
        })

    return alerts
