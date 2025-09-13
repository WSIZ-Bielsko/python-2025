from python_2025.aircraft.model import AircraftPart


def create_aircraft0(part_db: dict[int, AircraftPart]) -> AircraftPart:
    all_parts = [
        AircraftPart(id=1, name='Gulfstream G650ER', flights_since_overhaul=100, hours_since_overhaul=1500, max_flights=5000,
                     max_hours=15000, subparts=[2, 3, 4]),
        AircraftPart(id=2, name='Engine System', flights_since_overhaul=100, hours_since_overhaul=1500, max_flights=2000,
                     max_hours=8000, subparts=[5, 6]),
        AircraftPart(id=3, name='Avionics System', flights_since_overhaul=50, hours_since_overhaul=500, max_flights=10000,
                     max_hours=10000, subparts=[7, 8]),
        AircraftPart(id=4, name='Landing Gear System', flights_since_overhaul=30, hours_since_overhaul=700, max_flights=1500,
                     max_hours=6000, subparts=[9, 10]),
        AircraftPart(id=5, name='Turbofan Engine', flights_since_overhaul=100, hours_since_overhaul=1500, max_flights=2000,
                     max_hours=8000, subparts=[11, 12]),
        AircraftPart(id=6, name='Fuel System', flights_since_overhaul=90, hours_since_overhaul=1200, max_flights=2000,
                     max_hours=5000, subparts=[13]),
        AircraftPart(id=7, name='Flight Control Computer', flights_since_overhaul=50, hours_since_overhaul=500, max_flights=10000,
                     max_hours=10000, subparts=[]),
        AircraftPart(id=8, name='Navigation System', flights_since_overhaul=50, hours_since_overhaul=500, max_flights=10000,
                     max_hours=10000, subparts=[]),
        AircraftPart(id=9, name='Main Landing Gear', flights_since_overhaul=30, hours_since_overhaul=700, max_flights=1500,
                     max_hours=6000, subparts=[14]),
        AircraftPart(id=10, name='Nose Landing Gear', flights_since_overhaul=25, hours_since_overhaul=600, max_flights=1500,
                     max_hours=6000, subparts=[]),
        AircraftPart(id=11, name='Compressor', flights_since_overhaul=80, hours_since_overhaul=1200, max_flights=2000,
                     max_hours=8000, subparts=[]),
        AircraftPart(id=12, name='Turbine', flights_since_overhaul=80, hours_since_overhaul=1200, max_flights=2000,
                     max_hours=8000, subparts=[]),
        AircraftPart(id=13, name='Fuel Pump', flights_since_overhaul=90, hours_since_overhaul=1200, max_flights=2000,
                     max_hours=5000, subparts=[]),
        AircraftPart(id=14, name='Shock Absorber', flights_since_overhaul=30, hours_since_overhaul=700, max_flights=1500,
                     max_hours=6000, subparts=[])
    ]
    offset = 500
    for part in all_parts:
        part.id += offset
        part_db[part.id] = part
        part.subparts = [pid + offset for pid in part.subparts]

    return all_parts[0]




