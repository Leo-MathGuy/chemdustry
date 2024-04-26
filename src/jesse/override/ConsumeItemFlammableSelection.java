package jesse.override;

import arc.struct.Seq;
import mindustry.type.Item;
import mindustry.world.consumers.ConsumeItemFlammable;

public class ConsumeItemFlammableSelection extends ConsumeItemFlammable {
    Seq<String> items = new Seq<String>(new String[] { "coal", "pyratite", "spore-pod", "blast-compound" });

    public ConsumeItemFlammableSelection(float minFlammability) {
        this.minFlammability = minFlammability;
        filter = (Item item) -> {
            var flamCond = item.flammability >= this.minFlammability;

            return flamCond && items.contains(item.name);
        };
    }
}