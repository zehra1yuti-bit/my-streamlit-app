import streamlit as st

class ThermostatAgent:
    def __init__(self, target: float = 22.0, tolerance: float = 1.0):
        self.target = target
        self.tolerance = tolerance

    def act(self, temperature: float) -> str:
        if temperature > self.target + self.tolerance:
            return "❄️ COOL (ማቀዝቀዣውን አብራ)"
        if temperature < self.target - self.tolerance:
            return "🔥 HEAT (ማሞቂያውን አብራ)"
        return "👍 IDLE (ሁኔታው መካከለኛ ነው)"

st.title("🌡️ AI Thermostat Agent")
st.write("ይህ የላብ 1 ቀላል ሬፍሌክስ ኤጀንት (Simple Reflex Agent) በዌብ መልክ ሲዘጋጅ ነው።")

target_temp = st.slider("የታለመው የሙቀት መጠን (Target Temp °C)", 10.0, 30.0, 22.0)
current_temp = st.slider("የአሁኑ የክፍል ሙቀት (Current Temp °C)", 0.0, 40.0, 21.5)

agent = ThermostatAgent(target=target_temp)
action = agent.act(current_temp)

st.subheader("የኤጀንቱ ውሳኔ (Action):")
st.success(action)