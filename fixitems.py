import glob
import json
from pathlib import Path

#intervalLabors.subCategory.greatsword=Balanced
#intervalLabors.subCategory.rapier=Light
#intervalLabors.subCategory.twoHandedAxe=Specialist
#intervalLabors.subCategory.twoHandedMace=Physical
#intervalLabors.subCategory.twoHandedSpear=Technical

def main():
    for flail in glob.iglob(r".\assets\data\items\items\flail1hand*.json"):
        flail = Path(flail)
        print(flail.name)
        with flail.open() as f:
            data = json.load(f)
            data["category"] = "wand"
            data["subCategory"] = "rapier"
            data["tracks"] = [ "flail1hand_basic" ]
            data['modId'] = "expandedItemsShadowSpirit"

        with flail.open("w") as f:
            json.dump(data, f, indent=4)
            
    for flail in glob.iglob(r".\assets\data\items\items\flail2hand*.json"):
        flail = Path(flail)
        print(flail.name)
        with flail.open() as f:
            data = json.load(f)
            data["category"] = "staff"
            data["subCategory"] = "twoHandedMace"
            data["tracks"] = [ "flail2hand_basic" ]
            data['modId'] = "expandedItemsShadowSpirit"

        with flail.open("w") as f:
            json.dump(data, f, indent=4)


if __name__ == "__main__":
    main()
