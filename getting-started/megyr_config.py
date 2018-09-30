import megyr

def main():
    megyr.run({
        "input": {
            "mesa_configs": ["inlist.mustache"],
            "gyre_config": "gyre.in.mustache"
        },
        "output": {
            "mesa_profile_summary_file": "mesa_profile_attributes.csv",
            "gyre_oscillations_ad_summary_file": "oscillations_ad.csv"
        },
        "stages": {
            "mesa_params": {
                "initial_mass": [1, 1.1, 1.5]
            },
            "gyre_params": calc_gyre_params
        }
    })

def calc_gyre_params(mesa_params, mesa_data):
    return {
        "l": [0, 1, 2],

        # Look at all the profiles that are at least 0.0001 Gyr in age
        "profile": mesa_data[mesa_data["star_age"] > 100000]["profile"]
    }

if __name__ == "__main__":
    main()