def create_aircraft(part_db: dict[int, AircraftPart]) -> AircraftPart:
    # Level 1: Main Aircraft
    aircraft = AircraftPart(
        id=1,
        name="Boeing 737-800 Airframe",
        flights_since_overhaul=1250,
        hours_since_overhaul=2100,
        max_flights=25000,
        max_hours=60000,
        subparts=[2, 3, 4, 5]
    )

    # Level 2: Major Systems
    engine_left = AircraftPart(
        id=2,
        name="CFM56-7B Left Engine",
        flights_since_overhaul=850,
        hours_since_overhaul=1400,
        max_flights=15000,
        max_hours=25000,
        subparts=[6, 7, 8]
    )

    engine_right = AircraftPart(
        id=3,
        name="CFM56-7B Right Engine",
        flights_since_overhaul=780,
        hours_since_overhaul=1350,
        max_flights=15000,
        max_hours=25000,
        subparts=[9, 10, 11]
    )

    landing_gear = AircraftPart(
        id=4,
        name="Main Landing Gear Assembly",
        flights_since_overhaul=2300,
        hours_since_overhaul=3800,
        max_flights=12000,
        max_hours=20000,
        subparts=[12, 13, 14]
    )

    avionics = AircraftPart(
        id=5,
        name="Flight Management System",
        flights_since_overhaul=450,
        hours_since_overhaul=750,
        max_flights=8000,
        max_hours=15000,
        subparts=[15, 16]
    )

    # Level 3: Engine Components
    turbine_left = AircraftPart(
        id=6,
        name="High Pressure Turbine - Left",
        flights_since_overhaul=850,
        hours_since_overhaul=1400,
        max_flights=8000,
        max_hours=12000,
        subparts=[17, 18]
    )

    compressor_left = AircraftPart(
        id=7,
        name="High Pressure Compressor - Left",
        flights_since_overhaul=850,
        hours_since_overhaul=1400,
        max_flights=10000,
        max_hours=15000,
        subparts=[19]
    )

    fuel_system_left = AircraftPart(
        id=8,
        name="Fuel Control Unit - Left",
        flights_since_overhaul=320,
        hours_since_overhaul=520,
        max_flights=5000,
        max_hours=8000,
        subparts=[20]
    )

    turbine_right = AircraftPart(
        id=9,
        name="High Pressure Turbine - Right",
        flights_since_overhaul=780,
        hours_since_overhaul=1350,
        max_flights=8000,
        max_hours=12000,
        subparts=[21, 22]
    )

    compressor_right = AircraftPart(
        id=10,
        name="High Pressure Compressor - Right",
        flights_since_overhaul=780,
        hours_since_overhaul=1350,
        max_flights=10000,
        max_hours=15000,
        subparts=[23]
    )

    fuel_system_right = AircraftPart(
        id=11,
        name="Fuel Control Unit - Right",
        flights_since_overhaul=290,
        hours_since_overhaul=480,
        max_flights=5000,
        max_hours=8000,
        subparts=[24]
    )

    # Level 3: Landing Gear Components
    main_strut = AircraftPart(
        id=12,
        name="Main Landing Gear Strut",
        flights_since_overhaul=2300,
        hours_since_overhaul=3800,
        max_flights=12000,
        max_hours=20000,
        subparts=[25]
    )

    brake_assembly = AircraftPart(
        id=13,
        name="Brake Assembly",
        flights_since_overhaul=890,
        hours_since_overhaul=1450,
        max_flights=3000,
        max_hours=5000,
        subparts=[26]
    )

    tire_assembly = AircraftPart(
        id=14,
        name="Main Tire Assembly",
        flights_since_overhaul=180,
        hours_since_overhaul=290,
        max_flights=300,
        max_hours=500,
        subparts=[27]
    )

    # Level 3: Avionics Components
    autopilot = AircraftPart(
        id=15,
        name="Autopilot Computer",
        flights_since_overhaul=450,
        hours_since_overhaul=750,
        max_flights=8000,
        max_hours=15000,
        subparts=[28]
    )

    navigation = AircraftPart(
        id=16,
        name="Inertial Navigation Unit",
        flights_since_overhaul=650,
        hours_since_overhaul=1080,
        max_flights=6000,
        max_hours=10000,
        subparts=[29]
    )

    # Level 4: Detailed Components (deepest level)
    turbine_blades_left_hp = AircraftPart(
        id=17,
        name="HP Turbine Blades Set 1 - Left",
        flights_since_overhaul=850,
        hours_since_overhaul=1400,
        max_flights=4000,
        max_hours=6000,
        subparts=[]
    )

    turbine_nozzles_left = AircraftPart(
        id=18,
        name="Turbine Nozzle Guide Vanes - Left",
        flights_since_overhaul=850,
        hours_since_overhaul=1400,
        max_flights=6000,
        max_hours=9000,
        subparts=[]
    )

    compressor_blades_left = AircraftPart(
        id=19,
        name="Compressor Blade Set - Left",
        flights_since_overhaul=850,
        hours_since_overhaul=1400,
        max_flights=8000,
        max_hours=12000,
        subparts=[]
    )

    fuel_nozzles_left = AircraftPart(
        id=20,
        name="Fuel Injection Nozzles - Left",
        flights_since_overhaul=320,
        hours_since_overhaul=520,
        max_flights=2500,
        max_hours=4000,
        subparts=[]
    )

    turbine_blades_right_hp = AircraftPart(
        id=21,
        name="HP Turbine Blades Set 1 - Right",
        flights_since_overhaul=780,
        hours_since_overhaul=1350,
        max_flights=4000,
        max_hours=6000,
        subparts=[]
    )

    turbine_nozzles_right = AircraftPart(
        id=22,
        name="Turbine Nozzle Guide Vanes - Right",
        flights_since_overhaul=780,
        hours_since_overhaul=1350,
        max_flights=6000,
        max_hours=9000,
        subparts=[]
    )

    compressor_blades_right = AircraftPart(
        id=23,
        name="Compressor Blade Set - Right",
        flights_since_overhaul=780,
        hours_since_overhaul=1350,
        max_flights=8000,
        max_hours=12000,
        subparts=[]
    )

    fuel_nozzles_right = AircraftPart(
        id=24,
        name="Fuel Injection Nozzles - Right",
        flights_since_overhaul=290,
        hours_since_overhaul=480,
        max_flights=2500,
        max_hours=4000,
        subparts=[]
    )

    shock_strut = AircraftPart(
        id=25,
        name="Oleo-Pneumatic Shock Strut",
        flights_since_overhaul=2300,
        hours_since_overhaul=3800,
        max_flights=12000,
        max_hours=20000,
        subparts=[]
    )

    brake_discs = AircraftPart(
        id=26,
        name="Carbon Brake Discs",
        flights_since_overhaul=890,
        hours_since_overhaul=1450,
        max_flights=1500,
        max_hours=2500,
        subparts=[]
    )

    tire_rubber = AircraftPart(
        id=27,
        name="Radial Tire Assembly",
        flights_since_overhaul=180,
        hours_since_overhaul=290,
        max_flights=300,
        max_hours=500,
        subparts=[]
    )

    autopilot_processor = AircraftPart(
        id=28,
        name="Flight Control Processor Unit",
        flights_since_overhaul=450,
        hours_since_overhaul=750,
        max_flights=8000,
        max_hours=15000,
        subparts=[]
    )

    gyroscope = AircraftPart(
        id=29,
        name="Laser Ring Gyroscope",
        flights_since_overhaul=650,
        hours_since_overhaul=1080,
        max_flights=6000,
        max_hours=10000,
        subparts=[]
    )

    # Create a list of all parts for easy access
    all_parts: list[AircraftPart] = [
        aircraft, engine_left, engine_right, landing_gear, avionics,
        turbine_left, compressor_left, fuel_system_left,
        turbine_right, compressor_right, fuel_system_right,
        main_strut, brake_assembly, tire_assembly, autopilot, navigation,
        turbine_blades_left_hp, turbine_nozzles_left, compressor_blades_left, fuel_nozzles_left,
        turbine_blades_right_hp, turbine_nozzles_right, compressor_blades_right, fuel_nozzles_right,
        shock_strut, brake_discs, tire_rubber, autopilot_processor, gyroscope
    ]

    for part in all_parts:
        part_db[part.id] = part

    return aircraft


