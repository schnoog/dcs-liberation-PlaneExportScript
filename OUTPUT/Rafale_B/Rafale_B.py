from enum import Enum

from dcs import task
from dcs.planes import PlaneType
from dcs.weapons_data import Weapons

from pydcs_extensions.weapon_injector import inject_weapons




class WeaponsRafale_B:
    _3_Mk_20_Rockeye = {"clsid": "{B83CB620-5BBE-4BEA-910C-EB605A327EF9}", "name": "3 Mk-20 Rockeye", "weight": 726}
    _3_Mk_82 = {"clsid": "{60CC734F-0AFA-4E2E-82B8-93B941AB11CF}", "name": "3 Mk-82", "weight": 783}
    AASM_250_L = {"clsid": "{AASM_250_L}", "name": "AASM_250_L", "weight": 500}
    AASM_250_R = {"clsid": "{AASM_250_R}", "name": "AASM_250_R", "weight": 500}
    AGM_88C_ = {"clsid": "{B06DD79A-F21E-4EB9-BD9D-AB3844618C93}", "name": "AGM-88C", "weight": 361}
    AIM_9M_Sidewinder_IR_AAM = {"clsid": "{6CEB49FC-DED8-4DED-B053-E1F033FF72D3}", "name": "AIM-9M Sidewinder IR AAM", "weight": 86.64}
    AIM_9P_Sidewinder_IR_AAM = {"clsid": "{9BFD8C90-F7AE-4e90-833B-BFD0CED0E536}", "name": "AIM-9P Sidewinder IR AAM", "weight": 86.18}
    AN_AAQ_28_LITENING = {"clsid": "{A111396E-D3E8-4b9c-8AC9-2432489304D5}", "name": "AN/AAQ-28 LITENING", "weight": 300}
    AS_30L = {"clsid": "{AS_30L}", "name": "AS_30L", "weight": 292}
    Exocet = {"clsid": "{Exocet}", "name": "Exocet", "weight": 640}
    GBU_49 = {"clsid": "{GBU_49}", "name": "GBU_49", "weight": 525}
    GBU12PII = {"clsid": "{GBU12PII}", "name": "GBU12PII", "weight": 525}
    gbu12X2_L = {"clsid": "{gbu12X2_L}", "name": "gbu12X2_L", "weight": 525}
    gbu12X2_R = {"clsid": "{gbu12X2_R}", "name": "gbu12X2_R", "weight": 525}
    gbu12X3_L = {"clsid": "{gbu12X3_L}", "name": "gbu12X3_L", "weight": 525}
    gbu12X3_R = {"clsid": "{gbu12X3_R}", "name": "gbu12X3_R", "weight": 525}
    gbu24 = {"clsid": "{gbu24}", "name": "gbu24", "weight": 1000}
    LAU_10___4_ZUNI_MK_71 = {"clsid": "{F3EFE0AB-E91A-42D8-9CA2-B63C91ED570A}", "name": "LAU-10 - 4 ZUNI MK 71", "weight": 440}
    LAU_131___7_2_75__rockets_M151__HE_ = {"clsid": "{69926055-0DA8-4530-9F2F-C86B157EA9F6}", "name": "LAU-131 - 7 2.75' rockets M151 (HE)", "weight": 102.3}
    LAU_131x3_HYDRA_70_M151 = {"clsid": "LAU_131x3_HYDRA_70_M151", "name": "LAU-131*3 - 7 2.75' rockets M151 (HE)", "weight": 357.7}
    LAU_61___19_2_75__rockets_MK151_HE = {"clsid": "{FD90A1DC-9147-49FA-BF56-CB83EF0BD32B}", "name": "LAU-61 - 19 2.75' rockets MK151 HE", "weight": 290.59}
    LAU3_HE151 = {"clsid": "LAU3_HE151", "name": "LAU-3 - 19 2.75' rockets MK151 HE", "weight": 234}
    LAU3_HE5 = {"clsid": "LAU3_HE5", "name": "LAU-3 - 19 2.75' rockets MK5 HEAT", "weight": 234}
    LAU3_WP156 = {"clsid": "LAU3_WP156", "name": "LAU-3 - 19 2.75' rockets MK156 WP", "weight": 234}
    MER_2_MK_82 = {"clsid": "{D5D51E24-348C-4702-96AF-97A714E72697}", "name": "MER*2 MK-82", "weight": 200}
    MER_2_MK_83 = {"clsid": "{18617C93-78E7-4359-A8CE-D754103EDF63}", "name": "MER*2 MK-83", "weight": 200}
    Mercury_LLTV_Pod = {"clsid": "{B1EF6B0E-3D91-4047-A7A5-A99E7D8B4A8B}", "name": "Mercury LLTV Pod", "weight": 230}
    MICA_IR = {"clsid": "{0DA03783-61E4-40B2-8FAE-6AEE0A5C5AAE}", "name": "MICA IR", "weight": 110}
    mk_84 = {"clsid": "{mk_84}", "name": "mk_84", "weight": 1000}
    R_550_Magic_2 = {"clsid": "{FC23864E-3B80-48E3-9C03-4DA8B1D7497B}", "name": "R.550 Magic 2", "weight": 89}
    RAF_RPL711 = {"clsid": "{RAF_RPL711}", "name": "RAF_RPL711", "weight": 820}
    RAF_RPL751 = {"clsid": "{RAF_RPL751}", "name": "RAF_RPL751", "weight": 1450}
    SCALP = {"clsid": "{SCALP}", "name": "SCALP", "weight": None}
    Smokewinder___blue_smk = {"clsid": "{A4BCC903-06C8-47bb-9937-A30FEDB4E743}", "name": "Smokewinder - blue_smk", "weight": 200}
    Smokewinder___green = {"clsid": "{A4BCC903-06C8-47bb-9937-A30FEDB4E742}", "name": "Smokewinder - green", "weight": 200}
    Smokewinder___orange = {"clsid": "{A4BCC903-06C8-47bb-9937-A30FEDB4E746}", "name": "Smokewinder - orange", "weight": 200}
    Smokewinder___red_smk = {"clsid": "{A4BCC903-06C8-47bb-9937-A30FEDB4E741}", "name": "Smokewinder - red_smk", "weight": 200}
    Smokewinder___white = {"clsid": "{A4BCC903-06C8-47bb-9937-A30FEDB4E744}", "name": "Smokewinder - white", "weight": 200}
    Smokewinder___yellow = {"clsid": "{A4BCC903-06C8-47bb-9937-A30FEDB4E745}", "name": "Smokewinder - yellow", "weight": 200}
    TALIOS_THALES = {"clsid": "{TALIOS_THALES}", "name": "TALIOS_THALES", "weight": 265}
    Thales_RBE2 = {"clsid": "{Thales_RBE2}", "name": "Thales_RBE2", "weight": 1.4789}


inject_weapons(WeaponsRafale_B)


