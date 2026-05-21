import streamlit as st
import streamlit.components.v1 as components
import time

# --- 1. SET UP THE CORE CYBERPUNK LAYOUT ---
st.set_page_config(
    page_title="QUANTUM TRON HUD", 
    page_icon="🔮", 
    layout="centered"
)

# Initialize Session State Memory so it never sends 'None' to Python
if "step_memory" not in st.session_state:
    st.session_state.step_memory = 0

# --- 2. INJECT MASSIVE ULTRA-GLOW CSS CUSTOM DECORATIONS ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Share+Tech+Mono&display=swap');
    
    .stApp {
        background-color: #030308;
        background-image: linear-gradient(rgba(18, 10, 36, 0.4) 1px, transparent 1px),
                          linear-gradient(90deg, rgba(18, 10, 36, 0.4) 1px, transparent 1px);
        background-size: 20px 20px;
    }
    
    h1, h2, h3 {
        font-family: 'Orbitron', sans-serif !important;
        letter-spacing: 2px;
    }
    
    .neon-title {
        color: #b026ff !important;
        text-shadow: 0 0 10px #b026ff, 0 0 20px #b026ff, 0 0 30px #b026ff;
        text-align: center;
        font-weight: 900;
        font-size: 2.5rem;
        margin-bottom: 0px;
    }
    
    .glass-card {
        background: rgba(15, 15, 30, 0.65);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        border: 2px solid #b026ff;
        box-shadow: 0 0 15px rgba(176, 38, 255, 0.25), inset 0 0 15px rgba(176, 38, 255, 0.1);
        border-radius: 16px;
        padding: 20px;
        margin: 15px 0px;
        font-family: 'Share Tech Mono', monospace;
    }
    
    .badge {
        display: inline-block;
        padding: 5px 12px;
        border-radius: 6px;
        font-size: 14px;
        font-weight: bold;
        text-transform: uppercase;
        margin: 5px;
        border: 1px solid;
    }
    .unlocked {
        background: rgba(0, 255, 100, 0.15);
        color: #00ff64;
        border-color: #00ff64;
        box-shadow: 0 0 8px rgba(0, 255, 100, 0.3);
    }
    .locked {
        background: rgba(255, 255, 255, 0.05);
        color: #555;
        border-color: #333;
    }
    
    .stProgress > div > div > div > div {
        background-image: linear-gradient(90deg, #b026ff, #00ffff) !important;
        box-shadow: 0 0 10px #00ffff;
    }
    </style>
""", unsafe_allow_html=True)

# --- 3. DYNAMIC SYSTEM WELCOME ENGINE ---
current_hour = time.localtime().tm_hour
if current_hour < 12:
    greeting = "GOOD MORNING, OPERATOR"
elif current_hour < 18:
    greeting = "GOOD AFTERNOON, OPERATOR"
else:
    greeting = "GOOD EVENING, OPERATOR"

st.markdown(f"<p style='font-family:\"Share Tech Mono\", monospace; color:#00ffff; text-align:center; margin-bottom:0; letter-spacing:3px;'>[ SYSTEM ONLINE // {greeting} ]</p>", unsafe_allow_html=True)
st.markdown("<h1 class='neon-title'>⚡ QUANTUM STEP HUD ⚡</h1>", unsafe_allow_html=True)

# --- 4. SIDEBAR GEAR LOADOUT ---
with st.sidebar:
    st.markdown("<h2 style='color:#00ffff;'>⚙️ BOOT LOADOUT</h2>", unsafe_allow_html=True)
    goal = st.number_input("Set Step Milestone Target", min_value=100, max_value=50000, value=5000, step=500)
    
    st.markdown("---")
    st.markdown("<h3 style='color:#b026ff;'>🎒 WEIGHT MULTIPLIERS</h3>", unsafe_allow_html=True)
    inventory_load = st.selectbox(
        "Equipped Inventory Weight Mod",
        ["Barefoot / Light Rags (1.0x)", "Netherite Armor / Heavy Boots (1.3x)", "Carrying Diamond Stash (1.5x)"]
    )
    
    multiplier = 1.0
    if "1.3x" in inventory_load: multiplier = 1.3
    elif "1.5x" in inventory_load: multiplier = 1.5

# --- 5. THE RADICAL HARDWARE PEDOMETER INTERFACE ---
tracker_html = f"""
<div style="background: rgba(6, 6, 14, 0.85); padding: 25px; border-radius: 16px; text-align: center; font-family: 'Orbitron', sans-serif; border: 2px solid #00ffff; box-shadow: 0 0 20px rgba(0, 255, 255, 0.2), inset 0 0 10px rgba(0, 255, 255, 0.1);">
    <div style="font-size: 11px; color: #00ffff; letter-spacing: 4px; margin-bottom: 5px;">MOTION ENGINE STATUS: <span id="status" style="color: #ff3333; text-shadow: 0 0 8px #ff3333;">STANDBY</span></div>
    
    <div id="step-display" style="font-size: 72px; font-weight: 900; color: #ffffff; margin: 10px 0; text-shadow: 0 0 15px #00ffff, 0 0 30px #b026ff;">{st.session_state.step_memory}</div>
    <div style="font-family: 'Share Tech Mono', monospace; color: #888; font-size: 13px; letter-spacing: 2px; margin-bottom: 15px;">TOTAL MOTION IMPULSES CALIBRATED</div>
    
    <button id="perm-btn" style="padding: 12px 30px; font-size: 14px; font-family: 'Orbitron', sans-serif; font-weight: bold; background: transparent; color: #00ffff; border: 2px solid #00ffff; border-radius: 8px; cursor: pointer; box-shadow: 0 0 10px rgba(0,255,255,0.3); transition: all 0.3s ease;">
        ENGAGE CORE MOTION
    </button>
</div>

<script>
    let pulseCount = {st.session_state.step_memory};
    let baseline = 0;
    const triggerGap = 12.0;
    
    const display = document.getElementById('step-display');
    const button = document.getElementById('perm-btn');
    const systemStatus = document.getElementById('status');

    button.onmouseover = function() { this.style.background = '#00ffff'; this.style.color = '#000'; };
    button.onmouseout = function() { this.style.background = 'transparent'; this.style.color = '#00ffff'; };

    function activeCore() {
        window.addEventListener('devicemotion', (e) => {
            let motion = e.accelerationIncludingGravity;
            if (!motion) return;

            let netForce = Math.sqrt(motion.x*motion.x + motion.y*motion.y + motion.z*motion.z);
            
            if (netForce > triggerGap && baseline <= triggerGap) {
                pulseCount++;
                display.innerText = pulseCount;
                
                if (window.parent && window.parent.postMessage) {
                    window.parent.postMessage({
                        type: 'streamlit:setComponentValue',
                        value: pulseCount
                    }, '*');
                }
            }
            baseline = netForce;
        });
        
        systemStatus.innerText = "ONLINE / CAPTURING";
        systemStatus.style.color = "#00ff64";
        systemStatus.style.textShadow = "0 0 8px #00ff64";
        button.style.display = 'none';
    }

    button.addEventListener('click', () => {
        if (typeof DeviceMotionEvent.requestPermission === 'function') {
            DeviceMotionEvent.requestPermission()
                .then(res => { if (res === 'granted') activeCore(); })
                .catch(console.error);
        } else {
            activeCore();
        }
    });
</script>
"""

# Render JavaScript Core Pedometer
js_data = components.html(tracker_html, height=220)

# If the JavaScript returns a new step number, save it into our memory card
if js_data is not None:
    st.session_state.step_memory = int(js_data)

# Assign current steps safely from memory (guaranteed to be an integer)
current_steps = st.session_state.step_memory

# --- 6. RPG LEVEL & STAT ENGINE ---
if current_steps < 50:
    rank, hex_color, title_desc = "NOOB WALKER 🛑", "#ff3333", "Wake up system parameters..."
elif current_steps < 500:
    rank, hex_color, title_desc = "CASUAL ROAMER 👟", "#ffaa00", "Stepping out into the local world map."
elif current_steps < 1500:
    rank, hex_color, title_desc = "CARDIO SURGEON ⚔️", "#00ffff", "Slicing through distances gracefully."
elif current_steps < 4000:
    rank, hex_color, title_desc = "SPEED RUN CHAMP 🏃‍♂️", "#00ff64", "Breaking local speed records effortlessly."
else:
    rank, hex_color, title_desc = "LIMITLESS GOD 🌀", "#b026ff", "Infinite step capacity reached! Reality warped."

st.markdown(f"""
<div class="glass-card" style="border-color: {hex_color}; box-shadow: 0 0 15px {hex_color}40;">
    <div style="font-size:12px; color:#888; letter-spacing:1px;">CURRENT MATRICULATED RANK</div>
    <div style="font-size:26px; font-weight:bold; color:{hex_color}; font-family:'Orbitron', sans-serif; margin:5px 0;">{rank}</div>
    <div style="font-size:13px; color:#eee; font-style:italic;">"{title_desc}"</div>
</div>
""", unsafe_allow_html=True)

progress_pct = min(float(current_steps) / float(goal), 1.0)
st.progress(progress_pct)
st.markdown(f"<p style='text-align:right; font-family:\"Share Tech Mono\", monospace; color:#00ffff; margin-top:-10px;'>{int(progress_pct*100)}% TOWARD GOAL MAP</p>", unsafe_allow_html=True)

# --- 7. HARDWARE ANALYTICS GRID ---
st.markdown("<h3 style='color:#00ffff; font-size:16px;'>📊 VIRTUAL BIOMETRIC HUD</h3>", unsafe_allow_html=True)

distance_km = (current_steps * 0.6) / 1000  
calories_base = current_steps * 0.04 * multiplier

col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="📊 Step Registry", value=f"{current_steps} / {goal}")
with col2:
    st.metric(label="🚀 Projected Range", value=f"{distance_km:.3f} KM")
with col3:
    st.metric(label="🔥 Energy Vented", value=f"{calories_base:.1f} kCal")

# --- 8. ADVANCED INTERACTIVE ADAPTING DECORATIONS ---
st.markdown("""
<div class="glass-card">
    <div style="color:#00ffff; font-size:14px; margin-bottom:10px; font-weight:bold; letter-spacing:1px;">🍔 FOOD CALORIE DEEP BURN DATA</div>
""", unsafe_allow_html=True)

pizza_slices = calories_base / 250
diamond_swords_crafted = current_steps // 100

st.write(f"🔹 **Pizza Slices vaporized:** `{pizza_slices:.2f}` slices fully burned away.")
st.write(f"🔹 **Energy generated:** Enough kinetic force to forge `{diamond_swords_crafted}` Diamond Swords.")
st.markdown("</div>", unsafe_allow_html=True)

st.markdown("""
<div class="glass-card">
    <div style="color:#b026ff; font-size:14px; margin-bottom:10px; font-weight:bold; letter-spacing:1px;">🏆 ACHIEVEMENT TIER VAULT</div>
""", unsafe_allow_html=True)

b1 = "unlocked" if current_steps >= 1 else "locked"
b2 = "unlocked" if current_steps >= 100 else "locked"
b3 = "unlocked" if current_steps >= 1000 else "locked"
b4 = "unlocked" if current_steps >= goal else "locked"

st.markdown(f"""
    <span class="badge {b1}">⚡ First Spark</span>
    <span class="badge {b2}">👟 Century Strider</span>
    <span class="badge {b3}">🏃‍♂️ Dungeon Runner</span>
    <span class="badge {b4}">👑 Hollow Victor</span>
</div>
""", unsafe_allow_html=True)

if current_steps >= goal:
    st.balloons()
    st.markdown("""
    <div style="background:rgba(0,255,100,0.1); border:2px dashed #00ff64; border-radius:12px; padding:15px; text-align:center; color:#00ff64; font-family:'Orbitron',sans-serif; margin-top:20px; box-shadow: 0 0 15px rgba(0,255,100,0.2);">
        🎉 MAXIMUM CHRONO QUEST COMPLETE! CAP OVERRIDE ACHIEVED! 🎉
    </div>
    """, unsafe_allow_html=True)