def create_aircraft2(part_db: dict[int, AircraftPart]):
    # Level 1: Main Aircraft
    aircraft_2 = AircraftPart(
        id=100,
        name="Airbus A320neo Airframe",
        flights_since_overhaul=890,
        hours_since_overhaul=1650,
        max_flights=30000,
        max_hours=70000,
        subparts=[101, 102, 103, 104, 105]
    )

    # Level 2: Major Systems
    engine_left_2 = AircraftPart(
        id=101,
        name="LEAP-1A Left Engine",
        flights_since_overhaul=650,
        hours_since_overhaul=1200,
        max_flights=18000,
        max_hours=30000,
        subparts=[106, 107, 108]
    )

    engine_right_2 = AircraftPart(
        id=102,
        name="LEAP-1A Right Engine",
        flights_since_overhaul=720,
        hours_since_overhaul=1320,
        max_flights=18000,
        max_hours=30000,
        subparts=[109, 110, 111]
    )

    apu_system = AircraftPart(
        id=103,
        name="Auxiliary Power Unit",
        flights_since_overhaul=1200,
        hours_since_overhaul=2200,
        max_flights=8000,
        max_hours=15000,
        subparts=[112, 113]
    )

    hydraulic_system = AircraftPart(
        id=104,
        name="Primary Hydraulic System",
        flights_since_overhaul=1850,
        hours_since_overhaul=3400,
        max_flights=10000,
        max_hours=18000,
        subparts=[114, 115, 116]
    )

    flight_controls = AircraftPart(
        id=105,
        name="Fly-by-Wire Flight Controls",
        flights_since_overhaul=340,
        hours_since_overhaul=620,
        max_flights=12000,
        max_hours=22000,
        subparts=[117, 118]
    )

    # Level 3: Engine Components
    fan_assembly_left = AircraftPart(
        id=106,
        name="Fan Assembly - Left",
        flights_since_overhaul=650,
        hours_since_overhaul=1200,
        max_flights=12000,
        max_hours=18000,
        subparts=[119, 120]
    )

    combustion_chamber_left = AircraftPart(
        id=107,
        name="Combustion Chamber - Left",
        flights_since_overhaul=650,
        hours_since_overhaul=1200,
        max_flights=6000,
        max_hours=10000,
        subparts=[121]
    )

    exhaust_system_left = AircraftPart(
        id=108,
        name="Exhaust Nozzle Assembly - Left",
        flights_since_overhaul=650,
        hours_since_overhaul=1200,
        max_flights=15000,
        max_hours=22000,
        subparts=[122]
    )

    fan_assembly_right = AircraftPart(
        id=109,
        name="Fan Assembly - Right",
        flights_since_overhaul=720,
        hours_since_overhaul=1320,
        max_flights=12000,
        max_hours=18000,
        subparts=[123, 124]
    )

    combustion_chamber_right = AircraftPart(
        id=110,
        name="Combustion Chamber - Right",
        flights_since_overhaul=720,
        hours_since_overhaul=1320,
        max_flights=6000,
        max_hours=10000,
        subparts=[125]
    )

    exhaust_system_right = AircraftPart(
        id=111,
        name="Exhaust Nozzle Assembly - Right",
        flights_since_overhaul=720,
        hours_since_overhaul=1320,
        max_flights=15000,
        max_hours=22000,
        subparts=[126]
    )

    # Level 3: APU Components
    apu_turbine = AircraftPart(
        id=112,
        name="APU Turbine Section",
        flights_since_overhaul=1200,
        hours_since_overhaul=2200,
        max_flights=5000,
        max_hours=9000,
        subparts=[127]
    )

    apu_generator = AircraftPart(
        id=113,
        name="APU Generator Unit",
        flights_since_overhaul=980,
        hours_since_overhaul=1800,
        max_flights=8000,
        max_hours=15000,
        subparts=[128]
    )

    # Level 3: Hydraulic Components
    hydraulic_pump = AircraftPart(
        id=114,
        name="Engine Driven Hydraulic Pump",
        flights_since_overhaul=1850,
        hours_since_overhaul=3400,
        max_flights=7000,
        max_hours=12000,
        subparts=[129]
    )

    hydraulic_filter = AircraftPart(
        id=115,
        name="Hydraulic Return Filter",
        flights_since_overhaul=420,
        hours_since_overhaul=770,
        max_flights=2000,
        max_hours=3500,
        subparts=[]
    )

    hydraulic_accumulator = AircraftPart(
        id=116,
        name="Hydraulic Pressure Accumulator",
        flights_since_overhaul=1850,
        hours_since_overhaul=3400,
        max_flights=10000,
        max_hours=18000,
        subparts=[]
    )

    # Level 3: Flight Control Components
    elevator_actuator = AircraftPart(
        id=117,
        name="Elevator Servo Actuator",
        flights_since_overhaul=340,
        hours_since_overhaul=620,
        max_flights=8000,
        max_hours=14000,
        subparts=[]
    )

    aileron_computer = AircraftPart(
        id=118,
        name="Aileron Control Computer",
        flights_since_overhaul=340,
        hours_since_overhaul=620,
        max_flights=12000,
        max_hours=22000,
        subparts=[]
    )

    # Level 4: Detailed Components (deepest level)
    fan_blades_left = AircraftPart(
        id=119,
        name="Fan Blade Set - Left",
        flights_since_overhaul=650,
        hours_since_overhaul=1200,
        max_flights=8000,
        max_hours=12000,
        subparts=[]
    )

    fan_case_left = AircraftPart(
        id=120,
        name="Fan Case Assembly - Left",
        flights_since_overhaul=650,
        hours_since_overhaul=1200,
        max_flights=12000,
        max_hours=18000,
        subparts=[]
    )

    combustor_liner_left = AircraftPart(
        id=121,
        name="Combustor Liner - Left",
        flights_since_overhaul=650,
        hours_since_overhaul=1200,
        max_flights=3000,
        max_hours=5000,
        subparts=[]
    )

    thrust_reverser_left = AircraftPart(
        id=122,
        name="Thrust Reverser Cascade - Left",
        flights_since_overhaul=650,
        hours_since_overhaul=1200,
        max_flights=12000,
        max_hours=18000,
        subparts=[]
    )

    fan_blades_right = AircraftPart(
        id=123,
        name="Fan Blade Set - Right",
        flights_since_overhaul=720,
        hours_since_overhaul=1320,
        max_flights=8000,
        max_hours=12000,
        subparts=[]
    )

    fan_case_right = AircraftPart(
        id=124,
        name="Fan Case Assembly - Right",
        flights_since_overhaul=720,
        hours_since_overhaul=1320,
        max_flights=12000,
        max_hours=18000,
        subparts=[]
    )

    combustor_liner_right = AircraftPart(
        id=125,
        name="Combustor Liner - Right",
        flights_since_overhaul=720,
        hours_since_overhaul=1320,
        max_flights=3000,
        max_hours=5000,
        subparts=[]
    )

    thrust_reverser_right = AircraftPart(
        id=126,
        name="Thrust Reverser Cascade - Right",
        flights_since_overhaul=720,
        hours_since_overhaul=1320,
        max_flights=12000,
        max_hours=18000,
        subparts=[]
    )

    apu_compressor = AircraftPart(
        id=127,
        name="APU Centrifugal Compressor",
        flights_since_overhaul=1200,
        hours_since_overhaul=2200,
        max_flights=5000,
        max_hours=9000,
        subparts=[]
    )

    generator_rotor = AircraftPart(
        id=128,
        name="Generator Rotor Assembly",
        flights_since_overhaul=980,
        hours_since_overhaul=1800,
        max_flights=8000,
        max_hours=15000,
        subparts=[]
    )

    pump_impeller = AircraftPart(
        id=129,
        name="Hydraulic Pump Impeller",
        flights_since_overhaul=1850,
        hours_since_overhaul=3400,
        max_flights=7000,
        max_hours=12000,
        subparts=[]
    )

    # Create a list of all parts for the second aircraft
    all_parts_2 = [
        aircraft_2, engine_left_2, engine_right_2, apu_system, hydraulic_system, flight_controls,
        fan_assembly_left, combustion_chamber_left, exhaust_system_left,
        fan_assembly_right, combustion_chamber_right, exhaust_system_right,
        apu_turbine, apu_generator, hydraulic_pump, hydraulic_filter, hydraulic_accumulator,
        elevator_actuator, aileron_computer,
        fan_blades_left, fan_case_left, combustor_liner_left, thrust_reverser_left,
        fan_blades_right, fan_case_right, combustor_liner_right, thrust_reverser_right,
        apu_compressor, generator_rotor, pump_impeller
    ]

    for part in all_parts_2:
        part_db[part.id] = part

    return aircraft_2


