import minimalmodbus

SERPORT = 'COM4'
SERTIMEOUT = 0.5
SERBAUD = 19200

# Registers to retrieve data for
register_map = {
    10102 : ["XX voltage", 0.1, "V"],
    10103 : ["Float voltage", 0.1, "V"],
    10104 : ["Absorb voltage", 0.1, "V"],
    10105 : ["Battery low voltage", 0.1, "V"],
    10107 : ["Battery high voltage", 0.1, "V"],
    10108 : ["Max charger current", 0.1, "A"],
    10109 : ["Absorb charger current", 0.1, "A"],
    10110 : ["Battery type", 1, "map", {
        0 : "",
        1 : "User defined battery",
        2 : "Lithium battery",
        3 : "SEALED_LEAD  battery",
        4 : "AGM battery",
        5 : "GEL battery",
        6 : "FLOODED battery"}],

    15201 : ["Charger workstate", 1, "map", {
        0 : "Initialization mode",
        1 : "Selftest Mode",
        2 : "Work Mode",
        3 : "Stop Mode"}],
    15202 : ["MPPT state", 1, "map", {
        0 : "Stop",
        1 : "MPPT",
        2 : "Current limiting"}],
    15203 : ["Charging state", 1, "map", {
        0 : "Stop",
        1 : "Absorb charge",
        2 : "Float charge"}],
    15205 : ["PV voltage", 0.1, "V"],
    15206 : ["Battery voltage", 0.1, "V"],
    15207 : ["Charger current", 0.1, "A"],
    15208 : ["Charger power", 0.1, "W"],
    # 15209 : ["Radiator temperature", 1, "°C"],
    # 15210 : ["External temperature", 1, "°C"],
    15211 : ["Battery Relay", 1, ""],
    15212 : ["PV Relay", 1, ""],

    20109 : ["Energy use mode", 1, "map", {
        0 : "",
        1 : "SBU",
        2 : "SUB",
        3 : "UTI",
        4 : "SOL"}],
    20112 : ["SolarUse Aim", 1, "map", {
        0 : "LBU",
        1 : "BLU"}],
    20113 : ["Inverter max discharger current", 1, "A"],
    
    20125 : ["Grid max charger current set", 0.1, "A"],
    20143 : ["Charger source priority", 1, " mode"],
    25201 : ["Work state", 1, "map", {
        0 : "PowerOn",
        1 : "SelfTest",
        2 : "OffGrid",
        3 : "Grid-Tie",
        4 : "Bypass",
        5 : "Stop",
        6 : "Grid Charging"}],
    # 25202 : ["AcVoltageGrade", 1, "V"],
    # 25203 : ["RatedPower", 1, "W"],
    25205 : ["Battery voltage", 0.1, "V"],
    25206 : ["Inverter voltage", 0.1, "V"],
    25207 : ["Grid voltage", 0.1, "V"],
    25208 : ["BUS voltage", 0.1, "V"],
    25209 : ["Control current", 0.1, "A"],
    25210 : ["Inverter current", 0.1, "A"],
    25211 : ["Grid current", 0.1, "A"],
    25212 : ["Load current", 0.1, "A"],
    25213 : ["Inverter power(P)", 1, "W"],
    25214 : ["Grid power(P)", 1, "W"],
    25215 : ["Load power(P)", 1, "W"],
    25216 : ["Load percent", 1, "%"],
    25217 : ["Inverter complex power(S)", 1, "VA"],
    25218 : ["Grid complex power(S)", 1, "VA"],
    25219 : ["Load complex power(S)", 1, "VA"],
    25221 : ["Inverter reactive power(Q)", 1, "var"],
    25222 : ["Grid reactive power(Q)", 1, "var"],
    25223 : ["Load reactive power(Q)", 1, "var"],
    25225 : ["Inverter frequency", 0.01, "Hz"],
    25226 : ["Grid frequency", 0.01, "Hz"],
    25233 : ["AC radiator temperature", 1, "°C"],
    25234 : ["Transformer temperature", 1, "°C"],
    25235 : ["DC radiator temperature", 1, "°C"],
    25237 : ["Inverter relay state", 1, ""],
    25238 : ["Grid relay state", 1, ""],
    25239 : ["Load relay state", 1, ""],
    25240 : ["N_Line relay state", 1, ""],
    25241 : ["DC relay state", 1, ""],
    25242 : ["Earth relay state", 1, ""],
    25245 : ["Accumulated charger power high", 1, "kWh"],
    25246 : ["Accumulated charger power low", 0.1, "kWh"],
    25247 : ["Accumulated discharger power high", 1, "kWh"],
    25248 : ["Accumulated discharger power low", 0.1, "kWh"],
    25249 : ["Accumulated buy power high", 1, "kWh"],
    25250 : ["Accumulated buy power low", 0.1, "kWh"],
    25251 : ["Accumulated sell power high", 1, "kWh"],
    25252 : ["Accumulated sell power low", 0.1, "kWh"],
    25253 : ["Accumulated load power high", 1, "kWh"],
    25254 : ["Accumulated load power low", 0.1, "kWh"],
    25255 : ["Accumulated self_use power high", 1, "kWh"],
    25256 : ["Accumulated self_use power low", 0.1, "kWh"],
    25257 : ["Accumulated PV_sell power high", 1, "kWh"],
    25258 : ["Accumulated PV_sell power low", 0.1, "kWh"],
    25259 : ["Accumulated grid_charger power high", 1, "kWh"],
    25260 : ["Accumulated grid_charger power low", 0.1, "kWh"],
    25271 : ["Hardware version", 1, ""],
    25272 : ["Software version", 1, ""],
    25273 : ["Battery power", 1, "W"],
    25274 : ["Battery current", 1, "A"],
}

def read_register_values(i, startreg, count):
    register_id = startreg
    results = i.read_registers(startreg, count)
    for r in results:
        if register_id in register_map:
            r_name = register_map[register_id][0] # Name
            if register_map[register_id][2] == "map": # Mapped value
                r_value = register_map[register_id][3][r]
            else: # Unit value
                r_value = str(r*register_map[register_id][1])+register_map[register_id][2]
            print(str(r_name) + " = " + r_value)
        register_id += 1

i = minimalmodbus.Instrument(SERPORT, 4)
i.serial.timeout=SERTIMEOUT
i.serial.baudrate = SERBAUD
print("--------------- CHARGER ---------------")
read_register_values(i, 15201, 12)
print("--------------- INVERTER ---------------")
read_register_values(i, 25201, 74)
print("--------------- SETTINGS ---------------")
read_register_values(i, 10102, 10)
read_register_values(i, 20109, 5)


