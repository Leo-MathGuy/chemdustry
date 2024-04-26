package jesse;

import jesse.override.ConsumeItemFlammableSelection;
import mindustry.content.Blocks;

public class JesseWtfAreYouTakingAbout {
    public static void load_overrides() {
        Blocks.combustionGenerator.consumers[0] = new ConsumeItemFlammableSelection(0.2f);
        Blocks.steamGenerator.consumers[0] = new ConsumeItemFlammableSelection(0.2f);
    }
}