def display_aircraft(part_db: dict[int, AircraftPart], part: AircraftPart, level: int) -> None:
    print(f'{"    " * level}LV={level}, name={part.name} ({part.id})')
    for part_id in part.subparts:
        display_aircraft(part_db, part_db[part_id], level + 1)


def count_parts(part_db: dict[int, AircraftPart], part: AircraftPart) -> int:
    num_parts = 1
    for part_id in part.subparts:
        num_parts += count_parts(part_db, part_db[part_id])
    return num_parts


def min_hours_left(part_db: dict[int, AircraftPart], part: AircraftPart) -> int:
    difference = list()
    difference.append(part.max_hours - part.hours_since_overhaul)
    print(f'{part.id} - {part.name}: {difference}')
    for part_id in part.subparts:
        difference.append(min_hours_left(part_db, part_db[part_id]))
    return min(difference)

if __name__ == '__main__':
    all_parts: dict[int, AircraftPart] = dict()
    aircraft1 = create_aircraft0(part_db=all_parts)
    # aircraft2 = create_aircraft2(part_db=all_parts)
    display_aircraft(all_parts, aircraft1, level=0)
    # print(f'parts in aircraft1: {count_parts(all_parts, aircraft1)}')
    # print(f'min hours left for aircraft1: {min_hours_left(all_parts, aircraft1)}')
    # print('-------')
    # display_aircraft(all_parts, aircraft2, level=0)
    # print(f'parts in aircraft1: {count_parts(all_parts, aircraft2)}')
    # print(f'min hours left for aircraft2: {min_hours_left(all_parts, aircraft2)}')
    print(f'min_hours_left for aircraft0: {min_hours_left(all_parts, aircraft1)}')