class Rafale_B(PlaneType):
    id = "Rafale_B"
    flyable = True
    height = 5.2
    width = 10.86
    length = 14.36
    fuel_max = 3165
    max_speed = 2376
    chaff = 48
    flare = 48
    charge_total = 96
    chaff_charge_size = 1
    flare_charge_size = 1
    category = "Interceptor"  #{78EFB7A2-FD52-4b57-A6A6-3BF0E1D6555F}
    radio_frequency = 127.5

    class Liveries:

        class USSR(Enum):
            _01_rafale_b_lafayette = "01 rafale b lafayette"
            _02_rafale_b_mt_de_marsan = "02 rafale b mt de marsan"
            _03_rafale_b_qatar = "03 rafale b qatar"
            _04_rafale_b_egypte = "04 rafale b egypte"
            _05_rafale_b_inde = "05 rafale b inde"
            _06_rafale_b_grece = "06 rafale b grece"
            _07_rafale_b_croatia = "07 rafale b croatia"
            _08_rafale_b_export = "08 rafale b export"
            _09_rafale_b_india_air_force = "09 rafale b india air force"
            _10_tiger_meet_2009 = "10 tiger meet 2009"

        class Georgia(Enum):
            _01_rafale_b_lafayette = "01 rafale b lafayette"
            _02_rafale_b_mt_de_marsan = "02 rafale b mt de marsan"
            _03_rafale_b_qatar = "03 rafale b qatar"
            _04_rafale_b_egypte = "04 rafale b egypte"
            _05_rafale_b_inde = "05 rafale b inde"
            _06_rafale_b_grece = "06 rafale b grece"
            _07_rafale_b_croatia = "07 rafale b croatia"
            _08_rafale_b_export = "08 rafale b export"
            _09_rafale_b_india_air_force = "09 rafale b india air force"
            _10_tiger_meet_2009 = "10 tiger meet 2009"

        class Venezuela(Enum):
            _01_rafale_b_lafayette = "01 rafale b lafayette"
            _02_rafale_b_mt_de_marsan = "02 rafale b mt de marsan"
            _03_rafale_b_qatar = "03 rafale b qatar"
            _04_rafale_b_egypte = "04 rafale b egypte"
            _05_rafale_b_inde = "05 rafale b inde"
            _06_rafale_b_grece = "06 rafale b grece"
            _07_rafale_b_croatia = "07 rafale b croatia"
            _08_rafale_b_export = "08 rafale b export"
            _09_rafale_b_india_air_force = "09 rafale b india air force"
            _10_tiger_meet_2009 = "10 tiger meet 2009"

        class Australia(Enum):
            _01_rafale_b_lafayette = "01 rafale b lafayette"
            _02_rafale_b_mt_de_marsan = "02 rafale b mt de marsan"
            _03_rafale_b_qatar = "03 rafale b qatar"
            _04_rafale_b_egypte = "04 rafale b egypte"
            _05_rafale_b_inde = "05 rafale b inde"
            _06_rafale_b_grece = "06 rafale b grece"
            _07_rafale_b_croatia = "07 rafale b croatia"
            _08_rafale_b_export = "08 rafale b export"
            _09_rafale_b_india_air_force = "09 rafale b india air force"
            _10_tiger_meet_2009 = "10 tiger meet 2009"

        class Israel(Enum):
            _01_rafale_b_lafayette = "01 rafale b lafayette"
            _02_rafale_b_mt_de_marsan = "02 rafale b mt de marsan"
            _03_rafale_b_qatar = "03 rafale b qatar"
            _04_rafale_b_egypte = "04 rafale b egypte"
            _05_rafale_b_inde = "05 rafale b inde"
            _06_rafale_b_grece = "06 rafale b grece"
            _07_rafale_b_croatia = "07 rafale b croatia"
            _08_rafale_b_export = "08 rafale b export"
            _09_rafale_b_india_air_force = "09 rafale b india air force"
            _10_tiger_meet_2009 = "10 tiger meet 2009"

        class Combined_Joint_Task_Forces_Blue(Enum):
            _01_rafale_b_lafayette = "01 rafale b lafayette"
            _02_rafale_b_mt_de_marsan = "02 rafale b mt de marsan"
            _03_rafale_b_qatar = "03 rafale b qatar"
            _04_rafale_b_egypte = "04 rafale b egypte"
            _05_rafale_b_inde = "05 rafale b inde"
            _06_rafale_b_grece = "06 rafale b grece"
            _07_rafale_b_croatia = "07 rafale b croatia"
            _08_rafale_b_export = "08 rafale b export"
            _09_rafale_b_india_air_force = "09 rafale b india air force"
            _10_tiger_meet_2009 = "10 tiger meet 2009"

        class Sudan(Enum):
            _01_rafale_b_lafayette = "01 rafale b lafayette"
            _02_rafale_b_mt_de_marsan = "02 rafale b mt de marsan"
            _03_rafale_b_qatar = "03 rafale b qatar"
            _04_rafale_b_egypte = "04 rafale b egypte"
            _05_rafale_b_inde = "05 rafale b inde"
            _06_rafale_b_grece = "06 rafale b grece"
            _07_rafale_b_croatia = "07 rafale b croatia"
            _08_rafale_b_export = "08 rafale b export"
            _09_rafale_b_india_air_force = "09 rafale b india air force"
            _10_tiger_meet_2009 = "10 tiger meet 2009"

        class Norway(Enum):
            _01_rafale_b_lafayette = "01 rafale b lafayette"
            _02_rafale_b_mt_de_marsan = "02 rafale b mt de marsan"
            _03_rafale_b_qatar = "03 rafale b qatar"
            _04_rafale_b_egypte = "04 rafale b egypte"
            _05_rafale_b_inde = "05 rafale b inde"
            _06_rafale_b_grece = "06 rafale b grece"
            _07_rafale_b_croatia = "07 rafale b croatia"
            _08_rafale_b_export = "08 rafale b export"
            _09_rafale_b_india_air_force = "09 rafale b india air force"
            _10_tiger_meet_2009 = "10 tiger meet 2009"

        class Romania(Enum):
            _01_rafale_b_lafayette = "01 rafale b lafayette"
            _02_rafale_b_mt_de_marsan = "02 rafale b mt de marsan"
            _03_rafale_b_qatar = "03 rafale b qatar"
            _04_rafale_b_egypte = "04 rafale b egypte"
            _05_rafale_b_inde = "05 rafale b inde"
            _06_rafale_b_grece = "06 rafale b grece"
            _07_rafale_b_croatia = "07 rafale b croatia"
            _08_rafale_b_export = "08 rafale b export"
            _09_rafale_b_india_air_force = "09 rafale b india air force"
            _10_tiger_meet_2009 = "10 tiger meet 2009"

        class Iran(Enum):
            _01_rafale_b_lafayette = "01 rafale b lafayette"
            _02_rafale_b_mt_de_marsan = "02 rafale b mt de marsan"
            _03_rafale_b_qatar = "03 rafale b qatar"
            _04_rafale_b_egypte = "04 rafale b egypte"
            _05_rafale_b_inde = "05 rafale b inde"
            _06_rafale_b_grece = "06 rafale b grece"
            _07_rafale_b_croatia = "07 rafale b croatia"
            _08_rafale_b_export = "08 rafale b export"
            _09_rafale_b_india_air_force = "09 rafale b india air force"
            _10_tiger_meet_2009 = "10 tiger meet 2009"

        class Ukraine(Enum):
            _01_rafale_b_lafayette = "01 rafale b lafayette"
            _02_rafale_b_mt_de_marsan = "02 rafale b mt de marsan"
            _03_rafale_b_qatar = "03 rafale b qatar"
            _04_rafale_b_egypte = "04 rafale b egypte"
            _05_rafale_b_inde = "05 rafale b inde"
            _06_rafale_b_grece = "06 rafale b grece"
            _07_rafale_b_croatia = "07 rafale b croatia"
            _08_rafale_b_export = "08 rafale b export"
            _09_rafale_b_india_air_force = "09 rafale b india air force"
            _10_tiger_meet_2009 = "10 tiger meet 2009"

        class Libya(Enum):
            _01_rafale_b_lafayette = "01 rafale b lafayette"
            _02_rafale_b_mt_de_marsan = "02 rafale b mt de marsan"
            _03_rafale_b_qatar = "03 rafale b qatar"
            _04_rafale_b_egypte = "04 rafale b egypte"
            _05_rafale_b_inde = "05 rafale b inde"
            _06_rafale_b_grece = "06 rafale b grece"
            _07_rafale_b_croatia = "07 rafale b croatia"
            _08_rafale_b_export = "08 rafale b export"
            _09_rafale_b_india_air_force = "09 rafale b india air force"
            _10_tiger_meet_2009 = "10 tiger meet 2009"

        class Belgium(Enum):
            _01_rafale_b_lafayette = "01 rafale b lafayette"
            _02_rafale_b_mt_de_marsan = "02 rafale b mt de marsan"
            _03_rafale_b_qatar = "03 rafale b qatar"
            _04_rafale_b_egypte = "04 rafale b egypte"
            _05_rafale_b_inde = "05 rafale b inde"
            _06_rafale_b_grece = "06 rafale b grece"
            _07_rafale_b_croatia = "07 rafale b croatia"
            _08_rafale_b_export = "08 rafale b export"
            _09_rafale_b_india_air_force = "09 rafale b india air force"
            _10_tiger_meet_2009 = "10 tiger meet 2009"

        class Slovakia(Enum):
            _01_rafale_b_lafayette = "01 rafale b lafayette"
            _02_rafale_b_mt_de_marsan = "02 rafale b mt de marsan"
            _03_rafale_b_qatar = "03 rafale b qatar"
            _04_rafale_b_egypte = "04 rafale b egypte"
            _05_rafale_b_inde = "05 rafale b inde"
            _06_rafale_b_grece = "06 rafale b grece"
            _07_rafale_b_croatia = "07 rafale b croatia"
            _08_rafale_b_export = "08 rafale b export"
            _09_rafale_b_india_air_force = "09 rafale b india air force"
            _10_tiger_meet_2009 = "10 tiger meet 2009"

        class Greece(Enum):
            _01_rafale_b_lafayette = "01 rafale b lafayette"
            _02_rafale_b_mt_de_marsan = "02 rafale b mt de marsan"
            _03_rafale_b_qatar = "03 rafale b qatar"
            _04_rafale_b_egypte = "04 rafale b egypte"
            _05_rafale_b_inde = "05 rafale b inde"
            _06_rafale_b_grece = "06 rafale b grece"
            _07_rafale_b_croatia = "07 rafale b croatia"
            _08_rafale_b_export = "08 rafale b export"
            _09_rafale_b_india_air_force = "09 rafale b india air force"
            _10_tiger_meet_2009 = "10 tiger meet 2009"

        class UK(Enum):
            _01_rafale_b_lafayette = "01 rafale b lafayette"
            _02_rafale_b_mt_de_marsan = "02 rafale b mt de marsan"
            _03_rafale_b_qatar = "03 rafale b qatar"
            _04_rafale_b_egypte = "04 rafale b egypte"
            _05_rafale_b_inde = "05 rafale b inde"
            _06_rafale_b_grece = "06 rafale b grece"
            _07_rafale_b_croatia = "07 rafale b croatia"
            _08_rafale_b_export = "08 rafale b export"
            _09_rafale_b_india_air_force = "09 rafale b india air force"
            _10_tiger_meet_2009 = "10 tiger meet 2009"

        class Third_Reich(Enum):
            _01_rafale_b_lafayette = "01 rafale b lafayette"
            _02_rafale_b_mt_de_marsan = "02 rafale b mt de marsan"
            _03_rafale_b_qatar = "03 rafale b qatar"
            _04_rafale_b_egypte = "04 rafale b egypte"
            _05_rafale_b_inde = "05 rafale b inde"
            _06_rafale_b_grece = "06 rafale b grece"
            _07_rafale_b_croatia = "07 rafale b croatia"
            _08_rafale_b_export = "08 rafale b export"
            _09_rafale_b_india_air_force = "09 rafale b india air force"
            _10_tiger_meet_2009 = "10 tiger meet 2009"

        class Hungary(Enum):
            _01_rafale_b_lafayette = "01 rafale b lafayette"
            _02_rafale_b_mt_de_marsan = "02 rafale b mt de marsan"
            _03_rafale_b_qatar = "03 rafale b qatar"
            _04_rafale_b_egypte = "04 rafale b egypte"
            _05_rafale_b_inde = "05 rafale b inde"
            _06_rafale_b_grece = "06 rafale b grece"
            _07_rafale_b_croatia = "07 rafale b croatia"
            _08_rafale_b_export = "08 rafale b export"
            _09_rafale_b_india_air_force = "09 rafale b india air force"
            _10_tiger_meet_2009 = "10 tiger meet 2009"

        class Abkhazia(Enum):
            _01_rafale_b_lafayette = "01 rafale b lafayette"
            _02_rafale_b_mt_de_marsan = "02 rafale b mt de marsan"
            _03_rafale_b_qatar = "03 rafale b qatar"
            _04_rafale_b_egypte = "04 rafale b egypte"
            _05_rafale_b_inde = "05 rafale b inde"
            _06_rafale_b_grece = "06 rafale b grece"
            _07_rafale_b_croatia = "07 rafale b croatia"
            _08_rafale_b_export = "08 rafale b export"
            _09_rafale_b_india_air_force = "09 rafale b india air force"
            _10_tiger_meet_2009 = "10 tiger meet 2009"

        class Morocco(Enum):
            _01_rafale_b_lafayette = "01 rafale b lafayette"
            _02_rafale_b_mt_de_marsan = "02 rafale b mt de marsan"
            _03_rafale_b_qatar = "03 rafale b qatar"
            _04_rafale_b_egypte = "04 rafale b egypte"
            _05_rafale_b_inde = "05 rafale b inde"
            _06_rafale_b_grece = "06 rafale b grece"
            _07_rafale_b_croatia = "07 rafale b croatia"
            _08_rafale_b_export = "08 rafale b export"
            _09_rafale_b_india_air_force = "09 rafale b india air force"
            _10_tiger_meet_2009 = "10 tiger meet 2009"

        class United_Nations_Peacekeepers(Enum):
            _01_rafale_b_lafayette = "01 rafale b lafayette"
            _02_rafale_b_mt_de_marsan = "02 rafale b mt de marsan"
            _03_rafale_b_qatar = "03 rafale b qatar"
            _04_rafale_b_egypte = "04 rafale b egypte"
            _05_rafale_b_inde = "05 rafale b inde"
            _06_rafale_b_grece = "06 rafale b grece"
            _07_rafale_b_croatia = "07 rafale b croatia"
            _08_rafale_b_export = "08 rafale b export"
            _09_rafale_b_india_air_force = "09 rafale b india air force"
            _10_tiger_meet_2009 = "10 tiger meet 2009"

        class Switzerland(Enum):
            _01_rafale_b_lafayette = "01 rafale b lafayette"
            _02_rafale_b_mt_de_marsan = "02 rafale b mt de marsan"
            _03_rafale_b_qatar = "03 rafale b qatar"
            _04_rafale_b_egypte = "04 rafale b egypte"
            _05_rafale_b_inde = "05 rafale b inde"
            _06_rafale_b_grece = "06 rafale b grece"
            _07_rafale_b_croatia = "07 rafale b croatia"
            _08_rafale_b_export = "08 rafale b export"
            _09_rafale_b_india_air_force = "09 rafale b india air force"
            _10_tiger_meet_2009 = "10 tiger meet 2009"

        class SouthOssetia(Enum):
            _01_rafale_b_lafayette = "01 rafale b lafayette"
            _02_rafale_b_mt_de_marsan = "02 rafale b mt de marsan"
            _03_rafale_b_qatar = "03 rafale b qatar"
            _04_rafale_b_egypte = "04 rafale b egypte"
            _05_rafale_b_inde = "05 rafale b inde"
            _06_rafale_b_grece = "06 rafale b grece"
            _07_rafale_b_croatia = "07 rafale b croatia"
            _08_rafale_b_export = "08 rafale b export"
            _09_rafale_b_india_air_force = "09 rafale b india air force"
            _10_tiger_meet_2009 = "10 tiger meet 2009"

        class Vietnam(Enum):
            _01_rafale_b_lafayette = "01 rafale b lafayette"
            _02_rafale_b_mt_de_marsan = "02 rafale b mt de marsan"
            _03_rafale_b_qatar = "03 rafale b qatar"
            _04_rafale_b_egypte = "04 rafale b egypte"
            _05_rafale_b_inde = "05 rafale b inde"
            _06_rafale_b_grece = "06 rafale b grece"
            _07_rafale_b_croatia = "07 rafale b croatia"
            _08_rafale_b_export = "08 rafale b export"
            _09_rafale_b_india_air_force = "09 rafale b india air force"
            _10_tiger_meet_2009 = "10 tiger meet 2009"

        class China(Enum):
            _01_rafale_b_lafayette = "01 rafale b lafayette"
            _02_rafale_b_mt_de_marsan = "02 rafale b mt de marsan"
            _03_rafale_b_qatar = "03 rafale b qatar"
            _04_rafale_b_egypte = "04 rafale b egypte"
            _05_rafale_b_inde = "05 rafale b inde"
            _06_rafale_b_grece = "06 rafale b grece"
            _07_rafale_b_croatia = "07 rafale b croatia"
            _08_rafale_b_export = "08 rafale b export"
            _09_rafale_b_india_air_force = "09 rafale b india air force"
            _10_tiger_meet_2009 = "10 tiger meet 2009"

        class Yemen(Enum):
            _01_rafale_b_lafayette = "01 rafale b lafayette"
            _02_rafale_b_mt_de_marsan = "02 rafale b mt de marsan"
            _03_rafale_b_qatar = "03 rafale b qatar"
            _04_rafale_b_egypte = "04 rafale b egypte"
            _05_rafale_b_inde = "05 rafale b inde"
            _06_rafale_b_grece = "06 rafale b grece"
            _07_rafale_b_croatia = "07 rafale b croatia"
            _08_rafale_b_export = "08 rafale b export"
            _09_rafale_b_india_air_force = "09 rafale b india air force"
            _10_tiger_meet_2009 = "10 tiger meet 2009"

        class Kuwait(Enum):
            _01_rafale_b_lafayette = "01 rafale b lafayette"
            _02_rafale_b_mt_de_marsan = "02 rafale b mt de marsan"
            _03_rafale_b_qatar = "03 rafale b qatar"
            _04_rafale_b_egypte = "04 rafale b egypte"
            _05_rafale_b_inde = "05 rafale b inde"
            _06_rafale_b_grece = "06 rafale b grece"
            _07_rafale_b_croatia = "07 rafale b croatia"
            _08_rafale_b_export = "08 rafale b export"
            _09_rafale_b_india_air_force = "09 rafale b india air force"
            _10_tiger_meet_2009 = "10 tiger meet 2009"

        class Serbia(Enum):
            _01_rafale_b_lafayette = "01 rafale b lafayette"
            _02_rafale_b_mt_de_marsan = "02 rafale b mt de marsan"
            _03_rafale_b_qatar = "03 rafale b qatar"
            _04_rafale_b_egypte = "04 rafale b egypte"
            _05_rafale_b_inde = "05 rafale b inde"
            _06_rafale_b_grece = "06 rafale b grece"
            _07_rafale_b_croatia = "07 rafale b croatia"
            _08_rafale_b_export = "08 rafale b export"
            _09_rafale_b_india_air_force = "09 rafale b india air force"
            _10_tiger_meet_2009 = "10 tiger meet 2009"

        class Oman(Enum):
            _01_rafale_b_lafayette = "01 rafale b lafayette"
            _02_rafale_b_mt_de_marsan = "02 rafale b mt de marsan"
            _03_rafale_b_qatar = "03 rafale b qatar"
            _04_rafale_b_egypte = "04 rafale b egypte"
            _05_rafale_b_inde = "05 rafale b inde"
            _06_rafale_b_grece = "06 rafale b grece"
            _07_rafale_b_croatia = "07 rafale b croatia"
            _08_rafale_b_export = "08 rafale b export"
            _09_rafale_b_india_air_force = "09 rafale b india air force"
            _10_tiger_meet_2009 = "10 tiger meet 2009"

        class India(Enum):
            _01_rafale_b_lafayette = "01 rafale b lafayette"
            _02_rafale_b_mt_de_marsan = "02 rafale b mt de marsan"
            _03_rafale_b_qatar = "03 rafale b qatar"
            _04_rafale_b_egypte = "04 rafale b egypte"
            _05_rafale_b_inde = "05 rafale b inde"
            _06_rafale_b_grece = "06 rafale b grece"
            _07_rafale_b_croatia = "07 rafale b croatia"
            _08_rafale_b_export = "08 rafale b export"
            _09_rafale_b_india_air_force = "09 rafale b india air force"
            _10_tiger_meet_2009 = "10 tiger meet 2009"

        class Egypt(Enum):
            _01_rafale_b_lafayette = "01 rafale b lafayette"
            _02_rafale_b_mt_de_marsan = "02 rafale b mt de marsan"
            _03_rafale_b_qatar = "03 rafale b qatar"
            _04_rafale_b_egypte = "04 rafale b egypte"
            _05_rafale_b_inde = "05 rafale b inde"
            _06_rafale_b_grece = "06 rafale b grece"
            _07_rafale_b_croatia = "07 rafale b croatia"
            _08_rafale_b_export = "08 rafale b export"
            _09_rafale_b_india_air_force = "09 rafale b india air force"
            _10_tiger_meet_2009 = "10 tiger meet 2009"

        class TheNetherlands(Enum):
            _01_rafale_b_lafayette = "01 rafale b lafayette"
            _02_rafale_b_mt_de_marsan = "02 rafale b mt de marsan"
            _03_rafale_b_qatar = "03 rafale b qatar"
            _04_rafale_b_egypte = "04 rafale b egypte"
            _05_rafale_b_inde = "05 rafale b inde"
            _06_rafale_b_grece = "06 rafale b grece"
            _07_rafale_b_croatia = "07 rafale b croatia"
            _08_rafale_b_export = "08 rafale b export"
            _09_rafale_b_india_air_force = "09 rafale b india air force"
            _10_tiger_meet_2009 = "10 tiger meet 2009"

        class Poland(Enum):
            _01_rafale_b_lafayette = "01 rafale b lafayette"
            _02_rafale_b_mt_de_marsan = "02 rafale b mt de marsan"
            _03_rafale_b_qatar = "03 rafale b qatar"
            _04_rafale_b_egypte = "04 rafale b egypte"
            _05_rafale_b_inde = "05 rafale b inde"
            _06_rafale_b_grece = "06 rafale b grece"
            _07_rafale_b_croatia = "07 rafale b croatia"
            _08_rafale_b_export = "08 rafale b export"
            _09_rafale_b_india_air_force = "09 rafale b india air force"
            _10_tiger_meet_2009 = "10 tiger meet 2009"

        class Syria(Enum):
            _01_rafale_b_lafayette = "01 rafale b lafayette"
            _02_rafale_b_mt_de_marsan = "02 rafale b mt de marsan"
            _03_rafale_b_qatar = "03 rafale b qatar"
            _04_rafale_b_egypte = "04 rafale b egypte"
            _05_rafale_b_inde = "05 rafale b inde"
            _06_rafale_b_grece = "06 rafale b grece"
            _07_rafale_b_croatia = "07 rafale b croatia"
            _08_rafale_b_export = "08 rafale b export"
            _09_rafale_b_india_air_force = "09 rafale b india air force"
            _10_tiger_meet_2009 = "10 tiger meet 2009"

        class Finland(Enum):
            _01_rafale_b_lafayette = "01 rafale b lafayette"
            _02_rafale_b_mt_de_marsan = "02 rafale b mt de marsan"
            _03_rafale_b_qatar = "03 rafale b qatar"
            _04_rafale_b_egypte = "04 rafale b egypte"
            _05_rafale_b_inde = "05 rafale b inde"
            _06_rafale_b_grece = "06 rafale b grece"
            _07_rafale_b_croatia = "07 rafale b croatia"
            _08_rafale_b_export = "08 rafale b export"
            _09_rafale_b_india_air_force = "09 rafale b india air force"
            _10_tiger_meet_2009 = "10 tiger meet 2009"

        class Kazakhstan(Enum):
            _01_rafale_b_lafayette = "01 rafale b lafayette"
            _02_rafale_b_mt_de_marsan = "02 rafale b mt de marsan"
            _03_rafale_b_qatar = "03 rafale b qatar"
            _04_rafale_b_egypte = "04 rafale b egypte"
            _05_rafale_b_inde = "05 rafale b inde"
            _06_rafale_b_grece = "06 rafale b grece"
            _07_rafale_b_croatia = "07 rafale b croatia"
            _08_rafale_b_export = "08 rafale b export"
            _09_rafale_b_india_air_force = "09 rafale b india air force"
            _10_tiger_meet_2009 = "10 tiger meet 2009"

        class Denmark(Enum):
            _01_rafale_b_lafayette = "01 rafale b lafayette"
            _02_rafale_b_mt_de_marsan = "02 rafale b mt de marsan"
            _03_rafale_b_qatar = "03 rafale b qatar"
            _04_rafale_b_egypte = "04 rafale b egypte"
            _05_rafale_b_inde = "05 rafale b inde"
            _06_rafale_b_grece = "06 rafale b grece"
            _07_rafale_b_croatia = "07 rafale b croatia"
            _08_rafale_b_export = "08 rafale b export"
            _09_rafale_b_india_air_force = "09 rafale b india air force"
            _10_tiger_meet_2009 = "10 tiger meet 2009"

        class Sweden(Enum):
            _01_rafale_b_lafayette = "01 rafale b lafayette"
            _02_rafale_b_mt_de_marsan = "02 rafale b mt de marsan"
            _03_rafale_b_qatar = "03 rafale b qatar"
            _04_rafale_b_egypte = "04 rafale b egypte"
            _05_rafale_b_inde = "05 rafale b inde"
            _06_rafale_b_grece = "06 rafale b grece"
            _07_rafale_b_croatia = "07 rafale b croatia"
            _08_rafale_b_export = "08 rafale b export"
            _09_rafale_b_india_air_force = "09 rafale b india air force"
            _10_tiger_meet_2009 = "10 tiger meet 2009"

        class Croatia(Enum):
            _01_rafale_b_lafayette = "01 rafale b lafayette"
            _02_rafale_b_mt_de_marsan = "02 rafale b mt de marsan"
            _03_rafale_b_qatar = "03 rafale b qatar"
            _04_rafale_b_egypte = "04 rafale b egypte"
            _05_rafale_b_inde = "05 rafale b inde"
            _06_rafale_b_grece = "06 rafale b grece"
            _07_rafale_b_croatia = "07 rafale b croatia"
            _08_rafale_b_export = "08 rafale b export"
            _09_rafale_b_india_air_force = "09 rafale b india air force"
            _10_tiger_meet_2009 = "10 tiger meet 2009"

        class CzechRepublic(Enum):
            _01_rafale_b_lafayette = "01 rafale b lafayette"
            _02_rafale_b_mt_de_marsan = "02 rafale b mt de marsan"
            _03_rafale_b_qatar = "03 rafale b qatar"
            _04_rafale_b_egypte = "04 rafale b egypte"
            _05_rafale_b_inde = "05 rafale b inde"
            _06_rafale_b_grece = "06 rafale b grece"
            _07_rafale_b_croatia = "07 rafale b croatia"
            _08_rafale_b_export = "08 rafale b export"
            _09_rafale_b_india_air_force = "09 rafale b india air force"
            _10_tiger_meet_2009 = "10 tiger meet 2009"

        class GDR(Enum):
            _01_rafale_b_lafayette = "01 rafale b lafayette"
            _02_rafale_b_mt_de_marsan = "02 rafale b mt de marsan"
            _03_rafale_b_qatar = "03 rafale b qatar"
            _04_rafale_b_egypte = "04 rafale b egypte"
            _05_rafale_b_inde = "05 rafale b inde"
            _06_rafale_b_grece = "06 rafale b grece"
            _07_rafale_b_croatia = "07 rafale b croatia"
            _08_rafale_b_export = "08 rafale b export"
            _09_rafale_b_india_air_force = "09 rafale b india air force"
            _10_tiger_meet_2009 = "10 tiger meet 2009"

        class Yugoslavia(Enum):
            _01_rafale_b_lafayette = "01 rafale b lafayette"
            _02_rafale_b_mt_de_marsan = "02 rafale b mt de marsan"
            _03_rafale_b_qatar = "03 rafale b qatar"
            _04_rafale_b_egypte = "04 rafale b egypte"
            _05_rafale_b_inde = "05 rafale b inde"
            _06_rafale_b_grece = "06 rafale b grece"
            _07_rafale_b_croatia = "07 rafale b croatia"
            _08_rafale_b_export = "08 rafale b export"
            _09_rafale_b_india_air_force = "09 rafale b india air force"
            _10_tiger_meet_2009 = "10 tiger meet 2009"

        class Bulgaria(Enum):
            _01_rafale_b_lafayette = "01 rafale b lafayette"
            _02_rafale_b_mt_de_marsan = "02 rafale b mt de marsan"
            _03_rafale_b_qatar = "03 rafale b qatar"
            _04_rafale_b_egypte = "04 rafale b egypte"
            _05_rafale_b_inde = "05 rafale b inde"
            _06_rafale_b_grece = "06 rafale b grece"
            _07_rafale_b_croatia = "07 rafale b croatia"
            _08_rafale_b_export = "08 rafale b export"
            _09_rafale_b_india_air_force = "09 rafale b india air force"
            _10_tiger_meet_2009 = "10 tiger meet 2009"

        class SouthKorea(Enum):
            _01_rafale_b_lafayette = "01 rafale b lafayette"
            _02_rafale_b_mt_de_marsan = "02 rafale b mt de marsan"
            _03_rafale_b_qatar = "03 rafale b qatar"
            _04_rafale_b_egypte = "04 rafale b egypte"
            _05_rafale_b_inde = "05 rafale b inde"
            _06_rafale_b_grece = "06 rafale b grece"
            _07_rafale_b_croatia = "07 rafale b croatia"
            _08_rafale_b_export = "08 rafale b export"
            _09_rafale_b_india_air_force = "09 rafale b india air force"
            _10_tiger_meet_2009 = "10 tiger meet 2009"

        class Tunisia(Enum):
            _01_rafale_b_lafayette = "01 rafale b lafayette"
            _02_rafale_b_mt_de_marsan = "02 rafale b mt de marsan"
            _03_rafale_b_qatar = "03 rafale b qatar"
            _04_rafale_b_egypte = "04 rafale b egypte"
            _05_rafale_b_inde = "05 rafale b inde"
            _06_rafale_b_grece = "06 rafale b grece"
            _07_rafale_b_croatia = "07 rafale b croatia"
            _08_rafale_b_export = "08 rafale b export"
            _09_rafale_b_india_air_force = "09 rafale b india air force"
            _10_tiger_meet_2009 = "10 tiger meet 2009"

        class Combined_Joint_Task_Forces_Red(Enum):
            _01_rafale_b_lafayette = "01 rafale b lafayette"
            _02_rafale_b_mt_de_marsan = "02 rafale b mt de marsan"
            _03_rafale_b_qatar = "03 rafale b qatar"
            _04_rafale_b_egypte = "04 rafale b egypte"
            _05_rafale_b_inde = "05 rafale b inde"
            _06_rafale_b_grece = "06 rafale b grece"
            _07_rafale_b_croatia = "07 rafale b croatia"
            _08_rafale_b_export = "08 rafale b export"
            _09_rafale_b_india_air_force = "09 rafale b india air force"
            _10_tiger_meet_2009 = "10 tiger meet 2009"

        class Lebanon(Enum):
            _01_rafale_b_lafayette = "01 rafale b lafayette"
            _02_rafale_b_mt_de_marsan = "02 rafale b mt de marsan"
            _03_rafale_b_qatar = "03 rafale b qatar"
            _04_rafale_b_egypte = "04 rafale b egypte"
            _05_rafale_b_inde = "05 rafale b inde"
            _06_rafale_b_grece = "06 rafale b grece"
            _07_rafale_b_croatia = "07 rafale b croatia"
            _08_rafale_b_export = "08 rafale b export"
            _09_rafale_b_india_air_force = "09 rafale b india air force"
            _10_tiger_meet_2009 = "10 tiger meet 2009"

        class Portugal(Enum):
            _01_rafale_b_lafayette = "01 rafale b lafayette"
            _02_rafale_b_mt_de_marsan = "02 rafale b mt de marsan"
            _03_rafale_b_qatar = "03 rafale b qatar"
            _04_rafale_b_egypte = "04 rafale b egypte"
            _05_rafale_b_inde = "05 rafale b inde"
            _06_rafale_b_grece = "06 rafale b grece"
            _07_rafale_b_croatia = "07 rafale b croatia"
            _08_rafale_b_export = "08 rafale b export"
            _09_rafale_b_india_air_force = "09 rafale b india air force"
            _10_tiger_meet_2009 = "10 tiger meet 2009"

        class Cuba(Enum):
            _01_rafale_b_lafayette = "01 rafale b lafayette"
            _02_rafale_b_mt_de_marsan = "02 rafale b mt de marsan"
            _03_rafale_b_qatar = "03 rafale b qatar"
            _04_rafale_b_egypte = "04 rafale b egypte"
            _05_rafale_b_inde = "05 rafale b inde"
            _06_rafale_b_grece = "06 rafale b grece"
            _07_rafale_b_croatia = "07 rafale b croatia"
            _08_rafale_b_export = "08 rafale b export"
            _09_rafale_b_india_air_force = "09 rafale b india air force"
            _10_tiger_meet_2009 = "10 tiger meet 2009"

        class Insurgents(Enum):
            _01_rafale_b_lafayette = "01 rafale b lafayette"
            _02_rafale_b_mt_de_marsan = "02 rafale b mt de marsan"
            _03_rafale_b_qatar = "03 rafale b qatar"
            _04_rafale_b_egypte = "04 rafale b egypte"
            _05_rafale_b_inde = "05 rafale b inde"
            _06_rafale_b_grece = "06 rafale b grece"
            _07_rafale_b_croatia = "07 rafale b croatia"
            _08_rafale_b_export = "08 rafale b export"
            _09_rafale_b_india_air_force = "09 rafale b india air force"
            _10_tiger_meet_2009 = "10 tiger meet 2009"

        class SaudiArabia(Enum):
            _01_rafale_b_lafayette = "01 rafale b lafayette"
            _02_rafale_b_mt_de_marsan = "02 rafale b mt de marsan"
            _03_rafale_b_qatar = "03 rafale b qatar"
            _04_rafale_b_egypte = "04 rafale b egypte"
            _05_rafale_b_inde = "05 rafale b inde"
            _06_rafale_b_grece = "06 rafale b grece"
            _07_rafale_b_croatia = "07 rafale b croatia"
            _08_rafale_b_export = "08 rafale b export"
            _09_rafale_b_india_air_force = "09 rafale b india air force"
            _10_tiger_meet_2009 = "10 tiger meet 2009"

        class France(Enum):
            _01_rafale_b_lafayette = "01 rafale b lafayette"
            _02_rafale_b_mt_de_marsan = "02 rafale b mt de marsan"
            _03_rafale_b_qatar = "03 rafale b qatar"
            _04_rafale_b_egypte = "04 rafale b egypte"
            _05_rafale_b_inde = "05 rafale b inde"
            _06_rafale_b_grece = "06 rafale b grece"
            _07_rafale_b_croatia = "07 rafale b croatia"
            _08_rafale_b_export = "08 rafale b export"
            _09_rafale_b_india_air_force = "09 rafale b india air force"
            _10_tiger_meet_2009 = "10 tiger meet 2009"

        class USA(Enum):
            _01_rafale_b_lafayette = "01 rafale b lafayette"
            _02_rafale_b_mt_de_marsan = "02 rafale b mt de marsan"
            _03_rafale_b_qatar = "03 rafale b qatar"
            _04_rafale_b_egypte = "04 rafale b egypte"
            _05_rafale_b_inde = "05 rafale b inde"
            _06_rafale_b_grece = "06 rafale b grece"
            _07_rafale_b_croatia = "07 rafale b croatia"
            _08_rafale_b_export = "08 rafale b export"
            _09_rafale_b_india_air_force = "09 rafale b india air force"
            _10_tiger_meet_2009 = "10 tiger meet 2009"

        class Honduras(Enum):
            _01_rafale_b_lafayette = "01 rafale b lafayette"
            _02_rafale_b_mt_de_marsan = "02 rafale b mt de marsan"
            _03_rafale_b_qatar = "03 rafale b qatar"
            _04_rafale_b_egypte = "04 rafale b egypte"
            _05_rafale_b_inde = "05 rafale b inde"
            _06_rafale_b_grece = "06 rafale b grece"
            _07_rafale_b_croatia = "07 rafale b croatia"
            _08_rafale_b_export = "08 rafale b export"
            _09_rafale_b_india_air_force = "09 rafale b india air force"
            _10_tiger_meet_2009 = "10 tiger meet 2009"

        class Qatar(Enum):
            _01_rafale_b_lafayette = "01 rafale b lafayette"
            _02_rafale_b_mt_de_marsan = "02 rafale b mt de marsan"
            _03_rafale_b_qatar = "03 rafale b qatar"
            _04_rafale_b_egypte = "04 rafale b egypte"
            _05_rafale_b_inde = "05 rafale b inde"
            _06_rafale_b_grece = "06 rafale b grece"
            _07_rafale_b_croatia = "07 rafale b croatia"
            _08_rafale_b_export = "08 rafale b export"
            _09_rafale_b_india_air_force = "09 rafale b india air force"
            _10_tiger_meet_2009 = "10 tiger meet 2009"

        class Russia(Enum):
            _01_rafale_b_lafayette = "01 rafale b lafayette"
            _02_rafale_b_mt_de_marsan = "02 rafale b mt de marsan"
            _03_rafale_b_qatar = "03 rafale b qatar"
            _04_rafale_b_egypte = "04 rafale b egypte"
            _05_rafale_b_inde = "05 rafale b inde"
            _06_rafale_b_grece = "06 rafale b grece"
            _07_rafale_b_croatia = "07 rafale b croatia"
            _08_rafale_b_export = "08 rafale b export"
            _09_rafale_b_india_air_force = "09 rafale b india air force"
            _10_tiger_meet_2009 = "10 tiger meet 2009"

        class United_Arab_Emirates(Enum):
            _01_rafale_b_lafayette = "01 rafale b lafayette"
            _02_rafale_b_mt_de_marsan = "02 rafale b mt de marsan"
            _03_rafale_b_qatar = "03 rafale b qatar"
            _04_rafale_b_egypte = "04 rafale b egypte"
            _05_rafale_b_inde = "05 rafale b inde"
            _06_rafale_b_grece = "06 rafale b grece"
            _07_rafale_b_croatia = "07 rafale b croatia"
            _08_rafale_b_export = "08 rafale b export"
            _09_rafale_b_india_air_force = "09 rafale b india air force"
            _10_tiger_meet_2009 = "10 tiger meet 2009"

        class Italian_Social_Republi(Enum):
            _01_rafale_b_lafayette = "01 rafale b lafayette"
            _02_rafale_b_mt_de_marsan = "02 rafale b mt de marsan"
            _03_rafale_b_qatar = "03 rafale b qatar"
            _04_rafale_b_egypte = "04 rafale b egypte"
            _05_rafale_b_inde = "05 rafale b inde"
            _06_rafale_b_grece = "06 rafale b grece"
            _07_rafale_b_croatia = "07 rafale b croatia"
            _08_rafale_b_export = "08 rafale b export"
            _09_rafale_b_india_air_force = "09 rafale b india air force"
            _10_tiger_meet_2009 = "10 tiger meet 2009"

        class Austria(Enum):
            _01_rafale_b_lafayette = "01 rafale b lafayette"
            _02_rafale_b_mt_de_marsan = "02 rafale b mt de marsan"
            _03_rafale_b_qatar = "03 rafale b qatar"
            _04_rafale_b_egypte = "04 rafale b egypte"
            _05_rafale_b_inde = "05 rafale b inde"
            _06_rafale_b_grece = "06 rafale b grece"
            _07_rafale_b_croatia = "07 rafale b croatia"
            _08_rafale_b_export = "08 rafale b export"
            _09_rafale_b_india_air_force = "09 rafale b india air force"
            _10_tiger_meet_2009 = "10 tiger meet 2009"

        class Bahrain(Enum):
            _01_rafale_b_lafayette = "01 rafale b lafayette"
            _02_rafale_b_mt_de_marsan = "02 rafale b mt de marsan"
            _03_rafale_b_qatar = "03 rafale b qatar"
            _04_rafale_b_egypte = "04 rafale b egypte"
            _05_rafale_b_inde = "05 rafale b inde"
            _06_rafale_b_grece = "06 rafale b grece"
            _07_rafale_b_croatia = "07 rafale b croatia"
            _08_rafale_b_export = "08 rafale b export"
            _09_rafale_b_india_air_force = "09 rafale b india air force"
            _10_tiger_meet_2009 = "10 tiger meet 2009"

        class Italy(Enum):
            _01_rafale_b_lafayette = "01 rafale b lafayette"
            _02_rafale_b_mt_de_marsan = "02 rafale b mt de marsan"
            _03_rafale_b_qatar = "03 rafale b qatar"
            _04_rafale_b_egypte = "04 rafale b egypte"
            _05_rafale_b_inde = "05 rafale b inde"
            _06_rafale_b_grece = "06 rafale b grece"
            _07_rafale_b_croatia = "07 rafale b croatia"
            _08_rafale_b_export = "08 rafale b export"
            _09_rafale_b_india_air_force = "09 rafale b india air force"
            _10_tiger_meet_2009 = "10 tiger meet 2009"

        class Chile(Enum):
            _01_rafale_b_lafayette = "01 rafale b lafayette"
            _02_rafale_b_mt_de_marsan = "02 rafale b mt de marsan"
            _03_rafale_b_qatar = "03 rafale b qatar"
            _04_rafale_b_egypte = "04 rafale b egypte"
            _05_rafale_b_inde = "05 rafale b inde"
            _06_rafale_b_grece = "06 rafale b grece"
            _07_rafale_b_croatia = "07 rafale b croatia"
            _08_rafale_b_export = "08 rafale b export"
            _09_rafale_b_india_air_force = "09 rafale b india air force"
            _10_tiger_meet_2009 = "10 tiger meet 2009"

        class Turkey(Enum):
            _01_rafale_b_lafayette = "01 rafale b lafayette"
            _02_rafale_b_mt_de_marsan = "02 rafale b mt de marsan"
            _03_rafale_b_qatar = "03 rafale b qatar"
            _04_rafale_b_egypte = "04 rafale b egypte"
            _05_rafale_b_inde = "05 rafale b inde"
            _06_rafale_b_grece = "06 rafale b grece"
            _07_rafale_b_croatia = "07 rafale b croatia"
            _08_rafale_b_export = "08 rafale b export"
            _09_rafale_b_india_air_force = "09 rafale b india air force"
            _10_tiger_meet_2009 = "10 tiger meet 2009"

        class Philippines(Enum):
            _01_rafale_b_lafayette = "01 rafale b lafayette"
            _02_rafale_b_mt_de_marsan = "02 rafale b mt de marsan"
            _03_rafale_b_qatar = "03 rafale b qatar"
            _04_rafale_b_egypte = "04 rafale b egypte"
            _05_rafale_b_inde = "05 rafale b inde"
            _06_rafale_b_grece = "06 rafale b grece"
            _07_rafale_b_croatia = "07 rafale b croatia"
            _08_rafale_b_export = "08 rafale b export"
            _09_rafale_b_india_air_force = "09 rafale b india air force"
            _10_tiger_meet_2009 = "10 tiger meet 2009"

        class Algeria(Enum):
            _01_rafale_b_lafayette = "01 rafale b lafayette"
            _02_rafale_b_mt_de_marsan = "02 rafale b mt de marsan"
            _03_rafale_b_qatar = "03 rafale b qatar"
            _04_rafale_b_egypte = "04 rafale b egypte"
            _05_rafale_b_inde = "05 rafale b inde"
            _06_rafale_b_grece = "06 rafale b grece"
            _07_rafale_b_croatia = "07 rafale b croatia"
            _08_rafale_b_export = "08 rafale b export"
            _09_rafale_b_india_air_force = "09 rafale b india air force"
            _10_tiger_meet_2009 = "10 tiger meet 2009"

        class Pakistan(Enum):
            _01_rafale_b_lafayette = "01 rafale b lafayette"
            _02_rafale_b_mt_de_marsan = "02 rafale b mt de marsan"
            _03_rafale_b_qatar = "03 rafale b qatar"
            _04_rafale_b_egypte = "04 rafale b egypte"
            _05_rafale_b_inde = "05 rafale b inde"
            _06_rafale_b_grece = "06 rafale b grece"
            _07_rafale_b_croatia = "07 rafale b croatia"
            _08_rafale_b_export = "08 rafale b export"
            _09_rafale_b_india_air_force = "09 rafale b india air force"
            _10_tiger_meet_2009 = "10 tiger meet 2009"

        class Malaysia(Enum):
            _01_rafale_b_lafayette = "01 rafale b lafayette"
            _02_rafale_b_mt_de_marsan = "02 rafale b mt de marsan"
            _03_rafale_b_qatar = "03 rafale b qatar"
            _04_rafale_b_egypte = "04 rafale b egypte"
            _05_rafale_b_inde = "05 rafale b inde"
            _06_rafale_b_grece = "06 rafale b grece"
            _07_rafale_b_croatia = "07 rafale b croatia"
            _08_rafale_b_export = "08 rafale b export"
            _09_rafale_b_india_air_force = "09 rafale b india air force"
            _10_tiger_meet_2009 = "10 tiger meet 2009"

        class Indonesia(Enum):
            _01_rafale_b_lafayette = "01 rafale b lafayette"
            _02_rafale_b_mt_de_marsan = "02 rafale b mt de marsan"
            _03_rafale_b_qatar = "03 rafale b qatar"
            _04_rafale_b_egypte = "04 rafale b egypte"
            _05_rafale_b_inde = "05 rafale b inde"
            _06_rafale_b_grece = "06 rafale b grece"
            _07_rafale_b_croatia = "07 rafale b croatia"
            _08_rafale_b_export = "08 rafale b export"
            _09_rafale_b_india_air_force = "09 rafale b india air force"
            _10_tiger_meet_2009 = "10 tiger meet 2009"

        class Iraq(Enum):
            _01_rafale_b_lafayette = "01 rafale b lafayette"
            _02_rafale_b_mt_de_marsan = "02 rafale b mt de marsan"
            _03_rafale_b_qatar = "03 rafale b qatar"
            _04_rafale_b_egypte = "04 rafale b egypte"
            _05_rafale_b_inde = "05 rafale b inde"
            _06_rafale_b_grece = "06 rafale b grece"
            _07_rafale_b_croatia = "07 rafale b croatia"
            _08_rafale_b_export = "08 rafale b export"
            _09_rafale_b_india_air_force = "09 rafale b india air force"
            _10_tiger_meet_2009 = "10 tiger meet 2009"

        class Germany(Enum):
            _01_rafale_b_lafayette = "01 rafale b lafayette"
            _02_rafale_b_mt_de_marsan = "02 rafale b mt de marsan"
            _03_rafale_b_qatar = "03 rafale b qatar"
            _04_rafale_b_egypte = "04 rafale b egypte"
            _05_rafale_b_inde = "05 rafale b inde"
            _06_rafale_b_grece = "06 rafale b grece"
            _07_rafale_b_croatia = "07 rafale b croatia"
            _08_rafale_b_export = "08 rafale b export"
            _09_rafale_b_india_air_force = "09 rafale b india air force"
            _10_tiger_meet_2009 = "10 tiger meet 2009"

        class South_Africa(Enum):
            _01_rafale_b_lafayette = "01 rafale b lafayette"
            _02_rafale_b_mt_de_marsan = "02 rafale b mt de marsan"
            _03_rafale_b_qatar = "03 rafale b qatar"
            _04_rafale_b_egypte = "04 rafale b egypte"
            _05_rafale_b_inde = "05 rafale b inde"
            _06_rafale_b_grece = "06 rafale b grece"
            _07_rafale_b_croatia = "07 rafale b croatia"
            _08_rafale_b_export = "08 rafale b export"
            _09_rafale_b_india_air_force = "09 rafale b india air force"
            _10_tiger_meet_2009 = "10 tiger meet 2009"

        class Jordan(Enum):
            _01_rafale_b_lafayette = "01 rafale b lafayette"
            _02_rafale_b_mt_de_marsan = "02 rafale b mt de marsan"
            _03_rafale_b_qatar = "03 rafale b qatar"
            _04_rafale_b_egypte = "04 rafale b egypte"
            _05_rafale_b_inde = "05 rafale b inde"
            _06_rafale_b_grece = "06 rafale b grece"
            _07_rafale_b_croatia = "07 rafale b croatia"
            _08_rafale_b_export = "08 rafale b export"
            _09_rafale_b_india_air_force = "09 rafale b india air force"
            _10_tiger_meet_2009 = "10 tiger meet 2009"

        class Mexico(Enum):
            _01_rafale_b_lafayette = "01 rafale b lafayette"
            _02_rafale_b_mt_de_marsan = "02 rafale b mt de marsan"
            _03_rafale_b_qatar = "03 rafale b qatar"
            _04_rafale_b_egypte = "04 rafale b egypte"
            _05_rafale_b_inde = "05 rafale b inde"
            _06_rafale_b_grece = "06 rafale b grece"
            _07_rafale_b_croatia = "07 rafale b croatia"
            _08_rafale_b_export = "08 rafale b export"
            _09_rafale_b_india_air_force = "09 rafale b india air force"
            _10_tiger_meet_2009 = "10 tiger meet 2009"

        class USAFAggressors(Enum):
            _01_rafale_b_lafayette = "01 rafale b lafayette"
            _02_rafale_b_mt_de_marsan = "02 rafale b mt de marsan"
            _03_rafale_b_qatar = "03 rafale b qatar"
            _04_rafale_b_egypte = "04 rafale b egypte"
            _05_rafale_b_inde = "05 rafale b inde"
            _06_rafale_b_grece = "06 rafale b grece"
            _07_rafale_b_croatia = "07 rafale b croatia"
            _08_rafale_b_export = "08 rafale b export"
            _09_rafale_b_india_air_force = "09 rafale b india air force"
            _10_tiger_meet_2009 = "10 tiger meet 2009"

        class Brazil(Enum):
            _01_rafale_b_lafayette = "01 rafale b lafayette"
            _02_rafale_b_mt_de_marsan = "02 rafale b mt de marsan"
            _03_rafale_b_qatar = "03 rafale b qatar"
            _04_rafale_b_egypte = "04 rafale b egypte"
            _05_rafale_b_inde = "05 rafale b inde"
            _06_rafale_b_grece = "06 rafale b grece"
            _07_rafale_b_croatia = "07 rafale b croatia"
            _08_rafale_b_export = "08 rafale b export"
            _09_rafale_b_india_air_force = "09 rafale b india air force"
            _10_tiger_meet_2009 = "10 tiger meet 2009"

        class Spain(Enum):
            _01_rafale_b_lafayette = "01 rafale b lafayette"
            _02_rafale_b_mt_de_marsan = "02 rafale b mt de marsan"
            _03_rafale_b_qatar = "03 rafale b qatar"
            _04_rafale_b_egypte = "04 rafale b egypte"
            _05_rafale_b_inde = "05 rafale b inde"
            _06_rafale_b_grece = "06 rafale b grece"
            _07_rafale_b_croatia = "07 rafale b croatia"
            _08_rafale_b_export = "08 rafale b export"
            _09_rafale_b_india_air_force = "09 rafale b india air force"
            _10_tiger_meet_2009 = "10 tiger meet 2009"

        class Belarus(Enum):
            _01_rafale_b_lafayette = "01 rafale b lafayette"
            _02_rafale_b_mt_de_marsan = "02 rafale b mt de marsan"
            _03_rafale_b_qatar = "03 rafale b qatar"
            _04_rafale_b_egypte = "04 rafale b egypte"
            _05_rafale_b_inde = "05 rafale b inde"
            _06_rafale_b_grece = "06 rafale b grece"
            _07_rafale_b_croatia = "07 rafale b croatia"
            _08_rafale_b_export = "08 rafale b export"
            _09_rafale_b_india_air_force = "09 rafale b india air force"
            _10_tiger_meet_2009 = "10 tiger meet 2009"

        class Canada(Enum):
            _01_rafale_b_lafayette = "01 rafale b lafayette"
            _02_rafale_b_mt_de_marsan = "02 rafale b mt de marsan"
            _03_rafale_b_qatar = "03 rafale b qatar"
            _04_rafale_b_egypte = "04 rafale b egypte"
            _05_rafale_b_inde = "05 rafale b inde"
            _06_rafale_b_grece = "06 rafale b grece"
            _07_rafale_b_croatia = "07 rafale b croatia"
            _08_rafale_b_export = "08 rafale b export"
            _09_rafale_b_india_air_force = "09 rafale b india air force"
            _10_tiger_meet_2009 = "10 tiger meet 2009"

        class NorthKorea(Enum):
            _01_rafale_b_lafayette = "01 rafale b lafayette"
            _02_rafale_b_mt_de_marsan = "02 rafale b mt de marsan"
            _03_rafale_b_qatar = "03 rafale b qatar"
            _04_rafale_b_egypte = "04 rafale b egypte"
            _05_rafale_b_inde = "05 rafale b inde"
            _06_rafale_b_grece = "06 rafale b grece"
            _07_rafale_b_croatia = "07 rafale b croatia"
            _08_rafale_b_export = "08 rafale b export"
            _09_rafale_b_india_air_force = "09 rafale b india air force"
            _10_tiger_meet_2009 = "10 tiger meet 2009"

        class Ethiopia(Enum):
            _01_rafale_b_lafayette = "01 rafale b lafayette"
            _02_rafale_b_mt_de_marsan = "02 rafale b mt de marsan"
            _03_rafale_b_qatar = "03 rafale b qatar"
            _04_rafale_b_egypte = "04 rafale b egypte"
            _05_rafale_b_inde = "05 rafale b inde"
            _06_rafale_b_grece = "06 rafale b grece"
            _07_rafale_b_croatia = "07 rafale b croatia"
            _08_rafale_b_export = "08 rafale b export"
            _09_rafale_b_india_air_force = "09 rafale b india air force"
            _10_tiger_meet_2009 = "10 tiger meet 2009"

        class Japan(Enum):
            _01_rafale_b_lafayette = "01 rafale b lafayette"
            _02_rafale_b_mt_de_marsan = "02 rafale b mt de marsan"
            _03_rafale_b_qatar = "03 rafale b qatar"
            _04_rafale_b_egypte = "04 rafale b egypte"
            _05_rafale_b_inde = "05 rafale b inde"
            _06_rafale_b_grece = "06 rafale b grece"
            _07_rafale_b_croatia = "07 rafale b croatia"
            _08_rafale_b_export = "08 rafale b export"
            _09_rafale_b_india_air_force = "09 rafale b india air force"
            _10_tiger_meet_2009 = "10 tiger meet 2009"

        class Thailand(Enum):
            _01_rafale_b_lafayette = "01 rafale b lafayette"
            _02_rafale_b_mt_de_marsan = "02 rafale b mt de marsan"
            _03_rafale_b_qatar = "03 rafale b qatar"
            _04_rafale_b_egypte = "04 rafale b egypte"
            _05_rafale_b_inde = "05 rafale b inde"
            _06_rafale_b_grece = "06 rafale b grece"
            _07_rafale_b_croatia = "07 rafale b croatia"
            _08_rafale_b_export = "08 rafale b export"
            _09_rafale_b_india_air_force = "09 rafale b india air force"
            _10_tiger_meet_2009 = "10 tiger meet 2009"

    class Pylon1:
        MICA_IR = (1, Weapons.MICA_IR)
        Smokewinder___red_smk = (1, Weapons.Smokewinder___red_smk)
        Smokewinder___green = (1, Weapons.Smokewinder___green)
        Smokewinder___blue_smk = (1, Weapons.Smokewinder___blue_smk)
        Smokewinder___white = (1, Weapons.Smokewinder___white)
        Smokewinder___yellow = (1, Weapons.Smokewinder___yellow)
        Smokewinder___orange = (1, Weapons.Smokewinder___orange)
        AIM_9M_Sidewinder_IR_AAM = (1, Weapons.AIM_9M_Sidewinder_IR_AAM)
        AIM_9P_Sidewinder_IR_AAM = (1, Weapons.AIM_9P_Sidewinder_IR_AAM)
        R_550_Magic_2 = (1, Weapons.R_550_Magic_2)

    class Pylon2:
        gbu12X3_L = (2, Weapons.gbu12X3_L)
        gbu12X2_L = (2, Weapons.gbu12X2_L)
        AASM_250_L = (2, Weapons.AASM_250_L)
        GBU_49 = (2, Weapons.GBU_49)
        MER_2_MK_82 = (2, Weapons.MER_2_MK_82)
        _3_Mk_82 = (2, Weapons._3_Mk_82)
        GBU12PII = (2, Weapons.GBU12PII)
        _3_Mk_20_Rockeye = (2, Weapons._3_Mk_20_Rockeye)
        mk_84 = (2, Weapons.mk_84)
        gbu24 = (2, Weapons.gbu24)
        LAU_131___7_2_75__rockets_M151__HE_ = (2, Weapons.LAU_131___7_2_75__rockets_M151__HE_)
        LAU3_HE151 = (2, Weapons.LAU3_HE151)
        LAU3_WP156 = (2, Weapons.LAU3_WP156)
        LAU3_HE5 = (2, Weapons.LAU3_HE5)
        SCALP = (2, Weapons.SCALP)
        AS_30L = (2, Weapons.AS_30L)
        AGM_88C_ = (2, Weapons.AGM_88C_)

    class Pylon3:
        GBU_49 = (3, Weapons.GBU_49)
        gbu24 = (3, Weapons.gbu24)
        GBU12PII = (3, Weapons.GBU12PII)
        MER_2_MK_82 = (3, Weapons.MER_2_MK_82)
        _3_Mk_82 = (3, Weapons._3_Mk_82)
        AGM_88C_ = (3, Weapons.AGM_88C_)
        LAU3_HE151 = (3, Weapons.LAU3_HE151)
        LAU3_WP156 = (3, Weapons.LAU3_WP156)
        LAU_131x3_HYDRA_70_M151 = (3, Weapons.LAU_131x3_HYDRA_70_M151)
        AS_30L = (3, Weapons.AS_30L)
        RAF_RPL711 = (3, Weapons.RAF_RPL711)
        RAF_RPL751 = (3, Weapons.RAF_RPL751)
        mk_84 = (3, Weapons.mk_84)

    class Pylon4:
        AIM_9M_Sidewinder_IR_AAM = (4, Weapons.AIM_9M_Sidewinder_IR_AAM)
        AIM_9P_Sidewinder_IR_AAM = (4, Weapons.AIM_9P_Sidewinder_IR_AAM)
        MICA_IR = (4, Weapons.MICA_IR)
        LAU_10___4_ZUNI_MK_71 = (4, Weapons.LAU_10___4_ZUNI_MK_71)
        LAU_61___19_2_75__rockets_MK151_HE = (4, Weapons.LAU_61___19_2_75__rockets_MK151_HE)
        LAU3_HE151 = (4, Weapons.LAU3_HE151)

    class Pylon5:
        GBU12PII = (5, Weapons.GBU12PII)
        mk_84 = (5, Weapons.mk_84)
        RAF_RPL711 = (5, Weapons.RAF_RPL711)
        RAF_RPL751 = (5, Weapons.RAF_RPL751)
        Mercury_LLTV_Pod = (5, Weapons.Mercury_LLTV_Pod)
        SCALP = (5, Weapons.SCALP)
        Exocet = (5, Weapons.Exocet)
        GBU_49 = (5, Weapons.GBU_49)
        MER_2_MK_83 = (5, Weapons.MER_2_MK_83)
        MER_2_MK_82 = (5, Weapons.MER_2_MK_82)

    class Pylon6:
        LAU_10___4_ZUNI_MK_71 = (6, Weapons.LAU_10___4_ZUNI_MK_71)
        LAU_61___19_2_75__rockets_MK151_HE = (6, Weapons.LAU_61___19_2_75__rockets_MK151_HE)
        AIM_9M_Sidewinder_IR_AAM = (6, Weapons.AIM_9M_Sidewinder_IR_AAM)
        AIM_9P_Sidewinder_IR_AAM = (6, Weapons.AIM_9P_Sidewinder_IR_AAM)
        MICA_IR = (6, Weapons.MICA_IR)
        LAU3_HE151 = (6, Weapons.LAU3_HE151)

    class Pylon7:
        AN_AAQ_28_LITENING = (7, Weapons.AN_AAQ_28_LITENING)
        TALIOS_THALES = (7, Weapons.TALIOS_THALES)

    class Pylon8:
        GBU_49 = (8, Weapons.GBU_49)
        gbu24 = (8, Weapons.gbu24)
        GBU12PII = (8, Weapons.GBU12PII)
        MER_2_MK_82 = (8, Weapons.MER_2_MK_82)
        _3_Mk_20_Rockeye = (8, Weapons._3_Mk_20_Rockeye)
        _3_Mk_82 = (8, Weapons._3_Mk_82)
        mk_84 = (8, Weapons.mk_84)
        LAU3_HE151 = (8, Weapons.LAU3_HE151)
        LAU3_WP156 = (8, Weapons.LAU3_WP156)
        LAU_131x3_HYDRA_70_M151 = (8, Weapons.LAU_131x3_HYDRA_70_M151)
        AS_30L = (8, Weapons.AS_30L)
        AGM_88C_ = (8, Weapons.AGM_88C_)
        RAF_RPL711 = (8, Weapons.RAF_RPL711)
        RAF_RPL751 = (8, Weapons.RAF_RPL751)

    class Pylon9:
        gbu12X3_R = (9, Weapons.gbu12X3_R)
        gbu12X2_R = (9, Weapons.gbu12X2_R)
        AASM_250_R = (9, Weapons.AASM_250_R)
        GBU_49 = (9, Weapons.GBU_49)
        gbu24 = (9, Weapons.gbu24)
        MER_2_MK_82 = (9, Weapons.MER_2_MK_82)
        GBU12PII = (9, Weapons.GBU12PII)
        _3_Mk_20_Rockeye = (9, Weapons._3_Mk_20_Rockeye)
        mk_84 = (9, Weapons.mk_84)
        _3_Mk_82 = (9, Weapons._3_Mk_82)
        AGM_88C_ = (9, Weapons.AGM_88C_)
        LAU_131___7_2_75__rockets_M151__HE_ = (9, Weapons.LAU_131___7_2_75__rockets_M151__HE_)
        LAU3_HE151 = (9, Weapons.LAU3_HE151)
        LAU3_WP156 = (9, Weapons.LAU3_WP156)
        LAU3_HE5 = (9, Weapons.LAU3_HE5)
        SCALP = (9, Weapons.SCALP)
        AS_30L = (9, Weapons.AS_30L)

    class Pylon10:
        R_550_Magic_2 = (10, Weapons.R_550_Magic_2)
        AIM_9M_Sidewinder_IR_AAM = (10, Weapons.AIM_9M_Sidewinder_IR_AAM)
        AIM_9P_Sidewinder_IR_AAM = (10, Weapons.AIM_9P_Sidewinder_IR_AAM)
        Smokewinder___red_smk = (10, Weapons.Smokewinder___red_smk)
        Smokewinder___green = (10, Weapons.Smokewinder___green)
        Smokewinder___blue_smk = (10, Weapons.Smokewinder___blue_smk)
        Smokewinder___white = (10, Weapons.Smokewinder___white)
        Smokewinder___yellow = (10, Weapons.Smokewinder___yellow)
        Smokewinder___orange = (10, Weapons.Smokewinder___orange)
        MICA_IR = (10, Weapons.MICA_IR)

    class Pylon11:
        Thales_RBE2 = (11, Weapons.Thales_RBE2)

    pylons = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}

    tasks = [task.CAP, task.Escort, task.FighterSweep, task.GroundAttack, task.CAS, task.AFAC, task.RunwayAttack, task.AntishipStrike, task.SEAD, task.PinpointStrike]
    task_default = task.GroundAttack


